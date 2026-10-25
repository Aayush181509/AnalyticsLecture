# Assignment 2: Predictive data mining report

<p class="lead">
Your second written analytics report. You run GAP's Python code, which generates 500 synthetic house sales, draws two exploratory charts, turns each agent's written description into a Text Appeal Score with sentiment analysis, and fits a multiple linear regression that predicts the sale price. You then explain what it found to a real-estate firm's board in a five-section report, and submit the report and the executed notebook as one PDF on GAP.
</p>

*Adapted from the DATA 300 GAP course, In-Class Module 2, Assignment 2: Predictive Data Mining Report. Written in our own words; follow GAP for the official wording.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Run GAP's two code blocks (no coding of your own is required; one line needs a fix, see *Known pitfalls*), read the data snapshot, the two charts, the text-mining table, the test R² and RMSE, and the coefficient table, and write a report under GAP's five headings |
| **Why** | You play the lead data miner at *UrbanTrend Real Estate Analytics*, which wants an automated way to estimate a home's market value. Analysts have always ignored agents' written descriptions; your job is to turn the text into a number, add it to a price model, and explain to the board what the model can and cannot tell them |
| **CLOs** | CLO 1 (predictive approaches to business problems), CLO 2 (communicating findings with visualisations), CLO 3 (computational methods on structured and unstructured data), CLO 4 (building and evaluating a predictive model) |
| **Weight** | 6% |
| **Deadline** | **Sunday 22 November, 23:59 China Standard Time**, on GAP (briefing in period 4 of Day 4; studio support in periods 7 and 8 of Day 7) |
| **Before you start** | [Predictive regression](../D4_lecture_predictive_regression.md) (Parts 2–7 and 12) and [Text as a feature](../D4_lecture_text_features.md) (Parts 3, 5, 7, 8 and the briefing in Part 10); Day 3's [Text mining](../D3_lecture_text_mining.md), Parts 6 and 7, for how VADER scores text |

The data is **synthetic**: GAP's code creates it with a fixed random seed, so everyone who runs the code correctly gets the same 500 homes. Each row has the floor area (`SqFt`, square feet), the number of `Bedrooms`, the `Age` of the home in years, the agent's `Description`, and the sale `Price` in **US dollars**.

---

## 2. Route A: Try JupyterLab (as on GAP)

### Part 1: Open and name a notebook

Open Try JupyterLab, start a **Python (Pyodide)** notebook and rename it `YourLastName_DATA300_Assignment2.ipynb`.

### Part 2: Generate the data and explore it

Paste GAP's first code block into a cell. **Before you run it**, fix the loop line: GAP prints `for i in rangeNo:`, which raises a `NameError`; it must read `for i in range(n):` (see *Known pitfalls*). Then run it. In outline, the block:

1. installs the libraries with `%pip`;
2. fixes the random seed and draws floor area, age and bedrooms for 500 homes;
3. builds a baseline price from those three facts;
4. gives each home one of a few agent descriptions, adjusting the price for some of them;
5. adds random market noise and puts everything in a DataFrame, showing the first rows;
6. draws two charts side by side: a **scatter plot of floor area against price** and a **box plot of price for each number of bedrooms**.

### Part 3: Text mining and the regression

Paste and run GAP's second block. It:

1. tries to download the VADER lexicon; **if that fails, it silently switches to a much simpler built-in scorer** (see *Known pitfalls*);
2. scores every description and stores the compound score as `Text_Appeal_Score`, showing the first rows of description, score and price;
3. fits a **multiple linear regression** of price on the four features (floor area, bedrooms, age, text score) using an **80/20 train/test split** with a fixed `random_state`;
4. prints the **test R²** and **test RMSE**, then a table of **coefficients** formatted in dollars.

### Part 4: Write the report

Write the report in Word (or another editor) under GAP's **five headings exactly**; see *How to write the report* below.

### Part 5: Export

Run every cell from the top, then **File → Print → Save as PDF** with *Background graphics* ticked. See *Submission* below.

### How to write the report

**The five headings, exactly as GAP gives them, in this order:** `Executive Summary`, `Exploratory Data Analysis`, `Text Mining Methodology & Value`, `Predictive Analytics Results`, `Strategic Recommendations`. Write in **paragraphs**, not bullet lists, except for the two recommendations. What goes under each:

1. **Executive Summary**: one paragraph. The project's purpose, the two kinds of data (structured facts about each home; unstructured agent descriptions) and what the predictive model is for.
2. **Exploratory Data Analysis**: one or two paragraphs on the two charts. The relationship between floor area and price (direction, form, strength, scatter). From the box plot: whether more bedrooms always means a higher **median** price, and how the **spread** of prices (box heights) changes from 2 to 5 bedrooms.
3. **Text Mining Methodology & Value**: one or two paragraphs. What the text-mining step did, in words an executive understands: how a sentence became a number, what the score's range means, and why a pricing model needs text turned into a number at all. Describe the scores **your table actually shows** for each kind of description (see *Known pitfalls*: GAP's wording assumes the fallback scorer's results).
4. **Predictive Analytics Results**: two paragraphs. **Accuracy**: the test R² and what it says about predicting homes the model has not seen; the RMSE in dollars and what "typical error" means. **Business drivers**: the coefficient for one extra bedroom and for one more year of age, in dollars, each with its holding-constant clause. **The value of text**: what a one-unit change in the Text Appeal Score is worth in dollars according to your coefficient, remembering that the score runs from −1 to +1.
5. **Strategic Recommendations**: **two bullet points** of actionable advice to agents, each backed by a specific number from your output.

**Evidence and numbers.** Every claim should point to a chart or table and carry a number with its unit:

| Weak | Strong |
|---|---|
| "The model is accurate." | "On the 100 test homes it had not seen, the model's R² was [value]: it accounts for about [X]% of the variation in their prices. Its RMSE of $[value] means a typical prediction misses by roughly that amount." |
| "Bedrooms add value." | "Holding floor area, age and the text score constant, each additional bedroom is associated with about $[value] [more / less] in predicted price (coefficient table)." |
| "Good descriptions are worth a lot." | "The Text Appeal Score coefficient is $[value] per unit. Moving from a neutral description (0) to a highly positive one (+1) is associated with about $[value] in predicted price, other features held constant." |

The brackets are placeholders: fill them from **your own output**, and only with what it shows.

**Reading coefficients correctly** (Predictive regression lecture, Parts 3 and 12):

- Each coefficient has its own **unit**: dollars per square foot, per bedroom, per year of age, per **one unit** of the text score. GAP's table puts a `$` on all of them, but they are not all "per one thing" of the same kind.
- Each holds the **other features constant**: say so.
- A coefficient describes how prices **differ** between homes in this data, not what would happen if an agent changed something. Think about this before advising agents to rewrite descriptions (Text as a feature, Part 5).
- R² is **not** a percentage of correct predictions, and RMSE is a typical error size, not a guaranteed margin (Predictive regression, Part 6).

**Recommendations that are actionable.** Each says **who** does **what**, **why** (citing your evidence) and **how you would know it worked**. Stay within what the data supports, and say so where it limits the advice (the data is synthetic; it has no location, no market timing, and only a few kinds of description).

---

## 3. Route B: offline in Anaconda JupyterLab

Use this route if the `%pip` install or the VADER download fails, or if you prefer your own laptop. It generates **the same 500 homes** as GAP's code (same seed, same steps, with the loop line corrected), reads the real VADER lexicon from the course folder (`data/nltk_data`), and fits the same model on the same split, so nothing is installed or downloaded. Create a notebook **inside the `DATA300_GAP` folder** (next to `data`), named as in Route A. Paste the block into one cell, or split it at the `# ---` lines into cells that match GAP's parts.

Three small differences from GAP's code, none of which changes any number: the box plot uses one colour (this avoids a seaborn warning, see *Known pitfalls*); tables are printed with `print` rather than `display`; and one line reports which sentiment scorer was used.

