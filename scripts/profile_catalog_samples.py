"""Offline audit of the four exact files in the acquisition manifest.

Raw files are read only. Writes schema/quality metadata and private numerical
controls, never prepared learner data. Unexpected hashes or audit invariants
stop the run. This checks the observed snapshot, not upstream truth or Tableau.
"""

from decimal import Decimal
import hashlib
import json
from pathlib import Path
import platform

import openpyxl
import pandas as pd
import xlrd

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "data/metadata/catalog-audit-2026-10-12"


def schema(frame):
    return {
        "rows": len(frame), "columns": len(frame.columns),
        "exact_duplicate_rows": int(frame.duplicated().sum()),
        "fields": [{"name": str(name), "inferred_type": str(frame[name].dtype),
                    "missing": int(frame[name].isna().sum()),
                    "distinct_nonmissing": int(frame[name].nunique())}
                   for name in frame.columns],
    }


def date_scope(values):
    parsed = pd.to_datetime(values, errors="coerce")
    return {"min": str(parsed.min().date()), "max": str(parsed.max().date()),
            "missing_or_invalid": int(parsed.isna().sum()),
            "distinct": int(parsed.nunique())}


def total(values):
    # Sum stored numeric representations without rounding each source row.
    return str(sum((Decimal(str(v)) for v in values), Decimal(0)))


def retail(tables):
    orders, people, returns = (tables[s] for s in ("Orders", "People", "Returns"))
    customer_counts = orders.groupby("Order ID")["Customer ID"].nunique()
    conflicts = customer_counts[customer_counts > 1].index.tolist()
    assert orders["Row ID"].is_unique and orders["Row ID"].notna().all()
    assert returns["Order ID"].is_unique and people["Region"].is_unique
    assert set(returns["Order ID"]) <= set(orders["Order ID"])
    assert set(orders["Region"]) <= set(people["Region"])
    assert not (orders["Ship Date"] < orders["Order Date"]).any()
    quality = {
        "grain": "source order line; key Row ID",
        "distinct_orders": int(orders["Order ID"].nunique()),
        "duplicate_order_product_pairs": int(orders.duplicated(["Order ID", "Product ID"]).sum()),
        "countries_rows": orders["Country/Region"].value_counts().to_dict(),
        "order_dates": date_scope(orders["Order Date"]),
        "ship_dates": date_scope(orders["Ship Date"]),
        "order_customer_conflicts": conflicts,
        "returned_values": sorted(returns["Returned"].unique().tolist()),
        "ranges": {name: {"min": float(orders[name].min()), "max": float(orders[name].max())}
                   for name in ("Sales", "Profit", "Discount", "Quantity")},
        "order_attribute_conflicts": {
            name: int((orders.groupby("Order ID")[name].nunique(dropna=False) > 1).sum())
            for name in ("Order Date", "Ship Date", "Ship Mode", "Segment", "Country/Region", "Region")},
    }
    scoped = orders[orders["Order Date"].between("2023-01-01", "2025-12-31")]
    controls = {}
    for label, frame in (("all_source_rows", orders), ("proposed_complete_years_2023_2025", scoped)):
        controls[label] = {"rows": len(frame), "orders": int(frame["Order ID"].nunique()),
                           "reported_sales": total(frame["Sales"]),
                           "reported_profit": total(frame["Profit"]),
                           "quantity": int(frame["Quantity"].sum()),
                           "returned_orders_flagged": int(frame.loc[frame["Order ID"].isin(returns["Order ID"]), "Order ID"].nunique()),
                           "segments": {name: {"rows": len(group), "orders": int(group["Order ID"].nunique()),
                                              "reported_sales": total(group["Sales"]), "reported_profit": total(group["Profit"])}
                                        for name, group in frame.groupby("Segment")}}
    assert quality["distinct_orders"] == 5111 and len(conflicts) == 2
    return quality, controls


