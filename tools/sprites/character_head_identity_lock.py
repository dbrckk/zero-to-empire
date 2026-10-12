"""Conservative identity-preserving face/headgear transfer for sprite candidates.

A role's same-run IDLE frame is the visual reference; no external face model
or identity inference is involved. This never accepts semantics, never writes
runtime resources and skips poses whose full-body registration is unsafe.
"""
from __future__ import annotations

from PIL import Image, ImageChops, ImageDraw, ImageFilter

FRAME_SIZE = (256, 256)


def _head_anchor(frame: Image.Image):
    rgba = frame.convert("RGBA")
    if rgba.size != FRAME_SIZE:
        return None
    alpha = rgba.getchannel("A")
    bounds = alpha.getbbox()
    if bounds is None:
        return None
    left, top, right, bottom = bounds
    height = bottom - top
    if height < 120 or right - left < 24:
        return None
    # Centroid of the upper silhouette is less affected by a tool at waist
    # height than the geometric centre of the entire character bounding box.
    end = min(bottom, top + max(1, round(height * .25)))
    mask = alpha.crop((left, top, right, end))
    pix = mask.load()
    count = weighted = 0
    for y in range(mask.height):
        for x in range(mask.width):
            if pix[x, y] >= 120:
                count += 1
                weighted += x + left
    centre_x = round(weighted / count) if count else (left + right) // 2
    centre_y = top + round(height * .195)
    return centre_x, centre_y, bounds


def lock_head_to_idle(frame: Image.Image, idle: Image.Image):
    """Return (RGBA frame, applied bool, reason), no speculative approval.

    Only nearly upright, identically sized character silhouettes qualify.
    Crouching, high-arm silhouettes, small figures and strange framing retain
    the generated image for explicit manual review rather than a bad paste.
    """
    target = frame.convert("RGBA")
    reference = idle.convert("RGBA")
    a = _head_anchor(reference)
    b = _head_anchor(target)
    if a is None or b is None:
        return target, False, "missing-full-body-head-anchor"
    sx, sy, source_box = a
    tx, ty, target_box = b
    source_height = source_box[3] - source_box[1]
    target_height = target_box[3] - target_box[1]
    if abs(source_height - target_height) > 17:
        return target, False, "unsafe-body-scale"
    if abs(source_box[1] - target_box[1]) > 16:
        return target, False, "unsafe-top-silhouette"
    width, height = 72, 88
    if not (width // 2 <= sx < 256 - width // 2 and
            width // 2 <= tx < 256 - width // 2 and
            height // 2 <= sy < 256 - height // 2 and
            height // 2 <= ty < 256 - height // 2):
        return target, False, "unsafe-head-crop"
    piece = reference.crop((sx - width // 2, sy - height // 2,
                            sx + width // 2, sy + height // 2))
    target_head = target.crop((tx - width // 2, ty - height // 2,
                               tx + width // 2, ty + height // 2))
    # A copy from a different helmet profile, silhouette orientation or
    # displaced head would form a ghost/double-face. Enforce close shape
    # registration before compositing, then preserve manual review.
    source_binary = [v >= 64 for v in piece.getchannel("A").getdata()]
    target_binary = [v >= 64 for v in target_head.getchannel("A").getdata()]
    overlap = sum(a and b for a, b in zip(source_binary, target_binary))
    union = sum(a or b for a, b in zip(source_binary, target_binary))
    if not union or overlap / union < .78:
        return target, False, "unsafe-head-silhouette-overlap"
    soft = Image.new("L", (width, height), 0)
    ImageDraw.Draw(soft).ellipse((2, 1, width - 3, height - 2), fill=255)
    soft = soft.filter(ImageFilter.GaussianBlur(5))
    mask = ImageChops.multiply(piece.getchannel("A"), soft)
    piece.putalpha(mask)
    result = target.copy()
    result.alpha_composite(piece, (tx - width // 2, ty - height // 2))
    return result, True, "same-run-idle-headgear-reference"
