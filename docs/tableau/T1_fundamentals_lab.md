# T1 lab: Can we trust the sales table, in Tableau?

<p class="lead">
Connect Tableau to the Superstore file, set the same scope as the Python sessions, and prove you can count rows, orders and returned orders correctly. Then draw the shape of order value and delivery time.
</p>

This lab rebuilds parts of the [Session 2 lab](../lectures/02_data_and_grain_lab.md) and the [Session 4 lab](../lectures/04_descriptive_statistics_lab.md) in Tableau. If you get stuck, look back at how you did the same step in Python.

!!! note "Desktop and web editor"

    The click paths on this page are written for **Tableau Desktop Public Edition**. If you use the Tableau Public **web editor** in a browser, the menus differ slightly. Look for the same command in a nearby menu, or ask your facilitator.

---

## The business decision

The head of a retail business says:

> *"Before you show me any chart in this new tool, can I trust it? Does Tableau give the same number of orders and returns as your earlier analysis? And what does a typical order and a typical delivery look like?"*

A new tool is a new chance to count the wrong thing. Today you set up the data carefully and check every number by reconciliation: the parts must add up to the total.

!!! note "About the data"

    **Superstore** is a sample published by Tableau about a **fictitious** company. Sales and Profit are in the **file's own monetary units**. The file does not state a currency, so we never call them dollars or any other currency.

---

## How this lab works

| Part | What you do | Tasks |
|---|---|---|
| **Setup** | Connect to the file and set the course scope, everyone together | Setup |
| **Core** | Count rows, orders and returned orders; build a filtered bar chart; save | C1–C4 |
| **Stretch** | Draw distributions of order value and ship days | S1–S2 |
| **Challenge** | Check one order by hand; fix a colleague's summary | X1–X2 |

Each task has a level:

- **Core**: everyone completes it; it is enough for your portfolio.
- **Stretch**: for when you finish the core tasks early.
- **Challenge**: optional, harder reasoning.

---

## What you will be able to do

1. Connect Tableau to an Excel file and relate two of its sheets.
2. Set a **data source filter** so every sheet uses the course scope.
3. Count **order lines** and **orders** and explain why they differ.
4. Count **returned orders** and reconcile them with the total.
5. Build a bar chart with a filter, and check that its parts add up.
6. Save your work as a packaged workbook (`.twbx`).

**Evidence you keep:** your saved workbook, a rows-versus-orders table, a returned-orders table, a filtered bar chart and your reconciliation notes.

Before you start, work through the [T1 lecture](T1_fundamentals_lecture.md). Have the downloaded `sample_-_superstore.xls` file and your evidence log ready (see the [Tableau overview](index.md)).

---

## Set up the Superstore data source

Later labs (T2 and T3) start from this setup, so take care with each step.

!!! warning "Use the downloaded file, not the built-in sample"

    Tableau Desktop Public Edition has a built-in data source called **Sample - Superstore**. It may be a different version of the data. Always connect to the `sample_-_superstore.xls` file you downloaded, so your numbers match the course and your Python work.

### Step 1: Connect to the file

1. Open **Tableau Desktop Public Edition**.
2. In the **Connect** pane on the left, under **To a File**, click **Microsoft Excel**.
3. Find and open `sample_-_superstore.xls`.
4. Tableau opens the **Data Source** page. On the left, under **Sheets**, you see **Orders**, **People** and **Returns**.

### Step 2: Add the Orders sheet

1. Drag **Orders** onto the large empty area (the canvas) at the top.
2. A preview of the rows appears below. Look at the small icon above each column: **Abc** for text, **#** for numbers and a calendar for dates.

!!! tip "Check the IDs"

    **Order ID** should show **Abc** (text). **Row ID** shows **#**, but it is an identifier, not an amount. You will never add it up.

### Step 3: Relate Returns to Orders on Order ID

