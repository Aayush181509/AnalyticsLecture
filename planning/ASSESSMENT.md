# Assessment and evidence plan

Status: recommended assessment design for the confirmed practical portfolio and executive briefing. No grading weights, pass threshold, late policy, or presentation group size has been agreed by the user. No numerical answer key or Tableau workbook is verified by this plan.

## Assessment intent and evidence

Assess the full analytical process: decision → question → data understanding → preparation → analysis → validation → visualization → recommendation. A polished chart cannot compensate for an invalid denominator or an unsupported decision. Required assessment uses Tableau and a noncoding validation route. Python companions are optional and bring no extra marks merely for using code. The recommended essential practice budget is 19 hours total (60–90 minutes after most classes; two hours after classes 9–11), reusing in-class artifacts rather than producing parallel reports. An optional expanded route is about 25 practice hours; extra volume alone earns no extra marks. Workload feasibility is unverified until a novice pilot.

Learners submit a portfolio containing all five domains and one executive capstone that integrates at least three domains. The other two receive a short relevance/limitation screening note; learners must not invent a causal or row-level link to force integration. A recommended capstone scenario is a fictional Meridian Commerce leadership decision about the next quarter's investment or improvement priority, using synthetic 2025 evidence in NPR with an analytical as-of date of 2025-12-31. The company, currency, calendar, and scenario are recommendations, pending integration with the released data contracts.

## Required submissions

| Item | Minimum contents and format | Submission point | Evidence/outcomes |
| --- | --- | --- | --- |
| Decision and data brief | One page: stakeholder, decision, bounded questions, period, success measure, row meaning/keys, units, source/version, intended checks | Draft after class 1; updated in class 2 | O1, O2 |
| Retail case | Tableau workbook or approved equivalent export with editable workbook available to assessor; compact analysis note; metric contracts; preparation and validation log; corrected count/grain bug; class-3 Segment comparison using reported Sales/Profit, AOV and source-reported profit ratio; class-4 monthly trend/growth and qualified return-list interpretation, with synthetic refund examples separately labeled | After class 4 | O1–O6; deeply guided baseline |
| Finance case | Variance view and concise decision note; separate budget/actual reconciliation; signed and percent variance rule; corrected join-multiplication bug | After class 5 practice | O2–O6; finance |
| Operations case | Service rate and delay-distribution views; explicit due/eligible population including treatment of open shipments; missing-date sensitivity note; corrected exclusion bug | After class 6 practice | O2–O6; operations |
| Marketing case | Funnel/efficiency comparison; sum-based overall rate; spend recommendation; attribution caveat; corrected mean-of-rates bug | After class 7 practice | O2–O6; marketing |
| HR case | Historical workforce and recruitment/cohort views; population reconciliation; fair-comparison caveat; corrected historical-denominator bug | After class 8 practice | O2–O6; HR |
| Python connection | A short explanation mapping one preparation step, one aggregation, and one validation step to pandas concepts; plain language/pseudocode accepted | By class 9; optional notebook appendix | O8; no execution required |
| Capstone proposal | One decision; at least three domains; proposed metrics and links; source/grain compatibility; validation plan; two-domain screening note; expected action and limitations | Class 9 exit gate | O1, O2, O6, O7 |
| Draft capstone and peer audit | Draft Tableau dashboard/workbook; validation pack; critical-result audit by a peer; response and revision log | Class 10 draft; class 11 audit/rehearsal | O3–O7 |
| Final capstone and briefing | Editable Tableau workbook; executive briefing material; source/version and metric appendix; validation pack; prioritized recommendation, tradeoffs, risks, and monitoring plan | Class 12; final exact deadline unresolved | O1–O7 |
| Individual reflection/contribution | Half to one page: own contribution, a corrected error, what could change the recommendation, and one transferable method | After class 12 within agreed deadline | O4, O6–O8; individual accountability |

Recommended packaging: one named folder or archive with `README`, `workbooks/`, `analysis-notes/`, `metric-contracts/`, `validation/`, and `briefing/`. Include dataset release ID/checksum in the README and cite any approved external source. Preserve the provided raw files; record transformations instead of overwriting them. Exact filename conventions and submission platform are unresolved production details. A screenshot alone does not establish an editable, functional Tableau artifact.

Each domain note can be short (about 200–300 words excluding evidence): state the decision, define the population, give the finding with units and dates, cite a check, recommend an action, and state a limitation. Reuse shared definitions by reference while documenting domain-specific changes. One independent slice and its validation meets each required departmental extension; deeper segments are optional. Avoid duplicating the same prose in multiple files.

## Metric contract and validation expectations

Every assessed metric names its grain, key(s), unit, date window/as-of date, filters, numerator, denominator, zero-denominator behavior, missing-value behavior, and aggregation. Amounts and rates must be distinguishable. Validate the ratio of sums where appropriate; do not reward a mean of subgroup rates unless the question explicitly needs that statistic.

