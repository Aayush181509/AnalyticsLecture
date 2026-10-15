"""Independently validate the synthetic hr-v1 release (D07).

Checks, using only the standard library (no shared code with the generator):

1. manifest SHA-256 and byte counts;
2. employees: unique ids, hire before exit, no event after the cutoff, employees hired
   before 2025 present for the opening population;
3. department history: intervals start at hire, chain without gaps or overlaps, and end
   at the exit date for leavers (open otherwise);
4. recruitment: unique ids, ordered dates, statuses consistent with dates, filled roles
   linked to an employee with the same hire date;
5. monthly company bridges and department bridges (with transfers) reconcile;
6. built-in teaching cases exist; the generator reproduces the release byte for byte.

Usage:
    python scripts/validate_hr.py
    python scripts/validate_hr.py --answers instructor/solutions/hr-v1/reference_answers.md
Requires: requirements.txt (Python 3.12).
"""

from collections import defaultdict
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
DATA = ROOT / "data/synthetic/hr-v1"
GENERATOR = ROOT / "scripts/generate_hr.py"
CUTOFF = date(2025, 12, 31)
MONTHS = [date(2025, m, 1) for m in range(1, 13)] + [date(2026, 1, 1)]


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def d(text):
    return date.fromisoformat(text) if text else None


