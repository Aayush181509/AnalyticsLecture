# Tableau Lesson 4: Trends, returns and a decision dashboard

<p class="lead">
Add time to your segment comparison, read growth figures without being fooled by seasons, use the returns list carefully, and bring it all together in one dashboard with a recommendation.
</p>

!!! warning "Draft lesson: Tableau section (coming later)"

    The course currently teaches this lesson in Python: see [Session 7 lab](../lectures/07_trends_and_growth_lab.md). This Tableau version will be completed in the later Tableau section.

    The Tableau steps on this page have not yet been rehearsed on the course version of Tableau. Menu names may differ slightly on your computer.

---

## The business decision

The commercial lead asks:

> *"Before we test any change, show me how sales have moved over time, whether returns differ between segments, and which one test you would run first."*

A single snapshot cannot answer this. A month can look like a crash or a boom simply because of the time of year.

---

## What you will be able to do

By the end of this lesson you will be able to:

1. Build a monthly Sales trend and recognise seasonal patterns.
2. Calculate month-on-month and year-on-year growth, and explain when each is fair.
3. Measure the share of orders on the returns list, and state what it cannot tell you.
4. Combine views into a dashboard with one shared filter.
5. Write a recommendation for a test, with an honest limitation.

**Evidence you keep:** a retail dashboard, your growth and returns definitions, and a short recommendation. This dashboard is your **retail portfolio checkpoint**.

---

## Before you start

- Open your workbook from [Lesson 3](class-03.md) with the segment KPI table.
- Re-read [cherry-picked time windows](../foundations/misleading-statistics.md) and [storytelling with data](../foundations/storytelling.md).

---

## Part 1: The monthly trend

1. Start a new sheet.
2. Drag **Order Month** to **Columns**. Right-click it and choose the **continuous Month** option (green pill), so every month from January 2023 to December 2025 appears in order.
3. Drag your **Sales** measure to **Rows**. You now have a line chart.
4. Add **Segment** to **Color** to see one line per segment. Then remove it again for the overall view.

!!! hint "What do you notice?"

    Write down three observations. Look at the same months in different years. Are some months always high? Are January and February always low?

!!! note "Use the month field"

    `order_month` is the first day of each order's month. Using it keeps every order in the right calendar month and makes year-on-year comparisons simple.

---

## Part 2: Two kinds of growth

### Month-on-month growth

Compares each month with the **previous** month.

```
IF LOOKUP(SUM([Sales]), -1) <> 0 THEN
    (SUM([Sales]) - LOOKUP(SUM([Sales]), -1)) / LOOKUP(SUM([Sales]), -1)
END
```

### Year-on-year growth

Compares each month with the **same month one year earlier**.

```
IF LOOKUP(SUM([Sales]), -12) <> 0 THEN
    (SUM([Sales]) - LOOKUP(SUM([Sales]), -12)) / LOOKUP(SUM([Sales]), -12)
END
```

To use them:

1. Create both as calculated fields and format them as percentages with one decimal place.
2. Put **Order Month** (continuous month) on Columns and one growth measure on Rows.
3. Right-click the growth measure, choose **Compute Using**, and select **Order Month**.

!!! warning "Blank is correct sometimes"

    January 2023 has no previous month in this file, so its month-on-month growth is blank. All of 2023 has no year-earlier month, so its year-on-year growth is blank. Blank means *"no comparison available"*, never 0%.

!!! warning "Filters can remove the comparison"

    `LOOKUP` compares with the previous month **shown in the view**. If you filter the view to only 2025, January 2025 can no longer see December 2024 and becomes blank. Keep all months in the view and highlight the period you care about instead of filtering it away.

### Which one is fair?

| Growth type | Good for | Can mislead when |
|---|---|---|
| Month-on-month | Spotting sudden changes | The business is seasonal: January after a busy December always looks like a crash |
| Year-on-year | Comparing like with like across seasons | A one-off event happened in the same month last year |

---

## Part 3: The returns list

From Lesson 2, you know the returns flag marks orders that appear on the source's **returns list**.

