# Lab 7: Business intelligence case

<p class="lead">
Your second Excel lab of Day 6, and a dry run for the capstone. For the car maker of Lab 6, you forecast a quarterly battery cost four quarters ahead with Excel's Forecast Sheet, link the forecast's worst-case bound into a small dashboard that compares three sourcing strategies, and write a managerial report that weighs the financial and the ethical evidence. You submit the workbook and the report on GAP.
</p>

*Adapted from the DATA 300 GAP course, In-Class Module 2, Lab 7: BI Case Study Implementation. Written in our own words; follow GAP for the official wording and figures.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Enter 12 quarters of battery cost, build a Forecast Sheet to the end of 2026, build a *Case Study Dashboard* that uses the forecast's upper confidence bound, and answer five questions in a formal report |
| **Why** | **EcoDrive Motors (phase 2):** battery costs have swung with lithium and cobalt shortages, and the finance director wants to know where they are heading before committing to the ethical sourcing premium. The lab combines a predictive model with a multi-strategy comparison, which is what a BI case does |
| **CLOs** | CLO 4 (time series forecasting to project outcomes), CLO 5 (evaluating BI tools in a case, with a managerial report that considers ethical and societal context) |
| **Weight** | 2% |
| **Deadline** | **Wednesday 18 November, 23:59 China Standard Time**, on GAP (worked on in periods 9 and 10 of Day 6) |
| **Before you start** | [BI strategy, forecasting and ethics](../D6_lecture_bi_strategy_ethics.md), Parts 5, 6, 7, 12, 14 and 15 |

You need **desktop Excel 2016 or later** (Windows) or a recent Excel for Mac: Forecast Sheet is not in older versions or in Excel on the web. All money is in **US dollars**, as on GAP.

---

## 2. Route A: Excel (as on GAP, with one fix)

### Part 1: Time series forecasting

1. Open a blank workbook and save it with GAP's file name (your last name, the course code and "Lab7", as `.xlsx`). Rename *Sheet1* to **Historical Data**.
2. Type GAP's two headers in **A1:B1** and GAP's 12 quarters in **A2:B13**: the labels **Q1-2023 to Q4-2025** in column A and the battery cost per vehicle in column B. Format column B as currency.
3. **The fix: add a numeric timeline.** Forecast Sheet needs a timeline of **numbers or dates** at a constant step; labels such as `Q1-2023` are text, so Excel cannot use them. Right-click the column **B** header → **Insert**, so the costs move to column C. In **B1** type *Period* and in **B2:B13** type **1 to 12**. (Alternatively, type one real date per quarter, three months apart, such as the last day of each quarter; period numbers are the safer choice.) Keep the labels in column A for your report.
4. Select **B1:C13**: the period numbers and the costs, side by side, with their headers.
5. **Data → Forecast Sheet** (in the *Forecast* group). A preview window opens.
6. Choose the **line** chart. Set **Forecast End** to **16**: period 16 is **Q4-2026**, four quarters after the last actual quarter (period 12). If you used dates, set the date of Q4-2026 instead.
7. Click **Options** and check: *Forecast Start* at the last actual period; *Confidence Interval* **95%**; *Seasonality* **Detect Automatically** (as GAP intends); *Timeline Range* `$B$2:$B$13`; *Values Range* `$C$2:$C$13`. Ticking *Include forecast statistics* is optional and useful.
8. Click **Create**, and rename the new sheet **Predictive Forecast**.

### Where the Upper Confidence Bound is

The new sheet has a table with five columns: **Timeline**, the **values**, **Forecast**, **Lower Confidence Bound** and **Upper Confidence Bound**. The history fills the first rows; the forecast rows for periods 13 to 16 follow. On the **last actual** row (period 12), Excel copies the actual cost into the three forecast columns so the chart's lines meet; that row is not a forecast.

The cell you need is in the **Upper Confidence Bound** column, on the row whose timeline value is **16** (Q4-2026), which is the **last row** of the table. With Excel's usual layout that is **E17**, but check rather than assume: click the cell and read the formula bar. It should add a `FORECAST.ETS.CONFINT(...)` term to the forecast, and refer to the timeline cell holding 16.

### Part 2: The case study dashboard

1. Add a sheet and rename it **Case Study Dashboard**.
2. Type GAP's four constants with their labels in **A1:B4** (expected demand, sale price, non-battery manufacturing cost, fixed overhead).
3. In **A6** type GAP's label for the projected battery cost. In **B6** type `=`, click the **Predictive Forecast** tab, click the Upper Confidence Bound cell for period 16, and press **Enter**. B6 now shows that bound and updates if the forecast changes.
4. Build GAP's comparison table from row 8: the three strategy names in **B8:D8**; GAP's ethical premium for each in **B9:D9**; total variable cost per vehicle in **B10:D10** (non-battery cost + projected battery cost + premium, with `$` on the shared cells); and projected net profit in **B11:D11** (demand × price − demand × total variable cost − overhead). Format rows 9 to 11 as currency.

### Part 3: The managerial report

Write a formal report in Word, in sections that follow GAP's five questions. In outline:

1. **Trend:** describe the historical trend from your forecast sheet and give the **baseline** forecast for Q4-2026.
2. **Confidence intervals:** explain, in your own words, what the lower and upper bounds represent, and why the dashboard uses the **upper** bound rather than the baseline.
3. **Financial impact of ethics:** the projected net profit of strategy 1 and strategy 3 under the worst-case battery cost.
4. **Recommendation:** one or two paragraphs recommending one of the three strategies, balancing the numbers against brand reputation, human rights and corporate responsibility.
5. **The value of BI:** why a forecast combined with a multi-strategy dashboard beats looking at last year's costs.

Quote numbers from **your** workbook, with units, and say which sheet and cell each comes from.

---

## 3. Route B: a Python cross-check (offline)

The graded product is an Excel workbook, so there is no Python route that replaces it. The block below **mirrors** Part 1 with statsmodels, so you can check that Excel's forecast is sensible, and recomputes the dashboard from a bound. Run it in Anaconda JupyterLab from the `DATA300_GAP` folder (it reads no files).

Excel's Forecast Sheet fits the **AAA** version of exponential smoothing (additive error, trend and seasonality) and decides by itself whether there is a 4-quarter season. statsmodels fits the same family of models, but its starting values and optimiser differ from Excel's, so **expect close, not identical, numbers**. With only three years of data, the choice of season matters, so the block fits both versions. In Excel, `=FORECAST.ETS.SEASONALITY(C2:C13, B2:B13)` on the *Historical Data* sheet tells you which one Excel chose (4 means a quarterly season, 0 means none); compare with the matching Python version. **In your report, quote Excel's numbers.**

```{.python .offline}
# Route B cross-check for Lab 7: an exponential-smoothing mirror of Excel's Forecast Sheet.
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.exponential_smoothing.ets import ETSModel

# --- Part 1: GAP's 12 quarters, with a numeric timeline (periods 1-12)
quarters = [f"Q{q}-{y}" for y in (2023, 2024, 2025) for q in (1, 2, 3, 4)]
cost = [7500, 7650, 7900, 8100, 8000, 8350, 8600, 8900, 8800, 9200, 9550, 9800]
history = pd.DataFrame({"quarter": quarters, "period": range(1, 13), "battery_cost": cost})
y = pd.Series(history["battery_cost"].to_numpy(dtype=float))
horizon = 4                                   # periods 13-16 = Q1-2026 to Q4-2026

for label, seasonal in [("No season (trend only)", None), ("Quarterly season (AAA)", "add")]:
    periods = 4 if seasonal else None
    # Point forecast with Holt-Winters exponential smoothing
    hw = ExponentialSmoothing(y, trend="add", seasonal=seasonal, seasonal_periods=periods).fit()
    # 95% interval from the equivalent state-space ETS model (additive errors, as in Excel)
    ets = ETSModel(y, error="add", trend="add", seasonal=seasonal, seasonal_periods=periods).fit(disp=False)
    bounds = ets.get_prediction(start=len(y), end=len(y) + horizon - 1).summary_frame(alpha=0.05)
    out = pd.DataFrame({
        "period": range(13, 13 + horizon),
        "quarter": ["Q1-2026", "Q2-2026", "Q3-2026", "Q4-2026"],
        "forecast (Holt-Winters)": hw.forecast(horizon).to_numpy(),
        "forecast (ETS)": bounds["mean"].to_numpy(),
        "lower 95%": bounds["pi_lower"].to_numpy(),
        "upper 95%": bounds["pi_upper"].to_numpy(),
    })
    print(f"\n{label}")
    print(out.round(0).to_string(index=False))

# --- Part 2: the dashboard, from a battery-cost bound
# Type the Upper Confidence Bound for period 16 from YOUR Excel Predictive Forecast sheet here:
projected_battery = float(out["upper 95%"].iloc[-1])      # placeholder: the last Python version's bound
demand, price, non_battery, overhead = 15_000, 35_000, 18_000, 50_000_000
premiums = {"1. Profit-maximised (no ethics)": 0, "2. Hybrid sourcing (50% ethical)": 250,
            "3. Fully ethical (100% certified)": 500}
dash = pd.DataFrame({"ethical premium": premiums})
dash["total variable cost"] = non_battery + projected_battery + dash["ethical premium"]
dash["projected net profit"] = demand * price - demand * dash["total variable cost"] - overhead
print(f"\nProjected battery cost used: ${projected_battery:,.0f}")
print(dash.round(0).to_string())
```

Replace the `projected_battery` line with **your Excel bound** to check your dashboard's three profits to the dollar.

---

## 4. Checks you can make

These tell you whether your work is right without giving any answers away.

