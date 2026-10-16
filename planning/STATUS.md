# Project status

Updated: 2026-10-12 (Asia/Kathmandu). **Phase: foundation, source audit, D01 retail contract and D02 preparation complete. D03 numerical validation passed; Tableau worksheet checks remain open. Full lesson production has not started.**



## Claude session: Sessions 5 and 7 completed, D08 built — 2026-10-14

New lecture notebooks for Sessions 5 and 7; their labs restructured into Guided/Independent/Challenge with new tasks (Berkeley admissions, metric contract, construction spending) and "draft" removed; answers in `instructor/sessions/05/` and `07/`. D08 synthetic marketing data (campaign-day funnel, 2,555 rows; A/B test, 60,000 visitors) with generator, independent validator, README contract, manifest and private reference answers (DEC-046). Fixed a numpy/pandas DeprecationWarning that printed a local temp path in Session 6 outputs. Verification: `run_notebooks.py --check-data` on all 14 notebooks (no errors; PASS, 11 share one setup cell); `validate_marketing.py` PASS; `make convert-all`; no warnings or local paths in outputs; `check_docs.py` PASS (30 pages); strict MkDocs build clean. Not done: independent review, Colab trial.

## Claude session: Sessions 3, 4 and 6 built — 2026-10-14

Built lecture + lab notebooks and private answers for Session 3 (cleaning and preparing), Session 4 (descriptive statistics) and Session 6 (visualisation principles), DEC-045 naming. World Cup, Mobile OS and US home sales are downloaded inside the notebooks from Tableau's catalog and checked by SHA-256 (live files byte-identical to the preserved raw copies); nothing is bundled, consistent with SOURCE_RIGHTS. Added nav, roadmap and notebooks/README entries. Verification: `run_notebooks.py --check-data` on all 12 notebooks (no errors; PASS, 9 notebooks share one setup cell, 6,815 rows / 3,388 orders); `make convert-all`; `check_docs.py` PASS (28 pages); strict MkDocs build passed with no warnings. Session 7 output differed only in print-stream chunking and was restored. Not done: independent review, Colab trial.

## Claude session: Sessions 1 and 2 built — 2026-10-14

Built Session 1 (`01_why_data_analytics_lecture/lab.ipynb`) and Session 2 (`02_data_and_grain_lecture/lab.ipynb`) with quizzes and private answers in `instructor/sessions/01/` and `02/` (DEC-045). Renamed draft labs to `05_metrics_and_kpis_lab.ipynb` and `07_trends_and_growth_lab.ipynb` and fixed their titles, badges and links. Updated nav, roadmap, index, setup, Tableau draft links and notebooks/README. Verification: `run_notebooks.py --check-data` on all six notebooks (no errors; data check PASS, 4 notebooks share one setup cell, 6,815 rows / 3,388 orders); nbconvert of the six; `check_docs.py` PASS (27 pages); strict MkDocs build passed (INFO lists the five orphaned old lesson pages). Then, with user approval, deleted superseded notebooks 00–02 and old pages 00–04 and committed. Not done: independent review, Colab trial, push.

## Claude session: China classroom Days 4, 5 and 7 — 2026-10-16

Agents built Day 4 (regression and text-features lectures, Assignment 2), Day 5 (financial modelling and Excel simulation lecture with a synthetic practice workbook, Lab 5) and Day 7 (course review, capstone Assignment 4, private final exam and key). The Day 6 agent was stopped before writing files. Verification: all seven notebooks re-executed with unchanged sha256; no local paths, internet loaders or exam text in public files; `check_docs.py` PASS (72 pages); strict build PASS.

## Claude session: China classroom Day 3 — 2026-10-15

An agent built Day 3: text mining and forecasting lectures, Applied Labs 3 (VADER on bundled lexicon) and 4 (CO₂ seasonal ARIMA), and a private 100-mark, 90-minute midterm with key in `instructor/china_classroom/D3/`. User confirmed public own-words lab pages, same-day lab deadlines and offline PDF merging (DEC-053; guidance added to `docs/china/setup.md`). Verification: D3 notebooks re-executed with unchanged sha256, no local paths or internet loaders, strict build PASS.

## Claude session: China classroom restructured to WUT, Days 1–2 — 2026-10-15

