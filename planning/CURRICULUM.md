# Curriculum blueprint

> **Superseded for teaching structure (2026-10-14, DEC-044).** The working plan is [COURSE_PLAN.md](COURSE_PLAN.md): 16 Python sessions of 2-hour lecture + 3-hour lab, then a Tableau section. This file is kept for its original reasoning, outcomes mapping and domain evidence design.

Planning status: recommended instructional design; no full lessons, datasets, Tableau workbooks, or numerical answers have been produced or verified by this document.

## Requirements and design choices

| Status | Item | Implication |
| --- | --- | --- |
| Confirmed | Twelve live classes of two hours each, plus practice | 24 contact hours; exactly 120 minutes per class below, including a five-minute break |
| Confirmed | Working professionals with mixed experience; basic spreadsheets; no Python or Tableau assumed | Begin with Tableau navigation and data meaning; every required task has a noncoding route |
| Confirmed | Tableau Public, using synthetic/public data | Teach public-data boundaries before opening or publishing a workbook; use reviewed course data only |
| Confirmed | Retail/e-commerce, finance, operations, marketing, and HR receive meaningful coverage | Each domain yields a question, defined metric, visual, validation record, and recommendation |
| Confirmed | Hybrid data strategy plus Tableau sample-data catalog; sports, technology, government and other topics | Preserve five required business cases; add transferable choice exercises using appropriate external/synthetic data |
| Confirmed | Practical portfolio and executive briefing | Collect evidence throughout; use the final sessions to integrate, revise, and brief |
| Confirmed | Connect Python/pandas to analytical work | Show conceptual equivalences; optional companions initially; no Python marks or prerequisite |
| Recommended | Optional connected Meridian simulation, NPR/calendar2025/cutoff2025-12-31, alongside catalog sources | Simulation conventions apply only to synthetic records; external files retain their own context/dates/currency and separate validation |
| Recommended | Retail first, with deeper guidance; gradually remove scaffolding for other domains | Reuse the analytical process, not identical worksheets |
| Assumption to validate in a pilot | Learners can use a laptop, install/access the agreed Tableau Public authoring environment, and attend synchronously | A pre-course setup check and instructor demonstration file are release gates |
| Recommendation; feasibility unverified | Essential practice is budgeted at 19 hours total: 60–90 minutes after most classes and two hours during project weeks | This is additional to the 24 contact hours; use compact evidence notes and reuse in-class artifacts |
| Optional expanded route; feasibility unverified | About 25 hours total practice including deeper independent slices and revisions | Optional Python/stretch work may add further time; no extra marks merely for volume |
| Unresolved | Class size, calendar/cadence, device/OS mix, accessibility needs, attendance/reassessment policy | These affect support staffing and briefing format, not the confirmed contact-hour total |

Tableau Public access does not authorize disclosure of workplace data. Learners use the released synthetic/public course files. Public-profile hiding is not a privacy control. The selected Tableau catalog supplies candidates; each file still needs source, availability, schema, rights and release review before adoption. See DATA_CATALOG.md.

## Observable outcomes

| ID | By the end, a learner can… | Required evidence |
| --- | --- | --- |
| O1 | Turn an ambiguous request into a decision, stakeholder, analytical question, time window, and success measure | One-page decision brief and a question-to-evidence map |
| O2 | Explain row meaning, keys, units, missing values, and relationship risks; preserve raw inputs and document preparation | Dictionary/grain statement, preparation log, row/key checks |
| O3 | Calculate and interpret counts, amounts, margins, variances, service rates, marketing efficiency, and historical workforce measures with explicit populations | Metric contracts and five domain analyses |
| O4 | Detect a plausible wrong result and validate a corrected result against the exact released dataset version | Validation log, reconciliation, and one corrected debugging exercise per domain |
| O5 | Build usable Tableau views and a dashboard that answer a decision question with clear scales, filters, labels, and context | Submitted Tableau workbook/dashboard and filter/state checks |
| O6 | Explain uncertainty, missingness, confounding, attribution, and fairness limitations without turning association into causation | Limitations in each domain note and final briefing |
| O7 | Combine departmental evidence into a prioritized, measurable recommendation and communicate tradeoffs to an executive audience | Cross-domain capstone, executive briefing, and response to questions |
| O8 | Explain how a Tableau aggregation/filter/preparation step maps to a pandas operation | Short conceptual comparison; runnable notebook is optional |

The required route is Tableau plus a spreadsheet or supplied noncoding check table. Python installation, coding, and notebook execution are not required for any outcome. O8 can be demonstrated in plain language or pseudocode.

## Teaching pattern and support

Use business decision → question → data understanding → preparation → analysis → validation → visualization → recommendation in every case. Each case release must contain a stakeholder brief, dictionary, metric contract, worked example, guided and independent exercises, debugging task, recommendation challenge, optional Python connection, validation checkpoints, and separate instructor solutions.

