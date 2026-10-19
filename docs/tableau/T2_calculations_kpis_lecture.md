# T2 lecture: Calculations and KPIs

<p class="lead">
Learn to build your own measures in Tableau and to know when they can be trusted. A KPI is only useful if it is calculated at the right level, adds up where it should, and keeps its comparison when you filter.
</p>

In the Python sessions you built a segment KPI table ([Session 5](../lectures/05_metrics_and_kpis_lecture.md)) and monthly growth rates ([Session 7](../lectures/07_trends_and_growth_lecture.md)). Today you learn the Tableau tools that do the same jobs: calculated fields, table calculations and a first level of detail (LOD) expression. The traps are the same as in Python, so watch for them.

---

## What you will be able to explain

1. What a **calculated field** is, and the difference between **row-level** and **aggregate** calculations.
2. Why a ratio must be calculated as a **ratio of sums**, and why `AVG([Profit]/[Sales])` gives a different answer.
3. Why **distinct counts** do not always add up, and when they do.
4. What a **table calculation** is: running totals, and growth with **LOOKUP**.
5. What **Compute Using** means for a table calculation.
6. Why **filtering months breaks growth** figures, and what to do instead.
7. What a **FIXED level of detail expression** is, using the order total as an example.

---

## Part 1: Calculated fields

A **calculated field** is a new field you define with a formula. You create one with **Analysis → Create Calculated Field...**. It appears in the Data pane next to the fields from your file, and you can drag it into a view like any other field.

You already made three in T1:

| Field | Formula |
|---|---|
| `Returned Order` | `NOT ISNULL([Order ID (Returns)])` |
| `Distinct Orders` | `COUNTD([Order ID])` |
| `Ship Days` | `DATEDIFF('day', [Order Date], [Ship Date])` |

These three are not the same kind of calculation.

### Row-level and aggregate calculations

| Kind | What it does | Example | What you get |
|---|---|---|---|
| **Row-level** | Works on one row at a time, like a new column in the table | `DATEDIFF('day', [Order Date], [Ship Date])` | One value per order line. Tableau aggregates it when you drag it into a view, for example as SUM or AVG |
| **Aggregate** | Adds up (or counts) many rows first, then calculates | `COUNTD([Order ID])`, `SUM([Profit]) / SUM([Sales])` | One value per mark. The rows that go into each mark depend on the dimensions in the view |

You can tell them apart from the formula. If every field in it sits inside an aggregation such as `SUM`, `AVG` or `COUNTD`, it is an aggregate calculation. If no field is aggregated, it is row-level.

!!! warning "Cannot mix aggregate and non-aggregate arguments"

    A formula such as `SUM([Profit]) / [Sales]` mixes the two kinds: a total divided by one row's value. Tableau refuses it with this error message. Decide first whether you want one value per row or one value per mark, then aggregate every field or none.

In the Data pane, an aggregate calculated field shows as `AGG(...)` when you drag it into a view. You cannot change its aggregation, because the aggregation is already inside the formula.

!!! tip "Same idea as in pandas"

    A row-level field is like adding a column to your DataFrame. An aggregate field is like a calculation after `groupby(...).agg(...)`. You used both in the [Session 5 lab](../lectures/05_metrics_and_kpis_lab.md).

---

## Part 2: Ratio of sums versus mean of ratios

The profit ratio tells you how much profit each unit of sales earned. In the [Session 5 lecture](../lectures/05_metrics_and_kpis_lecture.md) you learnt the rule: **totals first, then divide**.

In Tableau, the correct field is an aggregate calculation:

```
Profit Ratio = SUM([Profit]) / SUM([Sales])
```

Tableau adds up Profit and Sales over the rows of each mark, then divides once. In a grand total row, it adds up over **all** rows and divides again. It does not add or average the segment ratios.

There is a tempting wrong version:

```
AVG([Profit] / [Sales])
```

This works out a profit ratio for **every order line** (a row-level calculation), then takes the simple average of those ratios. Each line counts the same, whether it sold a pen or a large table.

### A small example

| Line | Sales | Profit | Line ratio |
|---|---|---|---|
| A | 10,000 | 1,000 | 10% |
| B | 100 | 50 | 50% |

