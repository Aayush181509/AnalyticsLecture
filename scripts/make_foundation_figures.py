"""Generate the SVG figures used on the learner Foundations pages.

Inputs are preserved raw sources (Datasaurus Dozen, Challenger O-ring data),
published constants (Anscombe's quartet, Berkeley 1973 admissions) and small
synthetic illustrations created here with a fixed seed. Outputs go to
docs/assets/foundations/. Re-running produces identical files.

Usage:
    python scripts/make_foundation_figures.py
Requires: pandas, matplotlib, pyreadr (see requirements.txt).
"""

from pathlib import Path
import logging

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import pandas as pd
import pyreadr

# SVG text is rendered by the browser in the site font; local font lookups only affect layout metrics.
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "foundations"
DATASAURUS = ROOT / "data/raw/datasaurus-dozen/retrieved-2026-10-12/datasaurus_dozen.rda"
CHALLENGER = ROOT / "data/raw/challenger-o-rings/retrieved-2026-10-12/o-ring-erosion-or-blowby.data"

# Validated categorical slots (blue, orange, aqua) plus neutral context ink.
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
CONTEXT = "#b4b2ac"
INK, INK_2 = "#0b0b0b", "#52514e"
GRID = "#e6e5e1"
SURFACE = "#fcfcfb"

plt.rcParams.update({
    "svg.fonttype": "none",
    "svg.hashsalt": "foundations",
    "font.family": ["Lato", "Helvetica Neue", "Arial", "sans-serif"],
    "font.size": 11,
    "text.color": INK,
    "axes.labelcolor": INK_2,
    "axes.edgecolor": GRID,
    "axes.linewidth": 1,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.titlelocation": "left",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.axisbelow": True,
    "grid.color": GRID,
    "grid.linewidth": 0.8,
    "xtick.color": INK_2,
    "ytick.color": INK_2,
    "xtick.major.size": 0,
    "ytick.major.size": 0,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
})


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / name, format="svg", bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print("wrote", (OUT / name).relative_to(ROOT))


