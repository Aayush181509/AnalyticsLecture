# Lab 4: Forecasting

<p class="lead">
Your fourth graded Python lab. You forecast monthly carbon dioxide (CO₂) levels measured at the Mauna Loa Observatory: turn weekly readings into a monthly series, test it for stationarity, hold back the most recent part of the record, fit a seasonal ARIMA (SARIMA) model to the rest, forecast the held-back months, measure the error with RMSE and MAE, answer questions about what you see, and submit one PDF on GAP.
</p>

*Adapted from the DATA 300 GAP course, In-Class Module 1, Lab 4: Forecasting. Written in our own words; follow GAP for the official wording.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Run three blocks of given Python code (load and test for stationarity, split in time order, fit and evaluate SARIMA), then answer four questions in a Markdown cell at the bottom of the notebook |
| **Why** | Before anyone acts on a forecast, it must be shown to work on data it has not seen. The lab's scenario is a climate analyst who must prove a model's accuracy to policymakers by hiding recent history from it and checking its forecasts against what actually happened |
| **CLOs** | CLO 1 (the role of predictive analytics in a business or policy problem), CLO 2 (communicating results with analytical tools), CLO 5 (judging how a model supports a decision). It also practises CLO 4 (time series forecasting) |
| **Weight** | 3% |
| **Deadline** | **Thursday 12 November, 23:59 China Standard Time**, on GAP (worked on in periods 7 and 8 of Day 3) |
| **Before you start** | The [Time series and forecasting](../D3_lecture_forecasting.md) lecture, especially Parts 3, 4, 7, 8 and 9 |

The data is the Mauna Loa CO₂ record that ships with the `statsmodels` package: weekly readings, in **parts per million (ppm)**, from 1958 to 2001, with a few weeks missing.

---

## 2. Route A: Try JupyterLab (as on GAP)

### Part 1: Open and name a notebook

Open Try JupyterLab, start a **Python (Pyodide)** notebook and rename it with the file name GAP gives (your last name, the course code and "AppliedLab4").

### Part 2: Load the data and test for stationarity

Paste GAP's first code block into a cell and run it. In outline, it:

1. installs `statsmodels`, `scikit-learn`, `seaborn` and `matplotlib` into the browser session with `%pip`;
2. imports pandas, numpy, matplotlib, statsmodels, the `adfuller` test and scikit-learn's error functions, and hides warnings;
3. loads the CO₂ data from statsmodels, **resamples** the weekly readings to monthly averages with `resample('ME')`, and fills the gaps by carrying the previous month forward (`ffill`);
4. plots the monthly series;
5. runs the **Augmented Dickey-Fuller (ADF)** test on the whole monthly series and prints its statistic, its p-value and a one-line conclusion.

### Part 3: Train/test split in time order

Paste and run GAP's second block. It keeps the **first 80%** of the months as the training set and the **last 20%** as the test set (no shuffling), prints how many months are in each, and plots the two parts in different colours.

### Part 4: Fit SARIMA and measure accuracy

Paste and run GAP's third block. It fits a **SARIMA** model with the orders GAP gives, using the training data only; forecasts as many months as the test set holds; prints the **RMSE** and **MAE** of those forecasts against the actual test values, in ppm; and plots the end of the training data, the actual test data and the forecast together. The fit takes a while: see *Known pitfalls*.

### Part 5: Answer the questions

Add a **Markdown** cell at the bottom and answer GAP's four questions in full sentences. They cover: the ADF p-value and why it leads to differencing (*d* = 1); why a time-ordered train/test split is more rigorous than fitting on all the data, and what risk it reduces; your MAE and whether that error is excellent, acceptable or poor given the level of the series; and whether the forecast follows both the long-run trend and the yearly up-and-down pattern. Read every value from **your own output**, give units (ppm), and name the output it comes from.

### Part 6: Export and submit

Run everything from the top, then **File → Print → Save as PDF** with *Background graphics* ticked. See *Submission* below.

---

## 3. Route B: offline in Anaconda JupyterLab

Use this route if `%pip install` is slow in Try JupyterLab or the SARIMA fit freezes the browser tab, or if you prefer your own laptop. The CO₂ data ships inside statsmodels, so nothing is downloaded. Create a notebook **inside the `DATA300_GAP` folder**, named as in Route A. Paste the block into one cell, or split it at the `# ---` lines into three cells that match GAP's parts. The questions are the same as in Route A.

Two small differences from GAP's code, neither of which changes any number: the monthly resampling chooses `'ME'` or `'M'` to suit your pandas version, and the charts use colour-blind-safe colours.

