# Tableau sessions T1–T4 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish four Tableau sessions (T1–T4), each with a lecture page and a lab page, verified in Tableau Public web authoring, replacing the four old draft lessons.

**Architecture:** Plain Markdown pages in `docs/tableau/`, built by MkDocs (Read the Docs theme). Expected values are computed by one private pandas script from the same Superstore file the Python notebooks use and written to gitignored `instructor/tableau/`. A rehearsal in Chrome checks every lab against those values and supplies screenshots.

**Tech Stack:** MkDocs (Read the Docs theme, admonitions, tasklist), Python 3.12 `.venv` (pandas 2.2.3, xlrd), Tableau Public (desktop click paths; web authoring for rehearsal), Claude in Chrome.

Design: `planning/tableau/2026-10-19-tableau-sessions-design.md`.

## Global Constraints

- Edition: Tableau Public. Click paths written for Tableau Desktop Public Edition; each lab notes that the web editor's menus differ slightly.
- Never save or publish to Tableau Public without the user's explicit approval for that action; never enter credentials; each data upload in Chrome is approved by the user.
- Learner pages never print expected result numbers; learners check work by reconciliation (parts add up to totals).
- Private answers only in `instructor/tableau/Tn/answers.md` (gitignored; never `git add -f`; push `main` only).
- Superstore: Tableau's `sample_-_superstore.xls`, SHA-256 `5045ed4fec49cae2cc0dfc5ab0d204ba09efa767fe00c996822499e8cc42fbbd`, local copy `data/raw/eu-superstore/2026-10-12/sample_-_superstore.xls`. Scope matches the Python `load_orders()`: Order Date 2023-01-01 to 2025-12-31; returned flag = Order ID appears on the Returns sheet.
- Currency: Superstore values are "the file's own monetary units"; never label them dollars.
- Page style: lead paragraph, "What you will be able to do", numbered steps, `!!! note|tip|warning` admonitions, Core / Stretch / Challenge levels, quiz at the end of each lecture, Moodle submission (saved `.twbx` plus a PDF or image export) at the end of each lab, link back to the matching Python session.
- Build checks: `.venv/bin/python scripts/check_docs.py` PASS and `.venv/bin/mkdocs build --strict` PASS after every task.
- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Push only when the user approves.

## File map

| Path | Responsibility |
|---|---|
| `instructor/tableau/compute_answers.py` (private) | Loads Superstore exactly like `load_orders()`, prints every expected value by key; one function per session |
| `instructor/tableau/Tn/answers.md` (private) | Timing, quiz answers, expected values (lines starting `KEY:`), marking notes |
| `scripts/check_tableau_pages.py` | Fails if any `KEY:` value from the private answers appears on a learner page; skips silently when `instructor/` is absent |
| `docs/tableau/index.md` | Section overview: what the four sessions cover, edition, data download, how to submit |
| `docs/tableau/T1_fundamentals_{lecture,lab}.md` | T1 |
| `docs/tableau/T2_calculations_kpis_{lecture,lab}.md` | T2 |
| `docs/tableau/T3_dashboards_{lecture,lab}.md` | T3 |
| `docs/tableau/T4_publishing_portfolio_{lecture,lab}.md` | T4 |
| `docs/tableau/img/Tn_<step>.png` | Rehearsal screenshots |
| `mkdocs.yml` | "Tableau Sessions" nav section |

---

### Task 1: Expected-values script and leak checker

**Files:**
- Create: `instructor/tableau/compute_answers.py`
- Create: `scripts/check_tableau_pages.py`

**Interfaces:**
- Produces: `load_orders() -> pd.DataFrame` (same columns as the notebooks), `t1() / t2() / t3() -> dict[str, str]` of formatted values; the `KEY: <name> = <value>` line format used in every `answers.md`; `scripts/check_tableau_pages.py` exit code 0/1.

- [ ] **Step 1: Write the script** — copy `load_orders()` from the first code cell of `notebooks/05_metrics_and_kpis_lecture.ipynb` (do not change it), reading `data/raw/eu-superstore/2026-10-12/sample_-_superstore.xls`. Add:

```python
def t1(df):
    return {
        "rows": f"{len(df):,}",
        "orders": f"{df.order_id.nunique():,}",
        "returned_orders": f"{df.loc[df.returned_order_flag == 1, 'order_id'].nunique():,}",
        "median_order_value": f"{df.groupby('order_id').sales.sum().median():,.2f}",
        "median_ship_days": f"{df.order_to_ship_days.median():.0f}",
    }

def t2(df):
    seg = df.groupby("segment").agg(sales=("sales", "sum"), profit=("profit", "sum"),
                                    orders=("order_id", "nunique"))
    seg["margin"] = seg.profit / seg.sales
    out = {f"margin_{s}": f"{m:.1%}" for s, m in seg.margin.items()}
    out["overall_margin"] = f"{df.profit.sum() / df.sales.sum():.1%}"
    out["mean_of_line_margins"] = f"{(df.profit / df.sales).mean():.1%}"
    m = df.groupby("order_month").sales.sum()
    out["yoy_dec_2025"] = f"{m.loc['2025-12-01'] / m.loc['2024-12-01'] - 1:.1%}"
    out["mom_dec_2025"] = f"{m.loc['2025-12-01'] / m.loc['2025-11-01'] - 1:.1%}"
    return out

if __name__ == "__main__":
    df = load_orders()
    for name, fn in [("T1", t1), ("T2", t2)]:
        print(f"## {name}")
        for k, v in fn(df).items():
            print(f"KEY: {k} = {v}")
```

- [ ] **Step 2: Run it** — `.venv/bin/python instructor/tableau/compute_answers.py`. Expected: `KEY:` lines; `rows` equals the row count of `data/prepared/superstore/retail-v1/order_lines.csv` (`wc -l` minus 1). If not, stop and compare with `scripts/run_notebooks.py --check-data`.

- [ ] **Step 3: Write `scripts/check_tableau_pages.py`**

```python
"""Fail if a private expected value appears on a Tableau learner page."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
answers = sorted((ROOT / "instructor/tableau").glob("T*/answers.md"))
if not answers:
    print("SKIP: no private answers on this machine")
    sys.exit(0)
values = {m.group(2).strip() for a in answers
          for m in re.finditer(r"^KEY: (\S+) = (.+)$", a.read_text(), re.M)}
values = {v for v in values if len(v) >= 4}  # ignore tiny numbers like "4"
hits = [(p.name, v) for p in (ROOT / "docs/tableau").glob("*.md")
        for v in values if v in p.read_text()]
for name, v in hits:
    print(f"LEAK: {v} on {name}")
print("PASS" if not hits else f"FAIL: {len(hits)} leak(s)")
sys.exit(1 if hits else 0)
```

- [ ] **Step 4: Test the checker** — write a temporary `instructor/tableau/T0/answers.md` with `KEY: test = 9,999.99` and a temporary `docs/tableau/tmp.md` containing `9,999.99`; run `.venv/bin/python scripts/check_tableau_pages.py`; expected `FAIL: 1 leak(s)`, exit 1. Delete both files; run again; expected `SKIP` or `PASS`.

- [ ] **Step 5: Commit** — `git add scripts/check_tableau_pages.py` (the instructor script stays private) and commit "Add leak check for Tableau learner pages".

### Task 2: T1 Tableau fundamentals (lecture, lab, section index, nav)

**Files:**
- Create: `docs/tableau/index.md`, `docs/tableau/T1_fundamentals_lecture.md`, `docs/tableau/T1_fundamentals_lab.md`, `instructor/tableau/T1/answers.md`
- Modify: `mkdocs.yml` (replace the `Tableau (Coming Later)` block)
- Source material: `docs/lessons/class-01.md`, `class-02.md`, private `instructor/sessions/class-01-02/teaching-notes.md`, `docs/lectures/02_data_and_grain_lab.md`, `docs/lectures/04_descriptive_statistics_lab.md`

