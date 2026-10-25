# Assignment 1: Descriptive analytics report

<p class="lead">
Your first written analytics report. You run a given Python script on a restaurant's transaction records (bills, tips, party sizes, days and shifts), which prints two summary tables and draws three figures, and you turn what they show into a four-section business report for the restaurant's owner. You submit the report and the executed notebook as one PDF on GAP.
</p>

*Adapted from the DATA 300 GAP course, In-Class Module 1, Assignment 1: Data Visualization and Descriptive Analytics Report. Written in our own words; follow GAP for the official wording.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Run GAP's script (no coding of your own is required), read Table 1, Table 2 and Figures 1–3, and write a report under four fixed headings with two recommendations |
| **Why** | You play an analyst at a consulting firm, *Bistro Analytics*. The owner wants to schedule staff for the busiest periods and to understand tipping well enough to train servers in upselling. The skill being graded is turning tables and charts into evidence-based, specific advice |
| **CLOs** | CLO 1 (how descriptive analytics supports decisions), CLO 2 (visualisations that communicate findings), CLO 3 (computational methods to organise and analyse data) |
| **Weight** | 6% |
| **Deadline** | **Sunday 15 November, 23:59 China Standard Time**, on GAP (briefing and studio in periods 9 and 10 of Day 2; finish over the weekend) |
| **Before you start** | [Visualising and communicating data](../D2_lecture_visual_communication.md) (Parts 1, 5 and 6) and [Tableau concepts and dashboards](../D2_lecture_tableau_dashboards.md), Part 10, which practises reading a box plot and a regression line |

The data has one row per **restaurant bill** (a transaction): `total_bill` and `tip` in **US dollars**, the server's `sex`, whether the party included a `smoker`, the `day` (`Thur`, `Fri`, `Sat`, `Sun`), the `time` (`Lunch` or `Dinner`) and the party `size` (number of diners).

---

## 2. Route A: Try JupyterLab (as on GAP)

### Part 1: Open and name a notebook

Open Try JupyterLab, start a **Python (Pyodide)** notebook and rename it `YourLastName_DATA300_Assignment1.ipynb`.

### Part 2: Run the script

Paste GAP's whole script into the first cell and press **Shift + Enter**. In outline, it:

1. installs seaborn, pandas and matplotlib with `%pip`, and loads `tips.csv` from GitHub with `open_url`;
2. prints **Table 1**: the mean bill, mean tip and mean party size for each day;
3. prints **Table 2**: the total of all bills for each shift (Lunch and Dinner);
4. draws **Figure 1**: a bar chart of total bills by day;
5. draws **Figure 2**: a box plot of tips for each shift;
6. draws **Figure 3**: a scatter plot of tip against bill, with a fitted (OLS) regression line and a shaded band.

Check that both tables and all three figures appear before you start writing.

### Part 3: Write the report

Write the report in Word (or Markdown) using GAP's **four headings exactly**; see *How to write the report* below. Use paragraphs, except for the two recommendations, which are bullet points.

### Part 4: Export

Run the notebook from the top, then **File → Print → Save as PDF** with *Background graphics* ticked, named `YourLastName_Jupyter.pdf`. Save the report as `YourLastName_Report.pdf`. See *Submission* below.

### How to write the report

**The four headings, exactly as GAP gives them, in this order:** `1. Executive Summary`, `2. Descriptive Data Overview`, `3. Visual Insights & Graphical Trends`, `4. Strategic Business Recommendations`. What goes under each:

