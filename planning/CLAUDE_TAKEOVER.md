# Claude takeover brief

Prepared 2026-10-12 (Asia/Kathmandu) at the user's request. Workspace: `/Users/aayush/Documents/Kings/Data`.

**Update 2026-10-13:** the teaching path is now Python-first in Google Colab (DEC-041); see HANDOFF and AGENTS "Python lessons" before using the Tableau-focused next actions below.

**Resume the existing course project. Foundation, four-source inspection, the first retail contract and D02 preparation are complete. Independent numerical validation passed; D03 remains in progress for Tableau worksheet checks. Full course production is still a sequenced backlog.** This brief is a snapshot; AGENTS.md is the shared authority, and STATUS/TASKS record later changes.

## Start in this order

1. Read [AGENTS.md](../AGENTS.md), [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md), [STATUS.md](STATUS.md), [TASKS.md](TASKS.md) and [HANDOFF.md](HANDOFF.md).
2. Read [CURRICULUM.md](CURRICULUM.md), [ASSESSMENT.md](ASSESSMENT.md) and [CASE_STUDIES.md](CASE_STUDIES.md) for the teaching sequence. [PILOT_LESSON.md](PILOT_LESSON.md) is a detailed synthetic reference outline, not a source-backed lesson ready to teach.
3. Read the first retail [metric contract](../data/metadata/superstore/retail-v1/metric_contract.md), [dictionary](../data/metadata/superstore/retail-v1/dictionary.md), [settings](../data/metadata/superstore/retail-v1/contract.json), [preparation specification](../data/metadata/superstore/retail-v1/preparation_spec.md) and [freeze manifest](../data/metadata/superstore/retail-v1/freeze.json).
4. Read [SOURCE_AUDIT.md](SOURCE_AUDIT.md), [SOURCE_RIGHTS.md](SOURCE_RIGHTS.md) and [SOURCE_AUDIT_REVIEW.md](SOURCE_AUDIT_REVIEW.md) before adopting another source or changing delivery.

Do not repeat the four answered setup questions, restart curriculum planning or download the same sources again. The user's latest instruction is to let Claude take over after this development step.

## Confirmed scope and working defaults

| Confirmed by user | Consequence |
|---|---|
| Twelve two-hour live classes plus practice | Preserve 24 contact hours. |
| Basic spreadsheets; no Python or Tableau assumed | Tableau onboarding and beginner recovery belong in S1–S2. |
| Tableau Public with synthetic/public data | Tableau is essential; public upload is a distinct action. |
| Practical portfolio and executive briefing | Build observable evidence and separate instructor answers. |
| Retail/e-commerce, finance, operations, marketing and HR | All five domains remain meaningful; employee-level HR is synthetic. |
| Existing data strategy plus Tableau catalog, including broader subjects | Use suitable sports/technology/government choices within practice or optional extensions. |
| MkDocs, section-by-section development, bounded agents | Keep infrastructure small; delegate with exclusive ownership when tools support it. |

Recommendations remain recommendations: optional-first Python, 19 hours essential practice, all-five-domain portfolio with at least three domains synthesized in the briefing, proposed feedback rubric, and optional fictional Meridian Commerce/NPR/calendar-2025 simulation. None establishes a real business context, grading policy or schedule. R01 tracks class size/delivery/cadence, devices/accessibility, practice capacity, submission/deadlines and assessment/team decisions. These questions do not block offline source verification; resolve relevant ones before classroom production or distribution.

## What exists now