def sports(tables):
    matches, appearances, tournaments = (tables[s] for s in
        ("WorldCupMatches", "World Cup - Tableau format", "WorldCups"))
    clean = matches.drop_duplicates()
    assert not clean.duplicated(["Date", "HomeTeam", "AwayTeam"]).any()
    assert tournaments["Year"].is_unique
    yearly = clean.groupby("Year").agg(matches=("Year", "size"), home_goals=("HomeGoals", "sum"), away_goals=("AwayGoals", "sum"))
    check = yearly.join(tournaments.set_index("Year")[["MatchesPlayed", "GoalsScored"]], how="outer")
    check["match_count_residual"] = check["matches"] - check["MatchesPlayed"]
    check["goal_total_residual"] = check["home_goals"] + check["away_goals"] - check["GoalsScored"]
    assert len(clean) == 836 and len(matches) - len(clean) == 16
    assert (check["match_count_residual"] == 0).all()
    assert (check["goal_total_residual"] == 0).all()
    assert (appearances.groupby("Game #").size() == 2).all()
    quality = {"grain": "match in WorldCupMatches; team appearance in Tableau-format sheet",
               "match_dates": date_scope(matches["Date"]),
               "raw_matches_by_year": {str(k): int(v) for k, v in matches.groupby("Year").size().items()},
               "deduplicated_matches": len(clean),
               "duplicate_match_keys_raw": int(matches.duplicated(["Date", "HomeTeam", "AwayTeam"]).sum()),
               "appearance_game_ids": int(appearances["Game #"].nunique()),
               "duplicate_game_team_keys": int(appearances.duplicated(["Game #", "Team"]).sum()),
               "blank_observation_after_trim": int(matches["Observation"].fillna("").str.strip().eq("").sum()),
               "goals_missing": int(matches[["HomeGoals", "AwayGoals"]].isna().sum().sum()),
               "attendance_storage_types": tournaments["Attendance"].map(lambda v: type(v).__name__).value_counts().to_dict(),
               "goal_reconciliation_exceptions": check.loc[check["goal_total_residual"] != 0].reset_index().to_dict("records")}
    return quality, {"after_exact_dedup_by_year": check.reset_index().to_dict("records")}


def technology(frame):
    parsed = pd.to_datetime(frame["Date"], errors="coerce")
    dated = frame.loc[parsed.notna()].copy()
    dated["Date"] = parsed.loc[parsed.notna()]
    grouped = dated.groupby("Date")["Percent of Usage"].agg(["size", "sum"])
    periods = {str(k.date()): {"rows": int(row["size"]), "sum_percentage_points": float(row["sum"])}
               for k, row in grouped.iterrows()}
    assert len(frame) == 1898 and parsed.isna().sum() == 1772
    assert not dated.duplicated(["Date", "Mobile Operating System"]).any()
    quality = {"grain": "OS-period share where Date is present; undated records unresolved",
               "dates": date_scope(frame["Date"]), "dated_rows": len(dated),
               "os_categories": sorted(frame["Mobile Operating System"].unique().tolist()),
               "dated_periods": periods, "share_min": float(frame["Percent of Usage"].min()),
               "share_max": float(frame["Percent of Usage"].max()),
               "eligible_four_month_rows": int(dated[dated["Date"] < "2009-04-01"].shape[0])}
    return quality, {"dated_periods_only": periods}


