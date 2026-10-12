# From business question to recommendation

<p class="lead">
A useful analysis supports a decision. A chart becomes trustworthy when its population, calculations and limitations are clear.
</p>

We follow the same seven steps in every lesson and case.

---

## The seven steps

### 1. Business question

**Ask:** Who must decide what, and by when?

**Keep:** the decision and a one-sentence question.

### 2. Data understanding

**Ask:** What does each row represent? What is missing?

**Keep:** the grain, keys, units, data dictionary and scope.

### 3. Preparation

**Ask:** What changes are needed, and could someone else repeat them?

**Keep:** an untouched copy of the original data and a log of every change.

### 4. Analysis

**Ask:** Which comparison or metric actually answers the question?

**Keep:** the metric definition, filters and calculation.

### 5. Validation

**Ask:** Do totals reconcile? Can I explain any odd values?

**Keep:** a manual spot check, count and total checks, and edge cases.

### 6. Visualization

**Ask:** Can the audience see the important comparison at a glance?

**Keep:** a labelled chart showing the period, units and population.

### 7. Recommendation

**Ask:** What action follows, and what is still uncertain?

**Keep:** an action linked to evidence, one caveat and a follow-up measure.

---

## A worked example

!!! note "Why are orders falling?"

    A manager asks: *"Why are orders falling?"*

    The data file has one row per **order line**, so a single order with three products takes up three rows.

    1. Counting rows would count **lines**, not orders.
    2. First, define what an order is, which period to look at and which orders are eligible.
    3. Then count **distinct order IDs** in that population.
    4. Compare the result with an order-level summary before reading anything into the trend.

The same care applies elsewhere in the course:

- a budget repeated on every row after a join
- undelivered shipments left out of a service calculation
- campaign percentages averaged without their volumes
- past staff exits divided by **today's** headcount

---

## When a result looks wrong

Work through these checks in order:

1. Grain and keys
2. Date filters
3. Missing values
4. Join or relationship behaviour
5. Aggregation

Then write down **why** the wrong answer was tempting and **what evidence** supports the corrected one.

!!! warning "A plausible number is not a checked number"

    Looking reasonable is not the same as being validated.

---

## Association is not causation

A pattern in the data can tell you **where to look**. It does not prove that a discount, campaign, carrier or HR policy **caused** a result.

When a decision depends on cause and effect, recommend a follow-up comparison or a test.
