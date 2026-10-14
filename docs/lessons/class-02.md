# Tableau Lesson 2: Can we trust the sales table?

<p class="lead">
Before comparing anything, find out exactly what the retail file contains: what a row is, which columns can be added up, and how to count orders correctly.
</p>

!!! warning "Draft lesson: Tableau section (coming later)"

    The course currently teaches this lesson in Python: see [Python Lesson 2](../lectures/02_trust_the_sales_table.md). This Tableau version will be completed in the later Tableau section.

    The Tableau steps on this page have not yet been rehearsed on the course version of Tableau. Menu names may differ slightly on your computer.

---

## The business decision

The retail head now asks:

> *"Before you show me any chart, can I trust these numbers? How many orders did we actually have?"*

A wrong count at this stage spoils every later chart. Today is about building trust in the data.

---

## What you will be able to do

By the end of this lesson you will be able to:

1. State the **grain** of the file: what one row represents.
2. Tell which columns are identifiers, categories, dates or amounts.
3. Count **orders** correctly with a distinct count.
4. Explain what the returns flag does and does not tell you.
5. Check a small slice of data by hand.
6. Record what you changed in a short **preparation log**.

**Evidence you keep:** a grain statement, a short quality checklist, a preparation log and one checked order.

---

## Before you start

- Bring your saved [Lesson 1](class-01.md) workbook and your evidence log.
- Keep the original `order_lines.csv` untouched. If you ever need to experiment, work on a copy.

---

## Part 1: Meet the data dictionary

Every column has a job. Knowing that job tells you how to use it.

| Column | What it is | Can you add it up? |
|---|---|---|
| `row_id` | Unique number for each order line | No, it is an identifier |
| `order_id` | Order identifier; repeats across that order's lines | No, count it **distinctly** |
| `order_date`, `ship_date` | Calendar dates | No |
| `order_month` | First day of the order's month, for monthly grouping | No |
| `ship_mode` | Shipping service chosen | No |
| `customer_id` | Fictitious customer identifier | No |
| `segment` | Customer group: Consumer, Corporate or Home Office | No, use it to group |
| `country_region`, `region` | Location labels | No, use them to group |
| `category`, `sub_category` | Product groups | No, use them to group |
| `product_id`, `product_name` | Product identifier and name | No |
| `sales` | Sales reported for the line, in the file's own monetary units | **Yes** |
| `quantity` | Number of items on the line | **Yes**, but it counts items, not orders |
| `profit` | Profit reported for the line (can be negative) | **Yes** |
| `discount` | Discount value as given in the source | No, its exact definition is not documented |
| `returned_order_flag` | 1 if the order appears on the source's returns list, otherwise 0 | Not on line rows (see Part 4) |
| `order_to_ship_days` | Days between order date and ship date | No, not without care |
| `customer_analysis_eligible`, `customer_order_conflict` | Flags for a small data issue with customer IDs | Used only for customer analysis later |

!!! note "Scope of this file"

    The file contains orders placed from **1 January 2023 to 31 December 2025**. A few orders placed late in 2025 shipped in early 2026; they are kept because the order date is what defines the period.

---

## Part 2: Find the grain

**Grain** means: what does one row represent?

1. Open your workbook and go to the **Data Source** page.
2. Sort or scan the preview by `order_id`.
3. Find an order that appears on **more than one row**.
4. Compare those rows. What is the same? What is different?

!!! hint "Write your grain statement"

    Complete this sentence in your log: *"One row in order_lines.csv represents one ______ , identified by ______ ."*

---

## Part 3: Count orders correctly

### Demonstration

Your facilitator will show two numbers side by side:

- the number of **rows** (the field ending in **(Count)**)
- the number of **distinct orders**

Predict before you see them: will the two numbers be equal, or which will be larger?

### Guided practice

1. On a new sheet, drag the **(Count)** field to the view. This counts rows.
2. Drag **Order Id** into the view as well. Right-click it and choose **Measure → Count (Distinct)**. This counts orders.
3. Put both numbers in a small table and label them clearly.
4. Write one sentence explaining why they differ.

!!! tip "A reusable calculation"

    You can also create a calculated field named **Orders** with the formula:

    ```
    COUNTD([Order Id])
    ```

    Use this whenever a chart needs a number of orders.

---

## Part 4: What the returns flag means

`returned_order_flag` is `1` when an order appears on the source's **returns list**.

Be careful with what it does **not** tell you:

- It has **no** return date, quantity or refund amount.
- A `0` means **not on the list**. It does not prove the order was never returned.
- The flag repeats on **every line** of a listed order.

!!! warning "A common mistake"

    Adding up `returned_order_flag` across lines counts **lines** of returned orders, not returned **orders**. To count returned orders, count distinct `order_id` values where the flag is 1.

---

## Part 5: Check one order by hand

Pick one order with several lines.

1. Filter the view to that single `order_id`.
2. Show each line's `sales` and `profit` in a table.
3. Add up the lines yourself on paper or in a spreadsheet.
4. Compare with Tableau's total for that order. Do they match?

Record the order ID, your hand total and Tableau's total in your log.

---

## Part 6: Keep a preparation log

Write down every change you make to how the data is read or shaped, even small ones.

| Date | What I changed | Why | How I checked it |
|---|---|---|---|
| *example* | Created calculated field **Orders** = `COUNTD([Order Id])` | Rows are order lines, not orders | Compared with the row count; checked one order by hand |

The original file is never edited. Every change lives in Tableau or in your log.

---

## Part 7: Independent work

For each **Segment**, build a small table showing:

1. the number of rows,
2. the number of distinct orders,
3. total `sales`.

Then answer in your log:

- Do the segment order counts add up to the overall order count? Why might that be true for Segment?
- Try the same with **Category**. Do category order counts add up to the overall total? Why not?

!!! hint "Think about it"

    Can one order contain products from more than one category? Can one order belong to more than one segment?

---

## Part 8: Debugging challenge

A colleague sends this summary:

> *"We had [row count] orders, and [sum of returned_order_flag] of them were returned."*

1. Which two mistakes are in this sentence?
2. What should each number be counting instead?
3. How would you check your corrected numbers?

Write your corrected sentence. You do not need to share the numbers with anyone yet.

---

## Exit ticket

1. Your grain statement.
2. Why rows and orders differ in this file.
3. One thing the returns flag cannot tell you.

---

## After the lesson

- Finish the Segment and Category tables from Part 7.
- Complete your preparation log and one hand-checked order.
- Keep your workbook for [Lesson 3](class-03.md), where we compare segments using Sales, Profit and average order value.