1. **Executive Summary**: one paragraph. The client's objective, who you are (Bistro Analytics), the data analysed (the tips dataset and its number of transactions; check the count with `len(df)`), and the two operational goals: scheduling staff for peak demand, and growing revenue while keeping good servers. Lead with your main finding and what you recommend, in one or two sentences (the finding-first rule from the morning lecture).
2. **Descriptive Data Overview**: one or two paragraphs. From **Table 1**, which day has the highest average bill and which the highest average tip, with the values. From **Table 2**, total revenue for Lunch and for Dinner and how far apart they are.
3. **Visual Insights & Graphical Trends**: two or three paragraphs, one per figure. **Figure 1**: compare the weekday days in the data with the weekend days and name the peak days. **Figure 2**: compare the medians and interquartile ranges of tips at Lunch and Dinner, discuss what that means for a server's earnings, and comment on the points beyond the upper whiskers. **Figure 3**: describe the slope and direction of the regression line and what it suggests for upselling.
4. **Strategic Business Recommendations**: two detailed bullet points. **Recommendation 1 (staffing):** which days and shifts should get the strongest servers, and why. **Recommendation 2 (upselling and training):** a concrete programme justified by the bill-to-tip relationship, explaining how a higher bill benefits both the restaurant and the server.

**Evidence and numbers.** Every claim should point to a table or figure and carry a number with its unit:

| Weak | Strong |
|---|---|
| "[Day] is busy." | "Figure 1 shows bills on [day] totalling about $X, the [highest / second highest] of the four days and roughly Y times [another day]'s." |
| "[Shift] tips are better." | "The median tip at [shift] (about $X, Figure 2) is about $Y [higher / lower] than at [the other shift], and its box is [taller / shorter], so tips there are [more / less] variable." |
| "Tips go up with the bill." | "Figure 3's line rises by about $X in tip for every $10 added to the bill." |

The brackets, X and Y are placeholders: fill them from your own output, and only with what it shows. Write money as US dollars (`$` or "US dollars"), say "mean" or "median" rather than "average" when it matters, and round sensibly (to the cent for means, to the dollar for totals).

**Reading the box plot (Figure 2).** The line inside each box is the **median** tip; the box covers the middle half of the tips (the **interquartile range**, from the 25th to the 75th percentile); the whiskers reach the furthest tips within 1.5 × IQR of the box; dots beyond them are **outliers**: unusually large tips, not errors. Compare the medians (typical tip), the box heights (how predictable tips are) and the outliers (occasional large tips), and say what each means for a server choosing shifts. The box plot shows **tip amounts per bill**, not total tips per shift: a shift with more bills can earn a server more in total even with similar typical tips.

**Reading the regression line (Figure 3).** The slope is the average change in **tip (US dollars)** for each **one-dollar** increase in the bill. To read it from the chart, take two points on the line far apart, divide the rise in tip by the rise in bill, and state it in words ("about $X more tip for each extra $10 of bill"). Then: say over what range of bills it holds (do not extrapolate far beyond the data); say how widely the points scatter around the line; and remember it is an **association**: larger bills go with larger tips, but larger parties, longer meals and the day also differ between bills. The shaded band is the uncertainty of the **line**, not a range for individual tips. Route B below can print the slope for you.

**Recommendations that are actionable.** Each one says **who** does **what**, **when**, **why** (citing your evidence) and **how you would know it worked** (a metric to watch, such as average bill per table or tip per server shift). Keep them within what the data shows; for example, the data does not include staff costs or how many servers worked each shift, so say so if it limits the advice.

---

## 3. Route B: offline in Anaconda JupyterLab

Use this route if Try JupyterLab cannot load the data, or if you prefer your own laptop. It produces the same two tables and three figures from the bundled copy of the data, with nothing installed or downloaded. Create a notebook **inside the `DATA300_GAP` folder** (next to `data`), named as in Route A, and paste the block into one cell (or split it at the `# ---` lines).

