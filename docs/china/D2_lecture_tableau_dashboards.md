# Day 2 lecture: Building dashboards in Tableau

<p class="lead">
This morning you learned what makes a chart and a dashboard clear. This afternoon you build them in Tableau: connecting to data, dimensions and measures, aggregation, the Marks card, filters, calculated fields, sheets, dashboards, actions, formatting and printing to PDF. Short Python cells show the same ideas in pandas, so you can see that both tools do the same arithmetic.
</p>

Open **Tableau Desktop** and this notebook side by side. Follow the numbered steps in Tableau; run the Python cells in JupyterLab with **Shift + Enter**.

---

## What you will be able to do

1. Connect Tableau to a saved data source and to a CSV file, and check the data types.
2. Tell **dimensions** from **measures** and **discrete** (blue) from **continuous** (green) fields.
3. Explain how Tableau **aggregates** a measure for each mark, and change the aggregation.
4. Use the **Marks card** (Color, Size, Label, Detail, Tooltip) and the **Filters** shelf.
5. Write a **calculated field**, including a ratio KPI computed as a **ratio of sums**.
6. Assemble sheets into a **dashboard**, add a **filter action**, and format it for a reader.
7. Save a packaged workbook and **print a dashboard to PDF** for submission.

**Reading:** Tableau Software (n.d.), *What is data visualization?* and *Tableau for students* (licence and download).

| Part | Topic |
|---|---|
| 1 | The Tableau workspace |
| 2 | Connecting to data |
| 3 | Dimensions and measures, discrete and continuous |
| 4 | Aggregation and the level of detail |
| 5 | The Marks card |
| 6 | Filters |
| 7 | Calculated fields and a ratio KPI |
| 8 | From sheets to a dashboard |
| 9 | Actions: making the dashboard interactive |
| 10 | Formatting for the reader |
| 11 | Saving, printing to PDF and publishing |
| 12 | Assignment 1 briefing |

> **Field names differ between versions**
>
> Tableau has changed its Sample – Superstore data several times: dates, field names (*State* or *State/Province*) and some values differ between versions. Use the names you see in **your** Data pane. When a CSV column is called `total_bill`, Tableau may display it as **Total Bill**; it is the same field.


```python
import pandas as pd

pd.set_option("display.float_format", "{:,.2f}".format)
tips = pd.read_csv("data/tips.csv")
print("Rows (bills):", len(tips))
print("Columns:", list(tips.columns))
```

    Rows (bills): 244
    Columns: ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']


---

## Part 1: The Tableau workspace

When you open a worksheet, the screen has the same parts every time:

| Area | Where | What it does |
|---|---|---|
| **Data pane** | Left | Lists the fields of the connected data, dimensions above the line, measures below |
| **Columns** and **Rows** shelves | Top | Fields placed here define the chart's axes and headers |
| **Marks card** | Left of the view | Chooses the mark type and what drives colour, size, labels, detail and tooltips |
| **Filters** shelf | Above the Marks card | Fields placed here limit which rows are used |
| **View** (canvas) | Centre | The chart itself |
| **Show Me** | Top right | Suggests chart types for the fields you have selected |
| **Sheet tabs** | Bottom | Worksheets, dashboards and stories; plus the **Data Source** tab |

The three icons next to the sheet tabs create a **new worksheet**, a **new dashboard** and a **new story**.

> **How Tableau thinks**
>
> You never write "draw a bar chart". You drag **fields** onto **shelves**, and Tableau decides the chart from what you placed where. A measure on Rows and a dimension on Columns gives a bar chart; a date on Columns gives a line. **Show Me** is a shortcut, not a different method.

---

## Part 2: Connecting to data

### The built-in sample

1. Open Tableau Desktop. On the start page, under **Saved Data Sources** (left side), click **Sample – Superstore**.
2. A blank worksheet, **Sheet 1**, opens. The Data pane lists tables such as *Orders*, *People* and *Returns*.

