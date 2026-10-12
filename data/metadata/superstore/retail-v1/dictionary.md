# Superstore retail-v1 field dictionary

Updated 2026-10-12. **Frozen local-development design following the independent D01 review.** This is a dictionary for an inspected fictitious sample and a planned local prepared projection, not a claim that the projection, learner answers or Tableau workbook exists. `publication_approved: false`. Source-derived public download, packaged workbook and Tableau Public upload remain separate release decisions. The user confirmed hybrid sourcing, not this sample's dates, geography or business assumptions. See the [metric contract](metric_contract.md) and [review](../../../../planning/RETAIL_CONTRACT_REVIEW.md).

## Source identity and evidence

- Original: `data/raw/eu-superstore/2026-10-12/sample_-_superstore.xls`; SHA-256 `5045ed4fec49cae2cc0dfc5ab0d204ba09efa767fe00c996822499e8cc42fbbd`.
- Context: **fictitious Superstore sample**, United States/Canada. The catalog's EU title does not describe the inspected file's geography. Do not relabel it Meridian, NPR2025 or current observed company performance.
- Source Orders dates: 2023-01-03–2026-12-30; Ship Date through 2027-01-05, including future sample dates relative to inspection. Currency ISO code and Sales/Profit accounting definitions are unresolved. Use **source monetary units**; no inferred USD/CAD/NPR, exchange conversion, gross margin or COGS.
- Evidence: [source audit](../../../../planning/SOURCE_AUDIT.md), [machine-readable profiles](../../catalog-audit-2026-10-12/profiles.json), [source manifest](../../catalog-audit-2026-10-12/source_manifest.json), [rights record](../../../../planning/SOURCE_RIGHTS.md), and [private hand-check fixture](../../../../instructor/source-audit/retail-hand-check.md). Private controls are not released assessment answers.

Types/counts come from the frozen snapshot's pandas profile; examples, low-cardinality domains and Excel storage were checked read-only with xlrd on 2026-10-12. “Observed domain” is evidence about this exact snapshot, **not a universal business rule or permission to invent new ranges**. Development validation must verify the source hash and declared types/null policy; any different source/version requires review. High-cardinality labels/IDs are preserved, not constrained by a guessed regular expression or fabricated code list.

**Null policy N0:** every raw field below has zero missing values in the inspected parsed table. The planned development projection requires its retained fields to remain nonnull; unexpected null/blank input is a validation failure to investigate, never zero, a fabricated date or an invented category. A nonexistent Returns lookup row is handled by explicit membership logic, not interpreted as an observed source null. No string ID is converted to a number or regenerated.

**Additivity legend:** “No” means a label, identifier, date, rate or attribute must not be summed as a measure. “Line-additive” means sum across disjoint source lines in the same declared scope/units; it does not establish accounting semantics or cross-currency comparability. Distinct IDs must be recounted at the displayed grouping; overlapping groups are not additive.

## Raw Orders — 21 fields

Grain: one source order line; **Row ID** is the unique line key (10,194 rows, 10,194 distinct Row IDs). Order ID has 5,111 distinct values and repeats across lines. `(Order ID, Product ID)` repeats and is not a line key. All entries below use N0. Excel `number`/`date` describes observed storage; pandas inferred types describe the audit read, not an authoritative source specification.

