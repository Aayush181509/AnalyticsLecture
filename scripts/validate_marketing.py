"""Independently validate the synthetic marketing-v1 release (D08).

Re-reads the CSVs with the standard library only (no pandas), so the checks do
not share code with the generator. It checks:

1. manifest SHA-256 and row counts;
2. regeneration into a temporary folder is byte-identical (determinism);
3. marketing_daily: complete unique (date, campaign_id) keys for 2025,
   nonnegative values, funnel bounds, revenue only with conversions,
   and the documented zero-denominator and spend-0 review cases;
4. ab_test: unique visitors, valid domains, revenue only when converted,
   balanced random assignment;
5. the teaching effects survive the seed: Social beats Search on the mean of
   campaign conversion rates but loses on the weighted rate; the pooled daily
   spend-to-revenue slope exceeds the Jan-Sep slope (seasonal confounding);
   the A/B 95% confidence interval for the lift excludes zero.

Usage:
    python scripts/validate_marketing.py
    python scripts/validate_marketing.py --answers instructor/solutions/marketing-v1/reference_answers.md
Requires: requirements.txt (Python 3.12).
"""

from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
import csv
import hashlib
import json
import math
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/synthetic/marketing-v1"
GENERATOR = ROOT / "scripts/generate_marketing.py"
CAMPAIGNS = 7
COUNTS = ["impressions", "clicks", "sessions", "conversions"]


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def read(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ratio(num, den):
    return num / den if den else None


def slope(xs, ys):
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def check_manifest():
    manifest = json.loads((DATA / "manifest.json").read_text())
    for name, info in manifest["files"].items():
        data = (DATA / name).read_bytes()
        require(hashlib.sha256(data).hexdigest() == info["sha256"], f"{name} hash differs from manifest")
        require(len(data) == info["bytes"], f"{name} size differs from manifest")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([sys.executable, str(GENERATOR), "--out", tmp], check=True, capture_output=True)
        for name in list(manifest["files"]) + ["manifest.json"]:
            require((Path(tmp) / name).read_bytes() == (DATA / name).read_bytes(), f"{name} not reproducible")
    return manifest


def check_daily(rows):
    keys = {(r["date"], r["campaign_id"]) for r in rows}
    require(len(keys) == len(rows), "duplicate (date, campaign_id)")
    days = {(date(2025, 1, 1) + timedelta(d)).isoformat() for d in range(365)}
    campaigns = {r["campaign_id"] for r in rows}
    require(len(campaigns) == CAMPAIGNS and keys == {(d, c) for d in days for c in campaigns}, "keys incomplete")
    review = []
    for r in rows:
        n = [int(r[c]) for c in COUNTS]
        spend, rev = float(r["spend"]), float(r["attributed_revenue"])
        require(min(n) >= 0 and spend >= 0 and rev >= 0, f"negative value {r}")
        require(n[0] >= n[1] >= n[2] >= n[3], f"funnel order broken {r}")
        require((n[3] == 0) == (rev == 0), f"revenue without conversions or vice versa {r}")
        if spend == 0 and n[3] > 0:
            review.append(r)
    require(review and all(r["channel"] == "Email" for r in review), "spend-0 review cases missing or outside Email")
    require(any(int(r["clicks"]) == 0 for r in rows), "no zero-click rows for null CPC")
    require(any(int(r["conversions"]) == 0 for r in rows), "no zero-conversion rows for null CPA")
    return review


def daily_summaries(rows):
    by_campaign = defaultdict(lambda: defaultdict(float))
    names = {}
    for r in rows:
        c = by_campaign[r["campaign_id"]]
        names[r["campaign_id"]] = (r["channel"], r["campaign_name"])
        for f in ["spend", "attributed_revenue"] + COUNTS:
            c[f] += float(r[f])
    by_channel = defaultdict(lambda: defaultdict(float))
    rates = defaultdict(list)
    for cid, c in by_campaign.items():
        ch = names[cid][0]
        for f, v in c.items():
            by_channel[ch][f] += v
        rates[ch].append(c["conversions"] / c["sessions"])
    weighted = {ch: c["conversions"] / c["sessions"] for ch, c in by_channel.items()}
    mean_rates = {ch: sum(v) / len(v) for ch, v in rates.items()}
    require(mean_rates["Social"] > mean_rates["Search"] and weighted["Social"] < weighted["Search"],
            "Social/Search weighted-vs-mean-of-rates reversal did not survive")

    per_day = defaultdict(lambda: [0.0, 0.0])
    for r in rows:
        per_day[r["date"]][0] += float(r["spend"])
        per_day[r["date"]][1] += float(r["attributed_revenue"])
    all_days = sorted(per_day)
    base_days = [d for d in all_days if int(d[5:7]) <= 9]
    pooled = slope([per_day[d][0] for d in all_days], [per_day[d][1] for d in all_days])
    base = slope([per_day[d][0] for d in base_days], [per_day[d][1] for d in base_days])
    require(pooled > 1.5 * base, "seasonal confounding too weak")
    return by_campaign, names, by_channel, weighted, mean_rates, pooled, base


def check_ab(rows):
    require(len({r["visitor_id"] for r in rows}) == len(rows), "duplicate visitor_id")
    groups = defaultdict(lambda: [0, 0, 0.0])
    for r in rows:
        require(r["variant"] in {"A", "B"} and r["device"] in {"mobile", "desktop"}, f"bad domain {r}")
        require(r["converted"] in {"0", "1"}, f"bad converted {r}")
        require((r["converted"] == "1") == (float(r["revenue"]) > 0), f"revenue/converted mismatch {r}")
        for key in (r["variant"], (r["device"], r["variant"])):
            g = groups[key]
            g[0] += 1
            g[1] += int(r["converted"])
            g[2] += float(r["revenue"])
    share_b = groups["B"][0] / len(rows)
    require(abs(share_b - 0.5) < 0.01, "assignment unbalanced")

    def lift(a, b):
        pa, pb = a[1] / a[0], b[1] / b[0]
        se = math.sqrt(pa * (1 - pa) / a[0] + pb * (1 - pb) / b[0])
        pooled = (a[1] + b[1]) / (a[0] + b[0])
        z = (pb - pa) / math.sqrt(pooled * (1 - pooled) * (1 / a[0] + 1 / b[0]))
        p = math.erfc(abs(z) / math.sqrt(2))
        return pa, pb, pb - pa, pb - pa - 1.96 * se, pb - pa + 1.96 * se, z, p

    results = {"all": lift(groups["A"], groups["B"])}
    for dev in ("mobile", "desktop"):
        results[dev] = lift(groups[(dev, "A")], groups[(dev, "B")])
    require(results["all"][3] > 0, "overall A/B CI includes zero")
    return groups, results, share_b


def pct(x, d=2):
    return "null" if x is None else f"{100 * x:.{d}f}%"


def money(x):
    return "null" if x is None else f"{x:,.2f}"


def write_answers(path, manifest, review, summ, ab):
    by_campaign, names, by_channel, weighted, mean_rates, pooled, base = summ
    groups, results, share_b = ab
    sys.path.insert(0, str(ROOT / "scripts"))
    import generate_marketing as g  # design constants only, for the "true effect" section

    lines = [
        "# marketing-v1 reference answers (private)",
        "",
        f"Instructor-only. Computed by `scripts/validate_marketing.py --answers` from dataset `{manifest['dataset']}`",
        f"(marketing_daily.csv SHA-256 `{manifest['files']['marketing_daily.csv']['sha256']}`,",
        f"ab_test.csv SHA-256 `{manifest['files']['ab_test.csv']['sha256']}`, seed {manifest['seed']}).",
        "Amounts are neutral currency units. Do not copy into learner notebooks.",
        "",
        "## Campaign totals for 2025 (ratios of sums; null = zero denominator)",
        "",
        "| Campaign | Channel | Spend | Sessions | Conversions | Conv. rate | CPA | Revenue | ROAS |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for cid in sorted(by_campaign):
        c = by_campaign[cid]
        lines.append(f"| {cid} | {names[cid][0]} | {money(c['spend'])} | {int(c['sessions']):,} | {int(c['conversions']):,} | "
                     f"{pct(ratio(c['conversions'], c['sessions']))} | {money(ratio(c['spend'], c['conversions']))} | "
                     f"{money(c['attributed_revenue'])} | {ratio(c['attributed_revenue'], c['spend']):.2f} |")
    tot = defaultdict(float)
    for c in by_campaign.values():
        for f, v in c.items():
            tot[f] += v
    lines += [
        f"| **All** | | {money(tot['spend'])} | {int(tot['sessions']):,} | {int(tot['conversions']):,} | "
        f"{pct(tot['conversions'] / tot['sessions'])} | {money(tot['spend'] / tot['conversions'])} | "
        f"{money(tot['attributed_revenue'])} | {tot['attributed_revenue'] / tot['spend']:.2f} |",
        "",
        f"Company CTR {pct(tot['clicks'] / tot['impressions'], 3)}; CPC {money(tot['spend'] / tot['clicks'])}.",
        "Email ROAS looks extreme because Email has almost no media cost; say so rather than ranking it first.",
        "",
        "## Weighted rate vs mean of campaign rates (session conversion)",
        "",
        "| Channel | Weighted (sum/sum) | Mean of campaign rates |",
        "|---|---|---|",
    ]
    for ch in sorted(weighted):
        lines.append(f"| {ch} | {pct(weighted[ch])} | {pct(mean_rates[ch])} |")
    lines += [
        "",
        "Trap: Social looks better than Search on the mean of rates because the tiny SOC-02",
        "retargeting campaign converts very well; weighted by sessions, Search is far better.",
        "",
        "## Zero-denominator and review cases",
        "",
    ]
    daily = read("marketing_daily.csv")
    lines += [
        f"- Rows with spend = 0: {sum(float(r['spend']) == 0 for r in daily)} "
        f"(paused days with nothing served, plus Email free-send days).",
        f"- Spend = 0 but conversions > 0 (review cases, ROAS undefined, all Email): {len(review)} rows.",
        f"- Clicks = 0 (CPC null): {sum(int(r['clicks']) == 0 for r in daily)} rows.",
        f"- Conversions = 0 (CPA null): {sum(int(r['conversions']) == 0 for r in daily)} rows.",
        "",
        "## Spend and revenue: regression and confounding (Session 8)",
        "",
        "Daily company totals, ordinary least squares slope of attributed revenue on spend:",
        "",
        f"- All 365 days: {pooled:.2f} revenue per unit of spend.",
        f"- January to September only (no budget ramp, no holiday demand): {base:.2f}.",
        "",
        "Why they differ: the generator raises budgets in October to December (pacing x1.15, x1.45,",
        "x1.60) and, independently, raises demand in November and December (conversion and CTR",
        "multipliers). Season drives both spend and revenue, so the pooled slope overstates what",
        "extra spend buys. Controlling for month (or using Jan-Sep) is closer to the built-in effect.",
        "",
        "Built-in marginal revenue per unit of spend at typical spend outside peak season",
        f"(elasticity {g.ELASTICITY} x 1000/CPM x CTR x landing x CVR x mean order value):",
        "",
        "| Campaign | True marginal ROAS |",
        "|---|---|",
    ]
    for cid, _, _, base_spend, cpm, ctr, land, cvr, aov in g.CAMPAIGNS:
        lines.append(f"| {cid} | {g.ELASTICITY * 1000 / cpm * ctr * land * cvr * aov:.2f} |")
    lines += [
        "",
        "Impressions grow with spend to the power 0.85, so returns diminish: doubling spend gives",
        f"about {2 ** g.ELASTICITY:.2f}x the impressions, not 2x.",
        "",
        "## A/B test (Sessions 9 and 12)",
        "",
        f"Built-in truth: control conversion {pct(g.AB_BASE_CVR['mobile'], 1)} mobile / "
        f"{pct(g.AB_BASE_CVR['desktop'], 1)} desktop; absolute lift "
        f"+{100 * g.AB_LIFT['mobile']:.2f} points mobile, +{100 * g.AB_LIFT['desktop']:.2f} points desktop.",
        f"Share assigned to B: {pct(share_b)}.",
        "",
        "| Group | Visitors A | Visitors B | Conv. A | Conv. B | Lift (points) | 95% CI (points) | z | p (two-sided) |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for key, label in (("all", "All"), ("mobile", "Mobile"), ("desktop", "Desktop")):
        pa, pb, d, lo, hi, z, p = results[key]
        a = groups["A"] if key == "all" else groups[(key, "A")]
        b = groups["B"] if key == "all" else groups[(key, "B")]
        lines.append(f"| {label} | {a[0]:,} | {b[0]:,} | {pct(pa)} | {pct(pb)} | {100 * d:+.2f} | "
                     f"{100 * lo:+.2f} to {100 * hi:+.2f} | {z:.2f} | {p:.4f} |")
    rpv_a, rpv_b = groups["A"][2] / groups["A"][0], groups["B"][2] / groups["B"][0]
    lines += [
        "",
        f"Revenue per visitor: A {rpv_a:.2f}, B {rpv_b:.2f}. CI uses the unpooled normal",
        "approximation; z and p use the pooled two-proportion test. A bootstrap CI should be close.",
        "",
        "Teaching points: the overall lift is statistically clear but about half a percentage point;",
        "most of it comes from mobile. The desktop estimate is noisier than its true lift because",
        "of sampling error, which is itself a lesson: a subgroup result needs its own interval.",
        "",
    ]
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text("\n".join(lines))
    print(f"wrote {path}")


def main(argv):
    manifest = check_manifest()
    daily = read("marketing_daily.csv")
    ab_rows = read("ab_test.csv")
    review = check_daily(daily)
    summ = daily_summaries(daily)
    ab = check_ab(ab_rows)
    print(f"PASS: marketing_daily {len(daily)} rows, ab_test {len(ab_rows)} rows; hashes, reproducibility, "
          f"funnel bounds, keys, zero cases, rate reversal, confounding and A/B CI checked")
    if "--answers" in argv:
        write_answers(argv[argv.index("--answers") + 1], manifest, review, summ, ab)


if __name__ == "__main__":
    main(sys.argv[1:])
