# Setup

<p class="lead">
Everything in this course runs on your own computer, without needing Google or GitHub. Set it up before the first day and check it with the setup notebook.
</p>

---

## What you need

- A laptop (Windows or macOS), or a classroom lab PC
- **Anaconda**, which gives you Python and Jupyter
- **Tableau** (for Lab 2 and the readiness check)
- **Microsoft Excel** (for Labs 6–7 and Assignment 3)
- The course folder of notebooks and data, provided by your facilitator

---

## 1. Install Anaconda

1. Download the **Anaconda Distribution** installer for your computer and run it with the default options.
2. Open **Anaconda Navigator** and launch **JupyterLab**. (Or open "Anaconda Prompt" / Terminal and type `jupyter lab`.)
3. A browser tab opens with JupyterLab. This is where you run every notebook.

!!! tip "Two extra packages"

    Lab 3 needs `wordcloud`. Open Anaconda Prompt (Windows) or Terminal (macOS) and run:

    ```
    pip install wordcloud
    ```

    Your facilitator may provide an offline installer if the internet connection is slow.

---

## 2. Unzip the course folder

1. Copy the course folder you receive (for example `China_Classroom.zip`) to your Documents folder and unzip it.
2. Inside you will find the notebooks and a `data` folder. **Keep them together**: the notebooks load data from that folder, so they work without internet.
3. In JupyterLab, use the file browser on the left to open the folder.

---

## 3. Run the setup check

Open the setup check notebook from the course folder and run all cells (**Run → Run All Cells**). It confirms that Python and every package the course needs are installed, and that the data files load. If any line says **MISSING**, show it to your facilitator.

---

## 4. Tableau

1. Claim the free **Tableau for Students** licence with your university email, then download and activate Tableau Desktop.
2. Open it and check that you can open the **Sample – Superstore** data source.

---

## 5. Excel

Labs 6–7 and Assignment 3 use **Microsoft Excel** (`RAND()`, `NORM.INV()` and **Data Table**). It is installed on the lab PCs; if you use your own laptop, check that Excel opens before Day 5 (Tuesday 17 November).

---

## Running and submitting a notebook

1. Open a notebook, then choose **Run → Run All Cells**, or run cells one by one with **Shift + Enter**.
2. Save often with **Ctrl + S** (Windows) or **Cmd + S** (macOS).
3. To submit, follow the instructions in each lab. Most labs ask you to export the notebook to **PDF** (**File → Print**, then *Save as PDF*) and upload it to the matching assignment on **GAP (Moodle)**.

### Combining PDFs without internet

Several labs and assignments ask for one PDF made from two parts, for example your written answers and a dashboard or notebook. Online PDF tools are often blocked, so combine them on your own computer:

- **Word (any computer):** put everything in one Word document. Paste the dashboard or notebook output as pictures on new pages after your answers (in Tableau, **Dashboard → Export Image**), then **File → Save As → PDF**.
- **macOS Preview:** open the first PDF, choose **View → Thumbnails**, drag the second PDF into the sidebar below the last page, then **File → Export as PDF**.
- **Adobe Acrobat** (if installed): **Tools → Combine Files**.

Check that the final PDF has the parts in the order the lab asks for and the exact file name it gives.

!!! warning "Only use course data"

    Never use private company, customer or personal data in course work.
