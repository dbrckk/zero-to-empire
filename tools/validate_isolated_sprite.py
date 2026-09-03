from __future__ import annotations

import json
from collections import deque
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / 'art/generated'
MANIFEST = INBOX / 'assets.json'


def connected_components(alpha: Image.Image, threshold: int = 24):
    # Downsample for deterministic/cheap component analysis.
    max_side = 256
    scale = min(1.0, max_side / max(alpha.size))
    if scale < 1.0:
        alpha = alpha.resize((max(1, round(alpha.width * scale)), max(1, round(alpha.height * scale))))
    w, h = alpha.size
    px = alpha.load()
    seen = bytearray(w * h)
    comps = []

    def idx(x, y):
        return y * w + x

    for y in range(h):
        for x in range(w):
            i = idx(x, y)
            if seen[i] or px[x, y] <= threshold:
                continue
            q = deque([(x, y)])
            seen[i] = 1
            count = 0
            minx = maxx = x
            miny = maxy = y
            while q:
                cx, cy = q.popleft()
                count += 1
                minx, maxx = min(minx, cx), max(maxx, cx)
                miny, maxy = min(miny, cy), max(maxy, cy)
                for nx, ny in ((cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)):
                    if 0 <= nx < w and 0 <= ny < h:
                        ni = idx(nx, ny)
                        if not seen[ni] and px[nx, ny] > threshold:
                            seen[ni] = 1
                            q.append((nx, ny))
            comps.append((count, (minx, miny, maxx + 1, maxy + 1)))
    return sorted(comps, reverse=True)


def validate(path: Path) -> None:
    with Image.open(path) as opened:
        im = opened.convert('RGBA')
    alpha = im.getchannel('A')
    lo, hi = alpha.getextrema()
    if hi == 0:
        raise ValueError('fully transparent')
    transparent_ratio = sum(1 for p in alpha.get_flattened_data() if p <= 8) / (im.width * im.height)
    if transparent_ratio < 0.08:
        raise ValueError(f'background not transparent enough ({transparent_ratio:.1%})')

    bbox = alpha.getbbox()
    if bbox is None:
        raise ValueError('empty asset')
    left, top, right, bottom = bbox
    margin = min(left, top, im.width-right, im.height-bottom)
    if margin < max(2, round(min(im.size) * 0.015)):
        raise ValueError('subject touches canvas edge / insufficient safety margin')

    comps = connected_components(alpha)
    if not comps:
        raise ValueError('no visible component')
    total = sum(c[0] for c in comps)
    major = [c for c in comps if c[0] / total >= 0.08]
    if len(major) > 1:
        ratios = ', '.join(f'{c[0]/total:.1%}' for c in major[:6])
        raise ValueError(f'multiple major disconnected subjects detected: {ratios}')

    # A single subject should normally form one dominant occupancy region rather than many equal cells.
    dominant = comps[0][0] / total
    if dominant < 0.72:
        raise ValueError(f'fragmented/atlas-like alpha layout; dominant component only {dominant:.1%}')

    print(f'isolated sprite OK: {path.relative_to(ROOT)}; transparent={transparent_ratio:.1%}; dominant={dominant:.1%}')


def validate_sheet(path: Path, spec: dict) -> None:
    with Image.open(path) as opened:
        sheet = opened.convert('RGBA')
    columns = int(spec['columns'])
    rows = int(spec['rows'])
    expected = int(spec['frame_count'])
    if columns * rows != expected:
        raise ValueError(f'invalid sheet layout: {columns}x{rows} != {expected} frames')
    alpha = sheet.getchannel('A')
    transparent_ratio = sum(1 for p in alpha.get_flattened_data() if p <= 8) / (sheet.width * sheet.height)
    if transparent_ratio < 0.08:
        raise ValueError(f'sheet background not transparent enough ({transparent_ratio:.1%})')
    for row in range(rows):
        top = round(row * sheet.height / rows)
        bottom = round((row + 1) * sheet.height / rows)
        for column in range(columns):
            left = round(column * sheet.width / columns)
            right = round((column + 1) * sheet.width / columns)
            frame_alpha = sheet.crop((left, top, right, bottom)).getchannel('A')
            if frame_alpha.getbbox() is None:
                raise ValueError(f'empty frame at row={row}, column={column}')
            comps = connected_components(frame_alpha)
            total = sum(component[0] for component in comps)
            dominant = comps[0][0] / total
            if dominant < 0.72:
                raise ValueError(f'fragmented frame at row={row}, column={column}; dominant component only {dominant:.1%}')
    print(f'animation sheet OK: {path.relative_to(ROOT)}; frames={columns}x{rows}; transparent={transparent_ratio:.1%}')


def main() -> None:
    if not MANIFEST.exists():
        print('No art/generated/assets.json; nothing to validate.')
        return
    specs = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if not isinstance(specs, list):
        raise ValueError('assets.json must contain a JSON array')
    for spec in specs:
        path = INBOX / spec['source']
        if spec.get('kind') == 'sprite_sheet':
            validate_sheet(path, spec)
        else:
            validate(path)


if __name__ == '__main__':
    main()
