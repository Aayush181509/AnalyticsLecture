# Lesson notebooks

The `.ipynb` files in this folder **are** the Python sessions (DEC-041, DEC-042, DEC-044). Learners open them in Google Colab with the **Open in Colab** button. The MkDocs pages in `docs/lectures/` are generated from them.

Every session has a **lecture** notebook (theory, demonstrations, check-your-understanding questions, a quiz for the start of the next lecture) and a **lab** notebook (guided, independent and challenge tasks marked Core, Stretch or Challenge). Files are named `NN_topic_lecture.ipynb` and `NN_topic_lab.ipynb`, where `NN` is the session number in `planning/COURSE_PLAN.md`. Private answers live in `instructor/sessions/NN/`.

| Notebook | Session |
|---|---|
| `01_why_data_analytics_lecture.ipynb` | Session 1 lecture: Why data analytics matters |
| `01_why_data_analytics_lab.ipynb` | Session 1 lab: Python, Colab and always plotting your data |
| `02_data_and_grain_lecture.ipynb` | Session 2 lecture: Data, grain and the DataFrame |
| `02_data_and_grain_lab.ipynb` | Session 2 lab: Can we trust the sales table? |
| `03_cleaning_and_preparing_lecture.ipynb` | Session 3 lecture: Cleaning and preparing data |
| `03_cleaning_and_preparing_lab.ipynb` | Session 3 lab: Clean it, check it, log it |
| `04_descriptive_statistics_lecture.ipynb` | Session 4 lecture: Descriptive statistics and distributions |
| `04_descriptive_statistics_lab.ipynb` | Session 4 lab: What does a typical order look like? |
| `05_metrics_and_kpis_lecture.ipynb` | Session 5 lecture: Metrics and KPIs |
| `05_metrics_and_kpis_lab.ipynb` | Session 5 lab: Which segment deserves a closer look? |
| `06_visualisation_principles_lecture.ipynb` | Session 6 lecture: Visualisation principles |
| `06_visualisation_principles_lab.ipynb` | Session 6 lab: From default charts to decision charts |
| `07_trends_and_growth_lecture.ipynb` | Session 7 lecture: Time series and trends |
| `07_trends_and_growth_lab.ipynb` | Session 7 lab: Trends, returns and a decision dashboard |
| `08_correlation_and_regression_lecture.ipynb` | Session 8 lecture: Correlation and regression |
| `08_correlation_and_regression_lab.ipynb` | Session 8 lab: Discount, profit and advertising spend |
| `09_sampling_and_experiments_lecture.ipynb` | Session 9 lecture: Sampling, uncertainty and experiments |
| `09_sampling_and_experiments_lab.ipynb` | Session 9 lab: How sure are we? |
| `10_finance_budget_lecture.ipynb` | Session 10 lecture: Finance: budget accountability |
| `10_finance_budget_lab.ipynb` | Session 10 lab: Which spending needs review? |
| `11_operations_service_lecture.ipynb` | Session 11 lecture: Operations: service performance |
| `11_operations_service_lab.ipynb` | Session 11 lab: Are deliveries on time? |
| `12_marketing_campaigns_lecture.ipynb` | Session 12 lecture: Marketing: campaign evaluation |
| `12_marketing_campaigns_lab.ipynb` | Session 12 lab: Which campaigns deserve the budget? |
| `13_hr_workforce_lecture.ipynb` | Session 13 lecture: HR: workforce analytics |
| `13_hr_workforce_lab.ipynb` | Session 13 lab: Is workforce change creating a capacity problem? |
| `14_dashboards_storytelling_lecture.ipynb` | Session 14 lecture: Dashboards and storytelling |
| `14_dashboards_storytelling_lab.ipynb` | Session 14 lab: From analysis to a decision dashboard |
| `15_capstone_studio_lecture.ipynb` | Session 15 lecture: Capstone studio: combining evidence |
| `15_capstone_studio_lab.ipynb` | Session 15 lab: Build your capstone |
| `16_executive_briefings_lecture.ipynb` | Session 16 lecture: Executive briefings |
| `16_executive_briefings_lab.ipynb` | Session 16 lab: Brief, critique, revise |

## Workflow

1. Edit the notebook in Jupyter or Colab.
2. Execute all notebooks so they carry fresh outputs, and check the data:

    ```bash
    python scripts/run_notebooks.py --check-data
    ```

3. Convert them to Markdown for the site with the existing Makefile:

    ```bash
    make convert-all      # writes docs/lectures/*.md and *_files/ images
    ```

4. Check the site: `python3 scripts/check_docs.py` and `mkdocs build --strict`.

Use a Python 3.12 environment (matching Colab) built from `requirements.txt`, for example the gitignored project `.venv` (`uv venv -p 3.12 .venv && uv pip install -p .venv/bin/python -r requirements.txt`). Agent brief: `planning/agents/notebook-author.md`. pandas 2.2.3 does not run on Python 3.14.

## Conventions

- Synthetic case data (marketing-v1, finance-v1, operations-v1, hr-v1) is loaded by a dataset-specific setup cell that downloads from this repo on GitHub, checks SHA-256 and honours a `COURSE_*_DIR` offline override (set automatically by `run_notebooks.py`). Keep each dataset's setup cell identical wherever it is used.
- Every notebook that uses Superstore starts with the same **setup cell** as its first code cell. It downloads the Superstore sample from Tableau's site, checks its SHA-256 and defines `load_orders()`. Keep it identical in every notebook; `--check-data` enforces this and confirms it reproduces `data/prepared/superstore/retail-v1/order_lines.csv` exactly.
- Callouts are Markdown blockquotes (`> **Title**`), so they render well both in Colab and on the site. Do not use MkDocs `!!!` admonitions inside notebooks.
- Markdown cells must not hand-type result numbers; the executed outputs show them. "Your turn" exercise cells give working default code for learners to change; their answers go in `instructor/`, never in the notebooks.
- Links between lessons use the converted page names, for example `02_data_and_grain_lab.md`.
