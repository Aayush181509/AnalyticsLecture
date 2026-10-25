# Lab 6: Spreadsheet simulation

<p class="lead">
Your first graded Excel lab. For a car maker planning a new electric vehicle, you build a deterministic profit model, a two-way What-If Data Table of profit over demand and manufacturing cost, and a 50-trial Monte Carlo simulation of demand with a risk summary. You then answer four questions about prediction, risk and the ethics of the battery supply chain, and submit the workbook and a PDF of your answers on GAP.
</p>

*Adapted from the DATA 300 GAP course, In-Class Module 2, Lab 6: Advanced Spreadsheet Simulation. Written in our own words; follow GAP for the official wording and figures.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Build three sheets in one Excel workbook (*Base Model*, *What-If Analysis*, *Risk Simulation*) from GAP's figures, then answer four questions in a Word document saved as PDF |
| **Why** | The scenario is **EcoDrive Motors**, whose launch profit is uncertain because demand and battery-material costs move. The board must also choose between a cheap battery supplier with labour violations and a certified supplier that costs more per vehicle. The lab practises turning one "best guess" into a range of outcomes, and weighing a financial result against an ethical one |
| **CLOs** | CLO 4 (spreadsheet simulation to project outcomes), CLO 5 (how analytical models support decisions, with ethical and societal context) |
| **Weight** | 2% |
| **Deadline** | **Wednesday 18 November, 23:59 China Standard Time**, on GAP (worked on in periods 7 and 8 of Day 6) |
| **Before you start** | [Simulation under uncertainty](../D5_lecture_simulation_uncertainty.md), Parts 2, 4, 7, 8, 9 and 10; and [BI strategy, forecasting and ethics](../D6_lecture_bi_strategy_ethics.md), Parts 12, 14 and 15 |

Use desktop Excel (Windows, or a recent Excel for Mac). Excel on the web cannot build Data Tables reliably. All money is in **US dollars**, as on GAP.

---

## 2. Route A: Excel (as on GAP, with two fixes)

Follow GAP's figures and formulas. The steps below summarise them and show where GAP's Data Table instructions need changing.

### Part 1: The base deterministic model

1. Open a blank workbook and save it straight away with GAP's file name (your last name, the course code and "Lab6", as `.xlsx`).
2. Rename *Sheet1* to **Base Model**.
3. Type GAP's labels in **A1:A6** and GAP's five assumptions in **B2:B6**: expected demand, sale price, base manufacturing cost, ethical sourcing premium and fixed overhead, all per GAP. Format the money cells as currency.
4. Type the three output labels in **D1:D4** and GAP's three formulas in **E2:E4**: revenue (demand × price), variable costs (demand × (base cost + premium)) and net profit (revenue − variable costs − fixed overhead). Format column E as currency.
5. **Checkpoint.** GAP gives the expected net profit in **E4**: **$47,500,000**. If yours differs, check each input and each formula before going on.

### Part 2: What-If Data Table (with the fixes)

GAP puts the table on a new sheet and points its input cells at the *Base Model* sheet. Excel does not allow that, and GAP's selection puts an empty cell in the corner. Two rules to know:

- **A Data Table's row and column input cells must be on the same sheet as the table.** Point them at another sheet and Excel stops with *Input cell reference is not valid*.
- **The formula must sit in the top-left corner of the range you select**, with the row values to its right and the column values below it. GAP's formula is in B2 but its selection starts at A2, so Excel would treat the empty A2 as the formula and B2 as one of the row values.

The fix keeps GAP's numbers and GAP's table position; only the input cells and one column move.

