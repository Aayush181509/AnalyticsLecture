# Implementation backlog

Updated 2026-10-12. Status definitions: DONE = acceptance met with stated evidence; READY = dependencies met; PLANNED = depends on earlier work; IN PROGRESS = some checks complete, acceptance still open; NEEDS INPUT = explicit decision or external setup required. Foundation, source inspection, the first retail contract and D02 preparation are complete. D03 validation is in progress; remaining Tableau checks lead the next session. No inspection/design completion implies publication permission.

| ID / priority | Task | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|
| F01 / P0 | Inspect and preserve workspace | — | DONE | Inventory records tracked files, initial changes, instructions, tooling, legacy copy. |
| F02 / P0 | Establish context and teaching constraints | F01 | DONE | Confirmed user answers separated from recommendations and open questions. |
| F03 / P0 | Integrate curriculum, cases, data, assessment, pilot | F02 | DONE | All five domains, 24-hour sequence, metric contracts, detailed 120-minute pilot and review are coherent. |
| F04 / P0 | Establish MkDocs foundation and shared guidance | F01 | DONE | Safe learner navigation, template, role briefs, README/entry files, strict build and link checks recorded. |
| DOC01 / P1 | Make learner site spacious and easy to follow | F04 | DONE | User request 2026-10-12. Read the Docs theme kept (user preferred it over a brief Material trial, DEC-036) + readability stylesheet; six pages restructured with lead summaries, short paragraphs, numbered steps, subsections and admonitions; same substance and boundaries; docs checker and strict build pass; user reviewed the rendered site and approved it ("looks much better"). |
| FND01 / P0 | Foundations module before Tableau | F04 | DONE | User request 2026-10-12 (DEC-038). Six learner pages in docs/foundations/, ten figures generated reproducibly by scripts/make_foundation_figures.py (requirements-figures.txt), source data preserved with checksums, exercises on every page, linked from home, roadmap Stage 0 and Lesson 1. Independent read-only fact-check found 2 errors, 7 warnings and nits; all errors and warnings fixed (see STATUS). |
| PY01 / P0 | Python Lessons 0–4 as Colab notebooks (retail) | D02, FND01 | DONE (drafts, classroom trial pending) | User requests 2026-10-13 (DEC-041, DEC-042). Source: `notebooks/00–04_*.ipynb`, executed by `scripts/run_notebooks.py --check-data`, converted by `make convert-all` into `docs/lectures/`. Lesson 0 Python/Colab primer; Lessons 1–4 retail. All 85 code cells run; shared setup cell reproduces the validated CSV; re-execution byte-identical; strict docs build PASS. Remaining: Open in Colab only works after the notebooks are pushed to GitHub; a timed novice Colab trial; private exercise answers. |
| R01 / P0 | Confirm remaining logistics and teaching defaults | F03 | PARTLY DONE (DEC-050) | Record class size/format/cadence, device survey, workload, local submission channel, story/currency/date convention, grading/team policy. 2026-10-15: class size, delivery, submission channel and briefing policy confirmed; calendar/cadence, deadlines, completion criteria remain. |
| S01 / P0 | Audit first Tableau catalog candidates | F03 | DONE | Four originals preserved/hash-checked; actual schemas, keys, dates, missingness and internal controls inspected; source/provider terms researched with unresolved release conditions recorded; recommended roles/gaps in SOURCE_AUDIT.md and SOURCE_RIGHTS.md. No source-derived release approved. |
| D01 / P0 | Freeze first retail source data/metric contract | F03, S01 | DONE | All 25 raw fields/22 prepared fields documented; 13 metric definitions, scope/units/keys/returns/customer/precision policies, machine settings, preparation spec and private hand fixtures reviewed independently. Exact-source/fixture checker passes. Frozen local development only; other domain/transfer contracts remain future work. |
| D02 / P0 | Prepare first retail source | D01 | DONE | Implement frozen Superstore projection reproducibly; original unchanged; immutable output/contract/script hashes, typed CSV re-read and exception bridge; seed not needed for sourced data; defects separate; publication=false until permitted delivery/release review. |
| D02R / P1 | Freeze/prepare controlled retail refund and cost supplement | D01, V01 | PLANNED | Separate synthetic contract, explicit units/dates/sale cohort/event cutoff, refund/quantity/cost-recovery limits and exact hand checks; reproducible seed/config if generated; no invented source facts appended to Superstore. |
| D03 / P0 | Validate retail reference answers and Tableau behavior | D02 | IN PROGRESS | Keys, arithmetic, returns, filter effects and order counts checked independently against exact CSV; hand check reconciles; answers in instructor only. Actual Tableau whole/Segment/Region/eligible/Category and grand-total/empty/zero comparisons with version/evidence. Local import passed; worksheet checks remain. |
| L01 / P0 | Produce and rehearse S1–S2 foundations | D03, R01 | DEFERRED (Tableau section, DEC-041) | Learner setup/preparation pages, small guided tasks and recovery instructions; Public/local-save smoke test on actual target devices; no Python prerequisite. 2026-10-12: draft learner pages `docs/lessons/class-01.md`, `class-02.md` and private `instructor/sessions/class-01-02/teaching-notes.md` written at user request ahead of D03 (DEC-037); remaining: rehearse click paths on installed Tableau, D03 Tableau values, novice timing, device/R01 checks. |
| L02 / P0 | Produce S3 retail pilot and private solutions | L01, D03 | DEFERRED (Tableau section, DEC-041) | All PILOT_LESSON sections become actual instructions; questions/hints/answers tested on same CSV version. 2026-10-12: draft learner page `docs/lessons/class-03.md` (segment KPIs, totals-first ratios, reconciliation, region/category independent work, mean-of-ratios debug, five-sentence recommendation) and private `instructor/sessions/class-03/teaching-notes.md` with reference values and rehearsal checklist (DEC-040). Remaining: Tableau rehearsal, D03 checks, novice trial. |
| V01 / P0 | Trial pilot before extending production | L02 | PLANNED | Fresh Tableau run with version recorded; KPI cross-checks and timed novice trial; revise overloaded tasks and capture accessibility feedback. |
| L03 / P1 | Produce S4 retail dashboard and portfolio checkpoint | V01, D02R | DEFERRED (Tableau section, DEC-041) | Monthly growth and qualified return-list interpretation; separate controlled refund/cohort example; dashboard, critique prompts, alternative acceptable recommendations, rubric feedback and exact-data solutions. 2026-10-12: draft learner page `docs/lessons/class-04.md` (monthly trend, MoM vs YoY growth with LOOKUP caveats, returns-list share, dashboard with shared Region filter, seasonal debugging case, test recommendation) and private `instructor/sessions/class-04/teaching-notes.md`. Synthetic refund/cost exercise (D02R) still to build. Remaining: rehearsal and D02R. |
| D04 / P1 | Source/generate and validate finance data | D01 | DONE (local) | `data/synthetic/finance-v1/` from `scripts/generate_finance.py` (seed 20251101), validated by `scripts/validate_finance.py`; private answers in `instructor/solutions/finance-v1/` (DEC-047). Feeds S-10. |
| L04 / P1 | Produce S5 finance case | L03, D04 | PLANNED | Beginner prepared source and source-model extension; favorable/unfavorable variance task, debug, recommendation and separate verified answers. |
| D05 / P1 | Source/generate and validate operations data | D01 | DONE (local) | `data/synthetic/operations-v1/` from `scripts/generate_operations.py` (seed 20251201), validated by `scripts/validate_operations.py`; private answers `instructor/solutions/operations-v1/` (DEC-048). |
| L05 / P1 | Produce S6 operations case | L04, D05 | PLANNED | On-time service dashboard, pending shipment debug, completeness checks and feasible follow-up action. |
| D06 / P1 | Source/generate and validate marketing data | D01, V01 | SUPERSEDED (DEC-048) | Additive funnel counts and spend, attribution contract, weighted-rate counterexample, zero denominators and unassigned orders tested. |
| L06 / P1 | Produce S7 marketing case | L05, D06 | PLANNED | Weighted metrics, campaign comparison and attribution-limit challenge; verified solutions. |
| D07 / P1 | Generate/validate synthetic HR data | D01 | DONE (local) | `data/synthetic/hr-v1/` from `scripts/generate_hr.py` (seed 20251231), validated by `scripts/validate_hr.py` incl. company and department bridges; private answers `instructor/solutions/hr-v1/` (DEC-048). |
| L07 / P1 | Produce S8 HR case | L06, D07 | PLANNED | Historical turnover/cohort task, current-headcount debug, fair-comparison challenge and private solutions. |
| P01 / P1 | Write S9–S12 synthesis/capstone kit | L07, R01 | PLANNED | All-domain portfolio checklist; three-domain executive brief; no incompatible-grain grand join; peer review, briefing schedule and rubric exemplars. |
| X01 / P2 | Produce reviewed transfer choices: sports, technology, government | S01, V01 | PLANNED | Source-specific question/dictionary/metrics; guided, independent, debug and recommendation task; exact-data checks/private answers; use existing practice or optional route, preserve five core outcomes and24h contact. |
| N01 / P2 | Produce optional Python/pandas companions | V01, D04, D05, D06, D07 | PLANNED | Each notebook explains selection/grouping/date logic conceptually, runs on released data, reconciles Tableau results and includes environment instructions; no essential assessment requires code. |
| Q01 / P1 | Final instructional and technical QA | P01, N01 | PLANNED | Strict site build, rendered review, exact-data answer audit, all five case component checklists, device rehearsal and links; Python may be omitted from first release if explicitly logged. |
| PUB01 / P2 | Prepare a reviewed learner release | Q01 | PLANNED | Rights/license approved, downloads audited, no internal notes/answers; publication is a separately authorized action, not part of build verification. |