def anscombe():
    x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
    sets = {
        "I": (x, [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
        "II": (x, [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]),
        "III": (x, [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]),
        "IV": (x4, [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]),
    }
    fig, axes = plt.subplots(2, 2, figsize=(8, 6.4), sharex=True, sharey=True)
    line_x = np.array([2, 20])
    for ax, (name, (xs, ys)) in zip(axes.flat, sets.items()):
        slope, intercept = np.polyfit(xs, ys, 1)
        ax.plot(line_x, intercept + slope * line_x, color=ORANGE, linewidth=2, zorder=1)
        ax.scatter(xs, ys, s=46, color=BLUE, edgecolor=SURFACE, linewidth=1.5, zorder=2)
        ax.set_title(f"Dataset {name}")
        ax.set_xlim(2, 20)
        ax.set_ylim(2, 14)
    for ax in axes[1]:
        ax.set_xlabel("x")
    for ax in axes[:, 0]:
        ax.set_ylabel("y")
    fig.suptitle("Same averages, same spread, same trend line, four different stories",
                 x=0.01, ha="left", fontsize=13, fontweight="bold")
    fig.tight_layout()
    save(fig, "anscombe.svg")


def datasaurus():
    df = list(pyreadr.read_r(str(DATASAURUS)).values())[0]
    order = ["dino", "star", "bullseye", "x_shape", "circle", "slant_up",
             "h_lines", "v_lines", "wide_lines", "high_lines", "dots", "away", "slant_down"]
    fig, axes = plt.subplots(3, 5, figsize=(11, 7), sharex=True, sharey=True)
    for ax in axes.flat:
        ax.set_visible(False)
    for ax, name in zip(axes.flat, order):
        d = df[df.dataset == name]
        ax.set_visible(True)
        ax.scatter(d.x, d.y, s=9, color=ORANGE if name == "dino" else BLUE, linewidth=0)
        ax.set_title(name.replace("_", " "), fontsize=11)
        ax.set_xticks([20, 60, 100])
        ax.set_yticks([0, 50, 100])
    stats = df.groupby("dataset").agg(mx=("x", "mean"), my=("y", "mean"), sx=("x", "std"), sy=("y", "std"))
    corr = df.groupby("dataset")[["x", "y"]].apply(lambda d: d.x.corr(d.y))
    note = (f"Every panel:  mean x ≈ {stats.mx.mean():.1f}   mean y ≈ {stats.my.mean():.1f}\n"
            f"sd x ≈ {stats.sx.mean():.1f}   sd y ≈ {stats.sy.mean():.1f}\n"
            f"correlation between {corr.min():.2f} and {corr.max():.2f}")
    fig.suptitle("The Datasaurus Dozen: thirteen datasets with (almost) identical statistics",
                 x=0.01, ha="left", fontsize=13, fontweight="bold")
    fig.tight_layout()
    fig.text(0.62, 0.17, note, fontsize=10, color=INK_2, va="center")
    save(fig, "datasaurus.svg")


def ice_cream_crime():
    rng = np.random.default_rng(42)
    months = np.arange(36)
    temp = 22 + 9 * np.sin((months % 12 - 3) / 12 * 2 * np.pi) + rng.normal(0, 1.2, 36)
    ice = 40 + 6.5 * temp + rng.normal(0, 12, 36)
    crime = 55 + 1.6 * temp + rng.normal(0, 4, 36)
    r = np.corrcoef(ice, crime)[0, 1]

    fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 4.2))
    a.scatter(ice, crime, s=40, color=BLUE, edgecolor=SURFACE, linewidth=1.2)
    a.set_title(f"Strong link: r = {r:.2f}")
    a.set_xlabel("Ice cream sales (units, synthetic)")
    a.set_ylabel("Crime index (synthetic)")

    b.plot(months, (ice - ice.mean()) / ice.std(), color=BLUE, linewidth=2, label="Ice cream sales")
    b.plot(months, (crime - crime.mean()) / crime.std(), color=ORANGE, linewidth=2, label="Crime index")
    b.plot(months, (temp - temp.mean()) / temp.std(), color=CONTEXT, linewidth=2, linestyle="--",
           label="Temperature (hidden driver)")
    b.set_title("Both rise and fall with the weather")
    b.set_xlabel("Month")
    b.set_ylabel("Standardised value")
    b.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3, fontsize=9)
    fig.suptitle("Synthetic illustration: correlation without causation",
                 x=0.01, ha="left", fontsize=13, fontweight="bold")
    fig.tight_layout()
    save(fig, "ice-cream-crime.svg")


def truncated_axis():
    names = ["Product A", "Product B"]
    values = [96, 98]
    fig, (a, b) = plt.subplots(1, 2, figsize=(9, 3.8))
    for ax, ylim, title in [(a, (95, 98.5), "Axis starts at 95: B looks 3× bigger"),
                            (b, (0, 105), "Axis starts at 0: almost the same")]:
        ax.bar(names, values, color=[CONTEXT, BLUE], width=0.55)
        ax.set_ylim(*ylim)
        ax.set_title(title)
        ax.grid(axis="x", visible=False)
        for i, v in enumerate(values):
            ax.text(i, v + (ylim[1] - ylim[0]) * 0.02, f"{v}%", ha="center", color=INK, fontsize=10)
    a.set_ylabel("Customer satisfaction (synthetic)")
    fig.suptitle("Same two numbers, two impressions", x=0.01, ha="left", fontsize=13, fontweight="bold")
    fig.tight_layout()
    save(fig, "truncated-axis.svg")


