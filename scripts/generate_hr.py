"""Generate the synthetic hr-v1 teaching release (D07).

Three source tables for Session 13 (planning/COURSE_PLAN.md, CASE_STUDIES.md "HR"):

- employees.csv: one row per employment spell (one spell per employee, no rehires).
- department_history.csv: one row per department assignment interval [from, to).
- recruitment.csv: one row per requisition, at most one hire each.

Everything is synthetic: no real person, and no demographic or protected attributes.
Built-in teaching cases: seasonal warehouse turnover in Operations, a small People
department whose rates jump around, slow Technology hiring with requisitions still open
at the cutoff, offers accepted but not started by the cutoff, canceled requisitions,
transfers between departments, and exits dated on the first day of a month.

Exit date is the **first inactive date**. Cutoff: 2025-12-31.
Deterministic: a fixed numpy seed and fixed CSV formatting.

Usage:
    python scripts/generate_hr.py            # write data/synthetic/hr-v1/
    python scripts/generate_hr.py --out DIR  # write elsewhere (for re-run checks)
Requires: requirements.txt (Python 3.12).
"""

from datetime import date, timedelta
from pathlib import Path
import hashlib
import json
import sys

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data/synthetic/hr-v1"
SEED = 20251231
VERSION = "hr-v1"
START = date(2025, 1, 1)
CUTOFF = date(2025, 12, 31)

DEPARTMENTS = [("D01", "Sales"), ("D02", "Marketing"), ("D03", "Operations"),
               ("D04", "Technology"), ("D05", "People"), ("D06", "Finance and Admin")]
DEPT = dict(DEPARTMENTS)
FAMILY = {"D01": "Sales", "D02": "Marketing", "D03": "Warehouse", "D04": "Engineering",
          "D05": "Corporate", "D06": "Corporate"}
OPENING = {"D01": 70, "D02": 30, "D03": 160, "D04": 80, "D05": 12, "D06": 25}
# Monthly probability that an active employee leaves.
HAZARD = {"D01": 0.015, "D02": 0.012, "D03": 0.022, "D04": 0.006, "D05": 0.012, "D06": 0.008}
OPS_PEAK = (9, 10, 11)                # warehouse turnover peaks after the summer hiring push
OPS_NO_BACKFILL = (9, 10, 11, 12)     # autumn warehouse leavers are mostly not replaced
# Mean days from opening a requisition to an accepted offer, and from acceptance to start.
TIME_TO_ACCEPT = {"D01": 35, "D02": 40, "D03": 18, "D04": 70, "D05": 40, "D06": 40}
START_LAG = {"D01": 21, "D02": 21, "D03": 7, "D04": 28, "D05": 21, "D06": 21}
GROWTH = {"D04": [(2, 10), (4, 10), (6, 8)], "D03": [(5, 22), (6, 20)], "D01": [(9, 4)]}   # (month, extra roles)


def month_starts():
    return [date(2025, m, 1) for m in range(1, 13)]


def next_month(d):
    return date(d.year + (d.month == 12), d.month % 12 + 1, 1)


