# Business case previews

<p class="lead">
Five business problems, one for each department. Each case teaches a core skill and a common mistake to catch.
</p>

!!! note "Previews, not assignments yet"

    These are proposed case themes. Individual files have not been released yet.

    We combine selected [Tableau sample datasets](https://public.tableau.com/app/learn/sample-data) with synthetic (made-up) teaching data. **Meridian Commerce** is a proposed fictional company used only for the synthetic cases. Real datasets keep their own context, units and dates.

---

## The five core cases

### Retail

**Decision:** Which customer segment deserves a closer investigation?

**You will practise:** what a row means, distinct orders, average order value, Sales and Profit, ratios, discounts, customers, trends and the limits of a returns list.

**Mistake to catch:** treating order lines as orders.

### Finance

**Decision:** Which departments need a spending review?

**You will practise:** budget versus actual, time periods, reconciliation and whether a cost difference is favourable.

**Mistake to catch:** repeating a monthly budget on every transaction row.

### Operations

**Decision:** Where should delivery reliability improve?

**You will practise:** promised dates, overdue open shipments, distributions, median and mean.

**Mistake to catch:** dropping undelivered shipments from the service measure.

### Marketing

**Decision:** Which campaigns need closer evaluation before budget moves?

**You will practise:** weighted funnel rates, cost per conversion, return on ad spend and the limits of attribution.

**Mistake to catch:** averaging percentages that have different denominators.

### HR

**Decision:** How is the workforce changing, and which comparisons are fair?

**You will practise:** historical headcount, turnover, cohorts, tenure and recruitment timelines. All employee records are synthetic.

**Mistake to catch:** dividing past exits by the current headcount.

---

## What every case includes

- **Stakeholder brief**: the decision and why it matters
- **Data dictionary**: what each field means
- **Metric definitions**: exact formulas and scope
- **Worked example**: a guided walk-through
- **Exercises**: guided and independent practice
- **Debugging task**: find and fix a mistake
- **Recommendation challenge**: advise the stakeholder
- **Validation checkpoints**: confirm your numbers


Each case also has an optional pandas connection. Instructor answers are supplied separately.

---

## Combining evidence across departments

Before combining findings, explain any differences in grain, period and units.

- Within the synthetic company, marketing-attributed revenue is a view of the **same** retail revenue. Do not count it twice.
- Separate catalog datasets do **not** describe that fictional company.
- A good recommendation weighs trade-offs. It does not add incompatible KPIs together.

---

## Additional practice choices

You will also be able to practise on topics beyond the five departments:

| Topic | Example dataset |
|---|---|
| Sports | World Cup match results |
| Technology | Mobile operating-system usage (a data-quality exercise), start-up funding |
| Government | US construction spending, US home sales |
| Other | Science, education and entertainment datasets |

These are transfer exercises: the same process, with source-specific definitions and checks. They fit into your existing practice time or optional extensions. The five core cases remain the foundation of your portfolio.

!!! note "Every dataset is reviewed first"

    A dataset appearing in a catalog does not tell us what each row means, which calculations it supports or whether it can be shared. Each lesson will give you the exact reviewed file and dictionary, or instructions to download it from the source, before you use it.
