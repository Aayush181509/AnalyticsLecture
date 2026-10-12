# First catalog source audit

Audited 2026-10-12. **S01 source inspection is complete for four exact files.** These are local audit acquisitions, not approved learner releases. Recommended roles below remain working design choices; D01 must resolve and freeze the teaching contracts before preparation or lessons. The user confirmed the hybrid sourcing direction, not every dataset or proposed filter.

Subsequent D01 work has frozen the [first retail development contract](../data/metadata/superstore/retail-v1/metric_contract.md) after independent review. That specification supersedes the provisional retail recommendations in this historical audit for local preparation. Other sources and public/teaching release conditions remain separate.

## Evidence and selection

The lead followed download links observed in the rendered [Tableau catalog](https://public.tableau.com/app/learn/sample-data). All four downloads returned HTTP 200, passed file-signature checks, and were preserved without editing. Exact URLs, retrieval times, byte counts, paths and SHA-256 values are in [source_manifest.json](../data/metadata/catalog-audit-2026-10-12/source_manifest.json). [profiles.json](../data/metadata/catalog-audit-2026-10-12/profiles.json) records every actual column, inferred type, null count, cardinality, table size and quality checks. Inferred types are inspection evidence, not a final field dictionary.

| File / observed contents | Recommended course role | Required handling |
|---|---|---|
| Superstore: Orders 10,194×21, People 4×2, Returns 296×2 | First source-backed retail variant; retain controlled synthetic refund/cost fixtures | Correct the misleading EU catalog label; use native dates, reported monetary units and Segment. Resolve currency/metric semantics and isolate inconsistent customer records. |
| World Cup: matches 852×12, team appearances 1,704×13, tournaments 20×10 | Sports transfer choice: grain, duplicate detection, goals per match | Remove 16 exact duplicate match rows in a documented derivative; derive team appearances afresh; exclude attendance/outcome interpretation until separately defined. |
| Mobile OS: 1,898×3 | Technology quality/debugging choice; possible four-month descriptive subset | 1,772 rows lack dates. Never reconstruct dates from row order. Long historical trend use deferred pending a verified replacement export. |
| US construction: 50,208×20 | Government/economic-statistics transfer choice: series filters, units, time aggregation | Select one ownership/category/adjustment/error-type series. Do not sum the entire file or replace missing values with zero. |

Source/provider terms and attribution evidence are in [SOURCE_RIGHTS.md](SOURCE_RIGHTS.md). Source-linked learning, redistribution of prepared CSVs and Tableau Public uploads need distinct delivery decisions. All four manifest records retain `publication_approved: false`. No course license is invented and no source-derived public release is cleared by this audit.

## Retail: the catalog label differs from the file

The catalog calls its link **EU Superstore Sales**, but the actual workbook has United States (9,994 lines) and Canada (200), with order dates **2023-01-03–2026-12-30** and ship dates through **2027-01-05**. It is a fictitious sample with dates beyond the audit date. Do not describe it as European, NPR2025, current company performance or an observed historical business. Retain the catalog title in provenance and call the lesson source “Superstore sample, audited 2026-10-12.”

Orders has these source fields: Row ID, Order ID, Order Date, Ship Date, Ship Mode, Customer ID, Customer Name, Segment, Country/Region, City, State/Province, Postal Code, Region, Product ID, Category, Sub-Category, Product Name, Sales, Quantity, Discount, Profit. There are no null cells after parsing and no exact duplicate rows. Postal Code contains mixed representations and must be treated as an identifier; a beginner extract should omit it if not needed, rather than invent missing leading zeros.

**Grain and joins.** `Row ID` is unique and nonmissing; it is the line key. There are 5,111 distinct Order IDs. `(Order ID, Product ID)` repeats 11 times and is not a line key. People has one Regional Manager per Region; each of the four Orders regions matches it. Returns has 296 unique Order IDs, all present in Orders, and Returned is always Yes. Those tables can supply many-to-one descriptive lookups with unchanged line count; actual Tableau relationship/join behavior remains untested.

**Customer defect.** Orders `CA-2025-121465` and `CA-2026-130494` each refer to four Customer IDs. Do not silently assign an owner or merge these IDs. Flag these orders and exclude all their lines from customer-level exercises until a repair is justified; disclose the excluded population. Order date, ship date, ship mode, segment, country and region are internally consistent within each order, so the segment snapshot can retain the lines. Customer-based cohorts, retention and lifetime value need a separate contract and are outside the beginner pilot.

**Metric mapping proposed for D01.** Use a clear teaching population, provisionally Order Date in 2023–2025 inclusive, for three full sample calendar years without future dates. This is a recommended subset, not a claim that the data represents actual transactions during those years. All-source and proposed-scope control totals are stored privately, not released as lesson answers.

| Metric / field | Proposed definition and limits |
|---|---|
| Reported Sales | `SUM(Sales)` over the scoped order lines. Preserve stored precision and round only final presentation. No additional discount or refund adjustment. The workbook does not supply a formal sales accounting definition. |
| Orders | `COUNTD(Order ID)` in the same scope. Source segment is stable within order; order counts can reconcile across segments. Other dimensions, such as Category, may split an order and their distinct counts must not simply be added. |
| Average order value | Reported Sales / distinct scoped Orders; null/“not available” for zero orders. Same population in numerator and denominator. |
| Source-reported profit ratio | `SUM(Profit) / SUM(Sales)`; null for zero Sales. Use this label pending definition review. Do not claim gross margin, calculate COGS from it, or average row-level profit ratios. Negative Profit is an observed source value. |
| Segment | Consumer, Corporate, Home Office. This replaces Channel in the source-backed variant; it is not renamed as a sales channel. |
| Discount | Observed numeric range 0–0.8. The file lacks a formal definition/base amount. Keep source values; no double application to Sales and no causal claim that discount caused profit changes. |
| Returned-order flag | Membership in Returns, attached without multiplying lines. Flagged scoped distinct orders / all scoped distinct orders describes this workbook's return-list incidence. No return date, refund amount, quantity or cost recovery is available. It is not a time-to-return rate or return-adjusted revenue. |
| Order-to-ship days | Ship Date − Order Date, nonnegative for all source lines. It measures dispatch interval only. No promised arrival, actual delivery or pending-delivery population exists. |

Sales and Profit cells inspected in the XLS use `General`, with no currency identifier. US/Canadian locations are not evidence of a shared ISO currency or exchange conversion. Use **source monetary units** during contract review, and resolve currency before a currency-labeled learner release. The controlled synthetic retail variant retains its own explicit NPR/2025 assumptions and richer refund semantics; source and synthetic values must not be mixed into one reported total.

## Sports: a unique game identifier does not prove unique matches

`WorldCupMatches` covers 1930–2014. Sixteen exact duplicate rows inflate 2014 from 64 to 80 matches. Exact-row deduplication leaves **836 matches**. The resulting match counts and HomeGoals + AwayGoals reconcile to `WorldCups` MatchesPlayed and GoalsScored for **all 20 tournaments**. This is a useful internal cross-table check, not an independent check against FIFA records.

The raw candidate match key `(Date, HomeTeam, AwayTeam)` repeats 16 times; it is unique after exact deduplication. Preserve original row references in a future derivative and create a stable prepared Match ID tied to this source version. If nonidentical rows ever share that key, stop and investigate rather than keep the first arbitrarily. The Tableau-format sheet has 852 distinct Game # values and two team appearances per number, including the duplicate matches under different numbers. Its unique `(Game #, Team)` pairs conceal the defect. Do not combine its rows with the match table or count 1,704 matches. Generate a new appearance view from the deduplicated match table if needed.

**Supported descriptive metrics:** matches = count of clean match rows; tournament goals = sum of HomeGoals + AwayGoals; goals per match = that sum / match count, null for an empty scope. Team appearances require two records per clean match, each with goals for/against; team goals for can sum across teams, whereas summing both teams' “match total goals” would double count. Across tournaments, calculate the overall goals-per-match ratio from totals rather than averaging tournament averages equally.

Scores contain no missing HomeGoals/AwayGoals. Trim Observation whitespace (787 raw rows become blank) and retain meaningful text separately. Drawn numeric scores can coexist with extra-time/penalty narratives; do not infer advancement or shootout goals from the score comparison alone. Retain historical team labels until an explicit alias policy is reviewed. WorldCups Attendance mixes strings with dot separators, floats and integers; exclude it from the beginner contract until an authoritative normalization is checked.

The XLSX contains formulas and stored results. This audit reads cached values through pandas, not a recalculation engine. No formula recalculation or Excel/Tableau execution was performed. Internal reconciliation reduces some risk but does not validate all source formulas. The rights review could not retrieve a dataset-specific license from the named data.world compilation.

## Technology: the mirror does not support its advertised long trend

The CSV fields are Date, Mobile Operating System, Percent of Usage. Only **126 of 1,898 rows** have a date; these span five months, December 2008–April 2009. Twenty-six OS categories occur overall. December–March each have 26 dated categories with percentage-point totals 100.00, 100.00, 100.01 and 99.99. April has 22 dated rows totaling 99.17. Remaining rows have no date. Do not forward-fill, infer repeated 26-row blocks, or invent a 2008–2014 calendar from the catalog description.

**Preferred use:** quality investigation: identify the missing key, explain which question is unsupported, and request a correctly scoped source export. A bounded alternative is the **104 dated rows in December 2008–March 2009**, explicitly labeled as the available dated subset. Geography is suggested by the catalog's upstream `ww` URL but is not present in the file; resolve it before geographic claims. Four dated months do not establish long-term adoption.

Source values are percentage points (e.g. 59.9), not fractions. Divide by 100 only when a plotting/formatting field expects 0–1. Compare one OS across known months using percentage-point differences; do not sum its shares over time or combine regions without page-view denominators. Treat ±0.01 percentage points around 100 as observed rounding, not force-normalize shares silently. Missing dates remain missing; zero share remains an observed zero.

[Statcounter's FAQ](https://gs.statcounter.com/faq) defines its usage methodology and states CC BY-SA 3.0. The provider describes page-view activity, which must not be called device sales or unique owners. Exact historical scope/provenance still needs confirmation, as recorded in SOURCE_RIGHTS. Requesting a fresh official export would create a new source version; it must not overwrite this damaged mirror. The separate Start-up Venture Funding file noticed elsewhere in the workspace is not part of this four-file audit and is not approved by these findings.

## Government: distinguish amounts, rates, errors and overlapping totals

The construction CSV covers **177 months, January 2002–September 2016**, geography US only. The complete observed schema is in profiles.json: period, category, data-type, error-type, geography and adjustment identifiers/descriptions, `val`, `serialid`. `serialid` is unique. The nonnullable composite `(per_idx, cat_idx, dt_idx, et_idx, geo_idx, is_adj)` is also unique. There are 38 category codes, including annual-rate variants. Total, residential/nonresidential, ownership groups and component categories overlap.

`dt_code` distinguishes Total (T), Private (V), Public (P) and monthly percent changes; `dt_unit` distinguishes MLN$ and PCT. `et_idx=0` identifies the main estimates in the observed file, while the named E_* error-series records are separate. Of 50,208 records, **33,216 lack val**. All present values are monetary amounts; percentage/error blocks are entirely missing. Do not interpret these absent values as zero growth or zero error. The adjustment flag occurs alongside annual-rate category descriptions; never aggregate adjusted annual rates with unadjusted monthly amounts.

**Proposed beginner filter, all conditions required:** `cat_code='XXXX'`, `dt_code='T'`, `et_idx=0`, `geo_code='US'`, `is_adj=0`. This produces **177 unique monthly, nonmissing observations** with `dt_unit='MLN$'`. Preserve dates and units: source nominal million US dollars, no NPR conversion or inflation adjustment. Census defines construction value put in place as work installed during a period; [definitions](https://www.census.gov/construction/c30/definitions.html) and [methodology](https://www.census.gov/construction/c30/methodology.html) support interpretation, with historical mirror/vintage caveats in SOURCE_RIGHTS.

Sum unadjusted monthly values only within an explicit period; a full annual total needs 12 months. **2016 has nine months**, so compare January–September across years or exclude it from full-year comparisons. Growth uses matching units/scope and a nonzero prior value; null for missing or zero prior values. Seasonality can affect raw month-to-month comparison. Annual-rate values are kept for an advanced interpretation exercise, not summed as monthly spending. Do not add Total to Residential + Nonresidential, or Total to Private + Public.

For unadjusted monetary totals, both Total − Private − Public and Total − Residential − Nonresidential have maximum absolute residual **1 million dollars**, consistent with separately rounded published amounts. Use this observed tolerance for those checks on this snapshot, not exact equality and not a universal tolerance for every other category. This dataset supports public/private economic comparisons; it supplies no departmental budget ledger and cannot replace the core finance budget-variance case. Exact mirror redistribution terms remain unresolved.

## Integration and reproducibility

- Keep the five required business cases and synthetic HR. External retail can provide supported snapshot metrics; retain controlled finance, operations, marketing and refund cases where inputs are absent. The connected Meridian simulation remains recommended, not user-adopted.
- Add sports, technology quality and government transfer choices within existing practice or optional extensions. No extra contact hours, no grand join of unrelated sources.
- D01 should first freeze a Superstore field dictionary and source-specific metric contract with the above customer/currency/date choices. Keep the controlled S3 pilot outline as the reference until that mapping is approved by analytical review. D02 then writes reproducible prepared derivatives; D03 independently verifies exact release answers before lessons.
- Raw files are untouched. No prepared CSV, synthetic generator, learner download, notebook, Tableau workbook, screenshot or source-specific lesson was produced in S01. Numerical inspection controls are private under instructor/source-audit; they are not validated lesson solutions.

Run acquisition/integrity and offline profiling as documented in [data/README.md](../data/README.md). The tested environment is Python 3.12.14, pandas 2.2.3, openpyxl 3.1.5, xlrd 2.0.2. The profiler checks hashes, source keys and snapshot invariants before writing metadata and private controls. It reads only these four manifest paths; the separately present `scripts/fetch_catalog_sources.py`, duplicate raw directories, Start-up Venture Funding and US Home Sales are preserved, not executed or covered by this audit.

**Verification boundary:** actual local-file schema/numerical inspection and primary-source rights research completed. Internal tournament totals reconciled; raw-file integrity rechecked. No independent provider-value audit, historical Statcounter export match, full source-formula recalculation, Tableau calculation comparison, learner usability/timing trial or public release occurred.
