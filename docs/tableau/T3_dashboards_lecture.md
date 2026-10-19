# T3 lecture: Dashboards

<p class="lead">
Learn to put several sheets on one page that a busy manager can read in a minute. A good dashboard answers one question, is read in a set order, lets the reader filter without breaking the numbers, and still makes sense without colour.
</p>

In the [Session 14 lecture](../lectures/14_dashboards_storytelling_lecture.md) you built a decision dashboard in Python: KPI tiles, a monthly trend, two ranked comparisons and a scope note. Today you learn how Tableau builds the same kind of page. The design rules do not change; only the tools do. In the T3 lab you rebuild the Session 14 dashboard in Tableau, using the fields you made in T1 and T2. The Stretch task builds a second dashboard on the marketing case from [Session 12](../lectures/12_marketing_campaigns_lecture.md).

---

## What you will be able to explain

1. The difference between a **sheet** and a **dashboard**, and why a dashboard has **one message**.
2. How readers scan a page, and how to use that **reading order** in a layout.
3. What a good **KPI tile** shows, and how to build one in Tableau.
4. The difference between a **filter**, a **filter action** and a **highlight action**, and which views each one changes.
5. How to use **colour** with purpose and make a dashboard readable for people with colour-vision deficiency: **never colour alone**.
6. How to write **message titles**, **annotations** and a **scope note** in Tableau.
7. Why you check a dashboard's **size** and its **phone layout** before you share it.

---

## Part 1: From sheets to a dashboard

In T1 and T2 every chart lived on its own **sheet** (worksheet). A **dashboard** is a separate tab that places several sheets on one page, together with text, images and filter controls.

| | Sheet | Dashboard |
|---|---|---|
| What it holds | One chart or table | Several sheets, plus text, filters and legends |
| Where you build it | Shelves and the Marks card | The **Dashboard** pane: drag sheets onto the page |
| How you create it | **Worksheet → New Worksheet** | **Dashboard → New Dashboard** |
| Where you edit a chart | On the sheet | On the sheet. The dashboard shows the sheet; it does not copy it |

!!! note "Edit the sheet, not the dashboard"

    A dashboard shows live sheets. If you change a sheet (its colour, its title, a filter on it), the dashboard changes too. To change a chart, go back to its sheet tab.

### One message per dashboard

A dashboard is **explanatory**, not exploratory ([Session 14, Part 1](../lectures/14_dashboards_storytelling_lecture.md)). Before you open a new dashboard, write down three things:

1. **Who** will read it, and what they already know.
2. **What decision** they face.
3. Your **big idea**: one sentence with a point of view and what is at stake ([Storytelling with data](../foundations/storytelling.md)).

Every view on the page must help with that one message. If a chart does not, it belongs in your workbook, not on the dashboard. Session 14 gave a rule of thumb: **three to five views**, with the KPI tiles counting as one.

!!! tip "Sketch it on paper first"

    Draw boxes on paper for the tiles, the charts and the scope note before you open Tableau. Moving a box on paper takes a second. Moving a sheet on a dashboard takes much longer.

---

## Part 2: Layout and reading order

Readers of a page in English start at the **top left**, move right, then down. They spend most attention on the top of the page and less on each step down.

So a decision dashboard uses this order:

| Position | What goes there | Why |
|---|---|---|
| **Top**, as the dashboard title | The **headline**: your big idea as a message title | Read first. If the reader stops here, they still have the message |
| **Top row** | **KPI tiles**: three to five headline numbers, each with a comparison | Answers "how are we doing?" before any chart |
| **Middle, full width** | The **main view**, usually the trend | The widest space for the view that needs it |
| **Bottom row** | Supporting comparisons, for example by segment or region | Detail for the reader who wants it |
| **Bottom edge** | The **scope note** | Period, units, source, filters and the main limit: small, but always on the page |

This is the layout of the Session 14 decision dashboard. You rebuild it in the lab.

### Tiled and floating objects

When you drag a sheet onto a dashboard, it is either **tiled** or **floating**. You choose at the bottom of the **Objects** section in the Dashboard pane.