- **Ratio of sums:** 1,050 ÷ 10,100, about **10.4%**. This is what the business really earned per unit of sales.
- **Mean of ratios:** (10% + 50%) ÷ 2 = **30%**. The tiny line pulls the result as hard as the big one.

The ratio of sums is a **weighted** average of the line ratios, with each line weighted by its Sales. The mean of ratios gives every line the same weight.

!!! warning "A close answer is not a correct answer"

    On some data the two versions give similar numbers by chance. That does not make the mean of ratios correct. Split by a dimension, such as Segment, and the gap usually opens up. You test this in the lab.

!!! note "Division by zero"

    If a mark has no Sales, `SUM([Sales])` is zero and Tableau shows the ratio as blank (**Null**), not as an error. A blank means "not available". Never read it as 0%.

---

## Part 3: Distinct counts do not always add up

**Sums are additive.** The Sales of the three segments add up to total Sales, because each order line belongs to exactly one segment.

**Distinct counts may not be.** `COUNTD([Order ID])` counts each order once **within each mark**. Whether the marks add up to the total depends on whether an order can sit in more than one mark.

| Split by | Can one order appear in two marks? | Do the order counts add up to the total? |
|---|---|---|
| **Segment** | No. Every line of an order has the same Segment | **Yes**. Segment splits the orders into separate groups |
| **Category** | Yes. One order can contain Furniture **and** Office Supplies **and** Technology | **No**. An order with lines in two categories is counted once in each, so the sum is **larger** than the total |

You noticed this at the end of C3 in the [T1 lab](T1_fundamentals_lab.md). The grand total in Tableau is correct in both cases: Tableau recounts the distinct orders over all rows, it does not add up the bars. The mistake happens when **you**, or a colleague with a spreadsheet, add up the category values by hand and call it the number of orders.

!!! tip "The test for additivity"

    Ask: *can one item belong to more than one group?* If yes, distinct counts across those groups do not add up. Medians, percentiles and ratios do not add up either. Always recalculate them for the total.

---

## Part 4: Table calculations

A **table calculation** works on the numbers **already in the view**, after Tableau has aggregated them. It does not go back to the rows of your file. It looks at the other marks in the table: the one before, the one after, or all of them.

You met one in the T1 lab: the **running total** on the order-value histogram.

| Table calculation | What it does | Typical use |
|---|---|---|
| **Running total** | Adds each mark to all the marks before it | Sales so far this year |
| **Difference** / **Percent difference** | Compares each mark with the one before | Month-on-month change |
| **Percent of total** | Each mark as a share of all marks | A segment's share of Sales |
| **Rank** | Orders the marks | Top 10 products |

The quickest way to add one is to right-click a green pill in the view and choose **Quick Table Calculation**. A table calculation pill shows a small triangle (**Δ**) on its right.

### LOOKUP: the value from another mark

`LOOKUP` returns the value of an expression from another mark, a set number of steps away.

| Formula | Returns |
|---|---|
| `LOOKUP(SUM([Sales]), -1)` | Sales of the **previous** mark |
| `LOOKUP(SUM([Sales]), -12)` | Sales of the mark **12 steps back** |
| `LOOKUP(SUM([Sales]), 0)` | Sales of this mark |

With one mark per month, in date order, you can write growth rates:

```
MoM Growth = SUM([Sales]) / LOOKUP(SUM([Sales]), -1) - 1
```

```
YoY Growth = SUM([Sales]) / LOOKUP(SUM([Sales]), -12) - 1
```

**Month-on-month (MoM)** compares each month with the month before. **Year-on-year (YoY)** compares each month with the same month one year earlier. In the [Session 7 lecture](../lectures/07_trends_and_growth_lecture.md) you saw why the YoY comparison is fairer for a seasonal business: January after a busy December always looks like a crash.

!!! warning "LOOKUP counts marks, not months"

    `LOOKUP(..., -12)` means "12 marks back", not "12 months back". It gives the same month last year **only** if every month is in the view, in order, with none missing. Always check the number of marks in the status bar at the bottom left of the window: with the course scope you expect one mark per month, for three full years.

The first month in the view has no previous mark, so its MoM growth is blank. The first twelve months have no mark 12 steps back, so their YoY growth is blank. Blank means "no comparison available", never 0%.

### Compute Using: which direction?

