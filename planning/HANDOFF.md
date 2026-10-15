# Next-session handoff

Updated 2026-10-12. **Foundation, four-source audit, first retail development contract and D02 preparation complete. D03 numerical evidence is separate from its remaining Tableau checks. Full lesson production remains backlog.**

The user requests Claude takeover next. Read [AGENTS.md](../AGENTS.md) → [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) → [STATUS.md](STATUS.md) → [TASKS.md](TASKS.md), then the concrete [CLAUDE_TAKEOVER.md](CLAUDE_TAKEOVER.md). The takeover brief contains exact artifacts, hashes, commands, constraints and a suggested first prompt; shared authority stays in AGENTS.md.

## Claude session update — 2026-10-12

Learner site keeps the Read the Docs theme (user preference after a brief Material trial, DEC-036) plus `docs/stylesheets/readability.css`; all six pages were restructured for readability (DEC-034, DOC01). Write every new learner page in that style: lead sentence, `---` breaks, short paragraphs, numbered steps, tables or `###` subsections, note/tip/hint/warning admonitions. No Material-only syntax. User approved the rendered result. Preview with `/tmp/kings-data-docs-venv/bin/python -m mkdocs serve` (reinstall from requirements.txt if the venv is gone). D03 Tableau checks remain open because this session had no desktop-app control (DEC-035).

## DATA 300 China classroom — 2026-10-15 (read this first)

A second, separate course is being prepared: `planning/china_classroom/PLAN.md` and `docs/china/`. Offline-first (no Colab/GitHub); syllabus labs are graded work. Day 1 and the bundled data are done; use `planning/agents/china-notebook-author.md` for Days 2–7.

## All 16 Python sessions drafted — 2026-10-15

Sessions 1–16 have lecture and lab notebooks, quizzes and private answers. Build with the project `.venv`; delegate notebook work with `planning/agents/notebook-author.md`. Rubric confirmed (DEC-049). Next: Colab trial, then the Tableau section.

## Sessions 10–13 built — 2026-10-15

All four business cases exist (Sessions 10–13) with synthetic data finance-v1, operations-v1, hr-v1 and marketing-v1. Sessions 1–13 are drafted. Next: push the new data so Colab downloads work, then Session 14 (dashboards and storytelling) and the capstone Sessions 15–16. Keep the venv outside `/tmp` if possible: a temp cleanup wiped it once.

## Sessions 8–9 and finance data — 2026-10-14

Sessions 1–9 now have lecture + lab notebooks and private answers. `finance-v1` (D04) is ready for Session 10. Next: Session 10 finance case, then D05 operations data and Session 11. Run `scripts/run_notebooks.py --check-data` (it now merges split output, so re-runs are byte-stable), then `make convert-all`.

## Private answers are local only — 2026-10-14

The GitHub repo is public, so `instructor/` (answer keys, quiz keys, reference values) is in `.gitignore` and was removed from the entire git history, which the user force-pushed. Every commit ID before `27f52e4` changed; other clones (including any Codex workspace) must re-clone or hard-reset to `origin/main`. Keep writing private answers to `instructor/sessions/NN/` on disk, never commit them, and never `git push --all`: local branches `backup/before-history-rewrite` and `backup/before-untrack` still contain the old answers.

## Sessions 1–7 built, D08 ready — 2026-10-14 (read this first)

Sessions 1–7 each have lecture + lab notebooks, quiz and private answers. D08 synthetic marketing data exists for Sessions 8, 9 and 12. Next: Sessions 8 and 9, then case data D04–D07.

## Sessions 1–4 and 6 built — 2026-10-14

Sessions 3, 4 and 6 added the same day (see STATUS). Remaining Python sessions: 5 and 7 lectures (labs exist as drafts), 8–16. D08 blocks 8, 9, 12.

## Sessions 1–2 built — 2026-10-14

Session 1 and 2 lecture + lab notebooks, quizzes and private answers exist (DEC-045; see STATUS). Draft labs for Sessions 5 and 7 renamed. Superseded notebooks 00–02 and the old generated `docs/lectures/00–04` pages were deleted with user approval; `make convert-all` is safe again. Next: review + Colab trial of Sessions 1–2, then Session 3 and D08.

## Course plan v2 — 2026-10-14 (read this first)

`planning/COURSE_PLAN.md` is the working plan: every session = 2-hour lecture + 3-hour lab, applied statistics for analysts, 16 Python sessions + Tableau section. Next: build Sessions 1 and 2 end to end (lecture notebook, lab with core/stretch/challenge, quiz, private answers) as the template; then D08 synthetic A/B data for Sessions 8, 9 and 12.

## Python-first — 2026-10-13

Main path is now Python in Google Colab (DEC-041). The lesson source is `notebooks/NN_*.ipynb` (DEC-042): edit the notebook, run `scripts/run_notebooks.py --check-data` (Python 3.12, `requirements.txt`), then `make convert-all` to refresh `docs/lectures/`. Push to GitHub so the Open in Colab badges work. The Tableau drafts under `docs/lessons/class-0N.md` are a deferred later section. Next: Colab trial; private exercise answers for the Python lessons; D02R refunds; finance case.

## Lessons 3–4 drafts — 2026-10-12

Draft Lessons 1–4 now cover the whole retail stage. All four need one Tableau rehearsal with the user at the keyboard, using the checklists in `instructor/sessions/*/teaching-notes.md`; that rehearsal also closes D03. After that: D02R synthetic refund/cost supplement, then the finance case (D04 data contract, L04 lesson).

