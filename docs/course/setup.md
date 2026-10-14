# Setup and practice

<p class="lead">
What you need before you start, how to run the lessons in Google Colab, how to stay safe with data, and how to keep a simple evidence log.
</p>

---

## What you need

- A computer with a modern web browser (Chrome, Edge, Firefox or Safari)
- A Google account, to use Google Colab
- A way to receive course files and submit your work

!!! note "Before teaching starts"

    We will confirm devices, accessibility needs and the submission channel with everyone. Nothing needs to be installed for the Python lessons.

---

## Open a lesson in Google Colab

Every Python lesson page has an **Open in Colab** button near the top.

1. Click **Open in Colab**. The lesson notebook opens in Google Colab; sign in with your Google account if asked.
2. Run the cells from top to bottom: click a cell and press **Shift + Enter**.
3. Save your own copy with **File → Save a copy in Drive**, so your changes are kept.

The notebook opens with the facilitator's outputs already visible. Running it yourself replaces them with your own results.

The first code cell in each lesson downloads the course data from Tableau's sample-data page and checks that it is exactly the version the lesson was written for. If it prints a warning, tell your facilitator.

!!! tip "If something goes wrong"

    Choose **Runtime → Restart session and run all**. This runs everything again from the top and fixes most problems.

New to Python? Start with [Lesson 0: Python and Colab basics](../lectures/00_python_and_colab_basics.md).

---

## Keep your data safe

!!! warning "Only use course data"

    Use only the datasets supplied for this course. Never upload private employer, customer or employee files to Colab or any other online tool.

Notebooks you save in Google Drive are private to you unless you choose to share them. Check the sharing setting before sending a link to anyone.

---

## If something does not work

!!! tip "No internet or no Google account"

    Follow the demonstration or pair with a classmate, and keep writing your metric and checking notes. Run the notebook yourself later, once access is back.

---

## Tableau (later)

A separate Tableau section will come later in the course. You do not need Tableau for the Python lessons. When we reach that section, you will install **Tableau Desktop Public Edition** from the [official Tableau Public page](https://www.tableau.com/products/public).

!!! warning "Anything you publish to Tableau Public is public"

    Published workbooks and their data can be seen by anyone. Hiding an item on your profile does not make it private. Tableau Public also lets you save workbooks on your own computer, so publishing online is optional.

---

## Keep an evidence log

For every task, write down a few short notes. They make your portfolio much easier to build.

| Record | Example prompt |
|---|---|
| Data release | Which file and version did I use? |
| Question | What decision is this for? |
| Grain | What does one row represent? |
| Date window and filters | Which records are included? |
| Metric definition | What is the numerator and denominator? |
| Checks | How did I confirm the number is right? |
| Chart and recommendation | What should the stakeholder do next? |

Save your notebook and your notes together.

!!! tip "When two numbers disagree"

    Compare their populations and denominators **before** changing the chart.