- **Demonstration:** instructor narrates a decision and validates a small slice; learners predict the result before seeing it.
- **Guided practice:** a checklist and scaffold support one complete attempt; learners record evidence, not only click along.
- **Independent work:** change the segment, time window, or decision and reproduce the reasoning without a recipe.
- **Challenge:** defend a recommendation, test a competing explanation, or repair a deliberately flawed analysis.

Sessions 1–4 provide explicit steps and annotated examples. Sessions 5–8 retain metric contracts and checklists but progressively omit chart/calculation recipes. Sessions 9–12 give acceptance criteria and review prompts. A short re-entry card supports missed classes; optional challenge prompts deepen reasoning rather than increasing required software complexity. Learners who finish early audit a peer's denominator or test an alternative explanation.

## Twelve-class sequence: 24 contact hours

Every minute budget sums to 120. Demonstration and guided practice include Tableau use; independent practice is hands-on. The first retail CSV exists for local development, with numerical checks complete and Tableau checks still open; other prepared case data and scaffold workbooks remain production dependencies. Do not attempt every case component from scratch in a single class: complete assigned independent extensions between classes.

| Class | Decision and essential content | Minute budget | In-class evidence / exit check | Practice after class (recommended typical hours) |
| --- | --- | --- | --- | --- |
| 1. From decision to evidence | What does management need to decide? Analytical process; source/grain/keys; Tableau Public safety; connect CSV; dimensions/measures; first chart and filter; distinguish a row from an entity | 15 diagnostic/decision; 20 demonstration; 30 guided setup/view; 5 break; 25 independent view; 15 challenge/debrief; 10 exit check | Explain one row and one distinct entity; save a first view; write a bounded question | 1.0: setup recovery, decision brief, dictionary reading |
| 2. Retail: trust the sales table | Which products/segments warrant investigation? Order-line grain; types and nulls; dates; return-list limits; distinct order count; safe preparation and source preservation | 10 retrieval/decision; 20 demonstration; 30 guided preparation; 5 break; 30 independent segment/check; 15 debugging challenge; 10 exit check | Identify line vs order counts; log a transformation and validate a small order slice | 1.5: preparation log and independent segment |
| 3. Retail: compare segment KPIs | Which retail segment deserves investigation? Source-reported Sales/Profit, AOV and profit ratio by Segment; ratio of sums; explicit source-unit and accounting limits | 8 launch; 12 grain/preparation recall; 18 demonstration; 17 guided metrics; 5 break; 20 independent analysis; 15 debugging; 13 recommendation challenge; 10 debrief; 2 exit check | Metric contracts; reconciled numerator/denominator; justified segment investigation with source limitations | 1.5: segment comparison and corrected metric bug |
| 4. Retail: trends and a decision dashboard | Which intervention should the commercial lead test? Monthly growth/trend comparisons and return interpretation; distinguish source return-list membership from refund flows in a separately labeled synthetic exercise; view selection; dashboard layout; filter behavior; annotations; accessible color and labels; defensible recommendation | 10 retrieval/decision; 20 demonstration; 25 guided dashboard; 5 break; 35 independent build; 15 peer challenge; 10 exit check | Retail dashboard combining Segment, monthly trend, and qualified return evidence; recommendation with association/causation caveat | 1.5: revise and submit retail portfolio checkpoint |
| 5. Finance: budget accountability | Where should finance investigate spending variance? Monthly department/category budget vs transaction actuals; reporting period; reconciliation; expense favorable/unfavorable semantics; avoid budget multiplication | 10 decision/data reading; 20 demonstration; 25 guided reconciliation; 5 break; 30 independent variance views; 20 debugging/recommendation challenge; 10 exit check | Reconciled totals before/after combining; signed and percent variance with zero-budget rule | 1.5: finance note, independent department, corrected join bug |
| 6. Operations: service performance | Which carrier/warehouse intervention deserves a trial? Promised/delivered dates; due shipments; overdue/open records; on-time population; median vs mean; distributions | 10 decision/data reading; 20 demonstration; 25 guided dates/rate; 5 break; 30 independent distribution/segment; 20 debugging/recommendation challenge; 10 exit check | Rate denominator includes the contract's eligible open shipments; compare tail delay and typical delivery | 1.5: operations note and missing-delivery sensitivity check |
| 7. Marketing: spend allocation | Which campaigns merit a controlled budget change? Funnel denominators; weighted conversion rate; CPC/CPA/ROAS; attributed revenue and attribution limitations | 10 decision/data reading; 20 demonstration; 25 guided funnel/efficiency; 5 break; 30 independent campaign comparison; 20 debugging/recommendation challenge; 10 exit check | Rebuild overall rate from counts; distinguish tracked conversion/revenue from causal lift | 1.5: marketing note and corrected mean-of-rates bug |
| 8. HR: historical workforce questions | Which workforce issue should HR investigate? Headcount snapshots; hires/exits; monthly average population; tenure/cohort fairness; recruitment timeline; avoid current-headcount denominator | 10 decision/data reading; 20 demonstration; 25 guided historical metric; 5 break; 30 independent cohort/recruitment view; 20 debugging/recommendation challenge; 10 exit check | Historical population reconciliation and fair comparison; no identifiable employee display | 1.5: HR note and corrected historical-denominator bug |
| 9. Synthesis: departmental tradeoffs | Which company-wide action has the strongest defensible case? Common calendar/units; relationships vs joins; comparable grain; conflicting evidence; no invented person-level links | 10 decision/evidence inventory; 20 demonstration; 25 guided synthesis; 5 break; 30 independent capstone proposal; 20 challenge/conference; 10 exit check | Capstone proposal with one decision, at least three domains, all five domain portfolio checks, and feasible validation plan | 2.0: capstone analysis and initial dashboard |
| 10. Capstone build studio | What evidence and dashboard behavior will persuade a decision-maker? Parameter/filter choices as needed; drilldown; annotations; data/version traceability; audit critical results | 10 proposal retrieval; 15 targeted demonstration; 20 guided audit; 5 break; 45 independent build/coaching; 15 challenge; 10 exit check | Draft dashboard plus reproducible validation pack; documented current limitations | 2.0: complete draft workbook and executive narrative |
| 11. Critique and briefing rehearsal | Does the recommendation survive scrutiny? Peer analytical audit; alternative explanation; executive narrative; accessibility; public-data release check; rehearsal | 10 framing/checklist; 15 demonstration; 20 guided peer audit; 5 break; 35 independent repair; 25 rehearsal/challenge; 10 exit check | Revised recommendation, peer-review response, and timed rehearsal | 2.0: final portfolio, concise briefing materials, final verification |
| 12. Executive briefing and reflection | Which action should leadership authorize, monitor, or defer? Present, defend, prioritize, and state what evidence would change the recommendation | 10 setup; 70 briefing block; 5 break; 20 synthesis/feedback; 15 individual reflection | Briefing, questions, final evidence pack, individual transfer reflection | 1.5: feedback response and portfolio polish; optional beyond assessed submission if policy requires |

