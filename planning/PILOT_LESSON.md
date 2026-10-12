# Pilot lesson design — Session 3 synthetic reference: Which retail channel deserves attention?

## Status and decisions

- **Confirmed:** twelve two-hour live classes plus practice; learners have basic spreadsheet skills; no Python or Tableau knowledge assumed at entry; Tableau Public with synthetic/public data; practical portfolio and executive briefing assessment.
- **Recommended placement:** Session 3, after orientation and a Session 2 retail grain/preparation workshop. The pilot rehearses metric reasoning on prepared data; later sessions develop dashboards and returns analysis.
- **Recommended case:** Meridian Commerce, a fictional company; synthetic order lines, NPR, calendar 2025, reporting cutoff 2025-12-31. These are design choices, not confirmed user decisions.
- **Assumed readiness:** learners can connect a CSV, inspect data types, create a basic sheet and apply a date filter after Sessions 1–2. Provide a recovery route if these skills are not yet secure.
- **Production status:** detailed outline only. Dataset, workbook, screenshots, numerical answers and Tableau calculations have not been produced or verified. Proposed formulas below need testing in the selected Tableau Public version against a released dataset.

## Hybrid-source applicability update — 2026-10-12

**Current first-source mapping:** D01's [retail development contract](../data/metadata/superstore/retail-v1/metric_contract.md) is frozen after independent review. Its snapshot uses Segment, reported Sales/Profit, distinct orders, AOV and source-reported profit ratio over 2023–2025 Order Date, in source monetary units. The curriculum/assessment now name that source-backed first variant. The detailed business brief/formulas/pacing below remain the separately labeled Meridian/channel/synthetic reference, not ready-to-run Superstore instructions. D02/D03 must prepare and validate the source version before L02 translates this pacing/activity structure into the actual source-specific lesson. Return-list interpretation belongs to S4 and cannot substitute for synthetic refund economics.

The user confirmed existing strategy plus Tableau catalog datasets. This outline retains a **synthetic reference variant** with the proposed Meridian/NPR/2025 schema and unverified formulas below. [SOURCE_AUDIT.md](SOURCE_AUDIT.md) records the separate Superstore findings; its neutral units and reported metric meanings must not inherit the synthetic formula semantics. D01 now fixes the source mapping, while D02/D03 preparation/answers and L02 source-specific instructions remain to produce. Do not reconstruct COGS, reapply discounts, assume canceled/completed status, relabel the source Meridian or use return flags as refunds. Keep this reference labeled separately when adapting the teaching structure.

## Business decision and stakeholder brief

The retail director has one analyst available to investigate channel performance next month. Which channel should receive that investigation, and what further evidence should the director request before changing prices or promotions?

The director needs a comparison of discounted sales, distinct completed orders, average order value and gross profit margin. A large sales total alone is insufficient to choose an action. Learners will recommend an investigation supported by evidence, acknowledge a limitation and identify a next check. This lesson does not establish causal effects of discounts or claim that a high-margin channel should automatically receive more investment.

The analytical sequence is question → understand rows and scope → confirm preparation → calculate → validate → compare visually → recommend. All essential tasks use Tableau; Python is optional after class.

## Observable outcomes and evidence

| By the end, learners can… | Evidence to collect | Success check |
| --- | --- | --- |
| Explain the difference between an order and an order line | One-sentence grain statement plus a multi-line order inspection | Identifies `(order_id, line_id)` as the proposed line key and uses distinct order IDs for orders |
| State a metric's population and denominator | Short metric contract for AOV and margin | Includes completed 2025 orders, active filters, NPR units and pre-return scope |
| Build a channel comparison | Local workbook or agreed screenshots with four measures | Uses sums for money, distinct orders and ratio of sums for margin |
| Validate before interpreting | Completed reconciliation checklist | Records actual results, identifies one failed check or records that all specified checks passed |
| Diagnose an aggregation mistake | Written correction to one debugging prompt | Explains why line count or mean line margin changes the business meaning |
| Give a bounded business recommendation | 90-second briefing or five-sentence note | Names channel, cites two validated measures, states uncertainty and proposes one follow-up |

This is a formative portfolio component; the instructor returns feedback that learners can use in the final cross-department briefing. It is not a complete capstone.

## Data and metric contract — design proposal

### Proposed prepared input

