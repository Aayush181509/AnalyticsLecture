"""Check D01 retail settings/source invariants and private hand-designed fixtures.

Read-only: no prepared CSV, rewritten metadata, Tableau execution or publication.
Run in the audit environment from data/README.md (xlrd required).
"""

from collections import defaultdict
from datetime import date
from decimal import Decimal
import hashlib
import json
from pathlib import Path

import xlrd

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "data/metadata/superstore/retail-v1/contract.json"
FIXTURES = ROOT / "instructor/source-audit/retail-contract-fixtures.json"


def ratio(numerator, denominator):
    return numerator / denominator if denominator != 0 else None


def metrics(rows):
    sales = sum((Decimal(r["sales"]) for r in rows), Decimal(0))
    profit = sum((Decimal(r["profit"]) for r in rows), Decimal(0))
    orders = {r["order_id"] for r in rows}
    returned = {r["order_id"] for r in rows if r["returned_order_flag"] == 1}
    return {"lines": len(rows), "orders": len(orders), "sales": sales, "profit": profit,
            "units": sum(r["quantity"] for r in rows), "aov": ratio(sales, len(orders)),
            "profit_ratio": ratio(profit, sales), "returned_orders": len(returned),
            "return_list_share": ratio(Decimal(len(returned)), len(orders))}


def check_expected(actual, expected):
    for key, value in expected.items():
        target = Decimal(value) if isinstance(value, str) else value
        assert actual[key] == target, (key, actual[key], target)


def conflicts(rows):
    customers = defaultdict(set)
    for row in rows:
        customers[row["order_id"]].add(row["customer_id"])
    return sorted(key for key, values in customers.items() if len(values) > 1)


