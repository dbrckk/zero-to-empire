"""Review-only sprites preserved when IDLE generation fails.

Rejected frames are never written to the incoming candidate directory.
They are strictly forensic evidence for the next GPU retry and manual QA.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from PIL import Image

IDLE_ID = re.compile(r"^CHR-(OP|TECH|LOG|ENG)-IDLE$")
CELL = 256


def save_rejected_idle_preview(
    frames: list[Image.Image],
    asset_id: str,
    reason: str,
    output_directory: Path,
) -> tuple[Path, Path] | None:
    """Write unapproved frames and a provenance-readable rejection record."""
    if not IDLE_ID.fullmatch(asset_id) or not frames:
        return None
    if len(frames) > 6 or any(frame.size != (CELL, CELL) for frame in frames):
        raise ValueError("Invalid rejected IDLE frame dimensions or count")
    root = Path(output_directory)
    root.mkdir(parents=True, exist_ok=True)
    atlas = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
    for index, frame in enumerate(frames):
        atlas.alpha_composite(frame.convert("RGBA"),
                              ((index % 4) * CELL, (index // 4) * CELL))
    stem = asset_id.lower().replace("-", "_")
    image_path = root / f"{stem}_rejected_review_only.png"
    report_path = root / f"{stem}_rejected_review_only.json"
    atlas.save(image_path, "PNG", optimize=True)
    report_path.write_text(
        json.dumps({
            "id": asset_id,
            "status": "REJECTED",
            "reason": str(reason),
            "visible_frames": len(frames),
            "expected_frames": 6,
            "review_only": True,
            "strict_promotion_permitted": False,
            "technical_or_semantic_approval": False,
        }, indent=2) + "\n",
        encoding="utf-8",
    )
    return image_path, report_path
