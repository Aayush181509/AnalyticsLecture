# Course plan: Applied Data Analytics with Python (then Tableau)

Created 2026-10-14 (Asia/Kathmandu). **Status: the working plan, agreed in structure with the user (DEC-044); session contents are a recommendation to refine.** It replaces the 12 × 2-hour design in CURRICULUM.md for teaching structure. Metric contracts, case designs, data rules and the publication boundary in DATA_STRATEGY, CASE_STUDIES and AGENTS still apply.

## Confirmed by the user

| Item | Consequence |
|---|---|
| Every session = **2-hour lecture + 3-hour lab** | Theory and worked examples first, then hands-on practice the same day |
| Theory depth: **applied statistics for analysts** | Descriptive statistics, distributions, sampling and uncertainty, correlation, intro regression, confidence intervals and A/B tests, time-series basics. Always tied to a business decision; no proofs |
| Python first in Google Colab, read → run → modify | Learners run working code and change it in exercises; Tableau is a later section |
| Notebooks are the source; `make convert-all` publishes them | Each session = one lecture notebook and one lab notebook |
| Learner pages show **Lecture** and **Lab** parts, no hours | Hours appear only in this internal plan |
| Five business domains, Foundations before tools, content-first | Unchanged from earlier decisions |

The number of sessions follows the content. Below: **16 Python sessions + 4 Tableau sessions**. Calendar, class size and cadence remain open (R01).

## Session format

| Part | Length | Structure |
|---|---|---|
| **Lecture** | 2 h | 10 min recap quiz → 70 min theory with live examples and "predict, then reveal" questions → 10 min break → 25 min worked case in code → 5 min summary and lab briefing |
| **Lab** | 3 h | 45 min guided practice (step-by-step, everyone) → 10 min break → 75 min independent tasks (same skill, new question) → 35 min challenge or debugging task → 15 min share-out and exit ticket |

Each session produces: a **lecture notebook** (`NN_topic_lecture.ipynb`: theory, demonstrations, check-your-understanding questions), a **lab notebook** (`NN_topic_lab.ipynb`: guided, independent and challenge tasks with default code to modify), a short **theory quiz** (5–8 questions, start of next lecture), and private **instructor answers** in `instructor/sessions/NN/`.

Labs run at three levels so mixed experience works: **core** (everyone, enough for the portfolio), **stretch** (faster learners) and **challenge** (optional, harder reasoning).

## Learning outcomes (whole course)

1. Turn a business request into an answerable question with a decision, population, period and measure.
2. Load, inspect, clean and reshape data in pandas, keeping a reproducible preparation log.
3. Describe data with the right statistics and charts, and explain distributions, outliers and skew.
4. Define metrics precisely (grain, denominator, weighting) and avoid common traps.
5. Measure relationships and change over time, and explain what correlation and regression can and cannot show.
6. Quantify uncertainty with sampling ideas, confidence intervals and simple experiments.
7. Design clear visuals and dashboards and tell a decision-focused story.
8. Apply all of the above to retail, finance, operations, marketing and HR, and defend a recommendation to executives.
9. Rebuild key analyses in Tableau (later section).

## Session overview

