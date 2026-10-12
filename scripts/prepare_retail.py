"""Prepare the frozen Superstore retail-v1 local development slice.

Run with the data-audit Python/xlrd environment. Originals and frozen contracts
are read-only. Existing output versions are verified byte-for-byte, never replaced.
No network, Tableau execution, learner packaging or publication is performed.
"""

import csv
from collections import defaultdict
from datetime import date
from decimal import Decimal, getcontext
import hashlib
import io
import json
import platform
from pathlib import Path
import subprocess
import sys
import tempfile

import xlrd

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_DIR = ROOT / "data/metadata/superstore/retail-v1"
OUTPUT_DIR = ROOT / "data/prepared/superstore/retail-v1"
PRIVATE_PATH = ROOT / "instructor/solutions/superstore/retail-v1/preparation_exceptions.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def exact_totals(rows):
    return {
        "lines": len(rows),
        "orders": len({r["order_id"] for r in rows}),
        "customer_ids": len({r["customer_id"] for r in rows}),
        "sales": str(sum((Decimal(repr(r["sales"])) for r in rows), Decimal(0))),
        "profit": str(sum((Decimal(repr(r["profit"])) for r in rows), Decimal(0))),
        "quantity": sum(r["quantity"] for r in rows),
    }


def reconcile_partition(whole, parts):
    reference = exact_totals(whole)
    require(sum(len(p) for p in parts) == len(whole), "Partition line count")
    ids = [r["row_id"] for part in parts for r in part]
    require(len(ids) == len(set(ids)) == len(whole), "Partition row multiplication")
    require(set(ids) == {r["row_id"] for r in whole}, "Partition row coverage")
    for measure in ("sales", "profit", "quantity"):
        combined = sum((Decimal(str(exact_totals(part)[measure])) for part in parts), Decimal(0))
        require(combined == Decimal(str(reference[measure])), f"Partition {measure}")


def read_source(settings):
    source = ROOT / settings["source"]["path"]
    content = source.read_bytes()
    require(len(content) == settings["source"]["bytes"], "Source bytes changed")
    require(sha(content) == settings["source"]["sha256"], "Source hash changed")
    book = xlrd.open_workbook(file_contents=content)
    tables = {}
    for name in settings["source"]["sheets"]:
        sheet = book.sheet_by_name(name)
        headers = sheet.row_values(0)
        tables[name] = [dict(zip(headers, sheet.row_values(i))) for i in range(1, sheet.nrows)]
    raw = tables["Orders"]
    customers = defaultdict(set)
    for row in raw:
        customers[row["Order ID"]].add(row["Customer ID"])
    conflicts = {key for key, values in customers.items() if len(values) > 1}
    require(sorted(conflicts) == settings["customer_policy"]["expected_conflicting_orders_all_source"],
            "Unexpected whole-source customer conflicts")
    returned = {r["Order ID"] for r in tables["Returns"]}
    projected = []
    for original in raw:
        row = {}
        for column in settings["prepared"]["columns"]:
            if "source" not in column:
                continue
            value = original[column["source"]]
            if column["type"] == "date":
                moment = xlrd.xldate_as_datetime(value, book.datemode)
                require(moment.time().isoformat() == "00:00:00", "Source timestamp is not date-only")
                value = moment.date()
            elif column["type"] == "integer":
                require(value == int(value), "Source integer has a fractional component")
                value = int(value)
            row[column["name"]] = value
        conflict = int(row["order_id"] in conflicts)
        row.update(returned_order_flag=int(row["order_id"] in returned),
                   customer_order_conflict=conflict, customer_analysis_eligible=1 - conflict,
                   order_to_ship_days=(row["ship_date"] - row["order_date"]).days,
                   order_month=row["order_date"].replace(day=1))
        require(row["order_to_ship_days"] >= 0, "Negative dispatch interval")
        projected.append(row)
    return projected, sorted(conflicts)


def make_csv(rows, columns):
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow([c["name"] for c in columns])
    for row in rows:
        values = []
        for column in columns:
            value = row[column["name"]]
            if column["type"] == "date":
                value = value.isoformat()
            elif column["type"] == "decimal":
                value = repr(value)
            values.append(value)
        writer.writerow(values)
    return buffer.getvalue().encode("utf-8")