def read(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def check_manifest():
    manifest = json.loads((DATA / "manifest.json").read_text())
    for name, info in manifest["files"].items():
        data = (DATA / name).read_bytes()
        require(hashlib.sha256(data).hexdigest() == info["sha256"], f"{name} hash differs from manifest")
        require(len(data) == info["bytes"], f"{name} size differs from manifest")


def check_employees(emp):
    ids = [e["employee_id"] for e in emp]
    require(len(ids) == len(set(ids)), "employee_id not unique")
    for e in emp:
        e["hire"], e["exit"] = d(e["hire_date"]), d(e["exit_date"])
        require(e["hire"] <= CUTOFF, f"{e['employee_id']} hired after cutoff")
        if e["exit"]:
            require(e["hire"] < e["exit"] <= CUTOFF, f"{e['employee_id']} exit order or after cutoff")
    require(sum(e["hire"] < MONTHS[0] for e in emp) > 300, "expected pre-2025 employees")
    return {e["employee_id"]: e for e in emp}


def check_history(hist, emp):
    by = defaultdict(list)
    for h in hist:
        h["from"], h["to"] = d(h["effective_from"]), d(h["effective_to"])
        by[h["employee_id"]].append(h)
    require(set(by) == set(emp), "history does not cover exactly the employees")
    for eid, rows in by.items():
        rows.sort(key=lambda r: r["from"])
        require(rows[0]["from"] == emp[eid]["hire"], f"{eid} first interval not at hire")
        for a, b in zip(rows, rows[1:]):
            require(a["to"] == b["from"] and a["department_id"] != b["department_id"], f"{eid} gap, overlap or no-op transfer")
        require(rows[-1]["to"] == emp[eid]["exit"], f"{eid} last interval does not end at exit")
    return by


def check_recruitment(req, emp):
    ids = [r["requisition_id"] for r in req]
    require(len(ids) == len(set(ids)), "requisition_id not unique")
    for r in req:
        r["opened"], r["accepted"], r["hire"] = d(r["opened_date"]), d(r["offer_accepted_date"]), d(r["hire_date"])
        rid, st = r["requisition_id"], r["status"]
        require(r["opened"] <= CUTOFF, f"{rid} opened after cutoff")
        if st == "filled":
            require(r["accepted"] and r["hire"] and r["opened"] <= r["accepted"] <= r["hire"] <= CUTOFF, f"{rid} filled dates")
            require(emp[r["employee_id"]]["hire"] == r["hire"], f"{rid} hire date differs from employee")
        elif st == "accepted":
            require(r["accepted"] and not r["hire"] and not r["employee_id"], f"{rid} accepted dates")
        else:
            require(st in ("open", "canceled") and not r["accepted"] and not r["hire"], f"{rid} {st} dates")
    hired_2025 = {e["employee_id"] for e in emp.values() if e["hire"] >= MONTHS[0]}
    linked = {r["employee_id"] for r in req if r["employee_id"]}
    require(hired_2025 <= linked, "a 2025 hire has no requisition")


def active_at_start(start, intervals):
    """Count people whose interval contains the start of day `start` (from < start <= to)."""
    return sum(1 for f, t in intervals if f < start and (t is None or t >= start))


def bridges(emp, hist_by):
    company = []
    spans = [(e["hire"], e["exit"]) for e in emp.values()]
    for a, b in zip(MONTHS, MONTHS[1:]):
        op, cl = active_at_start(a, spans), active_at_start(b, spans)
        hires = sum(a <= e["hire"] < b for e in emp.values())
        exits = sum(1 for e in emp.values() if e["exit"] and a <= e["exit"] < b)
        require(cl == op + hires - exits, f"company bridge fails for {a}")
        company.append((a, op, hires, exits, cl))
    depts = sorted({h["department"] for rows in hist_by.values() for h in rows})
    dept_rows = {}
    for dept in depts:
        ivs, rows = [], []
        for eid, hs in hist_by.items():
            for h in hs:
                if h["department"] == dept:
                    ivs.append((h["from"], h["to"], eid, h, hs))
        for a, b in zip(MONTHS, MONTHS[1:]):
            op = active_at_start(a, [(f, t) for f, t, *_ in ivs])
            cl = active_at_start(b, [(f, t) for f, t, *_ in ivs])
            hires = sum(1 for f, t, eid, h, hs in ivs if h is hs[0] and a <= f < b)
            t_in = sum(1 for f, t, eid, h, hs in ivs if h is not hs[0] and a <= f < b)
            exits = sum(1 for f, t, eid, h, hs in ivs if h is hs[-1] and t and a <= t < b)
            t_out = sum(1 for f, t, eid, h, hs in ivs if h is not hs[-1] and a <= t < b)
            require(cl == op + hires + t_in - exits - t_out, f"{dept} bridge fails for {a}")
            rows.append((a, op, hires, t_in, exits, t_out, cl))
        dept_rows[dept] = rows
    return company, dept_rows


def check_cases(emp, hist_by, req):
    require(sum(len(v) > 1 for v in hist_by.values()) >= 15, "expected transfers")
    require(sum(1 for e in emp.values() if e["exit"] and e["exit"].day == 1) >= 5, "expected exits on a month start")
    statuses = {r["status"] for r in req}
    require({"filled", "accepted", "open", "canceled"} <= statuses, "expected all requisition statuses")


def check_reproducible():
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([sys.executable, str(GENERATOR), "--out", tmp], check=True, capture_output=True)
        for name in ("employees.csv", "department_history.csv", "recruitment.csv", "README.md"):
            require((Path(tmp) / name).read_bytes() == (DATA / name).read_bytes(), f"{name} not reproducible")


def turnover(rows, exit_col, close_col, open_col=1):
    avg = statistics.mean((r[open_col] + r[close_col]) / 2 for r in rows)
    exits = sum(r[exit_col] for r in rows)
    monthly = [r[exit_col] / ((r[open_col] + r[close_col]) / 2) for r in rows if (r[open_col] + r[close_col])]
    return exits, avg, exits / avg, exits / rows[-1][close_col], statistics.mean(monthly) * 12


def answers(emp, hist_by, req, company, dept_rows):
    lines = ["# hr-v1 reference answers (private)", "",
             f"Instructor-only. Computed by `scripts/validate_hr.py --answers` from dataset `hr-v1` (cutoff {CUTOFF}). "
             "Do not copy into learner notebooks.", "",
             "## Company monthly bridge (closing = opening + hires − exits)", "",
             "| Month | Opening | Hires | Exits | Closing | Avg headcount | Turnover |", "|---|---|---|---|---|---|---|"]
    for a, op, hi, ex, cl in company:
        lines.append(f"| {a:%Y-%m} | {op} | {hi} | {ex} | {cl} | {(op + cl) / 2:.1f} | {ex / ((op + cl) / 2) * 100:.1f}% |")
    exits, avg, right, wrong, mean12 = turnover(company, 3, 4)
    lines += ["", f"- Annual exits {exits}; mean of monthly average headcount {avg:.1f}; **annual turnover {right * 100:.1f}%**.",
              f"- Wrong: exits / December closing headcount = {wrong * 100:.1f}%; 12 × mean monthly rate = {mean12 * 100:.1f}%.", "",
              "## Department annual turnover (department bridges include transfers)", "",
              "| Department | Start | Peak | End | Exits | Transfers in | Transfers out | Correct | ÷ December | Note |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for dept, rows in dept_rows.items():
        exits = sum(r[4] for r in rows)
        avg = statistics.mean((r[1] + r[6]) / 2 for r in rows)
        peak = max(max(r[1], r[6]) for r in rows)
        note = "small group: flag, do not rank" if avg < 20 else ""
        lines.append(f"| {dept} | {rows[0][1]} | {peak} | {rows[-1][6]} | {exits} | {sum(r[3] for r in rows)} | "
                     f"{sum(r[5] for r in rows)} | {exits / avg * 100:.1f}% | {exits / rows[-1][6] * 100:.1f}% | {note} |")
    lines += ["", "## Recruitment", "", "| Department | Accepted | Median days to accept | Open at cutoff | Oldest open (days) |",
              "|---|---|---|---|---|"]
    by = defaultdict(list)
    for r in req:
        by[r["department"]].append(r)
    for dept in sorted(by):
        acc = [(r["accepted"] - r["opened"]).days for r in by[dept] if r["accepted"]]
        opn = [(CUTOFF - r["opened"]).days for r in by[dept] if r["status"] == "open"]
        lines.append(f"| {dept} | {len(acc)} | {statistics.median(acc) if acc else 'n/a'} | {len(opn)} | {max(opn) if opn else '-'} |")
    counts = defaultdict(int)
    for r in req:
        counts[r["status"]] += 1
    lines += ["", f"- Requisition statuses: {dict(sorted(counts.items()))}. Open roles must keep their open age, "
              "never zero days.", "", "## Tenure at the cutoff (active employees only)", ""]
    active = [(CUTOFF - e["hire"]).days for e in emp.values() if not e["exit"]]
    lines.append(f"- Active at cutoff {len(active)}; median tenure {statistics.median(active)} days; mean {statistics.mean(active):.0f} days.")
    lines.append(f"- Exits dated on the 1st of a month: {sum(1 for e in emp.values() if e['exit'] and e['exit'].day == 1)} "
                 "(the contract counts them in that month's opening headcount and as that month's exits, so the bridge still holds).")
    return "\n".join(lines) + "\n"


def main(argv):
    check_manifest()
    emp = check_employees(read("employees.csv"))
    hist_by = check_history(read("department_history.csv"), emp)
    req = read("recruitment.csv")
    check_recruitment(req, emp)
    company, dept_rows = bridges(emp, hist_by)
    check_cases(emp, hist_by, req)
    check_reproducible()
    print(f"PASS: employees {len(emp)}, history intervals {sum(len(v) for v in hist_by.values())}, requisitions {len(req)}; "
          "keys, chronology, intervals, links, company and department bridges, teaching cases and reproducibility checked")
    if "--answers" in argv:
        out = ROOT / argv[argv.index("--answers") + 1]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(answers(emp, hist_by, req, company, dept_rows))
        print(f"wrote private answers to {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
