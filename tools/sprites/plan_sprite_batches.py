#!/usr/bin/env python3
"""Build deterministic production lanes from the canonical AAA sprite manifest.

The planner is deliberately generation-backend agnostic. It prevents the project
from falling back to one-asset-at-a-time orchestration by grouping remaining
assets according to the cheapest safe production path.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
OUT = ROOT / "art/production"
ROW = re.compile(
    r"^\|\s*(?P<id>[^|]+?)\s*\|\s*(?P<asset>[^|]+?)\s*\|\s*(?P<description>[^|]+?)\s*\|\s*`(?P<runtime>[^`]+)`\s*\|\s*(?P<status>TODO|ART|CLEAN|RUNTIME|DONE|BLOCKED)\s*\|$"
)

# Batch sizes are intentionally asymmetric: CPU/procedural work is cheap, static
# GPU candidates can be produced moderately wide, while animated sheets remain
# small so semantic inspection does not become the next bottleneck.
BATCH_SIZE = {
    "procedural": 16,
    "gpu-static": 8,
    "gpu-animation": 4,
    "integration-only": 24,
    "blocked": 24,
}

@dataclass(frozen=True)
class Asset:
    id: str
    asset: str
    description: str
    runtime: str
    status: str
    lane: str


def classify(asset_id: str, description: str, status: str, runtime: str) -> str:
    if status == "BLOCKED":
        return "blocked"
    if status in {"ART", "CLEAN", "RUNTIME"}:
        # Already paid the expensive authoring cost; prioritize integration/CI.
        return "integration-only"

    aid = asset_id.upper()
    text = f"{description} {runtime}".lower()

    # Small VFX are the safest lane for deterministic procedural authoring.
    if aid.startswith("FX-"):
        return "procedural"

    # Character pose/cycle sheets and anything explicitly animated require a
    # dedicated animation-aware path. Do not fake these from one static master.
    if aid.startswith("CHR-") or any(k in text for k in ("sheet", "frames", "cycle", "walk", "idle", "animation", "animated")):
        return "gpu-animation"

    # Buildings, vehicles, props, terrain and static machinery can share the
    # isolated-object GPU lane, with category-specific prompts/normalization.
    return "gpu-static"


def chunks(items: list[Asset], n: int) -> list[list[Asset]]:
    return [items[i:i+n] for i in range(0, len(items), n)]


def main() -> int:
    rows: list[Asset] = []
    for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
        m = ROW.match(raw.strip())
        if not m:
            continue
        d = m.groupdict()
        rows.append(Asset(**d, lane=classify(d["id"], d["description"], d["status"], d["runtime"])))

    if len(rows) != 235:
        raise SystemExit(f"Manifest parsing safety check failed: expected 235 rows, got {len(rows)}")

    remaining = [a for a in rows if a.status != "DONE"]
    lanes: dict[str, list[Asset]] = {name: [] for name in BATCH_SIZE}
    for asset in remaining:
        lanes[asset.lane].append(asset)

    plan = {
        "manifest_total": len(rows),
        "done": len(rows) - len(remaining),
        "remaining": len(remaining),
        "lanes": {},
    }
    for lane, assets in lanes.items():
        batches = chunks(assets, BATCH_SIZE[lane])
        plan["lanes"][lane] = {
            "count": len(assets),
            "batch_size": BATCH_SIZE[lane],
            "batches": [[asdict(a) for a in batch] for batch in batches],
        }

    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "sprite_batch_plan.json"
    json_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = [
        "# Sprite production batch plan",
        "",
        f"- Manifest: **{plan['manifest_total']}**",
        f"- DONE: **{plan['done']}**",
        f"- Remaining: **{plan['remaining']}**",
        "",
        "| Lane | Assets | Batch size | Batches |",
        "|---|---:|---:|---:|",
    ]
    for lane, info in plan["lanes"].items():
        md.append(f"| {lane} | {info['count']} | {info['batch_size']} | {len(info['batches'])} |")
    md += ["", "## Next batches", ""]
    for lane, info in plan["lanes"].items():
        if not info["batches"]:
            continue
        ids = ", ".join(a["id"] for a in info["batches"][0])
        md.append(f"- **{lane}:** {ids}")
    (OUT / "sprite_batch_plan.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps({
        "done": plan["done"],
        "remaining": plan["remaining"],
        "lane_counts": {k: v["count"] for k, v in plan["lanes"].items()},
        "batch_counts": {k: len(v["batches"]) for k, v in plan["lanes"].items()},
    }, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
