# Day 2 lab: Applied Lab 2 — Dashboard creation

<p class="lead">
Build an interactive executive dashboard in Tableau from three worksheets (a monthly sales trend, a profit map and a sub-category bar chart), connect them with a filter action, and use the dashboard to answer five business questions for regional managers.
</p>

*Adapted from the DATA 300 syllabus, Applied Lab 2 (Dashboard creation). Instructions rewritten for this classroom.*

> **Graded work: Applied Lab 2 (3%, CLO 1, 2 and 3)**
>
> - **Tools:** Tableau Desktop (student licence) with the built-in **Sample – Superstore** data, and Word (or another editor that saves PDF).
> - **Hand in:** one PDF, `YourLastName_DATA300_AppliedLab2.pdf`, uploaded to **GAP (Moodle)**.
> - **Deadline:** 23:59 China Standard Time on **Wednesday 11 November**, unless your facilitator says otherwise.

| Part | What you do | Level |
|---|---|---|
| 1 | Connect to the data | Core (graded) |
| 2 | Build three worksheets | Core (graded) |
| 3 | Assemble the interactive dashboard | Core (graded) |
| 4 | Answer five business questions | Core (graded) |
| 5 | Export, combine and submit | Core (graded) |
| 6 | Improve the design | Stretch (optional) |
| 7 | Add a second action | Challenge (optional) |

---

## The business problem

You are an analytics consultant for a national retail chain, **Superstore**. Its regional managers say two things are hard to see in their current reports:

1. how **their own state's** sales are moving from month to month, and
2. which **product sub-categories** make or lose money in their state.

Your job is to build one interactive **Executive Summary Dashboard**. A manager clicks their state on a map, and the other charts immediately show that state's monthly sales trend and its sub-categories, coloured by profit.

This is this morning's dashboard design in practice: one audience (regional managers), one decision (which products to look at), a few views, and an action that filters every view.

---

## Before you start

1. Open **Tableau Desktop**. If it asks for a licence, use your student licence key.
2. On the start page, check that **Sample – Superstore** appears under **Saved Data Sources**. If it does not, ask your facilitator for the course copy of the Superstore file; then connect with **Connect → To a File → Microsoft Excel** and drag the **Orders** sheet onto the canvas.
3. Make a folder for this lab, for example `Lab2`, to keep your files together.

> **Your numbers may differ from your neighbour's**
>
> Tableau ships different versions of Sample – Superstore with different releases (different years, and sometimes Canadian provinces as well as US states). Answer from **your** dashboard. If a field is called *State/Province* instead of *State*, use that; the steps are the same.

---

## Part 1: Connect to the data (Core)

1. On the start page, under **Saved Data Sources**, click **Sample – Superstore**.
2. Tableau opens a blank worksheet called **Sheet 1**. The Data pane on the left lists the fields. You are connected.

> **Check:** you can see **Order Date**, **State** (or *State/Province*), **Sub-Category**, **Sales** and **Profit** in the Data pane.

---

## Part 2: Build three worksheets (Core)

A dashboard is assembled from separate worksheets. Build and name each one first.

### Sheet 1: Monthly Sales Trend (a line chart)

1. **Rename** the sheet: right-click the **Sheet 1** tab at the bottom → **Rename** → type `Monthly Sales Trend`.
2. Drag **Order Date** from the Data pane to the **Columns** shelf. Tableau shows a blue pill, `YEAR(Order Date)`: one column per year.
3. Right-click that pill. The menu shows two lists of date options. In the **second** list (the continuous date values, which show an example such as *May 2015*), choose **Month**. The pill turns **green**: the dates now form one continuous timeline, month by month.
4. Drag **Sales** to the **Rows** shelf. A line chart of total sales per month appears.

> **Check:** the pill on Columns is green and reads `MONTH(Order Date)`; the x-axis is a timeline across several years, not twelve month names.

### Sheet 2: Profitability by State (a filled map)

1. Click the **New Worksheet** icon (the first small icon to the right of the sheet tabs).
2. Rename the new tab `Profitability by State`.
3. In the Data pane, **double-click State** (or *State/Province*). Tableau draws a map with one dot per state.
4. On the **Marks** card, open the mark-type dropdown (it says **Automatic**) and choose **Map**. Each state is now filled.
5. Drag **Profit** onto **Color** on the Marks card. Tableau colours states on a diverging scale: **blue for profit, orange for loss**.

