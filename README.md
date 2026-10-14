# Practical Data Analytics course

A course under development for working professionals: twelve two-hour live classes, hands-on Tableau Public, five business domains, and optional Python/pandas companions. Learners will turn business questions into validated recommendations, supported by a practical portfolio and executive briefing.

**Current state: planning foundation, source audit and first prepared retail development dataset.** The curriculum and pilot are outlines. The retail CSV and provenance are local; full lessons, notebooks and reference Tableau workbooks remain to produce. See the [Claude takeover brief](planning/CLAUDE_TAKEOVER.md) for validation evidence and the remaining Tableau checks. This is not a classroom or public release.

## Start here

- [Project context](planning/PROJECT_CONTEXT.md): confirmed requirements, recommendations and open questions.
- [Curriculum](planning/CURRICULUM.md): 12-session sequence, outcomes, pacing options and practice.
- [Case studies](planning/CASE_STUDIES.md), [data strategy](planning/DATA_STRATEGY.md) and [catalog shortlist](planning/DATA_CATALOG.md): core cases, hybrid sourcing and additional topics.
- [Source audit](planning/SOURCE_AUDIT.md) and [rights evidence](planning/SOURCE_RIGHTS.md): actual file capabilities, quality issues, proposed uses and unresolved release conditions. [Data commands](data/README.md) reproduce the local inspection.
- [Retail contract](data/metadata/superstore/retail-v1/metric_contract.md), [dictionary](data/metadata/superstore/retail-v1/dictionary.md) and [preparation specification](data/metadata/superstore/retail-v1/preparation_spec.md): first source-specific development design and its verification rules.
- [Assessment](planning/ASSESSMENT.md) and [pilot outline](planning/PILOT_LESSON.md).
- [Tasks](planning/TASKS.md), [status](planning/STATUS.md), [decisions](planning/DECISIONS.md) and [handoff](planning/HANDOFF.md): current work and next steps.
- [Claude takeover](planning/CLAUDE_TAKEOVER.md): start here when continuing this project in Claude.
- [Initial inventory](planning/WORKSPACE_INVENTORY.md) and [documentation plan](planning/DOCUMENTATION_PLAN.md).

## Workspace map

| Location | Purpose |
|---|---|
| `docs/` | Learner site source; only this directory is published by MkDocs. |
| `planning/` | Internal curriculum design, backlog, decisions and reusable agent roles. |
| `instructor/` | Teaching notes, private solutions and reference answers; outside site. |
| `data/raw/`, `data/prepared/`, `data/synthetic/` | Immutable original sources, derived beginner tables, and future synthetic source releases. See data README. |
| `notebooks/` | Future optional Python companions, outside site until deliberate release. |
| `site/` | Existing generated output, ignored and preserved. |

## Preview and verify

From the project root, create a local Python 3.12 environment and install all project dependencies (one `requirements.txt`, grouped by purpose):

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check_docs.py
python -m mkdocs build --strict --site-dir /tmp/data-analytics-site-check
python -m mkdocs serve
```

Open the local address printed by MkDocs. The temporary build destination protects existing `site/` output. All dependencies (site, data scripts, figures, notebooks) are in requirements.txt; exact environments used are recorded in STATUS.md. Learners do not install anything: they run the lesson notebooks in Google Colab.

The pre-existing Makefile is retained. Its build/serve commands require the environment above; its `run` target references an absent `main.py`. `make convert-all` converts the lesson notebooks in `notebooks/` to `docs/lectures/`; run `python scripts/run_notebooks.py --check-data` first so they carry fresh outputs. `make deploy` publishes externally and is not a verification command. No site was published this session.

## Work conventions

All assistants read [AGENTS.md](AGENTS.md), then current context, status, tasks and handoff. [CLAUDE.md](CLAUDE.md) directs Claude to the same shared instructions and the takeover brief. Preserve user work and update state files at each substantial session. The user selected existing data strategy plus Tableau catalog datasets, including sports/technology/government and other suitable practice topics. Four files are inspected and the first retail contract and prepared CSV exist for local development; other case contracts and source-derived release permissions remain to resolve. The connected simulation, its date/currency conventions and detailed assessment policy remain recommendations.
