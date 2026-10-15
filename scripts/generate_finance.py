"""Generate the synthetic finance-v1 teaching release (D04).

Two tables for Session 10 (planning/COURSE_PLAN.md, CASE_STUDIES.md "Finance"):

- finance_actuals.csv: one row per expense posting in calendar 2025
  (positive = expense, negative = credit or reversal).
- finance_budget.csv: one row per approved monthly budget cell
  (month, department_id, account_id). An absent cell means the budget is
  unknown; an explicit 0 means an approved zero budget.

Everything is synthetic: a fictional company's management-expense view, not
a financial statement. Built-in teaching cases (a duplicated posting and its
reversal, a supplier credit, an approved zero budget with spend, an unbudgeted
new account, budget-only cells, a large-budget small-percentage overspend and
a small-budget large-percentage overspend) are listed in the README and in the
private reference answers.

Deterministic: a fixed numpy seed and fixed CSV formatting. Running twice
gives byte-identical files.

Usage:
    python scripts/generate_finance.py            # write data/synthetic/finance-v1/
    python scripts/generate_finance.py --out DIR  # write elsewhere (for re-run checks)
Requires: requirements.txt (Python 3.12).
"""

from pathlib import Path
import hashlib
import json
import sys

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data/synthetic/finance-v1"
SEED = 20251101
VERSION = "finance-v1"

DEPARTMENTS = [
    ("D01", "Sales"), ("D02", "Marketing"), ("D03", "Operations"),
    ("D04", "Technology"), ("D05", "People"), ("D06", "Finance and Admin"),
]
ACCOUNTS = [
    ("A100", "Salaries and wages"), ("A200", "Travel"), ("A300", "Software subscriptions"),
    ("A400", "Facilities"), ("A500", "Professional services"), ("A600", "Training"),
    ("A700", "Cloud hosting"),
]
DEPT = dict(DEPARTMENTS)
ACCT = dict(ACCOUNTS)

# Typical monthly budget (currency units) per department and account.
BASE = {
    "A100": {"D01": 82000, "D02": 41000, "D03": 124000, "D04": 71000, "D05": 26000, "D06": 31000},
    "A200": {"D01": 9200, "D02": 4100, "D03": 3200, "D04": 1500, "D05": 1100, "D06": 800},
    "A300": {"D01": 3900, "D02": 6200, "D03": 2800, "D04": 15400, "D05": 2100, "D06": 3100},
    "A400": {"D01": 5200, "D02": 3600, "D03": 20500, "D04": 6100, "D05": 2900, "D06": 3300},
    "A500": {"D01": 2100, "D02": 5300, "D03": 4200, "D04": 6400, "D05": 3100, "D06": 8200},
    "A600": {"D01": 1600, "D02": 1300, "D03": 1900, "D04": 2200, "D05": 4100, "D06": 900},
}
# Travel is higher in spring and autumn (conferences); other accounts are flat.
TRAVEL_SEASON = [0.7, 0.8, 1.1, 1.2, 1.3, 1.0, 0.6, 0.6, 1.2, 1.3, 1.1, 1.1]
MONTHS = pd.date_range("2025-01-01", "2025-12-01", freq="MS")

COLUMNS_ACTUALS = ["posting_id", "posting_date", "month", "department_id", "department",
                   "account_id", "account", "amount", "posting_type", "reference_posting_id",
                   "description"]
COLUMNS_BUDGET = ["month", "department_id", "department", "account_id", "account", "budget"]


def round100(x):
    return float(np.round(x / 100.0) * 100.0)


def make_budget():
    rows = []
    for acct, by_dept in BASE.items():
        for dept, base in by_dept.items():
            for i, month in enumerate(MONTHS):
                factor = TRAVEL_SEASON[i] if acct == "A200" else 1.0
                budget = round100(base * factor)
                if dept == "D06" and acct == "A600" and month.month <= 3:
                    budget = 0.0                      # approved zero budget (training freeze)
                rows.append((month, dept, acct, budget))
    # A700 Cloud hosting (Technology) starts in July with no approved budget: unknown, so no rows.
    budget = pd.DataFrame(rows, columns=["month", "department_id", "account_id", "budget"])
    return budget