class Model:
    def __init__(self, rng):
        self.rng = rng
        self.emp = []      # dicts: id, hire, exit, family, dept_hist [(dept, from, to)]
        self.req = []

    def add_employee(self, hire, dept, family):
        e = {"id": f"E{len(self.emp) + 1:04d}", "hire": hire, "exit": None, "family": family,
             "hist": [[dept, hire, None]]}
        self.emp.append(e)
        return e

    def opening_staff(self):
        for dept, n in OPENING.items():
            for _ in range(n):
                years_ago = min(self.rng.exponential(3.0), 9.5)
                hire = START - timedelta(days=int(30 + years_ago * 365))
                self.add_employee(hire, dept, FAMILY[dept])

    def open_req(self, opened, dept):
        if opened > CUTOFF:
            return None                       # would open after the cutoff: not observed
        rng = self.rng
        r = {"id": f"R{len(self.req) + 1:04d}", "dept": dept, "family": FAMILY[dept], "opened": opened,
             "accepted": None, "hire": None, "status": "open", "employee": None}
        if rng.random() < 0.05:
            r["status"] = "canceled"
        else:
            accept = opened + timedelta(days=int(5 + rng.gamma(2.0, TIME_TO_ACCEPT[dept] / 2.0)))
            if accept <= CUTOFF:
                r["accepted"], r["status"] = accept, "accepted"
                hire = accept + timedelta(days=int(START_LAG[dept] + rng.integers(0, 10)))
                if hire <= CUTOFF:
                    r["hire"], r["status"] = hire, "filled"
        self.req.append(r)
        return r

    def start_hires(self, before):
        """Create employees for filled requisitions whose start date is before `before`."""
        for r in self.req:
            if r["hire"] and r["hire"] < before and r["employee"] is None:
                r["employee"] = self.add_employee(r["hire"], r["dept"], r["family"])["id"]

    def dept_on(self, e, day):
        for dept, frm, to in e["hist"]:
            if frm <= day and (to is None or day < to):
                return dept
        return None

    def run(self):
        rng = self.rng
        # A few requisitions opened late in 2024 so January has hires.
        for dept in ("D01", "D03", "D04"):
            for _ in range(2):
                self.open_req(START - timedelta(days=int(rng.integers(10, 60))), dept)
        for ms in month_starts():
            me = next_month(ms)
            for dept, extra in [(d, n) for d, plan in GROWTH.items() for m, n in plan if m == ms.month]:
                for _ in range(extra):
                    self.open_req(ms + timedelta(days=int(rng.integers(0, 10))), dept)
            self.start_hires(me)
            # Exits among employees active at the month start.
            for e in self.emp:
                if e["exit"] or e["hire"] >= ms:
                    continue
                dept = self.dept_on(e, ms)
                h = HAZARD[dept] * (3.0 if dept == "D03" and ms.month in OPS_PEAK else 1.0)
                if (ms - e["hire"]).days < 90:
                    h *= 2.0                                  # new starters leave more often
                if rng.random() < h:
                    day = 1 if rng.random() < 0.10 else int(rng.integers(2, (me - ms).days + 1))
                    e["exit"] = ms.replace(day=day)
                    e["hist"][-1][2] = e["exit"]
                    replace = 0.3 if dept == "D03" and ms.month in OPS_NO_BACKFILL else 0.85
                    if rng.random() < replace:                # most leavers are replaced
                        self.open_req(e["exit"] + timedelta(days=int(rng.integers(0, 10))), dept)
            self.start_hires(me)       # roles opened this month may already have started
        self.transfers()

    def transfers(self):
        rng = self.rng
        candidates = [e for e in self.emp if e["hire"] < date(2025, 2, 1) and len(e["hist"]) == 1]
        for e in rng.choice(candidates, size=24, replace=False):
            day = START + timedelta(days=int(rng.integers(31, 334)))
            day = day.replace(day=1) if rng.random() < 0.5 else day
            if e["exit"] and e["exit"] <= day + timedelta(days=1):
                continue
            old = e["hist"][0][0]
            new = rng.choice([d for d in DEPT if d != old])
            e["hist"] = [[old, e["hist"][0][1], day], [str(new), day, e["exit"]]]


def tables(model):
    emp = pd.DataFrame([{"employee_id": e["id"], "hire_date": e["hire"].isoformat(),
                         "exit_date": e["exit"].isoformat() if e["exit"] else "",
                         "job_family": e["family"]} for e in model.emp])
    hist = pd.DataFrame([{"employee_id": e["id"], "department_id": d, "department": DEPT[d],
                          "effective_from": f.isoformat(), "effective_to": t.isoformat() if t else ""}
                         for e in model.emp for d, f, t in e["hist"]])
    req = pd.DataFrame([{"requisition_id": r["id"], "department_id": r["dept"], "department": DEPT[r["dept"]],
                         "job_family": r["family"], "opened_date": r["opened"].isoformat(),
                         "offer_accepted_date": r["accepted"].isoformat() if r["accepted"] else "",
                         "hire_date": r["hire"].isoformat() if r["hire"] else "",
                         "status": r["status"], "employee_id": r["employee"] or ""} for r in model.req])
    emp = emp.sort_values("employee_id").reset_index(drop=True)
    hist = hist.sort_values(["employee_id", "effective_from"]).reset_index(drop=True)
    req = req.sort_values(["opened_date", "requisition_id"]).reset_index(drop=True)
    return emp, hist, req


