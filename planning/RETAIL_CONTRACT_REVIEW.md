# Independent D01 review — Superstore retail-v1

Reviewed **2026-10-12**. **Recommendation: pass the first retail contract for a local-development freeze.** No blocking analytical error or contradiction was found across the reviewed dictionary, metric contract, JSON settings and preparation specification. This approves a bounded development design for D02; it does **not** approve a teaching release, public distribution, Tableau upload, or all other domain contracts.

## Scope and method

Reviewed `data/metadata/superstore/retail-v1/{dictionary.md,metric_contract.md,contract.json,preparation_spec.md}`, `scripts/check_retail_contract.py` and the [private synthetic fixtures](../instructor/source-audit/retail-contract-fixtures.json), against S01 source/profile/hash evidence and the earlier independent audit review. This role owns only this report and made no other file edits.

The lead reported a successful checker run. This reviewer did **not** treat that as independent arithmetic evidence or import its `metrics`, `ratio`, `conflicts` or `previous_month` helpers. Instead, an inline read-only script explicitly combined the fixture's individual rows, enumerated the expected order/category/return populations, and used literal calendar comparators. A separate part of that script inspected the exact XLS using direct xlrd iteration. Detailed monetary fixture values remain in the instructor JSON; they are not repeated here.

## Analytical and consistency findings

| Area | Result and consequence |
| --- | --- |
| Order date and ship boundary | Consistent half-open Order Date scope `[2023-01-01, 2026-01-01)`. Ship Date is retained even after the scope end. There is no fabricated completion/status filter or business-as-of date. The synthetic boundary fixture includes/excludes the correct endpoints and retains its crossing shipment. |
| Grain and projection | Row ID remains the unique source line key. Repeated Order ID/Product ID pairs are retained. All 22 prepared field names and their order match dictionary and JSON; 17 are source projections and five derived fields. The four omissions do not alter raw. No People join or invented currency/Channel/COGS field is specified. |
| Customer conflict and denominator | Conflicts are detected across the entire raw Orders table before any scope/filter selection. Primary segment KPIs keep all scoped lines. Customer work excludes every line of a conflicted order and applies that eligible population to Sales, orders, AOV and customer counts together. Known out-of-scope conflict records remain in the exception log. |
| Returns | Flags mean membership in a unique order list. R07 counts distinct listed orders; R08 divides by distinct orders in the same represented-line scope. Absence is not proof of no return; no event date, observation window, refund economics or category-specific returned-product claim is introduced. |
| AOV and overlapping categories | Whole-order/Segment AOV uses reported Sales divided by distinct orders. Category/product selections change the numerator to selected lines; the qualified label “Selected-line Sales per participating order” is explicit. Category order counts overlap and cannot be added to company orders. |
| Profit ratio and aggregation | Source-reported Profit divided by source-reported Sales, recomputed from totals. Negative Profit is retained. Mean line ratios and mean subgroup ratios are rejected. No gross/net-margin or inferred cost claim. |
| R10 coverage and group zero | Coverage is defined before optional group filters. A missing whole release month is a validation failure; a covered month with no selected lines can have a sample-record sum of zero plus a no-lines indicator. A genuinely unavailable month is not filled with zero, and a wholly empty selection has a no-rows display. |
| R11/R12 temporal comparators | Previous month/year means the exact calendar comparator in the same selected population, not the preceding visible mark. First/unavailable/zero prior values yield null; positive prior to covered zero current yields a decline rather than unavailable growth. Prior data must remain available before presentation filtering. Whole-year comparisons require complete matching years. |
| R13 dispatch interval | Optional mean/median has one observation per Order ID after date-stability checks. Dictionary warns against repeated-line weighting; metric contract specifies order weighting. No conflict between those statements. Dispatch interval is not delivery service. |
| Precision and units | Source-to-CSV canonical Decimal equality is separate from engine tolerances and weaker display-only checks. No per-line money rounding. Two-decimal display and ROUND_HALF_UP are teaching conventions, not evidence of currency. Ratio tolerance uses fractional representation, distinct from percentage-point display error; negative or greater-than-100% Profit ratios/growth are not clamped. |
| Freeze/publication | JSON and prose consistently preserve raw, use neutral source monetary units, keep publication false and Tableau verification false, and require a new contract version for semantic changes. Local development may proceed without inventing an ISO currency or clearing bundled/public delivery rights. |

