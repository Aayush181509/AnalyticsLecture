# DATA 300 — China classroom delivery plan

Created 2026-10-15. **Status: working plan built from the official syllabus and the user's timetable; day contents are a recommendation to confirm.** Source syllabus: `DATA300_Data Driven Decision Making_Syllabus_2026.pdf` (Westcliff University, 8-week course, 3 units). This is a **separate course** from the 16-session Python course, which stays unchanged.

## Confirmed by the user (2026-10-15)

| Item | Decision |
|---|---|
| Course | DATA 300 Data Driven Decision Making; syllabus graded work, weights and CLOs are authoritative |
| Teaching days | Tue 10, Wed 11, Thu 12, Mon 16, Tue 17, Wed 18, Thu 19 November 2026. Fri–Sun are free but may carry assignments and online support |
| Periods | 45 minutes; lunch from 11:40 |
| Tue | 08:10–11:40 theory (4 periods), 13:45–15:25 theory (2), 15:40–17:20 lab (2) |
| Wed | 08:10–11:40 theory (4), 13:45–15:25 theory (2), 15:40–20:10 lab with a dinner break (about 4 periods) |
| Thu | 08:10–11:40 theory (4), 13:45–17:20 lab (4) |
| Mon 16 | 08:10–11:40 theory (4) |
| Last teaching day | Thu 19 November; remaining graded work is due afterwards |
| Python environment | **Local Jupyter** on lab PCs or laptops (Anaconda), with data files shipped alongside the notebooks. No Google Colab or GitHub downloads, because those are blocked or unreliable in mainland China |
| Content strategy | Syllabus labs and assignments are the **graded work**, kept as written. Lectures and practice notebooks reuse our course material (Foundations, Sessions 1–16) |
| Location | Notebooks in `notebooks/China_Classroom/`; site section "DATA 300 (China classroom)" under `docs/china/` |

## Period budget

| Day | Theory periods | Lab periods |
|---|---|---|
| Tue 10 Nov | 6 | 2 |
| Wed 11 Nov | 6 | 4 |
| Thu 12 Nov | 4 | 4 |
| Mon 16 Nov | 4 | 0 |
| Tue 17 Nov | 6 | 2 |
| Wed 18 Nov | 6 | 4 |
| Thu 19 Nov | 4 | 4 |
| **Total** | **36 (27 h)** | **20 (15 h)** |

An 8-week syllabus has to fit 7 teaching days, so the plan follows **roughly one syllabus week per day**, with the weekend for Assignment 1 and revision.

## Day-by-day plan

