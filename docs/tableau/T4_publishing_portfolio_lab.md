# T4 lab: A portfolio piece from your capstone

<p class="lead">
Turn the strongest finding of your capstone into a portfolio piece: one Tableau dashboard and a three-point story that a stranger can follow in a minute. Save it on your own computer with a clear version history, check that everyone can read it, and, only if you choose to and only with safe data, publish it to Tableau Public.
</p>

This lab builds on your capstone from the [Session 15 lab](../lectures/15_capstone_studio_lab.md) and your briefing from the [Session 16 lab](../lectures/16_executive_briefings_lab.md). You already have the decision, the evidence register, the checks and the recommendation. Today you show one part of that argument in Tableau. If you get stuck on a finding, look back at how you computed it in Python.

!!! note "Desktop and web editor"

    The click paths on this page are written for **Tableau Desktop Public Edition**. If you use the Tableau Public **web editor** in a browser, the menus differ slightly. Look for the same command in a nearby menu, or ask your facilitator. In the web editor, **saving publishes**: read the warning in the Setup section before you save anything there.

---

## The business decision

Your capstone was written for the chief operating officer of the teaching frame. A portfolio piece has a different reader:

> *Hiring manager: "Show me one piece of analysis you are proud of. I have a minute. Tell me what question you answered, what the data showed, what it could not show, and what you recommended."*

The decision is **which one finding** from your capstone best shows your work, and **how to tell it** so that a reader who has never seen this course understands it, trusts it, and knows its limits.

!!! note "About the data: five separate contexts"

    **Superstore** is a sample published by Tableau about a **fictitious** company, with Sales and Profit in the **file's own monetary units**. The **marketing-v1**, **finance-v1**, **operations-v1** and **hr-v1** files are **synthetic** data generated **separately** by the course for fictional organisations, with amounts in neutral **currency units**. They share no customers, orders, employees or keys. Never join, relate or blend two of them, and never explain one with another ([Session 15, Part 5](../lectures/15_capstone_studio_lecture.md)).

---

## How this lab works

| Part | What you do | Tasks |
|---|---|---|
| **Setup** | Choose your finding and its data, start a versioned workbook | Setup |
| **Core** | Plan the piece in four sentences; build one dashboard; build a three-point story; save and export | C1–C4 |
| **Stretch** | Keep a version log; check the piece for accessibility | S1–S2 |
| **Challenge** | Decide what is safe to publish; optionally publish to Tableau Public after the privacy checklist | X1–X2 |

Each task has a level:

- **Core**: everyone completes it; it is enough for your portfolio.
- **Stretch**: for when you finish the core tasks early.
- **Challenge**: optional, harder reasoning. **Publishing is never required.**

---

## What you will be able to do

1. Choose one capstone finding and write it as **question, evidence, limitation, action**.
2. Build a one-message dashboard on your capstone data, with each dataset on its own data source.
3. Build a three-point Tableau story with a headline and a caption on each point.
4. Save versions of a `.twbx` with dated names and a change log.
5. Check a portfolio piece for accessibility.
6. Decide whether a workbook is safe to publish, using the privacy checklist.

**Evidence you keep:** your four-sentence plan, your saved workbook, the PDF of your dashboard and story, and any Stretch and Challenge notes.

Before you start, work through the [T4 lecture](T4_publishing_portfolio_lecture.md). Have your capstone outline, evidence register and Session 16 brief to hand, and your T3 workbook for reference.

---

## Setup: choose your finding and start the workbook

### Step 1: Choose one finding

1. Open your capstone evidence register from the [Session 15 lab](../lectures/15_capstone_studio_lab.md) (G2–G3).
2. Pick the **one** finding that carries your recommendation. It should come from **one** dataset.
3. Write in your log: the finding, its dataset, its metric, grain and period, and the **check** you ran in Python. You use the check again in C2.

!!! tip "Which dataset should I choose?"

    Any of the five datasets is fine for the Core tasks, because you keep the work on your own computer. If you think you may do the publishing Challenge (X2), choose a finding from one of the **synthetic** datasets now: Superstore must not be published in this course.

### Step 2: Download the data

Download only the file or files your finding needs.