### A CSV file

1. On the start page, under **Connect → To a File**, click **Text file**.
2. Go to the course folder `notebooks/China_Classroom/data/` and open `tips.csv`.
3. The **Data Source** page shows a preview of the rows. Above each column an icon shows the **data type** Tableau guessed:

| Icon | Type | Example in tips |
|---|---|---|
| **#** | Number | `total_bill`, `tip`, `size` |
| **Abc** | Text (string) | `sex`, `smoker`, `day`, `time` |
| Calendar | Date | (none in tips) |
| Globe | Geographic | (none in tips) |

4. Click a type icon to change it if the guess is wrong. Then click the **Sheet 1** tab at the bottom to start building.

> **Check what one row means**
>
> As in Python, look at the preview and say what one row is before you build anything. In `tips.csv` one row is **one bill** (one table served). In Superstore's *Orders* table one row is **one order line** (one product in one order), not one order.

The Python version of "connect and preview" is the cell you ran above, plus `head()`:


```python
tips.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



---

## Part 3: Dimensions and measures, discrete and continuous

Tableau sorts every field in two ways.

| | Meaning | Examples | Typical use |
|---|---|---|---|
| **Dimension** | A field you group **by**: categories, names, dates | Category, Region, `day`, `smoker` | Headers, colours, filters |
| **Measure** | A number you **aggregate** (add up, average) | Sales, Profit, `total_bill`, `tip` | Axes, bar lengths, sizes |

And separately, by colour of the pill:

| Pill colour | Kind | What it draws |
|---|---|---|
| **Blue** | **Discrete**: separate values | Headers and separate panes (Jan, Feb, Mar as labels) |
| **Green** | **Continuous**: a range of values | An axis (a time line from 2023 to 2026) |

Usually dimensions are discrete and measures continuous, but not always. A date can be either: **YEAR(Order Date)** as a blue pill gives one column per year; a green continuous month gives one long timeline. In Lab 2 you will change a date pill from discrete to continuous to draw a monthly trend.

> **A number that is really a category**
>
> In `tips.csv`, `size` (the number of people at the table) arrives as a measure, so Tableau would **add it up**. To compare party sizes, right-click `size` in the Data pane → **Convert to Dimension**, and Tableau treats each size as a group. In Python the same decision is whether you write `groupby("size")` or `["size"].sum()`.

> **Check your understanding**
>
> For each Superstore field, say dimension or measure, and discrete or continuous in a typical chart: *Region*, *Sales*, *Order Date* on a monthly trend line, *Quantity*, *Customer Name*.

---

## Part 4: Aggregation and the level of detail

When you drag a measure into the view, Tableau does not draw one mark per row. It draws **one mark for each combination of the dimensions in the view**, and **aggregates** the measure inside each mark. The default aggregation is **SUM**.

**In Tableau (with Sample – Superstore):**

1. Drag **Region** to Columns and **Sales** to Rows. The pill reads `SUM(Sales)`: one bar per region, each the total of its order lines.
2. Right-click the `SUM(Sales)` pill → **Measure (Sum)** → **Average**. The pill becomes `AVG(Sales)` and each bar shows the average **order line**, a different question.
3. Drag **Segment** to Color. Now there is one mark for each region **and** segment: the **level of detail** got finer, and each mark aggregates fewer rows.

The same three steps in pandas, on the tips data (grouping by `smoker` instead of Region):


```python
# Step 1: SUM, one value per group (Tableau's default).
print("SUM(total_bill) by smoker:")
print(tips.groupby("smoker")["total_bill"].sum().round(2))

# Step 2: AVG, the same groups, a different question.
print("\nAVG(total_bill) by smoker:")
print(tips.groupby("smoker")["total_bill"].mean().round(2))

