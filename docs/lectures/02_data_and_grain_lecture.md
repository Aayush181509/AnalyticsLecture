# Session 2 lecture: Data, grain and the DataFrame

<p class="lead">
Before you add anything up, know what kind of data each column holds, what one row stands for, and whether the table can be trusted.
</p>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Aayush181509/AnalyticsLecture/blob/main/notebooks/02_data_and_grain_lecture.ipynb)

Open this notebook in Google Colab with the button above, then run each cell from top to bottom with **Shift + Enter**. Save your own copy with **File → Save a copy in Drive**.

---

## Recap quiz

Start by answering the quiz at the end of the Session 1 lecture, [`01_why_data_analytics_lecture.md`](01_why_data_analytics_lecture.md). Write your answers down before the discussion.

---

## What you will be able to explain

1. The four **levels of measurement** and which calculations make sense for each.
2. What makes a table **tidy**.
3. The **grain** of a table, and the job of **primary** and **foreign keys**.
4. What a **data dictionary** records and why every analysis needs one.
5. Five **data-quality dimensions** and a pandas check for each.

| Part | Topic |
|---|---|
| 1 | Levels of measurement |
| 2 | Tidy data |
| 3 | Grain and keys |
| 4 | Data dictionaries |
| 5 | Data-quality dimensions |
| 6 | Worked case: the Superstore order lines |

> **How to use this notebook**
>
> When you see **Predict, then reveal**, write your guess first and only then run the cell. Being wrong on paper is the fastest way to learn.

Run the setup cell first. It prepares pandas, the chart style and the retail table used in Part 6.


```python
# Course data setup. Run this cell first; you do not need to understand it yet.
# It downloads the Superstore sample from Tableau's website, checks it is the
# exact version this course was written for, and prepares the order-lines table.
import hashlib
import os
import urllib.request

import matplotlib.pyplot as plt
import pandas as pd

SOURCE_URL = "https://public.tableau.com/app/sample-data/sample_-_superstore.xls"
EXPECTED_SHA256 = "5045ed4fec49cae2cc0dfc5ab0d204ba09efa767fe00c996822499e8cc42fbbd"
SOURCE_FILE = os.environ.get("COURSE_XLS_PATH", "sample_-_superstore.xls")

try:
    import xlrd  # noqa: F401  (needed to read .xls files)
except ImportError:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "xlrd"])

if not os.path.exists(SOURCE_FILE):
    urllib.request.urlretrieve(SOURCE_URL, SOURCE_FILE)

with open(SOURCE_FILE, "rb") as f:
    digest = hashlib.sha256(f.read()).hexdigest()
if digest != EXPECTED_SHA256:
    print("WARNING: Tableau has changed this sample file since the course was written.")
    print("Your numbers will differ from the lesson. Ask your facilitator for the course copy.")


def load_orders():
    """Return one row per order line, orders placed 2023-01-01 to 2025-12-31."""
    raw = pd.read_excel(SOURCE_FILE, sheet_name="Orders")
    returns = pd.read_excel(SOURCE_FILE, sheet_name="Returns")

    # Orders with more than one Customer ID (a known data issue), found before filtering.
    ids_per_order = raw.groupby("Order ID")["Customer ID"].nunique()
    conflict_orders = set(ids_per_order[ids_per_order > 1].index)

    in_scope = (raw["Order Date"] >= "2023-01-01") & (raw["Order Date"] < "2026-01-01")
    df = raw.loc[in_scope].copy()

    df = df.rename(columns={
        "Row ID": "row_id", "Order ID": "order_id", "Order Date": "order_date",
        "Ship Date": "ship_date", "Ship Mode": "ship_mode", "Customer ID": "customer_id",
        "Segment": "segment", "Country/Region": "country_region", "Region": "region",
        "Category": "category", "Sub-Category": "sub_category", "Product ID": "product_id",
        "Product Name": "product_name", "Sales": "sales", "Quantity": "quantity",
        "Discount": "discount", "Profit": "profit",
    })
    df["returned_order_flag"] = df["order_id"].isin(set(returns["Order ID"])).astype(int)
    df["customer_order_conflict"] = df["order_id"].isin(conflict_orders).astype(int)
    df["customer_analysis_eligible"] = 1 - df["customer_order_conflict"]
    df["order_to_ship_days"] = (df["ship_date"] - df["order_date"]).dt.days
    df["order_month"] = df["order_date"].dt.to_period("M").dt.to_timestamp()

    columns = [
        "row_id", "order_id", "order_date", "ship_date", "ship_mode", "customer_id",
        "segment", "country_region", "region", "category", "sub_category", "product_id",
        "product_name", "sales", "quantity", "discount", "profit", "returned_order_flag",
        "customer_analysis_eligible", "customer_order_conflict", "order_to_ship_days",
        "order_month",
    ]
    return df[columns].sort_values("row_id").reset_index(drop=True)


pd.set_option("display.float_format", "{:,.2f}".format)
plt.rcParams.update({
    "figure.figsize": (8, 4),
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.axisbelow": True,
    "grid.color": "#e6e5e1",
    "axes.prop_cycle": plt.cycler(color=["#2a78d6", "#eb6834", "#1baf7a"]),
    "axes.titleweight": "bold",
    "axes.titlelocation": "left",
})
print("Setup complete.")
```

    Setup complete.


