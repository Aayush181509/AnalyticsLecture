# T2 lab: Which segment deserves a closer look, and how are sales moving?

<p class="lead">
Build a segment KPI table in Tableau that reconciles with its totals, find out why a colleague's profit ratio is wrong, and add monthly growth figures that keep their comparison month.
</p>

This lab rebuilds parts of the [Session 5 lab](../lectures/05_metrics_and_kpis_lab.md) (segment KPIs) and the [Session 7 lab](../lectures/07_trends_and_growth_lab.md) (monthly trend and growth) in Tableau. If you get stuck, look back at how you did the same step in Python.

!!! note "Desktop and web editor"

    The click paths on this page are written for **Tableau Desktop Public Edition**. If you use the Tableau Public **web editor** in a browser, the menus differ slightly. Look for the same command in a nearby menu, or ask your facilitator.

---

## The business decision

The head of a retail business has one analyst free next month and asks:

> *"Which customer segment should we look at first? I want to see sales, profit and orders side by side, and the profit we make on each unit of sales. Then show me how sales have moved month by month, without being fooled by the time of year."*

A big Sales total alone is not enough to decide. A segment can sell a lot and still earn little per unit of sales. And a month can look like a crash or a boom just because of the season. Today you build fair measures and check each one by reconciliation.

!!! note "About the data"

    **Superstore** is a sample published by Tableau about a **fictitious** company. Sales and Profit are in the **file's own monetary units**. The file does not state a currency, so we never call them dollars or any other currency. The file does not explain how Profit is calculated, so we call Profit ÷ Sales the **profit ratio**, not "gross margin".

---

## How this lab works

| Part | What you do | Tasks |
|---|---|---|
| **Setup** | Open your T1 workbook and check its fields, everyone together | Setup |
| **Core** | Build a segment KPI table that reconciles; debug a colleague's profit ratio; write a recommendation | C1–C3 |
| **Stretch** | Draw the monthly trend with a running total; add MoM and YoY growth | S1–S2 |
| **Challenge** | Count the orders that appear in more than one category, with an LOD expression | X1 |

Each task has a level:

- **Core**: everyone completes it; it is enough for your portfolio.
- **Stretch**: for when you finish the core tasks early.
- **Challenge**: optional, harder reasoning.

---

## What you will be able to do

1. Create aggregate calculated fields and format them.
2. Build a KPI table with a grand total, and reconcile it.
3. Show why `AVG([Profit] / [Sales])` is not the profit ratio.
4. Explain why order counts by category do not add up to the total.
5. Add a running total and MoM and YoY growth with table calculations.
6. Focus on one year without breaking the growth figures.
7. Use a FIXED LOD expression to answer a question about each order.

**Evidence you keep:** your saved workbook, a segment KPI table with reconciliation notes, your explanation of the colleague's mistake, a short recommendation, and any Stretch and Challenge sheets.

Before you start, work through the [T2 lecture](T2_calculations_kpis_lecture.md). Have your T1 workbook and your evidence log ready.

---

## Setup: open your T1 workbook

### Step 1: Save a copy

1. Open **Tableau Desktop Public Edition** and open `T1_lab_YourName.twbx`.
2. Choose **File → Save As** and save it as a **Tableau Packaged Workbook (*.twbx)** named `T2_lab_YourName`.

Now you work in the copy, and your T1 workbook stays as you submitted it.