| | Tiled | Floating |
|---|---|---|
| How it sits | In a grid. Objects never overlap; Tableau resizes the neighbours | On top of the page, at a position and size you set |
| Use it for | Almost everything | Small items, such as a legend placed over an empty corner of a chart |
| Risk | Few | Objects can cover each other, especially on a smaller screen |

Use **tiled** objects for this course.

### Containers

A **container** is a box that holds other objects and arranges them in one line.

- A **Horizontal** container places its objects side by side. Use it for a row of KPI tiles, or for two comparison charts.
- A **Vertical** container stacks its objects. A whole dashboard can be one vertical container holding the rows of your sketch.

You find both under **Objects** in the Dashboard pane. To share space equally, select the container (click its grey top edge, or choose it in the **Layout** pane) and choose **Distribute Contents Evenly** from its drop-down menu.

### Size

Tableau can draw a dashboard at a **fixed size** or let it stretch to the screen (**Automatic**). You set this under **Size** in the Dashboard pane.

| Size setting | What happens | When to use |
|---|---|---|
| **Fixed size**, for example *Generic Desktop* | The page always has the same width and height | When you export a PDF or image, or share with others. What you see is what they see |
| **Automatic** | The page fits whatever window opens it | For your own use. Text and charts can be squeezed on a small screen |

!!! warning "Set the size before you arrange anything"

    If you change the size after laying out the page, Tableau moves and resizes every object. Choose **Fixed size** first, then build.

---

## Part 3: KPI tiles

A **KPI tile** (also called a big number) is a small sheet that shows one headline number. A good tile has four parts:

| Part | Example |
|---|---|
| **Label**: what is measured, and for which period | *Sales, 2025* |
| **Value**, large | the number, rounded for reading |
| **Comparison**, so the reader knows if it is good | *+x% vs 2024*, or *target y* |
| **Unit**, on the tile or in the scope note | *file's own monetary units* |

A number without a comparison cannot be judged. Is a profit ratio of 10% good? Only a comparison (last year, another region, a target) tells you.

### Building a tile in Tableau

A tile is a sheet with **one mark** and only text:

1. Create a sheet and drag the measure onto **Text** on the Marks card. The view shows one number.
2. Drag the comparison measure onto **Text** as well. Both pills now sit on the Marks card.
3. Click **Text** on the Marks card, then the **...** button, to edit the text. Write the label on the first line, the value on the second and the comparison on the third. Make the value larger.
4. Hide the sheet title or turn it into the label.

The tile uses the same rules as any KPI from T2:

- Ratios are **ratios of sums**, for example `SUM([Profit]) / SUM([Sales])`, never the average of ratios.
- Order counts use **`Distinct Orders`**, never the row count.
- Growth compares **whole years**, so the season cancels out ([Session 7 lecture](../lectures/07_trends_and_growth_lecture.md)).

### A value for one year

A tile for **2025** with a comparison to **2024** needs both years in the same sheet. A filter to 2025 would remove 2024. Instead, put the year **inside** the calculation:

```
Sales 2025 = SUM(IF YEAR([Order Date]) = 2025 THEN [Sales] END)
```

Read it as: *for each order line, keep Sales if the order was placed in 2025, otherwise leave it blank; then add up*. The `IF` works row by row; the `SUM` around it makes the whole field an aggregate. You met both kinds in [T2, Part 1](T2_calculations_kpis_lecture.md). With a matching `Sales 2024` field, the growth is:

```
Sales Growth = [Sales 2025] / [Sales 2024] - 1
```

!!! tip "Tiles must reconcile"

    A tile is still a number you can check. Sales 2025 on the tile must equal the 2025 Sales of your trend chart added up, and the 2025 Sales of the regions added up. You do these checks in the lab.

---

## Part 4: Filters and actions

A dashboard is interactive: the reader can narrow it down. Tableau offers several ways, and they differ in **which views change** and **what happens to the other marks**.

| Tool | How the reader uses it | What it does | Where you set it up |
|---|---|---|---|
| **Filter** (a filter control) | Picks values in a list or drop-down on the page | Removes the other values from the views it applies to | On a sheet: right-click a pill on the Filters shelf → **Show Filter** |
| **Filter action** | Clicks a mark in one view, for example a region bar | Removes the other values from the **target** views | **Dashboard → Actions... → Add Action → Filter...** |
| **Highlight action** | Clicks a mark | Keeps every mark, but **dims** the marks that do not match | **Dashboard → Actions... → Add Action → Highlight...**, or the highlighter on a colour legend |