---

## Part 1: Levels of measurement

Not every number is a quantity. A postcode, a shirt size and a temperature are all written with digits or ordered labels, yet you cannot treat them the same way.

Statisticians sort variables into four **levels of measurement**. Each level allows everything the level above it allows, plus something new.

| Level | What the values do | Examples | What makes sense |
|---|---|---|---|
| **Nominal** | Name a group; no order | Segment, region, product ID, postcode | Count, share, mode |
| **Ordinal** | Name a group **in order**; gaps not equal | Shirt size, satisfaction 1–5, ship class | + median, percentiles, "higher than" |
| **Interval** | Ordered with **equal gaps**, but zero is arbitrary | Temperature in °C, calendar dates | + differences, mean |
| **Ratio** | Equal gaps and a **true zero** | Sales, quantity, days to ship, age | + ratios: "twice as much" |

Nominal and ordinal variables are **categorical**. Interval and ratio variables are **numeric** (quantitative).

### Predict, then reveal: is 20 °C twice as hot as 10 °C?

Write down *yes* or *no*, then run the cell. It converts both temperatures to Fahrenheit and compares the ratios.


```python
celsius = pd.Series([10, 20], index=["cool day", "warm day"])
fahrenheit = celsius * 9 / 5 + 32

print("Ratio in Celsius:   ", celsius["warm day"] / celsius["cool day"])
print("Ratio in Fahrenheit:", round(fahrenheit["warm day"] / fahrenheit["cool day"], 2))
print("Difference in Celsius:", celsius["warm day"] - celsius["cool day"], "degrees")
```

    Ratio in Celsius:    2.0
    Ratio in Fahrenheit: 1.36
    Difference in Celsius: 10 degrees


The ratio changes when the unit changes, because 0 °C is not "no temperature". So ratios on an **interval** scale mean nothing. The **difference** is meaningful in either unit.

Sales is different: 0 really means no sales, so "Region A sold twice as much as Region B" stays true whatever the currency. That is a **ratio** scale.

### Predict, then reveal: numbers that are not quantities

The table below is made up. pandas sees three numeric columns. Which of the three averages printed by the next cell actually mean something?


```python
survey = pd.DataFrame({
    "customer": ["C1", "C2", "C3", "C4", "C5", "C6"],
    "postcode": [44600, 44700, 44600, 33700, 44600, 44800],
    "satisfaction_1_to_5": [5, 4, 5, 1, 4, 2],
    "orders_last_year": [3, 1, 6, 2, 0, 4],
})
print(survey.dtypes, end="\n\n")
survey[["postcode", "satisfaction_1_to_5", "orders_last_year"]].mean()
```

    customer               object
    postcode                int64
    satisfaction_1_to_5     int64
    orders_last_year        int64
    dtype: object
    





    postcode              42,833.33
    satisfaction_1_to_5        3.50
    orders_last_year           2.67
    dtype: float64



