"""Generate the synthetic operations-v1 teaching release (D05).

One table for Session 11 (planning/COURSE_PLAN.md, CASE_STUDIES.md "Operations"):

- shipments.csv: one row per shipment dispatched in calendar 2025, as known at
  the end of 2025-12-31 (the cutoff). Orders can split into several shipments.

Everything is synthetic: three fictional warehouses and three fictional carriers.
Built-in teaching cases: a December disruption that leaves one carrier with many
overdue undelivered shipments (hidden by a "delivered only" filter), a carrier mix
that makes one warehouse look worse than it is, a long late-delivery tail, split
orders, shipments promised after the cutoff (not yet due), shipments due on the
cutoff day and still pending, canceled shipments, and a few missing promise dates.

Deterministic: a fixed numpy seed and fixed CSV formatting.

Usage:
    python scripts/generate_operations.py            # write data/synthetic/operations-v1/
    python scripts/generate_operations.py --out DIR  # write elsewhere (for re-run checks)
Requires: requirements.txt (Python 3.12).
"""

from datetime import date, timedelta
from pathlib import Path
import hashlib
import json
import sys

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data/synthetic/operations-v1"
SEED = 20251201
VERSION = "operations-v1"
CUTOFF = date(2025, 12, 31)
N_ORDERS = 5200

WAREHOUSES = [("W1", "North hub"), ("W2", "Central hub"), ("W3", "South hub")]
CARRIERS = [("C1", "SwiftRoute"), ("C2", "ParcelOne"), ("C3", "Regional Express")]
# Carrier share by warehouse. South relies mostly on the slower, cheaper ParcelOne,
# so South looks worse overall even though each carrier performs the same everywhere.
CARRIER_MIX = {"W1": [0.55, 0.20, 0.25], "W2": [0.45, 0.30, 0.25], "W3": [0.15, 0.70, 0.15]}
WAREHOUSE_SHARE = [0.38, 0.37, 0.25]
# Promised transit days by service; typical transit days by carrier and service.
PROMISE_DAYS = {"Standard": 5, "Express": 2}
TRANSIT = {"C1": {"Standard": 2.0, "Express": 0.5}, "C2": {"Standard": 2.9, "Express": 0.9},
           "C3": {"Standard": 2.4, "Express": 0.7}}
DISRUPTION = (date(2025, 12, 8), date(2025, 12, 31))   # ParcelOne depot problem
COLUMNS = ["shipment_id", "order_id", "warehouse_id", "warehouse", "carrier_id", "carrier",
           "service", "dispatch_date", "promised_date", "delivered_date", "status"]


def season_weights(days):
    """More dispatches in November and December."""
    w = np.ones(len(days))
    for i, d in enumerate(days):
        if d.month == 11:
            w[i] = 1.5
        elif d.month == 12:
            w[i] = 1.8
        if d.weekday() == 6:
            w[i] *= 0.3                       # fewer Sunday dispatches
    return w / w.sum()


def transit_days(rng, carrier, service, dispatch):
    base = TRANSIT[carrier][service]
    days = base + rng.gamma(1.4, 0.55)        # long right tail
    if dispatch.month in (11, 12):
        days += rng.gamma(1.2, 0.6)           # peak-season congestion
    if rng.random() < 0.07:
        days += rng.integers(5, 22)           # occasional badly delayed parcel
    if carrier == "C2" and DISRUPTION[0] <= dispatch <= DISRUPTION[1]:
        days += rng.integers(6, 26)           # depot disruption
    return int(np.ceil(days))


def make_shipments(rng):
    all_days = [date(2025, 1, 1) + timedelta(days=i) for i in range(365)]
    weights = season_weights(all_days)
    rows = []
    order_days = rng.choice(len(all_days), size=N_ORDERS, p=weights)
    for n, idx in enumerate(sorted(order_days), start=1):
        order_date = all_days[idx]
        order_id = f"ORD-{n:05d}"
        wh = ["W1", "W2", "W3"][rng.choice(3, p=WAREHOUSE_SHARE)]
        n_ship = 1 if rng.random() > 0.13 else 2          # about 13% of orders split
        service = "Express" if rng.random() < 0.22 else "Standard"
        for k in range(n_ship):
            dispatch = order_date + timedelta(days=int(k * rng.integers(1, 4)))
            if dispatch > CUTOFF:
                continue                                    # not dispatched by cutoff
            carrier = ["C1", "C2", "C3"][rng.choice(3, p=CARRIER_MIX[wh])]
            promised = dispatch + timedelta(days=PROMISE_DAYS[service])
            delivered = dispatch + timedelta(days=transit_days(rng, carrier, service, dispatch))
            status = "delivered"
            if delivered > CUTOFF:
                delivered, status = None, "in_transit"
            rows.append([order_id, wh, carrier, service, dispatch, promised, delivered, status])
    df = pd.DataFrame(rows, columns=["order_id", "warehouse_id", "carrier_id", "service",
                                     "dispatch_date", "promised_date", "delivered_date", "status"])
    # Canceled shipments: a few, never delivered.
    cancel = rng.choice(df.index[df["status"] == "delivered"], size=40, replace=False)
    df.loc[cancel, ["delivered_date", "status"]] = [None, "canceled"]
    # Missing promise dates (data-quality issue) on a few delivered shipments.
    missing = rng.choice(df.index[(df["status"] == "delivered")], size=12, replace=False)
    df.loc[missing, "promised_date"] = None
    df = df.sort_values(["dispatch_date", "order_id", "carrier_id"], kind="stable").reset_index(drop=True)
    df.insert(0, "shipment_id", [f"SHP-{i:05d}" for i in range(1, len(df) + 1)])
    df["warehouse"] = df["warehouse_id"].map(dict(WAREHOUSES))
    df["carrier"] = df["carrier_id"].map(dict(CARRIERS))
    for col in ("dispatch_date", "promised_date", "delivered_date"):
        df[col] = df[col].map(lambda d: d.isoformat() if d is not None else "")
    return df[COLUMNS]


