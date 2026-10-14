# Lesson notebooks

The `.ipynb` files in this folder **are** the Python lessons (DEC-041, DEC-042). Learners open them in Google Colab with the **Open in Colab** button. The MkDocs lesson pages in `docs/lectures/` are generated from them.

| Notebook | Lesson |
|---|---|
| `00_python_and_colab_basics.ipynb` | Lesson 0: Python and Colab basics |
| `01_decision_to_evidence.ipynb` | Lesson 1: From decision to evidence |
| `02_trust_the_sales_table.ipynb` | Lesson 2: Can we trust the sales table? |
| `03_segment_comparison.ipynb` | Lesson 3: Which segment deserves a closer look? |
| `04_trends_returns_dashboard.ipynb` | Lesson 4: Trends, returns and a decision dashboard |

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

Use a Python 3.12 environment (matching Colab) built from `requirements.txt`. pandas 2.2.3 does not run on Python 3.14.

## Conventions

- The first code cell in Lessons 1–4 is the same **setup cell**. It downloads the Superstore sample from Tableau's site, checks its SHA-256 and defines `load_orders()`. Keep it identical in every notebook; `--check-data` enforces this and confirms it reproduces `data/prepared/superstore/retail-v1/order_lines.csv` exactly.
- Callouts are Markdown blockquotes (`> **Title**`), so they render well both in Colab and on the site. Do not use MkDocs `!!!` admonitions inside notebooks.
- Markdown cells must not hand-type result numbers; the executed outputs show them. "Your turn" exercise cells give working default code for learners to change; their answers go in `instructor/`, never in the notebooks.
- Links between lessons use the converted page names, for example `02_trust_the_sales_table.md`.