### Filters: which sheets do they apply to?

A filter you add on one sheet applies **only to that sheet** at first. On a dashboard, the other views ignore it. So the trend may change while the tiles do not, and the page tells two different stories.

To make one filter control change several views, click the filter control's drop-down menu on the dashboard and choose **Apply to Worksheets**:

| Option | Applies to |
|---|---|
| **Only This Worksheet** | One sheet (the default) |
| **Selected Worksheets...** | The sheets you tick |
| **All Using Related Data Sources** / **All Using This Data Source** | Every sheet that uses the same data |

!!! warning "Write the filter on the page"

    A reader who prints the dashboard does not see which region was selected. If a view is filtered, say so in its title or in the scope note.

### Filter actions: click to filter

A **filter action** turns a chart into a filter. The reader clicks the **West** bar, and the KPI tiles and the trend show West only. Click the bar again (or press **Esc**) and everything comes back.

When you add a filter action, Tableau asks:

| Setting | Meaning | Usual choice |
|---|---|---|
| **Source Sheets** | The view the reader clicks | The comparison chart, for example the region bars |
| **Run action on** | **Hover**, **Select** (click) or **Menu** | **Select** |
| **Target Sheets** | The views that change | The tiles and the trend. Usually not the source itself, so the reader still sees all regions to click |
| **Clearing the selection will** | What happens when the reader clicks the mark again | **Show all values** |

There is also a shortcut. On a dashboard, select a sheet and click its **Use as Filter** icon (a funnel) at the top right of the sheet. Tableau creates a filter action from that sheet to every other sheet on the dashboard. Open **Dashboard → Actions...** afterwards to see and edit it.

!!! note "A filter action is a dimension filter"

    In the filter order from [T1, Part 6](T1_fundamentals_lecture.md), a filter action works like a **dimension filter**. So everything you learned in T2 still applies. Table calculations such as `LOOKUP` see only the marks left after the filter: filtering on Region is safe for a monthly growth chart, but filtering on **months** breaks it ([T2, Part 5](T2_calculations_kpis_lecture.md)). A **FIXED** expression such as `Order Total` ignores the action, because FIXED is calculated before dimension filters.

### Highlight actions: keep the context

A **highlight action** dims the marks that do not match the reader's click, but keeps them on the page. Use it when the other marks are useful context:

- On a chart with one bar per channel in **two** views, clicking a channel in one view highlights the same channel in the other.
- On a line chart with one line per year, clicking the legend's **2025** dims the other years.

| Use a **filter** (or filter action) when... | Use a **highlight** when... |
|---|---|
| The reader wants the numbers for one group only, for example the tiles for one region | The reader wants to see one group **against** the others |
| Totals and tiles must change | Totals and tiles must stay the same |

---

## Part 5: Colour and accessibility

[Designing clear visuals](../foundations/visual-design.md) and [Session 14, Part 5](../lectures/14_dashboards_storytelling_lecture.md) gave the rules. Here is how they look in Tableau.

### Colour with a purpose

1. **Grey for context, one colour for attention.** Session 14 used grey for comparison values, blue for the current period and orange for the one thing that needs attention. In Tableau, click **Color** on the Marks card and choose **Edit Colors...** to set each value's colour by hand.
2. **One meaning per colour, across the whole page.** If 2025 is blue in the trend, it must be blue on every sheet. If orange means "needs attention", nothing else is orange.
3. **Do not colour by a field just because you can.** A bar chart of four regions does not need four colours: the bar labels already tell the regions apart.

### Colour-blind-safe palettes

About one in twelve men has some colour-vision deficiency, most often difficulty telling **red from green**. Tableau has a palette designed for this:

1. Click **Color** on the Marks card and choose **Edit Colors...**.
2. Open the **Select Color Palette** list and choose **Color Blind**.
3. Click **Assign Palette**, then **OK**.

Blue and orange, the pair used in Session 14, stay easy to tell apart for most readers. Red against green, the default "bad against good" pair, does not.