| Artifact | State and purpose |
|---|---|
| `docs/` and `mkdocs.yml` | Six learner preview/template pages; Read the Docs theme with readability stylesheet (DEC-034, DEC-036). Only docs/ enters the site. |
| `planning/` | Curriculum, five case designs, assessment, synthetic pilot, source evidence, decisions and backlog. |
| `data/metadata/catalog-audit-2026-10-12/` | Four-file acquisition manifest and schema/quality profiles. |
| `data/metadata/superstore/retail-v1/` | Reviewed D01 local-development specification. Seven frozen input hashes are authoritative. |
| `scripts/prepare_retail.py` | D02 offline preparation; frozen-checker preflight, staged typed comparison, immutable output checks. |
| `data/prepared/superstore/retail-v1/order_lines.csv` | Prepared source projection for local development; not yet a permitted learner/public package. |
| `data/prepared/superstore/retail-v1/manifest.json` | Source, contract, script and output identities plus runtime/schema/scope. |
| `data/prepared/superstore/retail-v1/preparation_report.json` | Row partitions, exceptions, coverage and reconciliation evidence. Internal; includes diagnostic counts/private path. |
| `instructor/solutions/superstore/retail-v1/preparation_exceptions.json` | Private exact population bridges and original conflict records. |
| `scripts/validate_retail.py` | Independent pandas source read versus typed saved CSV; hashes, populations, arithmetic and calendar checks. |
| `instructor/solutions/superstore/retail-v1/reference_answers.json` | Private exact-version whole/eligible/excluded, Segment/Region/Category/month KPIs, growth, dispatch and debugging references. |
| `instructor/solutions/superstore/retail-v1/numerical_validation.json` | PASS_NUMERICAL_ONLY; input/script/answer hashes, runtime, check counts and explicit app/release limits. |

Do not distribute the entire prepared directory: metadata includes diagnostic controls and internal references. Deliberate learner packaging must select reviewed files. No full synthetic source generator, optional notebook, teachable source-specific lesson, saved reference Tableau workbook or completed classroom trial exists.

## Exact retail version to continue

| Property | Frozen/prepared value |
|---|---|
| Contract | `superstore-retail-v1` |
| Original | `data/raw/eu-superstore/2026-10-12/sample_-_superstore.xls` |
| Original SHA-256 | `5045ed4fec49cae2cc0dfc5ab0d204ba09efa767fe00c996822499e8cc42fbbd` |
| CSV SHA-256 | `434ba08abf665b617294b188e38c0d0b8a86d0b3386d41eff8a42c15bc708de2` |
| CSV bytes/schema | 1,511,171 bytes; 22 fields in contract order; UTF-8/LF; ISO dates; source numbers unrounded |
| Grain/key | One original order line; unique `row_id`; repeated `order_id` is expected |
| Population | `2023-01-01 <= order_date < 2026-01-01`; observed 2023-01-03 through 2025-12-31 |
| Main scope | 6,815 lines; 3,388 orders; 36 calendar months |
| Customer-eligible scope | 6,811 lines; 3,387 orders; four lines/one order excluded consistently from customer work |
| Ship boundary | 34 scoped lines shipping in 2026 retained |
| Status | Local development; `publication_approved=false`; preparation metadata makes no Tableau-verification claim |

Analytical rules to preserve:

- Actual source context is a fictitious US/Canada Superstore sample, despite the catalog's EU title. Use **source monetary units**, Segment, reported Sales/Profit and Profit/Sales. Currency/accounting meaning is unknown. Do not relabel it Meridian/NPR, infer gross margin or reapply Discount to Sales.
- Count distinct orders. AOV and profit ratios divide matching totals. Segment/Region/month order counts reconcile; Category counts overlap (category counts sum to 4,779 versus 3,388 orders). Category AOV means selected-line Sales per participating order.
- Detect both customer conflicts on all raw Orders before date filtering: `CA-2025-121465` and `CA-2026-130494`. Main KPIs retain the scoped conflict lines. Customer analysis applies eligible=1 to every accompanying metric and discloses exclusions.
- Returned flag means membership in the supplied Returns list. Absence means not listed; it is not proof of no return. There are no return-event dates, amounts, quantities or refund/cost recovery facts.
- Monthly growth uses exact calendar comparators and coverage, not simply the previous visible mark. Zero/unavailable prior denominators yield null. A covered group month with no selected lines differs from an unavailable period. Dispatch summaries use one observation per order.
- Preserve exact canonical Decimal row values. Engine aggregate tolerances: 0.000001 source monetary units; 0.000000001 for fractional ratios. Counts/dates/IDs/flags are exact. Display-only checks are weaker and must be labeled separately.

The seven D01 inputs are frozen. Their phrases such as “No prepared CSV exists yet” describe the freeze-time state. **Do not edit them to update current status**: use this brief and STATUS. Semantic changes need a new version/review. Existing D02 outputs must byte-match or stop; never delete/overwrite them to make a rerun pass.

