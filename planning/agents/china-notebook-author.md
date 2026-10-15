# China classroom notebook author (DATA 300)

Reusable role brief; this file does not start an agent or prove the role ran. It extends `notebook-author.md`. Read that brief first, then apply these differences, which take precedence.

## Context

- DATA 300 *Data Driven Decision Making* (Westcliff University), taught intensively in person in China, 10–19 Nov 2026 (DEC-051).
- Plan, day mapping and period budget: `planning/china_classroom/PLAN.md`.
- Learner pages: `docs/china/`; the notebook rules are in `notebooks/China_Classroom/README.md`.
- **Authority for structure, weights and modules: the WUT syllabus** (`DATA_300_WUT_*.pdf`, repo root, gitignored; text at `/tmp/claude-501/wut_clean.txt`). **Detailed lab and assignment content** (datasets, tasks, questions) comes from the larger `DATA300_*.pdf` (text at `/tmp/claude-501/syllabus_clean.txt`). If those text files are gone, extract them with pypdf. Graded weights and module days are in `planning/china_classroom/PLAN.md` (WUT): use those weights, not the larger syllabus's. There are no SM activities; there is a midterm (15%, Module 1 Day 3) and a final exam (20%, Module 2 Day 4). Python basics and Activity 1 are pre-class (files `00_preclass_*`).
- Confirmed:
  - Students run **local Jupyter (Anaconda)**.
  - Students submit on **GAP (Moodle)**.
  - Students use the **Tableau student licence** and **Microsoft Excel**.
  - Deadlines are as in `docs/china/schedule.md`, in China time.
  - We write the midterm.

## Differences from the main course

- **Offline only.** No Colab badges, no `urllib`/`open_url`/`pyfetch`, no `%pip install`, no GitHub URLs. Load data with `pd.read_csv("data/<file>.csv")`, relative to `notebooks/China_Classroom/`. Bundled files and checksums are listed in `notebooks/China_Classroom/data/SOURCES.md`. The CO₂ series comes from `statsmodels.api.datasets.co2`.
- **NLTK offline setup** (use exactly this in any notebook that needs NLTK):

```python
import zipfile
from pathlib import Path

import nltk

NLTK_DIR = Path("data/nltk_data").resolve()
if not (NLTK_DIR / "tokenizers" / "punkt_tab").exists():
    with zipfile.ZipFile(NLTK_DIR / "tokenizers" / "punkt_tab.zip") as z:
        z.extractall(NLTK_DIR / "tokenizers")
nltk.data.path.insert(0, str(NLTK_DIR))
```

- **Allowed packages:** Anaconda defaults (numpy, pandas, matplotlib, seaborn, statsmodels, scikit-learn, nltk) plus `wordcloud`. Seaborn is allowed here because the syllabus uses it.
- **Graded labs and assignments** keep the syllabus's dataset, tasks, question substance, deliverables, file naming, weights and CLOs. Write the instructions **in our own words**; do not copy syllabus prose verbatim, because the syllabus carries a copyright notice and this repository is public. Code may follow the syllabus's approach. Credit the source, for example: "Adapted from the DATA 300 syllabus, Applied Lab 1". Submission is a PDF export uploaded to **GAP (Moodle)**.
- **Lecture notebooks** reuse and adapt our course material (`docs/foundations/`, `notebooks/NN_*`). Adapt by copying content into the China notebook and replacing data cells with local loading. Never edit the original notebooks.
- **Names:** `notebooks/China_Classroom/Dn_lecture_<topic>.ipynb` and `Dn_lab_<item>.ipynb`, where n is the teaching day 1–7. Titles start "# Day n lecture: …" or "# Day n lab: …".
- **Pages:** convert each notebook with `.venv/bin/jupyter nbconvert --to markdown notebooks/China_Classroom/<file>.ipynb --output-dir=docs/china/` (the same command the Makefile uses). Links between China pages use the converted names.
- **Private answers:** write them to `instructor/china_classroom/Dn/answers.md`, which is gitignored.

## Build and check

```bash
cd /Users/aayush/Documents/Kings/Data
.venv/bin/python scripts/run_notebooks.py notebooks/China_Classroom/<file>.ipynb   # run twice; sha256 must not change
```

`run_notebooks.py` executes each notebook from its own folder, so `data/` paths resolve. Read the generated pages and check them. Report as in `notebook-author.md`.
