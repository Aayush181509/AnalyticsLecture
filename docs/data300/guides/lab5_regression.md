# Lab 5: Regression

<p class="lead">
Your fifth graded Python lab, and the first of Module 2. You build a multiple linear regression that predicts a car's fuel economy in miles per gallon (MPG) from five engineering specifications, train it on 80% of the cars, test it on the 20% it has never seen, measure its error with RMSE, MAE and R², check its residuals, answer five questions about your own output, and submit one PDF on GAP.
</p>

*Adapted from the DATA 300 GAP course, In-Class Module 2, Lab 5: Predictive Linear Regression Modeling. Written in our own words; follow GAP for the official wording.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Run four blocks of given Python code (load and clean, split and fit, predict and evaluate, residual diagnostics), then answer five questions in a Markdown cell at the bottom of the notebook |
| **Why** | A model that fits the cars it was trained on may still fail on new ones. The lab's scenario is an automotive consultancy that must show a car maker that its fuel-economy model works on vehicles it has never seen before anyone designs around it |
| **CLOs** | CLO 4 (developing a predictive model with linear regression to project outcomes), CLO 5 (judging what a model's results mean for a business decision) |
| **Weight** | 2% |
| **Deadline** | **Tuesday 17 November, 23:59 China Standard Time**, on GAP (worked on in periods 7 and 8 of Day 5) |
| **Before you start** | The [Predictive regression](../D4_lecture_predictive_regression.md) lecture, especially Parts 2, 3, 5, 6 and 7, and Part 15 of [Simulation under uncertainty](../D5_lecture_simulation_uncertainty.md) (the Lab 5 bridge) |

The data is the classic **Auto MPG** data set: 398 cars from model years 1970 to 1982. The lab uses five features and one target:

| Column | Meaning | Unit |
|---|---|---|
| `mpg` | Fuel economy (the **target**) | miles per US gallon; higher is more economical |
| `cylinders` | Number of engine cylinders | count |
| `displacement` | Engine size | cubic inches |
| `horsepower` | Engine power | horsepower |
| `weight` | Vehicle weight | pounds |
| `acceleration` | Time to accelerate from 0 to 60 mph | seconds; a **larger** number is a **slower** car |

The file also has `model_year`, `origin` (`usa`, `japan` or `europe`) and `name`, which GAP's model does not use.

---

## 2. Route A: Try JupyterLab (as on GAP)

### Part 1: Open and name a notebook

Open Try JupyterLab, start a **Python (Pyodide)** notebook and rename it with the file name GAP gives (your last name, the course code and "AppliedLab5").

### Part 2: Load the data and prepare it

Paste GAP's first code block into a cell and run it. In outline, it:

1. installs seaborn, scikit-learn, matplotlib, pandas and numpy into the browser session with `%pip`;
2. imports pandas, numpy, seaborn, matplotlib, and from scikit-learn `train_test_split`, `LinearRegression` and three error functions;
3. downloads `mpg.csv` from the seaborn-data repository on GitHub, using Pyodide's `open_url` inside the browser and an ordinary `read_csv` elsewhere;
4. **drops every row with a missing value** (`dropna`);
5. sets the five features as **X** and `mpg` as **y**;
6. shows the first five rows and prints how many cars remain.

### Part 3: Split the data and train the model

Paste and run GAP's second block. It splits the cars **80% for training and 20% for testing** with `random_state=42`, so everyone gets the same split; prints how many cars are in each part; fits a `LinearRegression` on the training cars only; and shows a table with one **coefficient** per feature.

### Part 4: Predict the test cars and measure accuracy

Paste and run GAP's third block. It predicts MPG for the test cars, computes **RMSE** (as the square root of the mean squared error), **MAE** and **test R²**, prints them, and draws an **actual versus predicted** scatter plot with a red dashed **perfect-prediction line** (y = x).

### Part 5: Residual diagnostics

Paste and run GAP's fourth block. It computes the **residuals** (actual minus predicted) for the test cars and plots them against the predicted MPG, with a red dashed line at zero.

### Part 6: Answer the questions

Add a **Markdown** cell at the bottom (or a separate document, if your instructor asks for one) and answer GAP's five questions in full sentences. They cover: what the **weight** coefficient means in plain English, per pound and per 1,000 pounds; the **test R²** and what it says about predicting cars the model has not seen; the **MAE** and how you would explain it to engineers; whether the points in the actual-versus-predicted plot cluster tightly around the line, and whether the model struggles more with low-MPG or high-MPG cars; and whether the **residual plot** looks like a random cloud or shows a curve or a widening pattern, and what you conclude. Read every value from **your own output**, give units (MPG, pounds) and name the output each comes from.

### Part 7: Export and submit

Run everything from the top, then **File → Print → Save as PDF** with *Background graphics* ticked. See *Submission* below.

---

## 3. Route B: offline in Anaconda JupyterLab

Use this route if GitHub is blocked, `%pip install` is slow in Try JupyterLab, or you prefer your own laptop. The data is in the course folder as `data/mpg.csv`, the same file GAP downloads, so nothing is installed or downloaded. Create a notebook **inside the `DATA300_GAP` folder**, named as in Route A. Paste the block into one cell, or split it at the `# ---` lines into four cells that match GAP's parts. The questions are the same as in Route A.

The steps follow GAP exactly: drop missing rows, the same five features, an 80/20 split with `random_state=42`, the same model and the same three measures, so your numbers match a Route A classmate's. Three small differences, none of which changes a number: tables are printed with `print` instead of `display`; the perfect-prediction line spans both the actual and the predicted values (see *Known pitfalls*); and the charts use colour-blind-safe colours.

```{.python .offline}
# Route B for Lab 5: run offline in Anaconda JupyterLab.
# The data is the course copy of mpg.csv, so nothing is installed or downloaded.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# --- Part 2: load the data, drop missing rows, choose features (X) and target (y)
df = pd.read_csv("data/mpg.csv")
print(f"Cars in the file: {len(df)}")
print("Missing values per column:", df.isna().sum()[df.isna().sum() > 0].to_dict())

df = df.dropna()            # drop BEFORE choosing X and y, so both come from the same rows

features = ["cylinders", "displacement", "horsepower", "weight", "acceleration"]
X = df[features]
y = df["mpg"]

print("\n--- Dataset snapshot ---")
print(df[features + ["mpg"]].head())
print(f"\nTotal viable vehicles in dataset: {len(df)}")

# --- Part 3: 80/20 train/test split (random_state=42 as on GAP) and model training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
print(f"\nTraining on {len(X_train)} vehicles...")
print(f"Testing on {len(X_test)} vehicles (hidden during training)...")

model = LinearRegression()
model.fit(X_train, y_train)

print("\n--- Model coefficients (change in MPG per one unit of each feature) ---")
coefficients = pd.DataFrame({"Feature": features, "Coefficient": model.coef_})
print(coefficients.to_string(index=False))

# --- Part 4: predict the hidden test cars and measure accuracy
y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
r2_test = r2_score(y_test, y_pred)

print("\n--- Predictive performance on TEST data ---")
print(f"Root mean squared error (RMSE): {rmse:.2f} MPG")
print(f"Mean absolute error (MAE):      {mae:.2f} MPG")
print(f"Test R-squared (R2):            {r2_test:.4f}")

# The y = x line spans every value on either axis, so no point lies beyond its ends
low = min(y_test.min(), y_pred.min())
high = max(y_test.max(), y_pred.max())

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color="#0072B2")
plt.plot([low, high], [low, high], color="#D55E00", linestyle="--", linewidth=2,
         label="Perfect prediction (y = x)")
plt.title("Predictive accuracy: actual MPG vs predicted MPG")
plt.xlabel("Actual MPG (true values)")
plt.ylabel("Predicted MPG (model guesses)")
plt.legend()
plt.show()

# --- Part 5: residual diagnostics
residuals = y_test - y_pred

plt.figure(figsize=(8, 6))
plt.scatter(y_pred, residuals, alpha=0.7, color="#CC79A7")
plt.axhline(y=0, color="#D55E00", linestyle="--")
plt.title("Residual diagnostic plot (checking for homoscedasticity)")
plt.xlabel("Predicted MPG")
plt.ylabel("Residual error (actual - predicted)")
plt.show()
```

Export with **Kernel → Restart Kernel and Run All Cells**, then **File → Print → Save as PDF**.

---

## 4. Checks you can make

These tell you whether your output is right without giving any answers away.

- [ ] The file has **398** cars; only `horsepower` has missing values (**6** of them); after `dropna` there are **392** cars.
- [ ] The split prints **313** training cars and **79** test cars, which add up to 392. If you see 318 and 80, the missing values were filled in rather than dropped.
- [ ] The coefficient table has **five** rows, one per feature, in the order of `features`.
- [ ] RMSE and MAE are **positive** and in **MPG**, and RMSE is **at least as large as** MAE (it always is).
- [ ] Test R² is **below 1** and printed to four decimals. It is calculated on the **test** cars; say so in your answer.
- [ ] The actual-versus-predicted plot has **79** points, and the dashed line runs corner to corner at 45 degrees (equal scales on both axes would put it exactly on the diagonal).
- [ ] The residual plot has the same **79** points, scattered above and below the zero line. A residual **above** zero means the model **under**-predicted that car.
- [ ] Your weight answer gives the change in MPG for **1 pound** and for **1,000 pounds**, with the words "on average" and "holding the other features constant".
- [ ] Your MAE answer is a sentence with units that an engineer would understand, not a bare number.
- [ ] Your residual answer describes **the shape you see** (a random cloud, a curve, or a funnel) and connects it to what the model may be missing.

A classmate on the other route should get **the same** numbers to the printed decimals. If you do not, see the first two pitfalls below.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| `ValueError: Input X contains NaN` when fitting | Six cars have no `horsepower`. `LinearRegression` cannot use a row with a gap. Either `dropna()` was skipped, or it ran **after** `X = df[features]`, so X still holds the old rows | Run `df = df.dropna()` **before** defining X and y, as GAP does. Check with `print(len(X), len(y))`: both must be 392 |
| `ValueError: Found input variables with inconsistent numbers of samples: [392, 398]` | The missing rows were dropped from X but not from y (for example `X = df[features].dropna()` with `y = df["mpg"]`) | Drop from the whole data frame first, then take X and y from it |
| Your numbers differ from everyone else's, with 398 cars | The missing horsepower values were filled in (for example with the mean) instead of dropped. That keeps 398 rows, so `random_state=42` produces a **different** split | Follow GAP: drop the rows. Filling in is a reasonable choice in general, but not for this lab |
| Your numbers differ, with 392 cars | `random_state` or `test_size` was changed, or cells were run out of order | Use `test_size=0.20, random_state=42`, restart the kernel and run from the top |
| The dashed line does not reach some points in the actual-versus-predicted plot | GAP draws the line from `y.min()` to `y.max()`, the smallest and largest **actual** MPG in the whole data. A **prediction** can fall outside that range, and then its point sits beyond the end of the line | Not an error, and the numbers are unaffected. To draw the line across everything, use the minimum and maximum of both `y_test` and `y_pred`, as Route B does |
| The dashed line is tiny, or far from the points | `y` no longer holds MPG: it was overwritten later (for example by `y = np.log(df["mpg"])` in an extra task, or `y = y_pred`), and the plot cell was run again | Keep `y` for the target only and give new things new names (`log_y`, `y_pred`). Restart the kernel and run from the top |
| `TypeError: got an unexpected keyword argument 'squared'` | Many online examples and AI assistants write `mean_squared_error(..., squared=False)` for RMSE. Recent scikit-learn versions removed that option | Use `np.sqrt(mean_squared_error(y_test, y_pred))` as GAP does, or `root_mean_squared_error` from `sklearn.metrics` |
| `ModuleNotFoundError` for `sklearn` or `seaborn` in Try JupyterLab | The `%pip install` line did not run in this session, or is still running | Run the first cell again and wait for it to finish; every new session needs it |
| The data will not download, or `open_url` fails | GitHub is blocked or slow on your network | Use Route B with `data/mpg.csv`, or see [If the data will not download](../setup.md#if-the-data-will-not-download) |
| `%pip install` fails in Anaconda | It needs the internet, and Anaconda already includes these packages | Leave the `%pip` line out; Route B does |
| `ValueError: could not convert string to float: 'usa'` | `origin` was added to the features; it is text, and `LinearRegression` needs numbers | Only in an extra task: turn it into 0/1 dummy columns first (Day 4, Part 4) |
| A coefficient's sign surprises you | Cylinders, displacement, horsepower and weight overlap heavily, so one coefficient can absorb another's effect (multicollinearity, Day 4, Part 9) | Answer the question that is asked, about **weight**. Read a coefficient as "holding the other four constant" |
| You read `acceleration` as "faster is higher" | It is the **time** in seconds from 0 to 60 mph, so a larger value is a slower car | Say "per extra second of 0–60 time" in any sentence about it |
| The PDF cuts off a chart | The print scale | Print in landscape or reduce the scale in the print dialog |

---

## 6. Beyond the lab

Optional, not graded. Try these in the same notebook, below your answers, **after** you have answered GAP's questions, and keep GAP's outputs unchanged above them. Give every new model and every new target its own variable names so that GAP's `model`, `y` and `y_pred` are not overwritten.

1. **Add model year.** Refit with `model_year` as a sixth feature on the same split. Compare test RMSE, MAE and R² with GAP's model, and write one sentence on what the `model_year` coefficient means.
2. **Add origin.** Turn `origin` into dummy columns with `pd.get_dummies(..., drop_first=True)`, add them, and refit. Which origin is the reference category, and what does each dummy coefficient compare?
3. **A log transform.** Fit a model of `np.log(mpg)` on the same features. Back-transform the test predictions with `np.exp` before computing RMSE and MAE in MPG, so the comparison with GAP's model is fair. Draw its residual plot. Does the pattern change?
4. **Residuals against each feature.** Plot the test residuals of GAP's model against each of the five features in turn (a 2 × 3 grid of small scatter plots with a zero line works well). Which feature, if any, shows a pattern, and what would you add to the model because of it?
5. **A one-feature baseline.** Fit a model on `weight` alone and compare its test errors with GAP's five-feature model. How much do the other four features add? Relate your answer to multicollinearity.
6. **Variance inflation factors.** Compute the VIF of each of the five features with the `1 / (1 - R²)` definition from Day 4. Which coefficients would you warn a manager not to read on their own?
7. **A different split.** Rerun GAP's model with `random_state` set to 1, 2, 3 and 4. How much do the test measures move? What does that say about reporting them to four decimals?
8. **Write it for an engineer.** In three sentences, tell the car maker how accurate the model is, with units, where it is least reliable, and one thing it cannot tell them (hint: Day 4, Part 12 on causation).

---

## 7. Submission

| File | Contents |
|---|---|
| **Final file** | The executed notebook as one PDF: data snapshot and row count, split counts, coefficient table, the three measures, both plots and the Markdown cell with your answers, named `YourLastName_DATA300_AppliedLab5.pdf` |

1. Run **Kernel → Restart Kernel and Run All Cells** (Route B) or run every cell from the top (Route A), and check that every output and chart is visible.
2. Export with **File → Print → Save as PDF**, *Background graphics* ticked. If your instructor asks for HTML instead, use **File → Save and Export Notebook As… → HTML**. If you wrote answers in a separate document, combine the PDFs **offline** as described in [Combining PDFs without internet](../setup.md#combining-pdfs-without-internet).
3. Open the PDF and check every part is present and readable.
4. Upload it to **Applied Lab 5** on **GAP** and submit before **Tuesday 17 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)).