| # | Session | Lecture: theory | Lab: practice | Main data |
|---|---|---|---|---|
| **Part A — Thinking with data** |||||
| 1 | Why data analytics matters | Four levels of analytics; decision-driven questions; workflow; Anscombe, Datasaurus; misleading statistics | Colab and Python basics; recreate Anscombe and Datasaurus; compute and plot summaries | Built-in, Datasaurus |
| 2 | Data, grain and the DataFrame | Data types (nominal, ordinal, interval, ratio); tidy data; grain and keys; data dictionaries; data-quality dimensions | Load Superstore; types, dates, grain; rows vs orders; returns flag; hand-check one order | Superstore |
| 3 | Cleaning and preparing data | Missing data and why it matters; duplicates; outliers; type and date conversion; joins and cardinality; reshaping; reproducible logs | Fix World Cup duplicates and attendance text; Mobile OS missing dates; merge Orders, Returns and People with checks | World Cup, Mobile OS, Superstore |
| **Part B — Describing and measuring** |||||
| 4 | Descriptive statistics and distributions | Centre, spread, percentiles, shape, skew; box plots and histograms; z-scores; normal distribution as a reference | Distributions of order value, ship days, profit; median vs mean for home prices; spot outliers | Superstore, US Home Sales |
| 5 | Metrics and KPIs | Metric design and contracts; ratios of sums; weighted vs mean of rates; distinct counts; Simpson's paradox | Segment KPI table with reconciliation; Berkeley admissions paradox; debug a wrong KPI | Superstore, Berkeley |
| 6 | Visualisation principles | Chart choice; perception and pre-attentive attributes; data-ink; Gestalt; colour and accessibility; honest axes | Redesign bad charts; univariate, bivariate and multivariate plots; small multiples | Superstore, synthetic |
| **Part C — Relationships, change and uncertainty** |||||
| 7 | Time series and trends | Trend, seasonality, noise; MoM vs YoY; moving averages; index numbers; incomplete periods | Retail monthly trends and growth; construction spending series selection and seasonality | Superstore, US Construction |
| 8 | Correlation and regression | Covariance; Pearson and Spearman; confounding; simple linear regression; slope, R², residuals; extrapolation risk | Discount vs profit; ad spend vs revenue; residual plots; Anscombe regression | Superstore, synthetic marketing |
| 9 | Sampling, uncertainty and experiments | Population vs sample; sampling distribution; standard error; confidence intervals (bootstrap); A/B tests, p-values, practical vs statistical significance | Simulate sampling; bootstrap CI for AOV; analyse a synthetic A/B test; sample-size intuition | Superstore, synthetic A/B |
| **Part D — Business cases** |||||
| 10 | Finance: budget accountability | Budget vs actual; variance and favourability; reconciliation; join multiplication; materiality | Variance analysis; fix a duplicated-budget join; prioritise departments | Synthetic finance |
| 11 | Operations: service performance | Service levels; promised vs actual; open shipments and censoring; percentiles and tails; process variation | On-time rate with pending shipments; delay distributions by carrier; debug a dropped-records bug | Synthetic operations |
| 12 | Marketing: campaign evaluation | Funnel metrics; weighted conversion; CPA and ROAS; attribution limits; experiments vs observational data | Campaign comparison; mean-of-rates bug; interpret an A/B lift with a CI | Synthetic marketing |
| 13 | HR: workforce analytics | Headcount snapshots; turnover with average headcount; cohorts and tenure; fairness, privacy and small groups | Historical turnover; cohort retention; debug current-headcount denominator | Synthetic HR |
| **Part E — Communicating and synthesising** |||||
| 14 | Dashboards and storytelling | Audience and big idea; situation–complication–resolution; dashboard layout; annotation; Challenger case | Multi-panel dashboard in matplotlib; message titles; a three-slide story | All prior |
| 15 | Capstone studio | Synthesis across domains; evidence registers; trade-offs; validation packs; peer review | Build capstone analysis and dashboard with coaching | Learner's chosen domains |
| 16 | Executive briefings | Presenting to executives; handling questions; reflecting on limitations | Briefings, peer critique, revision plan | Capstone |
| **Part F — Tableau (later)** |||||
| T1 | Tableau fundamentals | Tableau's model: dimensions, measures, aggregation, marks | Rebuild Sessions 2 and 4 views | Superstore |
| T2 | Calculations and KPIs in Tableau | Calculated fields, COUNTD, ratio of sums, table calcs | Rebuild Session 5 KPIs and Session 7 growth | Superstore |
| T3 | Dashboards in Tableau | Layout, filters, actions, accessibility | Rebuild the Session 14 dashboard | Superstore + one case |
| T4 | Publishing and portfolio | Tableau Public privacy; versioning | Final Tableau portfolio piece | Capstone |