def csv_bytes(df):
    return df.to_csv(index=False, lineterminator="\n").encode("utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


README = """# operations-v1: synthetic shipments with promised and actual delivery (D05)

**Synthetic teaching data.** A fictional retailer's outbound shipments dispatched in
calendar 2025, as known at the end of **2025-12-31 (the cutoff)**. Generated by
`scripts/generate_operations.py` with seed {seed}. Warehouses and carriers are fictional.
Reuse terms for course-generated data are not yet chosen (DATA_STRATEGY "Rights status").

Used in Session 11 (operations case).

## shipments.csv

Grain: one row per **shipment** ({rows} rows). Key: `shipment_id`, unique. One order can be
split into more than one shipment, so `order_id` is **not** a key.

| Field | Type | Meaning |
|---|---|---|
| `shipment_id` | text | Unique shipment code |
| `order_id` | text | Customer order; repeats when an order is split |
| `warehouse_id`, `warehouse` | text | Dispatching warehouse (W1–W3) |
| `carrier_id`, `carrier` | text | Delivery carrier (C1–C3) |
| `service` | text | `Standard` (promise 5 calendar days) or `Express` (2 days) |
| `dispatch_date` | date | Day the shipment left the warehouse (all on or before the cutoff) |
| `promised_date` | date or blank | Day delivery was promised; may be after the cutoff; blank = unknown (data-quality issue) |
| `delivered_date` | date or blank | Day delivered; blank = not delivered as of the cutoff (or canceled) |
| `status` | text | `delivered`, `in_transit` (not delivered by the cutoff) or `canceled` |

## Contract

- Eligible shipments: status is not `canceled`.
- **Due population:** eligible shipments with a known promised date on or before the cutoff.
  It includes delivered **and** undelivered shipments.
- **On time:** delivered on or before the promised date. On-time rate = on-time due
  shipments / **all** due shipments. Overdue undelivered shipments stay in the denominator
  as failures; a "delivered only" filter overstates service.
- Shipments promised after the cutoff are **not yet due**: keep them for workload, but out of
  the on-time denominator, even if already delivered.
- Unknown promised dates are excluded from the rate with a visible count.
- Lead time = delivered − dispatched, in calendar days, for **delivered shipments only**;
  report it as "completed shipments" with the count, mean and median.
- Days past due (pending due shipments) = cutoff − promised date, at least 0. A shipment due
  on the cutoff day and still pending is a failure with 0 days past due.
- Rates for carriers, warehouses or months are ratios of counts; never average percentages.
  Count shipments, not orders, for service measures.

## Files and checks

`manifest.json` lists SHA-256, row counts, seed, generator hash and library versions.
`scripts/validate_operations.py` independently re-checks every rule above. Built-in teaching
cases and reference answers are in the private
`instructor/solutions/operations-v1/reference_answers.md`; do not copy them to learners.
"""


def main(argv):
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else DEFAULT_OUT
    out.mkdir(parents=True, exist_ok=True)
    shipments = make_shipments(np.random.default_rng(SEED))
    files = {"shipments.csv": csv_bytes(shipments),
             "README.md": README.format(seed=SEED, rows=len(shipments)).encode("utf-8")}
    for name, data in files.items():
        (out / name).write_bytes(data)
    manifest = {
        "dataset": VERSION, "label": "synthetic", "generator": "scripts/generate_operations.py",
        "generator_sha256": sha(Path(__file__).read_bytes()), "seed": SEED,
        "numpy": np.__version__, "pandas": pd.__version__, "cutoff": CUTOFF.isoformat(),
        "rights": "unresolved; see planning/DATA_STRATEGY.md Rights status",
        "files": {name: {"sha256": sha(data), "bytes": len(data)} for name, data in sorted(files.items())},
        "rows": {"shipments.csv": len(shipments)},
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(f"wrote {out}: shipments {len(shipments)} rows")


if __name__ == "__main__":
    main(sys.argv[1:])
