# Documentation architecture

## Current foundation navigation

`mkdocs.yml` builds only docs/ with the Read the Docs theme (user preference, DEC-036) plus `docs/stylesheets/readability.css`: 820px content width, 16px/1.75 body text, spaced headings, section rules, wrapping padded tables and roomier admonitions (DEC-034). Current pages: home; course roadmap/setup/workflow; business-case preview; reusable learner lesson template. These pages are foundation material, clearly labeled where provisional. No empty lesson pages imply completed production.

Internal planning and instructor answers are physically outside docs/. Hiding an answer from nav would not remove it from a MkDocs build. No solution or internal-state links belong in learner pages. Likewise, avoid source-repository links that inadvertently expose private answer keys if the repository is later made public.

## Proposed released navigation (future, not yet configured)

1. Start here: welcome, setup, workflow, portfolio guide, glossary.
2. Foundations: S1 orientation, S2 retail data understanding/preparation.
3. Retail: S3 metrics (pilot), S4 trends/returns/dashboard; reviewed data dictionary/download.
4. Departmental cases: S5 finance, S6 operations, S7 marketing, S8 HR; each brief, dictionary, tasks and checks.
5. Synthesis and project: S9 evidence register, S10 build, S11 critique, S12 executive briefing.
6. Reference: metric glossary, Tableau recovery guide, validation checklist, optional Python connections.

Add actual pages/navigation only after their dependency tasks pass. Source candidate slugs and private artifact conventions are in CASE_STUDIES and PILOT_LESSON. The lesson-template provides learner headings; no solutions section is included. Instructor assets use corresponding slugs outside docs/.

## Release boundaries

Dataset dictionaries originate in data contracts; learner copies must match a frozen release. Raw data is never overwritten. Review synthetic/public downloadable CSVs and notebook outputs before deliberately copying to a learner assets directory. Copying an entire data/instructor/planning tree into docs/ is prohibited by shared instructions.

Learner page style (DEC-034): open with a one-sentence `<p class="lead">` summary; separate sections with `---`; keep paragraphs to two or three sentences; use numbered steps for procedures, tables or `###` subsections for comparisons, bold-led bullet lists for overviews, and admonitions styled by the theme: `note` (status), `warning` (safety), `tip`/`hint` (help, checkpoints). Avoid Material-only syntax (content tabs, grid cards, icons). Enabled extensions: admonition, details, attr_list, md_in_html, tables, toc permalinks, highlight/superfences. No extra plugins. Manual visual QA is still required when detailed lessons, tables and screenshots are added.

## Verification

Run the lightweight local link/boundary checker and strict temporary MkDocs build from AGENTS.md. Check generated navigation, code blocks and tables; inspect generated files for internal-source leakage. Links to external resources are reference links, not an automated promise that an installation or Tableau behavior was tested. Official MkDocs [configuration](https://www.mkdocs.org/user-guide/configuration/) documents the docs_dir/nav behavior (checked 2026-10-12).

## Hybrid-source update — 2026-10-12

DATA_CATALOG.md records catalog candidates and audit status. Extend future learner navigation with reviewed source-specific transfer exercises (sports, technology, government, other topics) when actual materials exist. Do not add empty dataset download or lesson links now. Keep external-source attribution/terms and native units/dates with each released file; synthetic simulation conventions apply only to its own records. Direct linking and redistributing a data file are distinct release choices and must be documented per source.
