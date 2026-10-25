# Lab 1: Data exploration

<p class="lead">
Your first graded Python lab. You explore a table of diamonds for an imaginary jewellery retailer: check its structure and quality, build a pivot table of average price, draw a correlation heatmap, a violin plot and a hexbin plot, answer short questions about what you see, and submit one PDF on GAP.
</p>

*Adapted from the DATA 300 GAP course, In-Class Module 1, Lab 1: Data Exploration. Written in our own words; follow GAP for the official wording.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Run four steps of given Python code on the diamonds data (structure, pivot table, three charts), then answer seven questions in a Markdown cell at the bottom of the notebook |
| **Why** | Every later lab and assignment assumes you can check a dataset before trusting it, summarise it by group, and read a chart without over-reading it. The lab's scenario is a buyer deciding how to price and stock diamonds |
| **CLOs** | CLO 1 (the business question descriptive analytics can answer), CLO 2 (charts that communicate a finding), CLO 3 (computing to find relationships in structured data) |
| **Weight** | 3% |
| **Deadline** | **Tuesday 10 November, 23:59 China Standard Time**, on GAP (worked on in periods 7 and 8 of Day 1) |
| **Before you start** | The two Day 1 lectures: [Foundations of data-driven decisions](../D1_lecture_foundations_decisions.md) and [Exploring data](../D1_lecture_exploring_data.md) |

The data has one row per diamond: its weight (`carat`), three quality grades (`cut`, `color`, `clarity`), two proportions (`depth` and `table`, both percentages), its `price` in **US dollars**, and its length, width and depth in millimetres (`x`, `y`, `z`).

---

## 2. Route A: Try JupyterLab (as on GAP)

### Part 1: Open and name a notebook

Open Try JupyterLab, start a **Python (Pyodide)** notebook and rename it with the file name GAP gives (your last name, the course code and "AppliedLab1").

### Part 2: Load the data and inspect its structure

Paste GAP's first code block into a cell and run it. In outline, it:

1. installs seaborn into the browser session with `%pip`;
2. imports pandas, seaborn, matplotlib and numpy, and `open_url` from `pyodide.http`;
3. loads `diamonds.csv` from the seaborn-data repository on GitHub;
4. prints `info()`, the missing-value count per column and the `describe()` summary.

### Part 3: Pivot table

Paste and run GAP's second block. It builds a pivot table of the **mean price** with cut quality down the side and colour grade across the top. On GAP's scales, colour runs from D (colourless, best) to J (faint yellow), and cut from Fair (lowest) to Ideal (best).

### Part 4: Three charts for a large dataset

Paste and run GAP's third block. It draws:

1. a **correlation heatmap** of the numeric columns, annotated, on a fixed −1 to +1 scale;
2. a **violin plot** of price for each cut;
3. a **hexbin plot** of carat against price, with a colour bar for the number of diamonds per hexagon.

### Part 5: Answer the questions

Add a **Markdown** cell at the bottom and answer GAP's seven questions in full sentences. They come in three groups: data quality and structure (two questions), the pivot table (an unexpected comparison and the hidden variable behind it), and the charts (the strongest correlation with price, the shape of the price distribution, and where the hexbin is densest). Read every answer from **your own output** and name the table or chart it comes from.

### Part 6: Export and submit

Run everything from the top, then **File → Print → Save as PDF** with *Background graphics* ticked. See *Submission* below.

---

## 3. Route B: offline in Anaconda JupyterLab

Use this route if Try JupyterLab will not load the data, or if you prefer your own laptop. It follows the same steps as GAP's code but reads the bundled copy of the data, so nothing is installed or downloaded. Create a notebook **inside the `DATA300_GAP` folder** (next to `data`). You can paste the whole block into one cell, or split it at the `# ---` lines into four cells, which matches GAP's parts. The questions are exactly the same as in Route A.

```{.python .offline}
# Route B for Lab 1: run offline in Anaconda JupyterLab.
# The diamonds file comes from the course folder, so nothing is installed or downloaded.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)   # show every column when printing

# --- Part 2: load the data and inspect its structure
diamonds = pd.read_csv("data/diamonds.csv")

print("--- Structure ---")
diamonds.info()

print("\n--- Missing values in each column ---")
print(diamonds.isnull().sum())

print("\n--- Summary of the numeric columns ---")
print(diamonds.describe().round(2))

# --- Part 3: pivot table of mean price (US dollars) by cut and colour
price_pivot = pd.pivot_table(diamonds, values="price", index="cut",
                             columns="color", aggfunc="mean")
print("\n--- Mean price (US dollars) by cut (rows) and colour grade (columns) ---")
print(price_pivot.round(2))

# --- Part 4: three charts
sns.set_theme(style="whitegrid")

# Chart 1: correlation heatmap of the numeric columns
corr_matrix = diamonds.select_dtypes(include="number").corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm",
            linewidths=0.5, vmin=-1, vmax=1)
plt.title("Correlations between the numeric diamond attributes")
plt.show()

# Chart 2: violin plot of price for each cut (one colour, works on any seaborn version)
plt.figure(figsize=(10, 6))
sns.violinplot(data=diamonds, x="cut", y="price", color="#9cc3ef")
plt.title("Distribution of price for each cut quality")
plt.xlabel("Cut quality")
plt.ylabel("Price (US dollars)")
plt.show()

# Chart 3: hexbin of carat (x) against price (y)
plt.figure(figsize=(9, 6))
plt.hexbin(diamonds["carat"], diamonds["price"], gridsize=40, cmap="Blues", mincnt=1)
plt.colorbar(label="Number of diamonds in the hexagon")
plt.title("Where the diamonds concentrate: carat and price")
plt.xlabel("Carat (weight)")
plt.ylabel("Price (US dollars)")
plt.show()
```