1. Add a sheet and rename it **What-If Analysis**.
2. **Driver cells.** In **I2** type *Demand driver* and in **J2** type GAP's expected demand. In **I3** type *Base cost driver* and in **J3** type GAP's base manufacturing cost. These are the table's input cells, on the table's own sheet.
3. **Link the base model to the drivers.** On *Base Model*, replace the typed demand in **B2** with `='What-If Analysis'!J2` and the typed base cost in **B4** with `='What-If Analysis'!J3`. The model now takes those two inputs from the drivers. Check that E4 still shows the checkpoint value.
4. **Corner formula.** On *What-If Analysis*, in **B2** type `='Base Model'!E4`, as GAP says.
5. **Row values (cost):** type GAP's five base-cost values in **C2:G2**.
6. **Column values (demand):** type GAP's five demand values in **B3:B7**, directly **below** the corner formula (GAP puts them in A3:A7; move them one column right). Type a label such as *Demand ↓ / Cost →* in **A2** if you like.
7. Select **B2:G7** (the corner formula, the five costs and the five demands, and the empty block between them).
8. **Data → What-If Analysis → Data Table…**
9. **Row input cell:** `J3` (the costs run along a row, so they replace the cost driver). **Column input cell:** `J2` (the demands run down a column, so they replace the demand driver). Click **OK**.
10. Select **C3:G7**, format as currency, then **Home → Conditional Formatting → Color Scales → Green - Yellow - Red**, so the highest profits are green and the losses red.

An alternative that also works: leave *Base Model* untouched, and in B2 write the profit formula yourself from the driver cells, for example `=J2*'Base Model'!$B$3-J2*(J3+'Base Model'!$B$5)-'Base Model'!$B$6`. Either way the table must agree with the base model at GAP's base inputs.

### Part 3: Monte Carlo risk simulation

1. Add a sheet and rename it **Risk Simulation**. Type GAP's three headers in **A1:C1**.
2. Number the trials 1 to 50 in **A2:A51**.
3. In **B2** type GAP's `RANDBETWEEN` formula for demand, with GAP's lower and upper limits.
4. In **C2** type GAP's profit formula: the base model's net profit calculation with **B2** as the demand and the price, costs, premium and overhead taken from *Base Model* with **absolute** references (`'Base Model'!$B$3` and so on).
5. Select **B2:C2** and drag the fill handle down to row 51.
6. Build GAP's summary box in **E1:F4**: the average, minimum and maximum of C2:C51, and the probability of a loss, `=COUNTIF(C2:C51,"<0")/50`, formatted as a percentage.
7. Press **F9** several times (Mac: **Fn + F9**, or **Cmd + =**) and watch the trials and the summary box recalculate. That is the simulation working. Note which summary values move and by how much.

### Part 4: Answer the questions

In a Word document, answer GAP's four questions in full sentences. In outline they ask you to:

1. read the **Data Table** to find the lowest demand in GAP's grid at which the highest-cost scenario stops making a loss;
2. judge **how risky** the launch is from the probability of a loss, and state the **average** simulated profit, after recalculating several times;
3. set the ethical premium to zero, report how much **net profit** changes, and write a **3–4 sentence recommendation** to the board on keeping the ethical premium;
4. explain how a simulation like this helps the company bring an affordable vehicle to market **responsibly**, and why pricing on a single best case is dangerous, socially and financially.

For question 3, read the change from **your** base model, then **set the premium back to GAP's value** before you save.

---

## 3. Route B: a Python cross-check (offline)

The graded product is an Excel workbook, so there is no Python route that replaces it. The block below is a **cross-check**: it rebuilds the base model, the 25-cell Data Table and a 50-trial simulation in numpy, with GAP's figures, so you can confirm your spreadsheet. Run it in Anaconda JupyterLab from the `DATA300_GAP` folder (it reads no files).

- The **base model** and the **Data Table** have no randomness: your Excel values must match these **exactly**.
- The **simulation** uses a fixed seed, so it prints the same 50 trials every time. Excel's `RANDBETWEEN` has no seed, so your sheet's numbers will differ from these, and from your neighbour's. The extra lines at the end repeat the 50-trial simulation with 20 different seeds, so you can see how much the summary of a 50-trial run moves (Day 5, Part 9).