- [ ] *Historical Data* has **12** quarters, Q1-2023 to Q4-2025, with period numbers 1 to 12 (or evenly spaced dates) in the column next to the costs.
- [ ] The forecast table on *Predictive Forecast* ends at period **16**, and has **four** forecast rows after the last actual row.
- [ ] On every forecast row, Lower < Forecast < Upper, and the gap between the bounds **widens** from period 13 to period 16.
- [ ] Your forecast continues the direction of the history; if it looks flat or bends sharply, check the timeline and the seasonality setting.
- [ ] `FORECAST.ETS.SEASONALITY` tells you whether Excel used a season, and your report says which.
- [ ] Your forecast and bounds are **close** to the matching Route B version (within a few per cent), but not necessarily identical.
- [ ] *Case Study Dashboard* **B6** is a **link** (its formula starts with `='Predictive Forecast'!`), not a typed number, and it shows the period-16 upper bound.
- [ ] Rows 10 and 11 use `$` on the shared cells, so all three strategies use the same demand, price, costs and battery cost; only the premium differs.
- [ ] The three net profits differ by exactly **demand × the difference in premium**. If not, a formula points at the wrong cell.
- [ ] Your report quotes **Excel's** numbers, and your question 2 answer explains the bounds for this cost and this company, not only in general.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| Excel refuses the timeline, or the Forecast Sheet preview looks wrong | The timeline is the text labels `Q1-2023` … `Q4-2025` | Add a **Period** column with 1 to 12 (Part 1, step 3) and select it with the costs |
| Excel complains about the timeline even with dates | Dates not evenly spaced, a blank, or dates stored as text | Use period numbers, or type real dates three months apart; check they are right-aligned (numbers), not left-aligned (text) |
| The forecast stops before Q4-2026 | Forecast End left at its default | Set **Forecast End = 16** (or the Q4-2026 date) |
| Forecast Sheet treats the costs as the timeline | The columns were selected in the wrong order, or the labels were included | Select the period column and the cost column only, with the period on the **left** |
| The Forecast Sheet button is greyed out | No cell in the data selected, or Excel too old | Click inside the data; use desktop Excel 2016 or later |
| **B6** shows the forecast, not the bound | The link points at the *Forecast* column | Point it at the **Upper Confidence Bound** column on the period-16 row |
| **B6** shows a value from period 12 | The link points at the last **actual** row, where Excel copies the actual value into the bound columns | Use the **last row** of the table (period 16) |
| **B6** shows 0 or `#REF!` | The link points at an empty cell, or the forecast sheet was deleted and re-created | Re-create the link by typing `=` and clicking the bound for period 16 |
| All three strategies show the same profit | Row 10 adds the same premium cell to every strategy (missing column change) | Each column must add **its own** premium (B9, C9, D9); the other cells are absolute (`$B$3`, `$B$6`) |
| Profits change when you copy the formula along the row | Missing `$` on the constants | Use `$B$1`, `$B$2`, `$B$4` and `$B$3`, `$B$6` as GAP shows |
| Your numbers differ slightly from the Route B mirror | Excel and statsmodels fit ETS differently | Expected. Compare with the Route B version that matches Excel's seasonality, and quote Excel |
| A classmate's forecast differs from yours | Different seasonality setting, confidence level or a typing slip in the 12 costs | Compare the Options settings and the data cell by cell |
| Your recommendation lists ethical points without numbers | Question 4 asks you to **balance** the data against societal impacts | State the profit difference between strategies in plain units (per year, per vehicle), then the ethical evidence; Day 6, Part 14 |

---

## 6. Beyond the lab

Optional, not graded. Do these in a **copy** of your workbook.

1. **Another confidence level.** Rebuild the forecast at 80% and at 99%. How does the period-16 bound move? What would make a company plan at 99%?
2. **The bound as a percentile.** Using Day 6, Part 7, say which percentile the upper bound of a 95% interval is. Which percentile would suit a company for which a cost overrun is four times as costly as an underrun? Build it with `FORECAST.ETS` and `FORECAST.ETS.CONFINT`.
3. **Force the season.** Set *Seasonality* manually to 4 (or to 0, whichever Excel did not choose) and compare the forecast. With only three years of data, which would you trust, and why?
4. **A sensitivity table.** On the dashboard, build a one-way Data Table of the three profits for battery costs from the lower to the upper bound (its input cell must be on the dashboard sheet, so use **B6**'s value in a driver cell).
5. **Profit per vehicle.** Add a row showing each strategy's profit per vehicle and the ethical premium as a share of it.
6. **One page for the board.** Turn your report into a one-page memo in the structure of Day 6, Part 14.

---

## 7. Submission

| File | Contents |
|---|---|
| Workbook | *Historical Data*, *Predictive Forecast* and *Case Study Dashboard*, saved with GAP's file name (`YourLastName_DATA300_Lab7.xlsx`) |
| Report | Your formal managerial report from Word, saved as `YourLastName_Lab7_Report.pdf` |

1. Check that B6 is linked to the period-16 upper bound and that the dashboard's three profits use it.
2. Save the workbook as `.xlsx`.
3. Save the report with **File → Save As → PDF**. Paste the forecast chart into the report as a picture if it helps your argument, so you still submit one PDF ([Combining PDFs without internet](../setup.md#combining-pdfs-without-internet)).
4. Upload **both files** to **Applied Lab 7** on **GAP** and submit before **Wednesday 18 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)).