**Interfaces:**
- Consumes: `t1()` keys from Task 1.
- Produces: the data-source setup steps (connect XLS, Orders sheet, relationship to Returns on Order ID, data-source filter Order Date 2023-01-01 to 2025-12-31, calculated field `Returned Order = NOT ISNULL([Order ID (Returns)])`) that T2–T3 labs refer to by the heading "Set up the Superstore data source" on `T1_fundamentals_lab.md`.

- [ ] **Step 1: Write `docs/tableau/index.md`** — what T1–T4 cover (table from the design), install Tableau Public Desktop, download `sample_-_superstore.xls` from Tableau's sample-data page, the scope rule (2023–2025, as in the Python sessions), "Save to your computer as `.twbx`; publishing is optional and covered in T4", Moodle submission.
- [ ] **Step 2: Write the T1 lecture** — sections: how Tableau reads a table (data source, sheets, fields); dimensions vs measures; discrete vs continuous; aggregation and the level of detail of a view; the Marks card; filter types and order of operations (data source, extract, dimension, measure); Superstore grain recap (one row per order line) with a link to `../lectures/02_data_and_grain_lecture.md`; quiz of 6 questions.
- [ ] **Step 3: Write the T1 lab** — business decision; "Set up the Superstore data source" (exact steps from Interfaces); Core: count rows vs `COUNTD([Order ID])`, returned orders, bar chart of orders by segment with a filter, save `.twbx`; Stretch: histogram of order value (calculated field `{FIXED [Order ID] : SUM([Sales])}` introduced as "order total", explained in T2) and box plot of ship days by ship mode (`DATEDIFF('day', [Order Date], [Ship Date])`); Challenge: find one order by hand and reconcile its lines; evidence list; submission; web-editor note.
- [ ] **Step 4: Write `instructor/tableau/T1/answers.md`** — timing (2 h lecture, 3 h lab), quiz answers, all `t1()` values as `KEY:` lines, marking notes.
- [ ] **Step 5: Update `mkdocs.yml`** — replace the `Tableau (Coming Later)` block with:

```yaml
  - Tableau Sessions:
      - Overview: tableau/index.md
      - "T1: Tableau Fundamentals":
          - Lecture: tableau/T1_fundamentals_lecture.md
          - Lab: tableau/T1_fundamentals_lab.md
```

  Keep `lessons/class-0N.md` files on disk until Task 6 but out of the nav; if `check_docs.py` requires every page in nav, add them under a temporary "Old drafts" entry and remove it in Task 6.
- [ ] **Step 6: Verify** — `.venv/bin/python scripts/check_docs.py`, `.venv/bin/mkdocs build --strict`, `.venv/bin/python scripts/check_tableau_pages.py`; all PASS.
- [ ] **Step 7: Commit** — "Add Tableau T1: fundamentals lecture and lab".

### Task 3: T2 Calculations and KPIs

**Files:**
- Create: `docs/tableau/T2_calculations_kpis_lecture.md`, `docs/tableau/T2_calculations_kpis_lab.md`, `instructor/tableau/T2/answers.md`
- Modify: `mkdocs.yml` (add T2 under Tableau Sessions)
- Source material: `docs/lessons/class-03.md`, `class-04.md`, their private teaching notes, `docs/lectures/05_metrics_and_kpis_*.md`, `docs/lectures/07_trends_and_growth_*.md`

**Interfaces:**
- Consumes: T1 data-source setup (link `T1_fundamentals_lab.md#set-up-the-superstore-data-source`), `t2()` keys.
- Produces: calculated fields `Profit Ratio = SUM([Profit]) / SUM([Sales])`, `Orders = COUNTD([Order ID])`, `Order Total = {FIXED [Order ID] : SUM([Sales])}` used by T3.

