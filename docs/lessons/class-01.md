# Lesson 1: From decision to evidence

<p class="lead">
Turn a vague business request into a clear question, open your first dataset in Tableau, and build a first chart you can explain.
</p>

!!! warning "Draft lesson"

    The Tableau steps on this page have not yet been rehearsed on the course version of Tableau. Menu names may differ slightly on your computer. Your facilitator will confirm them in class.

---

## The business decision

The head of a retail business says:

> *"Sales feel uneven across our customer groups. I need to know where to look first."*

This is not yet a question you can answer with data. Today you will turn it into one, and then take a first look at the evidence.

!!! note "About the data"

    We use a **fictitious** retail sample published by Tableau (the "Superstore" sample), prepared for this course. It is not a real company. Sales and Profit are in the file's own monetary units; the currency is not stated, so we never label it as dollars, rupees or anything else.

---

## What you will be able to do

By the end of this lesson you will be able to:

1. Write a business question that names a decision, a population and a time period.
2. Connect Tableau to a CSV file and recognise dimensions and measures.
3. Build a simple bar chart and add a filter.
4. Explain the difference between **one row** and **one order** in this file.
5. Save your workbook on your computer and reopen it.

**Evidence you keep:** your written question, a saved first chart and a one-sentence explanation of what a row means.

---

## Before you start

- Read the [Foundations](../foundations/index.md) pages. They explain *why* the habits in this lesson matter.
- Install **Tableau Desktop Public Edition** (see [Setup and practice](../course/setup.md)).
- Complete the smoke test: open a CSV, create a sum, save, close and reopen.
- Get the course file `order_lines.csv` (release `superstore-retail-v1`) from your facilitator. Save it in a folder you can find again, for example `Documents/DataAnalytics/data`.

!!! tip "If Tableau will not install or open"

    Tell your facilitator before the session. You can follow the demonstration, pair with a classmate and still write your question and notes. You will build your own chart later.

---

## Part 1: From request to question

A good analytical question answers four things:

| Part | Ask yourself | Example |
|---|---|---|
| **Decision** | What will someone do differently? | Choose one customer segment to investigate next month |
| **Population** | Which records count? | All order lines in the course file |
| **Period** | Which dates? | Orders placed in 2023, 2024 and 2025 |
| **Measure** | What will we compare? | Sales by customer segment |

Putting it together:

> *"Which customer segment had the highest Sales for orders placed in 2023–2025, so we can choose one segment to investigate next month?"*

!!! hint "Your turn"

    Rewrite the head's request as your own question. Use the four parts in the table. Keep it to one sentence.

---

## Part 2: Watch the demonstration

Your facilitator will connect to the file and build a first chart while you watch. Before each step, **predict** what you think will happen.

Things to notice:

- How Tableau reads each column (text, number or date).
- Which fields appear as **dimensions** (things you group by) and which as **measures** (numbers you add up).
- What happens to a number when you drag it into the view.

---

## Part 3: Guided practice

Follow along step by step.

### Connect to the file

1. Open Tableau Desktop Public Edition.
2. In the **Connect** pane on the left, under **To a File**, choose **Text file**.
3. Find and open `order_lines.csv`.
4. Tableau opens the **Data Source** page with a preview of the rows.

### Check the column types

Look at the small icon above each column in the preview:

| Icon | Meaning | Examples in this file |
|---|---|---|
| **Abc** | Text | order_id, segment, region |
| **#** | Number | sales, profit, quantity |
| **Calendar** | Date | order_date, ship_date |

!!! warning "Check the IDs"

    `order_id` and `row_id` are identifiers, not amounts. Adding them up means nothing. If an ID shows as a number, note it in your log.

Tableau may tidy column names for display, for example showing `order_id` as **Order Id**. It is the same field.

### Build a first chart

1. Click the **Sheet 1** tab at the bottom.
2. In the **Data** pane, find **Segment** and drag it to **Rows**.
3. Find **Sales** and drag it to **Columns**.
4. You should see one bar per segment. Tableau shows this as **SUM(Sales)**.

### Add a filter

1. Drag **Region** to the **Filters** card.
2. Tick one region and click **OK**.
3. Watch how the bars change. Then clear the filter so all regions are included again.

!!! note "Write it down"

    Every time you filter, record it. A chart without its filters written down is easy to misread later.

### Save and reopen

1. Choose **File → Save As** and save the workbook in your course folder, for example `class01_first_view`.
2. Close Tableau, open it again and open your saved workbook.
3. Check that the chart and your filter settings are still there.

---

## Part 4: Rows versus orders

Open the Data Source page again and look at a few rows that share the same `order_id`.

- One **row** in this file is one **order line**: one product within an order.
- One **order** can have several lines.
- So the number of rows is **not** the number of orders.

!!! hint "Quick check"

    In the Data pane, Tableau lists a field named after the file with **(Count)** at the end. Drag it to the view. Is that counting rows or orders? Write your answer in one sentence.

You will measure orders properly in [Lesson 2](class-02.md).

---

## Part 5: Independent work

On a new sheet, build one more simple view on your own:

1. Choose a different grouping: **Region** or **Category**.
2. Show **Sales** for each group.
3. Add a title that says what the chart shows and for which period.
4. Write one sentence describing what the chart shows. Do not explain *why* yet.

---

## Part 6: Challenge

A colleague says:

> *"The biggest bar is the best segment, so we should invest there."*

In two or three sentences, explain why a bigger Sales bar alone does not tell us where to invest. What else would you want to see?

---

## Exit ticket

Before you finish, write:

1. Your one-sentence business question.
2. What one row in `order_lines.csv` represents.
3. One thing you are still unsure about.

---

## After the lesson

- Fix anything that did not work during setup.
- Read the [Analytical workflow](../course/workflow.md) page.
- Start your **evidence log** (see [Setup and practice](../course/setup.md)) with today's question, file name and filters.
