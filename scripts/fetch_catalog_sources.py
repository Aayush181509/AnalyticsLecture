"""Fetch audited Tableau sample-data files into data/raw (stdlib only).

Each source is stored as data/raw/<source-id>/<version>/<original filename>.
Existing files are never overwritten: they are only re-checked against the
recorded SHA-256. A fresh download whose checksum differs from the manifest is
kept under a ".mismatch" name and reported, because the upstream file changed.

Usage:
    python3 scripts/fetch_catalog_sources.py            # fetch missing, verify all
    python3 scripts/fetch_catalog_sources.py --verify   # verify only, no network
    python3 scripts/fetch_catalog_sources.py superstore # limit to source ids
"""

from pathlib import Path
import hashlib
import sys
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
BASE = "https://public.tableau.com/app/sample-data/"
VERSION = "retrieved-2026-10-12"

# source id, original filename, bytes, sha256 (recorded at S01 audit, 2026-10-12)
SOURCES = [
    ("superstore", "sample_-_superstore.xls", 3422208,
     "5045ed4fec49cae2cc0dfc5ab0d204ba09efa767fe00c996822499e8cc42fbbd"),
    ("fifa-world-cup-results", "world_cup_results.xlsx", 193600,
     "dbad641c16c914c14fef0c95bf6f918fa5d2746671e4dc269b6a1ec3e2a3cc45"),
    ("mobile-os-usage", "mobile_os_usage.csv", 28814,
     "0db44110e84a31c06491af89a30949cd8ced1c42fac56488cb04ca4f9e449995"),
    ("startup-venture-funding", "crunchbase_monthly_export_d43b4klo2ade53.xlsx", 50993574,
     "09ebd51f6da6752012eadb1db4b66d94dfe8b41420e1427c535a4f847f7141b7"),
    ("us-construction-spending",
     "enigma-us.gov_.census.eits_.vip-97d8678900cbb89fee543a41aa21ab9a_2_0.csv", 6414502,
     "6cf9ad9f20c8eeb2c5b33d9cc29b8c648579a52ff50a24d3f6f5f1ba332b8b34"),
    ("us-home-sales",
     "enigma-us.gov_.census.eits_.ressales-e7513e56d76050c05caf638306055c98_1.csv", 2641123,
     "cc5df3053fdf6b4b732ed5a3cc10f1e389f7c7ca70b2048a53fd16454dca0be6"),
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main(argv):
    verify_only = "--verify" in argv
    wanted = {a for a in argv if not a.startswith("--")}
    unknown = wanted - {s[0] for s in SOURCES}
    if unknown:
        print(f"Unknown source id(s): {', '.join(sorted(unknown))}")
        return 2
    failures = 0
    for source_id, name, size, digest in SOURCES:
        if wanted and source_id not in wanted:
            continue
        target = RAW / source_id / VERSION / name
        if not target.exists():
            if verify_only:
                print(f"MISSING  {source_id}: {target.relative_to(ROOT)}")
                failures += 1
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            partial = target.with_name(name + ".part")
            urllib.request.urlretrieve(BASE + urllib.parse.quote(name), partial)
            if sha256(partial) != digest:
                mismatch = target.with_name(name + ".mismatch")
                partial.replace(mismatch)
                print(f"CHANGED  {source_id}: upstream differs; kept {mismatch.relative_to(ROOT)}")
                failures += 1
                continue
            partial.replace(target)
            print(f"FETCHED  {source_id}")
        actual_size, actual_digest = target.stat().st_size, sha256(target)
        if actual_size == size and actual_digest == digest:
            print(f"OK       {source_id}: {size} bytes sha256 {digest[:12]}…")
        else:
            print(f"BAD      {source_id}: {actual_size} bytes sha256 {actual_digest}")
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
