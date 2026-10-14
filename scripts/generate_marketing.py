"""Generate the synthetic marketing-v1 teaching release (D08).

Two tables for Sessions 8, 9 and 12 (planning/COURSE_PLAN.md):

- marketing_daily.csv: one row per (date, campaign_id) for calendar 2025.
  Seven fictional paid campaigns with a same-day funnel, spend and
  single-campaign attributed revenue.
- ab_test.csv: one row per visitor in a four-week checkout-page experiment.

Everything is synthetic. Built-in effects (funnel rates, seasonality that
drives both spend and demand, A/B lift by device) are listed in the
generated README and in the private reference answers, so exercises have a
known truth to compare against.

Deterministic: a fixed numpy seed and fixed CSV formatting. Running twice
gives byte-identical files. The manifest records numpy/pandas versions,
because numpy may change random streams between releases.

Usage:
    python scripts/generate_marketing.py            # write data/synthetic/marketing-v1/
    python scripts/generate_marketing.py --out DIR  # write elsewhere (for re-run checks)
Requires: requirements.txt (Python 3.12).
"""

from pathlib import Path
import hashlib
import json
import sys

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data/synthetic/marketing-v1"
SEED = 20251001
VERSION = "marketing-v1"

# Campaign design. Sizes are deliberately unequal: the small, high-converting
# Social campaign (SOC-02) lifts Social's simple average of campaign rates above
# Search's, while Search wins on the weighted (sum/sum) rate.
#   base_spend: typical daily spend in currency units
#   cpm: cost per 1,000 impressions; ctr: clicks/impressions
#   land: share of clicks that become sessions; cvr: sessions -> purchase
#   aov: mean order value of attributed purchases
CAMPAIGNS = [
    # id,      name,                       channel,     base_spend, cpm,  ctr,    land, cvr,    aov
    ("SRCH-01", "Search - product terms",   "Search",    900.0,  22.0, 0.045, 0.92, 0.034, 118.0),
    ("SRCH-02", "Search - category terms",  "Search",    650.0,  18.0, 0.038, 0.90, 0.029, 104.0),
    ("SOC-01",  "Social - broad audience",  "Social",   1100.0,   7.5, 0.012, 0.80, 0.011,  92.0),
    ("SOC-02",  "Social - past visitors",   "Social",     60.0,   9.0, 0.020, 0.85, 0.060, 110.0),
    ("DISP-01", "Display - partner sites",  "Display",   500.0,   3.2, 0.004, 0.70, 0.008,  88.0),
    ("VID-01",  "Video - pre-roll",         "Video",     420.0,  11.0, 0.006, 0.75, 0.010,  97.0),
    ("EML-01",  "Email - newsletter",       "Email",      40.0,   0.6, 0.008, 0.95, 0.020, 101.0),
]
COLUMNS_DAILY = ["date", "campaign_id", "campaign_name", "channel", "spend", "impressions",
                 "clicks", "sessions", "conversions", "attributed_revenue"]

# Spend has diminishing returns: impressions scale with spend ** ELASTICITY.
ELASTICITY = 0.85

# A/B test design: control conversion rate and absolute lift by device.
AB_START, AB_DAYS, AB_VISITORS = "2025-03-03", 28, 60000
AB_DEVICE_SHARE = {"mobile": 0.62, "desktop": 0.38}
AB_BASE_CVR = {"mobile": 0.026, "desktop": 0.041}
AB_LIFT = {"mobile": 0.007, "desktop": 0.0005}
AB_AOV = 96.0


def seasonality(dates):
    """Demand multiplier by day: November-December peak, weekend dip, mild summer lull."""
    doy = dates.dayofyear.to_numpy()
    month = dates.month.to_numpy()
    peak = np.where(month == 11, 1.35, np.where(month == 12, 1.55, 1.0))
    lull = 1.0 - 0.12 * np.exp(-((doy - 200) / 30.0) ** 2)
    weekend = np.where(dates.dayofweek.to_numpy() >= 5, 0.88, 1.0)
    return peak * lull * weekend


def budget_pacing(dates):
    """Spend multiplier: marketers raise budgets ahead of the peak (the confounder)."""
    month = dates.month.to_numpy()
    return np.where(month == 11, 1.45, np.where(month == 12, 1.60, np.where(month == 10, 1.15, 1.0)))


