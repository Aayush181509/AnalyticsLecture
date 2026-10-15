# Learning roadmap

<p class="lead">
The course has sixteen Python sessions, followed by a Tableau section. Every session has two parts: a <strong>Lecture</strong> that teaches the theory with worked examples, and a <strong>Lab</strong> where you practise it yourself on real and synthetic data.
</p>

!!! note "This is the planned sequence"

    Lecture and lab materials are released only after they have been checked. Sessions marked with a link already have draft material.

---

## How each session works

**Lecture.** A short recap quiz, then the theory, explained with examples and questions where you predict the answer before seeing it. It ends with a worked case in code.

**Lab.** Three levels of practice in a Colab notebook:

1. **Guided:** step-by-step, everyone together.
2. **Independent:** the same skill applied to a new question.
3. **Challenge:** a harder problem or a deliberate mistake to debug.

You keep the evidence from every lab in your portfolio.

---

## Part A: Thinking with data

| Session | Lecture | Lab |
|---|---|---|
| **1. Why data analytics matters** | [Why data analytics matters](../lectures/01_why_data_analytics_lecture.md): the four levels of analytics, decision-driven questions, and why statistics alone can mislead | [Python, Colab and always plotting your data](../lectures/01_why_data_analytics_lab.md): recreate Anscombe's quartet and the Datasaurus |
| **2. Data, grain and the DataFrame** | [Data, grain and the DataFrame](../lectures/02_data_and_grain_lecture.md): types of data, tidy data, grain and keys, data dictionaries, data quality | [Can we trust the sales table?](../lectures/02_data_and_grain_lab.md) |
| **3. Cleaning and preparing data** | [Cleaning and preparing data](../lectures/03_cleaning_and_preparing_lecture.md): missing data, duplicates, outliers, dates, joins and their pitfalls, reshaping | [Clean World Cup and mobile-OS data; merge tables safely](../lectures/03_cleaning_and_preparing_lab.md) |

---

## Part B: Describing and measuring

| Session | Lecture | Lab |
|---|---|---|
| **4. Descriptive statistics and distributions** | [Descriptive statistics and distributions](../lectures/04_descriptive_statistics_lecture.md): centre, spread, percentiles, skew, outliers, histograms and box plots | [Distributions of order value and shipping time; median vs mean house prices](../lectures/04_descriptive_statistics_lab.md) |
| **5. Metrics and KPIs** | [Metrics and KPIs](../lectures/05_metrics_and_kpis_lecture.md): designing metrics, ratios of totals, weighted rates, Simpson's paradox | [Which segment deserves a closer look?](../lectures/05_metrics_and_kpis_lab.md); the Berkeley admissions paradox |
| **6. Visualisation principles** | [Visualisation principles](../lectures/06_visualisation_principles_lecture.md): choosing charts, perception, data-ink, Gestalt, colour and accessibility ([Designing clear visuals](../foundations/visual-design.md)) | [Redesign bad charts; one-, two- and many-variable views](../lectures/06_visualisation_principles_lab.md) |

---

## Part C: Relationships, change and uncertainty

| Session | Lecture | Lab |
|---|---|---|
| **7. Time series and trends** | [Time series and trends](../lectures/07_trends_and_growth_lecture.md): trend and seasonality, month-on-month vs year-on-year, moving averages | [Trends, returns and a decision dashboard](../lectures/07_trends_and_growth_lab.md); construction spending |
| **8. Correlation and regression** | [Correlation and regression](../lectures/08_correlation_and_regression_lecture.md): correlation, confounding, simple linear regression, residuals | [Discount vs profit; advertising spend vs revenue](../lectures/08_correlation_and_regression_lab.md) |
| **9. Sampling, uncertainty and experiments** | [Sampling, uncertainty and experiments](../lectures/09_sampling_and_experiments_lecture.md): samples and populations, confidence intervals, A/B tests, practical vs statistical significance | [Simulate sampling; bootstrap a confidence interval; analyse an A/B test](../lectures/09_sampling_and_experiments_lab.md) |

---

## Part D: Business cases

| Session | Lecture | Lab |
|---|---|---|
| **10. Finance** | [Budget accountability](../lectures/10_finance_budget_lecture.md): budget vs actual, variance, reconciliation | [Which spending needs review?](../lectures/10_finance_budget_lab.md) |
| **11. Operations** | [Service performance](../lectures/11_operations_service_lecture.md): service levels, open shipments, delay distributions | [Are deliveries on time?](../lectures/11_operations_service_lab.md) |
| **12. Marketing** | [Campaign evaluation](../lectures/12_marketing_campaigns_lecture.md): funnels, weighted conversion, cost per acquisition, attribution limits | [Which campaigns deserve the budget?](../lectures/12_marketing_campaigns_lab.md) |
| **13. HR** | [Workforce analytics](../lectures/13_hr_workforce_lecture.md): headcount, turnover, recruitment, fairness and privacy | [Is workforce change creating a capacity problem?](../lectures/13_hr_workforce_lab.md) |

---

## Part E: Communicating and bringing it together

| Session | Lecture | Lab |
|---|---|---|
| **14. Dashboards and storytelling** | [Dashboards and storytelling](../lectures/14_dashboards_storytelling_lecture.md): audience, the big idea, dashboard design, the Challenger case | [From analysis to a decision dashboard](../lectures/14_dashboards_storytelling_lab.md) |
| **15. Capstone studio** | [Combining evidence](../lectures/15_capstone_studio_lecture.md): evidence registers, no false joins, validation, trade-offs | [Build your capstone](../lectures/15_capstone_studio_lab.md) |
| **16. Executive briefings** | [Executive briefings](../lectures/16_executive_briefings_lecture.md): recommendation first, uncertainty, handling questions | [Brief, critique, revise](../lectures/16_executive_briefings_lab.md) |

---

## Part F: Tableau

| Session | Lecture | Lab |
|---|---|---|
| **T1. Tableau fundamentals** | How Tableau thinks: dimensions, measures, aggregation | Rebuild earlier views ([draft](../lessons/class-01.md)) |
| **T2. Calculations and KPIs** | Calculated fields, distinct counts, table calculations | Rebuild the segment KPIs and growth measures |
| **T3. Dashboards in Tableau** | Layout, filters, actions, accessibility | Rebuild your decision dashboard |
| **T4. Publishing and portfolio** | Tableau Public and privacy | Your Tableau portfolio piece |

---

## What you will be able to do

By the end of the course you should be able to:

1. Turn a business request into a clear question with a decision, population, period and measure.
2. Load, inspect, clean and reshape data in Python, keeping a record of every change.
3. Describe data with the right statistics and charts, and explain distributions, outliers and skew.
4. Define metrics precisely and avoid the common traps.
5. Measure relationships and change over time, and explain what correlation and regression can and cannot show.
6. Express uncertainty with confidence intervals and simple experiments.
7. Design clear charts and dashboards, and tell a decision-focused story.
8. Apply all of this to retail, finance, operations, marketing and HR, and defend a recommendation to executives.
9. Rebuild key analyses in Tableau.

---

## How you will be assessed

- **Theory quizzes** at the start of each lecture help you check your understanding. They are for feedback.
- Your **lab portfolio** collects your evidence from every session and covers all five business areas.
- Your **capstone** combines findings from at least three areas into a dashboard and an executive briefing.

Feedback rewards correct reasoning, careful checking and honest statements of uncertainty, not only attractive charts.

---

## Extra practice topics

Selected datasets from the [Tableau sample-data catalog](https://public.tableau.com/app/learn/sample-data) give you practice in sports, technology, government and more. Each keeps its own real dates, units and context.