- **Postcode** is nominal. The average postcode is not a place.
- **Satisfaction** is ordinal. The gap between 1 and 2 need not equal the gap between 4 and 5, so the mean is risky. The median and the share of 4s and 5s are safer.
- **Orders last year** is ratio. Its mean is meaningful.

The right summaries for the first two:


```python
print("Most common postcode:", survey["postcode"].mode()[0])
print("Median satisfaction: ", survey["satisfaction_1_to_5"].median())
print("Share scoring 4 or 5:", (survey["satisfaction_1_to_5"] >= 4).mean())
```

    Most common postcode: 44600
    Median satisfaction:  4.0
    Share scoring 4 or 5: 0.6666666666666666


### Telling pandas about order

An ordinal column stored as text sorts alphabetically, which is wrong. An **ordered categorical** keeps the real order.


```python
sizes = pd.Series(["M", "S", "XL", "L", "S", "M"])
print("Alphabetical:", sorted(sizes.unique()))

sizes = pd.Categorical(sizes, categories=["S", "M", "L", "XL"], ordered=True)
print("Real order:  ", list(sizes.categories))
print("Largest size:", sizes.max())
```

    Alphabetical: ['L', 'M', 'S', 'XL']
    Real order:   ['S', 'M', 'L', 'XL']
    Largest size: XL


> **Check your understanding 1**
>
> Classify each Superstore column as nominal, ordinal, interval or ratio: `segment`, `ship_mode`, `order_date`, `sales`, `quantity`, `order_to_ship_days`, `row_id`. For one of them, explain why someone could reasonably argue for two levels.

> **Remember**
>
> The data type pandas shows (`int64`, `object`) is about **storage**. The level of measurement is about **meaning**. An ID stored as a number is still nominal.

---

## Part 2: Tidy data

A table is **tidy** when:

1. Each **variable** is a column.
2. Each **observation** is a row.
3. Each **value** is a single cell.

Spreadsheets for people are often not tidy: months spread across columns look good on a page but are awkward to filter, group and chart.


```python
wide = pd.DataFrame({
    "region": ["North", "South", "East"],
    "Jan": [120, 95, 80],
    "Feb": [130, 90, 85],
    "Mar": [150, 110, 70],
})
wide
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
      <th>region</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>North</td>
      <td>120</td>
      <td>130</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South</td>
      <td>95</td>
      <td>90</td>
      <td>110</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East</td>
      <td>80</td>
      <td>85</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Predict, then reveal

The table has 3 rows and 3 month columns. After reshaping to one row per **region and month**, how many rows will there be?

`melt` turns column names into values of a new column.


```python
tidy = wide.melt(id_vars="region", var_name="month", value_name="sales")
print("Rows after melt:", len(tidy))
tidy
```

    Rows after melt: 9





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
      <th>region</th>
      <th>month</th>
      <th>sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>North</td>
      <td>Jan</td>
      <td>120</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South</td>
      <td>Jan</td>
      <td>95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East</td>
      <td>Jan</td>
      <td>80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>North</td>
      <td>Feb</td>
      <td>130</td>
    </tr>
    <tr>
      <th>4</th>
      <td>South</td>
      <td>Feb</td>
      <td>90</td>
    </tr>
    <tr>
      <th>5</th>
      <td>East</td>
      <td>Feb</td>
      <td>85</td>
    </tr>
    <tr>
      <th>6</th>
      <td>North</td>
      <td>Mar</td>
      <td>150</td>
    </tr>
    <tr>
      <th>7</th>
      <td>South</td>
      <td>Mar</td>
      <td>110</td>
    </tr>
    <tr>
      <th>8</th>
      <td>East</td>
      <td>Mar</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



Now "sales for March" is a filter and "sales by region" is a `groupby`, both one line of code:


```python
print(tidy[tidy["month"] == "Mar"])
print()
print(tidy.groupby("region")["sales"].sum())
```

      region month  sales
    6  North   Mar    150
    7  South   Mar    110
    8   East   Mar     70
    
    region
    East     235
    North    400
    South    295
    Name: sales, dtype: int64


The opposite move, long to wide, is `pivot`. Use wide tables for **reading**, tidy tables for **analysing**.

A second untidy pattern: two values in one cell.


```python
messy = pd.DataFrame({"customer": ["C1", "C2", "C3"],
                      "segment_region": ["Consumer/West", "Corporate/East", "Consumer/East"]})