In JupyterLab you may replace the `print(...)` around `describe()` and the pivot table with `display(...)` for nicer tables; the numbers are the same. Export with **Kernel → Restart Kernel and Run All Cells**, then **File → Print → Save as PDF**.

---

## 4. Checks you can make

These tell you whether your output is right without giving any answers away.

- [ ] The table has **10 columns**: three text columns (`cut`, `color`, `clarity`) and seven numeric ones. The row count you report comes from `info()` (the `RangeIndex` line) or from `diamonds.shape`; it is more than 50,000.
- [ ] `describe()` lists the **seven numeric columns** only, and its `count` row agrees with what `info()` and the missing-value check say.
- [ ] The pivot table has **5 rows** (one per cut) and **7 columns** (colour grades D to J), and every value is a price in US dollars.
- [ ] The heatmap is a **7 × 7** square with 1.00 down the diagonal; the colour bar runs from −1 to +1.
- [ ] The violin plot has **five violins**, one per cut, and a y-axis in US dollars.
- [ ] The hexbin plot has carat along the bottom, price up the side and a colour bar counting diamonds.
- [ ] Each answer names the output it comes from, gives numbers with units (US dollars, carats), and, for the "why" question, names a variable and says how you would check it.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| The first cell hangs or ends with a network error | GitHub is slow or blocked | Drag `diamonds.csv` from the course folder into Try JupyterLab's file browser and use `pd.read_csv("diamonds.csv")` in place of the `open_url` line, or switch to Route B |
| `ModuleNotFoundError: No module named 'seaborn'` in Try JupyterLab | The `%pip install` line did not run in this session | Run the first cell again; every new Try JupyterLab session needs it |
| `ModuleNotFoundError: No module named 'pyodide'` in Anaconda | GAP's browser-only code was pasted into Route B | Use the Route B code above |
| `FileNotFoundError: data/diamonds.csv` | The notebook is not in the `DATA300_GAP` folder | Save the notebook inside `DATA300_GAP`, next to `data`, and run again |
| `NameError: name 'display' is not defined` | `display()` exists only inside Jupyter, not in a plain Python script | Run the code in JupyterLab, or use `print()` as Route B does |
| The violin plot shows thin violins shifted away from their labels, plus a legend | GAP's code uses `hue="cut"` with `legend=False`, which needs **seaborn 0.13 or later**. Older seaborn (for example in an older Anaconda) ignores `legend=False` and squeezes the violins side by side | Check with `print(sns.__version__)`. On an older version, delete `hue="cut"`, `palette="muted"` and `legend=False` and use `color="#9cc3ef"`, as Route B does |
| The cuts in the pivot table are in the order Fair, Good, Ideal, Premium, Very Good | pandas sorts text alphabetically, not by quality | The values are still correct. To read the table in quality order, add `.reindex(["Fair", "Good", "Very Good", "Premium", "Ideal"])` after `pivot_table(...)` |
| The violins are in a different order from the pivot table | seaborn uses the order in which each cut first appears in the data | Add `order=["Fair", "Good", "Very Good", "Premium", "Ideal"]` to `violinplot` if you want quality order |
| Unsure what currency the prices are in | — | `price` is in **US dollars**, as in the original dataset; write "US dollars" or "$" in your answers |
| `x`, `y` and `z` look like coordinates | They are the stone's length, width and depth in millimetres | Treat them as size measurements when you read the heatmap |
| You notice repeated rows, or some diamonds with a length, width or depth of 0 | The dataset contains 146 fully duplicated rows and a few rows with a zero dimension, which is physically impossible | These are worth mentioning as **data-quality observations** in your answers if you find them. Do not delete them: GAP's questions are about the data as loaded |
| Charts print in grey or are missing from the PDF | *Background graphics* was off, or cells were not run before printing | Tick *Background graphics*; restart and run all, then print |
| The PDF cuts off the wide pivot table or the `describe()` table | The browser's print width | Print in landscape, or reduce the scale in the print dialog until the full table fits |

---

## 6. Beyond the lab

Optional, not graded. Try these in the same notebook after you have answered GAP's questions:

1. Count the problem rows yourself: `diamonds.duplicated().sum()` and `(diamonds[["x", "y", "z"]] == 0).any(axis=1).sum()`. Which data quality dimensions from the morning lecture do they break?
2. Build a second pivot table with `aggfunc="count"` in place of `"mean"`. Which cells rest on few diamonds, and how should that change how much you trust their averages?
3. Draw a histogram of `price` with `np.log10(diamonds["price"])` on the x-axis. How does the shape change compared with the violin plot?
4. Create carat bands with `pd.cut(diamonds["carat"], bins=[0, 0.5, 1, 1.5, 2, 6])` and build a pivot table of mean price by band and cut. What does it add to your answer about the hidden variable?
5. Calculate a price per carat (`diamonds["price"] / diamonds["carat"]`) and compare its median across cuts. Write one sentence for the retailer's buyer.

---

## 7. Submission

| File | Contents |
|---|---|
| **Final file** | The executed notebook as one PDF: structure output, pivot table, all three charts and the Markdown cell with your seven answers, named `YourLastName_DATA300_AppliedLab1.pdf` |

1. Run **Kernel → Restart Kernel and Run All Cells** (Route B) or run every cell from the top (Route A), and check that every table and chart is visible.
2. Export with **File → Print → Save as PDF**, *Background graphics* ticked. If you wrote answers in a separate document instead, combine the PDFs **offline** as described in [Combining PDFs without internet](../setup.md#combining-pdfs-without-internet).
3. Open the PDF and check every part is present and readable.
4. Upload it to **Applied Lab 1** on **GAP** and submit before **Tuesday 10 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)).