def berkeley():
    depts = ["A", "B", "C", "D", "E", "F"]
    men = [62, 63, 37, 33, 28, 6]
    women = [82, 68, 34, 35, 24, 7]
    labels = ["All\n(overall)"] + [f"Dept {d}" for d in depts]
    men_all = [44] + men
    women_all = [35] + women
    x = np.arange(len(labels))
    w = 0.36
    fig, ax = plt.subplots(figsize=(10, 4.4))
    ax.bar(x - w / 2 - 0.02, men_all, w, color=BLUE, label="Men")
    ax.bar(x + w / 2 + 0.02, women_all, w, color=ORANGE, label="Women")
    for i, (m, f) in enumerate(zip(men_all, women_all)):
        ax.text(i - w / 2 - 0.02, m + 1.5, f"{m}%", ha="center", fontsize=9, color=INK)
        ax.text(i + w / 2 + 0.02, f + 1.5, f"{f}%", ha="center", fontsize=9, color=INK)
    ax.axvline(0.5, color=CONTEXT, linewidth=1)
    ax.set_xticks(x, labels)
    ax.set_ylim(0, 95)
    ax.set_ylabel("Share of applicants admitted")
    ax.grid(axis="x", visible=False)
    ax.legend(frameon=False, ncol=2, loc="upper right")
    ax.set_title("UC Berkeley graduate admissions, 1973: overall vs the six largest departments")
    fig.tight_layout()
    save(fig, "simpsons-berkeley.svg")


def challenger():
    cols = ["at_risk", "incidents", "temp_f", "pressure", "order"]
    d = pd.read_csv(CHALLENGER, sep=r"\s+", header=None, names=cols)
    launch_f = 36
    # Separate flights that share the same temperature and damage count.
    d["y"] = d.incidents + d.groupby(["temp_f", "incidents"]).cumcount() * 0.12
    d["y"] = d.y - d.groupby(["temp_f", "incidents"]).y.transform(lambda v: (v.max() - v.min()) / 2)
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 4.2), sharey=True)
    hit = d[d.incidents > 0]
    a.scatter(hit.temp_f, hit.y, s=60, color=ORANGE, edgecolor=SURFACE, linewidth=1.2)
    a.set_title("Only flights with O-ring problems")
    b.scatter(d[d.incidents == 0].temp_f, d[d.incidents == 0].y, s=60, color=BLUE,
              edgecolor=SURFACE, linewidth=1.2, label="No problems")
    b.scatter(hit.temp_f, hit.y, s=60, color=ORANGE, edgecolor=SURFACE, linewidth=1.2,
              label="Erosion or blow-by")
    b.set_title("All 23 earlier flights")
    b.legend(frameon=False, loc="upper right", fontsize=9)
    for ax in (a, b):
        ax.set_xlim(30, 85)
        ax.set_ylim(-0.3, 3.2)
        ax.set_yticks([0, 1, 2, 3])
        ax.set_xlabel("Launch temperature (°F)")
        ax.axvline(launch_f, color=INK_2, linewidth=1.2, linestyle="--")
        ax.text(launch_f + 1, 2.95, "Challenger\nlaunch ≈ 36°F", fontsize=9, color=INK_2, va="top")
    a.set_ylabel("O-rings with damage (of 6)")
    fig.suptitle("Same data, different view: including the zero-problem flights reveals the cold-weather risk",
                 x=0.01, ha="left", fontsize=13, fontweight="bold")
    fig.tight_layout()
    save(fig, "challenger.svg")


def data_ink():
    regions = ["North", "South", "East", "West", "Central"]
    sales = [42, 35, 58, 29, 47]
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 4))
    loud = ["#c0392b", "#8e44ad", "#2980b9", "#27ae60", "#f39c12"]
    a.bar(regions, sales, color=loud, edgecolor=INK, linewidth=1.5, hatch="//")
    a.set_facecolor("#ececec")
    a.grid(True, color="#9a9a9a", linewidth=1.2)
    for s in a.spines.values():
        s.set_visible(True)
        s.set_color(INK)
        s.set_linewidth(1.5)
    a.set_title("Before: heavy grid, borders, five colours")
    a.set_ylabel("Sales (synthetic)")
    a.set_ylim(0, 70)

    order = np.argsort(sales)[::-1]
    r = [regions[i] for i in order]
    s = [sales[i] for i in order]
    b.barh(r[::-1], s[::-1], color=[CONTEXT] * 4 + [BLUE], height=0.6)
    b.grid(False)
    b.spines["left"].set_visible(False)
    b.spines["bottom"].set_visible(False)
    b.set_xticks([])
    for y, v in enumerate(s[::-1]):
        b.text(v + 1, y, str(v), va="center", fontsize=10, color=INK)
    b.set_title("After: sorted, one highlight, direct labels\nSales (synthetic)")
    fig.suptitle("Raising the data-ink ratio", x=0.01, ha="left", fontsize=13, fontweight="bold")
    fig.tight_layout()
    save(fig, "data-ink.svg")