- [ ] **Step 1: Write the T2 lecture** — calculated fields (row-level vs aggregate); ratio of sums vs mean of ratios (with `AVG([Profit]/[Sales])` as the wrong version); distinct counts are not additive (order counts by **category** do not add up to total orders, because one order can contain several categories; by segment they do add up, because each order has one segment); table calculations: running total, `LOOKUP` for MoM and YoY, "compute using", why filtering months breaks `LOOKUP` (highlight instead of filter); first LOD expression; quiz of 7 questions.
- [ ] **Step 2: Write the T2 lab** — Core: segment KPI table (Sales, Profit, Profit Ratio, Orders) with a grand total and a reconciliation step; Core: debugging case where `AVG([Profit]/[Sales])` gives a different margin; Stretch: monthly sales trend with MoM and YoY growth; Challenge: orders that appear in more than one category, shown with an LOD; evidence; submission.
- [ ] **Step 3: Write `instructor/tableau/T2/answers.md`** with `t2()` `KEY:` lines (extend `t2()` with category order overlap if the challenge needs it, and re-run Task 1 Step 2).
- [ ] **Step 4: Add T2 to `mkdocs.yml`**.
- [ ] **Step 5: Verify** (same three commands as Task 2 Step 6).
- [ ] **Step 6: Commit** — "Add Tableau T2: calculations and KPIs".

### Task 4: T3 Dashboards

**Files:**
- Create: `docs/tableau/T3_dashboards_lecture.md`, `docs/tableau/T3_dashboards_lab.md`, `instructor/tableau/T3/answers.md`
- Modify: `mkdocs.yml`, `instructor/tableau/compute_answers.py` (add `t3()`)
- Source material: `docs/lectures/14_dashboards_storytelling_*.md`, `docs/foundations/visual-design.md`, `docs/foundations/storytelling.md`, `docs/lectures/12_marketing_campaigns_lab.md` or `11_operations_service_lab.md`, `data/synthetic/marketing-v1/README.md` or `operations-v1/README.md`

