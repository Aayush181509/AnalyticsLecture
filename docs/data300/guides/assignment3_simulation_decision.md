# Assignment 3: Simulation decision model

<p class="lead">
Your graded spreadsheet simulation. For a company launching a new smart thermostat, you simulate twelve months of demand with random market volatility in Excel, compare two marketing strategies month by month, freeze the simulation, chart the two monthly profit lines in Tableau, and write a short executive report on which strategy to choose and why simulation is safer than a single fixed forecast.
</p>

*Adapted from the DATA 300 GAP course, In-Class Module 2, Assignment 3: Spreadsheet Simulation and Decision Model. Written in our own words; follow GAP for the official wording and figures.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Build a 12-month simulation table in Excel with `RANDBETWEEN`, lock it with Paste Special → Values, build a two-line profit chart in Tableau, and write a report answering two questions with the chart included |
| **Why** | You are an analytics planner at **SmartHome Tech**. Earlier data mining gave a baseline monthly demand, a range of random monthly swings and a fixed profit margin per unit. The company must choose between a **standard** and an **aggressive** marketing strategy, which differ in fixed monthly cost and in how much they lift demand. The assignment practises building a decision model under uncertainty, moving frozen results into a visual tool, and recommending a strategy from the evidence |
| **CLOs** | CLO 3 (computational problem-solving applied to a business scenario), CLO 4 (a predictive simulation model that projects outcomes), CLO 5 (evaluating what the results mean for a strategic decision) |
| **Weight** | 6% |
| **Deadline** | **Sunday 22 November, 23:59 China Standard Time**, on GAP (briefed in period 6 of Day 6; support in periods 7 and 8 of Day 7) |
| **Before you start** | [Simulation under uncertainty](../D5_lecture_simulation_uncertainty.md), Parts 2, 6, 7, 8, 10 and 13; [Tableau concepts and dashboards](../D2_lecture_tableau_dashboards.md); and [BI strategy, forecasting and ethics](../D6_lecture_bi_strategy_ethics.md), Parts 14 and 16 |

Use GAP's figures for the baseline, the volatility range, the margin, the two marketing costs and the demand multiplier. All money is in **US dollars**, as on GAP.

---

## 2. Route A: Excel and Tableau (as on GAP)

### Part 1: The simulation in Excel

1. Open a blank workbook and save it with GAP's file name (your last name, the course code and "Assignment3", as `.xlsx`).
2. **Headers.** Type GAP's seven headers in **A1:G1**: month, baseline demand, market volatility, standard demand, aggressive demand, standard profit and aggressive profit, spelt exactly as GAP gives them (with underscores).
3. **Month and baseline.** Type 1 to 12 in **A2:A13**, and GAP's baseline demand in every cell of **B2:B13**.
4. **Volatility.** In **C2** type GAP's `RANDBETWEEN` formula, with GAP's lower and upper limits, and fill it down to **C13**. `RANDBETWEEN` returns a whole number, and both limits can occur (Day 5, Part 7).
5. **Demand.** In **D2**, standard demand is baseline plus volatility. In **E2**, aggressive demand is GAP's formula: the same demand times GAP's multiplier, rounded to a whole unit with `ROUND(…, 0)`. Fill both down to row 13.
6. **Profit.** In **F2** and **G2**, type GAP's two profit formulas: demand × the margin per unit, minus that strategy's fixed monthly marketing cost. Fill both down to row 13.
7. Press **F9** a few times (Mac: **Fn + F9** or **Cmd + =**) and watch every month change.

### Part 2: Lock the simulation

`RANDBETWEEN` recalculates whenever the workbook changes or opens, so the numbers you write about would no longer be the numbers in the file (Chapter 7, section 7.3; Day 5, Part 8).

1. Select **A1:G13** and copy (**Ctrl + C**, Mac **Cmd + C**).
2. With the selection still in place, right-click **A1** → **Paste Special → Values** (the clipboard icon marked **123**). On Windows, **Ctrl + Alt + V**, then **V**, then **Enter** does the same.
3. Click any cell in C2:G13: the formula bar should now show a **number**, not a formula. Press F9: nothing should change.
4. **Save** and **close Excel** before you open Tableau.

### Part 3: The Tableau view

1. Open Tableau Desktop. Under **Connect**, choose **Microsoft Excel** and open your saved workbook.
2. On the data-source page, the Excel sheet (*Sheet1*) should appear on the canvas. If it does not, drag it there. Then click the **Sheet 1** tab at the bottom to open a worksheet.
3. Drag **Month** to the **Columns** shelf. Tableau treats it as a measure (a green `SUM(Month)` pill). Right-click the pill and choose **Dimension**, so each month becomes its own position on the axis.
4. Drag **Measure Values** (at the bottom of the Data pane) to the **Rows** shelf.
5. A **Measure Values** card appears below the Marks card, listing every numeric field. Remove every entry except the **standard profit** and **aggressive profit** sums (drag each other pill off the card, or right-click → **Remove**). Tableau may show the field names with spaces instead of underscores.
6. On the **Marks** card, change *Automatic* to **Line**.
7. Drag **Measure Names** onto **Color** on the Marks card, so each strategy has its own colour and a legend appears.
8. **Worksheet → Export → Image…**, save it as PNG or JPEG, and insert it into a blank Word document.