1. Drag **Returns** onto the canvas, next to **Orders**.
2. Tableau draws a line between the two boxes. This line is a **relationship**.
3. Click the line. In the panel that opens below, check that the matching fields are **Order ID** (Orders) **=** **Order ID** (Returns). If they are not, choose **Order ID** in both lists.
4. Close the panel.

!!! note "What the relationship does"

    The Returns sheet lists each returned order once. The relationship lets Tableau look up whether an order's Order ID is on that list. It does not change the Orders sheet.

### Step 4: Add the course scope as a data source filter

1. At the top right of the Data Source page, under **Filters**, click **Add**.
2. In the **Edit Data Source Filters** window, click **Add...**.
3. Choose **Order Date** (from the Orders table) and click **OK**.
4. Choose **Range of Dates** and click **Next**.
5. Set the start date to **1 January 2023** and the end date to **31 December 2025**. Both dates are included.
6. Click **OK**, then **OK** again.

The Filters area now shows **1** filter. Every sheet in this workbook will use only orders placed from 2023 to 2025, the same scope as the Python sessions.

!!! warning "Check the date format"

    Tableau shows dates in your computer's format. `01/12/2025` can mean 1 December or 12 January. Read the dates back after you type them.

### Step 5: Create the Returned Order field

1. Click the **Sheet 1** tab at the bottom of the window.
2. In the **Data** pane on the left, you now see two tables: **Orders** and **Returns**. The Order ID from Returns is shown as **Order ID (Returns)**.
3. Choose **Analysis → Create Calculated Field...**.
4. Name the field `Returned Order` and type this formula:

    ```
    NOT ISNULL([Order ID (Returns)])
    ```

5. Check that the message under the formula says **The calculation is valid**, then click **OK**.

In plain words: an order is returned when Tableau finds its Order ID on the Returns sheet.

### Step 6: Save straight away

1. Choose **File → Save As**.
2. Choose your course folder and save as a **Tableau Packaged Workbook (*.twbx)** named `T1_lab_YourName`.

Save again (**Ctrl + S** on Windows, **Cmd + S** on Mac) after each task.

---

## Core tasks

### C1 (Core): Rows versus orders

The `(Count)` field counts rows. In Superstore one row is one **order line**, so this is not the number of orders.

1. Rename **Sheet 1** to `Rows vs orders`: double-click the tab and type the new name.
2. Create a calculated field named `Distinct Orders` with this formula:

    ```
    COUNTD([Order ID])
    ```

3. In the Data pane, double-click **Orders (Count)**. Tableau shows one number: the number of order lines.
4. Double-click **Distinct Orders**. Tableau now shows both numbers in a small table, labelled by **Measure Names**.
5. Write both numbers in your evidence log.
6. Write one sentence explaining why the two numbers differ.

!!! tip "Another way to count orders"

    You can also drag **Order ID** into the view, right-click its pill and choose **Measure → Count (Distinct)**. The `Distinct Orders` field saves you doing this every time.

!!! note "Compare with Python"

    Check your two numbers against the rows and orders you found in the [Session 2 lab](../lectures/02_data_and_grain_lab.md). They should be the same. If they are not, check the data source filter in Step 4 first.

### C2 (Core): Returned orders

1. Create a new sheet: click the **New Worksheet** icon next to the sheet tabs. Name it `Returned orders`.
2. Drag **Returned Order** to **Rows**.
3. Drag **Distinct Orders** to **Text** on the Marks card.
4. You see **True** for orders on the Returns sheet. The other orders show as **False** or as **Null**, depending on how Tableau matches the two tables. Both mean "not on the Returns sheet".
5. Choose **Analysis → Totals → Show Column Grand Totals**.

**Reconcile:**

- Add the two numbers by hand. Do they equal the **Grand Total**?
- Is the Grand Total the same as **Distinct Orders** in C1?

Now swap **Distinct Orders** for **Orders (Count)**. The number next to **True** gets bigger. In one sentence, explain what it is counting now and why it is not the number of returned orders.