Recommended essential practice budget: **19 hours**: class 1 = 1 hour; classes 2–8 = 7 × 1.5 hours; classes 9–11 = 3 × 2 hours; class 12 = 1.5 hours. Plan for **43 total hours** including contact time. Reuse in-class artifacts, use compact evidence notes, and limit each required departmental extension to one independent slice and its validation. An optional expanded route of about **25 practice hours** adds deeper segments, sensitivity checks, and presentation polish (49 total hours); optional Python work can add further time. All workload estimates are unverified until novice pilot timing; revise scope/support if essential evidence exceeds the budget. Extra volume does not itself earn higher rubric scores. Classes 5–8 rely on an instructor-provided validated starting dataset and focused analytical question. Full raw-data ingestion, advanced Tableau modeling, and Python engineering are beyond the required contact-time budget.

Class 12's 70-minute block supports at most eight presentations at six minutes plus two minutes of questions (64 minutes plus six minutes transition buffer). For a larger class, use up to eight teams with individual contributions and questions documented, or parallel assessed rooms with consistent assessors. Individual recorded six-minute briefings plus in-class panel questions are a fallback recommendation only; format remains unresolved until class size and delivery policy are known. Preserve the 24-hour live schedule.

## Domain coverage and evidence

| Domain | Primary sessions | Meaningful independent evidence | Core analytical trap | Noncoding validation / optional pandas connection |
| --- | --- | --- | --- | --- |
| Retail/e-commerce | 2–4; revisited in 9–12 | Segment growth/profit/returns question; dashboard; recommendation about a policy test | Counting order lines as orders; mean of row margins | Distinct orders and sum-based metrics checked on a small order slice / `nunique`, `groupby`, ratio of sums |
| Finance | 5; synthesis in 9 | Department variance and reconciliation note; investigation priority | Monthly budgets multiplied by transaction join | Compare separate monthly totals at common grain / aggregate before merge, validate join cardinality |
| Operations | 6; synthesis in 9 | Service comparison including overdue undelivered shipments; delay distribution | Removing undelivered records and overstating service | Eligible due population and date spot checks / datetime differences, explicit missingness mask |
| Marketing | 7; synthesis in 9 | Funnel/efficiency comparison, weighted rate, spend recommendation with attribution limit | Averaging campaign rates or treating ROAS as causal effect | Sum conversions and eligible opportunities separately / sums before division, denominator masks |
| HR | 8; synthesis in 9 | Historical turnover/headcount, recruitment timeline, cohort comparison with fairness caveat | Using current headcount for past turnover | Monthly population and hire/exit reconciliation / dated snapshots, cohort grouping |

