# Superstore retail contract v1

Status: **frozen local-development specification, 2026-10-12**, following the [independent D01 review](../../../../planning/RETAIL_CONTRACT_REVIEW.md). This is an internal contract for local preparation, not a dataset release or user-confirmed business scenario. It uses the inspected Tableau sample alongside the retained synthetic strategy. No Tableau workbook or formula has been executed. Dictionary: [dictionary.md](dictionary.md); executable settings: [contract.json](contract.json); transformation plan: [preparation_spec.md](preparation_spec.md).

## Decision and population

The analyst supports a fictional retail director deciding **which customer segment deserves further investigation and which evidence to request before changing a promotion**. The S3 snapshot compares reported Sales, distinct orders, AOV, reported Profit and source-reported profit ratio by Segment. Association between discounts and performance does not establish causation. S4 may add calendar trends and the separately qualified return-list comparison. No real commercial decision is supported by this fictitious sample.

- Source is the exact XLS acquired 2026-10-12 at the path/hash in contract.json and the [audit manifest](../../catalog-audit-2026-10-12/source_manifest.json). Call it “Superstore sample, audited 2026-10-12”; retain the catalog's different EU title only in provenance. Actual file geography is US/Canada. It is not Meridian Commerce.
- **Frozen development population:** `2023-01-01 <= Order Date < 2026-01-01`, date-only calendar comparison, with all source order lines in that interval. Retain Ship Date even when it falls in 2026. No additional completion/cancellation filter exists. No date is invented or relabeled.
- Retrieval date identifies the file snapshot; it is **not** an observed business cutoff or return-event date. The full workbook contains later sample orders; they are excluded by the order-date scope, not deleted from raw data.
- Grain is one source order line. Source Row ID is the unique line key; Order ID may repeat. Preserve all scoped lines, including repeated Order ID/Product ID pairs. There is no justified source deduplication in this retail version.
- All required source fields are nonmissing in this snapshot. Unexpected missing keys, dates, Sales, Profit, Quantity or dimensions stop preparation; do not impute them or silently drop rows. Empty strings count as missing for text keys/dimensions. Zero values and negative Profit retain their meaning as source values.
- Monetary unit label is **source monetary units**. ISO currency is unknown. No currency symbol, conversion, inflation adjustment, cross-currency claim, gross-margin label or COGS reconstruction is permitted. Neutral labels resolve the current teaching contract; stronger accounting/currency claims require new source evidence and a revised contract.

Source accounting definitions remain unknown. “Reported” means the value supplied in the source column, not an assertion about refunds, tax, cost allocation or recognition. Sales are not renamed gross, net or refund-adjusted revenue. Discount values are retained but never reapplied to Sales. This choice allows the arithmetic lesson to proceed without inventing accounting semantics.

## Scope-preserving exceptions and lookups

Detect order/customer conflicts over **all raw Orders before filtering**, not just a chart selection. An order is conflicted if it has more than one Customer ID. Expected IDs in this snapshot are `CA-2025-121465` and `CA-2026-130494`. Set `customer_order_conflict=1` on every line of each order, and `customer_analysis_eligible=0` on those same lines. All other orders receive 0 and 1 respectively. Never replace IDs, merge customers or choose the first ID.

The primary segment snapshot keeps these lines: Segment and relevant order-level attributes are stable within order. A customer exercise applies `customer_analysis_eligible=1` to **all** its metrics, not only its customer-count denominator. It must disclose excluded lines/orders and monetary totals beside the result; its customer universe is “IDs on eligible orders in this scope,” not all customers or retention. Known conflicts outside 2023–2025 remain in the exception record even though they contribute no main-scope lines. Missing IDs are a preparation failure, not automatically eligible.

Returns has one unique Order ID per listed order, each Returned='Yes'. Define `returned_order_flag=1` for membership and 0 for absence. **Zero means not listed**, not verified never returned. Attach by a validated many-to-one membership lookup; repeated flags on lines do not make new return events. Returns has no date, refund amount, quantity, return completion status or cost recovery. Do not use this list for historical/as-of return rates, refund economics, returns within N days or causal conclusions.

