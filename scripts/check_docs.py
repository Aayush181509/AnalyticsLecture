"""Check local learner links and the docs-only publication boundary (stdlib only)."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
errors = []
pages = sorted(DOCS.rglob("*.md"))
config = (ROOT / "mkdocs.yml").read_text()
if not re.search(r"^docs_dir: docs\s*$", config, re.M):
    errors.append("mkdocs.yml must explicitly build only docs/")

for entry in DOCS.rglob("*"):
    if entry.is_symlink():
        errors.append(f"Learner source must not contain symlinks: {entry.relative_to(ROOT)}")
    if entry.is_file() and any(p in {"instructor", "planning", "solutions"} for p in entry.relative_to(DOCS).parts):
        errors.append(f"Internal content directory inside learner source: {entry.relative_to(ROOT)}")

for page in pages:
    content = page.read_text()
    # Ignore code examples. This intentionally checks inline Markdown links/images,
    # not remote URLs, anchor existence, or every possible HTML/reference-link syntax.
    content = re.sub(r"^```.*?^```[^\n]*$", "", content, flags=re.M | re.S)
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", content):
        target = target.strip().split(' "', 1)[0].strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        resolved = (page.parent / unquote(parsed.path)).resolve()
        if DOCS.resolve() not in (resolved, *resolved.parents):
            errors.append(f"Link leaves learner source: {page.relative_to(ROOT)} -> {target}")
        elif not resolved.exists():
            errors.append(f"Missing local target: {page.relative_to(ROOT)} -> {target}")

for target in re.findall(r":\s*([\w/.-]+\.md)\s*$", config, flags=re.M):
    if not (DOCS / target).is_file():
        errors.append(f"Navigation target missing: {target}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(pages)} learner Markdown pages; local inline links, nav targets, and docs boundary checked.")
print("Remote links, fragment anchors, reference links, rendered layout, and Tableau/data correctness require separate review.")