messy[["segment", "region"]] = messy["segment_region"].str.split("/", expand=True)
messy
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
      <th>customer</th>
      <th>segment_region</th>
      <th>segment</th>
      <th>region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C1</td>
      <td>Consumer/West</td>
      <td>Consumer</td>
      <td>West</td>
    </tr>
    <tr>
      <th>1</th>
      <td>C2</td>
      <td>Corporate/East</td>
      <td>Corporate</td>
      <td>East</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C3</td>
      <td>Consumer/East</td>
      <td>Consumer</td>
      <td>East</td>
    </tr>
  </tbody>
</table>
</div>



> **Check your understanding 2**
>
> A finance file has one row per department and a column for each of the 12 months' budgets, plus 12 columns for actual spend. Which tidy rule does it break? Sketch the column names of a tidy version.

---

## Part 3: Grain and keys

The **grain** of a table is what **one row** represents: one order, one product within an order, one customer per month, one employee per day.

Grain decides what simple counting means. If a row is a product within an order, then counting rows counts **order lines**, not orders.

Two kinds of key make grain explicit:

| Key | Meaning | Check |
|---|---|---|
| **Primary key** | Column(s) that identify each row uniquely; never missing | No duplicates, no blanks |
| **Foreign key** | Column that points to the primary key of **another** table | Every value exists in that other table |

Here is a tiny made-up shop with three tables at three different grains.


```python
customers = pd.DataFrame({"customer_id": ["C1", "C2", "C3"],
                          "segment": ["Consumer", "Corporate", "Consumer"]})

orders = pd.DataFrame({"order_id": ["O1", "O2", "O3", "O4"],
                       "customer_id": ["C1", "C1", "C2", "C3"],
                       "shipping_fee": [5, 5, 10, 5]})

order_lines = pd.DataFrame({"line_id": [1, 2, 3, 4, 5, 6, 7],
                            "order_id": ["O1", "O1", "O2", "O3", "O3", "O3", "O4"],
                            "product": ["Pen", "Desk", "Chair", "Pen", "Lamp", "Paper", "Desk"],
                            "sales": [4, 200, 150, 4, 30, 8, 220]})
order_lines
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
      <th>line_id</th>
      <th>order_id</th>
      <th>product</th>
      <th>sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>O1</td>
      <td>Pen</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>O1</td>
      <td>Desk</td>
      <td>200</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>O2</td>
      <td>Chair</td>
      <td>150</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>O3</td>
      <td>Pen</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>O3</td>
      <td>Lamp</td>
      <td>30</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>O3</td>
      <td>Paper</td>
      <td>8</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>O4</td>
      <td>Desk</td>
      <td>220</td>
    </tr>
  </tbody>
</table>
</div>



Grain of each table:

- `customers`: one customer, primary key `customer_id`.
- `orders`: one order, primary key `order_id`; `customer_id` is a foreign key.
- `order_lines`: one product within an order, primary key `line_id`; `order_id` is a foreign key.

Check the keys with code:


```python
print("line_id unique in order_lines? ", order_lines["line_id"].is_unique)
print("order_id unique in order_lines?", order_lines["order_id"].is_unique)
print("order_id unique in orders?     ", orders["order_id"].is_unique)
print("Every line's order exists?     ", order_lines["order_id"].isin(orders["order_id"]).all())
print()
print("Rows in order_lines:", len(order_lines))
print("Different orders:   ", order_lines["order_id"].nunique())
```

    line_id unique in order_lines?  True
    order_id unique in order_lines? False
    order_id unique in orders?      True
    Every line's order exists?      True
    
    Rows in order_lines: 7
    Different orders:    4


### Predict, then reveal: the shipping fee trap

We want total shipping fees. The fee lives in `orders` (one per order). A colleague joins it onto the order lines and adds it up.

Look at the `orders` table above and work out the true total fee by hand. Will the colleague's number be the same?


```python
joined = order_lines.merge(orders, on="order_id", how="left", validate="many_to_one")

