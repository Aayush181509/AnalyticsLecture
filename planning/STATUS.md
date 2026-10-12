# Project status

Updated: 2026-10-12 (Asia/Kathmandu). **Phase: foundation, source audit, D01 retail contract and D02 preparation complete. D03 numerical validation passed; Tableau worksheet checks remain open. Full lesson production has not started.**



## User-authorized Git checkpoint — 2026-10-12

The user requested a local commit of the changes made for this course. This checkpoint records course planning/learner previews, shared guidance/Claude handoff, audited source snapshots and metadata, preparation/validation scripts and private development references. Existing .gitignore lines are retained with our environment/cache additions. Unrelated Makefile, separate fetch script, duplicate source layouts/extra datasets and graphify-out/ remain unstaged and untouched. No push or deployment is requested or performed. Use `git log -1` for the resulting commit identity; historical sections below describe the earlier uncommitted development state. Production statuses and outstanding Tableau checks are unchanged. Pre-commit documentation and numerical validation passed. Staged whitespace inspection reports original CRLF endings in Mobile OS CSV and an existing final blank line in the hash-recorded private hand-check Markdown. Preserve those exact bytes; the staged check excluding these two known artifacts passes. All staged blobs were compared with workspace bytes.

## Latest development step and Claude takeover — 2026-10-12

The user requests Claude takeover after this work. [CLAUDE_TAKEOVER.md](CLAUDE_TAKEOVER.md) is the concrete continuation brief; CLAUDE.md/README/HANDOFF point to it. Earlier sections below preserve historical evidence and their then-current limitations; this section supersedes their next-action statements.

- **D02 DONE for local development.** `scripts/prepare_retail.py` runs frozen-contract preflight, derives whole-source customer conflicts before date scope, and writes immutable CSV/manifest/report/private exceptions. CSV: 6,815 lines, 3,388 orders, 22 fields, 36 months; customer-eligible 6,811 lines/3,387 orders. All 149,930 typed values matched. Thirty-four lines shipping beyond the Order Date window remain. Repeat generation preserved bytes and modification times.
- **D03 numerical slice PASS; task IN PROGRESS for Tableau.** `scripts/validate_retail.py` independently reads raw through pandas and saved CSV through DictReader/Decimal, without preparation/checker imports. Every typed value matched; seven frozen hashes, source/preparation/output identities, private controls, two-line source hand arithmetic, population bridges, group totals, weighted ratios/return denominators/category overlap and calendar growth checks passed. Two private reports were repeated byte-identically; lead reran successfully. Ratios expose exact numerators/denominators and use Decimal precision60 for repeating expansions.
- Private references/evidence: `instructor/solutions/superstore/retail-v1/{preparation_exceptions,reference_answers,numerical_validation}.json`. The numerical report explicitly says PASS_NUMERICAL_ONLY, Tableau=false, publication=false. These are not classroom-ready answer packs. Prepared metadata also has diagnostic controls/private paths; do not distribute the directory wholesale.
- **Tableau import only.** Installed native Tableau Public loaded the exact CSV via Text file and displayed 22 fields/6,815 rows. Observed Order ID as string, dates as dates, flags/interval as numbers. Worksheet navigation failed with native app-control `noWindowsAvailable` errors; refreshing the handle still showed the source, then the tool reported an application change. No worksheet KPI/filter/grand-total/empty/zero-case, installed-version or save/reopen check completed. No reference workbook saved; no public upload. Welcome-page update text is not installed-version evidence.
- Case/data worker owned preparation; pilot/reviewer owned independent numerical validator/reports; curriculum reviewer read-only accepted D02 and independently checked identities/schema/counts/coverage. Lead reviewed integration, reran the numerical validator and attempted the local app check. No blocking preparation defects found. Immutability refusal was code-reviewed, not tested by corrupting the output.

Actual data commands in the existing audited environment:

```bash
PYTHONPATH=/tmp/kings-source-audit-libs /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/prepare_retail.py
PYTHONPATH=/tmp/kings-source-audit-libs /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/validate_retail.py
```

Both PASS. Preparation invokes the read-only frozen checker first. Runtime: Python3.12.14/xlrd2.0.2, independent validator pandas2.2.3, Decimal precision60. The persistent `.venv-data` setup recipe is documented but not separately installation-tested. Temporary dependencies may expire; differing runtime metadata must not be resolved by overwriting immutable versions.

| Identity | SHA-256 |
|---|---|
| CSV | `434ba08abf665b617294b188e38c0d0b8a86d0b3386d41eff8a42c15bc708de2` |
| Preparation manifest | `1b662f9ec2628de3244d26c7f9152db56a38350a4eb9fb1ad9d9a46b999cc844` |
| Independent reference answers | `96c35dcf8449386fae5f4978bc86a23966594d1ddda51feb4d93eee046d1c929` |
| Numerical validation report | `53e8be7c59d63fbe15f4d9c24291dfbb9ccbe909c68fb8ba2d70632206dceec0` |

**Next concrete task:** close D03's remaining local Tableau comparisons with recorded app version and evidence, then L01/L02 after relevant R01 defaults. Keep S3 source-backed Segment metrics distinct from the retained synthetic pilot. Full lessons, synthetic generators, notebooks, learner-device/classroom/timing/accessibility/visual checks and permitted learner/public delivery remain future work. No deployment/commit/public upload performed. Raw sources, frozen inputs, existing site/ and unowned extra work preserved.

Final integration verification: `python3 scripts/check_docs.py` PASS (six learner pages); `/tmp/kings-data-docs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/data-analytics-site-check` PASS without warnings; local inline-link/whitespace scan PASS across41 selected project Markdown files. Python syntax/retail JSON parse, all seven frozen hashes, four original byte/hash identities and exact LEGACY_HOME bytes PASS. Twelve120-minute budgets,19h essential practice and100% proposed rubric rechecked. `git diff --check` PASS; status inspected and all work left uncommitted. Remote URLs/anchors/reference-link syntax, browser layout, Tableau worksheet calculations and teaching/device trials are outside these checks.

## Foundation completion (before source audit)

- Inspected repository/instructions/tooling, recorded inventory and preserved original home exactly in LEGACY_HOME.md. Existing Makefile and generated site/ preserved; existing ignore patterns retained with local environment/cache additions.
- Captured four user answers:12×2h live + practice; basic spreadsheets, no Tableau/Python; Tableau Public synthetic/public data; practical portfolio/executive briefing.
- Integrated eight observable outcomes, exact 120-minute class budgets, meaningful five-domain portfolio, recommended rubric and alternative pacing. Essential practice is recommended 19h (43h including class); expanded route about 25h practice is optional and unverified.
- Created all five case briefs with activity/validation/solution specifications, planned source/prepared schemas and explicit metric contracts. No external data adopted.
- Detailed S3 retail pilot, learner lesson template, internal instructor structure and future MkDocs navigation. Growth/returns reserved explicitly for S4.
- Created README, shared AGENTS, concise CLAUDE entry, five reusable role briefs, prioritized dependencies, decisions and handoff.
- Three bounded workers executed curriculum/assessment, case/data and pilot/template tasks. Pilot worker subsequently reviewed other authors' designs; lead independently integrated and reviewed all outputs. Role documents do not imply additional agents ran.
- Resolved analytic/integration findings: finance comparable totals, shipment cutoff/date rules, HR historical boundaries, cumulative refunds/cost recovery, three-domain capstone consistency, single-campaign synthetic attribution, S3 scope and practice load. Review report records findings and remaining release gates.

## Verification actually performed

