# Lesson template

**Template status:** this page shows the structure of future lessons. It is not a ready-to-teach lesson, a dataset download or a set of verified answers. Replace bracketed prompts when the lesson and its resources are ready.

## The business decision

[Name the stakeholder, the decision they face, the business constraints and the evidence they need. Label fictional organizations and synthetic data.]

## What you will demonstrate

By the end, you will be able to:

- [Explain the data's row meaning and population.]
- [Prepare and calculate the specified measures in Tableau.]
- [Validate a result and explain a common error.]
- [Present a recommendation supported by evidence and a limitation.]

Evidence: [Specify the workbook/export, validation notes and short business recommendation. State the assessed minimum and distinguish optional extensions.]

## Before class

[State required prior skills, estimated preparation time, tested Tableau setup, approved synthetic/public dataset release and an access-recovery route. Python starts optional.]

Only use data approved for this lesson in Tableau Public. Published workbooks and their data are public; hiding a profile does not make data private. Do not upload workplace or personal data. [State whether publishing is required and provide the tested submission route.]

## Understand the data

[Link to the learner-safe dataset and dictionary only when available. Identify release/version, provenance, rights and any prepared transformations.]

| Item | Definition to fill in |
| --- | --- |
| Row meaning and key | [One row represents…; unique key…] |
| Population and date scope | [Eligible records, exclusions, inclusive dates and reporting cutoff] |
| Units and dimensions | [Currency, units, order-level versus line-level attributes] |
| Missing and incomplete records | [What is excluded, retained as unknown or flagged; never silently treat missing amounts as zero] |
| Relationships | [Join/relationship keys, cardinality and duplication checks, when relevant] |

## Agree the measures

| Business measure | Numerator | Denominator | Filters and dates | Missing/zero behavior | Units |
| --- | --- | --- | --- | --- | --- |
| [Measure] | [Included amounts/events] | [Eligible population or not applicable] | [Scope] | [Explicit rule] | [Source currency, %, days, etc.] |

[Explain why these definitions answer the question. State whether amounts include refunds, taxes or other costs. Distinguish overall weighted rates from means of subgroup rates, and explain non-additive distinct counts where relevant.]

## Watch a worked example

[Provide a verified demonstration from the released dataset: question → understanding → preparation → analysis → validation → visualization → recommendation. Explain the reasoning behind each step and include a pause for a prediction. Mark illustrative examples as illustrative.]

Checkpoint: [What should learners inspect to confirm scope and method, without relying only on the appearance of the chart?]

## Try it with guidance

[State a bounded Tableau task, prompts, expected artifact and a validation checkpoint. Provide a recovery step and accessible table alternative for essential visuals.]

## Work independently

[Give a related business question with less scaffolding. Specify the common minimum, estimated time and evidence to submit.]

Validate your result: [List grain, duplication, scope, arithmetic, denominator and reconciliation checks appropriate to this dataset. Ask learners to record actual results.]

## Debug a result

[Present one intentional mistake without its correction. Ask what business meaning changed, how to diagnose it, how to fix it and how to verify the correction.]

If you get stuck: [Provide a hint or checkpoint route that supports reasoning without giving away the assessed answer.]

## Make a recommendation

[Ask for a short stakeholder briefing with a decision, quantitative evidence, scope, limitation and a next check. Require learners to distinguish observed association from a causal claim.]

## Optional Python connection

[Map the analysis to pandas concepts, using the same dataset and metric contract. Provide a tested companion only after release. This extension is not needed for the essential Tableau submission.]

## Submit and reflect

[List the tested submission route, artifact names, expected practice time and assessment criteria. Include a catch-up route for learners whose access failed.]

Exit ticket: [One concept check, one validation observation and one remaining uncertainty.]

[Offer a learner-safe recap and further practice when ready. Instructor answers and internal planning are maintained separately and are not linked from learner lessons.]
