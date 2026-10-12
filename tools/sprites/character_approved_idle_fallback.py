"""Fallback role identity from an existing strict-DONE IDLE sprite.

This is ONLY a source for *new* GPU regeneration when fresh text-to-image
anchors fail repeatedly. It never returns a valid review decision, never
changes the manifest, never updates runtime resources and cannot invent an
unreviewed engineer IDLE. Source pixels must pass full-body and isolation QA
in the caller before use.
"""
from __future__ import annotations

import re
from pathlib import Path
from PIL import Image

_ALLOWED = {"OP", "LOG", "TECH"}
_ITEM = re.compile(r"^\|\s*(CHR-(?:OP|LOG|TECH)-IDLE)\s*\|")


def load_approved_idle_anchor(
    role: str, manifest: Path, sprite_dir: Path
) -> tuple[Image.Image | None, str]:
    """Return a neutral 1024x1024 RGB seed or a specific rejection reason."""
    role = role.upper()
    if role not in _ALLOWED:
        return None, "role-not-eligible-for-existing-idle-fallback"
    source_id = f"CHR-{role}-IDLE"
    if not manifest.is_file():
        return None, "manifest-not-found"
    statuses = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if _ITEM.match(line) and line.split("|")[1].strip() == source_id:
            statuses.append(line.split("|")[-2].strip().upper())
    if statuses != ["DONE"]:
        return None, "source-idle-not-uniquely-strict-done"
    filename = sprite_dir / f"zte_chr_{role.lower()}_idle_final.png"
    if not filename.is_file():
        return None, "strict-done-idle-source-missing"
    try:
        with Image.open(filename) as src:
            if src.size != (1024, 1024):
                return None, "strict-done-idle-invalid-atlas-size"
            frame = src.convert("RGBA").crop((0, 0, 256, 256))
    except (OSError, ValueError):
        return None, "strict-done-idle-image-corrupt"
    alpha = frame.getchannel("A").point(lambda a: 255 if a >= 64 else 0)
    bbox = alpha.getbbox()
    if bbox is None:
        return None, "strict-done-idle-first-cell-empty"
    # Reject a pair of separate foreground people, even if combined bbox
    # is still tall. A large secondary connected alpha component cannot be
    # treated as an approved single-character identity anchor.
    foreground = alpha.load()
    visited: set[tuple[int, int]] = set()
    components: list[int] = []
    for yy in range(256):
        for xx in range(256):
            if foreground[xx, yy] == 0 or (xx, yy) in visited:
                continue
            stack = [(xx, yy)]
            visited.add((xx, yy))
            area = 0
            while stack:
                cx, cy = stack.pop()
                area += 1
                for nx, ny in ((cx - 1, cy), (cx + 1, cy),
                               (cx, cy - 1), (cx, cy + 1)):
                    if (0 <= nx < 256 and 0 <= ny < 256
                            and foreground[nx, ny] > 0 and (nx, ny) not in visited):
                        visited.add((nx, ny))
                        stack.append((nx, ny))
            components.append(area)
    components.sort(reverse=True)
    if len(components) > 1 and components[1] > max(150, .12 * components[0]):
        return None, "strict-done-idle-multiple-foreground-people"
    x0, y0, x1, y1 = bbox
    width, height = x1 - x0, y1 - y0
    if height < 125 or width < 25 or width / height > 0.90:
        return None, "strict-done-idle-not-tall-single-subject"
    # Use the original, already-approved character pixels. Rescale without
    # re-generating the face or drawing a new helmet/costume.
    crop = frame.crop(bbox)
    desired_height = 770
    desired_width = round(width * desired_height / height)
    if desired_width > 640 or desired_width < 70:
        return None, "strict-done-idle-suspicious-proportions"
    resized = crop.resize((desired_width, desired_height), Image.Resampling.LANCZOS)
    background = Image.new("RGB", (1024, 1024), (139, 139, 139))
    target_x = (1024 - desired_width) // 2
    target_y = (1024 - desired_height) // 2
    background.paste(resized.convert("RGB"), (target_x, target_y),
                     resized.getchannel("A"))
    return background, f"existing-reviewed-{source_id}-visual-reference-only"