```{.python .offline}
# Route B for Assignment 2: run offline in Anaconda JupyterLab.
# The VADER lexicon comes from the course folder (data/nltk_data), so nothing is downloaded.

# --- Setup: point NLTK at the bundled data (run once per session)
import zipfile
from pathlib import Path

import nltk

NLTK_DIR = Path("data/nltk_data").resolve()
if not (NLTK_DIR / "tokenizers" / "punkt_tab").exists():
    with zipfile.ZipFile(NLTK_DIR / "tokenizers" / "punkt_tab.zip") as z:
        z.extractall(NLTK_DIR / "tokenizers")
nltk.data.path.insert(0, str(NLTK_DIR))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

pd.set_option("display.max_colwidth", 60)
pd.set_option("display.width", 140)

# --- Part 2: generate the dataset exactly as GAP does (same seed, same order of random draws)
np.random.seed(101)
n = 500
sqft = np.random.normal(2200, 600, n)
age = np.random.uniform(1, 60, n)
beds = np.random.randint(2, 6, n)

price = (sqft * 150) - (age * 800) + (beds * 15000)          # baseline price from the structured facts

LUXURY = ("Absolutely stunning! Fully renovated with luxury finishes, granite, "
          "and beautiful hardwood. A dream home.")
FIXER = ("Needs significant work. Major fixer-upper. Roof is old and interior "
         "requires complete cosmetic updates. Sold as-is.")
FAMILY = ("Nice family home in a quiet neighborhood. Standard features, "
          "well maintained. Ready to move in.")

descriptions = []
for i in range(n):                                           # GAP prints "rangeNo" here: it must be range(n)
    rand_val = np.random.rand()
    if rand_val > 0.8:
        descriptions.append(LUXURY)
        price[i] += 45000
    elif rand_val < 0.2:
        descriptions.append(FIXER)
        price[i] -= 35000
    else:
        descriptions.append(FAMILY)

price += np.random.normal(0, 15000, n)                       # market noise

df = pd.DataFrame({"SqFt": sqft, "Bedrooms": beds, "Age": age, "Description": descriptions, "Price": price})
print("--- Step 1: Raw data snapshot (structured and unstructured) ---")
print("Homes:", len(df))
print(df.head())

# --- Part 2: exploratory charts
plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x="SqFt", y="Price", alpha=0.6, color="blue")
plt.title("EDA: Square Footage vs. Price")
plt.subplot(1, 2, 2)
sns.boxplot(data=df, x="Bedrooms", y="Price", color="#66c2a5")
plt.title("EDA: Price Distribution by Bedrooms")
plt.tight_layout()
plt.show()

# --- Part 3: text mining with the real VADER lexicon
analyzer = SentimentIntensityAnalyzer()
print("Sentiment scorer used:", type(analyzer).__name__)     # SentimentIntensityAnalyzer = real VADER
df["Text_Appeal_Score"] = df["Description"].apply(lambda x: analyzer.polarity_scores(x)["compound"])
print("\n--- Step 2: Data after text-mining feature engineering ---")
print(df[["Description", "Text_Appeal_Score", "Price"]].head())

# --- Part 3: multiple linear regression on an 80/20 split
features = ["SqFt", "Bedrooms", "Age", "Text_Appeal_Score"]
X = df[features]
y = df["Price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print("\n--- Step 3: Predictive model performance (on hidden test data) ---")
print(f"Test R-squared: {r2:.4f}")
print(f"Test RMSE:      ${rmse:,.2f}")

print("\n--- Step 4: Coefficients (US dollars per one unit of each feature) ---")
coef_df = pd.DataFrame({"Feature": features, "Coefficient": model.coef_})
coef_df["Coefficient"] = coef_df["Coefficient"].apply(lambda x: f"${x:,.2f}")
print(coef_df.to_string(index=False))
```

In JupyterLab you may replace the `print(...)` lines for tables with `display(...)`; the numbers are the same. Export with **Kernel → Restart Kernel and Run All Cells**, then **File → Print → Save as PDF**.

**If you used Route A and your numbers differ from a Route B classmate's**, check which scorer ran in your browser (see *Known pitfalls*). Both are acceptable to report from, but you must say which one you used, because the text scores, the R² and the coefficients all depend on it.

---

## 4. Checks you can make

These tell you whether your output and report are complete without giving any answers away.

