# Tableau Lesson 3: Which segment deserves a closer look?

<p class="lead">
Compare the three customer segments using five measures, calculate each one correctly, check that the numbers add up, and make a careful recommendation.
</p>

!!! warning "Draft lesson: Tableau section (coming later)"

    The course currently teaches this lesson in Python: see [Python Lesson 3](../lectures/03_segment_comparison.md). This Tableau version will be completed in the later Tableau section.

    The Tableau steps on this page have not yet been rehearsed on the course version of Tableau. Menu names may differ slightly on your computer.

---

## The business decision

The retail head has one analyst free next month and asks:

> *"Which customer segment should we investigate first, and what should we check before we change any promotions?"*

A big Sales total alone is not enough to decide. A segment can sell a lot and still earn little profit, or have many small orders. Today you build a fair comparison.

---

## What you will be able to do

By the end of this lesson you will be able to:

1. Define five measures precisely: Sales, Orders, Average order value, Profit and Profit ratio.
2. Build them in Tableau as calculated fields.
3. Calculate ratios **from totals**, not by averaging other ratios.
4. Check that segment results reconcile with the overall total.
5. Explain how a filter changes every measure.
6. Write a short, evidence-based recommendation with one limitation.

**Evidence you keep:** a segment KPI table, your metric definitions, a validation checklist and a five-sentence recommendation.

---

## Before you start

- Open your workbook from [Lesson 2](class-02.md), with the **Orders** calculated field.
- Have your grain statement and evidence log ready.
- Re-read the [averages and percentages traps](../foundations/misleading-statistics.md) in Foundations.

---

## Part 1: Agree the measures

Every measure uses the **same rows**: all order lines in the file, unless you deliberately apply a filter.

| Measure | What it means | How to calculate it |
|---|---|---|
| **Sales** | Total reported Sales | Add up `sales` |
| **Orders** | Number of different orders | Count distinct `order_id` |
| **Average order value (AOV)** | Typical Sales per order | Sales ÷ Orders |
| **Profit** | Total reported Profit (can be negative) | Add up `profit` |
| **Profit ratio** | Profit earned per unit of Sales | Profit ÷ Sales |

!!! note "About the money"

    Sales and Profit are in the file's own monetary units. The currency is not stated, so do not add a currency symbol. The source does not explain exactly how Profit is calculated, so call it **profit ratio**, not "gross margin".

!!! warning "Totals first, then divide"

    AOV and Profit ratio must be calculated from the **totals** for whatever you are looking at. Never average the ratios of individual rows or of segments. You will see why in Part 6.

---

## Part 2: Watch the demonstration

Your facilitator builds the five measures for the whole file and shows them as a small table.

Before each number appears, **predict**:

- Will AOV be larger or smaller than Sales divided by the number of **rows**? Why?
- Can Profit ratio be negative? When?

---

## Part 3: Guided practice — build the calculations

Create each calculated field (**Analysis → Create Calculated Field**). Type the name and formula exactly.

**Sales**

```
SUM([Sales])
```

**Orders** (from Lesson 2)

```
COUNTD([Order Id])
```

**AOV**

```
IF COUNTD([Order Id]) > 0 THEN SUM([Sales]) / COUNTD([Order Id]) END
```

**Profit**

```
SUM([Profit])
```

**Profit ratio**

```
IF SUM([Sales]) <> 0 THEN SUM([Profit]) / SUM([Sales]) END
```

!!! tip "Why the IF?"

    If a filter leaves no orders or no Sales, dividing would be undefined. The `IF` makes Tableau show a blank instead of an error or a misleading zero. A blank here means *"not available"*, never 0%.

Format the results:

- **Sales, Profit and AOV:** number with two decimal places, no currency symbol.
- **Profit ratio:** percentage with one decimal place.

---

## Part 4: Guided practice — the segment table

1. Start a new sheet.
2. Drag **Segment** to **Rows**.
3. Drag **Measure Names** to **Columns** and **Measure Values** to the table area. Keep only your five measures.
4. Turn on totals: **Analysis → Totals → Show Column Grand Totals**.
5. Give the sheet a clear title, for example *"Segment comparison, orders placed 2023–2025 (source monetary units)"*.

### Check that it reconciles

Tick each check in your evidence log:

- [ ] The three segment **Sales** add up to the grand total.
- [ ] The three segment **Profit** values add up to the grand total.
- [ ] The three segment **Orders** add up to the grand total. (They should, because every order belongs to exactly one segment.)
- [ ] The grand total **AOV** equals total Sales ÷ total Orders. It is **not** the average of the three segment AOVs.
- [ ] The grand total **Profit ratio** equals total Profit ÷ total Sales. It is **not** the average of the three segment ratios.

!!! hint "If a total looks wrong"

    Check that every measure uses the same filters, and that the grand total is recalculated, not summed. Right-click the measure and check which aggregation the total uses.

---

## Part 5: Independent work

### A. Filter by region

1. Duplicate your segment sheet.
2. Add **Region** to **Filters** and choose one region.
3. Record all five measures for each segment in that region.
4. Write two sentences: does the ranking of segments change inside this region?

### B. Look at a category

1. Duplicate the sheet again and filter to one **Category**.
2. Notice that AOV now means *"Sales of this category's lines per order that contains this category"*, not full basket value. Rename the column to say so.
3. Remove the filter and put **Category** on Rows instead of Segment. Do the category **Orders** add up to the overall total? Explain why not, in one sentence.

---

## Part 6: Debugging challenge

A colleague sends you this summary:

> *"Our overall profit ratio is the average of the three segment ratios. And our average order value is total Sales divided by the number of rows."*

1. Calculate the colleague's two numbers from your own table.
2. Compare them with your correct grand totals.
3. Explain each mistake in one sentence.
4. Which segment has the most influence on the correct overall profit ratio, and why?

!!! hint "Think about weights"

    A segment with much more Sales should pull the overall ratio more strongly than a small segment. Does a simple average of the three ratios allow that?

---

## Part 7: Make a recommendation

Write **five sentences** to the retail head:

1. **Recommendation:** which segment to investigate first.
2. **Evidence 1:** one measure, with its value and how it compares.
3. **Evidence 2:** a second, different measure.
4. **Limitation:** one thing this data cannot tell you. For example, it shows which segment *looks* different; it does not show *why*, and it does not prove a discount or promotion caused anything.
5. **Next check:** one specific piece of evidence to request before changing promotions.

!!! warning "Association, not cause"

    If a segment with more discounts has a lower profit ratio, that is a pattern worth investigating. It is not proof that the discounts caused it. Other differences between segments, such as product mix, could explain it.

---

## Validation checklist

Before submitting, confirm:

- [ ] Every measure uses the same filters and date scope.
- [ ] Orders are counted distinctly, not as rows.
- [ ] AOV and Profit ratio are calculated from totals.
- [ ] Segment Sales, Profit and Orders reconcile with the grand totals.
- [ ] Money is labelled "source monetary units", with no currency symbol.
- [ ] The recommendation names a limitation and a next check.

---

## Exit ticket

1. Why is the average of three segment ratios not the overall ratio?
2. What does a blank AOV or Profit ratio mean?
3. One question you would want answered before acting on your recommendation.

---

## After the lesson

- Finish the region and category work from Part 5.
- Correct the colleague's summary in Part 6 and add it to your evidence log.
- Keep your workbook for [Lesson 4](class-04.md), where we look at monthly trends and the returns list, and build a dashboard.
