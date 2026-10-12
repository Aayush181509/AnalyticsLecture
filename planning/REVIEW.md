# Foundation review — 2026-10-12

## Scope and disposition

**Disposition: suitable for planning/foundation handoff. Not a classroom release.** All concrete review findings below are resolved in source. Full lessons, datasets, exact numerical answers, notebooks and Tableau workbooks remain future work behind explicit release gates.

Reviewed shared instructions/context/state, curriculum, assessment, all five case briefs, data contracts, pilot, learner pages/navigation, documentation plan, backlog and instructor/data separation. The reviewer read the reusable reviewer brief and owned only this report during review; source repairs were made by the lead or assigned authors. The reviewer originally authored the pilot outline, so its review is a second-pass consistency check, not a fully independent author review. Other authors' analytical plans were reviewed independently.

Severity meanings: **High** would invalidate the planned analysis or expose private content; **Medium** is a substantive contract or teaching alignment gap to repair before production; **Low** is a consistency/clarity improvement. Findings marked resolved were re-read in current source; this is not a claim of executable verification.

## Findings and integration repairs

| ID | Severity / state | Location | Consequence and repair reviewed |
| --- | --- | --- | --- |
| R01 | Medium — resolved | `CURRICULUM.md`, S3/S4; learner roadmap; `TASKS.md`, L03 | S3 previously promised a growth/discount-policy analysis while the detailed pilot taught a channel KPI snapshot. S3 now names channel comparison; S4 and its production acceptance explicitly own monthly growth and return interpretation. |
| R02 | Medium — resolved | `DATA_STRATEGY.md`, marketing; `CASE_STUDIES.md`, marketing | A last-click attribution label was not supported by any proposed touchpoint source/window/tie rule. The design now uses synthetically assigned single-campaign attribution and explicitly disclaims validation of a last-click claim. Daily conversions reconcile unique credited orders under the one-order-per-purchasing-session simplification. |
| R03 | Medium — resolved | `DATA_STRATEGY.md`, finance | Grand-total variance could have silently included actuals whose budget is unknown. The authoritative contract now limits comparable variance totals/percentages to known-budget cells and separately reports unknown-budget actuals. Explicit zero budgets remain distinct from missing budgets. |
| R04 | Medium — resolved | `DATA_STRATEGY.md`, retail source schema | Multiple partial refunds needed cumulative bounds and a recovered-COGS limit. The source contract now caps quantities/refunds and recovered cost against original/proportional line amounts and requires explicit rounding-remainder allocation. |
| R05 | Medium — resolved | `DATA_STRATEGY.md`, operations and HR sources | Negative completed durations and future HR observations needed explicit constraints. Delivered dates must not precede dispatch or exceed cutoff; observed HR dates cannot exceed cutoff, and scheduled future starts/exits are not observations. |
| R06 | Low — resolved | `DATA_STRATEGY.md`, requirements; `CASE_STUDIES.md`, synthesis and retail | Optional-first Python is labeled recommended rather than user-confirmed; synthesis now agrees on at least three domains with all five in the portfolio; proposed retail pilot slug matches S3. |
| R07 | Low — resolved | `DATA_STRATEGY.md`, recruitment schema | Recruitment job-family comparisons lacked a job-family field on requisitions. The proposed source now contains it. |
| R08 | Low — resolved | `PILOT_LESSON.md`, independent-work paragraph | Pilot practice previously said 90–120 minutes while the essential curriculum budget assigned S3 90 minutes. The lead clarified **90 minutes essential, up to 120 minutes for optional expanded revision**, preserving the 19-hour essential estimate. Actual workload still requires the novice trial. |

The lead had identified several repairs before this reviewer pass; this report records verification of the resulting source contract, not sole discovery credit. R01/R02 were specifically raised during this pass. The lead owns final source integration and state logs.

## Analytical design checks

- **Retail:** completed order lines are not orders; distinct counts use the current population. Pre-return sales, AOV and gross margin share the same refund/cost/date scope. Margin uses summed profit divided by summed sales. Category distinct-order populations overlap; category sales per containing order is distinguished from full basket AOV. Cohort-refund amounts and refund-event-period totals remain separate; recent cohorts have shorter follow-up.
- **Finance:** independent aggregation precedes one-to-one combination at month–department–account grain. Union key coverage retains actual-only and budget-only cells. Credits remain signed, expense favorability is explicit, and absence becomes zero only after completeness checks. Missing budget and approved zero budget are different states.
- **Operations:** due-shipment denominator includes pending due shipments, excludes future-due shipments and exposes unknown promises. Split shipments use shipment IDs. Completed lead times do not pretend to include unresolved durations. End-of-day due-today failures can correctly have zero days past due.
- **Marketing:** campaign-day amounts/counts are disjoint under the simplified event definition; rates are ratios of sums. Attribution is one campaign per credited order and is descriptive. Attributed revenue is part of retail revenue, not additional company revenue; ROAS does not establish profitability or causal lift.
- **HR:** first-inactive exit dates and the opening/closing stock convention reconcile hires and exits. Company and department totals live in separate prepared tables; department bridges include transfers. Annual turnover recomputes its historical exposure denominator. Active tenure, completed service and open recruitment age are distinct populations. Same-day transfer/exit behavior remains an explicit D01 definition/fixture dependency.