def verify_csv(content, expected_rows, columns):
    """Typed re-read of every staged field against its canonical source mapping."""
    require(b"\r" not in content and not content.startswith(b"\xef\xbb\xbf"), "CSV encoding/newlines")
    reader = csv.DictReader(io.StringIO(content.decode("utf-8"), newline=""))
    names = [c["name"] for c in columns]
    require(reader.fieldnames == names, "CSV schema/order differs from frozen contract")
    reread = list(reader)
    require(len(reread) == len(expected_rows), "CSV line count")
    for serialized, expected in zip(reread, expected_rows):
        require(set(serialized) == set(names), "CSV row has extra/missing columns")
        for column in columns:
            name, kind = column["name"], column["type"]
            text, original = serialized[name], expected[name]
            require(text is not None and text != "", f"Missing CSV value: {name}")
            if kind in ("integer", "integer_flag"):
                value = int(text)
                require(str(value) == text, f"Noncanonical integer: {name}")
                if kind == "integer_flag":
                    require(value in (0, 1), f"Invalid flag: {name}")
            elif kind == "date":
                value = date.fromisoformat(text)
                require(value.isoformat() == text, f"Noncanonical date: {name}")
            elif kind == "decimal":
                value = Decimal(text)
                require(value.is_finite(), f"Nonfinite numeric: {name}")
                original = Decimal(str(original))
            else:
                value = text
            require(value == original, f"Source-to-CSV mismatch Row ID {expected['row_id']}: {name}")
    require([int(r["row_id"]) for r in reread] == sorted(r["row_id"] for r in expected_rows),
            "CSV Row ID ordering")
    return len(reread) * len(columns)


