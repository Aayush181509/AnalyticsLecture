# Lesson template

<p class="lead">
The structure every lesson in this course will follow. Each section below shows what that part of a lesson will contain.
</p>

!!! note "Template only"

    This page is not a ready-to-teach lesson, a dataset download or a set of verified answers. Text in [square brackets] is replaced when a lesson and its resources are ready.

---

## 1. The business decision

[Name the stakeholder, the decision they face, the business constraints and the evidence they need. Label fictional organisations and synthetic data clearly.]

---

## 2. What you will demonstrate

By the end, you will be able to:

- [Explain what a row means and which records are in scope.]
- [Prepare the data and calculate the specified measures in Tableau.]
- [Check a result and explain a common error.]
- [Present a recommendation supported by evidence and one limitation.]

**Evidence to submit:** [the workbook or export, validation notes and a short business recommendation. State the minimum required and mark optional extensions.]

---

## 3. Before you start

[Required prior skills, the tested Tableau setup, the approved dataset release and what to do if access fails. Python is optional.]

!!! warning "Data safety"

    Only use data approved for this lesson in Tableau Public. Published workbooks and their data are public, and hiding a profile item does not make it private. Never upload workplace or personal data.

    [State whether publishing is required and give the tested submission route.]

---

## 4. Understand the data

[Link to the learner dataset and dictionary only when available. Give the release/version, where it came from, usage rights and any preparation already done.]

| Item | What to fill in |
| --- | --- |
| Row meaning and key | [One row represents…; the unique key is…] |
| Population and dates | [Included records, exclusions, inclusive dates and reporting cutoff] |
| Units and dimensions | [Currency or units; order-level versus line-level fields] |
| Missing or incomplete records | [Excluded, kept as unknown or flagged. Never quietly treat a missing amount as zero.] |
| Relationships | [Join keys, how many rows match, and duplication checks, when relevant] |

---

## 5. Agree the measures

| Measure | Numerator | Denominator | Filters and dates | Missing or zero values | Units |
| --- | --- | --- | --- | --- | --- |
| [Measure] | [What is added up] | [Eligible population, or not applicable] | [Scope] | [Explicit rule] | [Currency, %, days…] |

[Explain why these definitions answer the question. Say whether amounts include refunds, taxes or other costs. Point out where an overall weighted rate differs from an average of rates, and where distinct counts do not add up.]

---

## 6. Watch a worked example

[A checked demonstration on the released dataset, following question → understanding → preparation → analysis → validation → visualization → recommendation. Explain the reasoning at each step and pause for a prediction. Mark illustrative examples as illustrative.]

!!! hint "Checkpoint"

    [What should you look at to confirm the scope and method, rather than trusting how the chart looks?]

---

## 7. Try it with guidance

[A bounded Tableau task with prompts, the expected result and a checkpoint. Include a recovery step and an accessible table alternative for key visuals.]

---

## 8. Work independently

[A related business question with less support. Give the minimum expected and the evidence to submit.]

!!! tip "Check your result"

    [List the grain, duplication, scope, arithmetic, denominator and reconciliation checks for this dataset. Record your actual results.]

---

## 9. Debug a result

[Present one deliberate mistake without its correction. Ask what business meaning changed, how to diagnose it, how to fix it and how to confirm the fix.]

!!! tip "If you get stuck"

    [A hint or checkpoint that supports your reasoning without giving away the assessed answer.]

---

## 10. Make a recommendation

[A short stakeholder briefing with a decision, numerical evidence, scope, one limitation and a next check. Separate what the data shows from any claim about cause.]

---

## 11. Optional Python connection

[How the same analysis looks in pandas, using the same dataset and metric definitions. Provided only after it is tested. Not needed for the essential Tableau submission.]

---

## 12. Submit and reflect

[The tested submission route, file names and assessment criteria. Include a catch-up route for anyone whose access failed.]

!!! note "Exit ticket"

    [One concept check, one validation observation and one remaining uncertainty.]

[A short recap and further practice when ready. Instructor answers and internal planning are kept separately and are not linked from lessons.]