print("True total fee (orders table):     ", orders["shipping_fee"].sum())
print("Colleague's total (after the join):", joined["shipping_fee"].sum())
joined[["line_id", "order_id", "product", "shipping_fee"]]
```

    True total fee (orders table):      25
    Colleague's total (after the join): 50





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
      <th>line_id</th>
      <th>order_id</th>
      <th>product</th>
      <th>shipping_fee</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>O1</td>
      <td>Pen</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>O1</td>
      <td>Desk</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>O2</td>
      <td>Chair</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>O3</td>
      <td>Pen</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>O3</td>
      <td>Lamp</td>
      <td>10</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>O3</td>
      <td>Paper</td>
      <td>10</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>O4</td>
      <td>Desk</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



After the join, each order's fee appears on **every line** of that order, so summing it counts the fee once per line. The join changed the grain of the fee.

Two habits prevent this:

1. Before adding up a column, ask: *at what grain is this value recorded?*
2. Use `validate=` in `merge` to state the relationship you expect (`"one_to_one"`, `"many_to_one"`, `"one_to_many"`). pandas raises an error if the keys break it.

The correct total, taken back at the order grain:


```python
print("Fee, one per order:", joined.drop_duplicates("order_id")["shipping_fee"].sum())
```

    Fee, one per order: 25


> **Check your understanding 3**
>
> A table has one row per employee per month. What is its primary key? If you sum `headcount = 1` over the whole year, what have you counted?

---

## Part 4: Data dictionaries

A **data dictionary** describes every column so that anyone can use the table correctly without asking you.

| Field | Example for `sales` |
|---|---|
| Name | `sales` |
| Meaning | Sales reported for the order line |
| Type (storage) | `float64` |
| Level of measurement | Ratio |
| Unit | Source monetary units; currency not stated |
| Allowed values | Zero or more |
| Can you add it up? | Yes, across lines and groups |
| Source and changes | Orders sheet, column "Sales"; not changed |

pandas can fill in the mechanical fields for you. The human fields (meaning, unit, "can you add it up?") need your judgement.


```python
def profile_columns(data):
    """One row per column: storage type, missing values, distinct values and an example."""
    return pd.DataFrame({
        "dtype": data.dtypes.astype(str),
        "missing": data.isna().sum(),
        "distinct": data.nunique(),
        "example": data.iloc[0],
    })


profile_columns(order_lines)
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
      <th>dtype</th>
      <th>missing</th>
      <th>distinct</th>
      <th>example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>line_id</th>
      <td>int64</td>
      <td>0</td>
      <td>7</td>
      <td>1</td>
    </tr>
    <tr>
      <th>order_id</th>
      <td>object</td>
      <td>0</td>
      <td>4</td>
      <td>O1</td>
    </tr>
    <tr>
      <th>product</th>
      <td>object</td>
      <td>0</td>
      <td>5</td>
      <td>Pen</td>
    </tr>
    <tr>
      <th>sales</th>
      <td>int64</td>
      <td>0</td>
      <td>6</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



> **Check your understanding 4**
>
> `profile_columns` says `line_id` is `int64` with as many distinct values as rows. Which **human** fields of the dictionary would you add for it, and what would you write under "Can you add it up?"

---

## Part 5: Data-quality dimensions

"Is the data good?" is too vague to check. Break it into **dimensions**, each with a test you can run.

| Dimension | Question | Example pandas check |
|---|---|---|
| **Completeness** | Are values missing that should be present? | `df.isna().sum()` |
| **Validity** | Do values follow the rules (type, range, allowed list)? | `(df["quantity"] > 0).all()` |
| **Consistency** | Do related values agree, within and across tables? | Ship date not before order date |
| **Uniqueness** | Is each real-world thing recorded once? | `df["id"].is_unique`, `df.duplicated()` |
| **Timeliness** | Is the data recent enough, and is the period complete? | `df["date"].max()` versus the reporting date |