| Check | Outcome / limits |
|---|---|
| `python3 scripts/check_docs.py` | PASS:6 learner Markdown pages; inline local links/nav targets/docs-only boundary. Remote URLs, fragments and reference-link syntax not exhaustively checked. |
| `/tmp/kings-data-docs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/data-analytics-site-check` | PASS with no warnings; temporary output protects existing site/. |
| Python design assertions |12 sessions; each120min;1,440 total contact min =24h; essential practice19h; rubric weights total100%. Reviewer also checked synthetic hand-reasoned HR date-boundary cases; these are formula sanity checks, not real-dataset validation. |
| Generated HTML structural inspection |8 HTML files with titles; course pages have H1s; no planning/instructor/notebook source paths copied. This is not browser visual QA. |
| Original-home byte comparison |LEGACY_HOME.md exactly equals pre-edit `git show HEAD:docs/index.md`; SHA256 `93f6983584e68e962ff3b88f10b5c945dae6c909b773656de6fa9f444d9b0eee`. |
| `git diff --check`; new Markdown whitespace scan; `git status --short` |Tracked diff clean; new Markdown checked separately; changes left uncommitted for review. |
| Official source checks |Tableau Public saving/FAQ and MkDocs configuration consulted; links in PROJECT_CONTEXT/setup/DOCUMENTATION_PLAN. No external dataset source or license adopted. |
| Browser visual review attempt |In-app browser unavailable; Chrome rejected local file URL under URL policy. No workaround attempted; browser layout/visual QA remains unverified. |

Documentation test environment: temporary venv using Python 3.9, MkDocs 1.6.1, pymdown-extensions 10.21.3, Markdown 3.9 and PyYAML 6.0.3. `requirements.txt` declares compatible ranges, not a full cross-platform lockfile. Initial restricted network installation failed; approved retry installed dependencies successfully. README gives persistent local setup instructions; temporary environment may not survive future sessions.

## Foundation handoff limits (before source audit)

No blocker remains to the requested planning handoff. Production needs selected-source field dictionaries/contracts and exact frozen releases before answers or lessons can be verified. No datasets, notebooks, reference workbooks, screenshots, calculations in Tableau, teaching times or graded submissions are verified or available. No public deployment or Git commit was performed.

Still unresolved: class size and final briefing logistics, delivery/cadence, access/accommodations, practice capacity, submission channel/deadlines, assessment/team policy, storyline/currency/date adoption and rights/license choice. R01 tracks these; D01 can independently turn current proposals into reviewable field dictionaries and hand fixtures. Publication requires a reviewed release and explicit instruction.

## Earlier hybrid dataset update — 2026-10-12 (before source audit)

The user confirmed the established data strategy **plus** Tableau catalog datasets, with sports, technology, government and other suitable topics. The rendered catalog was inspected before the user interruption; Business/Sports/Technology/Government and additional entries were visible. Text-only web access returned a JavaScript shell. A later browser handle was no longer available after interruption; no file inspection or download was performed.

Added DATA_CATALOG.md with concrete candidates, core-domain gaps, proposed transfer exercises and audit workflow. Updated source strategy/case plans, curriculum, assessment, pilot applicability, learner previews, context, shared/role guidance and backlog. The connected synthetic plan remains useful alongside catalog files; its NPR2025 conventions no longer apply to external sources. Five core cases and required synthetic employee records remain; added topics use existing practice or optional extensions. No additional required class hours.

Individual downloads/schemas/rights/answer totals remain unverified; catalog sourcing is confirmed, individual files are candidates. Existing dependency file is requirements.txt; README/current state adapted without changing its contents. Foundation checks from the earlier session remain historical evidence; current documentation checks are recorded after integration below.

## Earlier next step after source audit (now completed for retail)

D01: freeze the inspected Superstore field dictionary and source-specific metric contract. Resolve source currency/definition labels, proposed2023–2025 scope, Segment mapping and customer-conflict exclusions. D02/D03 prepare and independently validate an exact retail release, with synthetic supplements/controlled cases where inputs are absent. Only then author and rehearse the pilot. SOURCE_AUDIT.md records recommended sports/technology/government roles. See TASKS and HANDOFF.

