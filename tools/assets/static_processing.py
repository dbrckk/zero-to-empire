from __future__ import annotations

from collections import deque
import math

from PIL import Image


def _border_reference(im: Image.Image) -> tuple[int, int, int]:
    w, h = im.size
    px = im.load()
    samples = []
    stride = max(1, min(w, h) // 128)
    for x in range(0, w, stride):
        samples.append(px[x, 0])
        samples.append(px[x, h - 1])
    for y in range(0, h, stride):
        samples.append(px[0, y])
        samples.append(px[w - 1, y])
    channels = [sorted(c[i] for c in samples) for i in range(3)]
    mid = len(samples) // 2
    return tuple(ch[mid] for ch in channels)


def isolate(im: Image.Image) -> Image.Image:
    """Remove only border-connected background, preserving enclosed dark materials."""
    im = im.convert("RGB")
    w, h = im.size
    px = im.load()
    bg = _border_reference(im)
    hard = 28.0
    soft = 74.0

    def dist(rgb):
        return math.sqrt(sum((rgb[i] - bg[i]) ** 2 for i in range(3)))

    background = bytearray(w * h)
    q = deque()

    def push(x, y):
        idx = y * w + x
        if background[idx] or dist(px[x, y]) > soft:
            return
        background[idx] = 1
        q.append((x, y))

    for x in range(w):
        push(x, 0)
        push(x, h - 1)
    for y in range(h):
        push(0, y)
        push(w - 1, y)

    while q:
        x, y = q.popleft()
        if x:
            push(x - 1, y)
        if x + 1 < w:
            push(x + 1, y)
        if y:
            push(x, y - 1)
        if y + 1 < h:
            push(x, y + 1)

    alpha = Image.new("L", (w, h), 255)
    apx = alpha.load()
    for y in range(h):
        row = y * w
        for x in range(w):
            if not background[row + x]:
                continue
            d = dist(px[x, y])
            if d <= hard:
                apx[x, y] = 0
            else:
                apx[x, y] = max(
                    0,
                    min(255, round(255 * (d - hard) / (soft - hard))),
                )

    rgba = im.convert("RGBA")
    rgba.putalpha(alpha)
    return rgba


def components(alpha: Image.Image) -> tuple[int, float]:
    small = alpha.resize((128, 128), Image.Resampling.BILINEAR)
    px = small.load()
    seen = set()
    areas = []
    for y in range(128):
        for x in range(128):
            if (x, y) in seen or px[x, y] < 40:
                continue
            q = deque([(x, y)])
            seen.add((x, y))
            area = 0
            while q:
                cx, cy = q.popleft()
                area += 1
                for nx, ny in (
                    (cx - 1, cy),
                    (cx + 1, cy),
                    (cx, cy - 1),
                    (cx, cy + 1),
                ):
                    if (
                        0 <= nx < 128
                        and 0 <= ny < 128
                        and (nx, ny) not in seen
                        and px[nx, ny] >= 40
                    ):
                        seen.add((nx, ny))
                        q.append((nx, ny))
            if area >= 24:
                areas.append(area)
    if not areas:
        return 0, 0.0
    total = sum(areas)
    return len(areas), max(areas) / total


def normalize(master: Image.Image, side: int) -> Image.Image:
    bbox = master.getbbox()
    if not bbox:
        raise RuntimeError("empty alpha after background isolation")
    crop = master.crop(bbox)
    max_subject = int(side * .82)
    scale = min(max_subject / crop.width, max_subject / crop.height)
    crop = crop.resize(
        (max(1, round(crop.width * scale)), max(1, round(crop.height * scale))),
        Image.Resampling.LANCZOS,
    )
    out = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    x = (side - crop.width) // 2
    bottom = int(side * .08)
    y = side - bottom - crop.height
    if y < int(side * .08):
        y = (side - crop.height) // 2
    out.alpha_composite(crop, (x, y))
    return out


def validate(im: Image.Image) -> tuple[float, float]:
    a = im.getchannel("A")
    lo, hi = a.getextrema()
    if hi == 0 or lo == 255:
        raise RuntimeError("transparency validation failed")
    visible = sum(a.histogram()[8:]) / (im.width * im.height)
    if visible > .70:
        raise RuntimeError(f"alpha coverage too high: {visible:.1%}")
    pad = int(im.width * .04)
    edges = (
        a.crop((0, 0, im.width, pad)),
        a.crop((0, im.height - pad, im.width, im.height)),
        a.crop((0, 0, pad, im.height)),
        a.crop((im.width - pad, 0, im.width, im.height)),
    )
    if any(edge.getbbox() for edge in edges):
        raise RuntimeError("transparent safety padding failed")
    count, dominant = components(a)
    if count == 0 or dominant < .88:
        raise RuntimeError(
            f"subject isolation failed: components={count}, dominant={dominant:.1%}"
        )
    return visible, dominant