Use `retail_order_lines.csv` from a versioned synthetic release. Actual release path and version must be filled in at production. The data designer's baseline is one line from a completed order, with `order_date` in 2025. Canceled orders are excluded during preparation and documented in a source-to-prepared reconciliation. Refund events are kept separately for a later extension. Do not quietly subtract them in this lesson.

| Field(s) | Proposed meaning and checks |
| --- | --- |
| `order_id`, `line_id` | Composite line key unique and non-null; `order_id` repeats when an order contains several lines |
| `order_date` | Order date; inclusive 2025-01-01 through 2025-12-31; no time-of-day conversion in this lesson |
| `customer_id` | Synthetic customer identifier, not a person's name or contact information |
| `channel`, `region` | Order-level dimensions: each order must have one channel and one region |
| `category` | Line-level product category; an order may span categories |
| `quantity`, `unit_price_npr` | Positive quantity and price in NPR per unit; approved rules for zero-price items belong in the final dictionary |
| `discount_npr` | Total discount for the entire line, not discount per unit |
| `gross_sales_npr` | `quantity * unit_price_npr`, before discounts, refunds and taxes |
| `sales_npr` | `gross_sales_npr - discount_npr`, before refunds; VAT/taxes and shipping excluded |
| `cogs_npr` | Total cost of goods sold for the line, excluding shipping/overheads |
| `gross_profit_npr` | `sales_npr - cogs_npr`; a negative value can be a valid business result |

All monetary fields are NPR. Validate discount bounds and line arithmetic at the precision chosen for the release. Preserve source rows; use the prepared file, not live spreadsheet repairs. The final dictionary must state whether amounts are rounded to paisa per line or only at display time. No learner should have to infer this from screenshots.

### Measures

| Display label | Population and definition | Denominator / empty group behavior |
| --- | --- | --- |
| Discounted sales (before refunds), NPR | Sum `sales_npr` for completed 2025 order lines in the active filter context | Additive over included lines; label does not mean refund-adjusted net sales |
| Completed orders | Distinct `order_id` among those lines | No rows gives no observed group; do not invent a completed order |
| AOV (before refunds), NPR/order | Sum `sales_npr` / distinct `order_id` in the same scope | Zero orders → null / "No eligible orders" |
| Gross profit margin (before refunds), % | Sum `gross_profit_npr` / sum `sales_npr` in the same scope | Zero sales → null / "Not defined"; negative profit remains valid |

Required fields with missing keys, dates or amounts fail preparation and are resolved/quarantined before release; missing money is never silently converted to zero. Missing dimensions follow a documented `Unknown` category so totals can reconcile. Missing customer ID does not erase otherwise eligible sales; customer metrics are outside this lesson.

The default filter is the full year. Any channel/region comparison must use the same date window and eligibility rules. Channel and region partition orders only after the one-value-per-order check passes. Category order counts overlap: summing them can overstate all-company orders. Filtering to a category changes AOV to **included category sales per order containing that category**, not complete-order basket AOV. Category-filtered AOV is an extension, not the essential comparison.

Do not call the baseline "net sales" without its definition. A later return-adjusted contract must name the refund cutoff and distinguish order-cohort refunds from refunds occurring during a reporting period. The baseline sales/AOV/margin here exclude all refund adjustments consistently.

### Proposed Tableau calculations — unverified

Create or use prepared money fields, then propose these calculations. Production must test field names, type behavior, null behavior, totals, formatting and current UI steps in Tableau Public.

```text
// Completed orders
COUNTD([order_id])

// AOV (before refunds)
IF COUNTD([order_id]) = 0 THEN NULL
ELSE SUM([sales_npr]) / COUNTD([order_id]) END

// Gross profit margin (before refunds)
IF SUM([sales_npr]) = 0 THEN NULL
ELSE SUM([gross_profit_npr]) / SUM([sales_npr]) END
```

The instructor demonstrates why `COUNT([order_id])` counts lines and why `AVG([gross_profit_npr] / [sales_npr])` weights small lines equally with large lines. Averages of subgroup AOVs or margins also require their respective order or sales weights. Calculate the combined ratio from numerator and denominator instead.

## Readiness and pre-class work

Learner practice before class: 20–30 minutes, using a released Session 2 prepared file, checking row meaning and reopening a saved workbook. Python installation is not a prerequisite. Ask learners to bring the dictionary, their grain statement and a local or approved submission folder.

Instructor preparation, after production dependencies are complete:

1. Freeze the dataset release, rights/provenance record, checksum, dictionary and preparation reconciliation. Confirm every row is synthetic and safe for public exposure.
2. Rehearse the full lesson using the selected Tableau Public edition. Capture actual tested connection, calculation, saving and export steps; verify offline/local saving behavior rather than assuming it exists in every edition.
3. Produce an original instructor workbook, learner checkpoint workbook where supported, screenshots, and a private answer manifest for that exact dataset version. Keep instructor answers outside `docs/`.
4. Test accounts/access, network, screen sharing, font size and CSV import on representative learner devices. Prepare an accessible tabular view of the chart.
5. Test independent computation and Tableau reconciliation. Include unequal line values, multi-line orders, at least two channels and a documented zero-denominator test fixture so the intended traps are observable.
6. Prepare a recovery pack containing public-safe screenshots, a compact evidence table and a local spreadsheet alternative. Label the fallback as interpretation practice; it does not satisfy the Tableau artifact requirement until the learner completes a catch-up task.

Tableau Public publication makes the uploaded data public. A hidden profile is not a privacy control. Use only the reviewed synthetic release, and never ask learners to upload workplace data. Public publishing is not required for this pilot; agree the tested local export or screenshot submission route before teaching.

## Live sequence — exactly 120 minutes

| Minute | Duration | Mode and analytical step | Activity and observable checkpoint |
| --- | --- | --- | --- |
| 0–8 | 8 | Launch: question | Introduce the director's decision; learners identify one measure that sales totals cannot supply. Quick confidence check determines pair support. |
| 8–20 | 12 | Understand and confirm preparation | Reopen the prepared CSV; inspect one multi-line order, key, date and money types. Learners state line grain, order denominator and pre-return scope. Use prepared input rather than repeat Session 2 cleaning. |
| 20–38 | 18 | Demonstration: analysis and validation | Instructor builds a small KPI text table, explains distinct orders, derives AOV and ratio-of-sums margin, and compares an aggregate with the private answer manifest. Pause twice for denominator predictions. Learners record a metric contract. |
| 38–55 | 17 | Guided practice: analysis → validation → visualization | Pairs reproduce a channel table and one sorted bar chart, using a consistent full-year filter and explicit NPR/% labels. Reconcile channel sums to full-year sales; check distinct order counts only after confirming channels partition orders. Instructor checks a sample from each support group. |
| 55–60 | 5 | Break | Keep the checkpoint instructions visible; no required task. |
| 60–80 | 20 | Independent work: repeat the cycle | Each learner compares channel sales, orders, AOV and margin, checks one region filter, records scope, and completes the validation checklist. Submit an intermediate artifact or show a sheet at the 72-minute checkpoint. |
| 80–95 | 15 | Debugging: validation | Diagnose one intentionally flawed sheet or calculation: line count used as orders, or mean line margin used as overall margin. Explain the mechanism, correct it and record a before/after check. Extra challenge: explain non-additive category order counts. |
| 95–108 | 13 | Recommendation challenge | Write a five-sentence note: decision, two quantitative observations with scope, limitation, next check. Pairs rehearse a 90-second briefing and ask one question about the denominator or causal claim. |
| 108–118 | 10 | Debrief and recovery | Compare approaches using validated figures released by the instructor after submission. Discuss why refunds/cost scope could change the decision. Resolve one recurring error and assign targeted catch-up. |
| 118–120 | 2 | Exit ticket | State row grain, one denominator and one recommendation limitation. Save the artifact using its release/version label. |
| **Total** | **120** | | Includes a five-minute break. |

If the demonstration runs late, reduce the optional category discussion and select one debugging prompt; preserve independent work, validation and the recommendation. Do not remove the break or make Python essential to recover time.

## Production activity specifications

### Worked demonstration

Produce a verified miniature extract containing one multi-line order and unequal sales amounts. Show raw rows → completed-order count → money sums → AOV/margin → a full-file comparison. Label every miniature number as illustrative until it is computed from the released extract. Do not supply invented totals as course answers.

### Guided work

Provide a short field checklist and partially completed metric contract. Learners add channel to rows, build the measures, format money and percentages, and document the full-year filter. The instructor models one reconciliation; each learner performs the next. Include a chart title such as "2025 discounted sales by channel — before refunds (NPR)" and a companion metric table so high sales is not confused with high margin.

### Independent work and submission

