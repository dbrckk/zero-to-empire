"""Conservative cleanup of neutral gray ground-shadow pixels in character cells.

Never manufactures missing geometry, guesses limb positions, or approves a
sprite. Only apply when a broad bright neutral shadow extends visibly past
both lower legs. Dark/colored shadows stay for semantic review.
"""
from __future__ import annotations

from collections import deque
from PIL import Image

CELL_SIZE = (256, 256)


def _remove_foot_gap_background(rgba: Image.Image) -> int:
    """Clear only confidently missegmented neutral background between boots.

    An AI-generated gray cast shadow can connect both boots and prevent the
    border flood-fill from reaching the open space between two lower legs.
    Resolve that gap from two separately visible feet in the final rows.
    No limb, boot or colored uniform pixel may be synthesized or repainted.
    """
    bounds = rgba.getchannel("A").getbbox()
    if not bounds:
        return 0
    left, top, right, bottom = bounds
    height = bottom - top
    if height < 120:
        return 0
    pixels = rgba.load()
    feet = None
    for y in range(bottom - 3, max(top, bottom - 11), -1):
        xs = [x for x in range(left, right) if pixels[x, y][3] >= 120]
        if not xs:
            continue
        runs = []
        start = previous = xs[0]
        for x in xs[1:]:
            if x > previous + 1:
                runs.append((start, previous))
                start = x
            previous = x
        runs.append((start, previous))
        visible_feet = [(x0, x1) for x0, x1 in runs if x1 - x0 + 1 >= 9]
        if (len(visible_feet) == 2
                and visible_feet[1][0] - visible_feet[0][1] >= 13):
            feet = visible_feet
            break
    if feet is None:
        return 0

    gap_left, gap_right = feet[0][1] + 1, feet[1][0] - 1
    if gap_right - gap_left < 10:
        return 0
    upper_limit = top + round(.66 * height)
    pending = deque((x, bottom - 2) for x in range(gap_left, gap_right + 1))
    seen = set()
    removable = []
    while pending:
        x, y = pending.popleft()
        if ((x, y) in seen or not gap_left <= x <= gap_right
                or not upper_limit <= y < bottom):
            continue
        seen.add((x, y))
        r, g, b, alpha = pixels[x, y]
        neutral_gray = (
            max(r, g, b) - min(r, g, b) <= 20
            and 95 <= min(r, g, b) <= 245
        )
        if alpha >= 32 and not neutral_gray:
            continue
        if alpha >= 32:
            removable.append((x, y))
        pending.extend(((x - 1, y), (x + 1, y),
                        (x, y - 1), (x, y + 1)))

    if len(removable) < 100:
        return 0
    ys = [y for _, y in removable]
    if max(ys) - min(ys) < .06 * height:
        return 0
    for x, y in removable:
        pixels[x, y] = (0, 0, 0, 0)
    return len(removable)


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
            if x < knee_left - 24 or x > knee_right + 24:
                outside += 1

    # Don't alter white shoes, light trousers or ordinary pale details that
    # stay inside the limb envelope. Ambiguous cases remain for manual review.
    removed = 0
    if outside >= 80:
        # Even with a genuine exterior shadow, retain boots and pale cuffs
        # inside the leg envelope rather than erasing every neutral pixel.
        for x, y in candidates:
            if x < knee_left - 14 or x > knee_right + 14:
                pixels[x, y] = (0, 0, 0, 0)
                removed += 1
    # Most rejected ENG/LOG sprites instead have an enclosed gray region
    # bridging the two boots. The outside-only pass cannot reach that shadow.
    removed += _remove_foot_gap_background(rgba)
    return rgba, removed