No departmental case is merely a demonstration. Each has independent work, a debugging correction, validation evidence, and a recommendation. All five appear in the portfolio; the capstone integrates at least three, with a short screening note explaining relevance or limitations of the other two. This avoids forcing a false cross-domain relationship.

## Preconditions and mixed-experience delivery

Before class 1, provide a setup guide, small synthetic CSV, glossary, brief spreadsheet refresher, and a reversible save/open check. Diagnose basic percentages, date reading, and rows versus entities; provide recovery exercises without making Python a hidden prerequisite. Confirm the actual Tableau Public authoring/version/save workflow in production and update screenshots then. The instructor needs a working demonstration environment; an outage fallback uses supplied view exports and spreadsheet calculations for reasoning practice, followed by a Tableau recovery task. Fallback work alone does not satisfy the Tableau outcome.

At each class, use a five-minute retrieval question within the opening allocation, provide a baseline completion checklist, and separate optional stretch tasks from essential evidence. Permit learners to explain a result verbally before writing it. Use labels/text and accessible contrast rather than color alone. Publish concise recap and recovery instructions in learner docs; instructor answer keys remain outside `docs/`.

## Alternative pacing options — evaluated, not selected

The selected schedule is the confirmed **12 × 2 hours**. These alternatives are recommendations for a future cohort or explicit rescheduling only:

| Option | Contact hours | Tradeoff |
| --- | --- | --- |
| 8 × 3 hours | 24 | Fewer attendance dates; longer fatigue-prone blocks require extra breaks and consolidation; not the current schedule |
| 16 × 90 minutes | 24 | More frequent retrieval and shorter sessions; higher scheduling overhead and more transitions |
| 12 × 2 hours plus optional Python clinics | 24 required, clinic hours additional | Keeps beginner route intact; clinic staffing and time are additional, not silently included |

Do not compress five meaningful cases and the capstone into eight two-hour classes without reducing scope or adding contact/practice time.

## Design review and production boundaries

Design checks: twelve classes × 120 minutes = 1,440 minutes = 24 hours; each budget totals 120; essential practice budgets total 19 hours; O1–O8 have observable evidence; each domain has independent analysis and a specific trap; all essential work has a noncoding route. The optional expanded 25-hour route is an estimate, not a required schedule. Assessment mapping and recommended rubric are in `planning/ASSESSMENT.md`.

These are design-level checks. Actual completion times, prepared-dataset correctness, authoring workflow, screenshots, calculations, workbook behavior, and learner accessibility require a pilot with released data and real Tableau execution. The first four-source audit and [retail development contract](../data/metadata/superstore/retail-v1/metric_contract.md) now supply source evidence and definitions. Next: reproducibly prepare and independently validate retail, then produce/time the pilot before extending full lessons. The detailed Meridian/channel/refund outline remains a separately labeled synthetic reference variant; do not apply its NPR/gross-profit calculations to Superstore.

## Additional domains through transfer practice

Confirmed breadth now includes sports, technology, government and other suitable catalog topics alongside the five required business domains. Recommended implementation: introduce a short contrasting example during an existing demonstration, offer a source-specific independent slice after the essential core task, and let learners select one transfer challenge during S9 or optional expanded practice. Reuse existing independent/challenge allocations; do not add required sessions or silently increase the 19-hour essential practice estimate. If a transfer exercise replaces a practice slice, retain all required five-domain evidence.

| Choice | Candidate | Transfer outcome | Planned evidence |
|---|---|---|---|
| Sports | FIFA World Cup Match Results | Distinguish match grain from team appearances; compare rates with explicit populations | One checked comparison and a denominator/debug note |
| Technology | Mobile OS Usage; Start-up Venture Funding | Distinguish market-share percentages from counts; preserve company/round/investment grains | Trend or funding view, validation and limitation |
| Government/public sector | US Construction Spending; US Home Sales | Identify period, geography, monetary units and overlapping totals before aggregation | Time-series comparison and reconciliation/coverage note |
| Other catalog topics | Education, science, entertainment or lifestyle, after source review | Transfer grain, validation and communication skills to another context | Same compact evidence template; no additional mandatory portfolio domain |

The connected capstone can still use the synthetic core simulation to support one realistic cross-department decision. An external topic may supply an explicitly justified contextual comparison, not invented row-level links or an extra revenue stream. It does not automatically replace the three-domain synthesis requirement. Source-specific metrics and availability remain subject to file audit.