def csv_bytes(df):
    return df.to_csv(index=False, lineterminator="\n").encode("utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


README = """# hr-v1: synthetic employees, department history and recruitment (D07)

**Synthetic teaching data.** A fictional company's workforce, generated by
`scripts/generate_hr.py` with seed {seed}. No real person is described, and the release has
**no names and no demographic or protected attributes**. Cutoff: **2025-12-31**. Reuse terms
for course-generated data are not yet chosen (DATA_STRATEGY "Rights status").

Used in Session 13 (HR case).

## employees.csv

Grain: one row per **employment spell** ({emp_rows} rows; one spell per employee, no rehires).
Key: `employee_id`.

| Field | Type | Meaning |
|---|---|---|
| `employee_id` | text | Synthetic employee code |
| `hire_date` | date | First active day |
| `exit_date` | date or blank | **First inactive day**; blank = still employed at the cutoff |
| `job_family` | text | Sales, Marketing, Warehouse, Engineering or Corporate |

Employees hired before 2025 are included so the opening headcount on 2025-01-01 is known.

## department_history.csv

Grain: one row per **department assignment interval** ({hist_rows} rows).
Key: (`employee_id`, `effective_from`). An interval covers `[effective_from, effective_to)`;
a blank `effective_to` means still in that department at the cutoff. Intervals for one
employee do not overlap or leave gaps; the last one ends on the exit date for leavers.
A transfer ends one interval and starts the next on the same date.

## recruitment.csv

Grain: one row per **requisition** (open role) ({req_rows} rows). Key: `requisition_id`.

| Field | Type | Meaning |
|---|---|---|
| `requisition_id` | text | Requisition code |
| `department_id`, `department`, `job_family` | text | Where the role sits |
| `opened_date` | date | Day the role was opened |
| `offer_accepted_date` | date or blank | Day a candidate accepted; blank if not (yet) accepted |
| `hire_date` | date or blank | Start date if the person started by the cutoff |
| `status` | text | `filled`, `accepted` (accepted, starts after cutoff), `open` or `canceled` |
| `employee_id` | text or blank | The employee hired, for filled roles |

## Contract

- Active on day d: hire_date <= d and (exit_date blank or exit_date > d).
- For month [start, next start): opening = everyone hired **before** the start day whose
  exit_date is blank or **on or after** the start day (that is, active at the end of the
  previous month). Hires and exits are events dated in the month. Closing uses the same
  rule with the next start day. An exit dated on the 1st is in that month's opening
  headcount and counts as that month's exit.
  Company bridge: closing = opening + hires − exits.
- Department bridge adds transfers in − transfers out. A transfer is not a hire or an exit.
- Monthly average headcount ≈ (opening + closing) / 2. Monthly turnover = exits / that average.
  Annual turnover = annual exits / mean of the 12 monthly averages — never divide by the
  current (December) headcount and never average monthly rates.
- Tenure at the cutoff covers active employees only. Leavers' length of service is separate.
- Time to fill = offer_accepted_date − opened_date for accepted roles. Open roles keep an
  **open age** = cutoff − opened_date; never record them as zero days or drop them silently.
- Small groups (fewer than about 5 people or events) give unstable rates: combine or flag them.
- Do not infer employee quality, discrimination or causes from these descriptive patterns.

## Files and checks

`manifest.json` lists SHA-256, row counts, seed, generator hash and library versions.
`scripts/validate_hr.py` independently re-checks every rule above. Built-in teaching cases
and reference answers are in the private `instructor/solutions/hr-v1/reference_answers.md`;
do not copy them to learners.
"""


def main(argv):
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else DEFAULT_OUT
    out.mkdir(parents=True, exist_ok=True)
    model = Model(np.random.default_rng(SEED))
    model.opening_staff()
    model.run()
    emp, hist, req = tables(model)
    files = {"employees.csv": csv_bytes(emp), "department_history.csv": csv_bytes(hist),
             "recruitment.csv": csv_bytes(req),
             "README.md": README.format(seed=SEED, emp_rows=len(emp), hist_rows=len(hist),
                                        req_rows=len(req)).encode("utf-8")}
    for name, data in files.items():
        (out / name).write_bytes(data)
    manifest = {
        "dataset": VERSION, "label": "synthetic", "generator": "scripts/generate_hr.py",
        "generator_sha256": sha(Path(__file__).read_bytes()), "seed": SEED,
        "numpy": np.__version__, "pandas": pd.__version__, "cutoff": CUTOFF.isoformat(),
        "rights": "unresolved; see planning/DATA_STRATEGY.md Rights status",
        "files": {name: {"sha256": sha(data), "bytes": len(data)} for name, data in sorted(files.items())},
        "rows": {"employees.csv": len(emp), "department_history.csv": len(hist), "recruitment.csv": len(req)},
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(f"wrote {out}: employees {len(emp)}, department_history {len(hist)}, recruitment {len(req)} rows")


if __name__ == "__main__":
    main(sys.argv[1:])
