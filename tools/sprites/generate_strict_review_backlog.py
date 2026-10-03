#!/usr/bin/env python3
"""Generate the strict character review backlog from the canonical master queue."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MASTER = ROOT / "art/production/master-asset-queue.json"
OUT = ROOT / "art/production/character-strict-review-backlog.md"


def main() -> int:
    queue = json.loads(MASTER.read_text(encoding="utf-8"))
    remaining = [a for a in queue["assets"] if a.get("strict_status") != "DONE" and a["id"].startswith("CHR-")]
    strict_done = sum(a.get("strict_status") == "DONE" for a in queue["assets"])
    production = sum(
        a.get("strict_status") == "DONE"
        or a.get("pipeline_status") in {"AWAITING_REVIEW", "CANDIDATE", "TECHNICAL_PASS", "VALIDATED", "APPROVED", "RUNTIME_READY", "DONE"}
        for a in queue["assets"]
    )
    lines = [
        "# Character strict-review backlog", "",
        "Generated from `art/production/master-asset-queue.json` after production completion.", "",
        f"- Production processed: **{production}/{queue['target_total']}**",
        f"- Strict DONE: **{strict_done}/{queue['target_total']}**",
        f"- Semantic review remaining: **{len(remaining)}**",
        "- This report does **not** grant strict approval or runtime promotion.", "",
        "| Asset | Role | Action | Technical status | Review note |",
        "|---|---|---|---|---|",
    ]
    for asset in remaining:
        parts = asset["id"].split("-")
        reason = asset.get("review_reason") or "Semantic review required; no specific automated defect recorded."
        lines.append(f"| {asset['id']} | {parts[1]} | {'-'.join(parts[2:])} | {asset['pipeline_status']} | {reason.replace('|', '/')} |")
    lines += ["", "## Review rule", "",
        "A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.",
    ]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"STRICT_REVIEW_BACKLOG={len(remaining)} STRICT_DONE={strict_done}/{queue['target_total']} PRODUCTION={production}/{queue['target_total']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
