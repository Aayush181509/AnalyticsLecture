# T1 lecture: Tableau fundamentals

<p class="lead">
Learn how Tableau thinks about a table. Once you know how it sorts fields, adds up numbers and applies filters, every chart you build is easier to read and to check.
</p>

You already know the Superstore data from the Python sessions. Today you meet the same data in a new tool. The questions stay the same: what is one row, what are we counting, and which records are included?

---

## What you will be able to explain

1. How Tableau reads a table: the **data source**, **sheets** and **fields**.
2. The difference between **dimensions** and **measures**.
3. The difference between **discrete** (blue) and **continuous** (green) fields.
4. How Tableau **aggregates** numbers, and what the **level of detail** of a view is.
5. What each part of the **Marks card** does.
6. The four main **filter types** and the order in which Tableau applies them.
7. Why the grain of Superstore (one row per order line) matters in Tableau too.

---

## Part 1: How Tableau reads a table

Tableau works in three places.

| Place | What it is | Where you see it |
|---|---|---|
| **Data source** | The connection to your file, plus any tables you link and any filters you set on the whole data | The **Data Source** tab, bottom left |
| **Sheet** | One chart or table. A workbook can hold many sheets | The tabs along the bottom: **Sheet 1**, **Sheet 2**, ... |
| **Fields** | The columns of your data, listed in the **Data** pane on the left of each sheet | The **Data** pane |

You build a chart by dragging fields from the Data pane onto the **shelves**: **Columns**, **Rows**, **Filters** and the **Marks** card.

!!! note "Tableau never changes your file"

    Everything you do in Tableau (calculations, filters, renamed fields) lives in the workbook. The original Excel file stays as it was.

### One file, several tables

The Superstore file has three sheets: **Orders**, **People** and **Returns**. In Tableau each sheet can become a **table** in the data source. You can link two tables with a **relationship**: a line that says which field they share. In the lab you link **Orders** to **Returns** on **Order ID**, so you can tell which orders were returned.

---

## Part 2: Dimensions and measures

When Tableau connects, it sorts every field into one of two groups.

| Group | What it is | Examples in Superstore | What Tableau does with it |
|---|---|---|---|
| **Dimension** | A label you group or split by | Segment, Region, Category, Order ID, Order Date | Makes one header, bar or mark per value |
| **Measure** | A number you add up or summarise | Sales, Profit, Quantity, Discount | Aggregates it, by default with **SUM** |

In the Data pane, dimensions are listed above the line and measures below it.

!!! warning "Tableau's first guess is not always right"

    Tableau guesses from the data type. A number is not always a quantity. **Row ID** is a number, but adding Row IDs up means nothing. It is an identifier. If an ID shows up as a measure, drag it up into the dimensions, or right-click it and choose **Convert to Dimension**.

This is the same idea as the **levels of measurement** in the [Session 2 lecture](../lectures/02_data_and_grain_lecture.md): ask what a column *means* before you decide what to do with it.

---

## Part 3: Discrete and continuous

Tableau also marks every field as **discrete** or **continuous**. The colour tells you which.

| Type | Colour | What it draws | Example |
|---|---|---|---|
| **Discrete** | **Blue** | Separate headers, one per value | Segment on Rows gives one row per segment |
| **Continuous** | **Green** | An axis, a smooth range of values | SUM(Sales) on Columns gives a horizontal axis |

Dimensions are usually blue and measures usually green, but the two ideas are separate:

- **Dimension or measure** decides whether Tableau groups by the field or adds it up.
- **Discrete or continuous** decides whether Tableau draws headers or an axis.

Dates show the difference clearly. Drag **Order Date** to Columns and you get **YEAR(Order Date)** in blue: one header per year. Right-click it and choose the second **Year** in the menu (the green one) and you get a continuous time axis instead.

!!! tip "Read the pill colour first"

    When a chart looks strange, look at the colour of each pill on the shelves. A blue pill where you expected green (or the reverse) explains many surprises.

---

## Part 4: Aggregation and the level of detail

When you drag a measure into a view, Tableau does not show every row. It **aggregates**: it adds up (or counts, or averages) the rows that belong to each mark.

- Drag **Sales** to Columns on an empty sheet. You get one bar: **SUM(Sales)** over every row.
- Now drag **Segment** to Rows. You get one bar per segment. Each bar adds up only that segment's rows.

The dimensions in the view set the **level of detail**: how many marks there are and which rows go into each one. Add a dimension and the view splits into more, smaller marks. Remove one and the marks merge.

### Common aggregations