Next concrete task: complete D03's remaining local Tableau comparisons against the exact prepared CSV and private version-bound numerical references. Read [CLAUDE_TAKEOVER.md](CLAUDE_TAKEOVER.md) for current artifacts, commands and app-control limits. D02 is accepted for local preparation; no learner/public release is approved. L01/L02 follow D03 and relevant R01 decisions. Remaining source/simulation contracts freeze within D02R, D04–D07 and X01.

## First retail preparation completion evidence

D02: `scripts/prepare_retail.py` creates or byte-verifies immutable CSV/manifest/quality report/private exceptions after frozen-contract preflight. Exact output: 6,815 lines/3,388 orders/22 fields/36 months; 149,930 typed values match; eligible 6,811 lines/3,387 orders; 34 boundary-crossing ship-date lines retained. Repeat run preserved bytes and modification times. Independent read-only reviewer accepted preparation and verified recorded hashes/schema/counts/coverage. Original/frozen inputs unchanged. CSV SHA-256 `434ba08abf665b617294b188e38c0d0b8a86d0b3386d41eff8a42c15bc708de2`. The changed-existing-output refusal was code-reviewed, not corruption-tested.

D03: independent numerical validation PASS, recorded in STATUS and private `reference_answers.json`/`numerical_validation.json`; a separate pandas source read matches all 149,930 typed CSV values and source/hand controls, group metrics, population bridges and calendar growth. Repeat reports are byte-identical; lead rerun passed. Native Tableau import displayed 22 fields/6,815 rows; worksheet navigation hit app-control errors, so no app-calculated KPI/filter/grand-total or save/reopen result is claimed. Keep IN PROGRESS until those documented checks pass. A successful data or docs command does not close the app gap.