def gestalt():
    fig, axes = plt.subplots(1, 4, figsize=(11, 3.2))
    for ax in axes:
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 6)
        ax.set_aspect("equal")
        ax.axis("off")
    gx, gy = np.meshgrid(np.arange(6) + 0.5, np.arange(6) + 0.5)

    a = axes[0]
    xs = np.r_[np.arange(3) * 0.7 + 0.5, np.arange(3) * 0.7 + 3.6]
    for y in np.arange(6) * 0.9 + 0.7:
        a.scatter(xs, [y] * 6, s=60, color=INK_2)
    a.set_title("Proximity\nclose things group")

    b = axes[1]
    colors = [BLUE if (i % 2 == 0) else CONTEXT for i in range(6)]
    for i, x in enumerate(np.arange(6) + 0.5):
        b.scatter([x] * 6, np.arange(6) + 0.5, s=60, color=colors[i])
    b.set_title("Similarity\nsame colour groups")

    c = axes[2]
    c.scatter(gx.ravel(), gy.ravel(), s=60, color=INK_2)
    c.add_patch(plt.Rectangle((1.05, 2.05), 1.9, 1.9, facecolor=BLUE, alpha=0.18, edgecolor="none"))
    c.set_title("Enclosure\na shaded box groups")

    d = axes[3]
    d.scatter(gx.ravel(), gy.ravel(), s=60, color=INK_2, zorder=2)
    d.plot([0.5, 1.5, 2.5, 3.5], [1.5, 3.5, 2.5, 4.5], color=ORANGE, linewidth=2, zorder=1)
    d.scatter([0.5, 1.5, 2.5, 3.5], [1.5, 3.5, 2.5, 4.5], s=60, color=ORANGE, zorder=3)
    d.set_title("Connection\nlinked points group")
    fig.tight_layout()
    save(fig, "gestalt.svg")


def preattentive():
    rng = np.random.default_rng(7)
    digits = rng.integers(0, 10, size=(6, 18))
    digits[digits == 3] = 8
    spots = [(0, 4), (1, 11), (2, 2), (3, 15), (4, 7), (5, 13)]
    for r, c in spots:
        digits[r, c] = 3
    fig, axes = plt.subplots(2, 1, figsize=(9, 4.6))
    for ax, highlight, title in [(axes[0], False, "How many 3s? (count them)"),
                                 (axes[1], True, "How many 3s now?")]:
        ax.axis("off")
        ax.set_xlim(-0.5, 17.5)
        ax.set_ylim(-0.5, 5.5)
        for r in range(6):
            for c in range(18):
                v = digits[r, c]
                hot = highlight and v == 3
                ax.text(c, 5 - r, str(v), ha="center", va="center", fontsize=13,
                        color=ORANGE if hot else INK_2)
        ax.set_title(title)
    fig.tight_layout()
    save(fig, "preattentive.svg")