| Aggregation | What it does | Example |
|---|---|---|
| **SUM** | Adds the values | Total Sales |
| **AVG** | Mean of the values | Average Sales per line |
| **MEDIAN** | Middle value | Median Sales per line |
| **COUNT** | Counts rows with a value | Number of order lines |
| **COUNTD** | Counts **distinct** values | Number of different Order IDs, that is, orders |
| **MIN** / **MAX** | Smallest / largest value | First and last order date |

To change an aggregation, right-click a green pill and choose **Measure → ...**.

!!! warning "Rows are not orders"

    Superstore has one row per **order line**. An order with three products has three rows. So counting rows counts order lines, not orders. To count orders, use **COUNTD([Order ID])**. You did the same in Python with `nunique()`.

### The row-count field

Tableau adds a field to each table called **Orders (Count)** (named after the table). It counts **rows**. In Superstore that means order lines.

---

## Part 5: The Marks card

The **Marks** card controls how each mark looks. It sits to the left of the view.

| Control | What it does |
|---|---|
| **Mark type** (drop-down) | Bar, line, circle, square, text, and more. **Automatic** lets Tableau choose |
| **Color** | Colours marks by a field |
| **Size** | Sizes marks by a field |
| **Label** | Writes a value on or next to each mark |
| **Detail** | Adds a dimension to the level of detail **without** a header or colour |
| **Tooltip** | Sets what appears when you hover over a mark |

**Detail** is the one people forget. Put **Order ID** on Detail and you get one mark per order, even though no Order ID header appears. You use this in the lab for the ship-days box plot.

---

## Part 6: Filters and their order

Tableau can filter at several stages. Each stage happens **before** the next one, so the order changes your results.

| Order | Filter type | Where you set it | What it affects |
|---|---|---|---|
| 1 | **Extract filter** | When you create an extract of the data | Which rows are copied into the extract |
| 2 | **Data source filter** | The **Data Source** page, top right: **Filters → Add** | Every sheet in the workbook |
| 3 | **Dimension filter** | Drag a dimension (for example Region) to the **Filters** shelf | One sheet, unless you apply it to more |
| 4 | **Measure filter** | Drag a measure (for example SUM(Sales)) to the **Filters** shelf | One sheet; keeps only marks whose total passes the test |

!!! note "Two more stages you will meet later"

    **Context filters** sit between data source and dimension filters, and **table calculation filters** come last. You meet them in T2.

### Why the order matters

A measure filter works on the **aggregated** marks that are left after the dimension filters. Suppose you keep only segments whose SUM(Sales) is above some value, and you also filter to one Region. The Region filter runs first. The segment totals are then smaller, so a segment that passed before may now be removed.

!!! tip "Our scope belongs in a data source filter"

    The course period (orders placed 2023 to 2025) must apply to **every** sheet. That makes it a data source filter. You set it up once in the lab, and every chart after that uses the same scope as the Python sessions.

---

## Part 7: Superstore grain recap

You met the grain of Superstore in the [Session 2 lecture](../lectures/02_data_and_grain_lecture.md).

- One row is one **order line**: one product within an order, identified by **Row ID**.
- One **order**, identified by **Order ID**, can have several lines.
- Segment, Ship Mode, Order Date and Ship Date are the same on every line of an order.
- An order is **returned** when its Order ID appears on the **Returns** sheet. The Returns sheet has one row per returned order, not per line.

In Tableau this means:

| If you want ... | Use ... | Not ... |
|---|---|---|
| Number of order lines | **Orders (Count)** | |
| Number of orders | **COUNTD([Order ID])** | Orders (Count) |
| Number of returned orders | COUNTD([Order ID]) for returned orders | A count of rows marked as returned |
| Value of each order | The order's lines added up | The Sales of a single line |

In the [Session 4 lab](../lectures/04_descriptive_statistics_lab.md) you built a table with one row per order before you described order values. In Tableau you do the same thing by grouping on Order ID, or with an **order total** field that you meet in the T1 lab.

---

## Quiz

Answer these at the start of the T1 lab. Your facilitator will go through the answers.

1. Tableau lists **Row ID** as a measure. Why is that a problem, and what do you do about it?
2. You drag **Region** to Rows and **Sales** to Columns. How many bars do you get, and what does each bar add up?
3. A pill on the Columns shelf is green. Will you see an axis or separate headers?
4. Your colleague drags **Orders (Count)** into a view and says "this is the number of orders". What is it really counting, and which field should they use instead?
5. You add **Order ID** to the **Detail** control on the Marks card. What changes in the view, and why is there no Order ID header?
6. You want every sheet in your workbook to use only orders placed from 2023 to 2025. Which filter type do you use, and why not a filter on the Filters shelf of one sheet?