```{.python .offline}
# Route B for Assignment 1: run offline in Anaconda JupyterLab.
# The tips file comes from the course folder, so nothing is installed or downloaded.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/tips.csv")

# Put days and shifts in calendar order (GAP's version lists the days alphabetically;
# the numbers are the same, only the order differs)
df["day"] = pd.Categorical(df["day"], categories=["Thur", "Fri", "Sat", "Sun"], ordered=True)
df["time"] = pd.Categorical(df["time"], categories=["Lunch", "Dinner"], ordered=True)
print("Transactions in the data:", len(df))

# --- Table 1: average transaction metrics by day of week
day_summary = df.groupby("day", observed=True)[["total_bill", "tip", "size"]].mean().round(2)
day_summary.columns = ["Avg Total Bill ($)", "Avg Tip ($)", "Avg Party Size"]
print("\n--- Table 1: Average Transaction Metrics by Day ---")
print(day_summary)

# --- Table 2: total revenue by meal shift
time_summary = df.groupby("time", observed=True)[["total_bill"]].sum().round(2)
time_summary.columns = ["Total Revenue ($)"]
print("\n--- Table 2: Aggregate Revenue Breakdown by Meal Shift ---")
print(time_summary)

sns.set_theme(style="whitegrid")

# --- Figure 1: total revenue by day (one colour, works on any seaborn version)
rev_by_day = df.groupby("day", observed=True)["total_bill"].sum().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(data=rev_by_day, x="day", y="total_bill", color="#66c2a5")
plt.title("Figure 1: Total Gross Revenue Generated by Day of Week", fontsize=14, fontweight="bold")
plt.xlabel("Day of Week")
plt.ylabel("Total Revenue ($)")
plt.tight_layout()
plt.show()

# --- Figure 2: tip distribution for each shift
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="time", y="tip", color="#a1c9f4")
plt.title("Figure 2: Distribution of Server Tip Amounts: Lunch vs. Dinner", fontsize=14, fontweight="bold")
plt.xlabel("Meal Shift")
plt.ylabel("Tip Amount ($)")
plt.tight_layout()
plt.show()

# --- Figure 3: tip against bill with a fitted regression line
plt.figure(figsize=(9, 6))
sns.regplot(data=df, x="total_bill", y="tip", seed=0,
            scatter_kws={"alpha": 0.6}, line_kws={"color": "red", "linewidth": 2})
plt.title("Figure 3: Linear Relationship: Total Bill Size vs. Tip Amount", fontsize=14, fontweight="bold")
plt.xlabel("Total Bill Amount ($)")
plt.ylabel("Tip Amount ($)")
plt.tight_layout()
plt.show()

# --- Optional: the numbers behind Figure 3's line, for your report
slope, intercept = np.polyfit(df["total_bill"], df["tip"], 1)
r = df["total_bill"].corr(df["tip"])
print(f"Fitted line: tip = {intercept:.2f} + {slope:.3f} x total_bill   (US dollars)")
print(f"Correlation between bill and tip: r = {r:.2f}")
print(f"Bills in the data range from ${df['total_bill'].min():.2f} to ${df['total_bill'].max():.2f}")
```

In JupyterLab you may replace `print(day_summary)` and `print(time_summary)` with `display(...)` for nicer tables. Export with **Kernel → Restart Kernel and Run All Cells**, then **File → Print → Save as PDF**.

---

## 4. Checks you can make

These tell you whether your output and report are complete without giving any answers away.