Here is a small made-up extract with a problem planted in each dimension. Read it first and try to spot them.


```python
extract = pd.DataFrame({
    "order_id":   ["A1", "A2", "A3", "A3", "A5", "A6"],
    "region":     ["West", "west", "East", "East", None, "South"],
    "order_date": pd.to_datetime(["2025-03-01", "2025-03-02", "2025-03-02", "2025-03-02", "2025-03-04", "2025-03-05"]),
    "ship_date":  pd.to_datetime(["2025-03-03", "2025-03-01", "2025-03-05", "2025-03-05", "2025-03-06", "2025-03-07"]),
    "quantity":   [2, 1, 3, 3, -4, 1],
})
extract
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
      <th>order_id</th>
      <th>region</th>
      <th>order_date</th>
      <th>ship_date</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A1</td>
      <td>West</td>
      <td>2025-03-01</td>
      <td>2025-03-03</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A2</td>
      <td>west</td>
      <td>2025-03-02</td>
      <td>2025-03-01</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A3</td>
      <td>East</td>
      <td>2025-03-02</td>
      <td>2025-03-05</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>East</td>
      <td>2025-03-02</td>
      <td>2025-03-05</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A5</td>
      <td>None</td>
      <td>2025-03-04</td>
      <td>2025-03-06</td>
      <td>-4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A6</td>
      <td>South</td>
      <td>2025-03-05</td>
      <td>2025-03-07</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("Completeness: missing values per column")
print(extract.isna().sum(), end="\n\n")

print("Validity: rows with quantity not above zero")
print(extract[extract["quantity"] <= 0], end="\n\n")

print("Consistency (labels): region spellings ->", sorted(extract["region"].dropna().unique()))
print("Consistency (dates): rows shipped before they were ordered")
print(extract[extract["ship_date"] < extract["order_date"]], end="\n\n")

print("Uniqueness: is order_id unique?", extract["order_id"].is_unique,
      "| fully duplicated rows:", extract.duplicated().sum(), end="\n\n")

reporting_date = pd.Timestamp("2025-03-31")
print("Timeliness: last order", extract["order_date"].max().date(),
      "| days before the reporting date:", (reporting_date - extract["order_date"].max()).days)
```

    Completeness: missing values per column
    order_id      0
    region        1
    order_date    0
    ship_date     0
    quantity      0
    dtype: int64
    
    Validity: rows with quantity not above zero
      order_id region order_date  ship_date  quantity
    4       A5   None 2025-03-04 2025-03-06        -4
    
    Consistency (labels): region spellings -> ['East', 'South', 'West', 'west']
    Consistency (dates): rows shipped before they were ordered
      order_id region order_date  ship_date  quantity
    1       A2   west 2025-03-02 2025-03-01         1
    
    Uniqueness: is order_id unique? False | fully duplicated rows: 1
    
    Timeliness: last order 2025-03-05 | days before the reporting date: 26


Finding a problem does not mean deleting it. For each one, decide and **record** whether to fix, flag, exclude or keep, and why. Session 3 is about those decisions.

> **Check your understanding 5**
>
> For each planted problem above, name the dimension and say what you would do. Which one could be a genuine business event rather than an error?

---

## Part 6: Worked case — the Superstore order lines

Now apply every idea to the course data. The question from the business: *"How many orders did we have, and can I trust the number?"*

### Step 1: Load and profile