!!! warning "Returned means on the list"

    The Returns sheet has no return date, quantity or refund amount. An order that is not on the list is not proof that nothing came back. Write "orders on the returns list" when you report this number.

### C3 (Core): Orders by segment, with a filter

1. Create a new sheet named `Orders by segment`.
2. Drag **Segment** to **Rows** and **Distinct Orders** to **Columns**. You get one bar per segment.
3. Click the **Sort descending** icon in the toolbar so the longest bar is at the top.
4. Drag **Distinct Orders** onto **Label** on the Marks card, so each bar shows its value.
5. Choose **Analysis → Totals → Show Column Grand Totals**.
6. Double-click the sheet title and write a title that says what the chart shows and for which period, for example `Orders by customer segment, orders placed 2023–2025`.

**Reconcile:** add the three segment bars by hand. Do they equal the Grand Total, and the Distinct Orders number from C1?

Now add a filter:

1. Drag **Region** to the **Filters** shelf.
2. In the window that opens, tick one region only and click **OK**.
3. Right-click the **Region** pill on the Filters shelf and choose **Show Filter**. A filter control appears on the right.
4. Add your region to the title, for example `... (Region: West)`.
5. Add up the segment bars again. Do they still equal the new Grand Total?
6. Switch the filter back to **(All)** before you move on.

!!! note "Write your filters down"

    Every time you filter, record it in your evidence log. A chart without its filters written down is easy to misread later.

**Think about it.** Make a copy of the sheet (right-click the tab → **Duplicate**) and replace **Segment** with **Category**. Add the category bars by hand. Do they equal the Grand Total this time? Write one sentence on why not. *Hint: can one order contain products from more than one category? Can one order belong to more than one segment?*

### C4 (Core): Save and reopen

1. Save your workbook (**File → Save**).
2. Close Tableau completely.
3. Open Tableau again and open `T1_lab_YourName.twbx`.
4. Check that all your sheets, the **Returned Order** and **Distinct Orders** fields and the data source filter are still there.

---

## Stretch tasks

### S1 (Stretch): Histogram of order value

To describe orders, you first need the value of each **order**, not each line. In Session 4 you built an order-level table in Python. In Tableau you create an **order total** field.

1. Create a new sheet named `Order value`.
2. Create a calculated field named `Order Total`:

    ```
    { FIXED [Order ID] : SUM([Sales]) }
    ```

    In plain words: for each Order ID, add up the Sales of all its lines. Every line of an order then carries that order's total. You learn how this kind of formula works in T2.

3. In the Data pane, right-click **Order Total** and choose **Create → Bins...**.
4. Choose a round **Size of bins**, for example `100`, and click **OK**. A new field **Order Total (bin)** appears.
5. Drag **Order Total (bin)** to **Columns** and **Distinct Orders** to **Rows**.
6. Title the chart, for example `Order value, orders placed 2023–2025 (file's own monetary units)`.

!!! warning "Count orders, not rows"

    Every line of an order carries the same Order Total. If you used **Orders (Count)** on Rows, an order with three lines would be counted three times. **Distinct Orders** counts each order once.

**Reconcile:** every order falls in exactly one bin, so the bars must add up to Distinct Orders.

1. Drag **Distinct Orders** onto **Label** on the Marks card.
2. Right-click that Label pill and choose **Quick Table Calculation → Running Total**. Each label now adds its bar to all the bars before it. You meet running totals properly in T2.
3. Read the label on the last bar. Does it equal Distinct Orders from C1?
4. Right-click the Label pill and choose **Clear Table Calculation**.

**Read it.** In one or two sentences, describe the shape. Where are most orders? Is there a long tail to one side? Does it match the histogram you drew in the [Session 4 lab](../lectures/04_descriptive_statistics_lab.md)?

### S2 (Stretch): Box plot of ship days by ship mode

1. Create a new sheet named `Ship days`.
2. Create a calculated field named `Ship Days`:

    ```
    DATEDIFF('day', [Order Date], [Ship Date])
    ```

    In plain words: the number of days from the order date to the ship date.

