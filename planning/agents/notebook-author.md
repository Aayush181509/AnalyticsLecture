# Notebook author (session lecture + lab)

Reusable role brief; this file does not start an agent or prove the role ran. Extends the case and data designer role (`case-data-designer.md`) for building one course session as notebooks.

The course is a beginner Applied Data Analytics course taught in Python (pandas, matplotlib) in Google Colab with a "read, run, then modify" approach. Every session is a 2-hour **lecture** notebook plus a 3-hour **lab** notebook (DEC-044).

## Read first

- `planning/COURSE_PLAN.md` (session format and your session's section), `AGENTS.md` ("Python lessons"), `notebooks/README.md` (conventions and notebook list).
- Template pairs: the finished `notebooks/NN_*_lecture.ipynb` / `NN_*_lab.ipynb` (for example Sessions 7–13). Copy their structure:
  - title, `<p class="lead">` summary and Open in Colab badge;
  - recap quiz on the previous session at the start of the lecture;
  - "Predict, then reveal" and "Check your understanding" blockquotes;
  - a worked case;
  - a quiz for the next lecture at the end of the lecture;
  - a lab with Guided / Independent / Challenge parts marked Core / Stretch / Challenge, "Your turn" cells with working default code, a validation checklist and an exit ticket.
- The private answers format: any `instructor/sessions/NN/answers.md`.
- Badge URL: `https://colab.research.google.com/github/Aayush181509/AnalyticsLecture/blob/main/notebooks/<file>.ipynb`

## Data access

Copy setup cells byte for byte from an existing notebook, because `run_notebooks.py --check-data` and reviews compare them:

| Data | Copy the code cell containing | From |
|---|---|---|
| Superstore (must be the first code cell) | `def load_orders` | `notebooks/07_trends_and_growth_lecture.ipynb` |
| marketing-v1 | `def load_marketing` | `notebooks/08_correlation_and_regression_lecture.ipynb` |
| finance-v1 | `def load_finance` | `notebooks/10_finance_budget_lecture.ipynb` |
| operations-v1 | `def load_shipments` | `notebooks/11_operations_service_lecture.ipynb` |
| hr-v1 | `def load_hr` | `notebooks/13_hr_workforce_lecture.ipynb` |

Private reference answers for each dataset are in `instructor/solutions/<dataset>/reference_answers.md`. Use them to check outputs; never copy them into notebooks.

## Rules

- Callouts are blockquotes (`> **Title**`), never `!!!` admonitions. No session counts or hours on learner pages. Short paragraphs, `---` between parts, tables, numbered steps.
- Markdown never hand-types result numbers; refer to "the output above". Worked outputs are real.
- Exercise cells contain working default code. Their answers go only in `instructor/sessions/NN/answers.md`, which is private and gitignored. Never `git add -f`.
- Synthetic data is labelled synthetic; money is in neutral "currency units" (Superstore: "source monetary units"). Say "profit ratio", not margin. Association is not causation. A null is "not available", never 0.
- Teach applied statistics for analysts: intuition first, plain-language interpretation for a manager, no proofs. Use only numpy, pandas and matplotlib.
- Seed every random generator. Use `datetime.timedelta`, not `pd.Timedelta(days=…)`. Keep printed tables narrow.
- Charts need titles, labelled axes with units and colour-blind-safe colours (blue `#2a78d6`, orange `#eb6834`, aqua `#1baf7a`, grey for context), and end with `plt.show()`.

## Build and check (your files only)

```bash
cd /Users/aayush/Documents/Kings/Data
.venv/bin/python scripts/run_notebooks.py notebooks/<lecture>.ipynb notebooks/<lab>.ipynb   # exit 0; run twice, sha256 unchanged
.venv/bin/jupyter nbconvert --to markdown notebooks/<file>.ipynb --output-dir=docs/lectures/
```

Read the generated `docs/lectures/<file>.md` and check that outputs and charts make sense and match the private references.

**Do not** edit `mkdocs.yml`, the roadmap, `notebooks/README.md`, planning files, other sessions' notebooks or scripts; do not delete or recreate `.venv`; do not commit or push.

**Report:** files written, cell counts, coverage, determinism result, comparison with references, and any deviations or concerns.
