"""Fail if a private expected value appears on a Tableau learner page."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
answers = sorted((ROOT / "instructor/tableau").glob("T*/answers.md"))
if not answers:
    print("SKIP: no private answers on this machine")
    sys.exit(0)
values = {m.group(2).strip() for a in answers
          for m in re.finditer(r"^KEY: (\S+) = (.+)$", a.read_text(), re.M)}
values = {v for v in values if len(v) >= 4}  # ignore tiny numbers like "4"
hits = [(p.name, v) for p in (ROOT / "docs/tableau").glob("*.md")
        for v in values if v in p.read_text()]
for name, v in hits:
    print(f"LEAK: {v} on {name}")
print("PASS" if not hits else f"FAIL: {len(hits)} leak(s)")
sys.exit(1 if hits else 0)