## Session details

Each line below is the core content. Lecture notebooks must include short "check your understanding" questions; lab notebooks must contain core, stretch and challenge tasks.

### 1. Why data analytics matters
- **Lecture:** the Foundations stories (Snow, Nightingale, Moneyball, Walmart, Google Flu Trends); descriptive → prescriptive; question → recommendation workflow; Anscombe and Datasaurus as "always plot your data"; preview of misleading statistics.
- **Lab:** Colab basics (current Lesson 0); variables, lists, DataFrames; compute Anscombe statistics and plot all four; Datasaurus small multiples.
- **Evidence:** a workplace decision rewritten as an analytical question; Anscombe plots with a two-sentence lesson.

### 2. Data, grain and the DataFrame
- **Lecture:** levels of measurement and what you can compute with each; tidy data; grain, primary keys, foreign keys; data dictionaries; quality dimensions (completeness, validity, consistency, uniqueness, timeliness).
- **Lab:** current Lessons 1–2 (load, inspect types and dates, grain, `nunique`, returns flag, hand-checked order, segment vs category overlap).
- **Evidence:** grain statement, quality checklist, preparation log.

### 3. Cleaning and preparing data
- **Lecture:** types of missingness and their risks; when to drop, flag or keep; duplicates vs legitimate repeats; outlier detection vs deletion; parsing text numbers and dates; join types and cardinality (one-to-one, one-to-many, many-to-many); reshaping (wide ↔ long); never overwrite raw data.
- **Lab:** World Cup: remove 16 duplicate 2014 matches, parse European-style attendance, fix encoding; Mobile OS: diagnose missing dates and decide what is defensible; Superstore: merge Returns and People with row-count checks.
- **Evidence:** a cleaning log with before/after counts.

### 4. Descriptive statistics and distributions
- **Lecture:** mean, median, mode; range, IQR, standard deviation; percentiles; skew and long tails; histograms, box plots, ECDFs; z-scores; the normal curve as a reference, not an assumption.
- **Lab:** distributions of order value and ship days by segment and ship mode; profit tails; US home sales median vs average price; outlier flags with IQR rule.
- **Evidence:** a distribution summary with the right centre and spread for each variable.

### 5. Metrics and KPIs
- **Lecture:** what makes a good metric; metric contracts (grain, numerator, denominator, scope, zero/missing rules); ratio of sums vs mean of ratios; weighted rates; non-additive distinct counts; Simpson's paradox.
- **Lab:** current Lesson 3 (segment KPIs, reconciliation, debugging); Berkeley admissions; write a metric contract.
- **Evidence:** segment KPI table, metric contract, five-sentence recommendation.

### 6. Visualisation principles
- **Lecture:** Foundations visual pages in depth: chart choice by task, pre-attentive attributes, data-ink, Gestalt, colour for categories vs magnitude, colour-blind safety, honest axes, annotation.
- **Lab:** redesign three bad charts; univariate, bivariate and multivariate views of Superstore; small multiples by region.
- **Evidence:** before/after chart pairs with a short critique.

### 7. Time series and trends
- **Lecture:** components of a series; MoM vs YoY; rolling averages; index (base = 100); seasonal patterns; incomplete and missing periods; growth on filtered data.
- **Lab:** current Lesson 4 trends and growth; construction spending: choose one consistent series, plot seasonality, compare YoY.
- **Evidence:** trend chart with correct growth measure and a seasonal explanation.

### 8. Correlation and regression
- **Lecture:** scatter plots; covariance and correlation (Pearson, Spearman); correlation ≠ causation, confounders, reverse causation; simple linear regression: slope interpretation, R², residuals, outliers and leverage; dangers of extrapolation.
- **Lab:** discount vs profit ratio by line and by order; synthetic ad spend vs revenue regression; residual plots; Anscombe regressions showing identical fits.
- **Evidence:** an interpreted regression with one stated limitation.

