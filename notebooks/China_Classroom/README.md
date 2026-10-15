# DATA 300 — China classroom notebooks

Notebooks for the intensive in-person DATA 300 *Data Driven Decision Making* course (7 teaching days, 10–19 November 2026). Plan: `planning/china_classroom/PLAN.md`. Learner pages: `docs/china/`.

This is a **separate course** from the 16-session Python course in `notebooks/`. Notebooks here may be adapted copies of those sessions; the originals are not edited.

## Rules specific to this classroom

- **Offline first.** Google Colab and GitHub downloads are unreliable or blocked in mainland China. Every notebook loads data from `data/` next to it (no `urllib`, no `open_url`, no Colab badges). Datasets the syllabus downloads (penguins, diamonds, tips, mpg, CO₂, the VADER lexicon) are bundled here.
- **Local Jupyter (Anaconda).** Use only packages included in Anaconda plus `wordcloud`; a setup-check notebook verifies them.
- **Syllabus labs are graded work** and keep their questions, weights and CLOs; adapted only to load local data. Teaching notebooks reuse our course material.
- Private answers go to `instructor/china_classroom/` (gitignored), never here.

## Planned layout

| Prefix | Contents |
|---|---|
| `00_setup_check.ipynb` | Package and data check for students' machines |
| `00_preclass_*` | Pre-class self-study and Activity 1 |
| `D1_*` … `D7_*` | One folder-free set per teaching day: `Dn_lecture_<topic>.ipynb` (theory) and `Dn_lab_<lab>.ipynb` (graded lab, offline-ready) |
| `data/` | Bundled datasets and lexicons, with a `SOURCES.md` listing origin and terms |
