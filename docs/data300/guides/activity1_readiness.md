# Activity 1: Readiness self-check

<p class="lead">
A short diagnostic before the course starts: run a ready-made Python analysis of the Palmer Penguins data, build two Tableau charts on the Superstore sample, answer five questions, and submit one combined PDF on GAP.
</p>

*Adapted from the DATA 300 GAP course, Pre-In Class Module, Activity 1. Written in our own words; follow GAP for the official wording.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Run a given Python script in JupyterLab, answer three questions about its output; build two Tableau charts, answer two questions; combine everything into one PDF |
| **Why** | It proves your tools work before the intensive days, when a setup problem would cost a graded lab, and it shows you where your analytics vocabulary needs work |
| **CLOs** | CLO 1 (kinds of analytics), CLO 2 (visual tools), CLO 3 and CLO 4 (the computing groundwork for later labs) |
| **Weight** | 4% |
| **Deadline** | **Monday 9 November, 23:59 China Standard Time**, on GAP |
| **Before you start** | Read the [setup page](../setup.md); work through the [Python and Jupyter refresher](../D0_lecture_python_jupyter_refresher.md) |

You do not write new code for the Python part. The aim is to run code correctly, read its output and describe what you see.

---

## 2. Route A: Try JupyterLab and Tableau (as on GAP)

### Part 1: Open a notebook

Open Try JupyterLab, start a **Python (Pyodide)** notebook and rename it with the file name GAP gives (your last name, the course code and "Self_Check").

### Part 2: Run the script

Paste GAP's single code block into one cell and run it with **Shift + Enter**. In outline, the script:

1. installs seaborn into the browser session with `%pip`;
2. imports pandas, seaborn and matplotlib, and `open_url` from `pyodide.http`;
3. loads the penguins CSV from the seaborn-data repository on GitHub;
4. shows the first five rows and the summary statistics table (`describe()`);
5. draws a **scatter plot** of body mass against flipper length, coloured by species;
6. draws a **box plot** of body mass by island, split by sex.

If the data load hangs, see *Known pitfalls* below.

### Part 3: Answer the three Python questions

GAP asks about the summary statistics table (a value from the body mass column), the overall pattern in the scatter plot, and which species sits highest in it. Read each answer from **your own output**, write it in a sentence, and say which table or chart it comes from.

### Part 4: Export the notebook

Check that both tables and both charts are visible, then **File → Print → Save as PDF** with *Background graphics* ticked.

### Tableau: claim the licence and build two sheets