## Verification completed and limits

D02 generated the four artifacts and compared every one of 149,930 typed CSV values with its canonical source mapping. A repeat run preserved bytes and modification times. A separate read-only reviewer accepted local preparation after checking all recorded hashes, schema, order counts, row keys, coverage, flags and the unchanged repeat run. The refusal of changed existing bytes was inspected in code; no deliberately corrupted production output was used as a test.

D03 numerical results: **PASS_NUMERICAL_ONLY**, independently computed without importing preparation/checker helpers. All 149,930 saved typed values match a separate pandas source read; seven frozen hashes and recorded source/preparation/output identities match. Private controls, two-line source hand arithmetic, all population bridges, weighted ratios, distinct return-list denominators, category overlap and 36-month calendar comparisons passed. The validator and its private reports were repeated byte-identically; lead reran the validator successfully. Reference-answer SHA-256: `96c35dcf8449386fae5f4978bc86a23966594d1ddda51feb4d93eee046d1c929`; numerical-report SHA-256: `53e8be7c59d63fbe15f4d9c24291dfbb9ccbe909c68fb8ba2d70632206dceec0`. Answers expose exact numerators/denominators; nonterminating ratios use Decimal precision 60. Numerical validation does not verify Tableau expressions or teaching feasibility.

Tableau attempt on 2026-10-12: the installed `/Applications/Tableau Public (Apple silicon).app` opened Book1. The native Text file connector loaded the exact CSV and displayed **22 fields / 6,815 rows**. Order ID was shown as string; Order Date, Ship Date and Order Month as dates; flags/dispatch interval as numbers. This is an import/schema smoke check only. Worksheet navigation encountered native app-control `noWindowsAvailable` errors; a refreshed handle still showed the source, then the tool reported an application change. No worksheet KPI, filter/grand-total, empty/zero-case, local save/reopen, version or learner-device check was completed. No reference workbook was saved and no public upload was attempted. Do not turn the welcome page's advertised update version into an installed-version claim.

Final integration passed: six-page learner boundary/link check, strict temporary MkDocs build without warnings, local inline-link/whitespace scan across 41 selected project Markdown files, script syntax/retail JSON parse, seven frozen hashes, four original byte/hash identities, exact legacy-home preservation, twelve 120-minute budgets, 19 hours practice and 100% proposed rubric. `git diff --check` passed; status was inspected. Exact commands/results are in STATUS. Earlier browser visual review was refused for local file URLs; do not work around that policy. Remote URLs/anchors/reference-link syntax remain outside the local scan; a strict MkDocs build is not rendered visual or Tableau QA.

## Commands and environment

Run from the workspace root. Standard data setup recipe (documented, not separately installation-tested):

```bash
python3.12 -m venv .venv-data
.venv-data/bin/python -m pip install -r requirements.txt
.venv-data/bin/python scripts/check_retail_contract.py
.venv-data/bin/python scripts/prepare_retail.py
.venv-data/bin/python scripts/validate_retail.py
```

Actual successful data route in this session uses Python 3.12.14, pandas 2.2.3, openpyxl 3.1.5 and temporary xlrd 2.0.2:

```bash
PYTHONPATH=/tmp/kings-source-audit-libs /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_retail_contract.py
PYTHONPATH=/tmp/kings-source-audit-libs /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/prepare_retail.py
PYTHONPATH=/tmp/kings-source-audit-libs /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/validate_retail.py
```

Temporary dependencies may disappear. Recreate the documented environment if necessary; do not silently change versioned outputs to accommodate dependency drift. No seed is required for this source projection. Full synthetic generators remain future work.

Documentation checks:

```bash
python3 scripts/check_docs.py
/tmp/kings-data-docs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/data-analytics-site-check
git diff --check
git status --short
```

The docs venv used Python 3.9/MkDocs 1.6.1/pymdown-extensions 10.21.3. README has a persistent local setup recipe if the temporary environment is gone. Protect existing site/; do not use `make deploy` as verification. `scripts/acquire_catalog_samples.py` only verifies existing raw hashes when its manifest exists; no repeat download is needed. Profiling is source inspection, not prepared-data or app validation.

## Next actions, in dependency order