## First retail contract completion evidence

D01: dictionary/metric contract/settings/preparation spec under data/metadata/superstore/retail-v1; review in RETAIL_CONTRACT_REVIEW.md; private synthetic edge fixtures in instructor/source-audit. Read-only checker verifies exact source/schema, 2023–2025 scope, customer exclusions/bridge, 36 months, stored-value controls and hand fixture expectations. Independent reviewer used separate arithmetic/direct source iteration without checker helpers; no open design defects. Freeze manifest records exact contract/review/fixture/checker hashes. No prepared file, synthetic source generator, lesson, Tableau workbook or publication was produced by this task.

## Source-inspection completion evidence

S01: exact catalog-observed URLs returned four files; manifest records retrieval/bytes/SHA-256 and publication=false. Offline profiler verifies hashes, keys and snapshot invariants and records every field in profiles.json. Sports counts/goals reconcile after exact deduplication; retail controls and government aggregation tolerances are private inspection evidence. SOURCE_RIGHTS.md records primary-provider research and file-level uncertainty. Independent analytic review is in SOURCE_AUDIT_REVIEW.md. No prepared learner release, source-specific Tableau lesson or public upload was produced. Additional unowned source files/scripts noticed during integration were preserved and are outside this four-file audit.

## Foundation completion evidence

