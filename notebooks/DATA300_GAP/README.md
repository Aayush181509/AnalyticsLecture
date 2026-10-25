# DATA 300 — GAP course notebooks

Lecture notebooks for DATA 300 *Data Driven Decision Making* (Westcliff University), taught in person in China, 10–19 November 2026, following the course as it runs on GAP (Moodle). Learner pages: `docs/data300/`. Design: `planning/data300_gap/2026-10-25-design.md`.

This section is **separate** from the China classroom section (`notebooks/China_Classroom/`, `docs/china/`) and from the 16-session Python course. Those files are not edited from here.

## Rules for this section

- **Offline.** Every notebook loads data from `data/` next to it, relative to this folder. No `urllib`, `open_url`, `pyfetch`, `%pip`, `nltk.download` or GitHub URLs in notebooks. The bundle and its checksums are in `data/SOURCES.md`. The CO₂ series comes from `statsmodels`.
- **NLTK.** Notebooks that need NLTK use the offline setup cell in `planning/agents/china-notebook-author.md`, exactly as written there.
- **Two routes for students.** Students may follow GAP's Try JupyterLab (Pyodide) instructions (Route A) or work offline in local Anaconda JupyterLab with this bundle (Route B). The guide pages in `docs/data300/guides/` describe both.
- **Our own words.** Never copy Moodle or reading-packet prose; never reproduce Moodle code blocks in full. Credit as "Adapted from the DATA 300 GAP course, <item>".
- **No graded answers.** Lecture notebooks teach on non-graded data or ask different questions from the graded work, so their outputs never reveal a graded answer. Guide pages show code only, never its outputs.
- **Teach beyond Moodle.** Lectures add theory, worked examples, "predict, then run" questions, misconceptions, a business case, Core / Stretch / Challenge practice, a quiz, a reading-packet pointer and a closing "For the facilitator" timing table.
- **Private material** (answers, test scripts) goes only in `instructor/data300_gap/`, which is gitignored. Never `git add -f`.

## Layout

| Name | Contents |
|---|---|
| `D0_lecture_*.ipynb` | Pre-class self-study (before Tuesday 10 November) |
| `Dn_lecture_<topic>.ipynb` | Lecture for teaching day n (1–7) |
| `data/` | Offline bundle and `SOURCES.md` |

## Build

```bash
.venv/bin/python scripts/run_notebooks.py notebooks/DATA300_GAP/<file>.ipynb   # run twice; SHA-256 must not change
.venv/bin/jupyter nbconvert --to markdown notebooks/DATA300_GAP/<file>.ipynb --output-dir=docs/data300/
```