```python
df = load_orders()
print("Rows, columns:", df.shape)
profile_columns(df)
```

    Rows, columns: (6815, 22)





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
      <th>dtype</th>
      <th>missing</th>
      <th>distinct</th>
      <th>example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>row_id</th>
      <td>int64</td>
      <td>0</td>
      <td>6815</td>
      <td>1</td>
    </tr>
    <tr>
      <th>order_id</th>
      <td>object</td>
      <td>0</td>
      <td>3388</td>
      <td>US-2023-103800</td>
    </tr>
    <tr>
      <th>order_date</th>
      <td>datetime64[ns]</td>
      <td>0</td>
      <td>918</td>
      <td>2023-01-03 00:00:00</td>
    </tr>
    <tr>
      <th>ship_date</th>
      <td>datetime64[ns]</td>
      <td>0</td>
      <td>989</td>
      <td>2023-01-07 00:00:00</td>
    </tr>
    <tr>
      <th>ship_mode</th>
      <td>object</td>
      <td>0</td>
      <td>4</td>
      <td>Standard Class</td>
    </tr>
    <tr>
      <th>customer_id</th>
      <td>object</td>
      <td>0</td>
      <td>793</td>
      <td>DP-13000</td>
    </tr>
    <tr>
      <th>segment</th>
      <td>object</td>
      <td>0</td>
      <td>3</td>
      <td>Consumer</td>
    </tr>
    <tr>
      <th>country_region</th>
      <td>object</td>
      <td>0</td>
      <td>2</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>region</th>
      <td>object</td>
      <td>0</td>
      <td>4</td>
      <td>Central</td>
    </tr>
    <tr>
      <th>category</th>
      <td>object</td>
      <td>0</td>
      <td>3</td>
      <td>Office Supplies</td>
    </tr>
    <tr>
      <th>sub_category</th>
      <td>object</td>
      <td>0</td>
      <td>17</td>
      <td>Paper</td>
    </tr>
    <tr>
      <th>product_id</th>
      <td>object</td>
      <td>0</td>
      <td>1803</td>
      <td>OFF-PA-10000174</td>
    </tr>
    <tr>
      <th>product_name</th>
      <td>object</td>
      <td>0</td>
      <td>1794</td>
      <td>Message Book, Wirebound, Four 5 1/2" X 4" Form...</td>
    </tr>
    <tr>
      <th>sales</th>
      <td>float64</td>
      <td>0</td>
      <td>4640</td>
      <td>16.45</td>
    </tr>
    <tr>
      <th>quantity</th>
      <td>int64</td>
      <td>0</td>
      <td>14</td>
      <td>2</td>
    </tr>
    <tr>
      <th>discount</th>
      <td>float64</td>
      <td>0</td>
      <td>12</td>
      <td>0.20</td>
    </tr>
    <tr>
      <th>profit</th>
      <td>float64</td>
      <td>0</td>
      <td>5471</td>
      <td>5.55</td>
    </tr>
    <tr>
      <th>returned_order_flag</th>
      <td>int64</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>customer_analysis_eligible</th>
      <td>int64</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>customer_order_conflict</th>
      <td>int64</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>order_to_ship_days</th>
      <td>int64</td>
      <td>0</td>
      <td>9</td>
      <td>4</td>
    </tr>
    <tr>
      <th>order_month</th>
      <td>datetime64[ns]</td>
      <td>0</td>
      <td>36</td>
      <td>2023-01-01 00:00:00</td>
    </tr>
  </tbody>
</table>
</div>



### Step 2: Predict, then reveal — what is the grain?

Is the primary key `order_id` or `row_id`? Predict, then check both.


```python
print("row_id unique?  ", df["row_id"].is_unique)
print("order_id unique?", df["order_id"].is_unique)
print()
print("Rows (order lines):", len(df))
print("Different orders:  ", df["order_id"].nunique())
```

    row_id unique?   True
    order_id unique? False
    
    Rows (order lines): 6815
    Different orders:   3388


`row_id` is unique and `order_id` repeats: **one row is one product line within an order**, identified by `row_id`. `order_id` behaves like a foreign key to an (invisible) orders table.

So the answer to "how many orders?" is `nunique()` on `order_id`, never `len(df)`.

### Step 3: Which attributes belong to the order, and which to the line?

If a column is an attribute of the **order**, it should take exactly one value within each order. The next cell counts, for each column, the largest number of different values found inside one order.