- [ ] Table 1 has **four rows** (Thur, Fri, Sat, Sun) and **three columns**; money columns are in US dollars, party size in diners.
- [ ] Table 2 has **two rows** (Lunch and Dinner); the two totals add up to the sum of all bills, `df["total_bill"].sum()`.
- [ ] Figure 1 has four bars; Figure 2 has two boxes; Figure 3 has one rising or falling line through a cloud of points, with a shaded band.
- [ ] The report has the **four headings exactly** as GAP words them, in order, with paragraphs (and bullets only for the recommendations).
- [ ] Every number in the report can be found in, or read from, a table or figure, and carries a unit.
- [ ] Section 3 mentions medians, the IQR and outliers for Figure 2, and the slope in "dollars of tip per dollar (or per $10) of bill" for Figure 3.
- [ ] Each recommendation names specific days and shifts or a specific programme, cites evidence, and says how success would be measured.
- [ ] The PDF has the report first, then the executed notebook.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| The cell hangs or ends with a network error | GitHub is slow or blocked | Drag `tips.csv` from the course folder into Try JupyterLab's file browser and replace the `open_url` line with `df = pd.read_csv("tips.csv")`, or switch to Route B |
| `ModuleNotFoundError: No module named 'seaborn'` in Try JupyterLab | The `%pip install` line did not run in this session | Run the cell again from the top; every new Try JupyterLab session needs it |
| `ModuleNotFoundError: No module named 'pyodide'` in Anaconda | GAP's browser-only code was pasted into Route B | Use the Route B code above |
| `FileNotFoundError: data/tips.csv` | The notebook is not in the `DATA300_GAP` folder | Save the notebook inside `DATA300_GAP`, next to `data`, and run again |
| `AttributeError: Rectangle.set() got an unexpected keyword argument 'legend'` (Figure 1) or `TypeError: ... unexpected keyword argument 'legend'` (Figure 2) | GAP's code uses `hue=...` with `legend=False`, which needs **seaborn 0.13 or later**; older Anaconda installs may have 0.12 | Check with `print(sns.__version__)`. On an older version, remove `hue=...`, `legend=False` and `palette=...` from those two calls and add `color="#66c2a5"`, as Route B does |
| `NameError: name 'display' is not defined` | `display()` exists only inside Jupyter | Run the code in JupyterLab, or use `print()` as Route B does |
| The days appear as Fri, Sat, Sun, Thur | The data is read as text, which pandas sorts alphabetically | The values are still correct. Write about them in calendar order, or use Route B, which sets the order Thur, Fri, Sat, Sun |
| Unsure which days are "weekdays" | The data has only four days, and the label for Thursday is `Thur` | Thursday and Friday are the weekdays in the data; Saturday and Sunday the weekend. There is no Monday to Wednesday |
| Unsure what "revenue" means here | GAP calls the sum of `total_bill` "revenue" | Use GAP's term but say once that it is the total of bills in US dollars (tips are recorded separately in `tip`) |
| The regression slope is not printed anywhere | GAP's script only draws the line | Read it from the chart (rise ÷ run between two points on the line), or run Route B's optional last part |
| The report heading is "Executive summary" or "Recommendations" | Headings paraphrased | Copy GAP's four headings word for word, including the number and the "&" in section 3 |
| Figures missing or grey in the PDF | *Background graphics* off, or cells not run before printing | Tick *Background graphics*; restart and run all, then print |
| Online PDF merger is blocked or slow | — | Combine the PDFs **offline**: see [Combining PDFs without internet](../setup.md#combining-pdfs-without-internet) |

---

## 6. Beyond the assignment

Optional, not graded. Try these after you have written your report:

1. Count the bills for each day and shift with `pd.crosstab(df["day"], df["time"])`. Which day–shift combinations exist in the data, and what does that mean for comparing Lunch with Dinner?
2. Compute the **tip rate** two ways: `df["tip"].sum() / df["total_bill"].sum()` (ratio of sums) and `(df["tip"] / df["total_bill"]).mean()` (mean of ratios). Why do they differ (morning lecture, Part 6)?
3. Draw Figure 3 again with `hue="size"` or with `col="time"` in `sns.lmplot`. Does the bill-to-tip relationship look the same for small and large parties?
4. Make Figure 1 show the **mean bill per transaction** instead of the total. Which chart better supports a staffing decision, and which an upselling decision?
5. Rewrite each figure's title as a message title that states your finding.

---

## 7. Submission

| File | Contents |
|---|---|
| Report | Your four-section report, saved as `YourLastName_Report.pdf` |
| Notebook | The executed notebook with both tables and all three figures visible, saved as `YourLastName_Jupyter.pdf` |
| **Final file** | The two combined, **report first**, named `YourLastName_DATA300_Assignment1.pdf` |

1. Restart and run the notebook from the top; check that both tables and all three figures appear.
2. Export it with **File → Print → Save as PDF**, *Background graphics* ticked (or **File → Save and Export Notebook As → HTML**, then print the HTML to PDF).
3. Combine the report and the notebook PDF **offline**, report first ([Combining PDFs without internet](../setup.md#combining-pdfs-without-internet)).
4. Open the final PDF and check both parts are complete and readable.
5. Upload it to **Assignment 1** on **GAP** and submit before **Sunday 15 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)).