1. **Close D03's Tableau gap.** Record the installed version via the app. Open the exact CSV locally, confirm field types, and build actual ordinary-aggregate calculations matching the frozen contract. Compare whole scope, each Segment, one Region, eligible-only scope and one Category with the private numerical references. Check filter behavior, grand totals recomputed from totals, category overlap and empty selections. Test nonempty zero-denominator behavior with clearly separate synthetic fixtures, not edited reference data. Record precision versus display-only evidence explicitly. Save/reopen a local verification workbook if supported; keep instructor solutions outside learner resources. Do not publish to Tableau Public.
2. Resolve the relevant R01 logistics/access defaults without reasking the four answered questions. A single-machine import is not a learner-device readiness survey.
3. **L01:** produce S1–S2 learner setup/preparation and recovery instructions, then rehearse. **L02:** translate the detailed S3 synthetic pilot pacing into the actual Segment/source-metric lesson using this exact CSV. Include worked example, guided and independent practice, line-versus-order debug, recommendation challenge, validation checkpoints and separate instructor solutions.
4. **V01:** run a fresh Tableau comparison plus timed novice/accessibility trial before extending production. S3 is snapshot KPIs. S4 adds calendar growth/qualified return-list work; D02R supplies a separately contracted synthetic refund/cost example.
5. Continue D04–D07 and L04–L07 for finance, operations, marketing and synthetic HR; then synthesis/capstone. X01 transfer choices and N01 optional Python follow their backlog dependencies. Do not expand required contact/practice time casually or join unrelated datasets into one invented company.

Sports recommendation: remove 16 exact duplicate matches before deriving appearances; clean count 836 across 20 tournaments. Technology: 1,772 missing dates; use quality debugging or the explicitly scoped 104-row Dec 2008–Mar 2009 dated subset, without inventing dates. Government: use only US/XXXX/T/et_idx=0/is_adj=0 for 177 nonmissing monthly amounts in million US dollars; do not mix annual rates, percentage/error blocks, overlapping categories or incomplete 2016 totals. These are inspected candidates, not prepared/approved exercises. SOURCE_AUDIT/SOURCE_RIGHTS hold details.

## Preservation and release boundaries

The user subsequently requested a local commit of the course changes. This checkpoint includes the course artifacts described here; use `git log -1` for its identity. Unrelated workspace additions remain untracked. No push, deploy or public upload was performed. Earlier verification records describe the pre-commit state. Only docs/ is learner-facing; instructor/, planning/, data/metadata and local prepared diagnostics remain internal. Source availability does not establish standalone bundling/public-upload rights. Superstore/World Cup permissions and historical mirror provenance retain unresolved conditions; Statcounter/Census provider terms do not automatically settle every mirror's terms. No course license has been selected.

Preserve the initially untracked Makefile/.gitignore, existing generated site/, exact original-home archive in [LEGACY_HOME.md](LEGACY_HOME.md), and all unrelated uncommitted work. In particular preserve `scripts/fetch_catalog_sources.py`, duplicate `retrieved-2026-10-12` raw layouts, Start-up Venture Funding, US Home Sales and graphify-out/. Those extras appeared separately and were not executed/adopted/audited by this four-source workflow. Follow the exact four-path audit manifest.

Reusable roles are in planning/agents/. Completed execution this step: case/data worker implemented D02; pilot/reviewer independently implemented numerical validation; curriculum reviewer checked D02 read-only; lead integrated state and attempted local Tableau import. Role briefs alone do not imply future agents ran. Keep exclusive file ownership if delegating.

## Suggested first prompt to Claude

> Continue this Data Analytics course in `/Users/aayush/Documents/Kings/Data`. Read AGENTS.md, planning/CLAUDE_TAKEOVER.md and the canonical context/status/tasks/handoff. Preserve the frozen retail-v1 inputs and prepared CSV. Verify current artifacts with the documented commands, then complete D03's remaining local Tableau checks and record actual evidence. Continue to L01/L02 in dependency order, keeping source metrics distinct from the synthetic pilot. Preserve existing work and instructor/learner boundaries. Do not publish, deploy or commit unless separately instructed. Update TASKS, DECISIONS, STATUS and HANDOFF after substantive work.
