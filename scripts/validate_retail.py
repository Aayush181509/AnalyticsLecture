"""Independently validate saved retail-v1 CSV and write private numeric references.

Source reader: pandas.read_excel; prepared reader: csv.DictReader + Decimal.
Does not import/run preparation or frozen checker helpers, recalculate Excel,
invoke Tableau, change prepared/frozen inputs, or approve publication.
Existing reference/report bytes must agree; different outputs are never replaced.
"""

from collections import defaultdict
import csv
from datetime import date
from decimal import Decimal, ROUND_HALF_UP, getcontext
import hashlib
import io
import json
from pathlib import Path
import platform
import re
import statistics

import pandas as pd
import xlrd


ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "data/metadata/superstore/retail-v1"
PREPARED = ROOT / "data/prepared/superstore/retail-v1"
PRIVATE = ROOT / "instructor/solutions/superstore/retail-v1"
ANSWER = PRIVATE / "reference_answers.json"
REPORT = PRIVATE / "numerical_validation.json"


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def digest(content):
    return hashlib.sha256(content).hexdigest()


def encode(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True,
                       allow_nan=False) + "\n").encode("utf-8")


def serialize(value):
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: serialize(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(v) for v in value]
    return value


def ratio(numerator, denominator):
    return numerator / Decimal(denominator) if denominator else None


def kpis(rows, customer_scope=False):
    """Numerators and denominators remain exposed; Decimal ratios use precision60."""
    orders = {r["order_id"] for r in rows}
    returned = {r["order_id"] for r in rows if r["returned_order_flag"]}
    sales = sum((r["sales"] for r in rows), Decimal(0))
    profit = sum((r["profit"] for r in rows), Decimal(0))
    intervals = {}
    for r in rows:
        previous = intervals.setdefault(r["order_id"], r["order_to_ship_days"])
        require(previous == r["order_to_ship_days"], "Order dispatch dates disagree")
    result = {
        "lines": len(rows), "orders": len(orders), "reported_sales": sales,
        "reported_profit": profit, "units": sum(r["quantity"] for r in rows),
        "average_order_value": ratio(sales, len(orders)),
        "source_reported_profit_ratio": ratio(profit, sales),
        "orders_listed_in_returns": len(returned),
        "share_of_orders_listed_in_returns": ratio(Decimal(len(returned)), len(orders)),
        "customer_ids_observed_diagnostic_only": len({r["customer_id"] for r in rows}),
        "customer_conflict_lines": sum(r["customer_order_conflict"] for r in rows),
        "display_state": "rows_present" if rows else "no_rows_in_selection",
        "order_to_ship_days": {
            "population": "one interval per represented Order ID; dispatch, not delivery",
            "orders": len(intervals), "total_days": sum(intervals.values()),
            "mean_days": ratio(Decimal(sum(intervals.values())), len(intervals)),
            "median_days": statistics.median(map(Decimal, intervals.values())) if intervals else None,
        },
    }
    if customer_scope:
        require(all(r["customer_analysis_eligible"] == 1 for r in rows), "Ineligible customer scope")
        result["eligible_distinct_customer_ids"] = len({r["customer_id"] for r in rows})
    return result


def groups(rows, field):
    result = defaultdict(list)
    for r in rows:
        result[r[field]].append(r)
    return dict(sorted(result.items()))


def shifted_month(month, count):
    return (pd.Timestamp(month) - pd.DateOffset(months=count)).date()


def growth(current, prior, selection_has_rows=True):
    if not selection_has_rows:
        return {"value": None, "status": "no_rows_in_selection"}
    if prior is None:
        return {"value": None, "status": "unavailable_calendar_comparator"}
    if prior == 0:
        return {"value": None, "status": "zero_prior_sales"}
    return {"value": (current - prior) / prior, "status": "available"}


