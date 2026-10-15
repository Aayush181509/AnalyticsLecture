"""Independently validate the synthetic finance-v1 release (D04).

Checks, using only the standard library (no shared code with the generator):

1. manifest SHA-256 and byte counts;
2. posting keys unique, months consistent with posting dates, signs match posting
   types, every reversal references an existing posting of the opposite amount;
3. budget keys unique, budgets never negative, explicit zero budgets present;
4. the built-in teaching cases exist (zero budget with spend, unknown-budget account,
   budget-only cells, duplicated posting and reversal, supplier credit);
5. reconciliation: aggregated actuals equal signed posting totals; the naive
   posting-to-budget join inflates budget totals;
6. the generator reproduces the release byte for byte.

Usage:
    python scripts/validate_finance.py
    python scripts/validate_finance.py --answers instructor/solutions/finance-v1/reference_answers.md
Requires: requirements.txt (Python 3.12).
"""

from collections import defaultdict
from decimal import Decimal
from pathlib import Path
import csv
import hashlib
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/synthetic/finance-v1"
GENERATOR = ROOT / "scripts/generate_finance.py"


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def read(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def check_manifest():
    manifest = json.loads((DATA / "manifest.json").read_text())
    for name, info in manifest["files"].items():
        data = (DATA / name).read_bytes()
        require(hashlib.sha256(data).hexdigest() == info["sha256"], f"{name} hash differs from manifest")
        require(len(data) == info["bytes"], f"{name} size differs from manifest")
    return manifest


def check_actuals(rows):
    ids = [r["posting_id"] for r in rows]
    require(len(ids) == len(set(ids)), "posting_id not unique")
    by_id = {r["posting_id"]: r for r in rows}
    for r in rows:
        require(r["month"] == r["posting_date"][:8] + "01", f"{r['posting_id']} month mismatch")
        require(r["month"].startswith("2025-"), f"{r['posting_id']} outside 2025")
        amount = Decimal(r["amount"])
        if r["posting_type"] == "expense":
            require(amount > 0, f"{r['posting_id']} expense not positive")
        else:
            require(r["posting_type"] in ("credit", "reversal") and amount < 0,
                    f"{r['posting_id']} credit/reversal not negative")
        if r["posting_type"] == "reversal":
            ref = by_id.get(r["reference_posting_id"])
            require(ref is not None, f"{r['posting_id']} reverses a missing posting")
            require(Decimal(ref["amount"]) == -amount, f"{r['posting_id']} does not mirror its reference")
            require(ref["month"] < r["month"], f"{r['posting_id']} reversal not in a later month")
        else:
            require(r["reference_posting_id"] == "", f"{r['posting_id']} unexpected reference")


def check_budget(rows):
    keys = [(r["month"], r["department_id"], r["account_id"]) for r in rows]
    require(len(keys) == len(set(keys)), "budget key not unique")
    require(all(Decimal(r["budget"]) >= 0 for r in rows), "negative budget")


def aggregate(actuals, budget):
    actual = defaultdict(Decimal)
    postings = defaultdict(int)
    for r in actuals:
        key = (r["month"], r["department_id"], r["account_id"])
        actual[key] += Decimal(r["amount"])
        postings[key] += 1
    budgets = {(r["month"], r["department_id"], r["account_id"]): Decimal(r["budget"]) for r in budget}
    return actual, postings, budgets


def check_cases(actuals, actual, postings, budgets):
    zero_with_spend = [k for k, b in budgets.items() if b == 0 and actual.get(k, 0) > 0]
    require(len(zero_with_spend) == 1, "expected one approved-zero budget cell with spend")
    unknown = [k for k in actual if k not in budgets]
    require(len(unknown) == 6 and {k[2] for k in unknown} == {"A700"}, "expected six unknown-budget A700 cells")
    budget_only = [k for k, b in budgets.items() if k not in actual and b > 0]
    require(len(budget_only) == 5, "expected five positive budget-only cells")
    require(sum(r["posting_type"] == "reversal" for r in actuals) == 1, "expected one reversal")
    require(sum(r["posting_type"] == "credit" for r in actuals) == 1, "expected one supplier credit")
    dup = defaultdict(list)
    for r in actuals:
        dup[(r["posting_date"], r["department_id"], r["account_id"], r["amount"], r["description"])].append(r)
    require(sum(len(v) > 1 for v in dup.values()) == 1, "expected exactly one duplicated posting pair")
    return zero_with_spend, unknown, budget_only


def check_reconciliation(actuals, actual, postings, budgets):
    require(sum(actual.values()) == sum(Decimal(r["amount"]) for r in actuals), "aggregate actual mismatch")
    naive_budget = sum(budgets[k] * n for k, n in postings.items() if k in budgets)
    true_budget_matched = sum(budgets[k] for k in postings if k in budgets)
    require(naive_budget > true_budget_matched, "naive join should inflate budget")
    return naive_budget, true_budget_matched


def check_reproducible():
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([sys.executable, str(GENERATOR), "--out", tmp], check=True, capture_output=True)
        for name in ("finance_actuals.csv", "finance_budget.csv", "README.md"):
            require((Path(tmp) / name).read_bytes() == (DATA / name).read_bytes(), f"{name} not reproducible")


def money(x):
    return f"{x:,.2f}"


def pct(num, den):
    return "n/a" if not den else f"{num / den * 100:.1f}%"


def answers(actuals, budget, actual, postings, budgets, cases, naive):
    zero_with_spend, unknown, budget_only = cases
    naive_budget, true_budget_matched = naive
    keys = sorted(set(actual) | set(budgets))
    known = [k for k in keys if k in budgets]
    total_actual = sum(actual.values())
    known_actual = sum(actual.get(k, Decimal(0)) for k in known)
    known_budget = sum(budgets[k] for k in known)
    unknown_actual = sum(actual[k] for k in unknown)
    names = {r["department_id"]: r["department"] for r in budget}
    names.update({r["account_id"]: r["account"] for r in budget})
    names["A700"] = "Cloud hosting"
    lines = [
        "# finance-v1 reference answers (private)", "",
        "Instructor-only. Computed by `scripts/validate_finance.py --answers` from dataset `finance-v1` "
        f"(postings {len(actuals)}, budget cells {len(budget)}). Neutral currency units. "
        "Do not copy into learner notebooks.", "",
        "## Totals and reconciliation", "",
        f"- Postings: {len(actuals)}; month-department-account cells with postings: {len(actual)}; budget cells: {len(budgets)}; union of keys: {len(keys)}.",
        f"- Total signed actual (all postings): {money(total_actual)}.",
        f"- Comparable scope (known budget): actual {money(known_actual)}, budget {money(known_budget)}, "
        f"variance {money(known_actual - known_budget)} ({pct(known_actual - known_budget, known_budget)}).",
        f"- Unknown-budget actuals (A700 Cloud hosting, Jul–Dec), reported separately: {money(unknown_actual)}.",
        f"- Naive join of postings to budget cells: budget appears as {money(naive_budget)} instead of {money(true_budget_matched)} "
        f"for the same matched cells ({naive_budget / true_budget_matched:.2f}x).", "",
        "## Built-in teaching cases", "",
        f"- Approved zero budget with spend: {zero_with_spend[0]} actual {money(actual[zero_with_spend[0]])} (variance % not applicable).",
        f"- Unknown budget: {len(unknown)} A700 cells (Technology cloud hosting, July–December).",
        f"- Budget-only cells (no postings): {', '.join(k[0] + ' ' + k[1] + ' ' + k[2] for k in sorted(budget_only))}.",
        "- Sales travel May: one conference invoice posted twice (identical rows); the second copy is reversed in June. "
        "May looks unfavourable and June favourable; combined, the effect cancels.",
        "- People professional services October: supplier credit −2,000.00 lowers actual; not an operating improvement.",
        "- Operations salaries Jul–Dec: about 3% over a very large budget (large amount, small %).",
        "- People training September: about 3x a small budget (small amount, large %).",
        "- Technology software from April: about 25% over budget every month (supplier price rise).", "",
        "## Annual variance by department and account (known-budget cells only)", "",
        "| Department | Account | Actual | Budget | Variance | Variance % |", "|---|---|---|---|---|---|",
    ]
    by_da = defaultdict(lambda: [Decimal(0), Decimal(0)])
    for k in known:
        by_da[(k[1], k[2])][0] += actual.get(k, Decimal(0))
        by_da[(k[1], k[2])][1] += budgets[k]
    ranked = sorted(by_da.items(), key=lambda kv: -abs(kv[1][0] - kv[1][1]))
    for (d, a), (act, bud) in ranked:
        lines.append(f"| {names[d]} | {names[a]} | {money(act)} | {money(bud)} | {money(act - bud)} | {pct(act - bud, bud)} |")
    lines += ["", "## Annual variance by department (known-budget cells only)", "",
              "| Department | Actual | Budget | Variance | Variance % |", "|---|---|---|---|---|"]
    by_d = defaultdict(lambda: [Decimal(0), Decimal(0)])
    for (d, a), (act, bud) in by_da.items():
        by_d[d][0] += act
        by_d[d][1] += bud
    for d, (act, bud) in sorted(by_d.items()):
        lines.append(f"| {names[d]} | {money(act)} | {money(bud)} | {money(act - bud)} | {pct(act - bud, bud)} |")
    lines += ["", "## Monthly Sales travel (shows the duplicate and reversal)", "",
              "| Month | Actual | Budget | Variance |", "|---|---|---|---|"]
    for k in keys:
        if k[1] == "D01" and k[2] == "A200":
            lines.append(f"| {k[0][:7]} | {money(actual.get(k, 0))} | {money(budgets[k])} | {money(actual.get(k, 0) - budgets[k])} |")
    return "\n".join(lines) + "\n"


def main(argv):
    check_manifest()
    actuals, budget = read("finance_actuals.csv"), read("finance_budget.csv")
    check_actuals(actuals)
    check_budget(budget)
    actual, postings, budgets = aggregate(actuals, budget)
    cases = check_cases(actuals, actual, postings, budgets)
    naive = check_reconciliation(actuals, actual, postings, budgets)
    check_reproducible()
    print(f"PASS: finance_actuals {len(actuals)} rows, finance_budget {len(budget)} rows; hashes, keys, "
          "signs, reversal, teaching cases, reconciliation and reproducibility checked")
    if "--answers" in argv:
        out = ROOT / argv[argv.index("--answers") + 1]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(answers(actuals, budget, actual, postings, budgets, cases, naive))
        print(f"wrote private answers to {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