> **Check:** most states are blue, and a few are orange. If the map is empty or shows "unknown" locations, click the grey **unknown** indicator at the bottom right of the map and ask your facilitator.

### Sheet 3: Sales by Sub-Category (a bar chart coloured by profit)

1. Create another **New Worksheet** and rename it `Sales by Sub-Category`.
2. Drag **Sub-Category** to **Rows**.
3. Drag **Sales** to **Columns**. You see horizontal bars.
4. Click the **Sort Descending** button in the toolbar so the biggest sub-category is at the top.
5. Drag **Profit** onto **Color** on the Marks card. Now the **length** of each bar is sales and its **colour** is profit.

> **Check:** 17 bars, sorted from largest to smallest sales, most of them blue and a few orange.

---

## Part 3: Assemble the interactive dashboard (Core)

1. Click the **New Dashboard** icon (the second small icon next to the sheet tabs).
2. In the **Size** section on the left, change the size setting to **Automatic** so the dashboard fills the screen.
3. Under **Sheets** on the left you see your three worksheets. Drag them onto the canvas:
    - **Profitability by State** across the **top half**;
    - **Monthly Sales Trend** in the **bottom left**;
    - **Sales by Sub-Category** in the **bottom right**.
4. **Make the map a filter.** Click once on the map inside the dashboard so a grey border appears around it. At the top right of that border, click the small **funnel** icon (**Use as Filter**). It changes colour when it is on.
5. Test it: click **Texas** on the map. The trend and the bar chart should change to show Texas only. Click Texas again (or press **Esc**) to clear the selection.

> **Check:** clicking any state changes both bottom charts; clearing the selection brings back the national totals.

Rename the dashboard tab to `Executive Summary Dashboard`, then **save** your work: **File → Save As** → *Tableau Packaged Workbook* (`.twbx`) in your Lab2 folder.

---

## Part 4: Answer the business questions (Core)

Use your dashboard to answer these questions in a **Word document** (one or two sentences each, in full sentences). Put your name and student ID at the top.

### National view (no state selected)

**Question 1.** Looking at the whole country, which sub-category has the **highest total sales**? Is it profitable? (Is its bar blue or orange?)

**Question 2.** On the national map, name **two states** that make an overall **loss** (coloured orange).

### Using the dashboard filter

**Question 3.** Click **Texas** on the map.

- (a) In *Sales by Sub-Category*, which sub-category makes the **largest loss** in Texas (the darkest orange)?
- (b) In *Monthly Sales Trend*, in which **month and year** did Texas have an unusually large **spike** in sales?

**Question 4.** Now click **California**. Compare its *Sales by Sub-Category* chart with Texas's. Are the **top three** best-selling sub-categories the same in both states? If not, name California's top three.

### Visual design

**Question 5.** Why is it more useful to colour the *Sales by Sub-Category* bars by **Profit** rather than by Sales? What business insight does showing two measures in one chart (length = sales, colour = profit) reveal that a plain sales bar chart would hide?

> **Tip for Question 3(a)**
>
> Hover over a bar to see its exact profit in the tooltip. The darkest orange is the most negative profit, not the shortest bar.

The cell below prints a template for your answers document. Run it, copy the text into Word, and fill it in.