def analysis_types():
    rng = np.random.default_rng(11)
    days = np.clip(np.round(rng.gamma(1.6, 2.4, 400)), 0, None)
    spend = rng.uniform(5, 60, 120)
    revenue = 3.1 * spend + rng.normal(0, 18, 120)
    group = rng.choice([0, 1, 2], size=120)
    revenue_m = revenue + np.array([0, 25, -20])[group]

    fig, axes = plt.subplots(1, 3, figsize=(12, 3.8))
    a, b, c = axes
    a.hist(days, bins=np.arange(-0.5, days.max() + 1.5), color=BLUE, edgecolor=SURFACE, linewidth=1.5)
    a.set_title("Univariate: one variable")
    a.set_xlabel("Delivery days")
    a.set_ylabel("Number of orders")

    b.scatter(spend, revenue_m, s=26, color=BLUE, edgecolor=SURFACE, linewidth=0.8)
    b.set_title("Bivariate: two variables")
    b.set_xlabel("Ad spend")
    b.set_ylabel("Revenue")

    for g, col, name in [(0, BLUE, "Online"), (1, ORANGE, "Store"), (2, AQUA, "Partner")]:
        m = group == g
        c.scatter(spend[m], revenue_m[m], s=26, color=col, edgecolor=SURFACE, linewidth=0.8, label=name)
    c.set_title("Multivariate: three or more")
    c.set_xlabel("Ad spend")
    c.set_ylabel("Revenue")
    c.legend(frameon=False, fontsize=9, title="Channel", title_fontsize=9)
    fig.suptitle("Synthetic illustration: adding variables adds context",
                 x=0.01, ha="left", fontsize=13, fontweight="bold")
    fig.tight_layout()
    save(fig, "analysis-types.svg")


def cherry_pick():
    rng = np.random.default_rng(5)
    t = np.arange(60)
    sales = 130 - 0.35 * t + 10 * np.sin((t % 12 - 2) / 12 * 2 * np.pi) + rng.normal(0, 3, 60)
    sales[50] = 86.0  # March 2025: the worst month in the five years
    start, end = 50, 52
    pct = (sales[end] / sales[start] - 1) * 100
    months = pd.date_range("2021-01-01", periods=60, freq="MS")

    fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 4), gridspec_kw={"width_ratios": [1, 2.2]})
    a.plot(months[start:end + 1], sales[start:end + 1], color=ORANGE, linewidth=2.5, marker="o")
    a.set_title(f"Shown: Mar–May 2025, up {pct:.0f}%")
    a.set_ylabel("Monthly sales (synthetic)")
    a.set_xticks(months[start:end + 1], ["Mar", "Apr", "May"])

    b.plot(months, sales, color=CONTEXT, linewidth=2)
    b.plot(months[start:end + 1], sales[start:end + 1], color=ORANGE, linewidth=2.5)
    trend = np.polyval(np.polyfit(t, sales, 1), t)
    b.plot(months, trend, color=BLUE, linewidth=2, linestyle="--")
    b.text(months[2], trend[2] + 14, "Five-year trend: falling", color=BLUE, fontsize=10)
    b.set_title("Full history, 2021–2025")
    b.set_ylim(a.get_ylim()[0] - 5, max(sales) + 15)
    fig.suptitle("The same sales series, with and without a cherry-picked window",
                 x=0.01, ha="left", fontsize=13, fontweight="bold")
    fig.tight_layout()
    save(fig, "cherry-picking.svg")


def mean_median():
    salaries = [40_000] * 9 + [1_000_000]
    names = [f"Employee {i}" for i in range(1, 10)] + ["Director"]
    mean, median = np.mean(salaries), np.median(salaries)
    fig, ax = plt.subplots(figsize=(10, 4.4))
    y = np.arange(len(salaries))[::-1]
    ax.barh(y, salaries, color=[CONTEXT] * 9 + [BLUE], height=0.6)
    ax.set_yticks(y, names)
    ax.axvline(median, color=AQUA, linewidth=2)
    ax.axvline(mean, color=ORANGE, linewidth=2, linestyle="--")
    ax.text(median + 12_000, 9.2, f"Median {median:,.0f}", color=INK, fontsize=10)
    ax.text(mean + 12_000, 7.2, f"Mean {mean:,.0f}", color=INK, fontsize=10)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v / 1000:,.0f}k"))
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("Annual salary (synthetic)")
    ax.set_title("One very large value pulls the mean far above a typical salary")
    fig.tight_layout()
    save(fig, "mean-median.svg")


