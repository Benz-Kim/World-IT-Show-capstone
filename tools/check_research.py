"""Check local Markdown links and source IDs without third-party dependencies."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
for file in ROOT.rglob("*.md"):
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", file.read_text()):
        if "://" in target or target.startswith(("#", "mailto:")):
            continue
        path = target.split("#", 1)[0]
        if path and not (file.parent / path).exists():
            errors.append(f"{file.relative_to(ROOT)}: missing {path}")
register = (ROOT / "evidence/source-register.md").read_text()
source_ids = set(re.findall(r"\| ([WVT]\d{2}) \|", register))
with (ROOT / "evidence/claim-ledger.csv").open(newline="") as stream:
    rows = list(csv.DictReader(stream))
seen = set()
for row in rows:
    if row["claim_id"] in seen:
        errors.append(f"duplicate claim: {row['claim_id']}")
    seen.add(row["claim_id"])
    for source in row["source_ids"].split("|"):
        if source not in source_ids:
            errors.append(f"{row['claim_id']}: unknown source {source}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: local links, {len(rows)} claims and {len(source_ids)} source IDs")
