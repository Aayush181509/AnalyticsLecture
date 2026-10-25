# Setup

<p class="lead">
Get the three course tools working before the first day: JupyterLab for Python, Tableau Desktop and Microsoft Excel. For Python there are two routes. Route A is the browser version GAP describes; Route B runs on your own laptop and works without internet.
</p>

---

## What you need

| Tool | Used for | How to get it |
|---|---|---|
| **JupyterLab (Python)** | Activity 1, Labs 1, 3, 4 and 5, Assignments 1 and 2, the capstone | Route A: Try JupyterLab in a browser. Route B: Anaconda on your laptop |
| **Tableau Desktop** | Activity 1, Lab 2, Lab 7, the capstone | Free student licence |
| **Microsoft Excel** | Labs 6 and 7, Assignment 3, the capstone | Your own copy or the lab PCs |
| **A PDF tool** | Every submission | Word, macOS Preview or Adobe Acrobat (see below) |

Each guide page says which tool a task needs.

---

## Python, Route A: Try JupyterLab (as on GAP)

GAP's instructions use **Try JupyterLab**, a version of JupyterLab that runs entirely in your web browser.

1. Open `https://jupyter.org/try-jupyter/lab/` in Chrome, Edge or Firefox.
2. In the Launcher, under **Notebook**, click **Python (Pyodide)**.
3. Rename the notebook straight away (right-click its tab → **Rename Notebook…**) with the name the task asks for.

### How Try JupyterLab differs from ordinary Python

Try JupyterLab runs Python through **Pyodide**: Python translated so that a browser can run it, inside the tab itself. That has three consequences.

| On an ordinary computer | In Try JupyterLab |
|---|---|
| Packages are installed once and stay installed | Start each session with a `%pip install …` cell for the packages the task uses. A package installed yesterday, or in another tab, is not there today |
| `pd.read_csv("https://…")` downloads a file directly | The browser has to fetch the file, so GAP's code wraps the address with `open_url(...)` from `pyodide.http` |
| Files and results stay on your disk | Python's memory ends when the tab closes. The notebook file is kept only in that browser's storage, which is cleared with the browsing data and is not on any other computer |

> **Save your work out of the browser, every time**
>
> Before you close the tab: run every cell, export a PDF (**File → Print → Save as PDF**), and download the notebook (right-click it in the file browser → **Download**). Treat anything left only in the browser as lost.

### If the data will not download

GAP's code fetches datasets from GitHub, which is often slow or blocked in mainland China. If a cell hangs or ends in a network error:

1. Ask your facilitator for the course folder (Route B below) and take the CSV file you need from its `data` folder.
2. Drag the CSV file into Try JupyterLab's file browser on the left.
3. Load it by name instead of by address, for example `pd.read_csv("penguins.csv")`.

If that also fails in your browser, switch to Route B for the rest of the task. The results are the same.

---

## Python, Route B: Anaconda on your laptop (offline)

Route B runs the same Python on your own computer. It does not need the internet once it is installed, and your work is saved as ordinary files.

### 1. Install Anaconda

1. Download the **Anaconda Distribution** installer for Windows or macOS and run it with the default options. (Your facilitator can supply the installer on a USB drive if downloads are slow.)
2. Open **Anaconda Navigator** and click **Launch** under **JupyterLab**, or type `jupyter lab` in Anaconda Prompt (Windows) or Terminal (macOS).
3. JupyterLab opens in a browser tab, but it runs on **your computer**.

Anaconda already includes pandas, matplotlib, seaborn, statsmodels, scikit-learn and NLTK. You do **not** need any `%pip install` lines in Route B; delete them if you copy code from GAP.

### 2. Copy the course folder

1. Your facilitator gives you the course folder, `DATA300_GAP`, as a zip file or on a USB drive. Copy it to your **Documents** folder and unzip it.
2. Inside are the lecture notebooks and a `data` folder with every dataset the course uses: `penguins.csv`, `diamonds.csv`, `tips.csv`, `mpg.csv`, `datasaurus_dozen.csv` and the NLTK word lists in `nltk_data`.
3. **Keep your own notebooks in the `DATA300_GAP` folder, next to `data`.** Code then loads files with short paths such as `pd.read_csv("data/penguins.csv")`.