!!! tip "No T1 workbook?"

    Follow [Set up the Superstore data source](T1_fundamentals_lab.md#set-up-the-superstore-data-source) in the T1 lab first, then come back here and save as `T2_lab_YourName`.

### Step 2: Check the data source

1. Click the **Data Source** tab at the bottom left.
2. Check that **Orders** and **Returns** are on the canvas with a relationship line between them.
3. Check that the **Filters** area at the top right shows **1** filter. Click **Edit** and confirm it keeps **Order Date** from 1 January 2023 to 31 December 2025.

!!! warning "The scope must be right before you build KPIs"

    Without the data source filter, every total includes orders outside the course period, and none of your numbers will match your Python work.

### Step 3: Check your fields

Go to any sheet and look in the **Data** pane. You need these two calculated fields from T1:

| Field | Formula |
|---|---|
| `Distinct Orders` | `COUNTD([Order ID])` |
| `Order Total` | `{FIXED [Order ID] : SUM([Sales])}` |

If one is missing (for example, you did not do T1 Stretch S1), create it now with **Analysis → Create Calculated Field...**. Use exactly these names: T3 uses them too.

---

## Core tasks

### C1 (Core): The segment KPI table

#### Part A: Build the table

1. Create a new sheet and name it `Segment KPIs`.
2. Create a calculated field named `Profit Ratio`:

    ```
    SUM([Profit]) / SUM([Sales])
    ```

    In plain words: add up Profit, add up Sales, then divide once.

3. Format it as a percentage. In the Data pane, right-click **Profit Ratio** and choose **Default Properties → Number Format...**. Choose **Percentage**, set **Decimal places** to `1` and click **OK**.
4. Drag **Segment** to **Rows**.
5. Drag **Measure Names** to **Columns**.
6. Drag **Measure Values** onto **Text** on the Marks card. A **Measure Values** card appears below the Marks card, listing every measure in the data.
7. On the Measure Values card, drag off every pill except **SUM(Sales)**, **SUM(Profit)**, **AGG(Profit Ratio)** and **AGG(Distinct Orders)**. If one of these is missing, drag it from the Data pane onto the card.
8. Choose **Analysis → Totals → Show Column Grand Totals**.
9. Double-click the sheet title and write a title that says what the table shows and for which period, for example `Segment KPIs, orders placed 2023–2025 (file's own monetary units)`.

!!! tip "Another way to choose the measures"

    Instead of dragging pills off the Measure Values card, you can drag **Measure Names** to the **Filters** shelf and tick only the four measures you want.

#### Part B: Reconcile

Write each check in your evidence log, with the numbers you added up.

- [ ] Add the three segment **Sales** values by hand. Do they equal the Grand Total?
- [ ] Add the three segment **Profit** values. Do they equal the Grand Total?
- [ ] Add the three segment **Distinct Orders** values. Do they equal the Grand Total, and the Distinct Orders number from T1 C1?
- [ ] Divide the Grand Total **Profit** by the Grand Total **Sales** with a calculator. Does it equal the Grand Total **Profit Ratio**?
- [ ] Now take the simple average of the three segment Profit Ratios. Is it the same as the Grand Total Profit Ratio? Which one is the business's profit ratio?

!!! note "Small rounding differences"

    Tableau adds up the full values, then rounds what it shows. If your hand total differs from the Grand Total only in the last decimal place, that is rounding, not an error.

#### Part C: The same table by category

1. Duplicate the sheet (right-click the tab → **Duplicate**) and name the copy `Category KPIs`.
2. Drag **Category** onto the **Segment** pill on Rows to replace it.
3. Reconcile again: do the category **Sales** add up to the Grand Total? Do the category **Distinct Orders**?
4. Subtract the Grand Total Distinct Orders from your hand-added sum of category orders. Write the difference in your log.
5. In one or two sentences, explain why the sum is larger than the total, and why the same did not happen for segments. *Hint: Part 3 of the lecture.*

!!! warning "The Grand Total is right; the hand sum is not"

    Tableau's Grand Total recounts the distinct orders over all rows, so it is the true number of orders. Adding up the category rows counts some orders more than once.

### C2 (Core): Debug a colleague's profit ratio

A colleague built the same table, but with this field:

```
AVG([Profit] / [Sales])
```

They say: *"I calculated the average profit ratio, so it is the profit ratio for each segment."*

1. Go back to the `Segment KPIs` sheet.
2. Create a calculated field named `Avg Line Ratio` with the colleague's formula.
3. Format it as a percentage with one decimal place, as in C1 Part A step 3.
4. Drag **Avg Line Ratio** onto the **Measure Values** card, so it appears as a new column next to **Profit Ratio**.

**Compare** the two columns and answer in your log:

1. For each segment, which is larger: Profit Ratio or Avg Line Ratio? For which segment is the gap largest?
2. Look at the Grand Total row. Are the two numbers close or far apart? If they are close, does that make the colleague's field correct? Explain in one sentence.
3. In one sentence each, say what **Profit Ratio** calculates and what **Avg Line Ratio** calculates. Use the words "order line" and "weight".
4. Which segment has the most influence on the overall Profit Ratio, and why?

!!! tip "Check the weights"

    To see each segment's weight, right-click **SUM(Sales)** on the Measure Values card and choose **Quick Table Calculation → Percent of Total**. Then right-click it again and choose **Edit Table Calculation**, and under **Compute Using** choose **Segment** (or **Table (down)**). Otherwise each row is calculated on its own and shows 100%. Each segment's share of Sales is its weight in the overall Profit Ratio. Right-click again and choose **Clear Table Calculation** when you are done.

Finally, remove **Avg Line Ratio** from the table (drag it off the Measure Values card), so your submitted table shows only the correct measures. Keep the field in the Data pane so your facilitator can see it.

### C3 (Core): Write a recommendation and save

Write **three sentences** to the head of the business:

1. **Recommendation:** which segment to look at first.
2. **Evidence:** two measures from your `Segment KPIs` table that support it. Describe how they compare; you do not need to copy every number.
3. **Limitation:** one thing this table cannot tell you. For example, it shows which segment *looks* different, not *why*.

Save your workbook (**File → Save**).

---

## Stretch tasks

### S1 (Stretch): Monthly trend with a running total

1. Create a new sheet named `Monthly sales`.
2. Drag **Order Date** to **Columns**. Tableau shows **YEAR(Order Date)**.
3. Right-click the pill and choose the second **Month** in the menu (the green one, with an example such as *May 2015*). The pill turns green: a continuous month axis.
4. Drag **Sales** to **Rows**. You get a line chart with one point per month.
5. Title the chart, for example `Monthly Sales, orders placed 2023–2025 (file's own monetary units)`.

**Check the calendar.** Look at the status bar at the bottom left of the window. It shows the number of marks. With the course scope you expect one mark for each month of three full years. If the number is different, a month is missing, and `LOOKUP` in S2 will compare the wrong months.

**Read it.** Write three observations. Are some months high every year? Are some always low?

**Add a running total:**

1. Drag **Sales** to **Rows** again, next to the first **SUM(Sales)** pill. You get a second chart below the first.
2. Right-click the second pill and choose **Quick Table Calculation → Running Total**.
3. Right-click it again and choose **Compute Using → Order Date** (Tableau may label it **Month of Order Date**).

**Reconcile:** hover over the last point of the running total. It must equal the Grand Total **Sales** in your `Segment KPIs` table. If it does not, check the Compute Using setting and the data source filter.

### S2 (Stretch): MoM and YoY growth

1. Duplicate `Monthly sales` and name the copy `Growth`. Remove the running total pill (drag it off Rows).
2. Create two calculated fields:

    `MoM Growth`
    ```
    SUM([Sales]) / LOOKUP(SUM([Sales]), -1) - 1
    ```

    `YoY Growth`
    ```
    SUM([Sales]) / LOOKUP(SUM([Sales]), -12) - 1
    ```

3. Format both as percentages with one decimal place (**Default Properties → Number Format...**).
4. Drag **MoM Growth** onto the **SUM(Sales)** pill on Rows to replace it. In the Marks card drop-down, choose **Bar**.
5. Right-click the **MoM Growth** pill and choose **Compute Using → Order Date** (or **Month of Order Date**).
6. Drag **YoY Growth** to **Rows**, next to MoM Growth. Set its Compute Using the same way.
7. Title the sheet, for example `Sales growth by month, MoM and YoY, orders placed 2023–2025`.

**Reconcile** your MoM formula with Tableau's own:

1. Drag **Sales** to **Rows** again.
2. Right-click it and choose **Quick Table Calculation → Percent Difference**, then **Compute Using → Order Date**.
3. Hover over three months. The Percent Difference must equal your MoM Growth for each.
4. Drag the extra pill off Rows.

**Check the blanks.** Which months have no MoM bar? Which have no YoY bar? Explain each in one sentence.

**Read it.**

1. Find the month with the **largest** MoM growth. Write it down with the Sales of that month and of the month before (from `Monthly sales`). Is this a real boom, or something else?
2. Find January 2025. Compare its MoM and YoY growth. Which one should the head of the business see, and why?

#### The filter trap

1. Drag **Order Date** to the **Filters** shelf. Choose **Years**, click **Next**, tick **2025** only, and click **OK**.
2. Look at January 2025. What happened to its MoM growth? What happened to the YoY bars?
3. Write one sentence explaining why. *Hint: Part 5 of the lecture.*
4. Remove the filter: drag the **YEAR(Order Date)** pill off the Filters shelf.

#### Highlight instead of filter

1. Create a calculated field named `Focus Year`:

    ```
    IF YEAR(MIN([Order Date])) = 2025 THEN "2025" ELSE "Earlier years" END
    ```

    In plain words: label each month's mark "2025" or "Earlier years".

2. Drag **Focus Year** onto **Color** on the Marks card. The 2025 bars now stand out.
3. **Reconcile:** hover over January 2025. Its MoM and YoY growth must be the same as before you tried the filter.

!!! note "Why this field does not break the growth"

    `Focus Year` is an aggregate calculation, so it is a measure. A measure on Color does not split the view, so `LOOKUP` still moves along all the months. A dimension on Color, such as **YEAR(Order Date)**, would split the view into one part per year, and each January would lose its comparison month.

---

## Challenge tasks

### X1 (Challenge): Orders in more than one category

In C1 Part C, the category order counts added up to more than the total. Now find out exactly how many orders contain more than one category.

1. Create a new sheet named `Categories per order`.
2. Create a calculated field named `Categories in Order`:

    ```
    {FIXED [Order ID] : COUNTD([Category])}
    ```

    In plain words: for each order, count how many different categories its lines belong to.

3. In the Data pane, right-click **Categories in Order** and choose **Convert to Dimension**. If its icon is still green, right-click it again and choose **Convert to Discrete**.
4. Drag **Categories in Order** to **Rows** and **Distinct Orders** to **Text**.
5. Choose **Analysis → Totals → Show Column Grand Totals**.

**Reconcile** two ways:

1. Add the rows by hand. Do they equal the Grand Total, and Distinct Orders from C1? Why must they, this time?
2. Multiply each row's Distinct Orders by its number of categories, and add the results. Does this equal your hand-added sum of category orders from C1 Part C? Explain why in one sentence.

**Explain:** how many orders appear in more than one category? How does this number relate to the difference you wrote down in C1 Part C? *Hint: an order with three categories is counted twice too many.*

**Try a filter.** Drag **Category** to the **Filters** shelf and keep only **Furniture**. Do the labels 1, 2 and 3 still describe the whole order, or only its Furniture lines? Use the warning in Part 6 of the lecture to explain what you see. Remove the filter when you are done.

---

## Evidence checklist

Before you submit, check that you have:

- [ ] the `Segment KPIs` sheet with Sales, Profit, Profit Ratio and Distinct Orders, a grand total and a title
- [ ] your five reconciliation checks from C1 Part B
- [ ] the `Category KPIs` sheet and your sentence on why category orders do not add up
- [ ] the `Avg Line Ratio` field and your answers to the four C2 questions
- [ ] your three-sentence recommendation
- [ ] Stretch and Challenge sheets and notes, if you did them

---

## Submit on Moodle

1. Save your workbook as `T2_lab_YourName.twbx` (**File → Save**).
2. Export your `Segment KPIs` sheet: choose **File → Print to PDF**, or **Worksheet → Export → Image...**.
3. Open the **T2 lab** assignment on the course Moodle page.
4. Upload the `.twbx` file, the PDF or image, and your written answers (from your evidence log).

!!! warning "Do not publish this lab"

    You do not need to publish anything to Tableau Public for this lab. Anything published there is public. If you use the web editor, saving puts the workbook and its data on your Tableau Public profile. Keep your Superstore work on your own computer: never save or publish Superstore to Tableau Public, because the course has not found a clear permission to republish the file ([T4 lecture, Part 2](T4_publishing_portfolio_lecture.md)). Ask your facilitator how to work on this lab without saving to Tableau Public, and how to get your workbook for Moodle.

---

## Next

Keep this workbook. In T3 you combine the `Segment KPIs` table and the monthly views into a decision dashboard, using the same fields.