## Earlier hybrid-update verification

Re-ran `python3 scripts/check_docs.py` (six learner pages), strict temporary MkDocs build (no warnings), `git diff --check`, and a local inline-link/whitespace scan across32 Markdown files. Rechecked all twelve120-minute budgets and19h essential practice. README now points to the existing requirements.txt. Core/extension case and hybrid-source wording were reviewed by lead; no dataset downloads/answers or Tableau execution are implied. No deployment or commit performed.

## Current source audit — 2026-10-12

- Followed four download links observed in the rendered catalog: Superstore, World Cup Results, Mobile OS Usage, US Construction. All returned HTTP200, passed signatures and were preserved unchanged at the paths in `data/metadata/catalog-audit-2026-10-12/source_manifest.json`, with bytes, SHA-256 and retrieval evidence. Publication remains false.
- Added reproducible acquisition/integrity and offline profiling scripts, separate requirements-data.txt and data commands. Profiles capture every real column/type/null/cardinality, keys/date coverage and quality findings. Numerical inspection controls stay in instructor/source-audit, outside the learner site.
- SOURCE_AUDIT.md recommends supported uses and records catalog/file discrepancies: Superstore is US/Canada2023–2026, with currency/Profit meaning unresolved and two customer/order conflicts; sports has16exact duplicate matches; Mobile OS has1,772missing dates; government mixes overlapping amounts/annual rates/percentage/error series and has incomplete2016.
- SOURCE_RIGHTS.md records primary-source provider research. Direct learning-download guidance, provider licenses/policies, mirror provenance and bundling/public-upload permissions are distinguished. No blanket rights clearance or course license assigned.
- Reused case/data worker for rights evidence and case/strategy integration, reviewer for independent numerical/source audit. Exclusive file ownership observed; lead integrated other state, scripts and source-audit design.
- Separate source-fetch script, duplicate raw layouts and two additional files appeared during this work and were preserved unchanged. They are outside this four-file manifest and were not executed/audited by this run. Do not infer provenance or adoption from their presence.

### Checks actually performed for source audit

`python3 scripts/acquire_catalog_samples.py` acquired the files with normal TLS/curl under an approved network run; subsequent invocation verifies only the manifest hashes. Offline profiling command used:

```bash
PYTHONPATH=/tmp/kings-source-audit-libs /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/profile_catalog_samples.py
```

PASS: four byte/hash checks, retail line/lookup keys and date chronology, sports deduplication and all20tournament match/goal reconciliations, dated OS subset key, government nonnullable composite key and177unique nonmissing monthly observations. Schema/profile outputs generated. Environment: Python3.12.14, pandas2.2.3, openpyxl3.1.5, xlrd2.0.2; xlrd installed to temporary directory after approved pip access. Raw workbook values were read without editing or recalculating formulas. Local `.venv-data` installation recipe is documented but not separately executed.

Independent review uses direct xlrd iteration/Decimal rather than the profiler's pandas retail path, direct openpyxl sports rows, and CSV/Decimal government/technology checks. See SOURCE_AUDIT_REVIEW.md for exact controls, a hand-check fixture and limits. These validate the snapshot internally; they are not upstream truth checks or released lesson answers.

Remaining production/release conditions: source-specific dictionaries/contracts and prepared versions; source currency/accounting definitions or supported teaching labels; historic geography/provenance; permitted delivery; synthetic source generation; exact lesson answers; Tableau/device/classroom/visual QA. No prepared learner dataset, notebook, source-specific lesson, Tableau workbook or public upload was produced. No commit/deployment performed. Existing site/ and uncommitted work preserved.