**Interfaces:**
- Consumes: T2 calculated fields; synthetic case files from `data/synthetic/<case>/` (learners download them from the repository's GitHub page, as the Python notebooks do).
- Produces: `t3(df) -> dict` with the dashboard's headline values (sales, profit ratio and orders for the latest year and by region).

- [ ] **Step 1: Add `t3()`** to the private script (the values shown on the Session 14 dashboard, plus the synthetic case's headline KPI), re-run it.
- [ ] **Step 2: Write the T3 lecture** — reading order and layout, one message per dashboard, KPI tiles, filters vs actions (filter action, highlight action), colour and accessibility (colour-blind-safe palettes, never colour alone), message titles and annotations, device layouts; quiz of 6 questions.
- [ ] **Step 3: Write the T3 lab** — Core: rebuild the Session 14 decision dashboard (KPI tiles, trend, region bar with a filter action, message title); Stretch: dashboard on the chosen synthetic case; Challenge: critique and fix a deliberately poor dashboard described in the page; evidence; submission (`.twbx` plus dashboard PDF).
- [ ] **Step 4: Write `instructor/tableau/T3/answers.md`**, add T3 to `mkdocs.yml`.
- [ ] **Step 5: Verify** (three commands).
- [ ] **Step 6: Commit** — "Add Tableau T3: dashboards".

### Task 5: T4 Publishing and portfolio

**Files:**
- Create: `docs/tableau/T4_publishing_portfolio_lecture.md`, `docs/tableau/T4_publishing_portfolio_lab.md`, `instructor/tableau/T4/answers.md`
- Modify: `mkdocs.yml`
- Source material: `docs/lectures/15_capstone_studio_*.md`, `docs/lectures/16_executive_briefings_*.md`, `planning/PROJECT_CONTEXT.md` (Tableau Public privacy notes and official FAQ links)

- [ ] **Step 1: Write the T4 lecture** — what Tableau Public publishes (workbook and data are public, downloadable unless disabled), what is safe to publish (synthetic or public data only, never workplace data), hiding views and disabling downloads, `.twbx` versioning (file names with dates, a change log), story points, portfolio writing (question, evidence, limitation, action); quiz of 6 questions.
- [ ] **Step 2: Write the T4 lab** — Core: a portfolio piece from the learner's capstone (one dashboard and a three-point story), saved locally; Stretch: a version log and an accessibility check; Challenge (optional): publish to Tableau Public after a privacy checklist; submission.
- [ ] **Step 3: Write `instructor/tableau/T4/answers.md`** (timing, quiz answers, marking notes; no `KEY:` values needed), add T4 to `mkdocs.yml`.
- [ ] **Step 4: Verify** (three commands).
- [ ] **Step 5: Commit** — "Add Tableau T4: publishing and portfolio".

### Task 6: Retire old drafts and update cross-references

**Files:**
- Delete: `docs/lessons/class-01.md` … `class-04.md` (`git rm`)
- Modify: `mkdocs.yml`; any page linking to `lessons/class-0N.md` (find with `grep -rn "class-0" docs/ notebooks/*.ipynb`); `docs/index.md` and `docs/course/roadmap.md` mentions of the Tableau section ("coming later" wording); `planning/COURSE_PLAN.md` Part F status; `planning/TASKS.md` (L01–L03 superseded by T1–T4), `planning/STATUS.md`, `planning/HANDOFF.md`, `planning/DECISIONS.md` (new DEC: Tableau T1–T4 structure, Tableau Public, Chrome rehearsal).

- [ ] **Step 1:** Replace each link to an old draft with the matching T-session page.
- [ ] **Step 2:** `git rm docs/lessons/class-0{1,2,3,4}.md`; keep `lesson-template.md` only if still in the nav and useful, otherwise remove it from the nav too.
- [ ] **Step 3:** Update the planning records listed above.
- [ ] **Step 4: Verify** (three commands) and `grep -rn "class-0" docs/` returns nothing.
- [ ] **Step 5: Commit** — "Retire draft Tableau lessons; link the T1–T4 sessions".

### Task 7: Rehearse in Tableau Public (Chrome) and add screenshots

Needs the user at the keyboard for sign-in.

**Files:**
- Create: `docs/tableau/img/Tn_<step>.png`
- Modify: the four lab pages (screenshots, corrected click paths, web-editor notes), `instructor/tableau/Tn/answers.md` (rehearsal record: date, Tableau Public web version shown, pass/fail per value), `planning/TASKS.md` (D03 closure)

- [ ] **Step 1:** Load the Chrome tools, `tabs_context_mcp`, open a new tab at `https://public.tableau.com`. Ask the user to sign in themselves.
- [ ] **Step 2:** Ask the user to approve uploading `sample_-_superstore.xls` to web authoring ("Create a viz"). Do not save the workbook.
- [ ] **Step 3:** For each lab in order T1 → T3, follow the Core steps exactly as written; read each displayed value; compare with the `KEY:` values; record pass/fail. When a step fails because the page is wrong, fix the page; when the web editor differs from the desktop app, add a `!!! note "Web editor"` line instead of changing the desktop path.
- [ ] **Step 4:** Capture screenshots of key states (data source with relationship, first chart, KPI table, growth view, dashboard). The Chrome screenshot tool shows images to the agent but may not write files; to save a file, bring the Chrome window to the front and run `screencapture -x -R<x>,<y>,<w>,<h> docs/tableau/img/Tn_<step>.png` (macOS), or ask the user to save the screenshot. Save as `docs/tableau/img/Tn_<step>.png`, reference them in the lab pages with alt text. Screenshots must not show the user's account name or profile; crop or skip if they do.
- [ ] **Step 5:** Close the tab without saving. Confirm nothing was saved to the user's Tableau Public profile (ask the user to check if unsure).
- [ ] **Step 6: Verify** (three commands) and record D03 closure in `planning/TASKS.md` with the values compared.
- [ ] **Step 7: Commit** — "Rehearse Tableau labs in Tableau Public and add screenshots". Ask the user before pushing.

---

## Self-review notes

- Spec coverage: structure (Tasks 2–5), edition and web note (Global Constraints, Task 2–4 labs), verification in Chrome with no saving or publishing (Task 7), old drafts reused then removed (Tasks 2–3 sources, Task 6), expected values private (Task 1, `answers.md`), no numbers on pages (leak checker), D03 closure (Task 7).
- Assumption to confirm in Task 1: each Superstore order has one segment (true if `df.groupby('order_id').segment.nunique().max() == 1`); if not, adjust the T2 lecture's non-additivity example.
