"""Independently validate the synthetic operations-v1 release (D05).

Checks, using only the standard library (no shared code with the generator):

1. manifest SHA-256 and byte counts;
2. shipment keys unique; dispatch on or before the cutoff; promise not before dispatch;
   delivery on or after dispatch and never after the cutoff; status consistent with dates;
3. the built-in teaching cases exist (overdue pending shipments, not-yet-due shipments,
   due-today pending shipments, split orders, canceled shipments, missing promises);
4. populations reconcile: eligible = due + not yet due + unknown promise; on-time <= due;
5. the generator reproduces the release byte for byte.

Usage:
    python scripts/validate_operations.py
    python scripts/validate_operations.py --answers instructor/solutions/operations-v1/reference_answers.md
Requires: requirements.txt (Python 3.12).
"""

from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import csv
import hashlib
import json
import statistics
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/synthetic/operations-v1"
GENERATOR = ROOT / "scripts/generate_operations.py"
CUTOFF = date(2025, 12, 31)


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def d(text):
    return date.fromisoformat(text) if text else None


def read():
    with open(DATA / "shipments.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["dispatch"], r["promise"], r["delivered"] = d(r["dispatch_date"]), d(r["promised_date"]), d(r["delivered_date"])
    return rows


def check_manifest():
    manifest = json.loads((DATA / "manifest.json").read_text())
    for name, info in manifest["files"].items():
        data = (DATA / name).read_bytes()
        require(hashlib.sha256(data).hexdigest() == info["sha256"], f"{name} hash differs from manifest")
        require(len(data) == info["bytes"], f"{name} size differs from manifest")


def check_rows(rows):
    ids = [r["shipment_id"] for r in rows]
    require(len(ids) == len(set(ids)), "shipment_id not unique")
    for r in rows:
        sid = r["shipment_id"]
        require(r["dispatch"] is not None and r["dispatch"] <= CUTOFF, f"{sid} dispatch missing or after cutoff")
        if r["promise"]:
            require(r["promise"] >= r["dispatch"], f"{sid} promise before dispatch")
        if r["delivered"]:
            require(r["dispatch"] <= r["delivered"] <= CUTOFF, f"{sid} delivery outside dispatch..cutoff")
        expected = "delivered" if r["delivered"] else r["status"]
        require(r["status"] == expected and r["status"] in ("delivered", "in_transit", "canceled"),
                f"{sid} status inconsistent with dates")


def populations(rows):
    eligible = [r for r in rows if r["status"] != "canceled"]
    due = [r for r in eligible if r["promise"] and r["promise"] <= CUTOFF]
    future = [r for r in eligible if r["promise"] and r["promise"] > CUTOFF]
    unknown = [r for r in eligible if not r["promise"]]
    require(len(due) + len(future) + len(unknown) == len(eligible), "populations do not reconcile")
    on_time = [r for r in due if r["delivered"] and r["delivered"] <= r["promise"]]
    require(len(on_time) <= len(due), "on-time exceeds due")
    return eligible, due, future, unknown, on_time


def check_cases(rows, due, future, unknown):
    pending_due = [r for r in due if not r["delivered"]]
    require(len(pending_due) >= 100, "expected a material overdue pending backlog")
    require(any(r["promise"] == CUTOFF for r in pending_due), "expected due-today pending shipments")
    require(any(r["delivered"] for r in future), "expected some not-yet-due shipments already delivered")
    require(len(unknown) == 12, "expected 12 unknown promise dates")
    require(sum(r["status"] == "canceled" for r in rows) == 40, "expected 40 canceled shipments")
    per_order = Counter(r["order_id"] for r in rows)
    require(sum(n > 1 for n in per_order.values()) > 300, "expected split orders")


def check_reproducible():
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([sys.executable, str(GENERATOR), "--out", tmp], check=True, capture_output=True)
        for name in ("shipments.csv", "README.md"):
            require((Path(tmp) / name).read_bytes() == (DATA / name).read_bytes(), f"{name} not reproducible")


def rate(group):
    n = len(group)
    k = sum(1 for r in group if r["delivered"] and r["delivered"] <= r["promise"])
    return k, n, (f"{k / n * 100:.1f}%" if n else "n/a")


def answers(rows, eligible, due, future, unknown, on_time):
    delivered_due = [r for r in due if r["delivered"]]
    pending_due = [r for r in due if not r["delivered"]]
    completed = [r for r in eligible if r["delivered"]]
    lines = [
        "# operations-v1 reference answers (private)", "",
        f"Instructor-only. Computed by `scripts/validate_operations.py --answers` from dataset `operations-v1` "
        f"({len(rows)} shipments, cutoff {CUTOFF}). Do not copy into learner notebooks.", "",
        "## Populations", "",
        f"- Shipments {len(rows)}; orders {len({r['order_id'] for r in rows})}; split orders "
        f"{sum(n > 1 for n in Counter(r['order_id'] for r in rows).values())}.",
        f"- Canceled {len(rows) - len(eligible)}; eligible {len(eligible)} = due {len(due)} + not yet due {len(future)} "
        f"+ unknown promise {len(unknown)}.",
        f"- Due: delivered {len(delivered_due)}, still pending (overdue or due today) {len(pending_due)}; "
        f"due today and pending {sum(r['promise'] == CUTOFF for r in pending_due)}.",
        f"- Not yet due but already delivered: {sum(1 for r in future if r['delivered'])}.", "",
        "## On-time rate (correct denominator = all due shipments)", "",
        f"- Overall: {len(on_time)} / {len(due)} = {len(on_time) / len(due) * 100:.1f}%.",
        f"- Wrong 'delivered only' rate: {rate(delivered_due)[2]} (hides {len(pending_due)} pending due shipments).",
    ]
    dec = [r for r in due if r["promise"].month == 12]
    lines.append(f"- December promises: correct {rate(dec)[2]}; delivered-only {rate([r for r in dec if r['delivered']])[2]}.")
    lines += ["", "## By carrier, warehouse and warehouse × carrier", "",
              "| Group | On time | Due | Rate |", "|---|---|---|---|"]
    for key in ("carrier", "warehouse"):
        groups = defaultdict(list)
        for r in due:
            groups[r[key]].append(r)
        for g in sorted(groups):
            k, n, p = rate(groups[g])
            lines.append(f"| {g} | {k} | {n} | {p} |")
    groups = defaultdict(list)
    for r in due:
        groups[(r["warehouse"], r["carrier"])].append(r)
    for g in sorted(groups):
        k, n, p = rate(groups[g])
        lines.append(f"| {g[0]} × {g[1]} | {k} | {n} | {p} |")
    lines += ["", "South hub looks worst overall only because most of its shipments use ParcelOne; "
              "within each carrier the warehouses perform similarly.", "",
              "## Lead time, completed shipments only (calendar days)", "",
              "| Service | Completed | Mean | Median | 90th pct | Max |", "|---|---|---|---|---|---|"]
    for service in ("Standard", "Express"):
        lt = sorted((r["delivered"] - r["dispatch"]).days for r in completed if r["service"] == service)
        p90 = lt[int(0.9 * (len(lt) - 1))]
        lines.append(f"| {service} | {len(lt)} | {statistics.mean(lt):.2f} | {statistics.median(lt)} | {p90} | {max(lt)} |")
    lines += ["", "## Overdue pending backlog at the cutoff", "", "| Carrier | Pending due | Mean days past due | Max |", "|---|---|---|---|"]
    by_c = defaultdict(list)
    for r in pending_due:
        by_c[r["carrier"]].append((CUTOFF - r["promise"]).days)
    for c in sorted(by_c):
        lines.append(f"| {c} | {len(by_c[c])} | {statistics.mean(by_c[c]):.1f} | {max(by_c[c])} |")
    return "\n".join(lines) + "\n"


def main(argv):
    check_manifest()
    rows = read()
    check_rows(rows)
    eligible, due, future, unknown, on_time = populations(rows)
    check_cases(rows, due, future, unknown)
    check_reproducible()
    print(f"PASS: shipments {len(rows)} rows; hashes, keys, date order, statuses, populations, "
          "teaching cases and reproducibility checked")
    if "--answers" in argv:
        out = ROOT / argv[argv.index("--answers") + 1]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(answers(rows, eligible, due, future, unknown, on_time))
        print(f"wrote private answers to {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
