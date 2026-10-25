# Assignment 4: Capstone

<p class="lead">
The course's final project, worth a quarter of your grade. For an electronics company about to sign a five-year manufacturing contract, you turn five focus-group comments into a demand multiplier in Python, build a five-year profit model for two suppliers in Excel, chart the choice in Tableau, and write the board a recommendation that weighs profit against ethics.
</p>

*Adapted from the DATA 300 GAP course, Post-Class Module, Assignment 4: Final Comprehensive Assignment (Capstone). Written in our own words; follow GAP for the official wording, figures and rubric.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Score five focus-group comments with VADER and turn their average into a demand multiplier (JupyterLab); apply it to a five-year demand plan and compute profit under two suppliers (Excel); chart both profit paths by year (Tableau); write an executive summary that answers GAP's two questions (Word, saved as PDF) |
| **Why** | You are the lead BI analyst at **EcoVate**, which is launching a smart-home energy manager. Before it signs the contract, the executive team wants to know how well the product will sell, judging by what focus groups said, and whether to use a cheaper **standard** overseas manufacturer with a record of carbon-emission violations or a costlier **Fair-Trade Green Certified** one. The capstone practises the whole chain of the course: text → number → model → chart → recommendation |
| **CLOs** | CLO 4 (a predictive model that projects outcomes: the sentiment-adjusted demand and the profit model), CLO 5 (evaluating BI tools in a case and writing a managerial report that weighs ethical and societal context) |
| **Weight** | **25%** |
| **Deadline** | **Sunday 29 November, 23:59 China Standard Time**, on GAP (launched in period 5 of Day 7; studio in periods 6–8) |
| **Before you start** | [Course review and integration](../D7_lecture_course_review.md), Parts 4–6 and 11; [Text mining](../D3_lecture_text_mining.md), Parts 6–9; [Simulation under uncertainty](../D5_lecture_simulation_uncertainty.md), Parts 2–3; [BI strategy, forecasting and ethics](../D6_lecture_bi_strategy_ethics.md), Parts 12 and 14 |

Use GAP's figures for the five-year base demand, the selling price, the fixed cost and the two suppliers' unit costs. All money is in **US dollars**, as on GAP. Read GAP's capstone rubric before you start: everyone works from the same inputs, so the quality of your reasoning is what sets your report apart.

### The studio afternoon (Day 7, periods 5–8)

Use the afternoon to get every tool step done and checked while help is in the room, and leave the writing for the post-class week. Each checkpoint is something you can show your facilitator.

| Period | Goal | Checkpoint |
|---|---|---|
| **P5** 13:45–14:30 | Launch: read sections 1, 4 and 5 of this guide; choose Route A or Route B; run the text-mining step | **1.** The notebook runs from the top; you have written down the multiplier exactly as printed **and which scorer produced it** (see section 5); the notebook PDF is exported |
| **P6** 14:40–15:25 | Build the Excel model | **2.** Six columns and five years; every check in section 4 for the workbook passes; the file is saved as `.xlsx` and **closed** |
| **P7** 15:40–16:25 | Build the Tableau chart | **3.** Two series, one point or bar per year, a currency axis and a legend; the image is exported and pasted into a Word document |
| **P8** 16:35–17:20 | Plan the report (and get help with Assignments 2 and 3 if needed) | **4.** An outline: a two-sentence introduction; for question 1, your answer, the evidence you will quote (with the cell it comes from), the trade-off and one condition; for question 2, three reasons the three-tool chain beats a static spreadsheet |

After Day 7, aim for a full draft by the middle of the post-class week, so you have time to cut it down and check every number against your workbook before **Sunday 29 November**.

---

## 2. Route A: Try JupyterLab, Excel and Tableau (as on GAP)

### Part 1: Text mining in Try JupyterLab

