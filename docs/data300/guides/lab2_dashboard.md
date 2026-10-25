# Lab 2: Dashboard

<p class="lead">
Your first graded Tableau lab. You build three sheets from Tableau's built-in Sample – Superstore data (a monthly sales trend, a filled map of profit by state and a bar chart of sales by sub-category coloured by profit), combine them into one interactive executive dashboard in which clicking a state filters the other two charts, answer GAP's questions about what the dashboard shows, and submit one PDF on GAP.
</p>

*Adapted from the DATA 300 GAP course, In-Class Module 1, Lab 2: Dashboard Creation. Written in our own words; follow GAP for the official wording.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Build three worksheets in Tableau Desktop, assemble them on a dashboard with the map as a filter, use the dashboard to answer GAP's questions in a separate document, and submit the answers and the dashboard as one PDF |
| **Why** | Regional managers in the scenario cannot see their sales trend or which products lose money in their state. A linked dashboard lets each manager answer both questions with one click. Building one teaches the difference between a set of static charts and an interactive view |
| **CLOs** | CLO 2 (visualisation tools that communicate user-centred analytics), CLO 1 (descriptive analytics to evaluate performance), CLO 3 (organising information with computational tools) |
| **Weight** | 3% |
| **Deadline** | **Wednesday 11 November, 23:59 China Standard Time**, on GAP (worked on in periods 7 and 8 of Day 2) |
| **Before you start** | The two Day 2 lectures: [Visualising and communicating data](../D2_lecture_visual_communication.md) and [Tableau concepts and dashboards](../D2_lecture_tableau_dashboards.md). Tableau Desktop installed and activated ([setup](../setup.md#tableau-desktop)) |

!!! note "Your Superstore may differ from your neighbour's"

    Sample – Superstore ships inside Tableau Desktop, and Tableau has changed it between versions: field names (for example **State** or **State/Province**, **Country** or **Country/Region**), the range of order years, and therefore the totals. That is expected. Build the dashboard from the Superstore in **your** Tableau, read every answer from **your own** dashboard, and if a field name in GAP's steps does not exist, use the equivalent field you have.

---

## 2. Route A: Tableau Desktop (as on GAP)

### Part 1: Connect to the data

Open Tableau Desktop and click **Sample – Superstore** under *Saved Data Sources* on the start page. A blank Sheet 1 opens with the Superstore fields in the Data pane.

### Part 2: Build the three sheets

**Sheet 1, Monthly Sales Trend.** Rename the tab. Put **Order Date** on Columns. Open the pill's menu and choose the **second** *Month* entry, the one with a year in its example (such as "May 2015"): it is in the lower list of date **values**, and the pill turns **green** (continuous). Put **Sales** on Rows. You should see one line running across all the years, not twelve points. (Why: [Tableau lecture, Part 2](../D2_lecture_tableau_dashboards.md#discrete-blue-and-continuous-green).)

**Sheet 2, Profitability by State.** New worksheet, renamed. Double-click the state field (**State** or **State/Province**). Tableau draws a dot per state. On the Marks card, change *Automatic* to **Map** to make a filled map, then drag **Profit** onto **Color**. Profit is shown on a diverging palette: by default blue for profit and orange for loss.

**Sheet 3, Sales by Sub-Category.** New worksheet, renamed. **Sub-Category** on Rows, **Sales** on Columns, then the **Sort Descending** button on the toolbar. Drag **Profit** onto **Color**: now bar length shows sales and colour shows profit.

### Part 3: Assemble the dashboard

1. Click **New Dashboard** (next to New Worksheet at the bottom).
2. In the *Size* menu on the left, choose **Automatic**, as GAP asks. (Your version may start from *Fixed size* rather than *Range*; choose Automatic either way.)
3. Drag the map to the top half, the trend to the bottom left and the sub-category bars to the bottom right.
4. Click the map once to select it, then click its **Use as Filter** icon (a small funnel on the map's border, top right). Clicking a state now filters the other two charts.

### Part 4: Answer the questions

Open a Word document and answer GAP's questions in full sentences. They come in three groups:

- **Baseline (nothing selected):** the sub-category with the most sales nationally and whether it is profitable; two states operating at a loss.
- **Interactive (click a state):** for one named state, the sub-category with the largest loss and the month and year of an unusual spike in sales; for a second named state, whether its top three sub-categories by sales match the first state's.
- **Critical thinking:** why colouring the sales bars by profit is more useful than colouring them by sales, and what it reveals that a plain bar chart hides.

Name the sheet each answer comes from, give the values you read (with units: US dollars, months and years) and say how you read them (tooltip, colour, bar order).

### Part 5: Export

Clear any selection on the map, then **File → Print to PDF**, *Active Sheet* (with the dashboard as the active sheet). Save your answers as a PDF too, and combine the two files. See *Submission* below.

---

## 3. Route B: if Tableau Desktop is not working

There is **no Python route for this lab**, and that is deliberate. The graded product is a working Tableau dashboard; a Python chart would not show that skill, and Superstore is not part of the course folder (it comes with Tableau, in a version that differs between installations). An offline Python copy would give different numbers and could not be graded against your own Tableau.

If Tableau does not work on your laptop, in order of preference:

1. **Activation problems:** Tableau Desktop runs as a free **14-day trial** without a product key. Choose the trial, do the lab, and enter the student key when it arrives. Sample – Superstore is included in the trial.
2. **No laptop or installation fails:** use a lab PC with Tableau Desktop, or pair with a classmate to build it on their machine, then rebuild it on your own before the deadline. Your submission must be your own work.
3. **Still stuck:** tell your facilitator during period 7, not after the deadline.

To practise the same ideas without Superstore, the [Tableau lecture](../D2_lecture_tableau_dashboards.md) builds a linked three-view dashboard in Python on a synthetic bookshop chain (Part 8). Its facilitator note also shows how to save that data as a CSV, which you can open in Tableau with **Connect → To a File → Text file** for extra practice. Practice data does not replace the lab.

---

## 4. Checks you can make

These tell you whether your dashboard is right without giving any answers away.

- [ ] The trend sheet shows **one continuous line** across several years, with a **green** month pill, not twelve points or twelve bars.
- [ ] The map is **filled** (states shaded, not dots), and the colour legend runs from orange through to blue across zero.
- [ ] The sub-category bars are **sorted** longest first, and their colours vary with profit.
- [ ] On the dashboard, clicking a state makes the trend and the bars **change**; clicking the state again (or pressing **Esc**) brings back the national view.
- [ ] **Dashboard → Actions** lists one filter action with the map as its source.
- [ ] Your PDF shows the **national** view (no state highlighted) and all three charts are readable.
- [ ] Every answer names the chart it comes from and gives values with units. For the loss questions, you checked the value in the **tooltip** (a negative profit), not only the shade.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| No field called **State**, or no **State/Province** | Superstore's field names differ between Tableau versions | Use whichever state field your Data pane shows (**State** or **State/Province**); the steps are the same |
| Double-clicking the state field gives a list, or a map with no states | The field does not have a geographic role, or the country is not recognised | Right-click the state field → **Geographic Role → State/Province**. If an "unknown" indicator appears at the bottom right of the map, click it and choose **Edit Locations**, with the country set to the United States |
| The map shows dots, not shaded states | The mark type is still *Automatic* (a symbol map) | On the Marks card, open the mark-type menu and choose **Map** (the filled map) |
| The trend shows twelve points, or the pill is blue | The first *Month* entry (a discrete date **part**) was chosen | Open the pill's menu again and choose the **second** *Month* entry, in the lower list, showing a year (for example "May 2015") |
| A state looks orange-ish but its tooltip shows a positive profit, or shades change after clicking a state | The colour range is recomputed from the data in view, and the palette's midpoint may not sit at zero | **Color → Edit Colors → Advanced**, tick **Center** and set it to **0**. Always confirm a "loss" with the tooltip value |
| The sort order seems wrong after clicking a state | The bars were sorted by hand (dragging) rather than with the sort button | Use **Sort Descending** on the toolbar, or the axis sort icon; this sorts by the measure and updates with the filter |
| No *Range* option to change, or the size menu shows *Fixed size* | Newer versions start dashboards at a fixed size | Choose **Automatic** as GAP asks. If the PDF then looks cramped, choose a **Fixed size** such as *Letter landscape* or *A4 landscape* before printing |
| Can't find the filter icon on the map | The map is not selected, or the icon is small | Click once inside the map on the dashboard so a grey border appears; the **Use as Filter** funnel is on that border at the top right (hover to see its name). When on, it is filled in |
| Clicking a state does nothing to the other charts | The filter icon was not switched on, or was switched on for another sheet | Check **Dashboard → Actions**: there should be a filter action with the map as source and the other two sheets as targets. If not, select the map and click **Use as Filter** again |
| The PDF shows only one state's data | A state was still selected when you printed | Click an empty area of the map (the sea, or outside the states) or press **Esc** so nothing is selected, check both charts show national data, then print again |
| **Print to PDF** is missing from the File menu | Some versions and platforms (often macOS) do not have it | Use **File → Print…** and choose *Save as PDF* in the print dialog; or **Dashboard → Export Image…** and paste the image into your Word document |
| The PDF has several pages, or only one sheet | *Print Range* was set to *Entire Workbook*, or the wrong sheet was active | Click the dashboard tab first, then choose *Active Sheet* under *Print Range* |
| GAP mentions "the 5 questions" but lists more | Inconsistent wording | Answer **every** question GAP lists, each under its own number |
| GAP calls the coloured bar chart "dual-axis" | In Tableau, *dual axis* means two measures on two overlaid axes; this chart has one axis plus colour (a **dual encoding**) | Answer the question GAP means: what the second encoding (colour) adds |
| Online PDF merger is blocked or slow | — | Combine the PDFs **offline**: see [Combining PDFs without internet](../setup.md#combining-pdfs-without-internet) |

---

## 6. Beyond the lab

Optional, not graded. Try these after you have submitted:

1. Add **Profit Ratio** as a calculated field, `SUM([Profit]) / SUM([Sales])`, and put it on the map's Color instead of Profit. Which states change colour, and why might a rate be fairer than a total (Day 2 morning lecture, Part 4)?
2. Change the dashboard action from *Filter* to *Highlight* (**Dashboard → Actions → Edit**). When would a manager prefer each?
3. Rewrite each sheet's title as a **message title** that states what the national view shows, with a number where you can ([morning lecture, Part 5](../D2_lecture_visual_communication.md#titles-that-say-the-message)).
4. Add a **KPI text sheet** at the top showing total sales, total profit and profit ratio, and let the map filter it too.
5. Run through the [dashboard design checklist](../D2_lecture_tableau_dashboards.md#dashboard-design-checklist) and fix the two weakest points.

---

## 7. Submission

| File | Contents |
|---|---|
| Answers | Your answers to every GAP question, in full sentences, saved as `Answers_Lab2.pdf` |
| Dashboard | The dashboard, national view, from **File → Print to PDF** (*Active Sheet*), saved as `Tableau_Dashboard_Lab2.pdf` |
| **Final file** | The two combined into one PDF, named `YourLastName_DATA300_AppliedLab2.pdf` |

1. In Tableau, clear the selection on the map and check that the trend and bars show national data.
2. Export the dashboard and your answers as the two PDFs above.
3. Combine them **offline** ([Combining PDFs without internet](../setup.md#combining-pdfs-without-internet)). In Word you can instead paste an exported image of the dashboard below your answers and save once as PDF.
4. Open the final PDF and check that the answers and the full dashboard are present and readable.
5. Upload it to **Applied Lab 2** on **GAP** and submit before **Wednesday 11 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)). Save your workbook as a `.twbx` too, in case your facilitator asks for it.