def build_reports(raw, scoped, outside, conflicts, settings):
    eligible = [r for r in scoped if r["customer_analysis_eligible"] == 1]
    excluded = [r for r in scoped if r["customer_analysis_eligible"] == 0]
    reconcile_partition(raw, [scoped, outside])
    reconcile_partition(scoped, [eligible, excluded])
    require(len(scoped) == 6815 and len({r["order_id"] for r in scoped}) == 3388, "Frozen scope counts")
    require(len(eligible) == 6811 and len({r["order_id"] for r in eligible}) == 3387,
            "Eligible counts")
    require({r["order_id"] for r in excluded} == {"CA-2025-121465"}, "In-scope conflicts")
    require(len({r["row_id"] for r in raw}) == len(raw), "Raw Row ID uniqueness")
    require(len({r["row_id"] for r in scoped}) == len(scoped), "Prepared Row ID uniqueness")
    months = sorted({r["order_month"].isoformat() for r in scoped})
    require(months == [f"{year}-{month:02}-01" for year in range(2023, 2026) for month in range(1, 13)],
            "36-month coverage")
    end = date.fromisoformat(settings["scope"]["end_exclusive"])
    crossing = [r["row_id"] for r in scoped if r["ship_date"] >= end]
    require(bool(crossing), "Ship-date crossing records were lost")
    by_order = defaultdict(list)
    for row in raw:
        by_order[row["order_id"]].append(row)
    stable_names = {c["source"]: c["name"] for c in settings["prepared"]["columns"] if "source" in c}
    for group in by_order.values():
        for field in settings["order_stable_fields"]:
            require(len({r[stable_names[field]] for r in group}) == 1, f"Unstable {field}")
        for flag in ("returned_order_flag", "customer_order_conflict", "customer_analysis_eligible"):
            require(len({r[flag] for r in group}) == 1, f"Unstable {flag}")
    partitions = {}
    for field in ("segment", "region", "order_month"):
        groups = defaultdict(list)
        for row in scoped:
            groups[str(row[field])].append(row)
        reconcile_partition(scoped, list(groups.values()))
        order_total = sum(len({r["order_id"] for r in group}) for group in groups.values())
        require(order_total == 3388, f"{field} order-count partition")
        partitions[field] = {"groups": len(groups), "line_partition": True,
                             "exact_sales_profit_quantity_reconcile": True,
                             "distinct_order_counts_reconcile": True}
    categories = defaultdict(set)
    for row in scoped:
        categories[row["category"]].add(row["order_id"])
    category_sum = sum(map(len, categories.values()))
    require(category_sum > 3388, "Expected category order overlap is absent")
    private = {
        "contract_id": settings["contract_id"], "contract_date": settings["contract_date"],
        "purpose": "Private preparation exceptions and population bridges; not released lesson answers",
        "currency_label": settings["currency"]["label"], "publication_approved": False,
        "populations": {name: exact_totals(rows) for name, rows in (
            ("all_raw", raw), ("primary_scope", scoped), ("outside_date_scope", outside),
            ("customer_eligible", eligible), ("customer_conflict_excluded_from_customer_view", excluded))},
        "exact_bridges": {"all_raw_equals_primary_plus_outside": True,
                          "primary_equals_customer_eligible_plus_conflict": True},
        "conflicting_orders_all_raw": {},
    }
    included_ids = {r["row_id"] for r in scoped}
    for order in conflicts:
        private["conflicting_orders_all_raw"][order] = [{
            "row_id": r["row_id"], "order_id": r["order_id"], "customer_id": r["customer_id"],
            "order_date": r["order_date"].isoformat(), "ship_date": r["ship_date"].isoformat(),
            "sales": repr(r["sales"]), "profit": repr(r["profit"]), "quantity": r["quantity"],
            "in_primary_scope": r["row_id"] in included_ids,
            "customer_order_conflict": r["customer_order_conflict"],
            "customer_analysis_eligible": r["customer_analysis_eligible"],
        } for r in sorted(by_order[order], key=lambda r: r["row_id"])]
    report = {
        "contract_id": settings["contract_id"], "contract_date": settings["contract_date"],
        "local_development_only": True, "publication_approved": False, "tableau_verified": False,
        "source_lines": len(raw), "included_lines": len(scoped), "included_orders": 3388,
        "outside_scope_lines": len(outside), "customer_eligible_lines": len(eligible),
        "customer_eligible_orders": 3387, "conflict_orders_all_raw": len(conflicts),
        "conflict_orders_in_scope": 1, "customer_excluded_lines": len(excluded),
        "included_source_row_ids": sorted(included_ids),
        "excluded_source_row_ids": sorted(r["row_id"] for r in outside),
        "source_row_partition_disjoint_and_complete": True, "no_row_multiplication": True,
        "whole_source_conflicts_before_date_filter": True, "flags_stable_within_order": True,
        "stable_attributes_checked": settings["order_stable_fields"],
        "order_months": months, "ship_dates_after_scope_end_retained_row_ids": sorted(crossing),
        "partitions": partitions,
        "category_overlap_diagnostic": {"distinct_orders": 3388,
            "distinct_orders_by_category": {k: len(v) for k, v in sorted(categories.items())},
            "sum_category_distinct_orders": category_sum,
            "overlap_excess": category_sum - 3388, "counts_are_not_additive": True},
        "private_exception_path": str(PRIVATE_PATH.relative_to(ROOT)),
        "limits": ["Stored source values only; no formula recalculation", "No Tableau execution",
                   "No learner answer release or redistribution approval", "ISO currency/accounting semantics unknown"],
    }
    return report, private