# Step 3: a finer level of detail, one value per smoker AND time.
print("\nSUM(total_bill) by smoker and time:")
print(tips.groupby(["smoker", "time"])["total_bill"].sum().round(2))
```

    SUM(total_bill) by smoker:
    smoker
    No    2,897.43
    Yes   1,930.34
    Name: total_bill, dtype: float64
    
    AVG(total_bill) by smoker:
    smoker
    No    19.19
    Yes   20.76
    Name: total_bill, dtype: float64
    
    SUM(total_bill) by smoker and time:
    smoker  time  
    No      Dinner   2,130.14
            Lunch      767.29
    Yes     Dinner   1,530.16
            Lunch      400.18
    Name: total_bill, dtype: float64


| Tableau | pandas |
|---|---|
| Dimensions in the view (Columns, Rows, Color, Detail…) | The columns in `groupby([...])` |
| `SUM(Sales)` | `["sales"].sum()` |
| `AVG(Sales)` | `["sales"].mean()` |
| `CNT(Sales)` / `COUNTD(Order ID)` | `.size()` / `["order_id"].nunique()` |
| One mark | One row of the grouped result |

> **Predict, then reveal**
>
> In Tableau you put **Category** on Rows and `SUM(Sales)` on Columns: 3 bars. Then you drag **Order ID** onto **Detail**. How many marks do you expect now, and why does the chart stop making sense? (Try it.)

---

## Part 5: The Marks card

The **Marks card** controls how each mark looks.

| Button | What it encodes | Good use | Watch out |
|---|---|---|---|
| **Mark type** (dropdown) | Bar, Line, Circle, Square, Text, Map, Pie… | Leave on Automatic until you need a specific type | Pie only for two or three parts |
| **Color** | A dimension (categories) or measure (scale) | Highlight one thing, or profit (diverging) | Rainbow palettes; colour alone |
| **Size** | A measure | Secondary information | Area is read inaccurately (this morning, Part 2) |
| **Label** | Writes values on marks | Direct labels instead of an axis | Too many labels clutter |
| **Detail** | Splits marks without encoding them | Needed for maps and for tooltip fields | Makes the level of detail finer |
| **Tooltip** | Text shown on hover | Exact values, definitions | Hover does not exist on a printed PDF |

**Try it (Superstore):** on a sheet with **Sub-Category** on Rows and `SUM(Sales)` on Columns, drag **Profit** onto **Color**. Tableau uses a **diverging orange–blue** palette centred on zero: orange for losses, blue for profits. This is this morning's diverging palette, chosen automatically because Profit can be negative. Click **Color → Edit Colors** to check where the centre sits.

---

## Part 6: Filters

A filter limits **which rows** reach the view.

1. Drag a dimension (for example **Region**) to the **Filters** shelf, tick the values to keep, click **OK**.
2. Right-click the pill on the Filters shelf → **Show Filter** to put a filter control next to the chart for the reader.
3. To make one filter change several sheets: on the filter control's menu (small arrow) → **Apply to Worksheets → All Using This Data Source** (or **Selected Worksheets**).
4. Measures can be filtered too: drag **Sales** to Filters and choose a range of `SUM(Sales)`.

In pandas, a filter is a boolean condition applied **before** grouping:


```python
dinner = tips[tips["time"] == "Dinner"]          # filter: keep dinner bills only
print("Bills after the filter:", len(dinner), "of", len(tips))
dinner.groupby("smoker")["tip"].sum().round(2)  # then aggregate, as Tableau does
```

    Bills after the filter: 176 of 244





    smoker
    No    331.45
    Yes   214.62
    Name: tip, dtype: float64



> **State the filter on the page**
>
> A filtered chart answers a narrower question. Put the filter in the title or the scope note ("Dinner bills only"), or the reader will assume the whole dataset.

---

## Part 7: Calculated fields and a ratio KPI

A **calculated field** is a new field defined by a formula. Create one with **Analysis → Create Calculated Field**, or right-click in the Data pane → **Create → Calculated Field**. Give it a name, type the formula, and check that the message under the box says **The calculation is valid**.

### Row-level versus aggregate calculations

| Formula | What Tableau does | Result in the view (with AVG) |
|---|---|---|
| `[Tip] / [Total Bill]` | Computes the ratio for **every row**, then you aggregate it (Tableau suggests SUM; you would choose AVG) | The **mean of ratios**: each bill's tip % averaged |
| `SUM([Tip]) / SUM([Total Bill])` | Adds up the tips and the bills for each mark, **then** divides | The **ratio of sums**: the share of all spending that went to tips |

This morning (Part 11) you saw that these answer different questions, and that a KPI tile should normally use the **ratio of sums**. In Tableau, the `SUM(...) / SUM(...)` form is how you write it. Superstore's standard KPI is:

```
Profit Ratio = SUM([Profit]) / SUM([Sales])
```

After creating it, right-click the field → **Default Properties → Number Format → Percentage** so it always displays as a percentage.

Here are both versions in pandas, for each value of `smoker`:


```python
kpi = tips.groupby("smoker").agg(tips_sum=("tip", "sum"), bills_sum=("total_bill", "sum"))
kpi["ratio of sums %"] = 100 * kpi["tips_sum"] / kpi["bills_sum"]          # SUM([Tip]) / SUM([Total Bill])
kpi["mean of ratios %"] = 100 * (tips["tip"] / tips["total_bill"]).groupby(tips["smoker"]).mean()  # AVG([Tip] / [Total Bill])
kpi
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tips_sum</th>
      <th>bills_sum</th>
      <th>ratio of sums %</th>
      <th>mean of ratios %</th>
    </tr>
    <tr>
      <th>smoker</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>No</th>
      <td>451.77</td>
      <td>2,897.43</td>
      <td>15.59</td>
      <td>15.93</td>
    </tr>
    <tr>
      <th>Yes</th>
      <td>279.81</td>
      <td>1,930.34</td>
      <td>14.50</td>
      <td>16.32</td>
    </tr>
  </tbody>