```{.python .offline}
# Route B cross-check for Lab 6: rebuild GAP's model in numpy (no files needed).
import numpy as np
import pandas as pd

# --- Part 1: base model (GAP's inputs; money in US dollars)
demand = 15_000          # B2: expected unit sales
price = 35_000           # B3: sale price per vehicle
base_cost = 28_000       # B4: base manufacturing cost per vehicle
premium = 500            # B5: ethical sourcing premium per vehicle
overhead = 50_000_000    # B6: fixed overhead


def net_profit(units, cost=base_cost, prem=premium):
    revenue = units * price                     # E2
    variable = units * (cost + prem)            # E3
    return revenue - variable - overhead        # E4


print(f"Base model net profit (E4): ${net_profit(demand):,.0f}")

# --- Part 2: the two-way Data Table (rows: demand, columns: base cost)
demands = np.array([5_000, 10_000, 15_000, 20_000, 25_000])      # B3:B7
costs = np.array([24_000, 26_000, 28_000, 30_000, 32_000])        # C2:G2
grid = net_profit(demands[:, None], costs[None, :])               # every combination at once
table = pd.DataFrame(grid, index=pd.Index(demands, name="demand"), columns=pd.Index(costs, name="base cost"))
print("\nData Table (C3:G7):")
print(table.map(lambda v: f"{v:>15,.0f}").to_string())

# --- Part 3: 50-trial Monte Carlo with RANDBETWEEN(8000, 22000)
rng = np.random.default_rng(618)
sim_demand = rng.integers(8_000, 22_000 + 1, size=50)   # integers() excludes its upper limit, so add 1
sim_profit = net_profit(sim_demand)
print("\nFirst five trials:")
print(pd.DataFrame({"trial": range(1, 6), "demand": sim_demand[:5], "net profit": sim_profit[:5]}).to_string(index=False))
print(f"\nAverage profit:       ${sim_profit.mean():,.0f}")
print(f"Minimum profit:       ${sim_profit.min():,.0f}")
print(f"Maximum profit:       ${sim_profit.max():,.0f}")
print(f"Probability of loss:  {np.mean(sim_profit < 0):.0%}")

# --- How much does a 50-trial result move? Repeat with 20 seeds (like pressing F9 20 times)
repeats = [net_profit(np.random.default_rng(s).integers(8_000, 22_001, 50)) for s in range(20)]
averages = [r.mean() for r in repeats]
minimums = [r.min() for r in repeats]
print(f"\nOver 20 repeats, the average profit ranged from ${min(averages):,.0f} to ${max(averages):,.0f}")
print(f"and the worst trial ranged from ${min(minimums):,.0f} to ${max(minimums):,.0f}")
```

---

## 4. Checks you can make

These tell you whether your workbook is right without giving any answers away.