No material JSON/dictionary/spec contradiction was found. “Pending review”/development status markers are expected at this review snapshot; lead should update them consistently only after accepting the review and record the exact documents/version frozen. The freeze is for this retail slice; controlled synthetic supplements and other domains remain separate work.

## Independent evidence actually checked

Read-only script executed with the specified environment:

```bash
PYTHONPATH=/tmp/kings-source-audit-libs \
  /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 - <<'PY'
# Independent explicit fixture arithmetic/population/date checks;
# direct xlrd source iteration; no checker helper imports or output writes.
PY
```

The abbreviated block records the actual execution route and operations, not a complete replacement for the inline script recorded in the tool transcript. Environment follows S01: bundled Python 3.12.14 and temporary xlrd 2.0.2.

Observed results:

- All core fixture expectations independently matched: line/order distinction, Sales/Profit totals, quantity, AOV, ratio of sums, listed-order share and all three intended aggregation traps.
- Independently confirmed zero-Sales versus empty-population behavior, whole-order customer exclusion and its additive bridge, and date endpoints/retained later shipment.
- Literal month lookups confirmed unavailable first/prior month, unavailable zero-prior growth, positive-to-zero current growth and the twelve-month comparator. This did not use the checker's calendar helper.
- Lead added an explicit covered-month/no-selected-lines fixture after the initial review suggestion. A second independent inline check manually confirmed its covered empty month is zero, the subsequent zero-prior growth is unavailable, and the outside-coverage prior month remains missing. No checker helper was imported. The final checker block was also read; lead reported its rerun passed.
- Independently sanity-checked positive/negative half-tie display rounding and conversion of percentage-point display tolerance to ratio units. This is reference-rule arithmetic, not a claim about Tableau formatting behavior.
- Exact source hash matched contract.json. Whole-raw conflict detection found the two expected orders. Scoped population: **6,815 lines / 3,388 orders**; customer-eligible: **6,811 lines / 3,387 orders**; excluded: **four lines / one order**. Sales/Profit/quantity bridges reconciled without rounding.
- **34 scoped lines** retain Ship Dates on/after 2026-01-01. All **36 calendar months** in the declared release scope are represented. These are count/coverage controls, not a prepared-file check.
- A separate static comparison confirmed **22 ordered prepared fields**, **17 source projections** and **13 metric IDs** agree across documents/settings. Local links in the dictionary, metric contract and preparation specification resolve.
- `git diff --check` passed at the review snapshot. No shared checker rerun, preparation, metadata rewrite or raw-file mutation was performed by this role.

## Resolved review refinement and remaining release limits

The initial sparse monthly fixture tested explicit zero versus an unavailable calendar comparator. The reviewer recommended also encoding a **covered calendar month with no lines after a group filter**, carrying coverage independently of grouped rows. Lead added that private fixture and checker block; independent manual arithmetic passed. **This refinement is resolved; no open review defect remains before local-development freeze.** D02/D03 must carry these cases, plus a wholly empty selection, through the actual prepared/Tableau implementation rather than assume a helper assertion verifies rendered missing marks or no-lines indicators.

D02 must implement immutable, reproducible output and exact source-value re-read checks against this contract. D03 must independently validate the resulting frozen prepared version, filtered populations and private answers. Actual Tableau aggregate/filter/grand-total/empty-state/calendar behavior, display rounding, workbook/device/accessibility checks and teaching timings remain unverified. Source formula values are stored values; this review performs no workbook recalculation or upstream-provider truth audit.

Rights/delivery conditions in SOURCE_RIGHTS remain in force. A local-development freeze with neutral units does not authorize a packaged workbook, learner CSV bundle or public upload. No new download, prepared dataset, learner lesson, Tableau workbook or publication was produced by this review. Lead owns final TASKS/DECISIONS/STATUS/HANDOFF integration and the transition to D02.