The user named the WUT syllabus as authoritative (DEC-052). Python basics and Activity 1 became pre-class (`00_preclass_*`). Two agents built Day 1 (EDA lecture, Lab 1 diamonds; morning lecture's course map updated to WUT weights) and Day 2 (visualisation/communication and Tableau lectures, Lab 2 dashboard, Assignment 1 tips report) with private answers in `instructor/china_classroom/D1,D2/`. Verification: all 10 China notebooks re-executed with unchanged sha256; no local paths or internet loaders; `check_docs.py` PASS (61 pages); strict build PASS. Nav and schedule links updated.

## Claude session: China classroom data bundle and Day 1 — 2026-10-15

User answers: deadlines as proposed (China time), GAP = Moodle, Tableau student licence, Microsoft Excel, we write the midterm. Bundled offline data in `notebooks/China_Classroom/data/` (penguins, diamonds, tips, mpg from seaborn-data; Datasaurus CSV from the preserved rda; NLTK `vader_lexicon`, `stopwords`, `punkt_tab`; 7.0 MB) with `SOURCES.md` and checksums. Offline NLTK was tested with `punkt_tab` only, skipping the 14 MB `punkt`. `run_notebooks.py` now runs each notebook from its own folder. Added the China packages to requirements.txt and the repo brief `planning/agents/china-notebook-author.md`. An agent built Day 1: setup check, two lectures and the Activity 1 lab, plus private answers. Its first run died on a network error and was resumed. The China nav section had been removed from mkdocs.yml (the file matched HEAD) and was re-added with the Day 1 pages. Verification: all 4 notebooks re-run byte-identically, no internet loaders or local paths, strict build PASS (55 pages), private answers and extracted punkt_tab ignored.

## Claude session: DATA 300 China classroom planned — 2026-10-15

Read the 73-page DATA 300 syllabus (text extracted locally with pypdf into the project .venv; the PDF is not committed). The user gave the timetable and four choices: local Jupyter, ending Thu 19 Nov, Tue late block = lab with a Wednesday dinner break, syllabus labs graded as written with our material for teaching. Wrote `planning/china_classroom/PLAN.md` (period budget, day-by-day mapping of 8 syllabus weeks to 7 days, reuse map, risks), learner pages `docs/china/{index,schedule,setup}.md` and `notebooks/China_Classroom/README.md`, and added the nav section. `check_docs.py` PASS (51 pages); strict build PASS.

## Claude session: logistics confirmed — 2026-10-15

The user confirmed R01 logistics (DEC-050): 21–40 learners, in person, Moodle submissions, individual feedback-only briefings in two parallel rooms. The user declined a Colab trial and deferred the Tableau section. Updated the setup page (laptops, Google account, Moodle login, how to download .ipynb from Colab and upload to Moodle, file naming), the roadmap assessment wording, the home page and private Session 16 facilitator notes (two-room schedule). No notebook changed. Verification: `check_docs.py` PASS (48 pages), strict MkDocs build PASS. User approved commit and push.

## Claude session: Sessions 14–16, all Python sessions drafted — 2026-10-15

User approved commit and push of Sessions 8–13 (`c5bf5b4`, pushed; live data hashes on GitHub verified equal to local; private answers return 404). Built Session 14 (dashboards and storytelling) and Sessions 15–16 (capstone studio, executive briefings) with two agents. Both hit the API session limit and were resumed. A second temp cleanup wiped the /tmp venv and the scratchpad brief. The lead moved the brief into `planning/agents/notebook-author.md` and the environment into the gitignored project `.venv` (Python 3.12, from requirements.txt).

Verification over all 32 notebooks: five data loaders, each identical everywhere it is used; no errors, stderr, local paths or missing badges; full re-execution byte-identical; `--check-data` PASS (18 Superstore notebooks); `make convert-all` reproduced all pages; `check_docs.py` PASS (48 pages); strict MkDocs build PASS; no private content in the site. Agents report reference matches for marketing, operations, HR, finance and Challenger figures. Rubric weights confirmed by the user (DEC-049). User approved commit and push. Open: a real Colab trial, novice timing.

## Claude session: business cases (Sessions 10–13) and data D05/D07 — 2026-10-15

Built Sessions 10 (finance), 11 (operations), 12 (marketing) and 13 (HR), lecture + lab + quiz + private answers, using four case/data-designer agents with exclusive files. The lead built operations-v1 and hr-v1 generators and validators. Tuning found and fixed: an unrealistic first operations draft (59% on-time, no visible trap); a generator bug where same-month hires never created employees; replacement roles opened after the cutoff (caught by the validator); and the HR README opening-headcount wording. Incidents: a temp cleanup wiped `/tmp/kings-*` (the venv) and the scratchpad, including the shared agent brief, mid-run. The lead recreated the venv from requirements.txt and restored the brief; two agents briefly worked without it and later conformed. Two agents hit the API session limit and were resumed after the reset.

Verification: each dataset's setup cell is identical across its notebooks (5 loaders, 1 variant each); all 26 notebooks re-executed byte-identically; `--check-data` PASS; `make convert-all` reproduced every page; `check_docs.py` PASS (42 pages); strict MkDocs build PASS; no instructor content in the built site; `instructor/` still ignored. Agents report every case number matches the private references. Not verified: live Colab downloads for finance-v1, operations-v1 and hr-v1 (not yet pushed to GitHub), a real Colab run, novice timing.

## Claude session: review, Sessions 8–9 and finance data — 2026-10-14

Reviewed the previous session's Sessions 1–7 and D08 by re-running everything from a fresh environment: marketing generator + validator PASS (byte-identical); all 14 notebooks executed, data check PASS; `make convert-all` output identical except two pages. The kernel had split printed output into chunks unpredictably; fixed in `run_notebooks.py` by merging stream outputs, after which re-runs match the committed files exactly. Wording scan found only legitimate uses of "margin"/"return rate".

Built Session 8 (correlation and regression) and Session 9 (sampling, uncertainty and experiments) lecture + lab notebooks with quizzes and private answers, using two parallel case/data-designer agents with exclusive files. They share one verbatim marketing setup cell that downloads marketing-v1 from the public repo with SHA-256 checks. The lead fixed the Session 8 → 9 link and README titles. Results checked against private references: company spend–revenue slopes 9.23 / 2.64, campaign totals, A/B conversion 3.15% vs 3.64%, lift +0.50 points, CI +0.21 to +0.79, p 0.0008, device splits. Session 9 shows openly that formula CIs under-cover for skewed order values.

Built D04 synthetic finance data (`finance-v1`, DEC-047) with generator, standard-library validator and private reference answers.

Verification: all 18 notebooks executed twice, byte-identical, data check PASS (14 share the Superstore setup cell); no errors, stderr or local paths in Session 8–9 outputs; `make convert-all`; `check_docs.py` PASS (34 pages); strict MkDocs build PASS; no private answers in the built site. Not verified: a real Colab run of Sessions 8–9 (marketing data download works because it is on GitHub), novice timing.

## Claude session: course plan v2 — 2026-10-14

User asked for a rigorous course with theory and hands-on practice and gave three answers: 2-hour lecture + 3-hour lab per session; applied statistics for analysts; Lecture/Lab shown on pages without hours (DEC-044). Wrote `planning/COURSE_PLAN.md`, covering session format, outcomes, 16 Python sessions in five parts plus 4 Tableau sessions, per-session lecture and lab content, data plan, assessment and a mapping of existing material. Rewrote the learner roadmap to match, without hours. Marked CURRICULUM.md as superseded for structure. Added the session production backlog to TASKS. No notebooks changed. Verification: `check_docs.py` and strict build (below).

## Claude session: single requirements file and commit — 2026-10-14

Merged the three extra requirement files into one sectioned `requirements.txt` (DEC-043) and updated every reference (README, data/README, notebooks/README, AGENTS, CLAUDE_TAKEOVER, HANDOFF, script docstrings). Verification in a fresh uv venv (Python 3.12.13) from the merged file:

- `make_foundation_figures.py`, `run_notebooks.py --check-data` and `make convert-all` all ran, and every SVG, notebook and converted page was byte-identical to the committed state.
- `check_retail_contract.py` and `prepare_retail.py` passed.
- `validate_retail.py` refused, as designed, because its private reports record Python 3.12.14. In a second fresh venv on Python 3.12.14 from the same file it passed and re-verified both private reports byte-identically.
- `check_docs.py` and the strict MkDocs build passed.

The user then asked to commit.

## Claude session: notebooks become the source (DEC-042) — 2026-10-13

The user clarified they want `.ipynb` notebooks and already convert them with the Makefile. Changes:

- Converted the five lessons into `notebooks/00_python_and_colab_basics.ipynb`, `01_decision_to_evidence`, `02_trust_the_sales_table`, `03_segment_comparison` and `04_trends_returns_dashboard`. Admonitions became blockquotes; each notebook opens with an Open in Colab badge pointing to the public repo `Aayush181509/AnalyticsLecture`; each exercise has a "Your turn" note.
- Added `scripts/run_notebooks.py`, which executes notebooks in place with nbclient and checks the data. Ran `make convert-all` unchanged (jupyter from a Python 3.12 venv), producing `docs/lectures/*.md` and `*_files/*.png`.
- Removed the superseded custom pipeline (`scripts/build_python_lessons.py`, `notebooks/src/`, `docs/python/`, `docs/notebooks/`, `docs/assets/python/`). `requirements-lessons.txt` was replaced by `requirements-notebooks.txt`.
- Navigation now points Python Lessons to `docs/lectures/`. The setup page explains the Open in Colab button. CSS added for pandas tables (horizontal scroll) and blockquote callouts.
- Verification: run_notebooks executed all 5 notebooks (85 code cells, no errors). `--check-data` PASS (shared setup cell in 4 notebooks; 6,815 rows / 3,388 orders match the CSV). Re-execution was byte-identical. `make convert-all` succeeded. `check_docs.py` PASS (21 pages); strict build PASS; image paths resolve in the built site.
- Side effect found and reverted: an `ipykernel install --user` briefly created `~/Library/Jupyter/kernels/python3` pointing to the temporary venv. It was created in this session (the `kernels/` folder did not exist before) and was removed, leaving only the pre-existing `runtime/`.
- Not verified: Open in Colab links (the notebooks are not on GitHub until pushed), an actual Colab run, novice timing.

## Claude session: Python-first lessons — 2026-10-13

User switched the teaching path to Python (DEC-041; choices: Google Colab, read-run-modify, Tableau drafts kept as a later section).

- Pipeline: `scripts/build_python_lessons.py` + `notebooks/src/_setup.py` + `notebooks/src/lesson00–04.py` → `docs/python/lesson-00–04.md` (real executed outputs, 11 SVG charts in `docs/assets/python/`) and output-free `docs/notebooks/lesson-00–04.ipynb`. Lesson 0 (Python/Colab basics) and Lesson 1 were written by the lead. Lessons 2–4 were written by three parallel case/data-designer agents with exclusive files. Their sessions ended before they reported, so the lead rebuilt everything from scratch and reviewed it. Fixes: integer columns no longer display as decimals; the dashboard returns-share is shown as a percent; a raw legend label was replaced; a seasonal title reworded.
- Navigation: Python Lessons section; Tableau drafts moved to "Tableau (Coming Later)" with banners linking to the Python versions. Home, setup (Colab), roadmap (Stage 1 Python, Stage 4 Tableau), Foundations wording, the Anscombe exercise (now Python) and the lesson template were updated.
- Verification, actually run: builder `--check-data` PASS (the loader reproduces all 6,815 rows / 3,388 orders and every value of the validated CSV); two consecutive builds byte-identical (md, ipynb, svg); executed every code cell of all five downloadable notebooks in order, exercise cells included: 85 cells, no errors; the setup cell in an empty folder downloaded the live Tableau file and its SHA-256 matched (no warning); generated outputs checked against `reference_answers.json` (segment KPIs, overall AOV/ratio, returns 191 vs 511 lines, category 4,779, Jan 2025 MoM −75.1% / YoY +2.0%, Dec 2025, returns shares by segment); scan found no hand-typed result numbers, "margin", "return rate" or currency labels in lesson markdown; chart PNG previews inspected; `check_docs.py` PASS (21 pages); strict MkDocs build PASS; notebook download links resolve in the built site.
- Environments: the temporary docs venv had been wiped and was recreated with uv (Python 3.12, MkDocs 1.6.1, from requirements.txt). The lesson venv `/tmp/kings-python-lessons-venv` uses Python 3.12.13, pandas 2.2.3, matplotlib 3.11.2, xlrd 2.0.2, tabulate 0.10.0. pandas 2.2.3 segfaults on Python 3.14, hence 3.12.
- Not verified: an actual Google Colab session (local execution simulated it), novice timing, private answers for the Python exercise cells.

## User-authorized Git commit (Claude session) — 2026-10-12

User asked to commit everything so far. All Claude-session work is in one local commit: readability styling, Foundations module and figures, Lessons 1–4 drafts and private notes, planning updates. The commit also includes the previously untracked Makefile, `scripts/fetch_catalog_sources.py`, the `retrieved-2026-10-12` raw copies (byte-identical to the committed Codex copies, so Git stores each blob once) and the Datasaurus/Challenger inputs. By user choice the 49 MB CrunchBase workbook is excluded and listed in .gitignore, because its provider terms apply. graphify-out/ stays ignored. Pre-commit: docs checker PASS, strict build PASS. Staged whitespace check passes except two known generated/original artifacts: the original CRLF Mobile OS CSV (same bytes as the committed copy) and matplotlib SVG path output. No push.

## Claude session: Lessons 3–4 drafts — 2026-10-12

Wrote `docs/lessons/class-03.md` (segment comparison) and `docs/lessons/class-04.md` (trends, growth, returns list, dashboard), plus private `instructor/sessions/class-03/` and `class-04/` teaching notes (DEC-040). Lesson formulas follow the frozen metric-contract candidates; reference values in the notes come from `reference_answers.json`. The lead derived the debugging values (mean of segment ratios 13.14% vs 12.42%; Sales ÷ rows 231.98 vs AOV 466.64) and the annual Sales sums by Decimal arithmetic on that JSON. Seasonality claims (Sep/Nov/Dec peaks, Jan/Feb lows) and the Jan 2025 MoM −75.1% / YoY +2.0% case were checked against all 36 monthly records. Verification: docs checker PASS (16 pages); strict build PASS, no warnings; no instructor/planning paths in the built HTML; learner pages contain none of the segment reference values. Not verified: any Tableau execution, including LOOKUP growth behaviour, grand-total recomputation, filter actions and display field names.

## Claude session: Foundations module and content-first framing — 2026-10-12

- Added `docs/foundations/` (DEC-038): why analytics matters (Snow, Nightingale, Moneyball, Walmart, Google Flu Trends; four levels of analytics), statistics are not enough (Anscombe table and raw data, Datasaurus Dozen), how statistics mislead (ice cream/crime confounder, spurious correlations, Berkeley 1973 Simpson's paradox, truncated axes, cherry-picking, mean vs median, base rates, survivorship bias, checklist), types of analysis (uni/bi/multivariate with chart guide), designing clear visuals (data-ink, pre-attentive attributes, Gestalt, colour, checklist), storytelling with data (Challenger, big idea, situation–complication–resolution, exploratory vs explanatory). Every page ends with exercises.
- Figures: `scripts/make_foundation_figures.py` writes ten SVGs to `docs/assets/foundations/` (palette checked with the dataviz validator: blue/orange/aqua pass CVD and normal-vision checks; aqua below 3:1 contrast so it is only used with a legend). Two consecutive runs produced byte-identical SVGs. PNG previews of all ten were inspected; fixed a squeezed Datasaurus grid, gridlines drawn over bars and an overlapping legend. Inputs preserved: `data/raw/datasaurus-dozen/retrieved-2026-10-12/` (datasaurus_dozen.rda SHA-256 768b14e0…, MIT LICENSE.md ccc428c6…) and `data/raw/challenger-o-rings/retrieved-2026-10-12/o-ring-erosion-or-blowby.data` (7f38e97b…, UCI). Datasaurus summary statistics recomputed from the file (means 54.26–54.27 / 47.83–47.84, sd 16.76–16.77 / 26.93–26.94, r −0.06 to −0.07). Anscombe values are published constants; Berkeley rates are the published 1973 figures; ice cream, axis, data-ink and analysis-type charts use labelled synthetic data.
- Content-first framing (DEC-039): removed "twelve two-hour classes", practice-hour, minute and week references from all learner pages; roadmap reorganised into Stage 0–3 content stages; "Class N" lessons renamed "Lesson N".
- Verification: `check_docs.py` PASS (14 pages); strict MkDocs build PASS, no warnings; built HTML shows all images and admonitions, no raw admonition syntax, no instructor/planning paths; grep finds no remaining session/hour framing in docs/. Independent read-only reviewer (general-purpose agent, reviewer brief) recomputed the Anscombe, Datasaurus, Challenger, salary, correlation and figure claims and checked historical claims from knowledge (no web search). Fixed: bivariate panel now plots the same points as the multivariate panel; Tableau Anscombe exercise now turns off Aggregate Measures; John Snow story corrected (handle removed after his investigation, map drawn afterwards); Google Flu Trends cause stated per Lazer et al.; Datasaurus values rounded consistently in text and figure; Challenger duplicate points separated; pre-attentive demo uses colour only; Berkeley alt text and "all departments" row clarified; data-ink "after" panel keeps its unit; plus nits (Anscombe variance 4.13, Cairo and Knaflic credits, "plausibly driven", Wald "as usually told", lowest payroll, skewed histogram with median 3 vs mean ≈4). Figures regenerated byte-identically twice and changed ones re-inspected as PNG previews; docs checker and strict build PASS. Not done: Claude's own browser screenshot review (extension not connected). Follow-up after user review: "How statistics can mislead" lacked figures for sections 4–7; added cherry-picking, mean-vs-median, base-rate and survivorship figures (synthetic/simplified, labelled), now 14 SVGs regenerated byte-identically twice and previewed; build PASS.

## Claude session: Class 1–2 drafts (L01) — 2026-10-12

At the user's choice (DEC-037), wrote draft learner pages `docs/lessons/class-01.md` (decision to question, connect CSV, types, first chart, filter, save/reopen, rows vs orders) and `docs/lessons/class-02.md` (data dictionary, grain, COUNTD orders, returns-list limits, hand-checked order, preparation log, Segment vs Category overlap, debugging challenge), in the approved Read the Docs readability style. Added a "Classes" nav section and links from home and roadmap. Private `instructor/sessions/class-01-02/teaching-notes.md` holds facilitation notes, expected values cited to `reference_answers.json` keys and a rehearsal checklist.

Verification: `check_docs.py` PASS (8 pages); strict temporary MkDocs build PASS, no warnings; built HTML contains no instructor/planning/reference paths; learner pages contain none of the reference numbers (6,815 / 3,388 / 191 / 511). Field names, scope dates, 34 lines shipping in 2026, segment partition and category overlap were checked against the frozen dictionary and reference JSON. Not verified: any Tableau click path, field display name, `(Count)` field name or local save in the installed Tableau Public; novice timing; learner devices.

## Claude session: learner site readability — 2026-10-12

User requested easier-to-read, less compact MkDocs pages (DEC-034). Codex had committed `502dc1d` and the working tree was quiet before edits began.

- Theme briefly switched to Material; user then preferred the previous look, so Read the Docs is restored (DEC-036). `docs/stylesheets/readability.css` targets that theme: 820px width, 16px/1.75 text, spaced headings, section rules, wrapping padded tables, roomier admonitions.
- Rewrote all six learner pages for scanning: one-line lead, `---` section breaks, numbered steps, one subsection per case, bullet overviews, three-stage roadmap tables, admonitions for status/safety/tips, evidence-log table. Substance, provisional labels and boundaries preserved; no instructor/planning links.
- AGENTS.md, DOCUMENTATION_PLAN.md, CLAUDE_TAKEOVER.md and requirements.txt updated for the new theme and page style.

Verification actually performed: `python3 scripts/check_docs.py` PASS (6 pages); `/tmp/kings-data-docs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/data-analytics-site-check` PASS, no warnings, re-run after the theme revert; generated HTML inspected: Read the Docs theme, admonitions (note/tip/hint/warning) and tables render on every page where intended, readability.css linked, no leftover raw `!!!`/`===`/`:material-` syntax, no instructor/planning paths; `git diff --check` clean. Rendered review: user viewed the Read the Docs version and approved it ("Yes, it looks much better"); Claude did not take its own screenshots (Chrome extension not connected). Not performed: and any D03 Tableau work (no desktop-app control, DEC-035). Docs venv also has mkdocs-material 9.7.7 installed from the trial; it is no longer required. Retail artifacts re-verified unchanged with the documented Codex-runtime commands: `check_retail_contract.py`, `prepare_retail.py` (byte-verified existing outputs, CSV SHA-256 434ba08a…) and `validate_retail.py` all PASS.

## User-authorized Git checkpoint — 2026-10-12

The user requested a local commit of the changes made for this course. This checkpoint records course planning/learner previews, shared guidance/Claude handoff, audited source snapshots and metadata, preparation/validation scripts and private development references. Existing .gitignore lines are retained with our environment/cache additions. Unrelated Makefile, separate fetch script, duplicate source layouts/extra datasets and graphify-out/ remain unstaged and untouched. No push or deployment is requested or performed. Use `git log -1` for the resulting commit identity; historical sections below describe the earlier uncommitted development state. Production statuses and outstanding Tableau checks are unchanged. Pre-commit documentation and numerical validation passed. Staged whitespace inspection reports original CRLF endings in Mobile OS CSV and an existing final blank line in the hash-recorded private hand-check Markdown. Preserve those exact bytes; the staged check excluding these two known artifacts passes. All staged blobs were compared with workspace bytes.

## Latest development step and Claude takeover — 2026-10-12

The user requests Claude takeover after this work. [CLAUDE_TAKEOVER.md](CLAUDE_TAKEOVER.md) is the concrete continuation brief; CLAUDE.md/README/HANDOFF point to it. Earlier sections below preserve historical evidence and their then-current limitations; this section supersedes their next-action statements.

- **D02 DONE for local development.** `scripts/prepare_retail.py` runs frozen-contract preflight, derives whole-source customer conflicts before date scope, and writes immutable CSV/manifest/report/private exceptions. CSV: 6,815 lines, 3,388 orders, 22 fields, 36 months; customer-eligible 6,811 lines/3,387 orders. All 149,930 typed values matched. Thirty-four lines shipping beyond the Order Date window remain. Repeat generation preserved bytes and modification times.
- **D03 numerical slice PASS; task IN PROGRESS for Tableau.** `scripts/validate_retail.py` independently reads raw through pandas and saved CSV through DictReader/Decimal, without preparation/checker imports. Every typed value matched; seven frozen hashes, source/preparation/output identities, private controls, two-line source hand arithmetic, population bridges, group totals, weighted ratios/return denominators/category overlap and calendar growth checks passed. Two private reports were repeated byte-identically; lead reran successfully. Ratios expose exact numerators/denominators and use Decimal precision60 for repeating expansions.
- Private references/evidence: `instructor/solutions/superstore/retail-v1/{preparation_exceptions,reference_answers,numerical_validation}.json`. The numerical report explicitly says PASS_NUMERICAL_ONLY, Tableau=false, publication=false. These are not classroom-ready answer packs. Prepared metadata also has diagnostic controls/private paths; do not distribute the directory wholesale.
- **Tableau import only.** Installed native Tableau Public loaded the exact CSV via Text file and displayed 22 fields/6,815 rows. Observed Order ID as string, dates as dates, flags/interval as numbers. Worksheet navigation failed with native app-control `noWindowsAvailable` errors; refreshing the handle still showed the source, then the tool reported an application change. No worksheet KPI/filter/grand-total/empty/zero-case, installed-version or save/reopen check completed. No reference workbook saved; no public upload. Welcome-page update text is not installed-version evidence.
- Case/data worker owned preparation; pilot/reviewer owned independent numerical validator/reports; curriculum reviewer read-only accepted D02 and independently checked identities/schema/counts/coverage. Lead reviewed integration, reran the numerical validator and attempted the local app check. No blocking preparation defects found. Immutability refusal was code-reviewed, not tested by corrupting the output.

Actual data commands in the existing audited environment:

```bash
PYTHONPATH=/tmp/kings-source-audit-libs /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/prepare_retail.py
PYTHONPATH=/tmp/kings-source-audit-libs /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/validate_retail.py
```

Both PASS. Preparation invokes the read-only frozen checker first. Runtime: Python3.12.14/xlrd2.0.2, independent validator pandas2.2.3, Decimal precision60. The persistent `.venv-data` setup recipe is documented but not separately installation-tested. Temporary dependencies may expire; differing runtime metadata must not be resolved by overwriting immutable versions.

| Identity | SHA-256 |
|---|---|
| CSV | `434ba08abf665b617294b188e38c0d0b8a86d0b3386d41eff8a42c15bc708de2` |
| Preparation manifest | `1b662f9ec2628de3244d26c7f9152db56a38350a4eb9fb1ad9d9a46b999cc844` |
| Independent reference answers | `96c35dcf8449386fae5f4978bc86a23966594d1ddda51feb4d93eee046d1c929` |
| Numerical validation report | `53e8be7c59d63fbe15f4d9c24291dfbb9ccbe909c68fb8ba2d70632206dceec0` |

**Next concrete task:** close D03's remaining local Tableau comparisons with recorded app version and evidence, then L01/L02 after relevant R01 defaults. Keep S3 source-backed Segment metrics distinct from the retained synthetic pilot. Full lessons, synthetic generators, notebooks, learner-device/classroom/timing/accessibility/visual checks and permitted learner/public delivery remain future work. No deployment/commit/public upload performed. Raw sources, frozen inputs, existing site/ and unowned extra work preserved.

Final integration verification: `python3 scripts/check_docs.py` PASS (six learner pages); `/tmp/kings-data-docs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/data-analytics-site-check` PASS without warnings; local inline-link/whitespace scan PASS across41 selected project Markdown files. Python syntax/retail JSON parse, all seven frozen hashes, four original byte/hash identities and exact LEGACY_HOME bytes PASS. Twelve120-minute budgets,19h essential practice and100% proposed rubric rechecked. `git diff --check` PASS; status inspected and all work left uncommitted. Remote URLs/anchors/reference-link syntax, browser layout, Tableau worksheet calculations and teaching/device trials are outside these checks.

## Foundation completion (before source audit)

- Inspected repository/instructions/tooling, recorded inventory and preserved original home exactly in LEGACY_HOME.md. Existing Makefile and generated site/ preserved; existing ignore patterns retained with local environment/cache additions.
- Captured four user answers:12×2h live + practice; basic spreadsheets, no Tableau/Python; Tableau Public synthetic/public data; practical portfolio/executive briefing.
- Integrated eight observable outcomes, exact 120-minute class budgets, meaningful five-domain portfolio, recommended rubric and alternative pacing. Essential practice is recommended 19h (43h including class); expanded route about 25h practice is optional and unverified.
- Created all five case briefs with activity/validation/solution specifications, planned source/prepared schemas and explicit metric contracts. No external data adopted.
- Detailed S3 retail pilot, learner lesson template, internal instructor structure and future MkDocs navigation. Growth/returns reserved explicitly for S4.
- Created README, shared AGENTS, concise CLAUDE entry, five reusable role briefs, prioritized dependencies, decisions and handoff.
- Three bounded workers executed curriculum/assessment, case/data and pilot/template tasks. Pilot worker subsequently reviewed other authors' designs; lead independently integrated and reviewed all outputs. Role documents do not imply additional agents ran.
- Resolved analytic/integration findings: finance comparable totals, shipment cutoff/date rules, HR historical boundaries, cumulative refunds/cost recovery, three-domain capstone consistency, single-campaign synthetic attribution, S3 scope and practice load. Review report records findings and remaining release gates.

## Verification actually performed

| Check | Outcome / limits |
|---|---|
| `python3 scripts/check_docs.py` | PASS:6 learner Markdown pages; inline local links/nav targets/docs-only boundary. Remote URLs, fragments and reference-link syntax not exhaustively checked. |
| `/tmp/kings-data-docs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/data-analytics-site-check` | PASS with no warnings; temporary output protects existing site/. |
| Python design assertions |12 sessions; each120min;1,440 total contact min =24h; essential practice19h; rubric weights total100%. Reviewer also checked synthetic hand-reasoned HR date-boundary cases; these are formula sanity checks, not real-dataset validation. |
| Generated HTML structural inspection |8 HTML files with titles; course pages have H1s; no planning/instructor/notebook source paths copied. This is not browser visual QA. |
| Original-home byte comparison |LEGACY_HOME.md exactly equals pre-edit `git show HEAD:docs/index.md`; SHA256 `93f6983584e68e962ff3b88f10b5c945dae6c909b773656de6fa9f444d9b0eee`. |
| `git diff --check`; new Markdown whitespace scan; `git status --short` |Tracked diff clean; new Markdown checked separately; changes left uncommitted for review. |
| Official source checks |Tableau Public saving/FAQ and MkDocs configuration consulted; links in PROJECT_CONTEXT/setup/DOCUMENTATION_PLAN. No external dataset source or license adopted. |
| Browser visual review attempt |In-app browser unavailable; Chrome rejected local file URL under URL policy. No workaround attempted; browser layout/visual QA remains unverified. |

Documentation test environment: temporary venv using Python 3.9, MkDocs 1.6.1, pymdown-extensions 10.21.3, Markdown 3.9 and PyYAML 6.0.3. `requirements.txt` declares compatible ranges, not a full cross-platform lockfile. Initial restricted network installation failed; approved retry installed dependencies successfully. README gives persistent local setup instructions; temporary environment may not survive future sessions.

## Foundation handoff limits (before source audit)

No blocker remains to the requested planning handoff. Production needs selected-source field dictionaries/contracts and exact frozen releases before answers or lessons can be verified. No datasets, notebooks, reference workbooks, screenshots, calculations in Tableau, teaching times or graded submissions are verified or available. No public deployment or Git commit was performed.

Still unresolved: class size and final briefing logistics, delivery/cadence, access/accommodations, practice capacity, submission channel/deadlines, assessment/team policy, storyline/currency/date adoption and rights/license choice. R01 tracks these; D01 can independently turn current proposals into reviewable field dictionaries and hand fixtures. Publication requires a reviewed release and explicit instruction.

## Earlier hybrid dataset update — 2026-10-12 (before source audit)

The user confirmed the established data strategy **plus** Tableau catalog datasets, with sports, technology, government and other suitable topics. The rendered catalog was inspected before the user interruption; Business/Sports/Technology/Government and additional entries were visible. Text-only web access returned a JavaScript shell. A later browser handle was no longer available after interruption; no file inspection or download was performed.

Added DATA_CATALOG.md with concrete candidates, core-domain gaps, proposed transfer exercises and audit workflow. Updated source strategy/case plans, curriculum, assessment, pilot applicability, learner previews, context, shared/role guidance and backlog. The connected synthetic plan remains useful alongside catalog files; its NPR2025 conventions no longer apply to external sources. Five core cases and required synthetic employee records remain; added topics use existing practice or optional extensions. No additional required class hours.

Individual downloads/schemas/rights/answer totals remain unverified; catalog sourcing is confirmed, individual files are candidates. Existing dependency file is requirements.txt; README/current state adapted without changing its contents. Foundation checks from the earlier session remain historical evidence; current documentation checks are recorded after integration below.

## Earlier next step after source audit (now completed for retail)

D01: freeze the inspected Superstore field dictionary and source-specific metric contract. Resolve source currency/definition labels, proposed2023–2025 scope, Segment mapping and customer-conflict exclusions. D02/D03 prepare and independently validate an exact retail release, with synthetic supplements/controlled cases where inputs are absent. Only then author and rehearse the pilot. SOURCE_AUDIT.md records recommended sports/technology/government roles. See TASKS and HANDOFF.

## Earlier hybrid-update verification

Re-ran `python3 scripts/check_docs.py` (six learner pages), strict temporary MkDocs build (no warnings), `git diff --check`, and a local inline-link/whitespace scan across32 Markdown files. Rechecked all twelve120-minute budgets and19h essential practice. README now points to the existing requirements.txt. Core/extension case and hybrid-source wording were reviewed by lead; no dataset downloads/answers or Tableau execution are implied. No deployment or commit performed.

## Current source audit — 2026-10-12

- Followed four download links observed in the rendered catalog: Superstore, World Cup Results, Mobile OS Usage, US Construction. All returned HTTP200, passed signatures and were preserved unchanged at the paths in `data/metadata/catalog-audit-2026-10-12/source_manifest.json`, with bytes, SHA-256 and retrieval evidence. Publication remains false.
- Added reproducible acquisition/integrity and offline profiling scripts, separate requirements-data.txt and data commands. Profiles capture every real column/type/null/cardinality, keys/date coverage and quality findings. Numerical inspection controls stay in instructor/source-audit, outside the learner site.
- SOURCE_AUDIT.md recommends supported uses and records catalog/file discrepancies: Superstore is US/Canada2023–2026, with currency/Profit meaning unresolved and two customer/order conflicts; sports has16exact duplicate matches; Mobile OS has1,772missing dates; government mixes overlapping amounts/annual rates/percentage/error series and has incomplete2016.
- SOURCE_RIGHTS.md records primary-source provider research. Direct learning-download guidance, provider licenses/policies, mirror provenance and bundling/public-upload permissions are distinguished. No blanket rights clearance or course license assigned.
- Reused case/data worker for rights evidence and case/strategy integration, reviewer for independent numerical/source audit. Exclusive file ownership observed; lead integrated other state, scripts and source-audit design.
- Separate source-fetch script, duplicate raw layouts and two additional files appeared during this work and were preserved unchanged. They are outside this four-file manifest and were not executed/audited by this run. Do not infer provenance or adoption from their presence.

### Checks actually performed for source audit

`python3 scripts/acquire_catalog_samples.py` acquired the files with normal TLS/curl under an approved network run; subsequent invocation verifies only the manifest hashes. Offline profiling command used:

```bash
PYTHONPATH=/tmp/kings-source-audit-libs /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/profile_catalog_samples.py
```

PASS: four byte/hash checks, retail line/lookup keys and date chronology, sports deduplication and all20tournament match/goal reconciliations, dated OS subset key, government nonnullable composite key and177unique nonmissing monthly observations. Schema/profile outputs generated. Environment: Python3.12.14, pandas2.2.3, openpyxl3.1.5, xlrd2.0.2; xlrd installed to temporary directory after approved pip access. Raw workbook values were read without editing or recalculating formulas. Local `.venv-data` installation recipe is documented but not separately executed.

Independent review uses direct xlrd iteration/Decimal rather than the profiler's pandas retail path, direct openpyxl sports rows, and CSV/Decimal government/technology checks. See SOURCE_AUDIT_REVIEW.md for exact controls, a hand-check fixture and limits. These validate the snapshot internally; they are not upstream truth checks or released lesson answers.

Remaining production/release conditions: source-specific dictionaries/contracts and prepared versions; source currency/accounting definitions or supported teaching labels; historic geography/provenance; permitted delivery; synthetic source generation; exact lesson answers; Tableau/device/classroom/visual QA. No prepared learner dataset, notebook, source-specific lesson, Tableau workbook or public upload was produced. No commit/deployment performed. Existing site/ and uncommitted work preserved.

Final integration checks: `python3 scripts/check_docs.py` PASS (six learner pages); `/tmp/kings-data-docs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/data-analytics-site-check` PASS without warnings; local inline-link/whitespace scan PASS across 36 Markdown files; all scripts pass Python syntax compilation without execution; legacy-home bytes still exactly match HEAD's original home. `git diff --check` PASS; status inspected. The current docs build has no new learner lesson/data output. New unowned `graphify-out/` appeared at final status inspection and was left untouched, as were the separate source files/script. Remote links/anchors/reference syntax and visual layout are outside the final local-link scan.

## Earlier D01 retail development freeze — 2026-10-12

- Created `data/metadata/superstore/retail-v1/`: full field dictionary (25 raw fields/22 planned prepared fields), 13 metric definitions, machine settings and reproducible preparation specification. Independent review accepted the design; freeze.json records seven specification/review/fixture/checker SHA-256 values plus raw-source identity. This freezes the first retail local-development variant only, not all five-domain contracts or a learner/public release.
- Fixed date scope to 2023–2025 Order Date, keeping boundary-crossing Ship Dates. Chose source monetary-unit labels without currency/accounting inference; Segment instead of Channel; reported Sales/Profit rather than synthetic gross-profit/refund semantics. Whole-source customer conflicts remain flagged in primary totals and are excluded consistently only in customer work. Returns means listed/not listed, not proven no-return or event timing.
- Added private, explicitly synthetic JSON hand fixtures and a read-only retail contract checker. Checks cover order/line grain, ratios of totals, empty/zero denominators, overlapping category orders, repeated return flags, customer eligibility, date boundaries, calendar MoM/YoY and covered-month/no-selected-lines versus unavailable periods. No synthetic source generator or prepared dataset was created.
- Case/data worker authored only the dictionary; reviewer authored only RETAIL_CONTRACT_REVIEW.md and independently checked arithmetic/populations/direct source values without checker helpers. Lead accepted the review, added the covered-month refinement and froze the version. No open analytical review defects remain for local development.
- Aligned curriculum, assessment and learner previews to the first source-backed Segment snapshot; the detailed Meridian/channel pilot remains a labeled synthetic reference. Five domains, twelve classes and practice budgets are preserved. Shared guidance, data commands, decisions, tasks and handoff now point to D02.

Actual D01 command, read-only and repeated after freeze:

```bash
PYTHONPATH=/tmp/kings-source-audit-libs /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_retail_contract.py
```

Pre-freeze checks passed: exact original hash/schema/keys, 6,815 scoped lines/3,388 orders, 36 months, customer-eligible 6,811 lines/3,387 orders and excluded four-line/one-order population bridge; monetary/quantity controls reconciled without row rounding. Independent review additionally confirmed 34 retained lines ship after the scope end. Source was not edited and formulas were not recalculated. Tableau expressions were checked against official aggregate/filter documentation, not run in the app.

**D01 handoff at that time (now superseded):** D02 implements preparation_spec.md and writes a local immutable 22-column source projection, typed re-read validation, output manifest and private exceptions/reconciliation. Then D03 independently validates prepared-version answers and actual Tableau behavior. D02R separately covers synthetic refund/cost material; D04–D07/X01 freeze their own case contracts. Stronger currency/accounting claims, public delivery rights, full lessons, device/classroom/accessibility/visual QA and teaching timings remain unverified. Existing raw files, site/, extra source work and graphify-out/ are preserved; no publishing or commit.

Final D01 checks: post-freeze retail checker PASS (all seven frozen hashes, synthetic edge cases and exact source/bridge checks); `python3 scripts/check_docs.py` PASS (six learner pages); strict temporary MkDocs build PASS with no warnings; local inline-link/whitespace scan PASS across 40 Markdown files; script syntax and contract JSON parse PASS; original-home bytes unchanged; all twelve classes remain120minutes and essential practice19h. `git diff --check` and status inspected at handoff. Remote links/reference syntax/anchors, visual rendering and Tableau are outside these checks. The new specifications/fixtures remain outside docs/; learner previews contain no internal links or answer files.