def month_series(rows, coverage, customer_scope=False):
    by_month = groups(rows, "order_month")
    totals = {m: sum((r["sales"] for r in by_month.get(m, [])), Decimal(0)) for m in coverage}
    result = []
    for m in coverage:
        selected = by_month.get(m, [])
        result.append({
            "month": m, "source_calendar_covered": True,
            "selected_lines_present": bool(selected), "selection_has_any_rows": bool(rows),
            "kpis": kpis(selected, customer_scope),
            "sales_growth_mom": growth(totals[m], totals.get(shifted_month(m, 1)), bool(rows)),
            "sales_growth_yoy": growth(totals[m], totals.get(shifted_month(m, 12)), bool(rows)),
        })
    return result


def scope_answers(rows, coverage, customer_scope=False):
    return {
        "overall": kpis(rows, customer_scope),
        "monthly": month_series(rows, coverage, customer_scope),
        "by_dimension": {field: {label: {
            "kpis": kpis(part, customer_scope),
            "aov_label": ("Selected-line Sales per participating order" if field == "category"
                          else "Average order value"),
            "monthly": month_series(part, coverage, customer_scope),
        } for label, part in groups(rows, field).items()}
            for field in ("segment", "region", "category")},
    }


def main():
    getcontext().prec = 60
    fingerprints = {}

    def read(path):
        p = path if isinstance(path, Path) else ROOT / path
        require(ROOT in p.resolve().parents, "Input path must remain inside workspace")
        content = p.read_bytes()
        fingerprints[str(p.relative_to(ROOT))] = digest(content)
        return content

    def load(path):
        return json.loads(read(path))

    settings = load(META / "contract.json")
    freeze = load(META / "freeze.json")
    require(settings["status"] == "frozen_local_development", "Contract must be frozen")
    require(settings["contract_id"] == freeze["contract_id"] == "superstore-retail-v1", "Contract ID")
    frozen = {r["path"]: r["sha256"] for r in freeze["files"]}
    require(len(frozen) == len(freeze["files"]) == 7, "Expected seven distinct frozen files")
    for path, expected in frozen.items():
        require(digest(read(path)) == expected, f"Frozen file changed: {path}")
    manifest = load(PREPARED / "manifest.json")
    require(manifest["contract_id"] == settings["contract_id"], "Prepared contract ID")
    require(manifest["frozen_contract_files_sha256"] == frozen, "Prepared freeze file hashes differ")
    require(manifest["freeze_manifest"]["path"] == str((META / "freeze.json").relative_to(ROOT)), "Freeze path")
    require(manifest["freeze_manifest"]["sha256"] == fingerprints[manifest["freeze_manifest"]["path"]], "Freeze manifest hash")
    for key in ("scope", "currency", "source"):
        require(manifest[key] == settings[key], f"Prepared manifest {key} contradicts contract")
    require(manifest["schema"] == settings["prepared"]["columns"], "Prepared schema differs")
    require(manifest["publication_approved"] is False and manifest["tableau_verified"] is False
            and manifest["local_development_only"] is True, "D02 release boundary changed")
    prep_script = manifest["preparation_script"]
    require(digest(read(prep_script["path"])) == prep_script["sha256"], "Preparation script hash differs")
    output_records = {r["path"]: r for r in manifest["outputs"]}
    required_outputs = {
        str((PREPARED / "order_lines.csv").relative_to(ROOT)),
        str((PREPARED / "preparation_report.json").relative_to(ROOT)),
        str((PRIVATE / "preparation_exceptions.json").relative_to(ROOT)),
    }
    require(len(output_records) == len(manifest["outputs"]) == 3 and set(output_records) == required_outputs,
            "D02 manifest must identify its three exact outputs")
    for path, record in output_records.items():
        content = read(path)
        require(len(content) == record["bytes"] and digest(content) == record["sha256"], f"D02 output changed: {path}")
    source = settings["source"]
    require(source["sha256"] == freeze["source_sha256"], "Source/freeze hash disagrees")
    raw_content = read(source["path"])
    require(len(raw_content) == source["bytes"] and digest(raw_content) == source["sha256"], "Raw source integrity")
    audit_manifest = load(source["manifest"])
    source_record = next(r for r in audit_manifest["sources"] if r["source_id"] == source["source_id"])
    require(all(source_record[k] == source[k] for k in ("path", "bytes", "sha256")), "Audit source differs")
    profiles = load(ROOT / "data/metadata/catalog-audit-2026-10-12/profiles.json")
    profile = next(r for r in profiles["sources"] if r["source_id"] == source["source_id"])

    # Independent source route: pandas Excel parsing, no preparation/checker imports.
    tables = pd.read_excel(io.BytesIO(raw_content), sheet_name=None, engine="xlrd")
    require(set(tables) == set(source["sheets"]), "Source sheets changed")
    for name, frame in tables.items():
        require(len(frame) == source["sheets"][name], f"Source sheet size: {name}")
        require(list(frame.columns) == [f["name"] for f in profile["tables"][name]["fields"]], f"Source headers: {name}")
    raw = tables["Orders"].to_dict(orient="records")
    customer_sets = defaultdict(set)
    for row in raw:
        customer_sets[row["Order ID"]].add(row["Customer ID"])
    conflicts = sorted(order for order, customers in customer_sets.items() if len(customers) > 1)
    require(conflicts == settings["customer_policy"]["expected_conflicting_orders_all_source"], "Raw conflicts differ")
    returns = tables["Returns"]
    require(returns["Order ID"].notna().all() and returns["Order ID"].is_unique
            and returns["Returned"].eq("Yes").all(), "Returns membership key/value")
    returned = set(returns["Order ID"])
    require(returned <= set(customer_sets), "Returns contains unknown orders")
    people = tables["People"]
    require(people["Region"].notna().all() and people["Region"].is_unique
            and set(tables["Orders"]["Region"]) <= set(people["Region"]), "People cardinality/coverage")
    columns = settings["prepared"]["columns"]
    expected_all = []
    for original in raw:
        projected = {}
        for column in columns:
            if "source" not in column:
                continue
            value = original[column["source"]]
            require(pd.notna(value), f"Missing source {column['source']}")
            kind = column["type"]
            if kind == "date":
                moment = pd.Timestamp(value)
                require(moment == moment.normalize(), "Source timestamp has nonmidnight time")
                value = moment.date()
            elif kind == "integer":
                require(value == int(value), "Noninteger source identifier/count")
                value = int(value)
            elif kind == "decimal":
                value = Decimal(str(value))
                require(value.is_finite(), "Nonfinite source amount")
            else:
                require(isinstance(value, str) and value.strip(), "Nontext/blank source dimension")
            projected[column["name"]] = value
        require(projected["row_id"] > 0 and projected["quantity"] > 0, "Nonpositive row ID/quantity")
        require(projected["sales"] >= 0 and Decimal(0) <= projected["discount"] <= 1, "Sales/discount domain")
        delta = (projected["ship_date"] - projected["order_date"]).days
        require(delta >= 0, "Ship date precedes order")
        conflict = int(projected["order_id"] in conflicts)
        projected.update(customer_order_conflict=conflict, customer_analysis_eligible=1-conflict,
                         returned_order_flag=int(projected["order_id"] in returned),
                         order_to_ship_days=delta, order_month=projected["order_date"].replace(day=1))
        expected_all.append(projected)
    require(len({r["row_id"] for r in expected_all}) == len(expected_all), "Raw line key is not unique")
    source_to_prepared = {c["source"]: c["name"] for c in columns if "source" in c}
    for order, part in groups(expected_all, "order_id").items():
        for field in settings["order_stable_fields"]:
            require(len({r[source_to_prepared[field]] for r in part}) == 1, f"Unstable {order}/{field}")
    start = date.fromisoformat(settings["scope"]["start_inclusive"])
    end = date.fromisoformat(settings["scope"]["end_exclusive"])
    expected = sorted((r for r in expected_all if start <= r["order_date"] < end), key=lambda r: r["row_id"])
    outside = [r for r in expected_all if not start <= r["order_date"] < end]

    content = read(PREPARED / "order_lines.csv")
    require(b"\r" not in content and not content.startswith(b"\xef\xbb\xbf"), "CSV LF/UTF-8 contract")
    reader = csv.DictReader(io.StringIO(content.decode("utf-8"), newline=""))
    names = [c["name"] for c in columns]
    require(reader.fieldnames == names and len(names) == 22, "Saved CSV ordered schema")
    saved = []
    for text_row in reader:
        require(set(text_row) == set(names) and all(v is not None and v != "" for v in text_row.values()), "CSV row width/null")
        typed = {}
        for column in columns:
            name, kind = column["name"], column["type"]
            text = text_row[name]
            if kind in ("integer", "integer_flag"):
                value = int(text)
                require(str(value) == text, "Noncanonical saved integer")
                if kind == "integer_flag":
                    require(value in (0, 1), "Saved flag outside domain")
            elif kind == "date":
                value = date.fromisoformat(text)
                require(value.isoformat() == text, "Noncanonical saved date")
            elif kind == "decimal":
                value = Decimal(text)
                require(value.is_finite(), "Nonfinite saved decimal")
            else:
                require(bool(text.strip()), "Blank saved dimension")
                value = text
            typed[name] = value
        saved.append(typed)
    require(len(saved) == len(expected) == manifest["rows"], "Saved scope length differs")
    checked = 0
    for actual, wanted in zip(saved, expected):
        for name in names:
            require(actual[name] == wanted[name], f"Saved source mapping differs at row {wanted['row_id']}/{name}")
            checked += 1
    require(len({r["row_id"] for r in saved}) == len(saved), "Saved line-key duplicate")
    require([r["row_id"] for r in saved] == sorted(r["row_id"] for r in saved), "Saved row ordering")

    eligible = [r for r in saved if r["customer_analysis_eligible"]]
    excluded = [r for r in saved if not r["customer_analysis_eligible"]]
    populations = {"all_raw": expected_all, "primary_scope": saved, "outside_date_scope": outside,
                   "customer_eligible": eligible, "customer_conflict_excluded_from_customer_view": excluded}
    population_kpis = {name: kpis(rows, name == "customer_eligible") for name, rows in populations.items()}
    for whole, parts in ((expected_all, (saved, outside)), (saved, (eligible, excluded))):
        whole_ids = {r["row_id"] for r in whole}
        ids = [r["row_id"] for part in parts for r in part]
        require(len(ids) == len(set(ids)) == len(whole) and set(ids) == whole_ids, "Population line partition")
        for field in ("sales", "profit", "quantity"):
            require(sum((r[field] for r in whole), Decimal(0)) ==
                    sum((r[field] for part in parts for r in part), Decimal(0)), f"Population {field} bridge")
    prep_exceptions = load(PRIVATE / "preparation_exceptions.json")
    for name, reference in prep_exceptions["populations"].items():
        actual = population_kpis[name]
        for old, new in (("lines", "lines"), ("orders", "orders"), ("customer_ids", "customer_ids_observed_diagnostic_only"),
                         ("quantity", "units"), ("sales", "reported_sales"), ("profit", "reported_profit")):
            target = Decimal(reference[old]) if isinstance(reference[old], str) else reference[old]
            require(actual[new] == target, f"D02 private population mismatch: {name}/{old}")
    controls = load(ROOT / "instructor/source-audit/catalog-2026-10-12-controls.json")
    for label, rows in (("all_source_rows", expected_all), ("proposed_complete_years_2023_2025", saved)):
        control = controls["sources"]["eu-superstore"][label]
        actual = kpis(rows)
        for old, new in (("rows", "lines"), ("orders", "orders"), ("quantity", "units"),
                         ("returned_orders_flagged", "orders_listed_in_returns"),
                         ("reported_sales", "reported_sales"), ("reported_profit", "reported_profit")):
            require(actual[new] == (Decimal(control[old]) if isinstance(control[old], str) else control[old]), f"S01 control {label}/{old}")
        for segment, part in groups(rows, "segment").items():
            seg = control["segments"][segment]
            values = kpis(part)
            require(values["lines"] == seg["rows"] and values["orders"] == seg["orders"], "S01 Segment counts")
            require(values["reported_sales"] == Decimal(seg["reported_sales"]) and
                    values["reported_profit"] == Decimal(seg["reported_profit"]), "S01 Segment sums")

    coverage = [date(year, month, 1) for year in range(start.year, end.year) for month in range(1, 13)]
    require(sorted({r["order_month"] for r in saved}) == coverage and len(coverage) == 36, "Calendar coverage")
    main_kpis = kpis(saved)
    partition_checks = {}
    for field in ("segment", "region", "category", "order_month"):
        parts = list(groups(saved, field).values())
        values = [kpis(p) for p in parts]
        for key in ("lines", "units", "reported_sales", "reported_profit"):
            require(sum((v[key] for v in values), Decimal(0)) == main_kpis[key], f"Grouped {field}/{key}")
        total_orders = sum(v["orders"] for v in values)
        if field != "category":
            require(total_orders == main_kpis["orders"], f"Order partition {field}")
            require(sum(v["orders_listed_in_returns"] for v in values) == main_kpis["orders_listed_in_returns"], f"Returned-order partition {field}")
            require(ratio(sum((v["reported_sales"] for v in values), Decimal(0)), total_orders) == main_kpis["average_order_value"], "Order-weighted AOV")
        require(ratio(sum((v["reported_profit"] for v in values), Decimal(0)),
                      sum((v["reported_sales"] for v in values), Decimal(0))) == main_kpis["source_reported_profit_ratio"], "Sales-weighted profit ratio")
        partition_checks[field] = {"groups": len(parts), "additive_measures_reconcile": True,
            "sum_group_distinct_orders": total_orders, "company_distinct_orders": main_kpis["orders"],
            "distinct_orders_additive": field != "category", "overlap_excess": total_orders-main_kpis["orders"]}
    require(partition_checks["category"]["overlap_excess"] > 0, "Category overlap absent")

    # Validate an actual source hand check already documented privately, no hardcoded money answers.
    hand_path = ROOT / "instructor/source-audit/retail-hand-check.md"
    hand = read(hand_path).decode("utf-8")
    matches = re.findall(r"^\| (\d+) \| (\d+) \| ([A-Z]{2}-\d{4}-\d+) \| ([^|]+) \| ([^|]+) \|$", hand, re.M)
    require(len(matches) == 2, "Expected private two-line source hand fixture")
    fixture_rows = []
    for excel_row, row_id, order_id, sales, profit in matches:
        row = next(r for r in saved if r["row_id"] == int(row_id))
        require(int(excel_row) == int(row_id)+1 and row["order_id"] == order_id, "Hand fixture coordinates/order")
        require(row["sales"] == Decimal(sales.strip()) and row["profit"] == Decimal(profit.strip()), "Hand fixture cell values")
        fixture_rows.append(row)
    hand_sales = re.search(r"Sales = [^\n]+\n\s*= ([^\n]+)", hand)
    hand_profit = re.search(r"Profit = [^\n]+\n\s*= ([^\n]+)", hand)
    require(hand_sales is not None and hand_profit is not None, "Hand arithmetic totals absent")
    fixture_kpis = kpis(fixture_rows)
    require(fixture_kpis["orders"] == 1 and fixture_kpis["reported_sales"] == Decimal(hand_sales[1])
            and fixture_kpis["reported_profit"] == Decimal(hand_profit[1]), "Hand arithmetic did not reconcile")

    fixtures = load(ROOT / "instructor/source-audit/retail-contract-fixtures.json")
    for expected_growth in fixtures["monthly_expectations"]:
        monthly = {date.fromisoformat(r["month"]): Decimal(r["sales"]) for r in fixtures["monthly_rows"]}
        current = date.fromisoformat(expected_growth["month"])
        actual = growth(monthly[current], monthly.get(shifted_month(current, expected_growth["months_back"])))
        target = None if expected_growth["growth"] is None else Decimal(expected_growth["growth"])
        require(actual["value"] == target, "Calendar fixture failed")
    covered = fixtures["covered_month_fixture"]
    calendar = {date.fromisoformat(m): Decimal(0) for m in covered["covered_months"]}
    for row in covered["selected_line_sales"]:
        calendar[date.fromisoformat(row["month"])] += Decimal(row["sales"])
    for month, expected_sales in covered["expected_month_sales"].items():
        require(calendar[date.fromisoformat(month)] == Decimal(expected_sales), "Covered no-lines sum")
    for month, expected_growth in covered["expected_growth"].items():
        current = date.fromisoformat(month)
        require(growth(calendar[current], calendar.get(shifted_month(current, 1)))["value"] ==
                (None if expected_growth is None else Decimal(expected_growth)), "Covered no-lines growth")
    require(date.fromisoformat(covered["unavailable_outside_coverage"]) not in calendar, "Outside coverage filled")
    require(all(growth(Decimal(0), prior, False)["value"] is None for prior in (None, Decimal(0), Decimal(1))), "Empty scope growth")
    require(Decimal("1.005").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) == Decimal("1.01")
            and Decimal("-1.005").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) == Decimal("-1.01"), "Display rounding sanity")

    prep_report = load(PREPARED / "preparation_report.json")
    included_ids = sorted(r["row_id"] for r in saved)
    outside_ids = sorted(r["row_id"] for r in outside)
    crossing_ids = sorted(r["row_id"] for r in saved if r["ship_date"] >= end)
    require(prep_report["included_source_row_ids"] == included_ids and prep_report["excluded_source_row_ids"] == outside_ids, "D02 row-ID partition record")
    require(prep_report["ship_dates_after_scope_end_retained_row_ids"] == crossing_ids, "D02 crossing ship record")
    require(manifest["distinct_orders"] == main_kpis["orders"] and manifest["order_month_count"] == len(coverage), "Manifest counts")
    require(manifest["order_date_min"] == min(r["order_date"] for r in saved).isoformat()
            and manifest["order_date_max"] == max(r["order_date"] for r in saved).isoformat(), "Manifest dates")
    script = Path(__file__).resolve()
    validator_hash = digest(read(script))
    evidence = {"contract_id": settings["contract_id"], "version": manifest["version"],
        "source_sha256": source["sha256"], "csv_sha256": digest(content),
        "prepared_manifest_sha256": fingerprints[str((PREPARED / "manifest.json").relative_to(ROOT))],
        "freeze_manifest_sha256": fingerprints[str((META / "freeze.json").relative_to(ROOT))],
        "validator": {"path": str(script.relative_to(ROOT)), "sha256": validator_hash},
        "runtime": {"python": platform.python_version(), "pandas": pd.__version__, "xlrd": xlrd.__version__, "decimal_precision": 60},
        "publication_approved": False, "tableau_verified": False, "numeric_validation_only": True,
        "currency_label": settings["currency"]["label"], "currency_iso_code": None}
    answers = {**evidence,
        "purpose": "Private exact prepared-version numeric references; no Tableau comparison or learner release",
        "semantics": {"sales_profit": "Source-reported values, no accounting/currency inference or extra discount/refunds",
            "returns": "Unique represented orders listed in the whole-file Returns table; no event timing or completeness claim",
            "customer_metrics": "R09 only in consistently eligible-filtered scope; other customer-ID counts are diagnostics",
            "ratios": "Numerators/denominators exact; nonterminating Decimal ratios rounded at precision60, not exact rational expansions",
            "growth": "Calendar comparators and all-source coverage; prior unavailable/zero or wholly empty selection gives null",
            "category_aov": "Selected-line Sales per participating order; full order baskets not implied",
            "display_rounding": "Monetary/AOV two decimals ROUND_HALF_UP; percent one decimal; applied only for presentation"},
        "population_bridges": population_kpis,
        "primary_scope": scope_answers(saved, coverage),
        "customer_eligible_scope": scope_answers(eligible, coverage, True),
        "overlap_and_partition_checks": partition_checks,
        "source_hand_check": {"path": str(hand_path.relative_to(ROOT)), "sha256": fingerprints[str(hand_path.relative_to(ROOT))],
            "row_ids": [r["row_id"] for r in fixture_rows], "kpis": fixture_kpis, "matched": True},
        "debugging_diagnostics": {
            "line_count_is_not_order_count": len(saved) != main_kpis["orders"],
            "mean_line_profit_ratio": sum((r["profit"]/r["sales"] for r in saved), Decimal(0))/len(saved),
            "proper_profit_ratio": main_kpis["source_reported_profit_ratio"],
            "sum_line_return_flags": sum(r["returned_order_flag"] for r in saved),
            "proper_distinct_returned_orders": main_kpis["orders_listed_in_returns"]}}
    answer_bytes = encode(serialize(answers))
    report = {**evidence, "status": "PASS_NUMERICAL_ONLY",
        "input_sha256": dict(sorted(fingerprints.items())),
        "reference_answers": {"path": str(ANSWER.relative_to(ROOT)), "sha256": digest(answer_bytes), "bytes": len(answer_bytes)},
        "checks": {"frozen_files_verified": 7, "all_saved_typed_values_equal_independent_raw_projection": checked,
            "rows": len(saved), "columns": len(names), "orders": main_kpis["orders"],
            "customer_eligible_lines": len(eligible), "customer_eligible_orders": kpis(eligible)["orders"],
            "excluded_customer_lines": len(excluded), "raw_conflict_orders": len(conflicts),
            "covered_months": len(coverage), "retained_cross_end_ship_lines": len(crossing_ids),
            "source_controls_and_segment_totals_exact": True, "source_hand_check_exact": True,
            "population_bridges_exact": True, "returns_distinct_order_denominators": True,
            "weighted_ratios_and_category_overlap": True, "calendar_growth_and_covered_zero_vs_missing": True,
            "source_csv_manifest_preparation_script_hashes": True},
        "limits": ["No Tableau/UI/visual/filter execution; no prepared workbook", "No source-formula recalculation or upstream truth audit",
            "No public/teaching release or redistributed-source permission", "Rights and currency/accounting semantics remain separately qualified"],
        "report_self_hash": "Not embedded; verify externally to avoid circularity"}
    outputs = {ANSWER: answer_bytes, REPORT: encode(serialize(report))}
    # Preflight everything before any writes; existing versions are immutable.
    for path, original_hash in fingerprints.items():
        require(digest((ROOT / path).read_bytes()) == original_hash, f"Input changed during validation: {path}")
    for path, payload in outputs.items():
        require(not path.exists() or (path.is_file() and path.read_bytes() == payload), f"Immutable numeric output mismatch: {path}; nothing replaced")
    created = 0
    for path, payload in outputs.items():
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as handle:
                handle.write(payload)
            created += 1
        require(path.read_bytes() == payload, f"Saved numeric output changed: {path}")
    print(f"PASS independent numerical validation: {len(saved)} lines, {main_kpis['orders']} orders, {checked} exact typed values; seven frozen hashes verified.")
    print(f"{'Created' if created else 'Verified byte-identical'} two private immutable reports; numeric only, Tableau unverified, publication false.")


if __name__ == "__main__":
    main()
