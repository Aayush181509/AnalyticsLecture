# Planned preparation: Superstore retail v1

This is D01's reproducible transformation specification. **No prepared CSV exists yet.** Implement during D02 after contract review. The [metric contract](metric_contract.md), [dictionary](dictionary.md) and [settings](contract.json) are authoritative together; contradictions stop preparation. All work remains local and outside docs/ until a reviewed delivery mode is chosen.

## Inputs and fail conditions

1. Read the manifest-listed original only. Verify its byte count and SHA-256 against contract.json and the source manifest. Preserve it unchanged. Stop on different bytes, missing source, different sheet names or unexpected source columns. Never fall back to a similarly named workbook elsewhere in the workspace.
2. Read stored Orders/Returns/People values; no workbook recalculation. Validate all source Row IDs unique/nonmissing and integer-valued. Validate projected/derived fields are nonmissing, keys/dimensions nonblank, dates date-only, Quantity positive/integer, finite Sales/Profit/Discount and Sales>=0, Discount in [0,1]. This admits fixture zero Sales while the actual snapshot has positive Sales. Negative Profit is valid.
3. Verify the six order-stable attributes in contract.json have one value per Order ID. Nonidentical Order ID/Product ID duplicates are valid source lines, not a repair target. Do not deduplicate or trim/normalize source identifiers silently.
4. Verify Returns has unique/nonmissing Order IDs, Returned always Yes, and every returned ID exists in raw Orders. Verify People has one row per Region and every Orders Region is present, even though the beginner output does not join People. Any failed lookup/cardinality condition stops the run; do not multiply rows or select a first match.
5. Detect customer conflicts across all raw Orders and compare to the known two-order exception set. An unexpected conflict or missing Customer ID requires review rather than automatic expansion of exceptions. Log every original line ID for both known conflicts, original IDs preserved.

## Transformations in order

1. Derive conflict/eligible flags for all raw lines, including the 2026 conflict, then apply the half-open Order Date window in contract.json. Keep ship dates beyond the window. Record included and excluded source Row ID sets and counts; their disjoint union must equal all original Row IDs.
2. Project the 17 source fields to the 17 prepared names in contract.json. Omit Customer Name, City, State/Province and Postal Code from this beginner projection without modifying raw. This avoids teaching unsupported postcode reconstruction and keeps the sheet focused. Omit People entirely; do not add fictitious department/channel/currency/status fields.
3. Attach the three flags by validated membership/conflict maps. Derive `order_to_ship_days` from date subtraction; require nonnegative. Derive first-of-month `order_month`. Verify flags have one value per order and eligible=1-conflict.
4. Sort by Row ID and write exactly the 22 columns in contract order, UTF-8 CSV, LF line endings, one header, ISO dates, integer IDs/counts/flags and unrounded source numeric representations. Row ID is not resequenced. Use a CSV writer's proper quoting for names. Do not modify a resulting CSV by hand.
5. Re-read the saved CSV using declared types, not unrestricted type inference. Compare row-ID sets, identifiers, all dates/flags, and source numeric values by canonical Decimal equality. A re-read numeric conversion must not round to two decimals. Verify 36 first-of-month keys Jan 2023–Dec 2025 in this snapshot.

## Output separation and reconciliation

Planned local output: `data/prepared/superstore/retail-v1/order_lines.csv`. Do not claim this exists from the contract path. No separate customer copy is necessary: customer work filters eligible=1 from the same source and logs that scope. No money from synthetic supplements is appended to this table.

D02 writes an output manifest with contract ID and SHA-256 of each contract document/settings file, raw source hash, preparation-script hash, runtime versions, output bytes/hash, schema/count/date range and publication=false. It also writes a transformation/quality record. Existing output directories are immutable versions: repeat identical generation may verify byte identity; a different result must stop instead of overwrite. Algorithm/semantic changes require a new version.

Record exceptions privately under instructor/solutions/superstore/retail-v1 (or instructor/source-audit for pre-release checks): source line IDs/customer mappings, in-scope versus excluded conflict records, all-scope/customer-eligible population bridges, counts, quantities, Sales and Profit before/after. Inspect exact source control reconciliation. Metadata may report schema/exception counts but detailed exercise answers remain instructor-only. No assessed answer table or completed workbook enters docs/.

Required checks: unchanged raw hash; distinct Row IDs; 6,815 scoped lines and 3,388 distinct orders; in-scope conflict orders exactly the 2025 order; no order split by Order Date; full date coverage of 36 months; source and output values equal; flags/cardinalities correct; primary totals remain unchanged by customer flags; eligible plus excluded populations reconcile. Verify Segment/Region/date partitions reconcile additive measures and order counts. Demonstrate Category distinct counts may overlap. Numerical controls are compared without rounding, then with the stated engine tolerances only where appropriate.

Create intentional broken variants or synthetic edge fixtures only under clearly separate challenge/fixture paths, with an instructor issue manifest. Never insert defects into the reference prepared file. D01's small synthetic fixtures are unit cases, not employee data, actual source records or a full Meridian source generator.

D03 independently computes exact prepared-release answers and filtered checks, verifies a small hand fixture, then compares whole/filtered/grand-total/zero-case behavior in Tableau with version and evidence recorded. A CSV re-read or successful Python assertion is not a Tableau test. Once rights/delivery, content and app checks pass, review learner packaging deliberately; no publish/deploy command is part of D02 or D03 verification.