| Raw field | Observed type | Intended meaning / key or cardinality role | Observed domain / unit | Null policy | Additivity | Representative observed example |
|---|---|---|---|---|---|---|
| Row ID | Excel number; pandas `int64` | Source line identifier; unique primary key | Integers 1–10,194 in this snapshot; identifier, not quantity | N0 | No; count rows only at line grain | `1` |
| Order ID | Excel text; `object` | Source order identifier; 5,111 distinct, one-to-many to lines; Returns lookup key | Preserve 5,111 source strings; identifier | N0 | No; orders use distinct count | `US-2023-103800` |
| Order Date | Excel date; `datetime64[ns]` | Source-labeled order calendar date; stable within each order; primary scope date | 1,242 distinct dates, 2023-01-03–2026-12-30; calendar date | N0 | No | `2023-01-03` |
| Ship Date | Excel date; `datetime64[ns]` | Source-labeled dispatch/ship calendar date; stable within order; not actual delivery | 1,338 dates, 2023-01-07–2027-01-05; calendar date | N0 | No | `2023-01-07` |
| Ship Mode | Excel text; `object` | Shipment-service label, stable within order; not promised arrival target | `Standard Class`, `First Class`, `Second Class`, `Same Day`; category | N0 | No | `Standard Class` |
| Customer ID | Excel text; `object` | Source customer label/identifier; 804 distinct. Two orders have conflicting IDs; not a valid unique order owner without policy | Preserve source strings; identifier, not verified real person | N0 | No; distinct count only in eligible view | `DP-13000` |
| Customer Name | Excel text; `object` | Fictitious customer display label; 800 distinct, not a unique key. Omitted from beginner projection | Preserve source labels in raw; name | N0 | No | `Darren Powers` |
| Segment | Excel text; `object` | Source customer-segment classification; stable within order; **not Channel** | `Consumer`, `Home Office`, `Corporate`; category | N0 | No; recalculate metrics within groups | `Consumer` |
| Country/Region | Excel text; `object` | Source geographic label; stable within order; not currency evidence | `United States`, `Canada`; location category | N0 | No | `United States` |
| City | Excel text; `object` | Source city label, 542 distinct; not a unique geographic key. Omitted from beginner projection | Preserve observed source labels; location | N0 | No | `Houston` |
| State/Province | Excel text; `object` | Source state/province label, 59 distinct; no assumed global uniqueness. Omitted from beginner projection | Preserve observed source labels; location | N0 | No | `Texas` |
| Postal Code | Excel number **and** text; `object` | Postal identifier, 654 distinct; mixed representations, no fabricated leading zeros. Omitted from beginner projection | 9,983 numeric and 211 text cells; postal identifier, not amount | N0 | No | Numeric source value `77095.0` |
| Region | Excel text; `object` | Source region label, stable within order; many-to-one lookup to People.Region | `Central`, `East`, `South`, `West`; category | N0 | No | `Central` |
| Product ID | Excel text; `object` | Source product identifier, 1,862 distinct; repeats across lines; not a line key with Order ID | Preserve source strings; identifier | N0 | No | `OFF-PA-10000174` |
| Category | Excel text; `object` | Source line product category; orders can span categories | `Office Supplies`, `Furniture`, `Technology`; category | N0 | No; category distinct orders can overlap | `Office Supplies` |
| Sub-Category | Excel text; `object` | Source product subgroup; 17 distinct; not an order-level denominator | See complete observed list below; category | N0 | No | `Paper` |
| Product Name | Excel text; `object` | Source product display label; 1,849 distinct, not a unique key | Preserve source labels; product description | N0 | No | `Message Book, Wirebound, Four 5 1/2" X 4" Forms/Pg., 200 Dupl. Sets/Book` |
| Sales | Excel number; `float64` | **Source-reported line Sales**. Accounting definition/base not supplied; preserve stored values, apply no extra discount/refund | Observed min `0.44399999999999995`, max `22638.48`; source monetary units, ISO unknown | N0; no zero imputation | Line-additive within declared source-unit scope | `16.448` |
| Quantity | Excel number; `int64` | Source line item quantity; count of merchandise units, not orders | Observed integer set 1–14; source item units (not a common physical unit such as kg) | N0 | Line-additive item counts; not order count | `2` |
| Discount | Excel number; `float64` | Source discount value, **formal definition/base unresolved**; not line monetary discount or an independently verified effective rate | Observed values `0`, `0.1`, `0.15`, `0.2`, `0.3`, `0.32`, `0.4`, `0.45`, `0.5`, `0.6`, `0.7`, `0.8`; source numeric scale | N0; retain observed zero | No; no unapproved sum/weighted-rate formula | `0.2` |
| Profit | Excel number; `float64` | **Source-reported line Profit**; retain negative values; not defined gross profit/net income, not an inferred COGS input | Observed min `-6599.978000000001`, max `8399.975999999999`; source monetary units, ISO unknown | N0; no zero imputation | Line-additive within declared source-unit scope | `5.551199999999998` |

Observed Sub-Category list: `Paper`, `Binders`, `Labels`, `Storage`, `Art`, `Chairs`, `Fasteners`, `Phones`, `Furnishings`, `Accessories`, `Bookcases`, `Envelopes`, `Appliances`, `Tables`, `Supplies`, `Machines`, `Copiers`. Domain ordering above follows first observation; it is not an analytical ranking. Examples are raw first-row values displayed as readable ISO dates/integers where appropriate; long numeric representations show source precision rather than fabricated cents.

### Order-level consistency and customer eligibility