def order_values(rng, n, mean):
    """Right-skewed order values with the given mean (lognormal, sigma 0.55)."""
    sigma = 0.55
    mu = np.log(mean) - sigma ** 2 / 2
    return np.round(rng.lognormal(mu, sigma, n), 2)


def make_daily(rng):
    dates = pd.date_range("2025-01-01", "2025-12-31", freq="D")
    season = seasonality(dates)
    pacing = budget_pacing(dates)
    frames = []
    for cid, name, channel, base_spend, cpm, ctr, land, cvr, aov in CAMPAIGNS:
        n = len(dates)
        spend = base_spend * pacing * rng.lognormal(0, 0.18, n)
        # Paused days: spend 0 and nothing served. Email has no media cost on
        # some send days but still converts (flagged review case, not infinite ROAS).
        paused = rng.random(n) < (0.015 if channel != "Email" else 0.0)
        spend = np.where(paused, 0.0, spend)
        if channel == "Email":
            free_send = rng.random(n) < 0.03
            spend = np.where(free_send, 0.0, spend)
        else:
            free_send = np.zeros(n, dtype=bool)
        spend = np.round(spend, 2)

        effective = np.where(free_send, base_spend, spend)
        exp_impr = (effective * 1000.0 / cpm) * (base_spend / np.maximum(effective, 1e-9)) ** (1 - ELASTICITY)
        exp_impr = np.where(effective > 0, exp_impr, 0.0)
        impressions = rng.poisson(exp_impr)
        clicks = rng.binomial(impressions, np.clip(ctr * np.sqrt(season), 0, 1))
        sessions = rng.binomial(clicks, land)
        conversions = rng.binomial(sessions, np.clip(cvr * season, 0, 1))
        revenue = np.array([order_values(rng, k, aov).sum() for k in conversions])
        frames.append(pd.DataFrame({
            "date": dates.strftime("%Y-%m-%d"), "campaign_id": cid, "campaign_name": name,
            "channel": channel, "spend": spend, "impressions": impressions, "clicks": clicks,
            "sessions": sessions, "conversions": conversions, "attributed_revenue": np.round(revenue, 2),
        }))
    daily = pd.concat(frames, ignore_index=True).sort_values(["date", "campaign_id"], kind="stable")
    return daily[COLUMNS_DAILY].reset_index(drop=True)


def make_ab(rng):
    n = AB_VISITORS
    day = rng.integers(0, AB_DAYS, n)
    dates = pd.Timestamp(AB_START) + pd.to_timedelta(day, unit="D")
    device = np.where(rng.random(n) < AB_DEVICE_SHARE["mobile"], "mobile", "desktop")
    variant = np.where(rng.random(n) < 0.5, "A", "B")
    base = np.where(device == "mobile", AB_BASE_CVR["mobile"], AB_BASE_CVR["desktop"])
    lift = np.where(device == "mobile", AB_LIFT["mobile"], AB_LIFT["desktop"])
    p = base + np.where(variant == "B", lift, 0.0)
    converted = (rng.random(n) < p).astype(int)
    revenue = np.where(converted == 1, order_values(rng, n, AB_AOV), 0.0)
    ab = pd.DataFrame({"visitor_id": [f"V{i:06d}" for i in range(1, n + 1)],
                       "date": dates.strftime("%Y-%m-%d"), "device": device, "variant": variant,
                       "converted": converted, "revenue": np.round(revenue, 2)})
    return ab.sort_values(["date", "visitor_id"], kind="stable").reset_index(drop=True)


