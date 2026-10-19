# Tableau sessions

<p class="lead">
Four sessions that rebuild the analysis you did in Python, this time in Tableau. You use the same Superstore file, the same date window and the same checks, so you can compare your Tableau numbers with your Python numbers.
</p>

---

## What the four sessions cover

Each session has a **lecture** and a **lab**, like the Python sessions.

| Session | Lecture | Lab | Python link |
|---|---|---|---|
| **T1: Tableau fundamentals** | How Tableau reads a table: dimensions and measures, discrete and continuous fields, aggregation, the Marks card, level of detail and filters | Count rows and orders, flag returned orders, and draw distributions of order value and ship days | Sessions 2 and 4 |
| **T2: Calculations and KPIs** | Calculated fields, ratios done correctly, distinct counts, running totals and growth, a first level-of-detail expression | Rebuild the segment KPI table with a reconciliation check, and the monthly trend and growth | Sessions 5 and 7 |
| **T3: Dashboards** | Layout and reading order, filters and actions, colour and accessibility, message titles | Rebuild the decision dashboard in Tableau | Session 14 |
| **T4: Publishing and portfolio** | What Tableau Public makes public, what is safe to publish, keeping versions, telling a story | Build a portfolio piece from your capstone analysis | Sessions 15 and 16 |

---

## Before the first session

### 1. Install Tableau Desktop Public Edition

1. Go to the [official Tableau Public page](https://www.tableau.com/products/public).
2. Download **Tableau Desktop Public Edition**. It is free. You need to create a free Tableau Public account to download it.
3. Install it and open it once to check that it starts.

!!! tip "If you cannot install software on your laptop"

    Tell your facilitator before the first session. Tableau Public also has a **web editor** that runs in the browser. Its menus differ slightly from the desktop app, but you can follow every lab with it.

### 2. Download the course data

1. Download the Superstore file from Tableau's sample-data page: [sample_-_superstore.xls](https://public.tableau.com/app/sample-data/sample_-_superstore.xls).
2. Save it in a folder you can find again, for example `Documents/DataAnalytics/data`.
3. Do not open and re-save it in Excel. Keep the original file untouched.

This is the **same file** the Python sessions download in their setup cell.

!!! warning "Use the downloaded file, not the built-in sample"

    Tableau Desktop Public Edition comes with a built-in data source called **Sample - Superstore**. It may be a different version of the data, with different dates and rows. Always connect to the file you downloaded, so your numbers match the course.

---

## The course scope rule

All four sessions use the same rule as the Python sessions:

- **Period:** orders placed from **1 January 2023 to 31 December 2025**, by Order Date. Orders placed in 2026 are left out.
- **Grain:** one row is one **order line**: one product within an order.
- **Returns:** an order counts as returned when its Order ID appears on the file's **Returns** sheet.
- **Money:** Sales and Profit are in the **file's own monetary units**. The file does not state a currency, so we never call them dollars or any other currency.

You set up this scope once, in the T1 lab section [Set up the Superstore data source](T1_fundamentals_lab.md#set-up-the-superstore-data-source). Later labs start from the same setup.

---

## Save your work

Save every workbook **on your own computer** as a **packaged workbook** (`.twbx`). A packaged workbook keeps your charts and a copy of the data together in one file.

1. Choose **File → Save As**.
2. Pick your course folder and, under file type, choose **Tableau Packaged Workbook (*.twbx)**.
3. Name it clearly, for example `T1_lab_YourName.twbx`.

!!! warning "Publishing to Tableau Public is optional"

    Anything you publish to Tableau Public can be seen by anyone, including the data inside it. Hiding a workbook on your profile does not make it private. You do not need to publish anything in T1 to T3. T4 covers publishing safely.

---

## Submit your work on Moodle

Each Tableau lab has a Moodle assignment. For each lab, upload:

1. your saved **`.twbx`** file, and
2. a **PDF or image export** of your main sheet or dashboard (**File → Print to PDF**, or **Worksheet → Export → Image**),

plus any written answers the lab asks for.

!!! tip "Name your files clearly"

    Use `T1_lab_YourName.twbx` and `T1_lab_YourName.pdf`, for example `T1_lab_AnitaShrestha.twbx`.

---

## Start here

Begin with the [T1 lecture: Tableau fundamentals](T1_fundamentals_lecture.md), then the [T1 lab](T1_fundamentals_lab.md).