The source audit found Order Date, Ship Date, Ship Mode, Segment, Country/Region and Region consistent within each order. These attributes can group order-level KPIs in this snapshot. Product/category attributes can split an order; category order counts cannot simply be added.

`CA-2025-121465` and `CA-2026-130494` each have four Customer IDs. Detect conflict across the **entire raw Orders table** as more than one distinct Customer ID per Order ID, then attach that order-level result to every line before/with the date filter. Do not select a first customer, rewrite IDs, split an order into new IDs or discard the conflict from the primary KPI view. In the chosen date scope, **all lines remain in primary Sales/orders/AOV/profit-ratio work**; exclude **all** scoped lines of a conflicted order only in a separately explicit customer-eligible view. Disclose exclusions whenever customer-specific metrics are reported. Customer cohorts, retention and lifetime value are outside this dictionary's core KPI scope.

## Raw People — 2 fields

Grain: one source Region assignment; 4×2, Region unique/nonmissing and all four Orders regions match. Many Orders lines can map to one People row; lookup must preserve Orders line count. Manager labels are descriptive fictional sample labels, not a key to join departments or employee history. Both fields are omitted from the beginner projection except Orders' own Region.

| Raw field | Observed type | Intended meaning / key or cardinality role | Observed domain / unit | Null policy | Additivity | Representative observed example |
|---|---|---|---|---|---|---|
| Regional Manager | Excel text; `object` | Source manager display label; 4 distinct, no employment or reporting-period history supplied | `Sadie Pawthorne`, `Chuck Magee`, `Roxanne Rodriguez`, `Fred Suzuki`; label | N0 (0 missing) | No | `Sadie Pawthorne` |
| Region | Excel text; `object` | Unique lookup key; all Orders regions covered | `West`, `East`, `Central`, `South`; category | N0 (0 missing) | No | `West` |

## Raw Returns — 2 fields

Grain: one listed returned Order ID, **not a return event or refunded line**; 296×2. Order ID unique, all IDs present in Orders, Returned always Yes. Repeatedly joining an order-level flag onto lines does not make that flag line-additive. Scope return incidence by distinct orders, never summed flagged lines divided by order count.

| Raw field | Observed type | Intended meaning / key or cardinality role | Observed domain / unit | Null policy | Additivity | Representative observed example |
|---|---|---|---|---|---|---|
| Order ID | Excel text; `object` | Unique membership lookup key, 296 distinct; maps to one or more Orders lines | Preserve 296 source strings; identifier | N0 (0 missing) | No; distinct scoped orders | `US-2023-100762` |
| Returned | Excel text; `object` | Source list label; conveys membership, without event date/quantity/refund or observation completeness | Exactly `Yes` in this snapshot; category | N0 (0 missing) | No | `Yes` |

Absence from this table means **not listed**, not verified no-return. Do not infer return timing, a follow-up window, partial-return quantity, refunds, recovered cost or return-adjusted revenue. Any richer exercise uses a separately labeled synthetic supplement and its own dictionary.

## Planned prepared projection — exactly 22 fields

**Development scope:** `2023-01-01 <= Order Date < 2026-01-01`, applied to **Order Date only**. Keep both date columns; a shipment may cross a reporting boundary and is not independently filtered out. Source remains a fictitious sample. This is an internal development choice, not a user-confirmed business period. Prepared grain remains one scoped source line; `row_id` retains Row ID and is the unique primary key. No aggregation, invented line IDs, extra discount/refund transformation or deduplication is specified.

Prepared dates will serialize as ISO `YYYY-MM-DD`; source IDs as unchanged strings; Row ID/Quantity as integers; flags as integer `0`/`1`. Source Sales/Profit/Discount precision is preserved without line rounding; use final-display rounding only. Type below is the proposed representation, not an assertion that a CSV exists. Every prepared field is required/nonnull; do not impute source nulls. Derived values are recomputed from the source/version, not hand-edited.