```{.python .offline}
# Route B for Lab 4: run offline in Anaconda JupyterLab.
# The CO2 data ships with statsmodels, so nothing is installed or downloaded.
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error, mean_absolute_error

warnings.filterwarnings("ignore")

# --- Part 2: load, resample to monthly, plot, ADF test
dataset = sm.datasets.co2.load_pandas()
df = dataset.data

# pandas 2.2 renamed the month-end alias from 'M' to 'ME'; older versions only know 'M'
major, minor = (int(x) for x in pd.__version__.split(".")[:2])
MONTH_END = "ME" if (major, minor) >= (2, 2) else "M"
print("pandas", pd.__version__, "- monthly alias:", MONTH_END)

df = df.resample(MONTH_END).mean().ffill()

plt.figure(figsize=(10, 4))
plt.plot(df.index, df["co2"], color="#009E73")
plt.title("Monthly CO2 levels (Mauna Loa Observatory)")
plt.ylabel("CO2 (ppm)")
plt.xlabel("Date")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

print("--- Augmented Dickey-Fuller (ADF) test ---")
adf_result = adfuller(df["co2"])
print(f"ADF statistic: {adf_result[0]:.4f}")
print(f"p-value: {adf_result[1]:.4f}")
if adf_result[1] > 0.05:
    print("Conclusion: p-value > 0.05, so the series is NOT stationary.")
else:
    print("Conclusion: p-value <= 0.05, so the series IS stationary.")

# --- Part 3: sequential train/test split (first 80% train, last 20% test)
train_size = int(len(df) * 0.8)
train_data, test_data = df.iloc[:train_size], df.iloc[train_size:]

print(f"Total observations: {len(df)}")
print(f"Training horizon:   {len(train_data)} months")
print(f"Testing horizon:    {len(test_data)} months")

plt.figure(figsize=(10, 4))
plt.plot(train_data.index, train_data["co2"], label="Training data (80%)", color="#0072B2")
plt.plot(test_data.index, test_data["co2"], label="Test data (20%), held back", color="#E69F00")
plt.title("Sequential train/test split")
plt.ylabel("CO2 (ppm)")
plt.xlabel("Date")
plt.legend(loc="upper left")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# --- Part 4: fit SARIMA(1,1,1)(1,1,1,12) on the training data only, forecast the test period
print("Fitting the SARIMA model (this can take 10-60 seconds)...")
model = sm.tsa.statespace.SARIMAX(train_data["co2"], order=(1, 1, 1),
                                  seasonal_order=(1, 1, 1, 12))
sarima_result = model.fit(disp=False)

predictions = sarima_result.get_forecast(steps=len(test_data))
pred_mean = predictions.predicted_mean

rmse = np.sqrt(mean_squared_error(test_data["co2"], pred_mean))
mae = mean_absolute_error(test_data["co2"], pred_mean)
print("\n--- Out-of-sample accuracy ---")
print(f"Root mean squared error (RMSE): {rmse:.2f} ppm")
print(f"Mean absolute error (MAE):      {mae:.2f} ppm")

plt.figure(figsize=(12, 6))
plt.plot(train_data.index[-50:], train_data["co2"].iloc[-50:], label="Recent training data", color="#0072B2")
plt.plot(test_data.index, test_data["co2"], label="Actual test data", color="black")
plt.plot(test_data.index, pred_mean, label="SARIMA forecast", color="#D55E00", linestyle="--")
plt.title("SARIMA forecast against the held-back test period")
plt.ylabel("CO2 (ppm)")
plt.xlabel("Date")
plt.legend(loc="upper left")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
```

Export with **Kernel → Restart Kernel and Run All Cells**, then **File → Print → Save as PDF**.

---

## 4. Checks you can make

These tell you whether your output is right without giving any answers away.