1. Claim the student licence, install Tableau Desktop and activate it ([setup](../setup.md#tableau-desktop)).
2. Open **Sample – Superstore** from *Saved Data Sources*.
3. **Sheet 1:** a horizontal bar chart of total **Sales** for each **Category** (Category on Rows, Sales on Columns). Sorting the bars is optional but helps.
4. **Sheet 2:** a map of **Profit** by state (double-click the state field, then drag Profit to **Color** on the Marks card). Blue means profit, orange means a loss.
5. Answer GAP's two Tableau questions: the category with the highest sales, and at least one state making a loss.
6. **File → Print to PDF**, *Entire workbook*, so both sheets are included.

---

## 3. Route B: offline in Anaconda JupyterLab

Use this route if Try JupyterLab will not load the data, or if you prefer to work on your own laptop. It follows the same steps as GAP's script but loads the bundled copy of the data, so there is nothing to install or download. Create a notebook **inside the `DATA300_GAP` folder** (next to `data`), paste this into one cell and run it. The questions and the Tableau part are exactly the same as in Route A.

```{.python .offline}
# Route B for Activity 1: run offline in Anaconda JupyterLab.
# The penguins file comes from the course folder, so nothing is installed or downloaded.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)   # show every column when printing

# Read the bundled penguins table
df = pd.read_csv("data/penguins.csv")
print("Rows and columns:", df.shape)

# A first look: five rows, then the numeric summary
print("\nFirst five rows:")
print(df.head())
print("\nSummary of the numeric columns:")
print(df.describe())

# Chart 1: scatter of flipper length (x) and body mass (y), coloured by species
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g",
                hue="species", palette="deep")
plt.title("Flipper length and body mass of each penguin, by species")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.show()

# Chart 2: box plot of body mass on each island, one box per sex
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="island", y="body_mass_g", hue="sex", palette="pastel")
plt.title("Spread of body mass on each island, female and male")
plt.xlabel("Island")
plt.ylabel("Body mass (g)")
plt.show()
```

In JupyterLab you may replace the `print(df.head())` and `print(df.describe())` lines with `display(df.head())` and `display(df.describe())` for nicer tables; the numbers are the same. Export with **Kernel → Restart Kernel and Run All Cells**, then **File → Print → Save as PDF**.

---

## 4. Checks you can make

These tell you whether your output is right without giving any answers away.

- [ ] The data has **344 rows and 7 columns**: `species`, `island`, three body measurements, `body_mass_g` and `sex`.
- [ ] In the summary table, the **count** row is lower than 344 for the measurement columns. Some penguins have missing measurements, and `describe()` quietly leaves them out. That is expected.
- [ ] `describe()` lists only the four **numeric** columns. Species, island and sex do not appear, because they are text.
- [ ] The scatter plot has **three colours**, one per species, and a legend.
- [ ] The box plot has **three islands** along the bottom and **two boxes** (male and female) on each where both sexes were measured.
- [ ] Your answers say which table or chart each one comes from, and the body mass answer has its unit (grams).
- [ ] In Tableau, Sheet 1 has **three bars** (one per category) and Sheet 2 shows a map of the United States with the states coloured on a blue–orange scale.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| The cell hangs or ends with a network error | GitHub is slow or blocked | Drag `penguins.csv` from the course folder into Try JupyterLab's file browser and use `pd.read_csv("penguins.csv")` in place of the `open_url` line, or switch to Route B |
| `ModuleNotFoundError: No module named 'seaborn'` in Try JupyterLab | The `%pip install` line did not run in this session | Run the whole cell again from the top; every new Try JupyterLab session needs it |
| `ModuleNotFoundError: No module named 'pyodide'` in Anaconda | GAP's browser-only code was pasted into Route B | Use the Route B code above, which has no `pyodide` line |
| `FileNotFoundError: data/penguins.csv` | The notebook is not in the `DATA300_GAP` folder | Save the notebook inside `DATA300_GAP`, next to `data`, and run again |
| A `UserWarning` mentioning `palette` or missing values | seaborn is telling you about rows it skipped | Not an error; your charts are still correct |
| Charts print in grey or are missing from the PDF | *Background graphics* was off, or the cells were not run before printing | Tick *Background graphics*; restart and run all, then print |
| The notebook vanished from Try JupyterLab | The browser's storage was cleared, or you used another browser | Always export the PDF and download the `.ipynb` before closing the tab |
| No field called **State/Province** in Tableau | Older Tableau versions call it **State** | Use whichever state field your version shows |
| The map shows only a few dots, or none | Tableau did not recognise the field as geographic | Right-click the state field → **Geographic Role → State/Province**; check the country is the United States |
| **Print to PDF** is missing from the File menu | Some Tableau versions on macOS | Use **File → Print** and choose *Save as PDF*, or export each sheet as an image and paste it into Word |
| GAP's instructions give two different names for the notebook PDF, and mention both a Markdown cell and a Word document for answers | Inconsistent wording | The intermediate names do not matter once the files are merged. What counts is one PDF containing all five answers, the notebook output and the Tableau sheets, named as GAP's final instruction says. Ask your facilitator if unsure |

---

## 6. Beyond the activity

Optional, not graded. Try these in the same notebook if you finish early:

1. Count the missing values in every column with `df.isnull().sum()`. Which column has the most, and why might sex be harder to record than a measurement?
2. Make a table of how many penguins of each species were measured on each island with `pd.crosstab(df["island"], df["species"])`. Does every species live on every island? What does that mean for comparing islands in the box plot?
3. Plot bill length against bill depth, first without colour, then with `hue="species"`. Describe how the overall pattern changes once species is shown. (This is a preview of confounding, from Day 1.)
4. In Tableau, add **Profit** to the colour of the Sales by Category bars. Is the category with the most sales also the most profitable?

---

## 7. Submission

| File | Contents |
|---|---|
| Answers | Your five answers in full sentences, each naming the table or chart it comes from |
| Notebook PDF | The executed notebook with both tables and both charts visible |
| Tableau PDF | Both sheets (*Entire workbook*) |
| **Final file** | The three parts combined, answers first, named `YourLastName_DATA300_Week1_Readiness.pdf` |

1. Combine the three PDFs **offline** with Word, macOS Preview or Acrobat, as described in [Combining PDFs without internet](../setup.md#combining-pdfs-without-internet).
2. Open the combined file and check that all three parts are present and readable.
3. Upload it to **Activity 1** on **GAP** and submit before **Monday 9 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)).