F03: curriculum budgets and rubric checked; all five case contracts reviewed; S3/S4 boundaries and practice estimates reconciled; reviewer report in REVIEW.md and lead repairs recorded in DECISIONS.md. F04: six learner pages, safe navigation, five role briefs and shared instructions created; local docs checker and strict temporary build passed. Generated HTML structure and absence of internal-source copies checked; browser visual QA could not run under available browser policy. Full Tableau/data/classroom checks remain future work, not foundation acceptance claims. See STATUS.md for commands and limits.

## Git checkpoint

2026-10-12: user requests a local commit of our course changes. This records existing completed work and the Claude handoff; it does not close D03 or authorize publication/push. Unrelated untracked additions remain untouched. See STATUS and `git log -1` for checkpoint scope/identity.

## Claude session — 2026-10-12

DOC01 done: learner pages restyled for readability at the user's request (DEC-034). D03 remains IN PROGRESS: this Claude session has no native desktop-app control, so the Tableau worksheet comparisons still need either the user at the keyboard following a checklist or a session with app control (DEC-035). Next concrete task: rehearse the Class 1–2 drafts in the installed Tableau (user at keyboard, using the rehearsal checklist in the private teaching notes); this also closes the D03 whole-scope row/order/returns checks. L02/L03 drafts (Lessons 3–4) now exist; rehearse all four lessons together, then build D02R and the finance case (D04/L04).

Learner-time framing removed (DEC-039): learner pages focus on content; do not reintroduce session counts or hour budgets in docs/.

## Python-first switch — 2026-10-13

Teaching path is Python in Colab (DEC-041). L01–L03 Tableau drafts are deferred to the later Tableau section; D03 Tableau checks are needed only when that section is produced. Next concrete tasks: (1) Colab trial of Python Lessons 0–4 with a novice; (2) private exercise answers for the Python lessons in `instructor/sessions/`; (3) D02R synthetic refund supplement as a Python lesson extension; (4) finance case (D04 contract, then a Python lesson).

## Session production backlog — COURSE_PLAN.md (2026-10-14)

Each session needs: lecture notebook, lab notebook (core / stretch / challenge), theory quiz, private answers in `instructor/sessions/NN/`, `run_notebooks.py --check-data`, `make convert-all`, docs build, and an independent review. Status for the session as a whole:

| ID | Session | Depends on | Status | Notes |
|---|---|---|---|---|
| S-01 | Why data analytics matters | FND01, PY01 | REVIEW | `01_why_data_analytics_lecture/lab.ipynb` + `instructor/sessions/01/answers.md` built and executed 2026-10-14; needs independent review and a Colab trial |
| S-02 | Data, grain and the DataFrame | PY01 | REVIEW | `02_data_and_grain_lecture/lab.ipynb` + `instructor/sessions/02/answers.md` built, executed and data-checked 2026-10-14; old Lessons 1–2 merged into the lab; needs independent review and a Colab trial |
| S-03 | Cleaning and preparing data | S01 audit | REVIEW | `03_cleaning_and_preparing_lecture/lab.ipynb` + answers built 2026-10-14; World Cup and Mobile OS downloaded in-notebook from Tableau catalog with SHA-256 (no bundling); new quirks found: City trailing spaces, 73 `ï¿½` rows, Iran/IR Iran, empty-text Observation, mixed WorldCups Attendance types |
| S-04 | Descriptive statistics and distributions | S-02 | REVIEW | `04_descriptive_statistics_lecture/lab.ipynb` + answers built 2026-10-14; home sales series SOLD/US/unadjusted MEDIAN vs AVERAG, 1975-01–2016-10, downloaded in-notebook with SHA-256 |
| S-05 | Metrics and KPIs | S-02 | REVIEW | `05_metrics_and_kpis_lecture.ipynb` new, lab restructured (Berkeley, metric contract, Simpson within West/Technology), answers in `instructor/sessions/05/` — 2026-10-14 |
| S-06 | Visualisation principles | S-04 | REVIEW | `06_visualisation_principles_lecture/lab.ipynb` + answers built 2026-10-14; before/after demos for every principle |
| S-07 | Time series and trends | S-05 | REVIEW | `07_trends_and_growth_lecture.ipynb` new, lab restructured with construction spending (XXXX/T/US, not adjusted, 2002-01–2016-09, downloaded with SHA-256), answers in `instructor/sessions/07/` — 2026-10-14 |
| S-08 | Correlation and regression | S-04, D08 | DONE (draft; Colab trial pending) | Lecture + lab notebooks, quiz, private answers in `instructor/sessions/08/` (2026-10-14). Outputs match marketing-v1 references. |
| S-09 | Sampling, uncertainty and experiments | S-04, D08 | DONE (draft; Colab trial pending) | Lecture + lab notebooks, quiz, private answers in `instructor/sessions/09/` (2026-10-14). A/B results match marketing-v1 references. |
| S-10 | Finance case | D04 | DONE (draft; Colab trial pending) | Lecture + lab, quiz, private answers `instructor/sessions/10/` (2026-10-14). Matches finance-v1 references. |
| S-11 | Operations case | D05 | DONE (draft; Colab trial pending) | Lecture + lab, quiz, private answers `instructor/sessions/11/` (2026-10-14). Matches operations-v1 references. |
| S-12 | Marketing case | D08 | DONE (draft; Colab trial pending) | Lecture + lab, quiz, private answers `instructor/sessions/12/` (2026-10-15). Matches marketing-v1 references. |
| S-13 | HR case | D07 | DONE (draft; Colab trial pending) | Lecture + lab, quiz, private answers `instructor/sessions/13/` (2026-10-15). Matches hr-v1 references. |
| S-14 | Dashboards and storytelling | S-07 | DONE (draft; Colab trial pending) | Lecture + lab, quiz, private answers `instructor/sessions/14/` (2026-10-15). |
| S-15 | Capstone studio | S-10–S-13 | DONE (draft; Colab trial pending) | Lecture + lab, private answers `instructor/sessions/15/` (2026-10-15). Shows the false month join and the honest side-by-side view. |
| S-16 | Executive briefings | S-15, R01 | DONE (draft) | Lecture + lab, private answers `instructor/sessions/16/` (2026-10-15). Rubric weights confirmed by the user (DEC-049). Presentation format still depends on class size (R01). |
| D08 | Synthetic A/B test and marketing spend data | D01 pattern | DONE (local) | `data/synthetic/marketing-v1/` from `scripts/generate_marketing.py` (seed 20251001, numpy 2.5.4), validated by `scripts/validate_marketing.py`; private key in `instructor/solutions/marketing-v1/`. Notebooks should load it from a commit-pinned raw GitHub URL with SHA-256 after push |
| T-01–T-04 | Tableau section | S-14 | DEFERRED | From the Tableau drafts |

Sessions 1 and 2 built 2026-10-14 (REVIEW). The superseded notebooks 00–02 and old generated pages 00–04 were deleted with user approval. Sessions 3, 4 and 6 built 2026-10-14 (REVIEW). Sessions 5 and 7 completed and D08 built 2026-10-14. Next: (1) independent review + Colab trial of Sessions 1–7; (2) Sessions 8 and 9 (use D08); (3) D04–D07 case data for Sessions 10–13.

Next concrete task (2026-10-14): Session 10 (finance case) lecture + lab from finance-v1; then D05 operations data → S-11, D06/D07 → S-12/S-13.

Next concrete tasks (2026-10-15): push the new synthetic releases (finance-v1, operations-v1, hr-v1) so Colab downloads work; Session 14 (dashboards and storytelling); Sessions 15–16 (capstone kit); a real Colab trial; D06 is not needed (marketing case uses D08 marketing-v1).

All 16 Python sessions drafted (2026-10-15). Next: real Colab trial with a novice; then the Tableau section (T-01–T-04) and R01 logistics.

## DATA 300 China classroom (DEC-051) — 2026-10-15

| ID | Task | Status | Notes |
|---|---|---|---|
| CN-00 | Plan, schedule, setup pages | DONE (draft) | `planning/china_classroom/PLAN.md`, `docs/china/` |
| CN-01 | Bundle offline data + SOURCES.md + setup check notebook | DONE | penguins, diamonds, tips, mpg, CO₂ series, VADER lexicon; Lab 3/5/Assignment 2 text data |
| CN-D1 | Day 1: two lectures + Activity 1 lab + setup check | DONE (draft) | Private answers `instructor/china_classroom/D1/`. Activity 1 deadline and offline PDF merge method still to decide. |
| CN-D2…D7 | Lecture + offline-ready lab notebooks per day | PLANNED | Reuse Foundations and Sessions 1–16; syllabus labs graded as written |
| CN-Q | Confirm deadlines, LMS, Tableau licence, Excel/WPS, midterm source | DONE (2026-10-15) | See PLAN.md "Risks and open questions" |