def previous_month(value, months):
    month_index = value.year * 12 + value.month - 1 - months
    return date(month_index // 12, month_index % 12 + 1, 1)


def fixture_checks(settings):
    fixtures = json.loads(FIXTURES.read_text())
    assert fixtures["synthetic"] is True and fixtures["contract_id"] == settings["contract_id"]
    rows = fixtures["core_rows"]
    for name in ("core", "zero_sales", "empty"):
        actual = metrics([] if name == "empty" else fixtures[f"{name}_rows"])
        check_expected(actual, fixtures[f"{name}_expected"])
    wrong_mean = sum(Decimal(r["profit"]) / Decimal(r["sales"]) for r in rows) / len(rows)
    traps = fixtures["trap_expectations"]
    assert wrong_mean == Decimal(traps["mean_line_profit_ratio"])
    assert wrong_mean != metrics(rows)["profit_ratio"]
    categories = {r["category"] for r in rows}
    category_order_sum = sum(len({r["order_id"] for r in rows if r["category"] == category}) for category in categories)
    assert category_order_sum == traps["sum_category_distinct_orders"] > metrics(rows)["orders"]
    assert sum(r["returned_order_flag"] for r in rows) == traps["sum_line_return_flags"] > metrics(rows)["returned_orders"]
    customer_rows = fixtures["customer_rows"]
    bad_orders = conflicts(customer_rows)
    assert bad_orders == fixtures["customer_expected"]["conflicting_orders"]
    eligible = [r for r in customer_rows if r["order_id"] not in bad_orders]
    excluded = [r for r in customer_rows if r["order_id"] in bad_orders]
    for label, population in (("primary", customer_rows), ("eligible", eligible), ("excluded", excluded)):
        expected = fixtures["customer_expected"]
        assert len(population) == expected[f"{label}_lines"]
        assert sum(Decimal(r["sales"]) for r in population) == Decimal(expected[f"{label}_sales"])
        if f"{label}_orders" in expected:
            assert len({r["order_id"] for r in population}) == expected[f"{label}_orders"]
    start, end = (date.fromisoformat(settings["scope"][key]) for key in ("start_inclusive", "end_exclusive"))
    scoped = [r for r in fixtures["date_rows"] if start <= date.fromisoformat(r["order_date"]) < end]
    assert [r["row_id"] for r in scoped] == fixtures["date_expected"]["included_row_ids"]
    assert [(date.fromisoformat(r["ship_date"]) - date.fromisoformat(r["order_date"])).days for r in scoped] == fixtures["date_expected"]["dispatch_days"]
    series = {date.fromisoformat(r["month"]): Decimal(r["sales"]) for r in fixtures["monthly_rows"]}
    for expected in fixtures["monthly_expectations"]:
        current = date.fromisoformat(expected["month"])
        prior = series.get(previous_month(current, expected["months_back"]))
        actual = None if prior is None else ratio(series[current] - prior, prior)
        target = None if expected["growth"] is None else Decimal(expected["growth"])
        assert actual == target, expected
    covered = fixtures["covered_month_fixture"]
    covered_sales = {date.fromisoformat(key): Decimal(0) for key in covered["covered_months"]}
    for row in covered["selected_line_sales"]:
        covered_sales[date.fromisoformat(row["month"])] += Decimal(row["sales"])
    for key, value in covered["expected_month_sales"].items():
        assert covered_sales[date.fromisoformat(key)] == Decimal(value)
    for key, expected in covered["expected_growth"].items():
        current = date.fromisoformat(key)
        prior = covered_sales.get(previous_month(current, 1))
        actual = None if prior is None else ratio(covered_sales[current] - prior, prior)
        assert actual == (None if expected is None else Decimal(expected))
    assert date.fromisoformat(covered["unavailable_outside_coverage"]) not in covered_sales
    print("PASS synthetic fixtures: grain, weighted ratios, empty/zero, category overlap, return flags, customer scope, date boundaries and calendar comparators.")


def source_checks(settings):
    record = settings["source"]
    source = ROOT / record["path"]
    assert source.stat().st_size == record["bytes"]
    assert hashlib.sha256(source.read_bytes()).hexdigest() == record["sha256"]
    manifest = json.loads((ROOT / record["manifest"]).read_text())
    acquired = next(r for r in manifest["sources"] if r["source_id"] == record["source_id"])
    assert all(record[key] == acquired[key] for key in ("path", "sha256", "bytes"))
    book = xlrd.open_workbook(source)
    assert set(book.sheet_names()) == set(record["sheets"])
    tables = {}
    profiles = json.loads((ROOT / "data/metadata/catalog-audit-2026-10-12/profiles.json").read_text())
    observed = next(r for r in profiles["sources"] if r["source_id"] == record["source_id"])
    for name, expected_rows in record["sheets"].items():
        sheet = book.sheet_by_name(name)
        headers = sheet.row_values(0)
        assert headers == [field["name"] for field in observed["tables"][name]["fields"]]
        assert sheet.nrows - 1 == expected_rows
        tables[name] = [dict(zip(headers, sheet.row_values(i))) for i in range(1, sheet.nrows)]
    raw = tables["Orders"]
    for row in raw:
        for field in ("Order Date", "Ship Date"):
            parsed = xlrd.xldate_as_datetime(row[field], book.datemode)
            assert parsed.time().isoformat() == "00:00:00"
            row[field] = parsed.date()
    columns = settings["prepared"]["columns"]
    assert len(columns) == 22 and len({r["name"] for r in columns}) == 22
    source_fields = {r["source"] for r in columns if "source" in r}
    assert source_fields | set(settings["prepared"]["omitted_source_fields"]) == set(raw[0])
    assert len(source_fields) == 17
    assert settings["currency"]["iso_code"] is None and settings["publication"]["approved"] is False
    assert settings["tableau_verified"] is False
    assert len({r["Row ID"] for r in raw}) == len(raw)
    required = source_fields
    for row in raw:
        assert all(row[key] is not None and row[key] != "" for key in required)
        assert all(not isinstance(row[key], str) or row[key].strip() for key in required)
        assert row["Row ID"] == int(row["Row ID"]) and row["Row ID"] > 0
        assert row["Quantity"] == int(row["Quantity"]) and row["Quantity"] > 0
        assert row["Ship Date"] >= row["Order Date"]
        for key in ("Sales", "Profit", "Discount"):
            assert Decimal(str(row[key])).is_finite()
        assert row["Sales"] >= 0 and 0 <= row["Discount"] <= 1
    grouped = defaultdict(list)
    for row in raw:
        grouped[row["Order ID"]].append(row)
    for order_rows in grouped.values():
        for field in settings["order_stable_fields"]:
            assert len({r[field] for r in order_rows}) == 1
    bad_orders = sorted(key for key, group in grouped.items() if len({r["Customer ID"] for r in group}) > 1)
    assert bad_orders == settings["customer_policy"]["expected_conflicting_orders_all_source"]
    returned = [r["Order ID"] for r in tables["Returns"]]
    assert len(returned) == len(set(returned)) and set(returned) <= set(grouped)
    assert all(r["Order ID"] and r["Returned"] == "Yes" for r in tables["Returns"])
    regions = [r["Region"] for r in tables["People"]]
    assert len(regions) == len(set(regions)) and set(r["Region"] for r in raw) <= set(regions)
    start, end = (date.fromisoformat(settings["scope"][key]) for key in ("start_inclusive", "end_exclusive"))
    scoped = [r for r in raw if start <= r["Order Date"] < end]
    eligible = [r for r in scoped if r["Order ID"] not in bad_orders]
    excluded = [r for r in scoped if r["Order ID"] in bad_orders]
    assert len(scoped) == 6815 and len({r["Order ID"] for r in scoped}) == 3388
    assert any(r["Ship Date"] >= end for r in scoped)
    assert len(eligible) == 6811 and len(excluded) == 4
    assert len({r["Order ID"] for r in eligible}) == 3387
    assert {r["Order ID"] for r in excluded} == {"CA-2025-121465"}
    expected_months = {(year, month) for year in range(2023, 2026) for month in range(1, 13)}
    assert {(r["Order Date"].year, r["Order Date"].month) for r in scoped} == expected_months
    assert {r["Row ID"] for r in eligible}.isdisjoint(r["Row ID"] for r in excluded)
    for field in ("Sales", "Profit", "Quantity"):
        original = sum(Decimal(str(r[field])) for r in scoped)
        bridge = sum(Decimal(str(r[field])) for r in eligible) + sum(Decimal(str(r[field])) for r in excluded)
        assert original == bridge
    controls = json.loads((ROOT / "instructor/source-audit/catalog-2026-10-12-controls.json").read_text())
    expected = controls["sources"]["eu-superstore"]["proposed_complete_years_2023_2025"]
    assert sum(Decimal(str(r["Sales"])) for r in scoped) == Decimal(expected["reported_sales"])
    assert sum(Decimal(str(r["Profit"])) for r in scoped) == Decimal(expected["reported_profit"])
    assert len({r["Order ID"] for r in scoped if r["Order ID"] in returned}) == expected["returned_orders_flagged"]
    for row in scoped:
        for field in ("Sales", "Profit", "Discount"):
            assert Decimal(repr(row[field])) == Decimal(str(row[field]))
    print("PASS exact XLS/hash/schema and contract scope: 6815 lines, 3388 orders, 36 months; customer-eligible 6811 lines/3387 orders; private controls and exception bridge reconcile.")


def main():
    settings = json.loads(CONTRACT.read_text())
    assert settings["contract_id"] == "superstore-retail-v1"
    freeze_path = CONTRACT.parent / "freeze.json"
    if freeze_path.exists():
        freeze = json.loads(freeze_path.read_text())
        assert freeze["contract_id"] == settings["contract_id"]
        assert settings["status"] == "frozen_local_development"
        for record in freeze["files"]:
            path = ROOT / record["path"]
            assert hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"], path
        print("PASS frozen contract/fixture/checker hashes.")
    fixture_checks(settings)
    source_checks(settings)
    print("D01 checks complete: read-only; no prepared release or Tableau validation implied.")


if __name__ == "__main__":
    main()