## Foundations and content-first framing — 2026-10-12

New `docs/foundations/` module (DEC-038) precedes the Tableau lessons; regenerate its figures with `scripts/make_foundation_figures.py` (deps in requirements.txt). Learner pages must not frame the course by session count or hour budgets (DEC-039); lessons are "Lesson N".

## Class 1–2 drafts — 2026-10-12

Draft L01 pages exist: `docs/lessons/class-01.md`, `docs/lessons/class-02.md`; private notes and rehearsal checklist in `instructor/sessions/class-01-02/teaching-notes.md`. Next: rehearse them in the installed Tableau with the user at the keyboard (also closes D03 whole-scope checks), fix menu names, remove the "Draft lesson" banner only after rehearsal, then L02 Class 3 from PILOT_LESSON.md using Segment and source metrics.

## Resume here

Complete D03's actual local Tableau comparisons using `data/prepared/superstore/retail-v1/order_lines.csv` and the private numerical references. CSV SHA-256: `434ba08abf665b617294b188e38c0d0b8a86d0b3386d41eff8a42c15bc708de2`. It contains 6,815 lines/3,388 orders/22 fields/36 months. D02's typed comparison covered 149,930 values; repeat bytes and mtimes were unchanged, and an independent reviewer accepted preparation.

The native Tableau app imported the CSV and showed 22 fields/6,815 rows. Worksheet navigation encountered app-control errors; no KPI/filter/grand-total, zero-case, local save/reopen or installed-version check completed. No reference workbook was saved/publicly uploaded. Record app version and actual whole/Segment/Region/eligible/Category comparisons plus empty/zero behavior; distinguish full-precision from display-only evidence. See detailed brief for attempt limits. D03 remains IN PROGRESS.

Do not edit the seven D01 frozen inputs or D02 outputs to fix a mismatch. Freeze-time statements that preparation did not yet exist are historical; update current state here instead. Run `scripts/check_retail_contract.py`, `scripts/prepare_retail.py` and `scripts/validate_retail.py` in the documented data environment to verify current identities. No repeat source acquisition/design audit is needed. The first two scripts do not validate Tableau; the independent numerical validator does not either.

L01 produces/rehearses S1–S2 after D03/relevant R01 logistics. L02 translates the retained synthetic S3 pilot into actual Segment/source-metric instructions using this CSV; V01 trials novice timing/accessibility before extending. S3 is snapshot KPIs; S4 owns growth/qualified return-list interpretation and separate D02R synthetic refunds/costs. D04–D07 and X01 freeze their own contracts; all five core domains remain required. Do not begin all lessons in parallel.

## Preserve analytical decisions

Order Date 2023–2025, Row ID line key, no dedup/status filter, keep 2026 Ship Dates, source monetary units and reported Sales/Profit. Do not infer NPR/gross margin or reapply Discount. Detect both customer conflicts on all raw Orders; keep scoped conflict lines in main totals; customer work filters eligible=1 consistently (6,811 lines/3,387 orders) and discloses exclusions. Returns means listed/not listed, not event timing or refunds. Category orders overlap; growth uses calendar comparators and declared coverage. Detailed policies/tolerances live in the frozen contract.

Confirmed: 12×2h live plus practice; basic spreadsheets, no Tableau/Python assumed; Tableau Public synthetic/public data; portfolio/executive briefing; five core domains; hybrid existing strategy plus Tableau catalog and broader choice topics. Do not reask these. Optional-first Python, 19h essential practice, three-domain synthesis, proposed rubric and Meridian/NPR/2025 simulation remain recommendations. R01 tracks remaining logistics/assessment/access decisions.

Source-specific inspected sports/technology/government recommendations and unresolved rights are in SOURCE_AUDIT/SOURCE_RIGHTS. Do not invent dates, mix incompatible government measures, relabel unrelated files as one company, or treat downloadable files as blanket redistribution permission. Employee-level HR stays synthetic.

## Verification and preservation

Latest commands/results are in STATUS and the takeover brief. Final checks passed: six learner pages, strict temporary MkDocs build, local links/whitespace across41 selected project Markdown files, script syntax/JSON, frozen/source hashes, legacy-home bytes and course/rubric budgets; diff clean/status inspected. Build output at `/tmp/data-analytics-site-check` protects existing site/. Actual data environment was bundled Python3.12.14/pandas2.2.3/openpyxl3.1.5 plus temporary xlrd2.0.2; `.venv-data` recipe is documented, not separately installation-tested. Temporary dependencies may expire. Browser local-file visual review was policy-blocked; do not work around it. No classroom/novice timing trial exists.

Only docs/ enters the learner site. Private answers remain instructor-only; prepared metadata contains diagnostic controls/private paths, so do not distribute its directory wholesale. No course license, public data package or deployment was made. The user subsequently authorized a local course-work commit; use `git log -1` for its identity. Unrelated additions remain untracked, and nothing was pushed. Preserve original raw/frozen bytes, LEGACY_HOME, pre-existing Makefile/.gitignore, site/, separate fetch script/duplicate raw layouts/extra datasets and graphify-out/. Those extras were not adopted by this four-source workflow. Inspect git status before editing and never discard unowned changes.

Reusable bounded roles are in planning/agents/. Use exclusive file ownership. Update TASKS, DECISIONS, STATUS and this handoff after substantive work; also refresh CLAUDE_TAKEOVER.md if its snapshot becomes stale.