def target_actual(rng, month, dept, acct, budget):
    """Monthly spend before it is split into postings. None means no postings."""
    m = month.month
    if dept == "D06" and acct == "A600" and m <= 3:
        return 1850.0 if m == 2 else None           # spend against an approved zero budget
    if dept == "D02" and acct == "A600" and m >= 8:
        return None                                  # budget-only: training cancelled
    noise = rng.normal(0.0, 0.05)
    level = budget * (1.0 + noise)
    if dept == "D03" and acct == "A100" and m >= 7:
        level = budget * (1.03 + rng.normal(0.0, 0.005))   # big budget, small % overspend
    if dept == "D04" and acct == "A300" and m >= 4:
        level = budget * (1.25 + rng.normal(0.0, 0.02))    # supplier price rise
    if dept == "D05" and acct == "A600" and m == 9:
        level = budget * 3.0                               # small budget, large % overspend
    return float(np.round(level, 2))


def split(rng, total, acct):
    """Split a monthly amount into postings that sum exactly to it."""
    k = 2 if acct == "A100" else int(rng.integers(1, 7))
    weights = rng.dirichlet(np.ones(k) * 3.0)
    parts = np.round(total * weights, 2)
    parts[-1] = np.round(total - parts[:-1].sum(), 2)
    return [float(p) for p in parts]


def posting_days(rng, month, acct, k):
    last = month.days_in_month
    if acct == "A100":
        return [15, last][:k]
    return sorted(int(d) for d in rng.integers(1, last + 1, size=k))


def make_actuals(rng, budget):
    rows = []
    lookup = {(r.month, r.department_id, r.account_id): r.budget for r in budget.itertuples()}
    for acct in BASE:
        for dept in BASE[acct]:
            for month in MONTHS:
                total = target_actual(rng, month, dept, acct, lookup[(month, dept, acct)])
                if total is None:
                    continue
                parts = split(rng, total, acct)
                days = posting_days(rng, month, acct, len(parts))
                for amount, day in zip(parts, days):
                    rows.append([month.replace(day=day), month, dept, acct, amount, "expense", "",
                                 f"{ACCT[acct]} - {DEPT[dept]}"])
    # Unbudgeted new account: Technology cloud hosting from July.
    for month in MONTHS[6:]:
        total = float(np.round(7800 * (1 + 0.04 * (month.month - 7)) * (1 + rng.normal(0, 0.03)), 2))
        for amount, day in zip(split(rng, total, "A700"), posting_days(rng, month, "A700", 2)):
            rows.append([month.replace(day=day), month, "D04", "A700", amount, "expense", "",
                         "Cloud hosting - Technology"])
    actuals = pd.DataFrame(rows, columns=["posting_date", "month", "department_id", "account_id",
                                          "amount", "posting_type", "reference_posting_id",
                                          "description"])
    # Special postings added after the regular ones (ids assigned at the end).
    extra = pd.DataFrame([
        # Sales travel: one conference invoice posted twice in May (identical rows);
        # the second copy is reversed in June.
        [pd.Timestamp("2025-05-28"), pd.Timestamp("2025-05-01"), "D01", "A200", 6500.00, "expense",
         "", "Conference travel invoice"],
        [pd.Timestamp("2025-05-28"), pd.Timestamp("2025-05-01"), "D01", "A200", 6500.00, "expense",
         "", "Conference travel invoice"],
        [pd.Timestamp("2025-06-09"), pd.Timestamp("2025-06-01"), "D01", "A200", -6500.00, "reversal",
         "DUPLICATE", "Reversal of duplicated May conference invoice"],
        # People: supplier credit for an earlier overcharge.
        [pd.Timestamp("2025-10-21"), pd.Timestamp("2025-10-01"), "D05", "A500", -2000.00, "credit",
         "", "Supplier credit note for overcharge"],
    ], columns=actuals.columns)
    actuals = pd.concat([actuals, extra], ignore_index=True)
    actuals = actuals.sort_values(["posting_date", "department_id", "account_id", "amount"],
                                  kind="stable").reset_index(drop=True)
    actuals.insert(0, "posting_id", [f"P25-{i:05d}" for i in range(1, len(actuals) + 1)])
    # The reversal points at the second of the two identical May invoices.
    duplicated = actuals[actuals["description"] == "Conference travel invoice"]
    actuals.loc[actuals["reference_posting_id"] == "DUPLICATE", "reference_posting_id"] = \
        duplicated["posting_id"].iloc[1]
    actuals["department"] = actuals["department_id"].map(DEPT)
    actuals["account"] = actuals["account_id"].map(ACCT)
    actuals["posting_date"] = actuals["posting_date"].dt.strftime("%Y-%m-%d")
    actuals["month"] = pd.to_datetime(actuals["month"]).dt.strftime("%Y-%m-%d")
    return actuals[COLUMNS_ACTUALS]


