# Tableau sample-data shortlist

Updated 2026-10-12. **Confirmed sourcing direction:** combine the existing data strategy with [Tableau Public sample datasets](https://public.tableau.com/app/learn/sample-data), including sports, technology, government and other suitable topics. This is a hybrid plan; catalog files and synthetic cases/supplements serve different teaching needs.

## Evidence and status

The lead inspected the rendered catalog in Chrome on 2026-10-12. A text-only web open returned a JavaScript shell. **Four exact downloads are now inspected:** Superstore, World Cup results, Mobile OS usage and US construction. See [SOURCE_AUDIT.md](SOURCE_AUDIT.md) for observed schemas, quality issues and recommended roles, and [SOURCE_RIGHTS.md](SOURCE_RIGHTS.md) for provider evidence and remaining conditions. Other candidates below remain catalog listings only. No source-derived learner release is approved. Descriptions in the shortlist are catalog claims, not overrides of actual-file evidence: the Superstore file is US/Canada 2023–2026, and most Mobile OS dates are missing. Preserve these discrepancies in lesson planning.

## Core-domain candidates and gaps

| Core domain | Catalog candidate / catalog description | Proposed role and source audit needed | Synthetic strategy retained |
|---|---|---|---|
| Retail/e-commerce | EU Superstore Sales; fictitious company products, sales and profits; XLS link | Strong first candidate. Inspect sheets, grain, order/line IDs, dates, currency, sales/profit/discount semantics, available dimensions and any return information. No assumption that fields match the Meridian schema. | Controlled pilot and refund-event fixtures remain useful; no invented COGS, refund amounts or completion status appended as if sourced. |
| Finance | Global Sport Finances; team/athlete pay; University Advancement, Donations and Giving (described as fictitious); US Construction Spending | Transfer comparisons of amounts and periods. Catalog descriptions do not establish a department/month budget-versus-actual pair. | Preserve explicit budgets/ledger case for variance, sign/favorability and join multiplication when source lacks those structures. |
| Operations | EU Superstore Sales; FAA Wildlife Strikes | Potential order-process or event-quality context only after field audit. Order-to-ship intervals, if present, cannot establish delivery reliability against a promised date. Wildlife incidents are not a delivery denominator. | Preserve promised/actual/pending shipment case when these fields are absent. |
| Marketing | Retail sales context from EU Superstore; no named direct funnel candidate selected | Inspect available source fields before proposing segmentation. Sales alone do not establish campaign spend, sessions, conversions or attribution. | Preserve campaign-day funnel/spend and synthetic single-campaign allocation exercise where needed. |
| HR | Employment Changes in Great Britain by Industry; Millennial vs Baby Boomer Employment | Aggregate workforce/labor-market comparisons. Catalog describes industry/geographic groups, not employee spells or historical turnover inputs. | Employee-level HR remains synthetic as required; retain historical snapshots, hires/exits/transfers and recruitment case. |

The hybrid plan can use catalog samples directly for supported questions and the connected synthetic simulation for a realistic cross-department capstone. Do not force every business metric into one external file or present heterogeneous catalog files as one company.

## Additional-domain shortlist

| Topic | Actual catalog entry | Recommended transfer practice | Check before lesson adoption |
|---|---|---|---|
| Sports | FIFA World Cup Match Results (catalog:1930–2014; XLSX) | Match vs team-appearance grain, trend/comparison, denominator debugging | Match key, score/outcome rules, tournament scope, missing values, extra-time/penalty representation. |
| Sports alternatives | 2018 FIFA World Cup Rosters; Tour de France Statistics; Summer Olympics Medallist Dataset | Player cohorts, distributions or distinct medal/event counts | Date/age basis, population, repeated participants, medalists vs events and historical coverage. |
| Technology | Mobile OS Usage (catalog:2008–2014; CSV) | Time trends and percentage interpretation | Geography, period, share denominator, percent encoding and whether categories are exhaustive; never sum shares over time. |
| Technology | Start-up Venture Funding (XLSX; catalog names Companies, Rounds, Investments, Acquisition sheets) | Multi-table grain/cardinality and funding distributions | Company/round/investor keys, amount units/currency, overlapping funding totals, dates and missing/undisclosed amounts. |
| Government | US Construction Spending, by Value and Category, 2002–16 (CSV) | Public/sector time series and aggregation choices | Nominal units, period, annualized/seasonal-adjustment status and overlapping category totals. |
| Government | US Home Sales, 1963–2016 (CSV) | Median vs mean, geography and historic trends | Series units, counts vs prices, period and adjustment definitions; subgroup medians cannot be averaged into an overall median. |
| Government/technology | Worldwide Undersea Communications Cables, June 2016 (ZIP) | Optional spatial/network data quality challenge | Archive contents, spatial format, cable/segment grain, coordinate system and historical snapshot. Advanced extension only. |
| Science/environment | CO2 Emissions by London Borough (2005–2014; ZIP) | Absolute vs per-capita measures and spatial comparison | Boundary vintage, geography keys, emissions units, population denominators and geometry licensing. |
| Education | University Advancement, Donations and Giving (XLS, explicitly fictitious in catalog); American University Data | Donor/transaction or institution grain and fair comparisons | Actual table structure, aggregation, units, missingness and reference years. Preserve fictitious label where applicable. |
| Entertainment/lifestyle | Great British Bake Off (ZIP with separate dictionary PDF); Netflix Movies and TV Shows; Titanic Passenger List | Categorical comparisons, multi-table grain and missingness | Actual rows/keys, dictionary consistency, historical population, inclusion rules and source terms. |
| Further choices | Catalog also lists Health, Public Data and other subjects | Use an appropriate noncausal descriptive question under the same lesson template | Select deliberately after source review; not every listing needs a course lesson. |

## Adoption workflow — S01 inspected; D01 contract freeze next

1. Pick a small first set: retail candidate plus one sports, one technology and one government candidate. Avoid a bulk download of the catalog.
2. Follow the visible catalog download link; preserve the exact original under `data/raw/<source-id>/<version>/`. Record catalog URL, exact file URL, upstream provider, retrieval date, filename, bytes and SHA-256. Record failures rather than assuming the mirror works.
3. Inspect actual sheets/columns, row counts, grain/keys, types, dates, units, nulls and supported metrics. Keep observed schema separate from the proposed synthetic contract.
4. Record applicable original/provider and mirror terms, attribution and restrictions. Teaching from a directly linked source and bundling/republishing a copy are different delivery choices. Document the permitted choice before release; do not infer an unrestricted license from catalog presence.
5. Map fields to learning outcomes, identify gaps, and decide source-only, prepared subset, separate synthetic supplement or simulation. Never fabricate source semantics or silently change currency/date values to fit the old plan.
6. Freeze source-specific dictionary/metric contract and reproducible preparation log, then compute exact-version answers and verify in Tableau before releasing lessons.

Private source-inspection controls now exist, but no released lesson answers or source-specific Tableau steps have been validated. Refer to SOURCE_AUDIT.md for the four inspected candidates, DATA_STRATEGY.md for safeguards and CASE_STUDIES.md for planned activities. Sports/technology/government choices use existing practice or optional extensions; they do not erase the five core cases or add required contact hours.