### 3. Check that it works

Create a new notebook inside `DATA300_GAP` and run this cell:

```python
import pandas as pd, matplotlib, seaborn, statsmodels, sklearn, nltk

penguins = pd.read_csv("data/penguins.csv")
print("pandas", pd.__version__, "| rows loaded:", len(penguins))
```

If it prints the pandas version and a row count, Route B is ready. A `FileNotFoundError` means the notebook is not in the same folder as `data`; a `ModuleNotFoundError` means Anaconda did not install fully.

### Turning GAP code into Route B code

Each guide page gives the Route B code in full. If you adapt GAP's code yourself, make three changes:

| GAP (Try JupyterLab) | Route B (Anaconda) |
|---|---|
| `%pip install seaborn` | Delete the line |
| `from pyodide.http import open_url` | Delete the line |
| `pd.read_csv(open_url(url))` | `pd.read_csv("data/<file>.csv")` |

---

## Tableau Desktop

1. Go to the **Tableau for Students** page (`https://www.tableau.com/academic/students`) and request a free licence with your **university email address**. You may be asked to prove you are a student.
2. The product key arrives by email. Download **Tableau Desktop**, install it and enter the key.
3. Open Tableau and click **Sample – Superstore** under *Saved Data Sources* on the start page. If a blank sheet opens with the Superstore fields listed on the left, Tableau is ready.

Do this in the pre-class week: verification can take a day or two, and Activity 1 needs Tableau.

---

## Microsoft Excel

Labs 6 and 7, Assignment 3 and the capstone use Excel's **What-If Analysis → Data Table**, `RAND()`, `NORM.INV()` and **Data → Forecast Sheet**. These are built into Excel for Windows and Excel for Mac (Microsoft 365 or Excel 2016 and later). Excel on the web lacks some of them, so use the desktop program or a lab PC. Open Excel once before Day 5 (Tuesday 17 November) to check it starts.

---

## Saving and exporting

| Tool | Save your working file | Export for submission |
|---|---|---|
| JupyterLab | **Ctrl + S** (Cmd + S on macOS). Route A: also download the `.ipynb` | **Kernel → Restart Kernel and Run All Cells**, check every output, then **File → Print** → *Save as PDF* with *Background graphics* ticked |
| Tableau | **File → Save As** a packaged workbook (`.twbx`) | **File → Print to PDF** (choose *Entire workbook* when every sheet is needed); or **Worksheet → Export → Image** and paste the image into Word |
| Excel | **File → Save As** `.xlsx` | **File → Save As → PDF**, or submit the `.xlsx` if the task asks for it |

Always restart and run all before exporting a notebook, so the outputs in the PDF match the code.

---

## Combining PDFs without internet

Several tasks ask for **one** PDF made from two or three parts. Online PDF mergers are often blocked or unreliable, and uploading course work to them is unnecessary. Combine files on your own computer:

- **Word (Windows or macOS):** put your written answers in a Word document, then insert the other parts as pictures on new pages (**Insert → Pictures**). Use screenshots or exported images of the notebook and Tableau sheets. Finish with **File → Save As → PDF**.
- **macOS Preview:** open the first PDF, choose **View → Thumbnails**, drag the next PDF into the sidebar below the last page, repeat, then **File → Export as PDF**.
- **Adobe Acrobat** (the full program, if installed): **Tools → Combine Files**.

Open the final PDF and check that every part is there, in the order the task gives, and that the file has the exact name the task asks for.

---

## Submitting on GAP (Moodle)

1. Open the course on **GAP**, find the item (for example *Activity 1*) and click **Add submission**.
2. Upload the file with the required name and click **Save changes**.
3. If the item has a **Submit assignment** button, click it; until you do, the work stays a draft.
4. Check that the status reads *Submitted for grading* and that the file opens.

Deadlines are **23:59 China Standard Time**. Submit early: GAP can be slow near a deadline.

!!! warning "Only use course data"

    Never use private company, customer or personal data in course work.