Final integration checks: `python3 scripts/check_docs.py` PASS (six learner pages); `/tmp/kings-data-docs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/data-analytics-site-check` PASS without warnings; local inline-link/whitespace scan PASS across 36 Markdown files; all scripts pass Python syntax compilation without execution; legacy-home bytes still exactly match HEAD's original home. `git diff --check` PASS; status inspected. The current docs build has no new learner lesson/data output. New unowned `graphify-out/` appeared at final status inspection and was left untouched, as were the separate source files/script. Remote links/anchors/reference syntax and visual layout are outside the final local-link scan.

## Earlier D01 retail development freeze — 2026-10-12

- Created `data/metadata/superstore/retail-v1/`: full field dictionary (25 raw fields/22 planned prepared fields), 13 metric definitions, machine settings and reproducible preparation specification. Independent review accepted the design; freeze.json records seven specification/review/fixture/checker SHA-256 values plus raw-source identity. This freezes the first retail local-development variant only, not all five-domain contracts or a learner/public release.
- Fixed date scope to 2023–2025 Order Date, keeping boundary-crossing Ship Dates. Chose source monetary-unit labels without currency/accounting inference; Segment instead of Channel; reported Sales/Profit rather than synthetic gross-profit/refund semantics. Whole-source customer conflicts remain flagged in primary totals and are excluded consistently only in customer work. Returns means listed/not listed, not proven no-return or event timing.
- Added private, explicitly synthetic JSON hand fixtures and a read-only retail contract checker. Checks cover order/line grain, ratios of totals, empty/zero denominators, overlapping category orders, repeated return flags, customer eligibility, date boundaries, calendar MoM/YoY and covered-month/no-selected-lines versus unavailable periods. No synthetic source generator or prepared dataset was created.
- Case/data worker authored only the dictionary; reviewer authored only RETAIL_CONTRACT_REVIEW.md and independently checked arithmetic/populations/direct source values without checker helpers. Lead accepted the review, added the covered-month refinement and froze the version. No open analytical review defects remain for local development.
- Aligned curriculum, assessment and learner previews to the first source-backed Segment snapshot; the detailed Meridian/channel pilot remains a labeled synthetic reference. Five domains, twelve classes and practice budgets are preserved. Shared guidance, data commands, decisions, tasks and handoff now point to D02.

Actual D01 command, read-only and repeated after freeze:

```bash
PYTHONPATH=/tmp/kings-source-audit-libs /Users/aayush/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_retail_contract.py
```

Pre-freeze checks passed: exact original hash/schema/keys, 6,815 scoped lines/3,388 orders, 36 months, customer-eligible 6,811 lines/3,387 orders and excluded four-line/one-order population bridge; monetary/quantity controls reconciled without row rounding. Independent review additionally confirmed 34 retained lines ship after the scope end. Source was not edited and formulas were not recalculated. Tableau expressions were checked against official aggregate/filter documentation, not run in the app.

**D01 handoff at that time (now superseded):** D02 implements preparation_spec.md and writes a local immutable 22-column source projection, typed re-read validation, output manifest and private exceptions/reconciliation. Then D03 independently validates prepared-version answers and actual Tableau behavior. D02R separately covers synthetic refund/cost material; D04–D07/X01 freeze their own case contracts. Stronger currency/accounting claims, public delivery rights, full lessons, device/classroom/accessibility/visual QA and teaching timings remain unverified. Existing raw files, site/, extra source work and graphify-out/ are preserved; no publishing or commit.

Final D01 checks: post-freeze retail checker PASS (all seven frozen hashes, synthetic edge cases and exact source/bridge checks); `python3 scripts/check_docs.py` PASS (six learner pages); strict temporary MkDocs build PASS with no warnings; local inline-link/whitespace scan PASS across 40 Markdown files; script syntax and contract JSON parse PASS; original-home bytes unchanged; all twelve classes remain120minutes and essential practice19h. `git diff --check` and status inspected at handoff. Remote links/reference syntax/anchors, visual rendering and Tableau are outside these checks. The new specifications/fixtures remain outside docs/; learner previews contain no internal links or answer files.