### Part 4: The executive report

In the Word document with your chart, write a short executive report answering GAP's two questions:

1. **Strategic decision:** from **your** chart, which strategy gives the higher and more consistent profit over the twelve months; and, in **your** simulation, whether there were any months in which the aggressive strategy did worse than the standard one because of its higher fixed cost in a weak month. Answer from your own frozen data; check any month you mention against the Excel table.
2. **The value of simulation:** from a manager's point of view, why putting random volatility into the forecast is safer for planning than assuming exactly the baseline demand every month.

Write for a manager: lead with your answer, give numbers with units and the month they come from, and keep the evidence and your judgement separate (Day 6, Part 14).

---

## 3. Route B: a Python mirror (offline)

The graded products are an Excel workbook and a Tableau chart, so there is no Python route that replaces them. The block below **mirrors** Part 1 in numpy, so you can check that your columns follow the right rules, and draws the two profit lines as a preview of the Tableau view. Run it in Anaconda JupyterLab from the `DATA300_GAP` folder (it reads no files).

Your Excel numbers **will differ** from these: `RANDBETWEEN` has no seed, while the mirror uses a fixed one so it prints the same months every run. Change the seed to see other possible years. Answer the report questions from **your Excel** simulation, not from this mirror.

```{.python .offline}
# Route B mirror for Assignment 3: GAP's simulation in numpy, plus a preview chart.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# GAP's inputs (money in US dollars)
baseline = 1000                     # units per month
swing = 150                         # RANDBETWEEN(-150, 150)
margin = 100                        # profit per unit
cost_standard, cost_aggressive = 10_000, 25_000      # fixed marketing per month
multiplier = 1.4                    # aggressive demand lift

rng = np.random.default_rng(2026)   # Excel has no seed; change this number to see another year
sim = pd.DataFrame({"Month": np.arange(1, 13), "Baseline_Demand": baseline})
sim["Market_Volatility"] = rng.integers(-swing, swing + 1, size=12)   # +1: integers() excludes its top
sim["Standard_Demand"] = sim["Baseline_Demand"] + sim["Market_Volatility"]
# Excel's ROUND rounds halves away from zero and numpy rounds halves to even;
# here 1.4 x a whole number never ends in exactly .5, so the two agree.
sim["Aggressive_Demand"] = np.round(sim["Standard_Demand"] * multiplier).astype(int)
sim["Standard_Profit"] = sim["Standard_Demand"] * margin - cost_standard
sim["Aggressive_Profit"] = sim["Aggressive_Demand"] * margin - cost_aggressive
print(sim.to_string(index=False))

# Rule checks: the same checks as section 4 of the guide
assert sim["Market_Volatility"].between(-swing, swing).all()
assert (sim["Standard_Demand"] - sim["Baseline_Demand"]).between(-swing, swing).all()
assert sim["Aggressive_Demand"].dtype.kind == "i"     # whole units, as Excel's ROUND gives
print("\nAll rule checks passed.")

# Preview of the Tableau view: Month as a dimension, two measures, line marks, colour by measure
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(sim["Month"], sim["Standard_Profit"], marker="o", color="#0072B2", label="Standard_Profit")
ax.plot(sim["Month"], sim["Aggressive_Profit"], marker="o", color="#D55E00", label="Aggressive_Profit")
ax.set_xticks(sim["Month"])
ax.set_xlabel("Month")
ax.set_ylabel("Profit (US dollars)")
ax.set_title("Simulated monthly profit by strategy (one possible year)")
ax.legend(frameon=False)
plt.show()

# To open this mirror in Tableau for practice, save it (needs openpyxl, included in Anaconda):
# sim.to_excel("Assignment3_python_practice.xlsx", index=False)
```

---

## 4. Checks you can make

These tell you whether your work is right without giving any answers away.