People has a unique Region key and all Orders regions match it. The beginner table omits Regional Manager; no People join is necessary. Future source-model practice may use the lookup only after verifying cardinality and unchanged line count. The frozen beginner path uses one prepared table and requires no relationships or LOD expressions.

## Metric definitions

Every metric uses the **same filtered line population** unless its description explicitly specifies the customer-eligible restriction. Define totals first, then divide; do not average subgroup ratios. Count unique nonmissing Order IDs, not lines.

| ID / label | Calculation | Empty/zero behavior and interpretation |
|---|---|---|
| R01 Reported Sales | Sum `sales` | Additive across disjoint lines. Empty aggregation is 0 for machine reconciliation, but display “No rows” rather than a business zero. No extra discount/refund adjustment. |
| R02 Orders | Count distinct `order_id` | Empty = 0. Segment, month, Region and other verified order-level partitions reconcile. Category/Product counts overlap when an order has multiple kinds of lines. |
| R03 Average order value | R01 / R02 | Null if R02=0. At segment/whole-order scope this represents reported order-basket sales. At category/product scope label “Selected-line Sales per participating order”: the numerator covers only selected lines, not the full baskets. |
| R04 Reported Profit | Sum `profit` | Negative amounts allowed; additive across disjoint lines. Accounting cost scope unknown. Empty display rule as R01. |
| R05 Source-reported profit ratio | R04 / R01 | Null if R01=0, including nonempty zero-Sales fixtures. Recalculate from totals at every view/overall level. No gross/net margin claim. |
| R06 Units | Sum `quantity` | Positive integer quantities in this file. Empty =0 for reconciliation; not a count of orders. |
| R07 Orders listed in Returns | Distinct `order_id` where flag=1 | Count orders once, regardless of lines or categories. Empty =0. No return-event-time claim. |
| R08 Share of orders listed in Returns | R07 / R02 | Null if R02=0. Whole-file return-list membership among orders represented in the filtered lines. At category scope it does not establish that the selected category's products were returned. |
| R09 Eligible distinct customer IDs | Count distinct `customer_id` after eligible=1 filter | Apply the same filter to accompanying Sales/orders/AOV; disclose exclusions. Empty =0. No all-source customer/retention claim. |
| R10 Monthly reported Sales | R01 grouped by `order_month` | Date spine Jan 2023–Dec 2025. This unfiltered source population has records in all 36 months; a missing overall month in a derivative is an error to investigate. Within a covered month, a selection with no lines has sum=0 with a no-lines indicator, describing only records in this sample. Do not claim actual business inactivity or fill genuinely unavailable periods with zero. |
| R11 Monthly Sales growth | (current calendar month's R10 − previous calendar month's R10) / previous | Null for the first month, unavailable prior month or zero prior Sales. January 2023 has no released prior month. Partition by the declared comparison dimensions; previous means calendar month, not merely previous visible mark. |
| R12 Year-over-year monthly Sales growth | (R10 at month − R10 twelve calendar months earlier) / prior | Same scope/dimension and null rules; all 2023 results null. No extrapolation outside release. Whole-year comparison uses complete matching calendar years. |
| R13 Order-to-ship interval (optional diagnostic) | Calendar-day difference Ship Date − Order Date, **one observation per Order ID** | Nonnegative in source. Mean/median use distinct order records after checking dates are stable within order; never sum or average repeated line intervals as if orders were equally weighted. Dispatch interval is not delivery timeliness. Outside S3 required KPIs. |

R11/R12 must be computed with the required comparison months available **before** hiding a displayed period. A date selection that removes prior data yields unavailable growth unless preparation/calculation deliberately preserves that comparator. Segment filtering applies to both periods; a changing category/product selection changes the selected-line population and must be stated. No unspecified Tableau “quick table calculation” configuration is accepted as a metric definition.

Calendar coverage is evaluated before optional group filters. A covered month with no selected lines may contribute 0 to that group's sum and hence −100% growth from a positive prior month; a zero prior sum makes growth unavailable. A wholly empty selection still displays “No rows” rather than a trend. These are file-population arithmetic rules, not a verified claim that the fictional business had no unrecorded activity.

## Proposed Tableau mapping and filter checks