def base_rates():
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    for ax, (before, after, label) in zip(axes, [(1, 3, "Small branch"), (10_000, 30_000, "Whole company")]):
        ax.bar(["Last year", "This year"], [before, after], color=[CONTEXT, ORANGE], width=0.55)
        ax.set_title(f"{label}: complaints up 200%")
        ax.set_ylim(0, after * 1.2)
        ax.grid(axis="x", visible=False)
        for i, v in enumerate([before, after]):
            ax.text(i, v + after * 0.03, f"{v:,}", ha="center", fontsize=11, color=INK)
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    axes[0].set_ylabel("Number of complaints (synthetic)")
    fig.suptitle("The same percentage, very different situations",
                 x=0.01, ha="left", fontsize=13, fontweight="bold")
    fig.tight_layout()
    save(fig, "base-rates.svg")


def _plane(ax):
    body = dict(facecolor="#eceae5", edgecolor=INK_2, linewidth=1.2, zorder=1)
    ax.add_patch(matplotlib.patches.FancyBboxPatch((4.55, 0.6), 0.9, 8.6, boxstyle="round,pad=0.05,rounding_size=0.45", **body))
    ax.add_patch(matplotlib.patches.Polygon([(0.3, 5.0), (9.7, 5.0), (9.7, 5.9), (5.4, 6.8), (4.6, 6.8), (0.3, 5.9)], **body))
    ax.add_patch(matplotlib.patches.Polygon([(3.0, 1.0), (7.0, 1.0), (7.0, 1.5), (5.3, 2.1), (4.7, 2.1), (3.0, 1.5)], **body))
    engines = [(1.9, 6.1), (3.4, 6.3), (6.6, 6.3), (8.1, 6.1)]
    for x, y in engines:
        ax.add_patch(matplotlib.patches.Ellipse((x, y), 0.55, 1.2, facecolor="#dcdad4", edgecolor=INK_2, linewidth=1.2, zorder=2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")
    return engines


def survivorship():
    rng = np.random.default_rng(3)
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 5))
    engines = _plane(a)
    _plane(b)
    wing = np.c_[rng.uniform(0.6, 9.4, 40), rng.uniform(5.1, 5.8, 40)]
    wing = wing[[min(np.hypot(x - ex, y - ey) for ex, ey in engines) > 0.75 for x, y in wing]]
    body = np.c_[rng.uniform(4.7, 5.3, 18), rng.uniform(2.6, 4.6, 18)]
    tail = np.c_[rng.uniform(3.3, 6.7, 8), rng.uniform(1.1, 1.4, 8)]
    hits = np.r_[wing, body, tail]
    a.scatter(hits[:, 0], hits[:, 1], s=16, color=ORANGE, zorder=3)
    a.set_title("Hits on planes that came back")
    for x, y in engines:
        b.add_patch(matplotlib.patches.Ellipse((x, y), 0.95, 1.6, facecolor="none", edgecolor=BLUE, linewidth=2.2, zorder=3))
    b.add_patch(matplotlib.patches.Ellipse((5, 8.4), 1.5, 1.6, facecolor="none", edgecolor=BLUE, linewidth=2.2, zorder=3))
    b.set_title("Where the missing planes were probably hit")
    b.text(5, 0.1, "Engines and cockpit: almost no holes on returning planes", ha="center", fontsize=10, color=INK_2)
    fig.suptitle("Survivorship bias: the data only shows the survivors",
                 x=0.01, ha="left", fontsize=13, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.85)
    save(fig, "survivorship.svg")


if __name__ == "__main__":
    anscombe()
    datasaurus()
    ice_cream_crime()
    truncated_axis()
    berkeley()
    challenger()
    data_ink()
    gestalt()
    preattentive()
    analysis_types()
    cherry_pick()
    mean_median()
    base_rates()
    survivorship()
