"""Conservative 256px sprite cargo/hand-region lock for CARRY actions.

The first action frame supplies the unchanged waist-and-cargo pixels. When
subsequent frames retain the same character scale, foot pivot and alignment,
copy that bounded region back with feathered vertical boundaries, leaving
leg/boot motion intact. This cannot establish semantics or grant strict DONE.
"""
from __future__ import annotations

from PIL import Image, ImageDraw


def lock_cargo_region(frame: Image.Image, first_frame: Image.Image):
    """Return (candidate_rgba, applied_bool, diagnostic_reason)."""
    target, reference = frame.convert("RGBA"), first_frame.convert("RGBA")
    if target.size != (256, 256) or reference.size != (256, 256):
        return target, False, "invalid-character-cell-size"
    ref_box = reference.getchannel("A").getbbox()
    dst_box = target.getchannel("A").getbbox()
    if ref_box is None or dst_box is None:
        return target, False, "empty-character-frame"
    x0, y0, x1, y1 = ref_box
    xx0, yy0, xx1, yy1 = dst_box
    height, target_height = y1 - y0, yy1 - yy0
    if height < 120 or abs(height - target_height) > 12:
        return target, False, "unsafe-cargo-character-scale"
    if abs(y0 - yy0) > 9 or abs(y1 - yy1) > 5:
        return target, False, "unsafe-cargo-foot-pivot"
    if abs((x0 + x1) - (xx0 + xx1)) > 24:
        return target, False, "unsafe-cargo-horizontal-alignment"
    top = round(y0 + height * .38)
    bottom = round(y0 + height * .72)
    if top < 0 or bottom > 256 or bottom - top < 35:
        return target, False, "unsafe-cargo-region"
    if reference.getchannel("A").crop((0, top, 256, bottom)).getbbox() is None:
        return target, False, "empty-cargo-source"
    mask = Image.new("L", (256, 256), 0)
    brush = ImageDraw.Draw(mask)
    feather = 8
    for y in range(top, bottom):
        factor = min((y - top) / feather, (bottom - y - 1) / feather, 1)
        brush.line((0, y, 255, y), fill=max(0, min(255, round(255 * factor))))
    return Image.composite(reference, target, mask), True, "same-action-waist-and-cargo-region"