def main():
    require(not sys.flags.optimize, "Run without -O: frozen checker uses assertions")
    getcontext().prec = 60
    subprocess.run([sys.executable, str(ROOT / "scripts/check_retail_contract.py")], check=True, cwd=ROOT)
    settings = json.loads((CONTRACT_DIR / "contract.json").read_text())
    freeze_path = CONTRACT_DIR / "freeze.json"
    freeze_bytes = freeze_path.read_bytes()
    freeze = json.loads(freeze_bytes)
    frozen = {r["path"]: r["sha256"] for r in freeze["files"]}
    require(all(sha((ROOT / path).read_bytes()) == digest for path, digest in frozen.items()),
            "Frozen files changed after preflight")
    raw, conflicts = read_source(settings)
    start, end = (date.fromisoformat(settings["scope"][k]) for k in ("start_inclusive", "end_exclusive"))
    scoped = sorted((r for r in raw if start <= r["order_date"] < end), key=lambda r: r["row_id"])
    outside = [r for r in raw if not start <= r["order_date"] < end]
    report, private = build_reports(raw, scoped, outside, conflicts, settings)
    csv_content = make_csv(scoped, settings["prepared"]["columns"])
    report["typed_source_to_csv_values_checked"] = verify_csv(csv_content, scoped, settings["prepared"]["columns"])
    report_content, private_content = json_bytes(report), json_bytes(private)
    script_path = Path(__file__).resolve()
    manifest = {
        "contract_id": settings["contract_id"], "contract_date": settings["contract_date"],
        "dataset_label": settings["dataset_label"], "version": "retail-v1", "scope": settings["scope"],
        "currency": settings["currency"], "source": settings["source"],
        "frozen_contract_files_sha256": frozen,
        "freeze_manifest": {"path": str(freeze_path.relative_to(ROOT)), "sha256": sha(freeze_bytes)},
        "preparation_script": {"path": str(script_path.relative_to(ROOT)), "sha256": sha(script_path.read_bytes())},
        "runtime": {"python": platform.python_version(), "implementation": platform.python_implementation(),
                    "xlrd": xlrd.__version__, "decimal_precision": getcontext().prec},
        "schema": settings["prepared"]["columns"], "rows": len(scoped), "distinct_orders": 3388,
        "order_date_min": min(r["order_date"] for r in scoped).isoformat(),
        "order_date_max": max(r["order_date"] for r in scoped).isoformat(),
        "order_month_count": 36, "publication_approved": False, "tableau_verified": False,
        "local_development_only": True,
        "outputs": [{"path": str(path.relative_to(ROOT)), "bytes": len(content), "sha256": sha(content)}
                    for path, content in ((OUTPUT_DIR / "order_lines.csv", csv_content),
                                          (OUTPUT_DIR / "preparation_report.json", report_content),
                                          (PRIVATE_PATH, private_content))],
        "manifest_self_hash": "Not embedded; verify external SHA-256 to avoid circular self-reference",
    }
    outputs = {OUTPUT_DIR / "order_lines.csv": csv_content,
               OUTPUT_DIR / "preparation_report.json": report_content,
               PRIVATE_PATH: private_content, OUTPUT_DIR / "manifest.json": json_bytes(manifest)}
    with tempfile.TemporaryDirectory(prefix="superstore-retail-stage-") as temp:
        staged = {}
        for index, (destination, content) in enumerate(outputs.items()):
            stage = Path(temp) / str(index)
            stage.write_bytes(content)
            require(stage.read_bytes() == content, "Staged output bytes differ")
            staged[destination] = stage
        verify_csv(staged[OUTPUT_DIR / "order_lines.csv"].read_bytes(), scoped, settings["prepared"]["columns"])
        for destination, stage in staged.items():
            if destination.exists():
                require(destination.is_file() and destination.read_bytes() == stage.read_bytes(),
                        f"Immutable output mismatch: {destination.relative_to(ROOT)}; no outputs written")
        if OUTPUT_DIR.exists():
            require(set(OUTPUT_DIR.iterdir()) <= {p for p in outputs if p.parent == OUTPUT_DIR},
                    "Unexpected existing files in immutable output directory")
        require(sha((ROOT / settings["source"]["path"]).read_bytes()) == settings["source"]["sha256"],
                "Source changed during preparation")
        require(freeze_path.read_bytes() == freeze_bytes and
                all(sha((ROOT / path).read_bytes()) == digest for path, digest in frozen.items()),
                "Frozen contract changed during preparation")
        created = []
        for destination, stage in staged.items():
            if not destination.exists():
                destination.parent.mkdir(parents=True, exist_ok=True)
                with destination.open("xb") as handle:
                    handle.write(stage.read_bytes())
                created.append(destination)
        for destination, expected in outputs.items():
            require(destination.read_bytes() == expected, f"Final byte verification failed: {destination}")
        verify_csv((OUTPUT_DIR / "order_lines.csv").read_bytes(), scoped, settings["prepared"]["columns"])
    print(f"PASS {'created' if created else 'verified unchanged'} four immutable local artifacts: "
          f"6815 lines, 3388 orders, 22 fields, 36 months; CSV SHA-256 {sha(csv_content)}")
    print("Private bridges/exceptions checked; no Tableau execution or public release approval.")


if __name__ == "__main__":
    main()