| Dataset | Where to get it | File to use |
|---|---|---|
| Superstore | Tableau's sample-data page, as in the [Tableau overview](index.md) | `sample_-_superstore.xls` (you already have it) |
| marketing-v1 | [marketing-v1 folder](https://github.com/Aayush181509/AnalyticsLecture/tree/main/data/synthetic/marketing-v1) | `marketing_daily.csv` |
| finance-v1 | [finance-v1 folder](https://github.com/Aayush181509/AnalyticsLecture/tree/main/data/synthetic/finance-v1) | `finance_actuals.csv`, `finance_budget.csv` |
| operations-v1 | [operations-v1 folder](https://github.com/Aayush181509/AnalyticsLecture/tree/main/data/synthetic/operations-v1) | `shipments.csv` |
| hr-v1 | [hr-v1 folder](https://github.com/Aayush181509/AnalyticsLecture/tree/main/data/synthetic/hr-v1) | `employees.csv`, `department_history.csv`, `recruitment.csv` |

For a synthetic dataset:

1. Open its folder on GitHub and read **README.md** first: the grain, the units and the rules for each measure.
2. Click the CSV file, then click the **Download raw file** button at the top right of the file view, as in the [T3 lab, S1 Step 1](T3_dashboards_lab.md).
3. Save it in your course data folder without renaming it.

### Step 3: Start a versioned workbook

1. Open **Tableau Desktop Public Edition**.
2. Connect to your file: **Microsoft Excel** for Superstore (then follow [Set up the Superstore data source](T1_fundamentals_lab.md#set-up-the-superstore-data-source)), or **Text file** for a synthetic CSV.
3. Check the field types in the preview: every date must show a calendar icon.
4. Choose **File → Save As**, pick **Tableau Packaged Workbook (*.twbx)**, and name the file with today's date and a version number:

    ```
    T4_portfolio_YourName_YYYY-MM-DD_v01.twbx
    ```

    For example `T4_portfolio_AnitaShrestha_2026-11-20_v01.twbx`.

!!! warning "If you use the web editor"

    In the Tableau Public web editor, **saving** puts your workbook and its data on your public profile. If your finding uses **Superstore**, ask your facilitator before you start: you may need to work in Tableau Desktop Public Edition, or with a synthetic dataset, so that nothing is saved to Tableau Public.

!!! warning "One dataset per data source"

    If your piece uses two datasets, add the second as a **separate** data source (**Data → New Data Source**). Do **not** drag it onto the first data source's canvas: that creates a relationship, which is a false join between two fictional organisations.

---

## Core tasks

### C1 (Core): Plan the piece in four sentences

Before you open a sheet, write four sentences in your log. Use the [T4 lecture, Part 5](T4_publishing_portfolio_lecture.md) and your Session 16 brief.

| Part | Your sentence |
|---|---|
| **Question** | What decision, for whom? |
| **Evidence** | What the data shows, with a comparison, period and unit (no number yet: you fill it in from Tableau in C2) |
| **Limitation** | What the data cannot show; that the data is synthetic or a fictitious sample |
| **Action** | What should happen, who owns it, what to monitor |

Then sketch the dashboard on paper, as in the [T3 lab, C2](T3_dashboards_lab.md): headline, tiles, the main view, at most one supporting view, and the scope note.

### C2 (Core): Build the dashboard

Build the sheets first, then the dashboard. Reuse the methods from T1 to T3.

1. Create the **measures** your finding needs as calculated fields. Rates are **ratios of sums**, never averages of rates ([T2 lecture, Part 2](T2_calculations_kpis_lecture.md)). Counts of orders, shipments or employees use `COUNTD` on the right ID.
2. Build **two or three KPI tiles** with a period label and a comparison ([T3 lab, C1 Part A](T3_dashboards_lab.md)).
3. Build the **main view** that shows your evidence, for example a monthly trend or a ranked bar chart. Use grey for context and **one** highlight colour for the thing your message is about.
4. **Reconcile.** Compare each tile with the value in your Python evidence register. They must agree, apart from rounding. If they do not, find out why before you go on, and write the reason in your log.
5. Choose **Dashboard → New Dashboard**, name it `Portfolio dashboard`, and set **Size → Fixed size** first.
6. Lay out the page in reading order: tiles at the top, the main view in the middle, the scope note at the bottom.
7. Write a **so-what headline** (**Dashboard → Show Title**, then double-click the title) and message titles on each view. Each must stay true for every selection a reader can make.
8. Add a **Text** object at the bottom with the **scope note**: dataset and version (for example *operations-v1, synthetic data for a fictional retailer*), period, units, definitions of your measures, and the main limitation.

!!! tip "Fewer views, stronger message"

    A portfolio dashboard has **one** message. If a view does not help a stranger understand your finding, leave it in the workbook and off the page.

Save your workbook (**File → Save**).

### C3 (Core): Build a three-point story

1. Choose **Story → New Story**. Name the tab `Portfolio story`.
2. Double-click the story title and write your **headline**: the same big idea as the dashboard.
3. Build three story points, each with a one-sentence caption:

| Point | What it shows | Caption |
|---|---|---|
| **1. Question and evidence** | Your `Portfolio dashboard` | The question, and the finding with its number in context |
| **2. A closer look** | The main view, or a second view that tests the finding (for example the same measure by month, or one group against the rest) | What the closer look confirms, or where the finding is weaker |
| **3. Limitation and action** | The view that best supports the recommendation | What the data cannot show, then the action, owner and monitoring measure |

4. To add a point, click **Blank** under **New story point** in the Story pane, then drag a sheet or dashboard onto the story. Use **Duplicate** to keep the same view with a different selection; click **Update** to keep a change in the current point.
5. Click through the three points in order. Read only the captions: do they tell the whole argument?

!!! warning "Check every point after a click"

    In a story, readers can still click and filter. Click a mark in each point, then check that the caption and titles are still true.

Save your workbook.

### C4 (Core): Save a version and export

1. Choose **File → Save As** and save a new version: `T4_portfolio_YourName_YYYY-MM-DD_v02.twbx`. Keep v01.
2. Open the `Portfolio dashboard` tab, clear any selection, and choose **File → Print to PDF...**. Under **Range**, choose **Active Sheet**. Save as `T4_portfolio_YourName_dashboard.pdf`.
3. Open the `Portfolio story` tab and do the same: `T4_portfolio_YourName_story.pdf`.
4. Open both PDFs. Check that the headline, titles, captions and scope note are readable, and that **all three story points** appear. If the story PDF shows only one point, click each point in turn and export it on its own.

---

## Stretch tasks

### S1 (Stretch): A version log

Keep a change log in your evidence log, as in the [T4 lecture, Part 3](T4_publishing_portfolio_lecture.md):

| Version | Date | What changed | Why | Checked |
|---|---|---|---|---|
| v01 | | | | |
| v02 | | | | |

1. Fill in v01 and v02 from today's work.
2. Ask a classmate to read your PDFs for one minute, then tell you the question, the finding and the action in their own words.
3. Make the change their answer shows you need (often the headline or one caption). Save it as **v03** with **File → Save As**, and add the row to the log. The **Checked** column must say what you verified after the change.

### S2 (Stretch): An accessibility check

Go through your dashboard and story with this list. Write **yes**, **no** or **fixed** next to each line in your log.

- [ ] The headline and captions alone tell the argument.
- [ ] Nothing is shown **only** by colour: the highlighted mark also has a label, a value or a title that names it.
- [ ] No red–green pair is the only difference between two things.
- [ ] Text is large enough to read when the page is shown at half size; grey text is dark enough to read.
- [ ] Axes start at zero for bars.
- [ ] Every number has its unit, period and comparison.
- [ ] Tooltips are written in plain words, not raw field names such as `AGG(ROAS)`. (Click **Tooltip** on the Marks card to edit them.)
- [ ] The scope note says the data is synthetic or a fictitious sample, and gives its source.

View the dashboard PDF in greyscale. Can you still find the mark your headline is about?

---

## Challenge tasks

### X1 (Challenge): Safe to publish?

For each case, write **publish**, **do not publish** or **publish only after a change**, and one sentence why. Use the [T4 lecture, Part 2](T4_publishing_portfolio_lecture.md).

1. Your T3 marketing dashboard on marketing-v1, with a scope note that says *synthetic data*.
2. Your T3 decision dashboard on Superstore.
3. A dashboard of your employer's monthly sales by branch, with branch names replaced by letters.
4. A dashboard on hr-v1 whose scope note calls it *"Our company's staff turnover"*.
5. A workbook on operations-v1 that also contains, on a hidden sheet, a second data source with Superstore.
6. A public dataset you found on a website with no licence, about house prices in your city.
7. A dashboard of course survey answers from your classmates, with names removed but with age and home town.

### X2 (Challenge, optional): Publish to Tableau Public

**Only do this if you want a public portfolio link.** It is not needed to pass the lab, and nothing you submit on Moodle depends on it.

#### Step 1: Complete the privacy checklist

Write each line in your log with **yes** or **no**. If any line is **no**, stop: do not publish.

1. Every data source in the workbook is **synthetic course data** (marketing-v1, finance-v1, operations-v1 or hr-v1). Check the Data pane: every data source listed is published, even if no sheet uses it.
2. No data source holds **workplace, customer or employee** data, or anything copied from them.
3. **Superstore is not** in the workbook, not even on an unused or hidden sheet.
4. The scope note says the data is **synthetic**, describes a **fictional** organisation, and gives units (currency units) and period.
5. Nothing names a real person, a real company or your employer.
6. I have decided whether to allow downloads, and I know the views stay public either way.
7. I know that hiding the viz does not make it private, and that a downloaded copy cannot be recalled.

!!! warning "If your finding uses Superstore"

    Build a second, smaller piece on one synthetic dataset and publish that instead, or do not publish. Keep your Superstore work on your own computer.

#### Step 2: Save a local copy first

Save your workbook locally with **File → Save As** (a new version number). Publishing does not replace your local file, and your Moodle submission is always the local `.twbx`.

#### Step 3: Publish

1. Choose **Server → Tableau Public → Save to Tableau Public...**.
2. Sign in with your Tableau Public account.
3. Enter a clear, descriptive title, for example *"Peak-season delivery reliability (synthetic data)"*, and click **Save**.
4. Tableau creates an extract of your data and opens the viz on the Tableau Public website.

#### Step 4: Check what a stranger sees

1. On the viz page, open the viz **settings**. Decide whether to allow others to **download** the workbook and its data, and set the option. (Tableau's FAQ describes this option in the viz settings; the exact label may differ.)
2. Click **Edit Details** and write a short description: the question, that the data is **synthetic** and generated by a course for a fictional organisation, and the link to the dataset's folder on GitHub.
3. Copy the viz's URL. Open a **private browser window** (not signed in) and paste it. This is what a stranger sees. Check the download button and every tooltip.
4. Write the URL in your log.

!!! note "Changed your mind?"

    You can delete the viz from your Tableau Public profile. Deleting removes it from the website, but anyone who has already downloaded it or taken a screenshot keeps their copy.

---

## Evidence checklist

Before you submit, check that you have:

- [ ] your four-sentence plan (question, evidence, limitation, action) and your paper sketch
- [ ] your reconciliation of the tiles with your Python evidence register
- [ ] the `Portfolio dashboard` with headline, message titles and scope note
- [ ] the `Portfolio story` with three points and a caption on each
- [ ] at least two dated versions of your workbook
- [ ] the dashboard and story PDFs
- [ ] Stretch and Challenge notes, if you did them (version log, accessibility check, X1 answers, the privacy checklist and URL if you published)

---

## Submit on Moodle

1. Save your final version locally (**File → Save As**): for example `T4_portfolio_YourName_YYYY-MM-DD_v03_submitted.twbx`. Do not change this file after you submit.
2. Export the dashboard and the story as PDFs (C4).
3. Open the **T4 lab** assignment on the course Moodle page.
4. Upload the `.twbx` file, the PDF (or PDFs) of your portfolio piece, and your written answers (from your evidence log). If you published in X2, add the URL.

!!! warning "Moodle, not Tableau Public"

    Your submission is the **local** `.twbx` and the PDF. A Tableau Public link alone is not a submission, and you never need to publish to pass.

---

## Next

This is the last Tableau session. Keep your portfolio workbook and its version log with your capstone notebook and brief from [Session 15](../lectures/15_capstone_studio_lab.md) and [Session 16](../lectures/16_executive_briefings_lab.md): together they show the whole path from a business question to a checked recommendation.
</content>
</invoke>
<invoke name="Bash">
<parameter name="command">cd /Users/aayush/Documents/Kings/Data && git check-ignore -v instructor/tableau/T4/answers.md; mkdir -p instructor/tableau/T4