A table calculation needs to know **which marks to look along**. This is called **Compute Using**, and you set it by right-clicking the pill and choosing **Compute Using**.

| Setting | Meaning |
|---|---|
| **Table (across)** | Move left to right along the whole table |
| **Table (down)** | Move top to bottom |
| A named field, for example **Order Date** | Move along that field's values, whatever the layout |

Naming the field is safer than *across* or *down*. If you later swap rows and columns, the calculation still moves through the months.

!!! note "Partitions"

    Any dimension in the view that is **not** in Compute Using splits the table into separate parts. The table calculation restarts in each part. If you add **Segment** to Color on a monthly growth chart, each segment gets its own growth line, and each segment's first month is blank.

---

## Part 5: Why filtering months breaks growth

In T1 you learnt the order in which Tableau applies filters. Table calculations come **after** all the ordinary filters:

1. Extract filters
2. Data source filters
3. Context filters
4. Dimension filters
5. Measure filters
6. **Table calculations** are worked out here
7. Table calculation filters

So a dimension filter removes months **before** `LOOKUP` runs. Suppose you filter a monthly growth chart to the year 2025 to focus on it:

- December 2024 is no longer in the view.
- `LOOKUP(SUM([Sales]), -1)` for January 2025 finds no previous mark.
- January 2025's MoM growth becomes **blank**, and every YoY growth value becomes blank, even though the data is still in your file.

!!! warning "Highlight, do not filter"

    To focus on part of a time series, keep **all months** in the view and make the months you care about **stand out**, for example with colour. Then every growth value still has its comparison month. This is the same trap you met in Python in the [Session 7 lecture](../lectures/07_trends_and_growth_lecture.md): calculate growth on the full series first, then choose what to show.

There is also a more advanced fix. A **table calculation filter** (a filter on a table calculation field) runs **last**, after the growth values are calculated. It hides marks without removing them from the calculation. You do not need it today; highlighting is simpler and keeps the context visible.

---

## Part 6: A first level of detail expression

Sometimes you need a value at a **different level** from the view. The most common case in Superstore: you want the value of each **order**, but the rows are **order lines**.

A **level of detail (LOD) expression** calculates an aggregate at a level you choose. You used one in T1 S1:

```
Order Total = {FIXED [Order ID] : SUM([Sales])}
```

Read it as: *for each Order ID, add up Sales over all its lines*. The result is written back onto every line of that order. An order with three lines has the same Order Total on all three.

| | Table calculation | FIXED LOD expression |
|---|---|---|
| Works on | The marks already in the view | The rows of the data source |
| Level | Set by the view and Compute Using | Set by the dimensions in the braces |
| Changes when you add a dimension to the view? | Yes | No |

Because Order Total is repeated on every line, count orders with `Distinct Orders`, not with rows, when you use it. In T1 you did this for the order-value histogram.

LOD expressions also let you ask questions about each order, for example *how many different categories does this order contain?*:

```
{FIXED [Order ID] : COUNTD([Category])}
```

You build this in the lab Challenge.

!!! warning "FIXED ignores dimension filters"

    A FIXED expression is calculated **before** dimension filters (step 4 in Part 5). If you filter a sheet to one Category, Order Total still adds up **all** the order's lines, in every category. The data source filter still applies, so the course scope holds. This is often what you want for an order total, but say so when you report it.

---

## Quiz

Answer these at the start of the T2 lab. Your facilitator will go through the answers.

1. Is `DATEDIFF('day', [Order Date], [Ship Date])` a row-level or an aggregate calculation? How can you tell from the formula?
2. A colleague calculates the profit ratio as `AVG([Profit] / [Sales])`. In one sentence, what does this calculate, and why is it not the business's profit ratio?
3. In a segment table with a grand total, how does Tableau calculate the grand total of `SUM([Profit]) / SUM([Sales])`?
4. You show `Distinct Orders` by Segment and by Category. In which table do the rows add up to the total number of orders, and why?
5. Your monthly growth chart shows MoM growth for every month in 2025, but after you filter the view to 2025, January becomes blank. Why, and what should you do instead?
6. What does `LOOKUP(SUM([Sales]), -12)` return, and when does it **not** give the same month last year?
7. Every line of an order carries the same `Order Total`. Why should you count orders with `Distinct Orders` and not with the row count when you chart order values?
