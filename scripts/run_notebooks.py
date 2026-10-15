"""Execute the lesson notebooks in place so they carry real outputs.

Run this before `make convert-all`, which turns notebooks/*.ipynb into
docs/lectures/*.md. Each notebook runs top to bottom in a fresh kernel from the
notebooks/ folder. Execution timestamps are removed so unchanged notebooks stay
byte-identical.

The setup cell normally downloads the Superstore file from Tableau. If the
preserved local copy exists, it is used instead (COURSE_XLS_PATH), so builds
work offline and always use the audited version.

Usage:
    python scripts/run_notebooks.py [--check-data] [notebooks/01_*.ipynb ...]

--check-data also confirms that the notebooks' load_orders() reproduces the
validated prepared CSV exactly and that every notebook shares one setup cell.
Requires: requirements.txt (Python 3.12).
"""

from pathlib import Path
import os
import sys

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NB_DIR = ROOT / "notebooks"
LOCAL_XLS = ROOT / "data/raw/eu-superstore/2026-10-12/sample_-_superstore.xls"
LOCAL_MARKETING = ROOT / "data/synthetic/marketing-v1"
LOCAL_FINANCE = ROOT / "data/synthetic/finance-v1"
LOCAL_OPERATIONS = ROOT / "data/synthetic/operations-v1"
LOCAL_HR = ROOT / "data/synthetic/hr-v1"
PREPARED_CSV = ROOT / "data/prepared/superstore/retail-v1/order_lines.csv"


def merge_streams(outputs):
    """Join consecutive stdout/stderr chunks; the kernel splits them unpredictably."""
    merged = []
    for out in outputs:
        if (out.output_type == "stream" and merged and merged[-1].output_type == "stream"
                and merged[-1].name == out.name):
            merged[-1].text += out.text
        else:
            merged.append(out)
    return merged


def execute(path):
    nb = nbformat.read(path, as_version=4)
    NotebookClient(nb, timeout=600, kernel_name="python3",
                   resources={"metadata": {"path": str(NB_DIR)}}).execute()
    for cell in nb.cells:
        cell.metadata.pop("execution", None)
        if cell.cell_type == "code":
            cell.outputs = merge_streams(cell.outputs)
    errors = [o for c in nb.cells if c.cell_type == "code" for o in c.outputs if o.output_type == "error"]
    if errors:
        raise SystemExit(f"{path.name}: {len(errors)} cell(s) raised errors")
    nbformat.write(nb, path)
    print(f"executed {path.name}: {sum(c.cell_type == 'code' for c in nb.cells)} code cells")


def setup_source(path):
    nb = nbformat.read(path, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "code" and "def load_orders" in cell.source:
            return cell.source
    return None


def check_data(paths):
    import pandas as pd

    sources = {p.name: setup_source(p) for p in paths}
    with_setup = {k: v for k, v in sources.items() if v}
    assert len(set(with_setup.values())) == 1, "setup cells differ between notebooks"
    namespace = {}
    exec(next(iter(with_setup.values())), namespace)
    built = namespace["load_orders"]()
    ref = pd.read_csv(PREPARED_CSV, parse_dates=["order_date", "ship_date", "order_month"])
    assert list(built.columns) == list(ref.columns) and len(built) == len(ref)
    for col in ref.columns:
        if pd.api.types.is_float_dtype(ref[col]):
            assert ((built[col] - ref[col]).abs() < 1e-9).all(), col
        else:
            assert (built[col].astype(str).values == ref[col].astype(str).values).all(), col
    print(f"data check PASS: {len(with_setup)} notebooks share one setup cell; "
          f"{len(built)} rows / {built.order_id.nunique()} orders match {PREPARED_CSV.name}")


def main(argv):
    if LOCAL_XLS.exists():
        os.environ.setdefault("COURSE_XLS_PATH", str(LOCAL_XLS))
    if LOCAL_MARKETING.exists():
        os.environ.setdefault("COURSE_MARKETING_DIR", str(LOCAL_MARKETING))
    if LOCAL_FINANCE.exists():
        os.environ.setdefault("COURSE_FINANCE_DIR", str(LOCAL_FINANCE))
    if LOCAL_OPERATIONS.exists():
        os.environ.setdefault("COURSE_OPERATIONS_DIR", str(LOCAL_OPERATIONS))
    if LOCAL_HR.exists():
        os.environ.setdefault("COURSE_HR_DIR", str(LOCAL_HR))
    paths = [Path(a).resolve() for a in argv if a.endswith(".ipynb")] or sorted(NB_DIR.glob("*.ipynb"))
    for path in paths:
        execute(path)
    if "--check-data" in argv:
        check_data(paths)


if __name__ == "__main__":
    main(sys.argv[1:])
