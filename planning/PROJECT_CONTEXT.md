# Project context

Last updated: 2026-10-12 (Asia/Kathmandu). Phase: planning foundation, source audit and first retail development preparation; reference-answer and Tableau validation tracked in STATUS/TASKS.

## Confirmed by the user

**Logistics (2026-10-15, DEC-050):** 21–40 learners; in person; Moodle submissions; individual executive briefings for feedback only, run in two parallel rooms with two assessors in Session 16.

**Update 2026-10-13 (DEC-041):** the user switched the main teaching path to **Python** ("plan all these contents in python for now, later we can add a separate section and teach it for tableau"). Learners run notebooks in **Google Colab** using **read, run, then modify** code; the four Tableau lesson drafts are kept as a later "Tableau (coming later)" section. Learner pages focus on content, not session counts or hours (DEC-039). Items below that make Tableau the required first tool or Python optional are superseded in those respects; their data, metric and boundary rules still apply.


- Working professionals with mixed experience; basic spreadsheet skills, no assumed Python or Tableau.
- Twelve two-hour live classes across several weeks (24 contact hours), plus independent practice.
- MkDocs teaching documentation developed section by section.
- Tableau Public using synthetic/public data; Tableau is a required practical tool.
- Connections to Python and pandas; explanations, examples, exercises, debugging, questions, solutions, assessments, instructor support, and independent reference resources.
- Meaningful coverage of retail/e-commerce, finance, operations, marketing, and HR; HR uses synthetic employees.
- Practical portfolio and executive briefing assessment.
- Combine the established data strategy with datasets from the [Tableau Public sample-data catalog](https://public.tableau.com/app/learn/sample-data). Include sports, technology, government and other suitable topics alongside the five required business domains.
- End-to-end process: business question → data understanding → preparation → analysis → validation → visualization → recommendation.
- First session produces planning, a detailed representative pilot outline, and workspace foundation. Full lessons, data, notebooks, and workbooks belong in a sequenced backlog.
- Bounded agent collaboration is authorized. Preserve prior work and keep instructor solutions outside learner documentation.
- User requests a concrete Markdown takeover brief for Claude after this development step. See [CLAUDE_TAKEOVER.md](CLAUDE_TAKEOVER.md); shared authority remains AGENTS.md.

## Recommendations awaiting adoption

- Meridian Commerce, a wholly fictional online retailer, remains an optional connected simulation for core departmental cases and capstone. Catalog transfer exercises retain their own contexts. Retail remains the first deeply guided case.
- Retail spans S1–S4 foundation; finance/operations/marketing/HR S5–S8 progressively reduce support; S9–S12 synthesize and present.
- Python companions optional initially; all essential assessments can be completed in Tableau without code.
- Hybrid sourcing: use suitable catalog files alongside controlled synthetic cases and supplements. NPR/calendar-2025/cutoff2025-12-31 conventions apply only to the proposed Meridian simulation. Preserve each external dataset's own dates, units, currency, provenance and real/fictitious status.
- Local Tableau Desktop Public Edition is the reference authoring path; local workbook submission is acceptable. Publishing a portfolio is optional.
- Portfolio includes all five domains; executive briefing integrates evidence from at least three, considers trade-offs, and proposes a measurable next action.

## Planning assumptions

- One class per week is illustrative only. Calendar, class size, online/in-person delivery, accommodations, and presentation logistics remain unknown.
- Recommended essential practice totals 19 hours: 60–90 minutes most weeks and 2 hours in project weeks. Optional expanded practice is about 25 hours. Both estimates need a novice pilot and workload confirmation before scheduling.
- Learners have a compatible computer, installation rights, and access to class files. Test this before teaching; do not assume a browser-only interface matches desktop instructions.
- Curated beginner tables and short workbook scaffolds keep four single-session departmental cases feasible. Additional domains are recommended as transfer/choice exercises inside existing practice or optional extensions, without increasing the confirmed 24 contact hours or replacing required five-domain evidence.

## Unresolved questions and consequence

| Question | Consequence / resolution point |
|---|---|
| Class size; in-person, remote, or hybrid; weekly cadence? | Confirm before dates and S12 presentation slots; use parallel review or recorded briefings if needed. |
| OS, installation permissions, internet/account access, accessibility needs? | Run access survey and Tableau smoke test before S1; provide paired facilitator path for temporary problems. |
| Accept connected company, NPR, 2025 simulation scope, optional-first Python? | Resolve simulation conventions before freezing its generated source contracts. The independent Superstore variant uses native source labels and its own documented development scope. |
| Practice capacity, submission channel, deadlines, feedback turnaround? | Agree before releasing assessment calendar; do not invent an LMS. |
| Individual vs team executive briefing, grading/certification policy? | Recommend individual portfolio with optional pair feedback; rubric is for feedback until policy agreed. |
| Materials/data license and redistribution permissions? | Creator must select material/synthetic-data terms; record each external source's applicable reuse/redistribution terms before release. Catalog sourcing is selected; individual files are not yet adopted. |

## Constraints and evidence boundary

Only `docs/` is built into the learner site. Planning, instructor notes, data source storage, and notebooks stay outside unless deliberately reviewed and copied. No real employee or employer data is needed. Synthetic labels must travel with exports.

Tableau Public publication makes workbooks/data accessible; local saving is available in Public Edition, per the [official Public FAQ](https://help.tableau.com/current/pro/desktop/en-us/public_faq.htm) and [saving guide](https://help.tableau.com/current/pro/desktop/en-us/publish_workbooks_tableaupublic.htm) checked 2026-10-12. The installed native app imported the prepared CSV and displayed 22 fields/6,815 rows. Worksheet/KPI and local-save checks remain incomplete; no saved reference workbook or public upload exists from this work. See STATUS for the app-control limits.

See `WORKSPACE_INVENTORY.md` for initial state, `DECISIONS.md` for rationale, and `STATUS.md` for actual verification.

## Dataset-direction update — 2026-10-12

The user selected a **hybrid** approach: existing synthetic/data-contract strategy **plus** Tableau catalog datasets and broader subjects. The catalog was inspected in a JavaScript-enabled browser. Candidate names are in DATA_CATALOG.md; four exact downloaded files are inspected in SOURCE_AUDIT.md with machine-readable profiles/checksums. SOURCE_RIGHTS.md records primary-source research and unresolved permissions/provenance. The first retail development contract is frozen; other case contracts and prepared releases remain to produce. A catalog entry is not evidence that every planned metric is supported.

No requirement for finance budget variance, promised-versus-actual service, marketing funnels or historical HR turnover is removed. Use appropriate synthetic cases/supplements when catalog sources lack those fields. HR employee-level teaching records remain synthetic. Additional real/public sources must not be relabeled as Meridian company records or joined into a fictitious shared business without an explicitly synthetic scenario.

## First retail development choices — D01

The [Superstore contract](../data/metadata/superstore/retail-v1/metric_contract.md) specifies the first local source variant: Order Date in 2023–2025, line key Row ID, Segment comparisons, reported Sales/Profit and source monetary-unit labels without inferred ISO currency or gross-margin meaning. Keep all scoped lines in the primary KPIs; exclude whole conflicted orders only from consistently filtered customer analysis. Return membership is “listed in Returns,” not event timing/refunds. Full dictionary, settings, preparation specification and private synthetic hand fixtures support the contract. These are reviewed internal development choices, not new user-confirmed business facts or permission to publish. Other domain/transfer source contracts and the connected simulation remain future work.