- [ ] The monthly series starts in **1958** and ends in **2001**, and its plot shows a rising line with a regular yearly wiggle. The y-axis is in ppm.
- [ ] The ADF output prints **two numbers** (a statistic and a p-value) and a conclusion that matches the p-value and the 0.05 rule.
- [ ] Training months + testing months = total observations, and the training months are about **four times** the testing months.
- [ ] On the split chart, the training data comes **first** and the test data **after**, with no gap and no overlap.
- [ ] The forecast covers exactly the test period: the dashed line starts where the training data ends.
- [ ] RMSE and MAE are **positive**, in **ppm**, and RMSE is **at least as large as** MAE (it always is).
- [ ] Your MAE answer compares the error with the **level** of the series (for example as a percentage of a typical value), not just as a bare number.
- [ ] Your answer on differencing states the ADF test's **null hypothesis** and connects the p-value to *d* = 1.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| `ValueError: Invalid frequency: ME` | GAP's `resample('ME')` needs **pandas 2.2 or later**; older Anaconda versions have pandas 2.0 or 2.1 | Check with `print(pd.__version__)`. On an older version, use `resample('M')` (the old name for the same month-end rule). Route B chooses automatically. On pandas 2.2 or later, `'M'` still works but prints a deprecation warning |
| `MissingDataError` from `adfuller`, or the SARIMA fit fails with NaN | `.ffill()` was left off: some months have no weekly readings, so their monthly average is empty | Keep `.ffill()` after `.mean()`, exactly as GAP does |
| `ModuleNotFoundError: No module named 'statsmodels'` in Try JupyterLab | The `%pip install` line did not run in this session, or is still running | Run the first cell again and wait for it to finish; every new Try JupyterLab session needs it |
| The `%pip install` cell takes several minutes | statsmodels and scikit-learn are large packages to load into the browser | Wait; do not run it twice. If it never finishes, switch to Route B |
| The SARIMA cell runs for a long time (`[*]` stays for a minute or more) | A seasonal model with four seasonal and non-seasonal terms is slow to fit, especially in the browser | Run it **once** and wait. GAP says 10–20 seconds on a fast machine; in Try JupyterLab it can take several times longer. Do not click Run again while it is busy, and do not close the tab |
| The browser tab freezes or crashes during the SARIMA fit | The browser ran out of memory | Close other tabs and run again from the top, or use Route B |
| `ConvergenceWarning` or frequency warnings appear | The `warnings.filterwarnings("ignore")` line was skipped or run after the model | They are warnings, not errors. Run the import cell first to hide them |
| `TypeError: got an unexpected keyword argument 'squared'` | Some online examples use `mean_squared_error(..., squared=False)`, which recent scikit-learn removed | Use `np.sqrt(mean_squared_error(...))` as GAP does |
| The forecast and actual lines are hard to tell apart | GAP draws the actual test data in orange and the forecast in red, which many colour-blind readers cannot separate | The dashed line style and the legend still identify them; Route B uses black and orange. Your numbers do not change |
| Your numbers differ slightly from a classmate's | Different versions of pandas or statsmodels, or the cells were run out of order | Restart the kernel and run from the top. Report your own output; small differences in the last decimal are normal across versions |
| The PDF cuts off the last chart | The print scale | Print in landscape or reduce the scale in the print dialog |

---

## 6. Beyond the lab

Optional, not graded. Try these in the same notebook after you have answered GAP's questions:

1. Run the ADF test on `df["co2"].diff().dropna()` and on `df["co2"].diff().diff(12).dropna()`. How do the conclusions change, and which part of SARIMA's orders does each difference correspond to?
2. Compute a **seasonal naive** baseline for the test period (each month's forecast is the value 12 months before; you will need the last 12 training months to start) and its MAE. Does SARIMA beat it, and by how much?
3. Add the **MAPE** (`np.mean(np.abs((actual - forecast) / actual)) * 100`) to your error measures. Why is it easy to explain to a policymaker?
4. Draw the forecast's 95% interval with `predictions.conf_int()` and `plt.fill_between`. Does it widen across the test period? How many actual months fall outside it?
5. Fit a simpler SARIMA(0,1,1)(0,1,1,12) and compare its RMSE, MAE and fit time with GAP's model. Which would you recommend, and why?
6. Write two sentences for a policymaker that give your forecast's accuracy in words, with units and a comparison to the level of the series, and one assumption behind it.

---

## 7. Submission

| File | Contents |
|---|---|
| **Final file** | The executed notebook as one PDF: monthly plot, ADF output, split counts and chart, error measures, forecast chart and the Markdown cell with your answers, named `YourLastName_DATA300_AppliedLab4.pdf` |

1. Run **Kernel → Restart Kernel and Run All Cells** (Route B) or run every cell from the top (Route A), and check that every output and chart is visible.
2. Export with **File → Print → Save as PDF**, *Background graphics* ticked. If you wrote answers in a separate document instead, combine the PDFs **offline** as described in [Combining PDFs without internet](../setup.md#combining-pdfs-without-internet).
3. Open the PDF and check every part is present and readable.
4. Upload it to **Applied Lab 4** on **GAP** and submit before **Thursday 12 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)).
