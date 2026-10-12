# From business question to recommendation

A useful analysis supports a decision. A chart becomes trustworthy when its population, calculations and limitations are clear.

| Stage | Ask | Keep as evidence |
|---|---|---|
| Business question | Who must decide what, and by when? | Decision and question statement. |
| Data understanding | What does each row represent? What is absent? | Grain, keys, units, dictionary and scope. |
| Preparation | What changes are needed, and can we reproduce them? | Original copy and transformation log. |
| Analysis | Which comparison or metric answers the question? | Definition, filters and calculation. |
| Validation | Can we reconcile totals and explain anomalies? | Manual spot check, count/totals checks and edge cases. |
| Visualization | Can the audience see the meaningful comparison? | Labeled chart with period, units and population. |
| Recommendation | What action follows, and what is uncertain? | Evidence-linked action, caveat and follow-up measure. |

## Worked reasoning example

A stakeholder asks, “Why are orders falling?” A file contains order lines, with some orders occupying multiple rows. Counting rows measures lines, not orders. First define an order, the period and eligible statuses. Then count distinct order IDs in that population. Compare that count with an order-level summary before interpreting a trend.

The same discipline applies to budgets repeated after a join, undelivered shipments missing from a service denominator, campaign percentages averaged without their volumes, and historical turnover divided by today's headcount.

## When a result looks wrong

Check grain and keys first, then date filters, missing values, join/relationship behavior and aggregation. Write down why the incorrect answer was tempting and what evidence supports the corrected answer. A plausible number is not a validation check.

An association can suggest what to investigate. It does not establish that a discount, campaign, carrier or HR policy caused a result. Recommend a follow-up comparison or test when a causal decision needs stronger evidence.