def government(frame):
    key = ["per_idx", "cat_idx", "dt_idx", "et_idx", "geo_idx", "is_adj"]
    assert frame[key].notna().all().all()
    assert not frame.duplicated(key).any() and frame["serialid"].is_unique
    monthly = frame[(frame["cat_code"] == "XXXX") & (frame["dt_code"] == "T") &
                    (frame["et_idx"] == 0) & (frame["geo_code"] == "US") & (frame["is_adj"] == 0)]
    assert len(monthly) == 177 and monthly["val"].notna().all() and monthly["per_name"].is_unique
    assert set(monthly["dt_unit"]) == {"MLN$"}
    amounts = frame[(frame["et_idx"] == 0) & (frame["is_adj"] == 0) & frame["dt_code"].isin(["T", "V", "P"])]
    ownership = amounts[amounts["cat_code"] == "XXXX"].pivot(index="per_name", columns="dt_code", values="val")
    ownership_residual = ownership["T"] - ownership["V"] - ownership["P"]
    types = amounts[amounts["dt_code"] == "T"].pivot(index="per_name", columns="cat_code", values="val")
    type_residual = types["XXXX"] - types["00XX"] - types["NRXX"]
    blocks = (frame.assign(has_value=frame["val"].notna()).groupby(
        ["is_adj", "dt_code", "et_code", "dt_unit"], dropna=False)["has_value"].agg(["size", "sum"]).reset_index())
    quality = {"grain": "period-category-data type-error type-geography-adjustment record",
               "candidate_key": key, "dates": date_scope(frame["per_name"]),
               "missing_values": int(frame["val"].isna().sum()),
               "category_codes": sorted(frame["cat_code"].unique().tolist()),
               "data_types": frame[["dt_idx", "dt_code", "dt_desc", "dt_unit"]].drop_duplicates().fillna("<missing>").to_dict("records"),
               "error_types": frame[["et_idx", "et_code", "et_desc", "et_unit"]].drop_duplicates().fillna("<missing>").to_dict("records"),
               "geographies": frame[["geo_code", "geo_desc"]].drop_duplicates().to_dict("records"),
               "value_blocks": blocks.fillna("<missing>").to_dict("records"),
               "beginner_monthly_total_rows": len(monthly),
               "max_abs_total_minus_private_public_million_dollars": float(ownership_residual.abs().max()),
               "max_abs_total_minus_residential_nonresidential_million_dollars": float(type_residual.abs().max())}
    return quality, {"proposed_unadjusted_monthly_total": {"rows": len(monthly), "sum_million_dollars": total(monthly["val"]),
                        "first_five": monthly.sort_values("per_name")[["per_name", "val"]].head().to_dict("records")},
                     "ownership_residual_max_abs": float(ownership_residual.abs().max()),
                     "type_residual_max_abs": float(type_residual.abs().max())}


def main():
    manifest = json.loads((META / "source_manifest.json").read_text())
    profiles, controls = [], {}
    for record in manifest["sources"]:
        path = ROOT / record["path"]
        assert record["status"] == "downloaded"
        assert path.stat().st_size == record["bytes"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"], path
        if path.suffix in (".xls", ".xlsx"):
            tables = pd.read_excel(path, sheet_name=None)
        else:
            tables = {"CSV": pd.read_csv(path, low_memory=False)}
        source_id = record["source_id"]
        if source_id == "eu-superstore":
            quality, reference = retail(tables)
        elif source_id == "world-cup-results":
            quality, reference = sports(tables)
        elif source_id == "mobile-os-usage":
            quality, reference = technology(tables["CSV"])
        elif source_id == "us-construction":
            quality, reference = government(tables["CSV"])
        else:
            raise ValueError(f"Source is outside this four-file audit: {source_id}")
        profiles.append({"source_id": source_id, "path": record["path"], "sha256": record["sha256"],
                         "tables": {name: schema(frame) for name, frame in tables.items()}, "quality": quality})
        controls[source_id] = reference
        print(f"PROFILED {source_id}: " + ", ".join(f"{name}={len(frame)} rows" for name, frame in tables.items()))
    environment = {"python": platform.python_version(), "pandas": pd.__version__,
                   "openpyxl": openpyxl.__version__, "xlrd": xlrd.__version__}
    (META / "profiles.json").write_text(json.dumps({"environment": environment, "sources": profiles}, indent=2, allow_nan=False) + "\n")
    private = ROOT / "instructor/source-audit"
    private.mkdir(parents=True, exist_ok=True)
    (private / "catalog-2026-10-12-controls.json").write_text(json.dumps(
        {"scope": "Source inspection controls, not released lesson answers; no Tableau cross-check", "environment": environment,
         "sources": controls}, indent=2, allow_nan=False) + "\n")
    print("PASS hashes, keys and snapshot invariants; metadata/private controls written. Raw files unchanged.")


if __name__ == "__main__":
    main()