</table>
</div>



The two percentage columns in the output above differ. Look closely: do they even rank smokers and non-smokers in the **same order**? If a dashboard tile said "Tip rate" without saying which one, two analysts could report different numbers from the same data. **Name the formula** in the tile or the scope note.

> **Other useful calculations**
>
> - `IF SUM([Profit]) < 0 THEN "Loss" ELSE "Profit" END`: a label you can put on Color.
> - `DATEDIFF('day', [Order Date], [Ship Date])`: days to ship, per row.
> - `COUNTD([Order ID])`: distinct orders, because Superstore has several rows per order.

> **Check your understanding**
>
> In Superstore, why does `AVG([Profit] / [Sales])` give a different number from `SUM([Profit]) / SUM([Sales])` for the whole company? Which one would you put on an executive dashboard, and why?

---

## Part 8: From sheets to a dashboard

A dashboard is built from **worksheets**: build and title each chart on its own sheet first, then arrange them.

### Plan before you build

Use this morning's principles. On paper, sketch:

1. The **decision** and the **audience** (for example: a regional manager deciding which products to review).
2. The **3–5 views**, each answering one part of the question.
3. The **layout**: headline and KPIs at the top left, detail below and to the right.

### Build

1. Build each sheet and **rename its tab** (double-click the tab), for example *Sales trend*, *Profit by state*, *Sales by sub-category*. The tab name becomes the default title on the dashboard.
2. Click the **New Dashboard** icon at the bottom.
3. On the left, under **Size**, choose **Automatic** so the dashboard fills the screen (or a **Fixed size** such as A4 landscape if you will print it).
4. Under **Sheets**, drag each sheet onto the canvas. Grey shaded areas show where it will land: top, bottom, left or right of what is already there.
5. Leave objects **Tiled** (the default) so they line up in a grid; **Floating** objects sit on top and are easy to misalign.
6. Add a **Text** object (under **Objects**) for the headline message and a small one for the scope note (period, data source, units).
7. Remove legends you do not need (click the legend → **x**), and delete repeated titles.