Learners select a channel for follow-up, compare it with another channel and record a region filter's effect. The essential artifact is a KPI comparison sheet or tested screenshot/export route, a scope note, validation evidence and a five-sentence recommendation. A workbook alone does not demonstrate reasoning; a written recommendation without validation is incomplete. Recommend 90 minutes of essential after-class practice to finish or revise the comparison, document the corrected bug and prepare the retail portfolio checkpoint after Session 4. An optional expanded revision may take up to 120 minutes; it is not part of the essential 19-hour course practice budget. Workload remains a planning estimate to confirm with learners; Python is not required.

### Debugging and recovery

| Symptom | Diagnostic question | Recovery action |
| --- | --- | --- |
| Orders seem too high | Does an order ID appear on more than one row? | Inspect one ID; replace line count with distinct count; recalculate AOV |
| Margin changes unexpectedly when adding a category | Is the measure an average of row percentages? | Rebuild numerator/denominator from summed profit/sales; verify filter scope |
| Currency field behaves as text | Did import infer a text field or include currency symbols? | Reconnect the approved numeric prepared CSV; review the data type; preserve source files |
| KPI and chart totals disagree | Do the sheets use the same year/region/channel filters? | Reset to the documented baseline; apply the same filters; reconcile again |
| Channel orders do not add to overall orders | Is channel constant within an order? | Stop the partition claim and flag a data-contract failure; use the reviewed release |
| Category orders exceed the company total | Can an order contain several categories? | Explain overlapping populations; do not add category distinct counts |
| Calculation is null or blank | Is its denominator zero or has the selection no rows? | Show the appropriate undefined/no-data label; never replace with an invented zero rate |
| Access or connection fails | Can the learner use a prepared checkpoint or the evidence pack? | Pair with a peer or use the fallback table; schedule the Tableau catch-up |

### Mixed-experience support

- Core route: dictionary, field checklist, metric contract prompts and checkpoint views. Offer a buddy plus instructor check at minute 72; each learner still submits individual reasoning.
- Standard route: build the comparison without starter calculations, then verify the same scope.
- Extension route: inspect category non-additivity or explain the sales-weighted margin mathematically. Extension work is not required for core completion.
- Use readable labels, a table alternative to each essential chart, keyboard-accessible materials where supported, and an asynchronous recovery pack. Pairing must not prevent a learner with access needs from demonstrating the outcomes individually.

## Optional Python/pandas connection

After class, a future companion notebook can load the exact released CSV, inspect duplicate composite keys, use `nunique` for orders, group money by channel and calculate ratios after aggregation. Start by mapping spreadsheet/Tableau concepts to a table, grouping and aggregation; do not assume syntax knowledge. Demonstrate that `groupby(...).mean()` on row-level margins answers a different question.

The notebook must use the same filters, missing-value rules, rounding and zero-denominator behavior, and compare its outputs with the Tableau result and private answer manifest. No notebook or output has yet been built or executed. Optional Python completion must not change the assessed Tableau minimum.

## Verification and release gate

Before classroom use, record actual commands, dataset version/hash and outcomes in the private validation record:

1. Run the released generation/validation procedure documented in `data/README.md`; preserve raw sources and provenance. Validate keys, dates, allowed values, order-level channel/region consistency, missingness, status exclusions and line arithmetic.
2. Independently compute baseline rows, distinct orders, sales, profit, AOV and margin; repeat by channel and one region filter. Establish monetary comparison tolerance from the release's rounding contract.
3. Compare those exact values with Tableau grand totals and filtered views. Validate that grand-total AOV/margin are recomputed ratios, and test missing/zero-denominator behavior with a separate fixture.
4. Store worked answers, debugging corrections, accepted interpretation variants and rubric guidance under `instructor/`, tied to the version/hash. Learner sheets must not link to them.
5. Rehearse timing and mixed-experience recovery with a representative beginner. Confirm the 120-minute plan is feasible; log actual issues and adjust before release.
6. Inspect learner-site output for accidental answers, planning links or private data. Run the documented docs/link/build checks. A successful MkDocs build alone does not verify the lesson's calculations.

**Current evidence:** this synthetic reference outline is design-aligned with its proposed pre-return contract and Session 3 pacing. No synthetic source release, synthetic lesson answers, Tableau UI/workbook, notebook or teaching timing has been empirically verified. The separate source-backed Superstore variant now has a reviewed D01 contract and private source/edge checks; it still needs D02/D03 and source-specific instructions. Supported Tableau edition/device setup, tested submission route and actual novice timings remain open.
