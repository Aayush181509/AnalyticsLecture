# DATA 300 (GAP course)

<p class="lead">
DATA 300 <em>Data Driven Decision Making</em> as it runs on GAP (Moodle), taught in person in China from 10 to 19 November 2026. These pages follow the GAP course item by item and add lectures, worked examples and practice that go further than GAP does.
</p>

!!! note "Draft materials"

    Every page of this section now exists: the overview, timetable and setup page, the pre-class refresher, the lectures for Days 1 to 7, and a guide for every graded item from Activity 1 to the capstone. All of them are **drafts** awaiting the facilitator's review. The Python code has been run offline, but the Excel and Tableau steps have **not yet been tried end to end in the real programs**, so menu names and click paths may differ slightly from what you see. Announcements in class and the wording on GAP take precedence.

---

## What the course is about

Every organisation makes decisions. This course is about making them on evidence: describing what happened, predicting what is likely to happen, and choosing what to do. You will work with real and case data in **Python (JupyterLab)**, **Tableau Desktop** and **Microsoft Excel**, and you will learn to explain each result to a manager who has to act on it.

| Theme | You will learn to |
|---|---|
| Descriptive analytics | Explore data, check its quality, summarise it and spot patterns without over-reading them |
| Visualisation and communication | Choose honest charts, build a dashboard and tell a short, clear story with data |
| Text mining | Turn customer reviews into word counts and sentiment scores |
| Forecasting | Model a time series, test the forecast on data it has not seen and measure its error |
| Predictive regression | Build a regression model, judge it on new data and read its coefficients sensibly |
| Spreadsheet simulation | Model uncertainty in Excel with What-If Data Tables and Monte Carlo trials |
| Business intelligence | Combine everything into a managerial recommendation that weighs ethics and society |

---

## Course learning outcomes

The official course learning outcomes are:

1. **CLO 1:** Describe the principles of descriptive, predictive and prescriptive analytics to solve business data challenges.
2. **CLO 2:** Design and use data visualisation and modelling tools to communicate user-centred analytics for strategic decisions.
3. **CLO 3:** Apply computational problem-solving to perform data and text mining, discovering relationships in structured and unstructured data.
4. **CLO 4:** Develop predictive models using time series forecasting, linear regression and spreadsheet simulation to project future outcomes.
5. **CLO 5:** Evaluate the impact of business intelligence tools within a comprehensive case study to generate managerial reports that consider ethical and societal contexts.

---

## The four modules

| Module | When | Mode | Main work |
|---|---|---|---|
| Pre-class | The week before Tuesday 10 November | Online, self-study | Setup, Python refresher, Activity 1 |
| In-class Module 1 | Tuesday 10 – Thursday 12 November | On campus | Exploring data, visualisation and Tableau, midterm, text mining, forecasting; Labs 1–4; Assignment 1 |
| In-class Module 2 | Monday 16 – Thursday 19 November | On campus | Regression, spreadsheet simulation, business intelligence and ethics, final exam; Labs 5–7; Assignments 2–3 |
| Post-class | The week after 19 November | Online | Assignments 2 and 3, and the capstone (Assignment 4) |

The [timetable](timetable.md) shows what happens in every period.

---

## Graded work

| Item | Tool | Weight | Due (23:59 China Standard Time) |
|---|---|---|---|
| Activity 1: Readiness self-check | JupyterLab and Tableau | 4% | Monday 9 November |
| Lab 1: Data exploration | JupyterLab | 3% | Tuesday 10 November |
| Lab 2: Dashboard | Tableau | 3% | Wednesday 11 November |
| Lab 3: Text mining | JupyterLab | 3% | Thursday 12 November |
| Lab 4: Forecasting | JupyterLab | 3% | Thursday 12 November |
| Lab 5: Regression | JupyterLab | 2% | Tuesday 17 November |
| Lab 6: Spreadsheet simulation | Excel | 2% | Wednesday 18 November |
| Lab 7: Business intelligence case | Excel and Tableau | 2% | Wednesday 18 November |
| Assignment 1: Descriptive analytics report | JupyterLab | 6% | Sunday 15 November |
| Assignment 2: Predictive data mining report | JupyterLab | 6% | Sunday 22 November |
| Assignment 3: Simulation decision model | Excel | 6% | Sunday 22 November |
| Midterm exam (Thursday 12 November, periods 1–2) | In class | 15% | — |
| Final exam (Thursday 19 November) | In class | 20% | — |
| Assignment 4: Capstone | JupyterLab, Tableau and Excel | 25% | Sunday 29 November |
| **Total** | | **100%** | |

Labs are due at the end of the day they are set unless your facilitator announces otherwise. Everything is submitted on **GAP (Moodle)**.

---

## Three environments

The course grades work done in three different programs. Knowing which one a task needs, and how each one keeps (or loses) your work, saves more marks than any formula.

| | JupyterLab (Python) | Tableau Desktop | Microsoft Excel |
|---|---|---|---|
| Where it runs | **Route A:** Try JupyterLab, inside a browser tab. **Route B:** Anaconda JupyterLab on your own laptop | Installed on your laptop | Installed on your laptop or the lab PC |
| Setting up | Route A: install packages with `%pip` at the start of every session. Route B: nothing to install each time | Activate the free student licence once | Nothing extra; Data Tables and Forecast Sheet are built in |
| Where your work is kept | Route A: inside that browser, and it can disappear. Route B: an `.ipynb` file on your disk | A `.twbx` workbook you save | An `.xlsx` file you save |

### Why you export before closing a Try JupyterLab tab

Try JupyterLab runs Python **inside the browser tab** (a system called Pyodide), not on a server and not on your disk. The moment the tab closes, the Python session ends: every variable, installed package and chart is gone. The notebook file may survive in that browser's storage, but it disappears if the browser data is cleared, and it is not on any other computer. So before you close the tab:

1. Run every cell from the top, so all outputs are visible.
2. Export a **PDF** (**File → Print → Save as PDF**, with *Background graphics* ticked).
3. Download the notebook too (right-click it in the file browser → **Download**), so you can open it again later.

The [setup page](setup.md) explains both Python routes in detail.

---

## Start here

1. Read the [setup page](setup.md) and get JupyterLab, Tableau and Excel working.
2. Work through the [Python and Jupyter refresher](D0_lecture_python_jupyter_refresher.md).
3. Complete [Activity 1](guides/activity1_readiness.md) by **Monday 9 November**.

---

## Main textbook

Gordon, M. E. (2023). *Business analytics: Combining data, analysis and judgement to inform decisions*. SAGE Publications.

The course also has a reading packet with one chapter per module; each lecture says which chapter to read.

*This section is adapted from the DATA 300 GAP course (Westcliff University) and written in our own words.*