def finish_budget(budget):
    budget = budget.sort_values(["month", "department_id", "account_id"]).reset_index(drop=True)
    budget["department"] = budget["department_id"].map(DEPT)
    budget["account"] = budget["account_id"].map(ACCT)
    budget["month"] = budget["month"].dt.strftime("%Y-%m-%d")
    return budget[COLUMNS_BUDGET]


def csv_bytes(df):
    return df.to_csv(index=False, lineterminator="\n", float_format="%.2f").encode("utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


README = """# finance-v1: synthetic expense actuals and budgets (D04)

**Synthetic teaching data.** A fictional company's monthly management-expense view for
calendar 2025, generated by `scripts/generate_finance.py` with seed {seed}. No real
company, person or supplier is described. Amounts are in neutral **currency units**
(the course has not fixed a currency). This is not a financial statement: there is no
revenue, no balance sheet and no audit claim. Reuse terms for course-generated data are
not yet chosen (DATA_STRATEGY "Rights status").

Used in Session 10 (finance case).

## finance_actuals.csv

Grain: one row per **expense posting** ({actual_rows} rows). Key: `posting_id`, unique.

| Field | Type | Meaning |
|---|---|---|
| `posting_id` | text | Unique posting code, e.g. `P25-00001` |
| `posting_date` | date | Day the posting was recorded |
| `month` | date (first of month) | Accounting month of the posting |
| `department_id`, `department` | text | Six departments, D01–D06 |
| `account_id`, `account` | text | Seven expense accounts, A100–A700 |
| `amount` | decimal, currency units | Positive = expense; negative = credit or reversal |
| `posting_type` | text | `expense`, `credit` or `reversal` |
| `reference_posting_id` | text | For a reversal, the posting it reverses; otherwise blank |
| `description` | text | Short free-text description |

## finance_budget.csv

Grain: one row per **approved monthly budget cell** ({budget_rows} rows).
Key: (`month`, `department_id`, `account_id`), unique.

| Field | Type | Meaning |
|---|---|---|
| `month` | date (first of month) | Budget month |
| `department_id`, `department` | text | Department |
| `account_id`, `account` | text | Expense account |
| `budget` | decimal, currency units | Approved budget, never negative; `0` is an approved zero budget |

## Contract

- **Aggregate first, then combine.** Sum postings to (month, department, account) before
  joining to budgets. Joining raw postings to budget cells repeats each budget once per
  posting and inflates budget totals.
- Actual = sum of signed posting amounts. Budget = sum of unique budget cells.
- Variance = actual − budget. For expenses, positive is **unfavourable** (overspend) and
  negative is **favourable** (underspend).
- Variance % = variance / budget, only when budget > 0. An approved zero budget with spend
  is "unbudgeted spend against zero", not a percentage. A missing budget cell is
  **unknown**: variance and variance % are both unknown, and those actuals are reported
  separately from the comparable total.
- Use an outer join so actual-only cells (unknown budget) and budget-only cells (no
  postings, actual = 0 after posting completeness is accepted) both stay visible.
- Never average monthly or departmental percentages to get a total percentage; recompute
  from totals of the comparable (known-budget) scope.
- A credit or reversal lowers actual spending in its month; it does not by itself show
  better operating performance.

## Files and checks

`manifest.json` lists SHA-256, row counts, seed, generator hash and library versions.
`scripts/validate_finance.py` independently re-checks every rule above. The built-in
teaching cases and reference totals are in the private
`instructor/solutions/finance-v1/reference_answers.md`; do not copy them to learners.
"""


def main(argv):
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else DEFAULT_OUT
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    budget_raw = make_budget()
    actuals = make_actuals(rng, budget_raw)
    budget = finish_budget(budget_raw)
    files = {
        "finance_actuals.csv": csv_bytes(actuals),
        "finance_budget.csv": csv_bytes(budget),
        "README.md": README.format(seed=SEED, actual_rows=len(actuals),
                                   budget_rows=len(budget)).encode("utf-8"),
    }
    for name, data in files.items():
        (out / name).write_bytes(data)
    manifest = {
        "dataset": VERSION,
        "label": "synthetic",
        "generator": "scripts/generate_finance.py",
        "generator_sha256": sha(Path(__file__).read_bytes()),
        "seed": SEED,
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "currency": "neutral currency units (not fixed by the course)",
        "rights": "unresolved; see planning/DATA_STRATEGY.md Rights status",
        "files": {name: {"sha256": sha(data), "bytes": len(data)} for name, data in sorted(files.items())},
        "rows": {"finance_actuals.csv": len(actuals), "finance_budget.csv": len(budget)},
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(f"wrote {out}: finance_actuals {len(actuals)} rows, finance_budget {len(budget)} rows")


if __name__ == "__main__":
    main(sys.argv[1:])