- [ ] *Base Model* **E4** shows the checkpoint **$47,500,000**, both before and after you link B2 and B4 to the driver cells.
- [ ] The *What-If Analysis* sheet has the corner formula in **B2**, five costs in **C2:G2**, five demands in **B3:B7**, and 25 filled cells in **C3:G7**.
- [ ] Clicking any cell in C3:G7 shows `{=TABLE(J3,J2)}` in the formula bar: the row input first, then the column input.
- [ ] The cell for GAP's base demand and base cost (row 15,000, column 28,000) equals the checkpoint value.
- [ ] Moving **one column to the right** lowers profit by the same amount in every cell of a row (demand × $2,000). Moving **one row down** changes profit by the same amount in every cell of a column. If not, the input cells are swapped or a driver is not used.
- [ ] Every value in C3:G7 matches the Route B table to the dollar.
- [ ] In *Risk Simulation*, every demand in B2:B51 is a **whole number** between GAP's two limits, and every profit in C2:C51 changes when you press F9.
- [ ] The average lies between the minimum and the maximum, and the probability of a loss is a multiple of **2%** (it counts losses out of 50).
- [ ] The ethical premium on *Base Model* is back at GAP's value in the file you submit.
- [ ] Your answer to question 2 describes what you saw over **several** recalculations, not just one press of F9.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| *Input cell reference is not valid* | A row or column input cell is on another sheet (GAP points them at *Base Model*) | Use the driver cells **J3** (row) and **J2** (column) on the *What-If Analysis* sheet, and link *Base Model* to them (Part 2, steps 2–3) |
| The results are zeros, or do not make sense | The selection starts at **A2**, so the empty A2 is taken as the formula and the corner formula in B2 becomes a row value | Put the demands in **B3:B7** and select **B2:G7**, so the formula is the top-left cell |
| Every cell of the table shows the same number | The corner formula does not depend on the input cells: *Base Model* B2 and B4 are still typed numbers, not links to J2 and J3 | Link them (Part 2, step 3), or write the corner formula from J2 and J3 |
| The table's values look wrong, but the centre is right | Row and column input cells swapped | Costs run across the top, so **Row input cell = J3**; demands run down, so **Column input cell = J2**. Delete C3:G7 and rebuild |
| *Cannot change part of a data table* | You tried to edit or delete one cell inside C3:G7 | Select **all** of C3:G7 and press **Delete**, then rebuild |
| The table does not update when an input changes | Calculation is set to *Automatic except for Data Tables* | **Formulas → Calculation Options → Automatic**, or press **F9** |
| The simulation never changes | Calculation is set to *Manual*, or the values were pasted as values | Set calculation to Automatic. Keep `RANDBETWEEN` live in this lab; only freeze a copy if you want to keep one run |
| Copied profit formulas point at the wrong row of *Base Model* | Missing `$` signs, so `B3` became `B4`, `B5`, … when dragged | Use absolute references, `'Base Model'!$B$3`, for every assumption; only `B2` (the trial's demand) stays relative |
| `#REF!` or `#NAME?` in a formula | The sheet name has a space but no quotes, or the sheet was renamed after the formula was written | Write `'Base Model'!B3` with single quotes; retype the reference by clicking the cell |
| The probability of a loss shows as a decimal such as 0.04 | The cell is not formatted as a percentage | **Home → Number → Percentage** |
| Excel rejects the `COUNTIF` formula | The criterion is not in quotes | Write the criterion as `"<0"`, in double quotes |
| F9 does nothing on a Mac | The function keys control the brightness or volume | Press **Fn + F9**, or **Cmd + =** |
| Colour scale shows losses in green | The colour scale was chosen in reverse (*Red - Yellow - Green*) | **Conditional Formatting → Manage Rules → Edit**, and choose **Green - Yellow - Red** (highest value green) |
| Your Route B simulation numbers differ from your Excel | Expected: Excel's random numbers are not seeded | Only the base model and the Data Table must match exactly; compare the simulation's **range** of results |
| Your recommendation for question 3 is only about money | The question asks you to argue **for** the premium, using non-financial evidence | Use Day 6, Parts 12 and 14: brand and legal risk, human rights, what the company has said publicly, and the cost per vehicle in plain terms |

---

## 6. Beyond the lab

Optional, not graded. Do these in a **copy** of your workbook, so the submitted file stays as GAP describes.

1. **More trials.** Extend the simulation to 1,000 rows and compare the summary box with your 50-trial result. Use Day 5, Part 9 to say how precise each estimate is.
2. **Uncertain cost too.** Make the base cost random as well (for example `=NORM.INV(RAND(), 28000, 1500)`) and compare the risk summary. Which input matters more?
3. **Correlation.** Battery shortages may lower demand (fewer cars can be built) while raising cost. Following Day 5, Part 11, build a version where demand and cost move together and compare the probability of a loss.
4. **A one-way table on the premium.** Build a one-way Data Table of net profit for premiums from $0 to $1,000. Express the premium as a share of the sale price and of profit per vehicle.
5. **Break-even by formula.** Write a formula for the demand at which profit is zero for any base cost, and check it against your Data Table.
6. **Write it for the board.** Rewrite your question 3 recommendation in the structure of Day 6, Part 14: answer first, financial evidence, ethical evidence, the trade-off in plain units, conditions.

---

## 7. Submission

| File | Contents |
|---|---|
| Workbook | The three sheets, with the premium back at GAP's value, saved with GAP's file name (`YourLastName_DATA300_Lab6.xlsx`) |
| Answers | Your answers to the four questions, from Word, saved as `YourLastName_Lab6_Answers.pdf` |

1. Check the *Base Model* checkpoint, the full Data Table and the summary box, and set the ethical premium back to GAP's value.
2. Save the workbook as `.xlsx` (not `.xlsm` or `.csv`).
3. Save your answers from Word with **File → Save As → PDF**. If you add screenshots of the sheets, insert them into the Word file before saving, so you still submit one PDF ([Combining PDFs without internet](../setup.md#combining-pdfs-without-internet)).
4. Upload **both files** to **Applied Lab 6** on **GAP** and submit before **Wednesday 18 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)).