| Prepared field | Proposed type / unit | Source or derivation / role | Domain and null policy | Additivity / use | Example for observed Row ID 1, **planned mapping only** |
|---|---|---|---|---|---|
| row_id | Integer identifier | Orders.Row ID, unchanged primary key | Source integer ID; nonnull/unique | No | `1` |
| order_id | String identifier | Orders.Order ID, unchanged | Source string; nonnull; may repeat | No; distinct order count | `US-2023-103800` |
| order_date | ISO date | Orders.Order Date; primary scope date | Nonnull; within chosen half-open interval | No | `2023-01-03` |
| ship_date | ISO date | Orders.Ship Date; retained even across date boundary | Nonnull; source date; >= order_date | No | `2023-01-07` |
| ship_mode | String category | Orders.Ship Mode | Exact observed four-label domain; nonnull | No | `Standard Class` |
| customer_id | String identifier | Orders.Customer ID; not rewritten | Source strings; nonnull; interpret with conflict/eligibility | No | `DP-13000` |
| segment | String category | Orders.Segment; never renamed Channel | Consumer/Home Office/Corporate; nonnull | No; same-scope order-group KPIs | `Consumer` |
| country_region | String category | Orders.Country/Region | United States/Canada; nonnull; not currency | No | `United States` |
| region | String category | Orders.Region | Central/East/South/West; nonnull | No | `Central` |
| category | String category | Orders.Category | Observed three-label domain; nonnull | No; distinct orders may overlap | `Office Supplies` |
| sub_category | String category | Orders.Sub-Category | Observed 17-label domain; nonnull | No | `Paper` |
| product_id | String identifier | Orders.Product ID | Source strings; nonnull | No; not a line key | `OFF-PA-10000174` |
| product_name | String label | Orders.Product Name | Source labels; nonnull | No | Raw Product Name example above |
| sales | Numeric, source monetary units | Orders.Sales unchanged | Finite source values; nonnull; preserve precision | Line-additive; same scope denominator | `16.448` |
| quantity | Integer, item count | Orders.Quantity unchanged | Observed 1–14; nonnull; no inferred new limits for other source versions | Line-additive units, not orders | `2` |
| discount | Numeric, source scale | Orders.Discount unchanged | Observed numeric domain above; nonnull; base unresolved | No approved aggregate discount KPI | `0.2` |
| profit | Numeric, source monetary units | Orders.Profit unchanged | Finite source values including negatives; nonnull | Line-additive; source-reported profit ratio only | `5.551199999999998` |
| returned_order_flag | Integer flag | `1` iff order_id is in raw Returns.Order ID; otherwise `0` | `{0,1}`; no null; `0` means not listed | Not order-additive on line rows; count distinct flagged orders | `0` |
| customer_analysis_eligible | Integer flag | `1 - customer_order_conflict` for this version | `{0,1}`; nonnull, stable within order | Filter only customer-eligible view; not primary KPI scope | `1` |
| customer_order_conflict | Integer flag | `1` iff raw whole-source Order ID has >1 distinct Customer ID; otherwise `0` | `{0,1}`; nonnull, stable within order | No; do not silently drop primary lines | `0` |
| order_to_ship_days | Integer, calendar days | `ship_date - order_date` | Nonnegative; nonnull; do not replace unknown dates with zero | No; mean/median needs a declared line/order weighting | `4` |
| order_month | ISO date | First day of order_date's calendar month | Nonnull; `YYYY-MM-01`; derived grouping key | No | `2023-01-01` |

Beginner projection drops Customer Name, City, State/Province and Postal Code, and does not add Regional Manager. Dropping means omitted from the derivative, not deleted from preserved raw sources. No row-level COGS, currency code, Channel, refund or delivery-promise field is fabricated. All 22 field names and order above are the intended output schema; any schema revision must be reviewed with the lead's metric/preparation contract.

`order_to_ship_days` is dispatch interval, not delivery time or on-time service. It repeats across order lines, so averaging it at line grain weights multi-line orders more heavily. An order-weighted summary must first select one interval per Order ID or otherwise use a validated order-level calculation; never label a line-weighted mean as order-weighted. The same nonadditivity warning applies to repeated return/conflict flags.

## Verification and release boundary

This dictionary role read existing profile/audit/rights evidence and ran two read-only xlrd inspections of the exact original to confirm examples, categorical values, numeric bounds and raw storage types; no source/prepared file was changed or generated. The Row ID 1 planned example has a four-calendar-day ship interval and is not in the Returns list; conflict policy uses the audit's two identified orders. These are mapping examples, not released exercise solutions.

Future preparation validation must check the source hash; raw table/field set; row key and lookup cardinalities; no unexpected source nulls; order-attribute consistency; whole-source customer conflict flags; the order-date-only population; unchanged source values and precision; and exactly this 22-field projection. The lead's separate metric contract defines KPI denominators, zero-denominator display and validation fixtures. No Tableau relationship behavior, calculation, workbook or screenshot is claimed tested. Currency/accounting semantics, source-derived distribution permissions, prepared release and independent exact-answer checks remain documented gates.