These expressions use planned prepared field names and are **documentation-checked candidates, not app-tested calculations**:

```text
Reported Sales: SUM([sales])
Orders: COUNTD([order_id])
Average order value:
  IF COUNTD([order_id]) > 0 THEN SUM([sales]) / COUNTD([order_id]) END
Reported Profit: SUM([profit])
Source-reported profit ratio:
  IF SUM([sales]) <> 0 THEN SUM([profit]) / SUM([sales]) END
Orders listed in Returns:
  COUNTD(IF [returned_order_flag] = 1 THEN [order_id] END)
Share of orders listed in Returns:
  IF COUNTD([order_id]) > 0 THEN
    COUNTD(IF [returned_order_flag] = 1 THEN [order_id] END) / COUNTD([order_id])
  END
```

Tableau's official [aggregate functions](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_aggregate_create.htm) document SUM, COUNTD and numeric floating-point limits (checked 2026-10-12). This contract uses ordinary aggregates that follow the selected population. Avoid introducing FIXED calculations as a shortcut: [Tableau's LOD filter documentation](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod_filters.htm) explains that FIXED is evaluated before ordinary dimension filters. Any later LOD/table-calculation design must explicitly test filter behavior and totals. Grand totals must agree with ratios recomputed from base measures rather than means or sums of displayed ratio cells; exact Tableau behavior remains a D03/V01 check.

Before releasing the Tableau variant, compare whole scope, each Segment, one Region, eligible-only scope, one Category and empty selections. Category tests must demonstrate order-count overlap and the changed AOV label. Do not put an unqualified “return rate” or “margin” in the chart title.

## Precision and presentation

- Reference arithmetic sums `Decimal(str(source numeric value))` with no per-line rounding. XLS stores binary numeric values; their decimal representations do not establish an original currency's minor unit or accounting precision.
- Planned CSV values preserve the shortest round-trip source float representation (`repr`/`str`), not formatted display text or two-decimal rounding. No arithmetic reconstructs Sales/Profit. IDs remain identifiers; dates serialize ISO `YYYY-MM-DD` and flags as 0/1.
- Private reference display: two decimal places for monetary measures and AOV using ROUND_HALF_UP. Two decimal places are a teaching display convention, not a currency assertion. Rate/growth display: one decimal percent; comparison differences explicitly say percentage points. No percent formatting of values already multiplied by 100.
- Machine counts, IDs, flags, dates and source-to-prepared Decimal values must match exactly. Source-to-CSV row values use exact canonical-decimal equality. Engine aggregate comparisons allow absolute monetary error at most **0.000001 source units** and ratio error at most **0.000000001** in fractional representation, before percent formatting. This is an error unit, not a constraint on a metric's range: Profit ratios and growth can be negative or exceed 100%, and must not be clamped. Investigate larger differences; do not widen tolerances to hide a scope defect.
- If only formatted Tableau values can be captured, compare to reference within one displayed unit (0.01 source units, 0.1 percentage point). Record that weaker check separately from full-precision checks. Independently rounded category/segment displays can differ from the separately rounded overall total; do not alter underlying rows to force display sums.
- Empty population: show “No rows in this selection.” Nonempty zero denominator: show “Not available: zero Sales/orders,” with the underlying numerator/denominator. Do not make an unavailable ratio 0%.

## Freeze and later release gates

D01 review checks the dictionary, settings, transformation specification, hand fixtures and source invariants. Changing the date window, source hash, metric meaning, eligibility, projection or rounding afterward requires a new contract version and validation record. A documentation typo can be corrected with a log entry; it must not silently change prepared bytes/answers.

D02 will produce a local prepared development version with manifest/checksums and exception reconciliation. It may proceed with neutral source-unit labels. D03 computes exact-version private answers independently and checks Tableau; D01 source controls are not those answers. Local-development freeze does not approve public distribution: direct-source learning is supported by Tableau guidance, while bundled derivatives/public uploads retain unresolved rights conditions in [SOURCE_RIGHTS.md](../../../../planning/SOURCE_RIGHTS.md). No course license is assigned. Synthetic refunds/costs, finance, service targets, campaigns and employee records keep their own contracts and must not be appended as observed facts about this file.