The validation pack must include:

1. Dataset release ID and checksums; raw/prepared provenance and transformation log.
2. Row/key/null checks and at least one manually checked small slice or independently computed noncoding check table per domain.
3. Reconciliation of critical totals and entity counts before/after preparation or combining tables; budgets checked at monthly department/category grain.
4. A corrected bug per domain with wrong reasoning, correction, numerical comparison against the exact released version, and effect on the recommendation.
5. A missingness or denominator sensitivity check where relevant (especially open shipments and historical headcount).
6. Dashboard interaction checks: date/segment filters, reset/default state, labels, totals, empty selections, and no unexplained difference from the validated check totals.

Instructor solutions must be calculated independently against the exact dataset release and stored in `instructor/`. Dataset-dependent tolerance and rounding rules belong in the released instructor check specification. Do not invent expected totals now. Where a result differs, first determine whether the population, filter, date boundary, or rounding differs; do not silently change the answer key.

## Formative gates and recovery

These are recommended feedback gates, not agreed pass/fail rules. Diagnose, repair, and resubmit before dependent work. A learner can progress on other tasks while a repair is underway, but cannot treat unresolved critical results as final evidence.

| Gate | Timing | Observable check | Recovery |
| --- | --- | --- | --- |
| G0: ready to author | Before/class 1 | Opens synthetic CSV, connects in Tableau, saves/reopens agreed artifact | Setup support; documented catch-up Tableau task after any outage fallback |
| G1: grain and preparation | Class 2 | Correct row/entity explanation; count reconciliation; preserved raw data | Rework a three-order sample, then repeat full-data check |
| G2: retail baseline | Class 4 | AOV/profit ratio/order counts use the selected source contract; dashboard supports the question | Repair metric and rerun view/filter checks before using as capstone evidence |
| G3: departmental evidence | Classes 5–8 | Each domain has independent finding, corrected bug, validation, and recommendation | Targeted denominator/join/date/cohort exercise with reassessment of affected artifact |
| G4: feasible capstone | Class 9 | One decision, three justified domains, compatible grains/calendar, bounded scope | Narrow the decision; use separate departmental views if a join is invalid |
| G5: defensible draft | Classes 10–11 | Peer checks one critical result and one competing explanation; learner resolves feedback | Repair evidence, qualify uncertainty, or withdraw unsupported claim |
| G6: release and briefing readiness | Class 11 | Only reviewed synthetic/public data; functional Tableau artifact; timed briefing; cited dataset version | Remove unsafe/unreviewed content and repair the submission before any public sharing |

Provide a short instructor feedback note for each gate: observed evidence, critical issue if any, and one next action. Stronger learners can investigate sensitivity, confounding, or scenario alternatives; do not turn optional challenge work into a hidden prerequisite.

## Recommended analytic rubric

Recommendation: score six criteria on a four-level scale. For each criterion, award its weight × level ÷ 4; absent evidence receives zero. This provides a transparent 100-point working rubric without establishing an official grading policy. Any pass threshold, grade bands, rounding, moderation, remediation, or late policy needs a separate user decision. Use the same dataset/version and rubric calibration examples for all assessors.

| Criterion | Weight | 4 — strong, independently defensible | 3 — sound and usable | 2 — developing, substantive repair needed | 1 — limited or unreliable |
| --- | --- | --- | --- | --- | --- |
| Decision framing and metric contracts | 15% | Decision and success measure bounded; all critical populations/windows/units/zero/missing rules explicit; measures directly serve the decision | Clear decision and correct core definitions; minor omissions do not change interpretation | Broad decision or unclear population/filter; one important definition needs repair | No actionable decision; definitions largely missing or contradictory |
| Preparation and analytical correctness | 25% | Grain/relationships preserved; five domain methods correct; critical calculations reproducible; aggregation and historical populations justified | Core results correct with traceable preparation; small noncritical issues remain | Join, date, denominator, or aggregation issue affects an important result, but some correct work is present | Core results cannot be trusted; repeated row/population errors or untraceable preparation |
| Validation and reproducibility | 20% | Exact release traceable; independent slice checks and reconciliations complete; all five bugs explained and corrected; interactions checked | Critical checks and corrections complete; minor documentation gaps | Checks mostly visual or incomplete; one material discrepancy unresolved | Little usable validation; sources/version unclear; unexplained totals treated as facts |
| Tableau visual communication | 15% | Views match questions; clear labels/units/date context; accessible encodings; filters work and support exploration; dashboard directs attention | Usable dashboard and appropriate views; small layout/label issues | A misleading encoding, unclear filter state, or missing context materially hinders use | Required Tableau artifact absent/nonfunctional or charts misrepresent evidence |
| Recommendation, synthesis, and limitations | 15% | Three-domain synthesis weighs tradeoffs; all five domains covered in portfolio; recommendation prioritized with owner/monitoring; plausible alternatives and limits explicit | Evidence supports a feasible action; three-domain synthesis and limitations present | Action weakly linked to evidence, integration superficial, or causal/attribution caveat insufficient | Unsupported recommendation; major overclaim; little cross-domain reasoning |
| Executive briefing and individual explanation | 10% | Concise decision-first briefing; answers challenge with evidence; contribution and pandas conceptual mapping clear; states what would change conclusion | Clear briefing and competent questions; individual work and conceptual connection explained | Overlong/unclear narrative, weak defense, or incomplete individual explanation | Cannot explain own work or key assumptions; essential briefing evidence missing |