### 9. Sampling, uncertainty and experiments
- **Lecture:** population, sample, sampling error; sampling distributions by simulation; standard error; confidence intervals (bootstrap first, formula second); A/B tests: randomisation, control, lift, p-value meaning, practical vs statistical significance, peeking and multiple comparisons.
- **Lab:** draw repeated samples from Superstore orders; bootstrap a CI for AOV; analyse a synthetic A/B test with CI and p-value; explore how sample size changes the CI.
- **Evidence:** a CI and A/B result explained in plain language for a manager.

### 10–13. Business cases
Each case follows the same pattern from CASE_STUDIES.md: stakeholder brief, dictionary, metric contract, worked example (lecture), guided + independent + debugging tasks (lab), recommendation challenge, private answers.
- **Finance:** budget vs actual, signed and percentage variance, cost favourability, zero/unknown budgets, the duplicated-budget join trap.
- **Operations:** due shipments including still-open ones, on-time rate, delay percentiles, carrier comparison weighted by volume, the dropped-pending-records trap.
- **Marketing:** funnel counts, weighted conversion, CPA, ROAS, synthetic single-campaign attribution and its limits, an A/B lift with uncertainty, the mean-of-rates trap.
- **HR:** monthly headcount snapshots, turnover on average headcount, cohort retention, tenure distribution, small-group privacy, the current-headcount trap.

### 14. Dashboards and storytelling
- **Lecture:** Foundations storytelling and Challenger in depth; exploratory vs explanatory; dashboard layout, hierarchy, filters and annotations; writing for executives.
- **Lab:** build a decision dashboard (matplotlib subplots) for one case; write message titles; draft a three-slide story.

### 15–16. Capstone
- **Lecture 15:** combining evidence across domains without false joins; evidence register; validation pack; trade-offs. **Lab 15:** capstone build with coaching.
- **Lecture 16:** executive presentation technique and handling challenge. **Lab 16:** briefings, peer critique, revision.

## Data plan

| Data | Used in | Status |
|---|---|---|
| Superstore retail-v1 (fictitious sample, downloaded from Tableau in each notebook) | 2–9, 14 | Validated (D01–D03 numerical) |
| Datasaurus Dozen, Anscombe, Berkeley 1973, Challenger | 1, 4, 5, 8, 14 | Preserved and used in Foundations |
| World Cup, Mobile OS, US Construction, US Home Sales (Tableau catalog) | 3, 4, 7 | Audited; prepared subsets and rights notes needed |
| Synthetic finance, operations, marketing (incl. A/B test), HR | 8–13 | Contracts designed in CASE_STUDIES / DATA_STRATEGY; generators to build (D04–D07, D08 A/B) |

## Assessment

- **Theory quizzes** (start of each lecture): formative, check understanding of the previous session.
- **Lab portfolio:** core lab evidence from every session; must cover all five business domains.
- **Capstone:** analysis across at least three domains, validation pack, dashboard and executive briefing.
- Rubric from ASSESSMENT.md applies, extended with a "statistical reasoning" criterion (uncertainty, correlation vs causation, appropriate summaries).

## Mapping existing material

| Existing | New place |
|---|---|
| Foundations pages | Lecture reading for Sessions 1, 6, 14; preserved as the site's Foundations section |
| `00_python_and_colab_basics.ipynb` | Session 1 lab |
| `01_decision_to_evidence.ipynb`, `02_trust_the_sales_table.ipynb` | Session 2 lab (to split into lecture + lab) |
| `03_segment_comparison.ipynb` | Session 5 lab |
| `04_trends_returns_dashboard.ipynb` | Session 7 lab (dashboard part also feeds Session 14) |
| Tableau drafts | Part F |