| Day | Syllabus week | Theory | Lab | Graded work |
|---|---|---|---|---|
| **Tue 10 Nov** | 1 | Course, CLOs and graded work; data-driven decisions (Gordon Ch. 1); descriptive, predictive, prescriptive analytics; analysis fundamentals (Ch. 4); statistics are not enough (Anscombe, Datasaurus). Afternoon theory: Jupyter and Python basics, DataFrames, data types, grain | **Activity 1** self-assessment: Jupyter (Penguins EDA) and Tableau (Superstore) setup | Activity 1 (4%) |
| **Wed 11 Nov** | 1–2 | Descriptive statistics and distributions; data quality and cleaning; pivot tables and groupby; correlation and confounding (Simpson's paradox). Afternoon theory: visualisation principles, misleading statistics | **Lab 1** Diamonds data exploration; guided practice on the Tips data | Lab 1 (4%) |
| **Thu 12 Nov** | 2 | Communicating results (Ch. 5): storytelling, dashboards, KPIs and ratio metrics; marketing analytics (Ch. 6) | **Lab 2** Tableau dashboard; Assignment 1 briefing and start | Lab 2 (4%) |
| **Fri 13 – Sun 15** | 2–3 | Online support | — | **Assignment 1** Tips descriptive report (8%), due Sun 15 Nov |
| **Mon 16 Nov** | 3 | Text mining: structured vs unstructured data, tokenising, stop words, word frequency, word clouds, lexicon sentiment (VADER), limits and ethics; midterm scope | — | SM Activity 1 (3%) released |
| **Tue 17 Nov** | 4 | Forecasting (Ch. 9): components, naive and moving average, exponential smoothing, stationarity (ADF), ARIMA intuition, train/test, MAE/RMSE, forecast uncertainty | **Lab 3** text mining (reviews) | Lab 3 (4%) |
| **Wed 18 Nov** | 4–5 | Periods 1–2: **Midterm exam**. Then regression (Ch. 8): simple and multiple linear regression, coefficients, R², RMSE, train/test, multicollinearity, logistic regression intuition; predictive data mining with text features (Assignment 2 briefing) | **Lab 4** forecasting (CO₂); **Lab 5** multiple regression (MPG) | Midterm (15%), Lab 4 (4%), Lab 5 (4%) |
| **Thu 19 Nov** | 6–8 | Simulation and decision models in Excel (Monte Carlo, distributions, Data Tables, scenarios, risk); BI case studies, ethics and societal context; capstone briefing | **Lab 6** Excel simulation (EcoDrive); **Lab 7** BI case study start | Lab 6 (4%), Lab 7 (4%) |
| **After the course** | 5–8 | Online support | — | Assignment 2 (7%), Assignment 3 (7%), **Assignment 4 capstone (25%)**, SM Activity 2 reflection (3%) |

Proposed deadlines (to confirm with the institution): SM Activity 1 and Lab 7 by Sun 22 Nov; Assignment 2 and Assignment 3 by Sun 22 Nov; Assignment 4 and SM Activity 2 by Sun 29 Nov. All times China Standard Time unless the institution requires Pacific Time, as the syllabus states.

## Reuse of existing material

| Need | Reuse |
|---|---|
| Why analytics, statistics are not enough, misleading statistics, visual design, storytelling | `docs/foundations/` pages and figures |
| Python and Jupyter basics, data and grain, cleaning, descriptive statistics | Sessions 1–4 lecture notebooks, adapted for local Jupyter |
| Metrics and KPIs, visualisation, trends and growth | Sessions 5–7 |
| Correlation and regression; sampling and experiments | Sessions 8–9 |
| Dashboards and storytelling; capstone and executive briefing | Sessions 14–16 |

Adapting means copying a notebook into `notebooks/China_Classroom/` and replacing the Colab/GitHub data cells with local file loading. The original Python course is never edited for this.

## Resolved 2026-10-15 (user)

Proposed deadlines confirmed (treated as China Standard Time); GAP is the university Moodle; students use the Tableau student licence; lab PCs have Microsoft Excel; we write the midterm.

## Risks and open questions

1. **Internet access in China.** Syllabus labs download data from `raw.githubusercontent.com` and NLTK data from GitHub. Plan: bundle every dataset and the VADER lexicon in `notebooks/China_Classroom/data/` and replace downloads with local loading; test offline.
2. **Python packages.** Lab 3 needs `nltk` and `wordcloud`; Lab 4 needs `statsmodels` and `scikit-learn`. Anaconda includes most of these; `wordcloud` may need installing in advance. Provide a one-time setup check notebook.
3. **Tableau.** The student licence needs university-email verification and a download; Tableau Public Desktop is the fallback. Test installation on the lab PCs before 10 November.
4. **Excel** is needed for Labs 6–7 and Assignment 3; confirm Microsoft Excel (or WPS Spreadsheets, whose RAND/NORM.INV/Data Table support must be checked) on the lab PCs.
5. **Dataset rights.** The seaborn-data datasets (penguins, diamonds, tips, mpg) and the CO₂ series have their own sources and terms. Bundle them for classroom use; record sources before publishing copies in the public repository.
6. **LMS.** The syllabus submits to the university portal (GAP). Confirm whether the China cohort uses GAP or another system.
7. **Midterm.** Format, length and question bank are not specified in the syllabus extract; confirm whether the institution supplies it.
8. **Deadlines** above are proposals.

## Next steps

1. User confirms the day plan, deadlines and open questions 3–7.
2. Build `notebooks/China_Classroom/` day by day: lecture notebooks (theory, adapted from our course) plus the syllabus labs made offline-ready, with bundled data and private answer keys in `instructor/china_classroom/`.
3. Add the learner site pages per day and an offline setup check.