3. Drag **Ship Mode** to **Columns** and **Ship Days** to **Rows**.
4. Tableau shows **SUM(Ship Days)**. Right-click the pill and choose **Measure → Average**.
5. Drag **Order ID** onto **Detail** on the Marks card. You now have one mark per **order**.
6. In the Marks card drop-down, choose **Circle**.
7. Right-click the vertical axis and choose **Add Reference Line**. At the top of the window, choose **Box Plot**, then click **OK**.
8. Title the chart, for example `Days from order to shipment by ship mode, orders placed 2023–2025`.

!!! tip "Why Average and not Sum?"

    Every line of an order has the same Order Date and Ship Date, so the same Ship Days. The average of identical values is that value. **SUM** would add it once per line and make orders with more lines look slower.

Hover over a box to see its median and quartiles.

**Read it.** Which ship mode is fastest? Which has the widest spread? Write one sentence a customer service lead could use when making a delivery promise. Compare with the ship-days results in the [Session 4 lab](../lectures/04_descriptive_statistics_lab.md).

---

## Challenge tasks

### X1 (Challenge): Check one order by hand

A total you cannot check is a total you cannot trust. Pick one order and reconcile its lines.

1. Create a new sheet named `One order`.
2. Drag **Order ID** to **Rows** and **Orders (Count)** to **Text**.
3. Click the **Sort descending** icon in the toolbar, so orders with the most lines are at the top.
4. Right-click one Order ID with several lines and choose **Keep Only**.
5. Drag **Product Name** to **Rows**, after Order ID. Drag **Sales** to **Text**, replacing Orders (Count).
6. Choose **Analysis → Totals → Show Column Grand Totals**.
7. Add the line Sales yourself, with a calculator or on paper.

**Reconcile** three numbers and write them in your log:

- your hand total,
- Tableau's Grand Total for the order,
- the **Order Total** field from S1 for this order (drag it to the view and set it to **Minimum** or **Average**; every line has the same value).

Do all three agree? Also check that **Segment**, **Ship Mode** and **Ship Days** are the same on every line of the order.

### X2 (Challenge): Fix a colleague's summary

A colleague sends this summary:

> *"We had [Orders (Count) for all data] orders, and [Orders (Count) for Returned Order = True] of them were returned."*

1. Which two mistakes are in this sentence?
2. Which field should each number use instead?
3. How would you check your corrected numbers? Name the reconciliation.

Write your corrected sentence in your log. Remember the wording from C2: "on the returns list".

---

## Evidence checklist

Before you submit, check that you have:

- [ ] the data source set up with the Returns relationship and the 2023–2025 data source filter
- [ ] the `Rows vs orders` sheet, with your sentence on why the numbers differ
- [ ] the `Returned orders` sheet, with your reconciliation note
- [ ] the `Orders by segment` sheet with a title, a Region filter and your reconciliation note
- [ ] your sentence on why category orders do not add up to the total
- [ ] Stretch and Challenge sheets, if you did them

---

## Submit on Moodle

1. Save your workbook as `T1_lab_YourName.twbx` (**File → Save**).
2. Export your `Orders by segment` sheet: choose **File → Print to PDF**, or **Worksheet → Export → Image...**.
3. Open the **T1 lab** assignment on the course Moodle page.
4. Upload the `.twbx` file, the PDF or image, and your written answers (from your evidence log).

!!! warning "Do not publish this lab"

    You do not need to publish anything to Tableau Public for this lab. Anything published there is public. If you use the web editor, saving puts the workbook and its data on your Tableau Public profile. Keep your Superstore work on your own computer: never save or publish Superstore to Tableau Public, because the course has not found a clear permission to republish the file ([T4 lecture, Part 2](T4_publishing_portfolio_lecture.md)). Ask your facilitator how to work on this lab without saving to Tableau Public, and how to get your workbook for Moodle.

---

## Next

Keep this workbook. In T2 you start from the same data source to build KPIs and growth rates.