- [ ] Row 1 holds GAP's seven headers, spelt as GAP gives them, and rows 2 to 13 hold months 1 to 12.
- [ ] Every baseline cell holds GAP's baseline, and every volatility value is a **whole number** within GAP's limits.
- [ ] Standard demand = baseline + volatility in every row.
- [ ] Aggressive demand = standard demand × GAP's multiplier, **rounded to a whole number**, in every row.
- [ ] Each profit = that row's demand × the margin − that strategy's fixed cost. Check one row by hand.
- [ ] After Paste Special, clicking any cell in C2:G13 shows a **number** in the formula bar, and F9 changes nothing.
- [ ] The workbook was saved and closed **before** you connected Tableau, and the values in your chart match the table in Excel for at least two months you checked.
- [ ] Your Tableau chart has **12** points on each line, **two** lines, and a legend naming the two profit measures, and no other measure appears on the Measure Values card.
- [ ] Every month you mention in the report can be found in your frozen Excel table.
- [ ] Your answer to question 2 is about **planning decisions** (staffing, stock, cash, budgets), not just a definition of randomness.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| The numbers in your report do not match the file you submitted | The simulation was not frozen, so it recalculated when you saved or reopened | Paste Special → Values over **A1:G13** before writing (Part 2). If it is already too late, freeze now and rewrite the numbers from the frozen table |
| Paste Special pasted formulas again, or `#REF!` appeared | **Paste** (or *Paste Special → All*) was chosen instead of **Values**, or the selection moved before pasting | Undo, select A1:G13, copy, right-click **A1** and choose **Values** (123) |
| Tableau shows one point or one bar, not twelve | **Month** is still a measure, so Tableau adds all twelve months into one `SUM(Month)` | Right-click the Month pill → **Dimension** |
| Many lines, or a line for the month or the demand columns | The Measure Values card still lists other measures | Remove every pill from the Measure Values card except the two profits |
| One line only, in one colour | **Measure Names** is not on Color | Drag **Measure Names** onto **Color** on the Marks card |
| Bars or shapes instead of lines | The mark type is *Automatic* | Choose **Line** on the Marks card |
| Tableau cannot open the workbook, or shows old values | The file was still open in Excel, or Tableau connected before you saved the frozen version | Save, close Excel, then in Tableau **Data → Refresh** (or reconnect) |
| No *Measure Values* field in the Data pane | It appears at the bottom of the Data pane, below the other fields | Scroll down the Data pane; or double-click one profit measure and then drag the other onto the same axis |
| The field names show spaces instead of underscores | Tableau tidies field names automatically | Nothing to fix: *Standard Profit* in Tableau is your `Standard_Profit` column |
| Some aggressive demands have decimals | `ROUND(…, 0)` was left out of the aggressive-demand formula | Use GAP's formula with `ROUND`, then freeze again |
| Volatility never reaches the limits | Not an error: with only 12 draws the extremes are unlikely | Leave it; `RANDBETWEEN` can return both limits |
| F9 does nothing on a Mac | The function keys control brightness or volume | **Fn + F9**, or **Cmd + =** |
| The exported image is blank or cut off | The view was exported before it finished drawing, or the window was small | Enlarge the worksheet, wait for the chart, then **Worksheet → Export → Image…** again |
| Your report's answer matches a classmate's exactly | Each simulation is different | Write from **your** chart and table; a classmate's months are not your evidence |

---

## 6. Beyond the assignment

Optional, not graded. Do these in a **copy** of your workbook, after you have frozen the graded one.

1. **Many years, not one.** Keep the formulas live in a copy and add a summary row: total annual profit for each strategy. Use a one-way Data Table with an empty input cell (Day 5, Part 9) to recalculate it 200 times, and describe the spread of each strategy's annual total.
2. **A normal swing.** Replace `RANDBETWEEN` with `NORM.INV(RAND(), 0, 75)` rounded to whole units. How does the shape of monthly demand change, and does it change your conclusion?
3. **A seasonal baseline.** Thermostats sell more before winter and summer. Replace the flat baseline with a seasonal one (for example 20% above the average in four months and 20% below in four others, with the same annual total) and describe how the monthly lines change.
4. **Uncertain lift.** Make the multiplier itself uncertain (for example between 1.1 and 1.6) and compare the risk of the two strategies (Day 5, Part 10).
5. **A dashboard.** In Tableau, add a second sheet with each strategy's monthly profit as a bar and a reference line at zero, and combine both sheets in a dashboard with a short message title.
6. **Write the recommendation.** Turn your report into a one-page memo in the structure of Day 6, Part 14, with one condition that would change your recommendation.

---

## 7. Submission

| File | Contents |
|---|---|
| Workbook | The **frozen** simulation (values, not formulas), saved with GAP's file name (`YourLastName_DATA300_Assignment3.xlsx`) |
| Report | Your executive report with the Tableau image included, saved as `YourLastName_Assignment3_Report.pdf` |

1. Check that the workbook holds values only (click a few cells in C2:G13) and that your report's numbers match it.
2. Insert the exported Tableau image into the Word document **before** saving, so the report is one PDF. If you must combine separate files, do it offline ([Combining PDFs without internet](../setup.md#combining-pdfs-without-internet)).
3. Save the report from Word with **File → Save As → PDF**.
4. Upload **both files** to **Assignment 3** on **GAP** and submit before **Sunday 22 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)).