Create two measures:

**Orders on returns list**

```
COUNTD(IF [Returned Order Flag] = 1 THEN [Order Id] END)
```

**Share of orders on returns list**

```
IF COUNTD([Order Id]) > 0 THEN
    COUNTD(IF [Returned Order Flag] = 1 THEN [Order Id] END) / COUNTD([Order Id])
END
```

Add the share to your segment table.

!!! warning "What the returns list cannot tell you"

    - **When** an order was returned, or how many items.
    - **How much** money was refunded.
    - Whether an order **not** on the list was definitely kept.

    So call it *"share of orders on the returns list"*, not "return rate", and do not subtract anything from Sales because of it. A separate synthetic exercise will cover refund amounts later.

---

## Part 4: Guided practice — build the dashboard

1. Create a new dashboard (**Dashboard → New Dashboard**).
2. Drag in three sheets:
    - your **segment KPI table** from Lesson 3, with the returns share added
    - the **monthly Sales trend**
    - the **year-on-year growth** chart
3. Add a **Region** filter. Click its menu and choose **Apply to Worksheets → All Using This Data Source**, so every view responds together.
4. Give each sheet a **message title** that says what to notice, for example in the form *"[Segment] sales [rose / fell] most in [period]"*, filled in with what your chart actually shows.
5. Add one short **text box** stating the scope: *"Orders placed 2023–2025. Source monetary units. Fictitious sample data."*

### Design checks

Use what you learned in [Designing clear visuals](../foundations/visual-design.md):

- [ ] The most important view is at the top left.
- [ ] Colour is used only where it means something, and each segment keeps the same colour everywhere.
- [ ] Every chart has labelled axes with units.
- [ ] Nothing can be understood only by colour; labels or a table are available too.
- [ ] When you change the Region filter, all views change together and the totals still reconcile.

---

## Part 5: Independent work

1. Choose **one segment**. Using your dashboard, describe its trend over the three years in three sentences.
2. Compare the **same quarter** across years for that segment. Is it growing, flat or falling?
3. Add one **annotation** to the trend chart marking something a manager should notice (**right-click a point → Annotate → Mark**).

---

## Part 6: Debugging challenge

A colleague posts this in a team chat:

> *"Disaster! Sales fell about 75% in January 2025. And I filtered the dashboard to 2025 to check, but now January's growth is blank. Something is broken."*

1. Is January's fall a real problem, or a seasonal pattern? Which growth measure would you show instead, and what does it say?
2. Why did January's month-on-month growth become blank after filtering to 2025?
3. Rewrite the colleague's message so it is accurate.

---

## Part 7: Recommend a test

Write **five sentences** to the commercial lead:

1. **The test:** one specific change to try, in one segment.
2. **Evidence:** one measure from the trend or growth views.
3. **Evidence:** one measure from the segment table, including the returns share.
4. **Limitation:** for example, the trend shows *when* sales change, not *why*; the returns list has no refund amounts; the data is a fictitious sample.
5. **How to measure success:** the measure and comparison period you would use to judge the test, such as year-on-year Sales and profit ratio for the same months.

!!! tip "Why a test?"

    Past data shows patterns, not causes. A small, well-measured test, compared fairly with the same months last year or with an untouched group, is how you find out whether a change actually works.

---

## Validation checklist

- [ ] The trend shows all 36 months with no gaps.
- [ ] Growth measures compute along Order Month, and blanks appear only where no comparison exists.
- [ ] Returns are counted as distinct orders, not lines.
- [ ] The dashboard filter changes every view, and segment totals still reconcile with the overall total.
- [ ] Titles state messages; scope and units are written on the dashboard.

---

## Exit ticket

1. Why can month-on-month growth mislead for a seasonal business?
2. What is one thing the returns list cannot tell you?
3. What would you measure to judge whether your proposed test worked?

---

## After the lesson

- Finish your dashboard and recommendation. Together they form your **retail portfolio checkpoint**.
- Save the workbook locally with a clear name, and record the file name in your evidence log.