All five briefs contain a stakeholder decision, dictionary/metric specifications, worked/guided design, independent practice, debugging, recommendation challenge, optional pandas connection, validation and separate future instructor solutions. These components are specifications, not produced assets.

## Feasibility and first-session completeness

The twelve-class plan preserves 24 contact hours and breaks. Prepared, checked beginner tables and compact after-class notes make the four single-session departmental cases plausible; actual novice completion is unverified. S4's trends, returns and dashboard combination is the most obvious next pacing risk: production should use a checked return summary rather than introduce raw event modeling and dashboard construction together. If rehearsal overruns, move deeper refund modeling to the optional source challenge while retaining essential return interpretation.

All five domains require independent evidence and one corrected bug. The final briefing integrates at least three, with the other two screened for relevance/limits. Conceptual pandas mapping has a plain-language route; executable Python remains optional. Briefing capacity is explicitly bounded at eight presentations, and class-size/delivery alternatives await a decision.

The requested initial inventory, context, curriculum/pacing options, five briefs, data/metric strategy, MkDocs navigation/template, detailed pilot, dependency backlog and reusable role briefs are present. Shared state/decision/handoff finalization remains the lead's integration task; its completion must be checked in final state rather than inferred from this report. Full lesson production is correctly deferred.

## Actual verification evidence and limits

Reviewer commands run successfully:

- `python3 scripts/check_docs.py`: **PASS**, six learner Markdown pages; local inline links, navigation targets and docs boundary checked. The script explicitly does not validate remote links, anchors, reference links, rendered layout or analytical results.
- `git diff --check`: passed at the review snapshot.
- Inline Python parsing the actual curriculum rows: **12 class budgets each sum to 120 minutes**, essential practice totals **19 hours**. Actual assessment weights parse as **15+25+20+15+15+10 = 100%**. Twelve classes imply 1,440 contact minutes / 24 hours; plus practice implies 43 essential hours. Six-minute briefings plus two-minute questions give eight slots / 64 minutes within the 70-minute block.
- An independent inline Python logic check enumerated **21 artificial valid hire/exit combinations** around January boundaries and confirmed `closing = opening + hires - exits` using the proposed formulas. This tests design semantics only; it is not an answer check against course data.
- Read learner source and navigation: no local links to planning or instructor answers found; only `docs/` is the configured MkDocs source. Synthetic/public publication constraints and public-profile limits are explicit.

**Lead-reported evidence, not rerun by reviewer:** strict MkDocs build passed in `/tmp/kings-data-docs-venv` with output `/tmp/data-analytics-site-check`. The lead attempted browser visual review; the in-app browser was unavailable and Chrome refused the file URL under its URL policy. No workaround was attempted. Rendered visual QA remains unverified; successful build/link checks do not establish visual quality.

**Not verified by this review:** real dataset values/rights, generator correctness, source/prepared reconciliation, Tableau calculations/UI/save behavior/workbooks, notebook execution, exact answer tolerances, teaching timings, device/accessibility behavior, grading reliability or deployment. No dataset was adopted, no source files replaced, and no publication or deployment was used as a check.

## Handoff

Lead: finish status/decisions/handoff and repeat final diff/status/docs checks after the last edit. Next production work is D01 contract/fixture freeze, then D02/D03 retail generation and independent exact-version checks. Only then produce/rehearse S1–S3 and the pilot. Preserve the unresolved logistics, licensing and submission decisions as explicit requirements to settle before classroom or public release.

## Hybrid sourcing integration review — 2026-10-12 (lead)

The user subsequently selected the existing strategy plus Tableau catalog datasets and broader subjects. This update supplements the earlier review; it does not claim that the earlier synthetic schema matches any external file. Lead reviewed current DATA_CATALOG, revised source strategy and core/extension briefs, curriculum/assessment, pilot applicability, learner pages and backlog.

Checked: the five original cases and analytical safeguards remain; sports/technology/government have concrete transfer briefs; catalog listing evidence is separated from unperformed downloads/schema/rights/answer checks; native currency/dates/context are preserved; simulation conventions apply only to simulation; no false source-to-company joins are proposed; core outcomes/contact time remain intact; the pilot is explicitly a synthetic reference variant until mapped to an audited external source. Candidate selection/audit S01 precedes source-specific D01 contracts and exact-answer production. No material design contradiction identified in the reviewed integration.

The catalog was observed by lead in the browser, not by the case-design worker. Source files have not been inspected. Source-specific answers, file availability, terms and Tableau behavior remain future audit/production work. Current docs/link/build and arithmetic checks are recorded in STATUS.md; those checks do not validate external datasets.