```python
template = """DATA 300 — Applied Lab 2: Dashboard creation
Name: ____________________   Student ID: ____________________

Question 1 (top sub-category nationally; profitable?):

Question 2 (two loss-making states):

Question 3(a) (largest loss in Texas):

Question 3(b) (month and year of the Texas sales spike):

Question 4 (California's top three compared with Texas):

Question 5 (why colour the bars by profit?):
"""
print(template)
```

    DATA 300 — Applied Lab 2: Dashboard creation
    Name: ____________________   Student ID: ____________________
    
    Question 1 (top sub-category nationally; profitable?):
    
    Question 2 (two loss-making states):
    
    Question 3(a) (largest loss in Texas):
    
    Question 3(b) (month and year of the Texas sales spike):
    
    Question 4 (California's top three compared with Texas):
    
    Question 5 (why colour the bars by profit?):
    


---

## Part 5: Export, combine and submit (Core)

| Step | What to do | File name |
|---|---|---|
| 1 | In Word, finish your answers to Questions 1–5 and **save as PDF** | `Answers_Lab2.pdf` |
| 2 | In Tableau, open the **Executive Summary Dashboard** tab and **clear any selection** on the map (click an empty area of the map or press **Esc**), so the dashboard shows the national view | |
| 3 | **File → Print to PDF**. Under *Range* choose **Active Sheet** (your dashboard). Click **OK** and save | `Tableau_Dashboard_Lab2.pdf` |
| 4 | **Combine** the two PDFs into one file, answers first, dashboard second | `YourLastName_DATA300_AppliedLab2.pdf` |
| 5 | Upload the single PDF to the **Applied Lab 2** drop-box on **GAP (Moodle)** and click **Submit** | |

> **Combining PDFs without internet**
>
> - **Word:** insert the dashboard as a picture instead (**Dashboard → Export Image** in Tableau, then **Insert → Pictures** in Word on a new page after your answers), and save the whole document as one PDF named `YourLastName_DATA300_AppliedLab2.pdf`.
> - **Mac:** open the answers PDF in Preview, show thumbnails, and drag the dashboard PDF into the sidebar below the last page; then save.
> - **Adobe Acrobat** (if installed): **Tools → Combine Files**.
>
> Whichever method you use, the final PDF must contain your answers and a readable, full dashboard.

---

## Part 6: Improve the design (Stretch, optional)

These steps are not required for the grade, but they apply this morning's principles and make the dashboard better for a manager.

1. **Message titles.** Double-click each sheet title on the dashboard and replace it with a sentence that states the finding, for example what the map shows about losses.
2. **A profit ratio KPI.** Create a calculated field `Profit Ratio = SUM([Profit]) / SUM([Sales])`, format it as a percentage, and add it to the bar chart's **Tooltip** or **Label**.
3. **A scope note.** Add a small **Text** object at the bottom: data (Sample – Superstore), period covered, units, and "click a state to filter".
4. **Accessibility.** Check that the orange–blue colours are kept (they are colour-blind safe) and that each chart also has labels or tooltips that carry the numbers.

---

## Part 7: Add a second action (Challenge, optional)

1. **Dashboard → Actions → Add Action → Highlight.** Source: *Sales by Sub-Category*; target: *Profitability by State*; run on **Select**. What happens to the map when you click *Tables*?
2. Explain in two sentences when a **highlight** action is better for a manager than a **filter** action.

---

## How this lab is marked

The lab is marked out of 100 with the course's lab rubric, then scaled to its 3% weight.

| Criterion | Points | What earns them here |
|---|---|---|
| **CLO 1**: principles of descriptive (and later predictive and prescriptive) analytics | 25 | Correct, specific answers to the descriptive questions (1–4), read from the right view |
| **CLO 2**: visualisation tools that communicate for decisions | 25 | A complete, readable dashboard with all three views and a working filter; a thoughtful answer to Question 5 |
| **CLO 3**: computational problem-solving to find relationships | 30 | Correct use of the dashboard filter to answer the state-level questions (3 and 4) |
| **Professional formatting** | 10 | One combined PDF, correct file name, name and ID on the answers, dashboard not cut off |
| **Writing** | 10 | Clear, complete sentences with correct terms |

---

## Validation checklist

Before you upload, tick every line:

- [ ] Three worksheets, named `Monthly Sales Trend`, `Profitability by State` and `Sales by Sub-Category`.
- [ ] The trend uses a **continuous** (green) month pill.
- [ ] The map is a filled map coloured by Profit; the bar chart is sorted and coloured by Profit.
- [ ] Clicking a state filters both other views; nothing is selected in the exported PDF.
- [ ] All five questions answered in full sentences, with name and student ID.
- [ ] One PDF named `YourLastName_DATA300_AppliedLab2.pdf`, answers first, uploaded to GAP.
- [ ] Your `.twbx` workbook is saved in case you need to re-export.

---

## Exit ticket

Write one sentence for each, and hand it to your facilitator or post it as instructed:

1. One thing your dashboard shows a regional manager that a table of numbers would not.
2. One design change you would make if the dashboard were for the **chief executive** instead of a regional manager.