def csv_bytes(df):
    return df.to_csv(index=False, lineterminator="\n", float_format="%.2f").encode("utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


README = """# marketing-v1: synthetic marketing and A/B test data (D08)

**Synthetic teaching data.** Every campaign, visitor and number is generated by
`scripts/generate_marketing.py` with seed {seed} (stream 1 for the daily table, stream 2 for the A/B test). No real company, brand, person or
platform is described. Monetary amounts are in neutral **currency units**: the course
has not fixed a currency (DEC-006's NPR proposal is still a recommendation), so do not
label them as dollars, rupees or anything else. Reuse terms for course-generated data
are not yet chosen (DATA_STRATEGY "Rights status").

Used in Session 8 (correlation and regression), Session 9 (sampling, confidence
intervals, A/B tests) and Session 12 (marketing case).

## marketing_daily.csv

Grain: one row per **calendar day in 2025 x paid campaign** ({daily_rows} rows = 365 days x 7 campaigns).
Key: (`date`, `campaign_id`), unique and complete.

| Field | Type | Meaning |
|---|---|---|
| `date` | date (YYYY-MM-DD) | Calendar day the activity happened |
| `campaign_id` | text | Campaign code, e.g. `SRCH-01` |
| `campaign_name` | text | Readable campaign name |
| `channel` | text | Search, Social, Display, Video or Email |
| `spend` | decimal, currency units | Media cost that day; 0 on paused days and on some Email send days |
| `impressions` | integer | Times an ad or email was shown |
| `clicks` | integer | Clicks on the ad or email |
| `sessions` | integer | Website visits that started from those clicks |
| `conversions` | integer | Sessions that ended in a purchase (one order per purchasing session) |
| `attributed_revenue` | decimal, currency units | Sum of those orders' values, pre-return |

Contract:

- Funnel bounds hold on every row: impressions >= clicks >= sessions >= conversions >= 0.
- Attribution is a **synthetic single-campaign allocation**: each purchase belongs to exactly one
  campaign, same day. There is no touchpoint history, no view-through and no organic traffic,
  so this table cannot validate a last-click or multi-touch claim.
- Rates are ratios of sums at every scope: CTR = clicks / impressions; session conversion rate =
  conversions / sessions; CPC = spend / clicks; CPA = spend / conversions;
  ROAS = attributed_revenue / spend. A zero denominator gives a blank (null), never 0 or infinity.
- Rows with spend = 0 and conversions > 0 (Email free-send days) are **review cases**: report
  them, do not compute ROAS for them.
- Never average daily or campaign rates to get a total rate; weight by the denominator.

## ab_test.csv

Grain: one row per **visitor** randomly assigned to variant A (current checkout page) or
B (new checkout page), {ab_rows} visitors over 28 days from {ab_start}.

| Field | Type | Meaning |
|---|---|---|
| `visitor_id` | text | Unique visitor code |
| `date` | date | Day of the visitor's first visit in the test |
| `device` | text | `mobile` or `desktop` |
| `variant` | text | `A` (control) or `B` (treatment) |
| `converted` | 0/1 | 1 if the visitor purchased during the test |
| `revenue` | decimal, currency units | Order value if converted, else 0 |

Contract: one row per visitor; assignment is random and independent of device; conversion
rate = converted visitors / visitors in the group; revenue per visitor includes zeros.

## Files and checks

`manifest.json` lists SHA-256, row counts, seed, generator hash and library versions.
`scripts/validate_marketing.py` independently re-checks every rule above.
Built-in "true" effects for teaching are in the private
`instructor/solutions/marketing-v1/reference_answers.md`; do not copy them to learners.
"""


def main(argv):
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else DEFAULT_OUT
    out.mkdir(parents=True, exist_ok=True)
    # Independent streams, so changing one table's design never changes the other.
    daily = make_daily(np.random.default_rng([SEED, 1]))
    ab = make_ab(np.random.default_rng([SEED, 2]))
    files = {"marketing_daily.csv": csv_bytes(daily), "ab_test.csv": csv_bytes(ab),
             "README.md": README.format(seed=SEED, daily_rows=len(daily), ab_rows=len(ab),
                                        ab_start=AB_START).encode("utf-8")}
    for name, data in files.items():
        (out / name).write_bytes(data)
    manifest = {
        "dataset": VERSION,
        "label": "synthetic",
        "generator": "scripts/generate_marketing.py",
        "generator_sha256": sha(Path(__file__).read_bytes()),
        "seed": SEED,
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "currency": "neutral currency units (not fixed by the course)",
        "rights": "unresolved; see planning/DATA_STRATEGY.md Rights status",
        "files": {name: {"sha256": sha(data), "bytes": len(data)} for name, data in sorted(files.items())},
        "rows": {"marketing_daily.csv": len(daily), "ab_test.csv": len(ab)},
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(f"wrote {out}: marketing_daily {len(daily)} rows, ab_test {len(ab)} rows")


if __name__ == "__main__":
    main(sys.argv[1:])
