# Course data workspace

The user selected a hybrid approach: the established synthetic strategy plus [Tableau sample-data catalog](https://public.tableau.com/app/learn/sample-data) sources. Four catalog originals have been acquired and inspected locally. They are audit sources, not learner releases; no source-derived publication is approved. See [source audit](../planning/SOURCE_AUDIT.md), [rights evidence](../planning/SOURCE_RIGHTS.md) and [data strategy](../planning/DATA_STRATEGY.md).

- `raw/`: untouched external acquisitions. Audited originals are the exact four paths in `metadata/catalog-audit-2026-10-12/source_manifest.json`. Keep provider, retrieval date, original file and rights evidence. Additional files/layouts present in the workspace are preserved but not covered by this manifest.
- `synthetic/`: future immutable versioned synthetic source releases, with generator seed, schema, manifest, checksums and synthetic labels.
- `prepared/`: derived learner tables for a specific source version, with transformation and reconciliation logs. Never edit a prepared CSV to fix a source without recording the change.
- `metadata/`: source manifests and reproducible schema/quality profiles; not a learner download directory.

## Reproduce the four-source audit

From the repository root:

```bash
python3 scripts/acquire_catalog_samples.py
python3 -m venv .venv-data
.venv-data/bin/python -m pip install -r requirements-data.txt
.venv-data/bin/python scripts/profile_catalog_samples.py
```

The acquisition script uses curl with normal TLS verification. With the existing manifest, it only rechecks the original SHA-256 values and performs no network request. On a first acquisition without a manifest, it downloads four catalog-observed URLs and saves originals exclusively. It stops if an original already exists without its manifest; inspect that situation instead of deleting or overwriting. Missing/hash-changed originals must be investigated before profiling. A changed upstream file requires a separately recorded version, not an in-place replacement.

The offline profiler verifies bytes/hashes, reads the manifest's XLS/XLSX/CSV files, checks the observed keys and snapshot invariants, then writes `metadata/catalog-audit-2026-10-12/profiles.json` and private `instructor/source-audit/catalog-2026-10-12-controls.json`. It does not modify raw files, reconstruct missing dates, deduplicate originals, create learner derivatives or recalculate workbook formulas. Source workbook reads use stored results. Control totals are source-inspection evidence, not released lesson answers or independent upstream verification.

Tested: Python 3.12.14, pandas 2.2.3, openpyxl 3.1.5, xlrd 2.0.2. The actual audit used the bundled Python plus xlrd installed in a temporary library directory; the local-venv recipe is a reproducibility path, not a separately tested installation. `requirements-data.txt` declares audit dependency ranges, not an exact lockfile. These dependencies are separate from MkDocs and are not required for the essential Tableau learner path.

The separately present `scripts/fetch_catalog_sources.py` and its six-source layout were not executed or adopted by this audit. Do not confuse its paths with the four-source manifest or treat its embedded checksums as verification evidence from this run.

## Next production gates

The first retail development contract is under [metadata/superstore/retail-v1/](metadata/superstore/retail-v1/metric_contract.md): [field dictionary](metadata/superstore/retail-v1/dictionary.md), [machine settings](metadata/superstore/retail-v1/contract.json) and [preparation specification](metadata/superstore/retail-v1/preparation_spec.md). It uses the exact audited original with a 2023–2025 Order Date scope, neutral source monetary-unit labels and explicit customer/return policies. This local design is distinct from a public or classroom-ready release and from the retained synthetic contracts.

Read-only D01 verification, after installing the audit dependencies above:

```bash
.venv-data/bin/python scripts/check_retail_contract.py
```

This checks the exact retail source hash/schema/keys, calendar scope, all-source customer conflicts, eligible/excluded population bridge and private control reconciliation. It also evaluates small **synthetic JSON fixtures** for distinct-order grain, weighted ratios, zero/empty cases, category overlap, return flags, customer eligibility, date boundaries and calendar comparators. It does not generate CSVs, overwrite metadata or test Tableau. The same check was executed successfully with the bundled audit Python/temp-xlrd route recorded in STATUS.md. Review evidence: [retail contract review](../planning/RETAIL_CONTRACT_REVIEW.md).

S01 inspection, the first retail D01 local-development freeze and D02 preparation are complete. [freeze.json](metadata/superstore/retail-v1/freeze.json) records seven specification/review/fixture/checker hashes; the checker verifies those frozen bytes before source/fixture checks. Frozen documents describe their historical pre-preparation state; do not edit them to reflect later completion. Other source/core contracts remain separate future work. Controlled synthetic refund/cost material follows D02R under a separate contract; no full synthetic source generator exists. Planned defect fixtures must be separate from clean reference data.

## First prepared retail development version

After installing the data dependencies above:

```bash
.venv-data/bin/python scripts/prepare_retail.py
.venv-data/bin/python scripts/validate_retail.py
```

The preparation script runs the frozen contract checker first. It projects the exact original into [prepared/superstore/retail-v1/order_lines.csv](prepared/superstore/retail-v1/order_lines.csv), stages and compares every typed value, and creates a [manifest](prepared/superstore/retail-v1/manifest.json), [quality report](prepared/superstore/retail-v1/preparation_report.json) and private exceptions under instructor/solutions/superstore/retail-v1. Existing outputs must match byte-for-byte before any new output is created; differing bytes stop the run. Do not delete or overwrite outputs to resolve a mismatch. No source fields are imputed, rounded or relabeled.

The CSV contains 6,815 lines, 3,388 distinct orders, 22 fields and 36 months, scoped by 2023–2025 Order Date. Its SHA-256 is `434ba08abf665b617294b188e38c0d0b8a86d0b3386d41eff8a42c15bc708de2`. Main KPIs retain the four scoped customer-conflict lines; customer analysis filters eligible=1 consistently. Thirty-four lines with Ship Date in 2026 remain. Preparation was repeated successfully with identical bytes and modification times in the actual bundled Python/temp-xlrd environment above.

The independent validator reads the saved CSV with declared types and Decimal, compares it to a separate pandas source read, and writes version-bound private reference answers and numerical evidence under instructor/solutions/superstore/retail-v1. It does not import the preparation helpers, change the source/CSV or run Tableau. See STATUS and the [Claude takeover brief](../planning/CLAUDE_TAKEOVER.md) for actual completion evidence, environment and remaining app checks.

This remains **local development**, not an approved learner/public release. The installed Tableau app imported the CSV and displayed 22 fields/6,815 rows; worksheet calculations, filters/grand totals and local save/reopen remain unverified. Preparation/validation metadata conservatively records no Tableau verification. Do not distribute the entire prepared directory: its quality report contains diagnostic answer counts and a private path. Select permitted delivery and reviewed learner files deliberately.

All HR data will be synthetic. No course license has been selected; obtain creator permission and record licensing before a public material/data release. No external source is assumed licensed merely because it is downloadable.
