#!/usr/bin/env python3
"""Build deterministic production lanes from the canonical AAA sprite manifest.

The planner is generation-backend agnostic. It groups remaining assets by the
cheapest safe production path and, critically, treats already-materialized art
as integration work even when the human ledger is stale.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
INCOMING = ROOT / "art/incoming/final-sprites"
OUT = ROOT / "art/production"
ROW = re.compile(
    r"^\|\s*(?P<id>[^|]+?)\s*\|\s*(?P<asset>[^|]+?)\s*\|\s*(?P<description>[^|]+?)\s*\|\s*`(?P<runtime>[^`]+)`\s*\|\s*(?P<status>TODO|ART|CLEAN|RUNTIME|DONE|BLOCKED)\s*\|$"
)

BATCH_SIZE = {
    "procedural-fx": 18,
    "procedural-terrain": 14,
    "gpu-static": 12,
    "gpu-animation": 4,
    "integration-only": 32,
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
    materialized: bool


def is_materialized(runtime: str) -> bool:
    runtime_path = ROOT / runtime
    stem = Path(runtime).stem
    candidate = INCOMING / f"{stem}.png"
    return runtime_path.exists() or candidate.exists()


def classify(asset_id: str, description: str, status: str, runtime: str, materialized: bool) -> str:
    if status == "BLOCKED":
        return "blocked"
    if materialized or status in {"ART", "CLEAN", "RUNTIME"}:
        return "integration-only"

    aid = asset_id.upper()
    text = f"{description} {runtime}".lower()
    if aid.startswith("FX-"):
        return "procedural-fx"
    if aid.startswith("TER-"):
        return "procedural-terrain"
    if aid.startswith("CHR-") or any(k in text for k in ("sheet", "frames", "cycle", "walk", "idle", "animation", "animated")):
        return "gpu-animation"
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
        materialized = is_materialized(d["runtime"])
        rows.append(Asset(**d, materialized=materialized, lane=classify(d["id"], d["description"], d["status"], d["runtime"], materialized)))

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
        "materialized_remaining": sum(a.materialized for a in remaining),
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
    (OUT / "sprite_batch_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = [
        "# Sprite production batch plan", "",
        f"- Manifest: **{plan['manifest_total']}**",
        f"- DONE: **{plan['done']}**",
        f"- Remaining: **{plan['remaining']}**",
        f"- Already materialized but not DONE: **{plan['materialized_remaining']}**",
        "", "| Lane | Assets | Batch size | Batches |", "|---|---:|---:|---:|",
    ]
    for lane, info in plan["lanes"].items():
        md.append(f"| {lane} | {info['count']} | {info['batch_size']} | {len(info['batches'])} |")
    md += ["", "## Next batches", ""]
    for lane, info in plan["lanes"].items():
        if info["batches"]:
            md.append(f"- **{lane}:** " + ", ".join(a["id"] for a in info["batches"][0]))
    (OUT / "sprite_batch_plan.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps({
        "done": plan["done"],
        "remaining": plan["remaining"],
        "materialized_remaining": plan["materialized_remaining"],
        "lane_counts": {k: v["count"] for k, v in plan["lanes"].items()},
        "batch_counts": {k: len(v["batches"]) for k, v in plan["lanes"].items()},
    }, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
