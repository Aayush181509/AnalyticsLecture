# T4 lecture: Publishing and portfolio

<p class="lead">
Learn what happens to your work and your data when you publish to Tableau Public, decide what is safe to publish, keep your workbook versions in order, and turn one dashboard into a short story that a stranger can follow: question, evidence, limitation, action.
</p>

In [Session 15](../lectures/15_capstone_studio_lecture.md) you built your capstone: one decision, evidence from at least three domains, and a validation pack. In [Session 16](../lectures/16_executive_briefings_lecture.md) you learned to brief an executive: recommendation first, so-what titles, numbers with context and honest uncertainty. Today you learn how to show that work in Tableau, and how to share it **without** sharing anything you should not. In the T4 lab you build a portfolio piece from your capstone: one dashboard and a three-point story, saved on your own computer.

---

## What you will be able to explain

1. What **Tableau Public** makes public when you save or publish to it: the views, the **workbook** and the **data**.
2. Which data is **safe to publish**, and which data you must never publish.
3. What **hiding a viz** and **turning off downloads** do, and what they do **not** do.
4. How to keep **versions** of a `.twbx` file with dated file names and a change log.
5. How a Tableau **story** and its **story points** guide a reader through an argument.
6. How to write a portfolio piece in four parts: **question, evidence, limitation, action**.

---

## Part 1: What Tableau Public makes public

So far you have saved every workbook **on your own computer** as a `.twbx` file. Nobody else could see it unless you sent it to them. Tableau Public is different: it is a free website for sharing visualisations with **everyone**.

Tableau's own [Tableau Public FAQ](https://help.tableau.com/current/pro/desktop/en-us/public_faq.htm) says it plainly: workbooks and data published to your Tableau Public profile **are not private** and are **freely accessible to anyone**. The viz can be seen by anyone on the internet.

When you publish, Tableau sends three things, not one:

| What is published | What a stranger can do with it |
|---|---|
| The **views**: your dashboards, sheets and story | Open them in a browser, click, filter, read every label and tooltip, take screenshots |
| The **workbook** (`.twbx`) | Download it and open it in their own copy of Tableau, unless you turn downloads off |
| The **data** inside the workbook | Download it with the workbook, unless you turn downloads off. Publishing creates an **extract** of your data, which can hold every row and field of the data source, not only what your views show |

!!! warning "Saving in the web editor is publishing"

    If you work in the Tableau Public **web editor** in a browser, **saving** puts the workbook and its data on your Tableau Public profile. There is no "save privately" in the web editor. In Tableau Desktop Public Edition you can choose: **File → Save As** keeps the work on your computer; saving to Tableau Public publishes it.

### Turning off downloads

The FAQ says you can **turn off** the option to download the workbook and its data in the viz's settings on the Tableau Public website, and set the default for new vizzes in your **profile settings**.

Turning downloads off helps, but it does **not** make the data private:

- Every number shown in a view, a label or a tooltip can still be read, copied and screenshotted.
- Filters and actions let a viewer step through the data, one selection at a time.
- Anything already downloaded before you changed the setting stays downloaded.

### Hiding a viz

You can **hide** a viz on your profile. The FAQ is clear about what that means: visitors to your **profile page** cannot see the hidden viz, but **anyone who knows (or stumbles across) its URL can still see it**.

!!! warning "There is no private option on Tableau Public"

    Tableau's FAQ describes **no private or unlisted way** to publish. Hiding only removes the viz from your profile list; the viz and its data stay on the public website. Tableau's own advice is to use Tableau Public only for **data that is suitable for a public audience**. If data must stay private, keep the workbook on your own computer and never publish it.