> **Check your understanding**
>
> Your dashboard has six sheets and three legends and still has no headline. Using this morning's principles, name three changes.

---

## Part 9: Actions: making the dashboard interactive

**Actions** let a click on one view change the others.

### The quick way: Use as Filter

1. On the dashboard, click once on a view (for example a map) to select it. A grey border appears with small icons at its top right.
2. Click the **funnel** icon (**Use as Filter**). Now clicking a mark in that view (a state) **filters** every other view on the dashboard.
3. To clear the selection, click the same mark again, or click an empty part of the view, or press **Esc**.

### The full way: Dashboard → Actions

**Dashboard → Actions → Add Action** offers:

| Action | Effect |
|---|---|
| **Filter** | Clicking a mark keeps only the matching rows in the target views (this is what *Use as Filter* creates) |
| **Highlight** | Clicking a mark highlights matching marks elsewhere and greys the rest, without removing them |
| **Go to Sheet / URL / parameter / set** | Navigation and advanced uses |

For each action choose the **source sheet**, **target sheets**, and whether it runs on **Hover**, **Select** (click) or **Menu**, and what happens when the selection is cleared (**Show all values** is usually what a reader expects).

In Python there is no clicking, but the idea of one filter driving every view is a function with a parameter. Every number below is recomputed for the chosen group:


```python
def mini_dashboard(data, smoker=None):
    """Recompute every KPI for one selection, as a dashboard filter action does."""
    view = data if smoker is None else data[data["smoker"] == smoker]
    return pd.Series({
        "bills": len(view),
        "total spend (dollars)": view["total_bill"].sum(),
        "tip rate, sum/sum (%)": 100 * view["tip"].sum() / view["total_bill"].sum(),
        "average party size": view["size"].mean(),
    }).round(2)


pd.DataFrame({
    "All bills": mini_dashboard(tips),
    "Click: smoker = Yes": mini_dashboard(tips, "Yes"),
    "Click: smoker = No": mini_dashboard(tips, "No"),
})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>All bills</th>
      <th>Click: smoker = Yes</th>
      <th>Click: smoker = No</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bills</th>
      <td>244.00</td>
      <td>93.00</td>
      <td>151.00</td>
    </tr>
    <tr>
      <th>total spend (dollars)</th>
      <td>4,827.77</td>
      <td>1,930.34</td>
      <td>2,897.43</td>
    </tr>
    <tr>
      <th>tip rate, sum/sum (%)</th>
      <td>15.15</td>
      <td>14.50</td>
      <td>15.59</td>
    </tr>
    <tr>
      <th>average party size</th>
      <td>2.57</td>
      <td>2.41</td>
      <td>2.67</td>
    </tr>
  </tbody>
</table>
</div>



> **Actions do not print**
>
> A PDF shows one state of the dashboard. Before printing, **clear all selections** so the reader sees the whole picture, unless the assignment asks for a filtered view; then say in a caption which state is selected.

---

## Part 10: Formatting for the reader

Apply this morning's design rules inside Tableau:

| Goal | Where in Tableau |
|---|---|
| **Message titles** | Double-click a sheet title on the dashboard and type the finding; keep units in the axis title |
| **Sort** bars by value | The **Sort Descending** button in the toolbar, or right-click the dimension → **Sort** |
| **Number formats** (thousands separators, %) | Right-click the measure pill or axis → **Format** → Numbers |
| **Colour-blind-safe colours** | **Color → Edit Colors** → choose the **Color Blind** palette for categories; keep orange–blue for profit and loss |
| **Remove clutter** | **Format → Lines**: set grid lines to None; right-click an axis → uncheck **Show Header** when bars are labelled |
| **Direct labels** | Click **Label** on the Marks card → **Show mark labels** |
| **Readable tooltips** | Click **Tooltip** on the Marks card and rewrite it as a sentence |
| **Scope note** | A small Text object at the bottom: data source, period, filters, units |

> **Bars still start at zero in Tableau**
>
> Tableau's bar axes start at zero by default. If you right-click an axis → **Edit Axis** and untick **Include zero**, you have built this morning's misleading truncated bar chart.

---

## Part 11: Saving, printing to PDF and publishing

| Task | How | Notes |
|---|---|---|
| **Save your work** | **File → Save As** → *Tableau Packaged Workbook* (`.twbx`) | A `.twbx` contains the data, so it opens on another computer. A `.twb` does not |
| **Print to PDF** (for GAP) | **File → Print to PDF** → *Range*: **Active Sheet** (with the dashboard tab open) → **OK** → choose a file name | Choose landscape paper; check that nothing is cut off |
| **Export an image** | **Dashboard → Export Image** | Useful for a Word report |
| **Publish to the web** | **Server → Tableau Public → Save to Tableau Public** | Anyone on the internet can see it. **Never publish confidential or personal data**; course submissions go to GAP as PDF |

> **Before you print, check**
>
> 1. The dashboard tab is the **active sheet**.
> 2. No mark is selected and no filter is left on by accident.
> 3. Every title is a message, every axis has units, and the scope note is visible.
> 4. Open the PDF and read it as the reader will: is anything cut off or too small?

---

## Summary

- Tableau draws **one mark per combination of dimensions in the view** and **aggregates** each measure in that mark (SUM by default), exactly like `groupby` in pandas.
- **Blue** pills are discrete (headers), **green** pills are continuous (axes). Dates can be either.
- The **Marks card** maps fields to colour, size, label, detail and tooltip; the **Filters** shelf limits rows.
- Ratio KPIs are calculated fields written as `SUM([numerator]) / SUM([denominator])`.
- A dashboard is a few titled sheets, laid out for one decision, connected by **actions**, with a headline and a scope note.
- Submit dashboards as a **PDF** from **File → Print to PDF**; keep a `.twbx` copy of your work.

---

## Closing quiz

1. What is the difference between a dimension and a measure? Give one example of each from Superstore.
2. A pill is green. What does that tell you, and what will it draw?
3. You put `SUM(Sales)` on Rows and **Region** on Columns, then add **Segment** to Color. What happens to the number of marks?
4. Write the calculated field for a profit ratio KPI. Why not `AVG([Profit] / [Sales])`?
5. What does the funnel (**Use as Filter**) icon on a dashboard view do?
6. Name two things to check before **Print to PDF**.

---

## Part 12: Assignment 1 briefing

> **Assignment 1: Data visualisation and descriptive analytics report** (6%, CLO 1–3)
>
> **Due Sunday 15 November 2026, 23:59 China Standard Time**, on **GAP (Moodle)**.

You act as an analytics consultant for **Bistro Analytics**, advising a busy restaurant. Using the tips data (244 bills), you run a Python notebook that produces two summary tables and three figures, then write a short **business report** with four fixed sections:

1. Executive summary
2. Descriptive data overview
3. Visual insights and graphical trends
4. Strategic business recommendations

The restaurant owner wants help with two decisions: **when to schedule the strongest staff** and **how to raise revenue and server income through upselling**.

Everything you learned today applies: message titles, honest axes, ratio of sums, and turning findings into a recommendation for a specific audience.

**Start here:** [Assignment 1 brief and starter notebook](D2_assignment1_tips_report.md). Open `D2_assignment1_tips_report.ipynb` in JupyterLab, read the brief, and save your own copy as `YourLastName_DATA300_Assignment1.ipynb`.

After this briefing, the lab starts with [Applied Lab 2: Dashboard creation](D2_lab_lab2_dashboard.md). If you finish the lab early, start Assignment 1.
