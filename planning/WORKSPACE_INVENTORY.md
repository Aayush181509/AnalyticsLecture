# Initial workspace inventory

Inspected 2026-10-12 at `/Users/aayush/Documents/Kings/Data/` before edits.

| Existing item | Finding | Treatment |
|---|---|---|
| `.git/` | Git repository; latest commit `5784497 Slight modification` | Preserved; no commit/deploy requested. |
| `docs/index.md` | Tracked finance/Python/ICAN starter; Tableau row incorrectly listed loops/tax calculator | Exact original copied to `planning/LEGACY_HOME.md`; learner home adapted to current five-domain brief. |
| `mkdocs.yml` | Tracked, single home nav, Read the Docs theme with unused Material-style options, pymdownx extensions | Retain theme, site name and copyright; make docs boundary/navigation explicit and simplify theme configuration. |
| `Makefile` | Pre-existing untracked file; build/serve/deploy and notebook conversion targets; run references absent main.py | Preserve byte-for-byte. README gives supported direct commands; deployment/run not used. |
| `.gitignore` | Pre-existing untracked file; ignores site/ and several editor/temp files | Preserve existing lines; add local environment/cache ignore patterns only. |
| `docs/lectures/`, `notebooks/` | Empty directories | Retained; notebooks gain usage README, future lecture pages may use new lesson directory. |
| `site/` | Generated site assets already present, ignored by Git | Preserved. Verification builds go to temporary directory rather than overwrite this output. |
| Planning/data/instructor/shared agent guidance | Absent | Add requested lightweight foundation. |

## Instructions and tool discovery

Checked AGENTS.md at filesystem root and each ancestor through this workspace; none existed. Recursive project/parent search found no AGENTS.md. No project-specific instructions were available before shared guidance was added.

Initial `git status --short`: only `?? .gitignore` and `?? Makefile`; tracked source was clean. Python 3 was available at `/usr/bin/python3`; no `mkdocs` command on PATH and no MkDocs/pymdown packages in that interpreter. `uv` was available. Verification environment setup and outcome are recorded in STATUS.md.

No datasets, licenses, workbooks, screenshots, lesson notebooks, or numerical answer keys existed. No external data was adopted during planning.