```python
columns_to_test = ["order_date", "ship_mode", "segment", "region", "category", "product_id", "sales"]
values_per_order = df.groupby("order_id")[columns_to_test].nunique().max()
values_per_order.rename("max distinct values within one order")
```




    order_date     1
    ship_mode      1
    segment        1
    region         1
    category       3
    product_id    11
    sales         11
    Name: max distinct values within one order, dtype: int64



Where the maximum is 1, the column is recorded **at order grain** (repeated on every line). Where it is above 1, it is recorded **at line grain**.

This matters for counting. Distinct orders add up across groups of an order-grain column, but not across groups of a line-grain column:


```python
for column in ["segment", "category"]:
    orders_per_group = df.groupby(column)["order_id"].nunique()
    print(f"{column:9s}: group order counts add up to {orders_per_group.sum()}"
          f" | overall distinct orders {df['order_id'].nunique()}")
```

    segment  : group order counts add up to 3388 | overall distinct orders 3388
    category : group order counts add up to 4779 | overall distinct orders 3388


### Step 4: Five quality dimensions in one cell


```python
print("Completeness | missing values:", df.isna().sum().sum())
print("Validity     | quantity always above zero:", (df["quantity"] > 0).all(),
      "| sales never negative:", (df["sales"] >= 0).all())
print("Consistency  | ship date never before order date:", (df["ship_date"] >= df["order_date"]).all())
print("Uniqueness   | row_id unique:", df["row_id"].is_unique,
      "| fully duplicated rows:", df.duplicated().sum())
print("Timeliness   | order dates from", df["order_date"].min().date(), "to", df["order_date"].max().date(),
      "| months present:", df["order_month"].nunique())
```

    Completeness | missing values: 0
    Validity     | quantity always above zero: True | sales never negative: True
    Consistency  | ship date never before order date: True
    Uniqueness   | row_id unique: True | fully duplicated rows: 0
    Timeliness   | order dates from 2023-01-03 to 2025-12-31 | months present: 36


Read the output line by line. Each line is one entry for a quality checklist, with its evidence.

> **One known consistency issue**
>
> A few orders in the raw file carry more than one customer ID. The setup cell flags them in `customer_order_conflict`. They stay in all order and Sales counts; they are excluded only when analysing individual customers. You will explore this in the lab.

---

## Summary

| Idea | One-line takeaway |
|---|---|
| Levels of measurement | Nominal → ordinal → interval → ratio; only ratio data supports "twice as much" |
| Tidy data | One variable per column, one observation per row, one value per cell |
| Grain | Say what one row is before you count anything |
| Keys | Primary key unique and complete; foreign keys point to another table; `validate=` guards joins |
| Data dictionary | Meaning, type, level, unit, rules, additivity and source for each column |
| Quality dimensions | Completeness, validity, consistency, uniqueness, timeliness, each with a check and a decision |

---

## Quiz

Answer these at the start of the next lecture. Write short answers.

1. Give one example each of a nominal, ordinal, interval and ratio variable from a business you know.
2. Why is "the average satisfaction score rose from 3.9 to 4.1" weaker evidence than "the share of customers scoring 4 or 5 rose from 62% to 70%"?
3. A table lists one row per store with columns `sales_2024` and `sales_2025`. Is it tidy? What would the tidy version look like?
4. In the Superstore table, why does `len(df)` not answer "how many orders?"
5. What is the difference between a primary key and a foreign key?
6. A delivery fee recorded once per order is joined onto order lines and summed. What goes wrong, and how do you avoid it?
7. Name the quality dimension each check belongs to: (a) no ship date before its order date, (b) `row_id` has no duplicates, (c) no blank `region`, (d) last order date is close to today.
8. Why are distinct order counts by **category** not additive, while those by **segment** are?

---

## Lab briefing

In the [Session 2 lab](02_data_and_grain_lab.md) you will turn a vague request into a question, take the Superstore table apart, write its grain statement and data dictionary, run a five-dimension quality checklist, hand-check one order and fix a colleague's counting mistakes.

**Evidence to keep:** your question, grain statement, data dictionary, quality checklist, preparation log and one hand-checked order.
