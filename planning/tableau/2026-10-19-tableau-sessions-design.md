# Tableau sessions T1–T4 — design

Created 2026-10-19. Status: approved by the user in conversation (structure, edition, verification method and this design). Implements Part F of `planning/COURSE_PLAN.md`.

## Decisions

| Item | Decision |
|---|---|
| Structure | Four sessions, T1–T4, each with a **lecture** page and a **lab** page, like the Python sessions (2-hour lecture, 3-hour lab; hours stay internal) |
| Edition | **Tableau Public** (free). Click paths are written for Tableau Desktop Public Edition; local save to `.twbx` is the default way to keep work; publishing is optional and covered in T4 |
| Verification | Claude rehearses each lab in **Tableau Public web authoring in Chrome**, after the user signs in. Claude never enters credentials and never saves or publishes to Tableau Public (saving there makes workbook and data public). Each data upload is approved by the user. Screenshots are taken from the unsaved session |
| Old drafts | `docs/lessons/class-01.md` … `class-04.md` and their private teaching notes are reused as source material, then removed from the site |

## Sessions

| Session | Lecture | Lab (Core / Stretch / Challenge) | Data |
|---|---|---|---|
| T1 Tableau fundamentals | Tableau's model: data source, dimensions vs measures, discrete (blue) vs continuous (green), aggregation, the Marks card, level of detail, filters and their order | Rebuild Session 2 and Session 4 views: rows vs orders (`COUNTD([Order ID])`), returns flag, distributions (histogram, box plot) of order value and ship days | Superstore |
| T2 Calculations and KPIs | Calculated fields; ratio of sums vs mean of ratios; distinct counts and non-additivity; table calculations (running total, MoM and YoY growth with `LOOKUP`, why filtering months breaks them); a first LOD expression (`{FIXED [Order ID] : SUM([Sales])}`) | Rebuild the Session 5 segment KPI table with a reconciliation check and the mean-of-ratios debugging case; rebuild Session 7 monthly trend and growth | Superstore |
| T3 Dashboards | Dashboard layout and reading order, filters and actions, colour and accessibility, message titles and annotation (Session 14 principles) | Rebuild the Session 14 decision dashboard in Tableau; Stretch: a second dashboard on one synthetic case (marketing-v1 or operations-v1) | Superstore + one synthetic case |
| T4 Publishing and portfolio | Tableau Public privacy (everything published is public, including data), what is safe to publish, versioning `.twbx` files, portfolio storytelling and story points | Build a portfolio piece from the learner's capstone analysis; optional publish only with synthetic or public data | Capstone data |

## Files

| Path | Content |
|---|---|
| `docs/tableau/T1_fundamentals_lecture.md`, `T1_fundamentals_lab.md` | T1 pages |
| `docs/tableau/T2_calculations_kpis_lecture.md`, `T2_calculations_kpis_lab.md` | T2 pages |
| `docs/tableau/T3_dashboards_lecture.md`, `T3_dashboards_lab.md` | T3 pages |
| `docs/tableau/T4_publishing_portfolio_lecture.md`, `T4_publishing_portfolio_lab.md` | T4 pages |
| `docs/tableau/img/` | Screenshots from the rehearsal, named `Tn_<step>.png` |
| `instructor/tableau/Tn/answers.md` (gitignored) | Expected numbers, quiz answers, timing, marking notes |

`mkdocs.yml`: replace "Tableau (Coming Later)" with "Tableau Sessions", each session holding Lecture and Lab entries. Remove `docs/lessons/class-01.md` … `class-04.md` from the site once their content is reused; keep `lesson-template.md` unless it is no longer referenced.

## Page conventions

- Same voice and layout as the Python session pages: lead paragraph, "What you will be able to do", numbered steps, MkDocs admonitions (`!!! note`, `!!! tip`, `!!! warning`).
- Each lab: business decision, guided practice, independent work, challenge, a short evidence list, Moodle submission (saved `.twbx` plus a PDF or image export), and a link back to the matching Python session.
- Each lecture ends with a 5–8 question quiz for the start of the next session; answers live only in `instructor/`.
- Learner pages never print expected result numbers; learners check their own work with reconciliation steps (for example, segment totals add up to the overall total).
- A note on each lab says that click paths are for Tableau Desktop Public Edition and that the web editor's menus differ slightly.
- Superstore is downloaded from Tableau's sample-data page, the same file and version the Python sessions use; synthetic cases come from `data/synthetic/` in this repository.

## Expected values

Computed in pandas from the validated Superstore file (`data/raw/eu-superstore/2026-10-12/sample_-_superstore.xls`, same SHA-256 as the notebooks' setup cell) and the synthetic releases, and stored in `instructor/tableau/Tn/answers.md`. The rehearsal compares Tableau's displayed values with these; any difference is investigated and explained before the page is final.

## Verification

1. `scripts/check_docs.py` PASS and `mkdocs build --strict` PASS.
2. Each lab rehearsed in Tableau Public web authoring; values match the private answers; screenshots saved; any web-vs-desktop difference noted on the page.
3. Nothing saved or published to Tableau Public without the user's explicit approval for that action.
4. No expected numbers or instructor content on learner pages.

This rehearsal also closes the long-open D03 check (Tableau's own values against the private references).

## Out of scope

- Tableau for the China classroom (it already has its own Day 2 Tableau lecture and Lab 2).
- Tableau Server or Cloud, and licensed Desktop features.
