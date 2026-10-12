# Independent four-source audit review

Reviewed **2026-10-12**. **Disposition: source-audit findings are supported for planning and D01 contract work. No blocking numerical or analytical inaccuracy found in the bounded review.** This is not approval of learner distribution, source adoption for every metric, or Tableau publication.

## Scope and independence

Reviewed `SOURCE_AUDIT.md`, the four-record `source_manifest.json`, `profiles.json`, `scripts/profile_catalog_samples.py`, private inspection controls and the recorded rights/definition limits. Independently read the four manifest files without running the profiler or changing its outputs. Retail arithmetic used **xlrd direct worksheet iteration and Decimal, not pandas**. Sports used openpyxl cached worksheet values; government and technology used the standard-library CSV reader and Decimal.

This role edited this report and the linked private retail hand check only. It did not download anything, run acquisition scripts, create prepared data, produce released answers, publish, or execute Tableau. The separately present `scripts/fetch_catalog_sources.py`, additional six-directory raw layout, Start-up Venture Funding and US Home Sales are outside scope and were not executed or inspected as audit inputs.

## Findings

| Finding | Severity / disposition | Evidence or action |
| --- | --- | --- |
| Source claims and metric populations | No blocking defect found | Reported Sales, source-reported Profit ratio, order-count denominator, segment stability, return-list incidence and dispatch interval are appropriately limited to observed fields. No invented COGS, refund amounts, promised delivery or channel fields. |
| Sports profiler did not originally stop on goal reconciliation failure | Low — repaired by lead during review | Initial script computed exceptions but only asserted match-count residuals. Final source now asserts every goal residual is zero. Independent cached-value iteration also reconciled goals/counts for all 20 tournaments. |
| Government composite key lacked an explicit null assertion | Low — repaired by lead during review | Initial script asserted uniqueness only. Final source asserts all composite-key fields non-null. Independent CSV iteration confirmed both non-nullness and uniqueness in this snapshot. |
| Rights, currency and historical-vintage limits | Future release gates, not numerical defects | Four manifest records keep `publication_approved: false`. Superstore currency/Profit semantics, sports compilation license, Statcounter mirror provenance and Census/Enigma mirror terms remain unresolved as stated. Do not remove these limits merely because arithmetic reconciles. |
| Exact controls versus teaching answers | Future production gate | Current controls are inspection results for raw source scopes, not D03 prepared-release solutions. The 2023–2025 subset, precision/tolerance, customer exclusions and delivery mode still need D01 decisions. |

Lead updated `data/README.md` during integration: it now describes the acquired audit files and reproducible profiling route rather than the earlier no-download state. Final project status/handoff updates remain the lead's responsibility.

## Retail: independent direct-iteration check

Checked workbook hash against the manifest: `5045ed4fec49cae2cc0dfc5ab0d204ba09efa767fe00c996822499e8cc42fbbd`. All four source byte counts and SHA-256 values also matched their manifest records.

Directly read header positions and every Orders row with xlrd. Dates were converted using the workbook's date mode, with the proposed scope **2023-01-01 ≤ Order Date < 2026-01-01**. Summed `Decimal(str(cell_value))` without per-row rounding; counted unique Order IDs with Python sets, separately by Segment. This preserves the profiler's documented numeric-representation convention. It does not recover an unstated original decimal accounting precision from binary XLS cells.

**All-source and proposed-scope** row counts, distinct orders, quantities, flagged-return orders, Sales and Profit matched private controls exactly. Every Segment's rows/orders/Sales/Profit also matched exactly. Source scope: 10,194 lines, 5,111 orders, quantity 38,654 and 296 flagged orders. Proposed 2023–2025 scope: 6,815 lines, 3,388 orders, quantity 25,917 and 191 flagged orders.

Independent Segment totals and a two-line order fixture passed. Detailed monetary totals, rounding explanation and hand arithmetic are retained in the [private retail hand check](../instructor/source-audit/retail-hand-check.md).

Independently confirmed that both named conflicting orders (`CA-2025-121465`, `CA-2026-130494`) have four Customer IDs each. That supports flagging the entire affected order for customer analyses while retaining source-consistent segment comparisons. Checked every Sales/Profit cell's XLS number-format definition: all were `General`, supporting the audit's refusal to infer currency from formatting.

## Sports, technology and government checks

**Sports:** direct cached-value reads reproduced 852 match rows and 16 exact duplicates. Exact-row deduplication produced 836 rows with unique `(Date, HomeTeam, AwayTeam)` keys. Raw 2014 has 80 rows; cleaned 2014 has 64 matches and 171 numeric-score goals. For each of 20 tournaments, cleaned match counts and summed HomeGoals + AwayGoals matched the workbook's tournament table. The appearance sheet has 1,704 rows, 852 Game IDs, two rows per Game ID and unique Game/Team pairs, supporting the warning that those identifiers conceal duplicate matches. The audit correctly keeps raw preservation separate from a future derivative, warns against double counting team-level match totals, and does not turn numeric draws into advancement/shootout claims. These are internal cached-workbook checks, not independent FIFA verification or formula recalculation.

**Technology:** direct CSV/Decimal inspection reproduced 1,898 rows, 1,772 undated records and 126 dated rows. The five dated periods have row-count/share totals **26/100.00, 26/100.00, 26/100.01, 26/99.99, 22/99.17**, matching profiles/controls. December 2008–March 2009 therefore has 104 dated records. The report appropriately treats the rest as unresolved rather than inferring dates, sums neither an OS's shares across time nor shares across geographies without denominators, and distinguishes percentage points from fractions. Provider methodology/rights were reviewed from the recorded research; no new historical export or provider-value verification was performed.

**Government:** direct CSV inspection reproduced 50,208 rows, 33,216 blank `val` cells and non-null unique composite keys. Every nonblank value belonged to a monetary `MLN$` main-estimate record in this snapshot. The proposed five-condition filter produced 177 nonmissing, unique monthly observations from 2002-01-01 through 2016-09-01; 2016 contributes nine months. Decimal summation matched the private monthly-series control. Independently calculated maximum absolute residuals of **1 million dollars** for Total − Private − Public and Total − Residential − Nonresidential across those months. Thus the report's snapshot-specific tolerance, overlapping-series warning, full-year requirement and adjusted-annual-rate exclusion are supported. These checks do not verify historical mirror values against an official Census release or establish mirror licensing.

## Execution evidence and limits

Both independent inline read-only scripts were executed using:

```bash
PYTHONPATH=/tmp/kings-source-audit-libs \
  /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 - <<'PY'
# First script: xlrd direct Orders/Returns iteration; Decimal sums; set counts;
# compare all-source/proposed-scope/segment controls; inspect XLS formats/fixture.
# Second script: openpyxl data_only cached rows for sports;
# csv.DictReader + Decimal for government and technology checks.
PY
```

This records the actual execution route and operations; the abbreviated block is not a complete replacement for the two inline review scripts. Verified interpreter **Python 3.12.14**, xlrd **2.0.2**. A preliminary import probe also confirmed xlrd in host Python 3.9.6; all independent data checks above used the specified bundled 3.12 interpreter. No pandas was imported by the independent scripts. Reviewed the profiler's final added assertions without rerunning its metadata-writing main function. `git diff --check` passed at the review snapshot.

No original was edited. Remaining gates are source-native field/metric definitions, currency and precision policy, rights/delivery resolution, reproducible prepared derivatives, exact-version lesson answers, actual Tableau validation and classroom/accessibility timing. The numerical agreement supports this raw-source audit; it does not clear those later gates.