*Sources checked on 19 October 2026: [Tableau Public FAQ](https://help.tableau.com/current/pro/desktop/en-us/public_faq.htm) and [Save workbooks to Tableau Public](https://help.tableau.com/current/pro/desktop/en-us/publish_workbooks_tableaupublic.htm). Tableau changes its website; read the FAQ again before you publish.*

---

## Part 2: What is safe to publish

Use one rule: **publish only data that you would be happy to print on a poster in the street, and that you have the right to share.**

| Data | Publish? | Why |
|---|---|---|
| Data from your **workplace**: sales, customers, suppliers, budgets, staff | **Never** | It belongs to your employer. Even totals can reveal business secrets, and you almost never have permission |
| **Customer** or **employee** data, even with names removed | **Never** | People can often be recognised from a few fields (department, age band, start date). Removing names is not enough |
| A dataset you found online with **no licence** or unclear terms | **No** | Being downloadable is not the same as being allowed to republish |
| **Superstore**, Tableau's sample file | **Not in this course** | Tableau invites learners to download it and practise, but the course has not found a clear permission to republish the file. Keep Superstore work on your own computer |
| The course's **synthetic** cases: marketing-v1, finance-v1, operations-v1, hr-v1 | **Only once the course confirms its reuse terms** | Generated by the course for fictional organisations; no real company or person. Ask your facilitator first. If they agree, label the data as synthetic and link to its source |
| **Openly licensed public** data whose licence allows sharing | **Yes, with care** | Follow the licence: name the source and keep any required notice |

!!! warning "Synthetic does not mean anything goes"

    A dashboard on synthetic data can still mislead. Say clearly on the page that the data is **synthetic** and describes a **fictional** organisation, give its units (currency units, never a real currency) and its period, and never present it as a real company's results.

### The privacy checklist

Before anyone in this course publishes, they complete this checklist. Every line must be **yes**.

1. Every data source in the workbook is **synthetic course data** or **openly licensed public data**. (Check **Data → Edit Data Source** for each one; a forgotten second data source is published too.)
2. No data source holds **workplace, customer or employee** data, or anything copied from them.
3. Superstore is **not** in the workbook, not even in an unused sheet.
4. The page says the data is **synthetic** (or names the public source and its licence), with units and period.
5. Nothing on the page names a real person, a real company or your employer.
6. I have decided whether to allow downloads, and I know that the views stay public either way.
7. I understand that hiding the viz will not make it private, and that a downloaded copy cannot be recalled.

---

## Part 3: Keeping versions of your workbook

Tableau Desktop Public Edition does not keep a history of your local file. If you overwrite `capstone.twbx` with a broken version, the old one is gone. So keep versions yourself.

### Dated file names

Each time you reach a milestone, choose **File → Save As** and give the file a new name:

```
T4_portfolio_YourName_2026-11-20_v01.twbx
T4_portfolio_YourName_2026-11-22_v02.twbx
T4_portfolio_YourName_2026-11-24_v03_submitted.twbx
```

- Write the date as **year-month-day**, so the files sort in date order.
- Add a **version number** so two saves on one day stay apart.
- Mark the version you **submitted**, and never overwrite it.

!!! tip "`.twbx`, not `.twb`"

    A **packaged** workbook (`.twbx`) holds the data with the views. A plain `.twb` file only points to the data on your computer: send it to someone else and the views break. Keep saving as **Tableau Packaged Workbook (*.twbx)**.

### A change log

A file name says **when**; a change log says **what** and **why**. Keep it as a short table in your evidence log:

| Version | Date | What changed | Why | Checked |
|---|---|---|---|---|
| v01 | 2026-11-20 | First dashboard: tiles, trend, scope note | Capstone outline | Tiles reconcile with the Python register |
| v02 | 2026-11-22 | Changed the headline; added the limitation story point | Peer feedback: headline was a topic | Titles true for every selection |

The **Checked** column matters most. It records what you verified after the change, as in the validation pack of [Session 15](../lectures/15_capstone_studio_lecture.md).

---

## Part 4: Stories and story points

A dashboard shows everything at once and lets the reader explore. A **story** takes the reader through an argument **one step at a time**. In Tableau, a story is a separate tab made of **story points**; each point shows one sheet or dashboard with a short **caption**.

| | Dashboard | Story |
|---|---|---|
| Reader | Looks at everything, chooses where to look | Follows your order, point by point |
| Best for | Monitoring and exploring | Explaining one decision |
| Text | Headline, titles, scope note | A caption for each point, plus the titles |

### Building a story

1. Choose **Story → New Story**. A new tab opens with the **Story** pane on the left.
2. Double-click the story title at the top and write your **headline**.
3. Drag a sheet or dashboard from the Story pane onto the empty area. This is your first story point.
4. Click the caption box above the view and write the point's message in one sentence.
5. Click **Blank** (under **New story point** in the Story pane) to add the next point, and drag the next view in. Click **Duplicate** instead to keep the same view and change a filter or highlight.
6. If you change a filter or a selection in a point, click **Update** above the caption to keep the change in that point.

!!! tip "Three points are enough for a portfolio piece"

    A good short story follows the **question → evidence → limitation and action** order. More points do not make a stronger argument; they make a longer one.

---

## Part 5: Writing a portfolio piece

A portfolio piece is read by someone who has **never seen your course**: a hiring manager, a reviewer, a classmate next year. They give it a minute. In that minute they must understand four things.

| Part | Question it answers | Example (operations case, Session 16) |
|---|---|---|
| **Question** | What decision did this analysis support, and for whom? | *Should the operations manager review the carriers before next year's peak season?* |
| **Evidence** | What does the data show, with numbers in context? | *December promises were kept far less often than in January to October, and one carrier accounts for most of the misses.* (Add the rates, with their denominators.) |
| **Limitation** | What can this data **not** tell us? | *The data shows which promises were missed, not why. It is synthetic data for a fictional retailer.* |
| **Action** | What should happen next, who owns it, and how do we know it worked? | *Review the carrier's peak capacity before November; track the December on-time rate.* |

This is the pyramid from [Session 16, Part 1](../lectures/16_executive_briefings_lecture.md) in a shorter form. The rules you already know still apply:

- **So-what titles** on every view, true for every selection ([Session 16, Part 2](../lectures/16_executive_briefings_lecture.md); [T3, Part 6](T3_dashboards_lecture.md)).
- **Numbers with context**: denominator, period, comparison, unit ([Session 16, Part 3](../lectures/16_executive_briefings_lecture.md)).
- **No false joins.** Your capstone datasets are separate fictional organisations. Never relate or blend two of them in Tableau, and never explain one with another ([Session 15, Part 5](../lectures/15_capstone_studio_lecture.md)). Put them side by side, each on its own data source.
- **No causal claims** the data cannot support.

!!! note "A portfolio piece is not the whole capstone"

    Pick **one** finding that carries your recommendation, and tell it well. Your full capstone stays in your notebook and your brief. The portfolio piece links to them in words: *"Full analysis and checks: capstone notebook, Session 15."*

---

## Quiz

Answer these at the start of the T4 lab. Your facilitator will go through the answers.

1. You publish a dashboard to Tableau Public and turn off downloads. Name two ways a stranger can still learn what is in your data.
2. A friend says: *"I hid the viz on my profile, so it is private now."* What is wrong with this, according to Tableau's FAQ?
3. Your manager asks you to build a quick dashboard of last quarter's team sales and "just put it on Tableau Public so I can see it on my phone". What do you say, and what do you do instead?
4. Why may a dashboard on the course's synthetic marketing data be published only once your facilitator confirms the course's reuse terms, while one on Superstore is not, in this course? What must the published page say about the synthetic data?
5. You have files named `final.twbx`, `final2.twbx` and `final_REAL.twbx`. Name two problems, and rename them following the lecture.
6. Write the four parts of a portfolio piece for this finding: *"Display and Video campaigns returned less attributed revenue than they cost in 2025 (synthetic marketing-v1)."* One sentence per part.
