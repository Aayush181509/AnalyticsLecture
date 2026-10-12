# Implementation backlog

Updated 2026-10-12. Status definitions: DONE = acceptance met with stated evidence; READY = dependencies met; PLANNED = depends on earlier work; IN PROGRESS = some checks complete, acceptance still open; NEEDS INPUT = explicit decision or external setup required. Foundation, source inspection, the first retail contract and D02 preparation are complete. D03 validation is in progress; remaining Tableau checks lead the next session. No inspection/design completion implies publication permission.

| ID / priority | Task | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|
| F01 / P0 | Inspect and preserve workspace | — | DONE | Inventory records tracked files, initial changes, instructions, tooling, legacy copy. |
| F02 / P0 | Establish context and teaching constraints | F01 | DONE | Confirmed user answers separated from recommendations and open questions. |
| F03 / P0 | Integrate curriculum, cases, data, assessment, pilot | F02 | DONE | All five domains, 24-hour sequence, metric contracts, detailed 120-minute pilot and review are coherent. |
| F04 / P0 | Establish MkDocs foundation and shared guidance | F01 | DONE | Safe learner navigation, template, role briefs, README/entry files, strict build and link checks recorded. |
| R01 / P0 | Confirm remaining logistics and teaching defaults | F03 | NEEDS INPUT | Record class size/format/cadence, device survey, workload, local submission channel, story/currency/date convention, grading/team policy. |
| S01 / P0 | Audit first Tableau catalog candidates | F03 | DONE | Four originals preserved/hash-checked; actual schemas, keys, dates, missingness and internal controls inspected; source/provider terms researched with unresolved release conditions recorded; recommended roles/gaps in SOURCE_AUDIT.md and SOURCE_RIGHTS.md. No source-derived release approved. |
| D01 / P0 | Freeze first retail source data/metric contract | F03, S01 | DONE | All 25 raw fields/22 prepared fields documented; 13 metric definitions, scope/units/keys/returns/customer/precision policies, machine settings, preparation spec and private hand fixtures reviewed independently. Exact-source/fixture checker passes. Frozen local development only; other domain/transfer contracts remain future work. |
| D02 / P0 | Prepare first retail source | D01 | DONE | Implement frozen Superstore projection reproducibly; original unchanged; immutable output/contract/script hashes, typed CSV re-read and exception bridge; seed not needed for sourced data; defects separate; publication=false until permitted delivery/release review. |
| D02R / P1 | Freeze/prepare controlled retail refund and cost supplement | D01, V01 | PLANNED | Separate synthetic contract, explicit units/dates/sale cohort/event cutoff, refund/quantity/cost-recovery limits and exact hand checks; reproducible seed/config if generated; no invented source facts appended to Superstore. |
| D03 / P0 | Validate retail reference answers and Tableau behavior | D02 | IN PROGRESS | Keys, arithmetic, returns, filter effects and order counts checked independently against exact CSV; hand check reconciles; answers in instructor only. Actual Tableau whole/Segment/Region/eligible/Category and grand-total/empty/zero comparisons with version/evidence. Local import passed; worksheet checks remain. |
| L01 / P0 | Produce and rehearse S1–S2 foundations | D03, R01 | PLANNED | Learner setup/preparation pages, small guided tasks and recovery instructions; Public/local-save smoke test on actual target devices; no Python prerequisite. |
| L02 / P0 | Produce S3 retail pilot and private solutions | L01, D03 | PLANNED | All PILOT_LESSON sections become actual instructions; questions/hints/answers tested on same CSV version. |
| V01 / P0 | Trial pilot before extending production | L02 | PLANNED | Fresh Tableau run with version recorded; KPI cross-checks and timed novice trial; revise overloaded tasks and capture accessibility feedback. |
| L03 / P1 | Produce S4 retail dashboard and portfolio checkpoint | V01, D02R | PLANNED | Monthly growth and qualified return-list interpretation; separate controlled refund/cohort example; dashboard, critique prompts, alternative acceptable recommendations, rubric feedback and exact-data solutions. |
| D04 / P1 | Source/generate and validate finance data | D01, V01 | PLANNED | Monthly budget and ledger reconcile; intentional duplication trap reproducible; cost favorability and zero budgets tested. |
| L04 / P1 | Produce S5 finance case | L03, D04 | PLANNED | Beginner prepared source and source-model extension; favorable/unfavorable variance task, debug, recommendation and separate verified answers. |
| D05 / P1 | Source/generate and validate operations data | D01, V01 | PLANNED | Frozen due cohort includes overdue open shipments; future/missing dates flagged; hand-worked denominator and median checks. |
| L05 / P1 | Produce S6 operations case | L04, D05 | PLANNED | On-time service dashboard, pending shipment debug, completeness checks and feasible follow-up action. |
| D06 / P1 | Source/generate and validate marketing data | D01, V01 | PLANNED | Additive funnel counts and spend, attribution contract, weighted-rate counterexample, zero denominators and unassigned orders tested. |
| L06 / P1 | Produce S7 marketing case | L05, D06 | PLANNED | Weighted metrics, campaign comparison and attribution-limit challenge; verified solutions. |
| D07 / P1 | Generate/validate synthetic HR data | D01, V01 | PLANNED | Employment spells, historical snapshots, exits and recruitment dates reconcile; synthetic-only, no real identifiers; small cohorts represented carefully. |
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