1. Open Try JupyterLab, start a **Python (Pyodide)** notebook and rename it with the file name GAP gives (your last name, the course code and "Capstone", as `.ipynb`).
2. Paste GAP's single code block into a cell and run it. In outline, it:
    1. installs pandas and NLTK into the browser session with `%pip`;
    2. tries to download NLTK's VADER lexicon with `nltk.download` and create the VADER analyser, and **if anything goes wrong, quietly switches to a small keyword-based stand-in scorer** that gives one of three fixed scores depending on a few words;
    3. puts the five focus-group comments in a DataFrame;
    4. scores each comment and stores the compound score;
    5. averages the five scores and turns the average into a **demand multiplier**: 1, plus the average score times 0.20, so a fully positive average would add at most 20% to demand;
    6. shows the table and prints the average and the multiplier to three decimal places.
3. Add one cell under GAP's cell and run `print(type(analyzer).__name__)`. It prints the name of the scorer that actually ran: `SentimentIntensityAnalyzer` is VADER; anything else is the stand-in. Keep this cell in your PDF.
4. Write the multiplier down **exactly as printed** (three decimals).
5. Export: **File → Print → Save as PDF**, with GAP's file name for the notebook PDF.

### Part 2: The financial model in Excel

1. Open a blank workbook and save it with GAP's file name (your last name, the course code and "Capstone", as `.xlsx`).
2. **Headers.** Type GAP's six headers in **A1:F1**: `Year`, `Base_Demand`, `Colab_Multiplier`, `Adjusted_Demand`, `Standard_Profit`, `Ethical_Profit`. (The third header is a leftover from an older version that used Google Colab; see section 5.)
3. **Years and base demand.** Type 1 to 5 in **A2:A6** and GAP's five base-demand figures in **B2:B6**.
4. **Multiplier.** Type your multiplier, as printed, into **C2:C6** (the same value in all five cells).
5. **Adjusted demand.** In **D2**, type GAP's formula: base demand times the multiplier, rounded to a whole unit with `ROUND(…, 0)`. Fill it down to **D6**.
6. **Profit.** In **E2** and **F2**, type GAP's two profit formulas: adjusted demand times that supplier's margin per unit (the selling price minus that supplier's unit cost), minus the yearly fixed cost. Fill both down to row 6.
7. Optionally format E2:F6 as **Currency** (Home → Number Format). Save, then **close Excel** before you open Tableau.

### Part 3: The chart in Tableau

1. Open Tableau Desktop. Under **Connect**, choose **Microsoft Excel** and open your saved workbook. Drag the sheet onto the canvas if it is not there already, then click the **Sheet 1** tab at the bottom.
2. Drag **Year** to **Columns**. Tableau makes it a green `SUM(Year)` pill; right-click it and choose **Dimension**.
3. Drag **Measure Values** (at the bottom of the Data pane) to **Rows**.
4. On the **Measure Values** card below the Marks card, remove every measure except the sums of **Standard Profit** and **Ethical Profit**.
5. On the Marks card, choose **Line** or **Bar**, and drag **Measure Names** onto **Color**.
6. Format the vertical axis as **currency** (see section 5 for the menu path).
7. **Worksheet → Export → Image…**, save the image and insert it into a blank Word document.

### Part 4: The managerial report

In the Word document that holds your chart, write a short executive summary: a brief introduction, then your answers to GAP's two questions.

1. **Strategic and ethical recommendation (CLO 5).** GAP asks you to assume that the focus groups showed the target customers care a great deal about a company's carbon footprint, and to recommend one supply chain to the board, weighing how large the profit difference is against the ethical context and the long-term value of the brand.
2. **The value of an integrated BI chain.** GAP asks why moving from text mining to a spreadsheet model to a visual story gives a sounder, more realistic plan than a static spreadsheet alone.

Use the structure from Day 6, Part 14 and Day 7, Part 6: answer first, the evidence with its numbers, the trade-off stated in plain units, the conditions and limits.

### Part 5: Submit

See section 7.

---

## 3. Route B: offline in Anaconda JupyterLab

Use this route if `%pip` or the NLTK download fails in Try JupyterLab, or if you prefer your own laptop. It scores the same five comments with **real VADER**, reading the lexicon from the course folder (`data/nltk_data`), and it **stops with an error** instead of switching to a stand-in scorer if the lexicon cannot be found. Create a notebook **inside the `DATA300_GAP` folder** (next to `data`), named as in Route A. The five comments are bundled in `data/ecovate_focus_group.csv`.

```{.python .offline}
# Route B for the capstone, Part 1: VADER offline, no downloads and no silent fallback.
from pathlib import Path

import nltk
import pandas as pd

NLTK_DIR = Path("data/nltk_data").resolve()
nltk.data.path.insert(0, str(NLTK_DIR))
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()     # raises an error if the lexicon is missing: no silent fallback
print("Scorer used:", type(analyzer).__name__, "| NLTK", nltk.__version__)

# The five focus-group comments from GAP, bundled with the course
df = pd.read_csv("data/ecovate_focus_group.csv")
assert len(df) == 5, "expected five comments"

# Score each comment: the compound score runs from -1 (very negative) to +1 (very positive)
df["Sentiment_Score"] = df["Review_Text"].apply(lambda text: analyzer.polarity_scores(text)["compound"])

# GAP's rule: baseline demand 1.0, plus up to 0.20 for a fully positive average
avg_sentiment = df["Sentiment_Score"].mean()
demand_multiplier = 1.0 + avg_sentiment * 0.20

pd.set_option("display.max_colwidth", 100)
print(df[["Review_ID", "Review_Text", "Sentiment_Score"]].to_string(index=False))
print(f"\nAverage sentiment score: {avg_sentiment:.3f}")
print(f"Demand multiplier (type this, as printed, into Excel C2:C6): {demand_multiplier:.3f}")
```

Optionally, after you have built your workbook **by hand in Excel**, the block below rebuilds Part 2 in pandas so that you can compare it with your workbook cell by cell, and previews the Tableau chart. It does not replace the Excel file: the workbook you submit must be your own, with formulas. Replace the multiplier with the one your notebook printed.

```{.python .offline}
# Route B mirror for the capstone, Part 2: check your Excel workbook, and preview the chart.
from pathlib import Path

import nltk
import pandas as pd
import matplotlib.pyplot as plt

# Your multiplier, exactly as your notebook printed it (three decimals).
# This line recomputes it with VADER; replace the right-hand side with the number you typed into Excel.
nltk.data.path.insert(0, str(Path("data/nltk_data").resolve()))
from nltk.sentiment.vader import SentimentIntensityAnalyzer
_texts = pd.read_csv("data/ecovate_focus_group.csv")["Review_Text"]
_sia = SentimentIntensityAnalyzer()
multiplier = round(1.0 + 0.20 * _texts.apply(lambda t: _sia.polarity_scores(t)["compound"]).mean(), 3)

# GAP's inputs (US dollars)
base_demand = [10_000, 15_000, 22_000, 30_000, 45_000]
price, fixed_cost = 200, 500_000
unit_cost_standard, unit_cost_ethical = 120, 140

model = pd.DataFrame({"Year": [1, 2, 3, 4, 5], "Base_Demand": base_demand})
model["Colab_Multiplier"] = multiplier
# Excel's ROUND rounds halves away from zero; Python's round() rounds halves to even.
# Use the Excel rule so the mirror matches your workbook in every case.
raw = model["Base_Demand"] * model["Colab_Multiplier"]
model["Adjusted_Demand"] = (raw + 0.5).astype(int)
model["Standard_Profit"] = model["Adjusted_Demand"] * (price - unit_cost_standard) - fixed_cost
model["Ethical_Profit"] = model["Adjusted_Demand"] * (price - unit_cost_ethical) - fixed_cost
print(model.to_string(index=False))

# Rule checks: the same rules as section 4 of the guide
assert (model["Adjusted_Demand"] == (model["Base_Demand"] * multiplier + 0.5).astype(int)).all()
assert model[["Adjusted_Demand", "Standard_Profit", "Ethical_Profit"]].notna().all().all()
print("\nRule checks passed. Compare each cell with your Excel workbook.")

# Preview of the Tableau view: Year as a dimension, two measures, colour by measure, currency axis
fig, ax = plt.subplots(figsize=(8, 4))
for column, colour in [("Standard_Profit", "#0072B2"), ("Ethical_Profit", "#009E73")]:
    ax.plot(model["Year"], model[column], marker="o", color=colour, label=column.replace("_", " "))
ax.set_xticks(model["Year"])
ax.set_xlabel("Year")
ax.set_ylabel("Profit (US dollars)")
ax.yaxis.set_major_formatter(lambda value, _: f"${value:,.0f}")
ax.set_title("Preview: profit by year under each supplier")
ax.legend(frameon=False)
plt.show()
```

In JupyterLab you may replace the `print(... .to_string(index=False))` lines with `display(df)` for nicer tables. Export the first block's notebook with **Kernel → Restart Kernel and Run All Cells**, then **File → Print → Save as PDF**.

---

## 4. Checks you can make

These tell you whether your work is right without giving any answers away.

**Notebook**

- [ ] The table has **five rows**, one per comment, and every score lies between **−1 and +1**.
- [ ] Your PDF shows **which scorer ran** (VADER's `SentimentIntensityAnalyzer` or a stand-in).
- [ ] The multiplier lies between **0.8 and 1.2**, as GAP's rule allows, and equals 1 + 0.20 × the printed average (check it on a calculator).
- [ ] Every score and the average are visible in the PDF, not cut off.

**Workbook**

- [ ] Row 1 holds six headers; rows 2 to 6 hold years 1 to 5 and GAP's five base-demand figures.
- [ ] **C2:C6** all hold the **same** multiplier, exactly as your notebook printed it.
- [ ] Every adjusted demand is a **whole number**, and equals base demand × multiplier rounded.
- [ ] Each profit = adjusted demand × that supplier's margin − the fixed cost. Check one row by hand for each supplier.
- [ ] Clicking D2, E2 or F2 shows a **formula** in the formula bar, not a typed number.

**Chart**

- [ ] **Five** years on the horizontal axis, two series, and a legend that names the two profit measures; nothing else on the Measure Values card.
- [ ] The vertical axis shows dollar signs.
- [ ] The values in the chart match your workbook for at least two years you checked (hover over a mark).

**Report**

- [ ] The introduction says what was decided and how, in two or three sentences.
- [ ] Your answer to question 1 names **one** supply chain, quotes numbers from **your** workbook, states how big the profit difference is in plain terms, and weighs it against the ethical and brand context.
- [ ] Your answer to question 2 explains what each tool added that a static spreadsheet could not, not just what each tool is.
- [ ] You say which scorer produced your multiplier, and you note at least one limit of scoring five short comments.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| A header called `Colab_Multiplier`, though the course does not use Colab | GAP's header list is a leftover from a version that used Google Colab | Any clear header works (for example `Demand_Multiplier`), **as long as you use the same name in Tableau**. Keeping GAP's header is simplest: it matches GAP's instructions and Tableau shows it as *Colab Multiplier* |
| Your multiplier differs from a classmate's | GAP's code **silently** switches to a stand-in keyword scorer if `nltk.download` fails, as it may in the browser or behind a blocked network, and the stand-in gives different scores from VADER | Add `print(type(analyzer).__name__)` (Route A, Part 1 step 3) or use Route B. Carry **your** multiplier consistently through Excel, Tableau and the report, and say in the report which scorer produced it. If you are unsure which to use, ask your facilitator |
| `nltk.download` hangs or fails offline | No internet access, or GitHub is blocked | Use Route B: the lexicon is already in `data/nltk_data` and nothing is downloaded |
| `%pip` errors in Anaconda | `%pip install` lines are for the browser session | Delete them in Route B; Anaconda already has pandas and NLTK |
| `NameError: name 'display' is not defined` | `display` exists only inside Jupyter | Run the code in a notebook, or use `print(df.to_string(index=False))` |
| `FileNotFoundError` for `data/ecovate_focus_group.csv` | The notebook is not in the `DATA300_GAP` folder | Save the notebook next to the `data` folder, or fix the path |
| Adjusted demand differs by one unit from a classmate's | Different numbers of decimals in the multiplier | Type the multiplier **exactly as printed** (three decimals) in all five cells; do not paste a longer unrounded value |
| Adjusted demand has decimals | `ROUND(…, 0)` left out | Use GAP's formula with `ROUND` |
| Only C2 holds the multiplier and later rows show zero demand | C3:C6 were left empty | Fill the multiplier into every cell of C2:C6 |
| Tableau shows **one** bar or point instead of five | **Year** is a measure, so Tableau adds the five years together into `SUM(Year)` | Right-click the Year pill → **Dimension** |
| Extra lines or bars (base demand, the multiplier, adjusted demand) | The Measure Values card still lists every measure | Remove every pill from the Measure Values card except the two profit sums; or right-click **Measure Names** → **Filter** and tick only the two profits |
| Double-clicking the axis does not offer currency | Double-click opens **Edit Axis** (range and title), not the number format | Right-click the axis → **Format…** → in the Format pane, **Axis** tab → **Scale → Numbers** → **Currency (Standard)** or **Currency (Custom)** with 0 decimals. Or right-click each profit field in the Data pane → **Default Properties → Number Format… → Currency** |
| Tableau cannot open the workbook, or shows old values | The file is still open in Excel, or it was saved after Tableau connected | Save and close Excel, then in Tableau **Data → Refresh** (or reconnect) |
| Field names show spaces instead of underscores | Tableau tidies field names automatically | Nothing to fix: *Standard Profit* is your `Standard_Profit` column |
| The workbook was saved as `.csv` | **Save As** chose the wrong type | Save again as **Excel Workbook (.xlsx)**; GAP asks for the `.xlsx` |
| The Try JupyterLab notebook is gone the next day | The browser session ended | Export the PDF and download the `.ipynb` before closing the tab ([why](../index.md#why-you-export-before-closing-a-try-jupyterlab-tab)) |
| The exported image is blank or cut off | Exported before the view finished drawing, or the window was small | Enlarge the worksheet, wait, then **Worksheet → Export → Image…** again |

---

## 6. Beyond the capstone

Optional, not graded. Do these in **copies** of your notebook and workbook, after the graded files are finished.

1. **Read the comments yourself.** Score the five comments by hand on a scale from −1 to +1, then compare your scores with VADER's. Which comment would you score differently, and which words explain the difference (Day 3, Part 7)?
2. **How much does the 0.20 matter?** GAP caps the sentiment effect at 20%. In a copy of the workbook, put the 0.20 in its own input cell and build a one-way Data Table (Day 5, Part 4) with values from 0.10 to 0.30. Describe how the adjusted demand responds.
3. **Uncertain demand.** Base demand is a forecast, not a fact. Replace it with `=ROUND(NORM.INV(RAND(), B2, 0.15*B2), 0)` in a copy, simulate 500 trials of each year's two profits with a Data Table (Day 5, Part 9), and describe each supplier's range and chance of a loss.
4. **A dashboard.** In Tableau, add a second sheet showing adjusted demand by year as bars, and combine both sheets in a dashboard with a message title.
5. **A one-page memo.** Rewrite your answer to question 1 as a one-page memo in the structure of Day 6, Part 14, labelling each statement as a fact, an estimate or a judgement, and adding one condition that would change your recommendation.

---

## 7. Submission

| File | Contents |
|---|---|
| Report | Your executive summary with the Tableau image, saved as `YourLastName_Capstone_Report.pdf` |
| Notebook | The executed notebook as a PDF, with GAP's name for it (`LastName_JupyterLabLab.pdf`, or as GAP instructs), attached to the end of the report **or** submitted as a separate file |
| Workbook | `YourLastName_DATA300_Capstone.xlsx`, with formulas in columns D to F |

1. Run the notebook from the top (Route B: **Kernel → Restart Kernel and Run All Cells**) and export it with **File → Print → Save as PDF**, *Background graphics* ticked.
2. Insert the Tableau image into the Word document **before** writing around it, and save the report from Word with **File → Save As → PDF**.
3. If you attach the notebook PDF to the end of the report, combine the files **offline** ([Combining PDFs without internet](../setup.md#combining-pdfs-without-internet)), then open the result and check that every page is there.
4. Check that every number in the report matches your workbook and that the workbook is the final version.
5. Upload the files to **Assignment 4** on **GAP** and submit before **Sunday 29 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)).