### Never colour alone

Colour should **repeat** a message, not carry it alone. Every highlighted mark also needs at least one of these:

| Instead of only colour | Add |
|---|---|
| An orange bar | Its **value** as a label, and a **message title** that names it |
| A blue line for 2025 and a grey line for 2024 | The **year written** at the end of each line |
| A red or green tile | A **sign** (+ or -) and the words *vs 2024* |

Test it: print the dashboard in black and white, or look at it through your phone's greyscale mode. Can you still find the bar your title is about?

!!! tip "Text you can read"

    Keep text at a size you can still read when the page is shown at half size. Grey text on a white background must be dark enough to read: Tableau's lightest greys are for gridlines, not for words.

---

## Part 6: Message titles, annotations and the scope note

### Message titles

A **message title** says what the reader should notice; a descriptive title only says what is plotted ([Session 14, Part 2](../lectures/14_dashboards_storytelling_lecture.md)). In Tableau:

- **Sheet title:** double-click the title on the sheet and type. The **Insert** menu in the edit window can add a field value, such as the selected region, to the title.
- **Dashboard title:** choose **Dashboard → Show Title**, then double-click the title to edit it. This is where your **headline** goes.

!!! warning "A title must stay true"

    A message title is written for the data you see now. When a reader clicks a region, the trend shows that region only, but a title such as "*Sales rose in every month*" may no longer be true. Write titles that hold for every selection, or say in the title which selection it describes, and check by clicking every region yourself.

### Annotations

An **annotation** is a short note placed on the chart, next to the mark it explains. It is read at the right moment, unlike a paragraph under the chart.

1. On a sheet, right-click a mark and choose **Annotate**.
2. Choose **Mark** (a note tied to one mark), **Point** (a position on the chart) or **Area** (a region of the chart).
3. Type a short note, for example *"Same month last year was the year's low."*

Keep annotations to one or two per view.

### The scope note

On the dashboard, drag a **Text** object from **Objects** to the bottom of the page. Write:

- the **period** (orders placed 2023 to 2025, or the years shown),
- the **units** (the file's own monetary units, or the case's currency units),
- the **source** (Superstore, a fictitious sample published by Tableau),
- any **filters** or actions the reader should know about,
- the **main limit** (for example, the returns list shows which orders are listed, not why or for how much).

---

## Part 7: Size, phone layout and export

A dashboard is often opened on a phone. Tableau lets you design a separate **phone layout** of the same dashboard.

1. At the top of the Dashboard pane, click **Device Preview**.
2. Choose **Phone** as the device type.
3. Click **Add Phone Layout**. Tableau creates a layout that stacks the views in one column.
4. In the phone layout, remove or reorder views. On a phone, keep the headline, the tiles and the one most important chart.
5. Click **Default** (at the top of the Dashboard pane) to return to the desktop layout.

The phone layout shows the same sheets, so a change to a sheet changes both layouts.

### Exporting for others

When you send a dashboard as a file, the reader cannot click it. So the PDF or image must stand on its own: headline, tiles, titles and the scope note must say everything.

- **File → Print to PDF...** saves the dashboard as a PDF. Choose **Active Sheet** when the dashboard is the open tab.
- **Dashboard → Export Image...** saves a picture of the page.

Clear any selection before you export, unless the export is meant to show one region; then say so in the title.

---

## Quiz

Answer these at the start of the T3 lab. Your facilitator will go through the answers.

1. Readers scan a dashboard from the top left. Where do you place the headline, the KPI tiles, the main trend and the scope note, and why?
2. A KPI tile shows only *"Sales: 1.2 million"*. Name two things it is missing, and explain why each matters.
3. You add a **Region** filter control on the trend sheet. On the dashboard, the trend changes when you pick a region, but the KPI tiles do not. Why, and how do you fix it?
4. What is the difference between a **filter action** and a **highlight action**? Give one situation where each is the better choice.
5. A dashboard colours tiles **red** for "below target" and **green** for "above target", with no other sign. Name two problems and two fixes.
6. Your dashboard title names the region with the highest share of orders on the returns list. A reader clicks a **different** region's bar, which filters the tiles and the trend. Which parts of the page can still be trusted, and what would you change so the title stays true?
