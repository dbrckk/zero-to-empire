"""Conservative cleanup of neutral gray ground-shadow pixels in character cells.

Never manufactures missing geometry, guesses limb positions, or approves a
sprite. Only apply when a broad bright neutral shadow extends visibly past
both lower legs. Dark/colored shadows stay for semantic review.
"""
from __future__ import annotations

from PIL import Image

CELL_SIZE = (256, 256)


def remove_baked_ground_shadow(frame: Image.Image) -> tuple[Image.Image, int]:
    """Return cleaned RGBA frame and the count of discarded gray pixels.

    A long, near-neutral cast shadow on a light gray AI generation background
    sometimes fuses to the boots in alpha. An outside-of-leg evidence check
    protects pale shoe materials from indiscriminate deletion.
    """
    rgba = frame.convert("RGBA")
    if rgba.size != CELL_SIZE:
        return rgba, 0
    bounds = rgba.getchannel("A").getbbox()
    if not bounds:
        return rgba, 0
    left, top, right, bottom = bounds
    height = bottom - top
    if height < 120:
        return rgba, 0

    # Knee-level silhouette estimates where the feet can legitimately extend.
    knee_y = max(0, min(255, top + round(.79 * height)))
    knee_xs = [
        x for x in range(256)
        if rgba.getpixel((x, knee_y))[3] >= 96
    ]
    if len(knee_xs) < 15:
        return rgba, 0
    knee_left, knee_right = min(knee_xs), max(knee_xs)
    start = max(0, bottom - round(.13 * height))

    candidates = []
    outside = 0
    pixels = rgba.load()
    for y in range(start, bottom):
        for x in range(left, right):
            r, g, b, alpha = pixels[x, y]
            # Shadows seen in failed ENG/OP assets are flat neutral gray,
            # unlike the dark textured shoes, coat and bright safety colors.
            if alpha < 32 or min(r, g, b) < 155 or max(r, g, b) - min(r, g, b) > 16:
                continue
            candidates.append((x, y))
            if x < knee_left - 13 or x > knee_right + 13:
                outside += 1

    # Don't alter white shoes, light trousers or ordinary pale details that
    # stay inside the limb envelope. Ambiguous cases remain for manual review.
    if outside < 30:
        return rgba, 0
    for x, y in candidates:
        pixels[x, y] = (0, 0, 0, 0)
    return rgba, len(candidates)