- [ ] The first cell runs without a `NameError` (the loop says `range(n)`), and the snapshot reports **500 homes** with five columns.
- [ ] The scatter plot has 500 points; the box plot has **four boxes**, for 2, 3, 4 and 5 bedrooms.
- [ ] You know **which scorer ran**: Route B prints `SentimentIntensityAnalyzer`; in Route A, run `print(type(analyzer).__name__)` in a new cell (`SimpleSentimentAnalyzer` means the fallback).
- [ ] Every `Text_Appeal_Score` lies between **−1 and +1**, and the score takes as many distinct values as there are distinct descriptions (check with `df["Text_Appeal_Score"].nunique()` and `df["Description"].nunique()`).
- [ ] The split leaves **400 training and 100 test homes** (`len(X_train)`, `len(X_test)`).
- [ ] The coefficient table has **four rows**, one per feature, and the RMSE is in dollars.
- [ ] The report has GAP's **five headings exactly**, in order, in paragraphs (bullets only for the two recommendations).
- [ ] Every number in the report can be found in your output, carries a unit, and each coefficient sentence says what is held constant.
- [ ] Your *Text Mining* section describes the scores your own table shows, and names the scorer.
- [ ] The final PDF has the report first and the executed notebook after it.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| `NameError: name 'rangeNo' is not defined` in the first cell | A typo in GAP's code: the loop reads `for i in rangeNo:` | Change it to `for i in range(n):` and run the cell again. Later cells fail with `NameError: name 'df' is not defined` until this cell has run successfully |
| `[nltk_data] Error loading vader_lexicon …`, but the cell finishes anyway | `nltk.download` needs the internet (it fetches from GitHub). If the download fails and no copy of the lexicon is on your machine, GAP's `try … except` **silently** switches to a simple built-in scorer | Check which scorer ran (see *Checks*). For real VADER without internet, use Route B. Say in your report which scorer you used |
| Your scores do not match what GAP's report prompt describes | The prompt's wording (enthusiastic descriptions near 0.8 and higher, "fixer-upper" descriptions negative) matches the **fallback** scorer, which assigns fixed scores by keyword. **Real VADER scores the fixer-upper description positively** (above zero) | Report what **your** table shows, not what the prompt expects. Explain the score with how a lexicon works (Day 3 text-mining lecture, Parts 6 and 7; Text as a feature, Part 3). Consider what this means for the model and the board's trust in the score |
| Your R² or coefficients differ from a classmate's | Different scorers (fallback in the browser, real VADER offline); or the seed, the numbers or the generator were edited; or cells were run out of order after an edit | Use the same scorer, keep GAP's generator unchanged apart from `range(n)`, and run **Restart and Run All**. Name the scorer in your report |
| `FutureWarning: Passing palette without assigning hue is deprecated…` under the charts | Seaborn 0.13 warns about GAP's box plot, which sets `palette=` without `hue=` | Harmless: the chart is correct. To silence it, add `hue="Bedrooms", legend=False` to the `boxplot` call (seaborn 0.13 or later), or use one colour as Route B does |
| `%pip install` hangs or fails in Anaconda | The install needs the internet; the libraries are already in Anaconda | Delete the `%pip` line in Anaconda, or use Route B |
| `ModuleNotFoundError: No module named 'nltk'` (or `sklearn`) in Try JupyterLab | The `%pip install` line did not run in this session | Run the first cell again; every new Try JupyterLab session needs it |
| `LookupError` for `vader_lexicon` (Route B) | The notebook is not in the `DATA300_GAP` folder, or the setup lines were skipped | Save the notebook inside `DATA300_GAP`, next to `data`, restart the kernel and run from the top |
| `NameError: name 'display' is not defined` | `display()` exists only inside Jupyter | Run the code in JupyterLab, or use `print()` as Route B does |
| Every coefficient is shown with a `$` | GAP's table formats all four the same way | Write each with its own unit: per square foot, per bedroom, per year of age, per one unit of the text score |
| The output calls R² "Accuracy" and RMSE an "Error margin" | GAP's labels are shorthand | In the report, describe R² as the share of the variation in test-home prices the model accounts for, and RMSE as the typical size of a prediction error in dollars |
| Descriptions are cut off with `...` in the tables | pandas shortens long text | Widen with `pd.set_option("display.max_colwidth", 120)`, or read the full texts in the code |
| A heading reads "EDA" or "Recommendations" | Headings paraphrased | Copy GAP's five headings word for word, including the `&` in *Text Mining Methodology & Value* |
| Charts are grey or missing in the PDF | *Background graphics* off, or cells not run before printing | Tick *Background graphics*; restart and run all, then print |
| Online PDF merger is blocked or slow | — | Combine the PDFs **offline**: see [Combining PDFs without internet](../setup.md#combining-pdfs-without-internet) |

---

## 6. Beyond the assignment

Optional, not graded. Try these after you have written your report:

1. Look up each word of the three descriptions in `analyzer.lexicon.get("word")`. Which words drive each score, and which does VADER not know?
2. Fit the model **without** `Text_Appeal_Score` on the same split. How much do the test R² and RMSE change? What does that say about the value of the text feature in this data?
3. Replace the sentiment score with two **keyword flags** (for example, "renovated" and "fixer") and refit. How do the coefficients and the test error compare? (Text as a feature, Part 4.)
4. Draw a residual plot (residuals of the test homes against predicted price) and describe it as in the Predictive regression lecture, Part 7.
5. Read the generator code again. Which step creates both the description and its price adjustment? What does that imply about how far this model's accuracy would carry over to real listings? (Text as a feature, Part 7; reading packet Chapter 5, last review question.)
6. Compute the VIFs of the four features (Predictive regression, Part 9). Would you trust each coefficient for explanation?

---

## 7. Submission

| File | Contents |
|---|---|
| Report | Your five-section report, saved as `LastName_Assignment2_Report.pdf` |
| Notebook | The executed notebook with the snapshot, both charts, the text-mining table, the performance figures and the coefficient table visible, saved as `LastName_Assignment2_JupyterLab.pdf` |
| **Final file** | The two combined, **report first**, notebook as an appendix, named `YourLastName_DATA300_Assignment2.pdf` |

1. Restart and run the notebook from the top; check that every table and both charts appear.
2. Export it with **File → Print → Save as PDF**, *Background graphics* ticked.
3. Combine the report and the notebook PDF **offline**, report first ([Combining PDFs without internet](../setup.md#combining-pdfs-without-internet)).
4. Open the final PDF and check both parts are complete and readable.
5. Upload it to **Assignment 2** on **GAP** and submit before **Sunday 22 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)).