Recommended integrity rule: mark a materially wrong critical metric as needing revision and prohibit treating the affected recommendation as verified until corrected. Report the relevant criterion score and repair requirement clearly; do not hide the issue inside an overall average. Whether this also imposes a formal grade cap is unresolved and must not be assumed.

## Evidence-to-outcome and domain mapping

| Outcome | Main assessment evidence | Domain coverage |
| --- | --- | --- |
| O1: bounded business question | Decision brief, retail note, capstone proposal/briefing | All five briefs; capstone selects at least three |
| O2: understand/prepare data | Dictionary, contracts, transformation/reconciliation log | All five; finance grain and HR population receive explicit checks |
| O3: calculate/interpret metrics | Five case analyses, final workbook | Retail amounts/counts/margins; finance variance; operations rates/distributions; marketing efficiency; HR historical measures |
| O4: validate/debug | Five corrected bugs and exact-version validation pack | One independent correction per domain |
| O5: Tableau communication | Retail dashboard, domain views, capstone dashboard/interactions | All five have views; selected domains integrated for briefing |
| O6: qualify conclusions | Domain limitations, sensitivity checks, briefing questions | Retail association; finance period/category comparability; operations missingness; marketing attribution; HR cohort fairness |
| O7: prioritize and brief | Cross-domain capstone, monitoring plan, Q&A | At least three integrated; remaining two screened explicitly |
| O8: Python connection | Plain-language mapping or optional notebook plus individual explanation | One chosen domain with preparation, aggregation, and validation connections |

Optional notebooks may demonstrate extra fluency but cannot substitute for required Tableau evidence. Working code without an explained business decision is insufficient.

## Executive briefing format and feasibility

Recommended maximum: six minutes of presentation plus two minutes of questions. A concise deck, Tableau story, or dashboard-led narrative is acceptable; slide production is not mandatory. Suggested flow: decision requested; two or three evidence-backed findings; cross-domain tradeoff; recommended action and owner; monitoring measure and review period; limits/next evidence. Keep metric definitions, checks, and detailed slices in an appendix for questions.

The 70-minute class-12 presentation block accommodates eight presentations (64 minutes) with six minutes transition buffer. Class size is unresolved. If there are more than eight learners, choose up to eight teams with individual contributions/questions assessed, parallel staffed rooms, or an agreed recorded-briefing format with live questions. Team grading, individual marks, and recording consent require an explicit delivery decision. Do not promise individual live briefings for an unlimited cohort within two hours.

Recommend group practice and peer review while keeping each learner responsible for explaining a metric, a check, and a limitation. Public Tableau publication is optional unless a later explicit course policy requires it; submission can use the approved editable workbook workflow. Any publication must contain only reviewed synthetic/public material, including workbook extracts, tooltips, hidden sheets, and metadata.

## Design review, uncertainties, and next action

Design-reviewed: every outcome maps to evidence; all five domains require substantive independent work; rubric weights total 100%; essential assessment has a noncoding path; presentation capacity is bounded; instructor answers and internal plans are excluded from learner publication.

Not yet verified: dataset answers, expected tolerances, Tableau calculations/interactions, save/export workflow, learner completion time, rubric inter-rater reliability, and actual class-size logistics. The official grading policy, submission platform, deadlines, collaboration rules, accessibility arrangements, and reassessment policy remain unresolved. Next production step: use the validated retail pilot release to create one exemplar submission and instructor scoring annotation, then time a novice attempt and calibrate the rubric before extending full assessment materials.

## Hybrid sources and transfer choices — 2026-10-12

Use the established data strategy alongside reviewed Tableau catalog datasets. All five core domains remain required; sports, technology, government and other subjects provide recommended choice/transfer practice. Assess the same reasoning, validation and communication criteria regardless of source. Extra domains or more charts do not earn marks by volume.

Each external-source submission records its actual source/file version, units, dates and applicable terms; each synthetic supplement is clearly labeled and traceable. Do not grade against Meridian/NPR/2025 answers when the learner uses an external file with different semantics. An external business-case substitution needs an approved metric/field mapping that still demonstrates the required outcome; aggregate employment statistics alone cannot demonstrate employee turnover. The connected simulation remains a useful capstone path; unrelated catalog files must not be portrayed as one company or joined to manufacture a cross-domain story.
