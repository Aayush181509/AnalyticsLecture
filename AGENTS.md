# Shared project instructions

Read `planning/PROJECT_CONTEXT.md`, `planning/STATUS.md`, `planning/TASKS.md`, and `planning/HANDOFF.md` before substantive work. This file is the shared authority for all assistants; tool-specific entry files only point here.

## Scope and ownership

- This is a practical Data Analytics course for working professionals. Tableau is essential; Python/pandas companions start optional. Cover retail, finance, operations, marketing, and HR meaningfully. Use the confirmed hybrid data approach: existing synthetic strategy plus Tableau sample-data catalog sources, with sports/technology/government and other suitable choice exercises.
- The current phase is planning and foundation, not full lesson production. Complete production tasks in dependency order.
- Preserve existing work and uncommitted user changes. Do not deploy, publish, commit, or replace source datasets as an incidental verification step.
- User authorizes bounded subagents. Lead integrates and reviews. Give every role exclusive file ownership; reusable briefs are in `planning/agents/`.
- Mark confirmed requirements, recommendations, assumptions, unresolved questions, and verification evidence explicitly. Do not turn a recommendation into a user decision.

## Teaching and analytical standards

- Start with a business decision, then follow question → understanding → preparation → analysis → validation → visualization → recommendation.
- Use demonstration → guided practice → independent work → challenge. Make outcomes observable and map them to evidence.
- Every case needs a stakeholder brief, dictionary, metric contract, worked example, exercises, debugging, recommendation challenge, optional Python connection, validation, and separate instructor solutions.
- Specify grain, keys, units, date window, filters, denominators, zero-denominator behavior, and missing-value treatment. Distinguish weighted rates from means of rates, and association from causation.
- Label fictional/synthetic records accurately; preserve external sources' real contexts, units, currencies and dates. Do not label all catalog data synthetic or force heterogeneous files into one company. Preserve raw sources; document derivations, version, checksums, provenance, rights, and exact-dataset answer checks. Verify availability and licensing before adopting external data.
- Never claim Tableau workbooks, screenshots, calculations, data answers, or builds were verified without checking them. Log actual commands and limits.

## Publication boundary

- Only `docs/` is learner-facing MkDocs source. Keep planning in `planning/`, notes/answers in `instructor/`, datasets in `data/`, and companions in `notebooks/`.
- Never link learner pages to instructor answers or internal planning. Publish only reviewed synthetic/public data; Tableau Public publication is public. Public profile hiding is not a privacy control.
- Keep infrastructure small. Retain the established Read the Docs theme unless an explicit need justifies changing it.

## Verification and handoff

- Documentation: run `python3 scripts/check_docs.py` after it exists, then `python3 -m mkdocs build --strict --site-dir /tmp/data-analytics-site-check` in the documented environment. Do not use deploy as a check.
- Catalog audit: run `python3 scripts/acquire_catalog_samples.py` to verify the existing manifest hashes (no network when the manifest exists), then `scripts/profile_catalog_samples.py` in the data environment documented in `data/README.md`. These inspect sources only; they do not validate prepared releases, recalculate source formulas or test Tableau. Follow the four exact manifest paths; preserve unrelated extra source work.
- Retail contract: `scripts/check_retail_contract.py` in that same data environment verifies the exact source and private synthetic hand fixtures against `data/metadata/superstore/retail-v1/`. A development contract freeze does not create a prepared release or grant public redistribution; preserve the recorded review/version boundary.
- Retail preparation: `scripts/prepare_retail.py` uses that data environment, checks the frozen contract first, and creates or byte-verifies the immutable local CSV/manifest/report/private exceptions. Never overwrite a differing output or edit the seven frozen inputs. Exact-version independent checks run through `scripts/validate_retail.py`; numerical evidence and private answers remain in instructor/. A local Tableau import is distinct from worksheet/filter/grand-total validation; see current handoff.
- Before generators exist, schema and metric plans are design-reviewed only. Later run generator/validation commands documented in `data/README.md` against the released version; compare exact numerical answers before distributing solutions.
- Inspect `git diff --check` and `git status --short`. Do not discard unrelated changes. Review learner output and publication boundaries.
- End each substantial session by updating `planning/TASKS.md`, `planning/DECISIONS.md`, `planning/STATUS.md`, and `planning/HANDOFF.md`: changes, evidence, uncertainty, and next concrete task.
