"""Acquire the four catalog-linked audit samples without overwriting originals.

Uses curl's normal TLS verification. Run once for acquisition; profiling and
integrity verification are separate offline operations. No file is published.
"""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = "2026-10-12"
CATALOG = "https://public.tableau.com/app/learn/sample-data"
BASE = "https://public.tableau.com/app/sample-data/"
SOURCES = [
    ("eu-superstore", "EU Superstore Sales", "sample_-_superstore.xls"),
    ("world-cup-results", "FIFA World Cup Match Results", "world_cup_results.xlsx"),
    ("mobile-os-usage", "Mobile OS Usage", "mobile_os_usage.csv"),
    ("us-construction", "US Construction Spending", "enigma-us.gov_.census.eits_.vip-97d8678900cbb89fee543a41aa21ab9a_2_0.csv"),
]
PROVENANCE = {
    "eu-superstore": {"provider": "Tableau", "upstream_url": CATALOG,
                      "data_character": "fictitious sample; catalog EU label differs from file geography"},
    "world-cup-results": {"provider": "Sports Viz Sundays 2018 on data.world; mirrored by Tableau",
                          "upstream_url": "https://data.world/sportsvizsunday/sports-viz-sundays-2018/workspace/file?filename=World+Cup+Results.xlsx",
                          "data_character": "historical match compilation; source values not independently verified"},
    "mobile-os-usage": {"provider": "Statcounter Global Stats; mirrored by Tableau",
                        "upstream_url": "https://gs.statcounter.com/#mobile_os-ww-monthly-200812-201412",
                        "data_character": "usage statistics; file dates incomplete, exact historical scope unresolved"},
    "us-construction": {"provider": "US Census / Department of Commerce via Enigma; mirrored by Tableau",
                        "upstream_url": None,
                        "upstream_status": "Exact original Enigma dataset/version unresolved; see source-rights record",
                        "provider_reference_url": "https://www.census.gov/construction/c30/historical_data.html",
                        "data_character": "historical economic statistics; exact mirror vintage unresolved"},
}


def check_signature(path):
    prefix = path.read_bytes()[:256]
    if path.suffix == ".xls":
        return prefix.startswith(bytes.fromhex("d0cf11e0a1b11ae1"))
    if path.suffix == ".xlsx":
        return prefix.startswith(b"PK")
    return bool(prefix) and not prefix.lstrip().lower().startswith((b"<", b"{"))


def main():
    meta = ROOT / "data/metadata/catalog-audit-2026-10-12"
    meta.mkdir(parents=True, exist_ok=True)
    manifest_path = meta / "source_manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        for record in manifest["sources"]:
            if record["status"] != "downloaded":
                continue
            path = ROOT / record["path"]
            assert hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"], path
        print("Existing acquisition manifest retained; downloaded original hashes match.")
        return
    records = []
    for source_id, title, filename in SOURCES:
        directory = ROOT / "data/raw" / source_id / VERSION
        directory.mkdir(parents=True, exist_ok=True)
        destination = directory / filename
        if destination.exists():
            raise SystemExit(f"Original exists without manifest; inspect rather than overwrite: {destination}")
        record = {"source_id": source_id, "title": title, "catalog_url": CATALOG,
                  "download_url": BASE + filename, "source_version": VERSION,
                  "path": str(destination.relative_to(ROOT)), "status": "not_downloaded",
                  "publication_approved": False, "rights_status": "see planning/SOURCE_RIGHTS.md"}
        record.update(PROVENANCE[source_id])
        record["rights_checked_date"] = VERSION
        with tempfile.TemporaryDirectory(prefix="catalog-acquire-") as temporary:
            temporary_path = Path(temporary) / filename
            result = subprocess.run([
                "curl", "--fail", "--location", "--silent", "--show-error",
                "--max-time", "45", "--retry", "1", "--max-filesize", "20000000",
                "--output", str(temporary_path), "--write-out",
                "%{http_code}\n%{content_type}\n%{url_effective}\n", record["download_url"],
            ], capture_output=True, text=True)
            record["retrieved_at_utc"] = datetime.now(timezone.utc).isoformat()
            record["response"] = result.stdout.strip().splitlines()
            if result.returncode or not temporary_path.exists() or not check_signature(temporary_path):
                record["status"] = "failed"
                record["error"] = result.stderr.strip() or "Unexpected data-file signature"
            else:
                content = temporary_path.read_bytes()
                with destination.open("xb") as output:
                    output.write(content)
                record.update(status="downloaded", bytes=len(content), sha256=hashlib.sha256(content).hexdigest())
        records.append(record)
        print(source_id, record["status"], record.get("bytes", ""))
    manifest = {"catalog_url": CATALOG, "audit_date": VERSION,
                "purpose": "Local course source audit; not learner publication", "sources": records}
    with manifest_path.open("x") as output:
        json.dump(manifest, output, indent=2)
        output.write("\n")


if __name__ == "__main__":
    main()
