from __future__ import annotations

import json
from pathlib import Path
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / 'art/generated'
PROCESSED = ROOT / 'art/processed'
RUNTIME = ROOT / 'app/src/main/res/drawable-nodpi'
MANIFEST = INBOX / 'assets.json'


def trim_alpha(im: Image.Image) -> Image.Image:
    alpha = im.getchannel('A')
    bbox = alpha.getbbox()
    if not bbox:
        raise ValueError('asset is fully transparent')
    return im.crop(bbox)


def pad_square(im: Image.Image, padding_ratio: float = 0.10) -> Image.Image:
    w, h = im.size
    side = max(w, h)
    pad = max(16, round(side * padding_ratio))
    canvas_side = side + pad * 2
    out = Image.new('RGBA', (canvas_side, canvas_side), (0, 0, 0, 0))
    # bottom-centre placement preserves the world pivot while retaining safety padding.
    x = (canvas_side - w) // 2
    y = canvas_side - pad - h
    out.alpha_composite(im, (x, y))
    return out


def alpha_quality(im: Image.Image) -> None:
    if im.mode != 'RGBA':
        raise ValueError('RGBA transparency required')
    a = im.getchannel('A')
    lo, hi = a.getextrema()
    if hi == 0:
        raise ValueError('empty alpha')
    # Reject images that are effectively opaque rectangles. Generated sheets/backgrounds must not pass.
    transparent = sum(1 for p in a.get_flattened_data() if p <= 8)
    if transparent / (im.width * im.height) < 0.02:
        raise ValueError('insufficient transparent area; likely background/sheet')


def process(spec: dict) -> None:
    src = INBOX / spec['source']
    asset_id = spec['id']
    target = spec['target']
    size = int(spec.get('runtime_size', 512))
    if not src.is_file():
        raise FileNotFoundError(src)
    with Image.open(src) as opened:
        im = opened.convert('RGBA')
    alpha_quality(im)
    im = trim_alpha(im)
    im = pad_square(im, float(spec.get('padding_ratio', 0.10)))
    im.thumbnail((size, size), Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    x = (size - im.width) // 2
    y = size - max(8, round(size * 0.08)) - im.height
    y = max(0, y)
    canvas.alpha_composite(im, (x, y))
    alpha_quality(canvas)

    PROCESSED.mkdir(parents=True, exist_ok=True)
    RUNTIME.mkdir(parents=True, exist_ok=True)
    preview = PROCESSED / f'{asset_id}.png'
    canvas.save(preview, 'PNG', optimize=True)
    runtime = RUNTIME / target
    if runtime.suffix.lower() == '.webp':
        canvas.save(runtime, 'WEBP', lossless=True, method=6)
    else:
        canvas.save(runtime, 'PNG', optimize=True)
    print(f'processed {asset_id}: {src.relative_to(ROOT)} -> {runtime.relative_to(ROOT)}')


def process_sheet(spec: dict) -> None:
    src = INBOX / spec['source']
    asset_id = spec['id']
    target = spec['target']
    columns = int(spec['columns'])
    rows = int(spec['rows'])
    frame_size = int(spec['frame_size'])
    padding_ratio = float(spec.get('padding_ratio', 0.10))
    if not src.is_file():
        raise FileNotFoundError(src)
    with Image.open(src) as opened:
        source = opened.convert('RGBA')
    alpha_quality(source)
    sheet = Image.new('RGBA', (columns * frame_size, rows * frame_size), (0, 0, 0, 0))
    for row in range(rows):
        top = round(row * source.height / rows)
        bottom = round((row + 1) * source.height / rows)
        for column in range(columns):
            left = round(column * source.width / columns)
            right = round((column + 1) * source.width / columns)
            frame = trim_alpha(source.crop((left, top, right, bottom)))
            frame = pad_square(frame, padding_ratio)
            frame.thumbnail((frame_size, frame_size), Image.Resampling.LANCZOS)
            cell = Image.new('RGBA', (frame_size, frame_size), (0, 0, 0, 0))
            cell.alpha_composite(frame, ((frame_size - frame.width) // 2, (frame_size - frame.height) // 2))
            sheet.alpha_composite(cell, (column * frame_size, row * frame_size))
    alpha_quality(sheet)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    RUNTIME.mkdir(parents=True, exist_ok=True)
    sheet.save(PROCESSED / f'{asset_id}.png', 'PNG', optimize=True)
    runtime = RUNTIME / target
    if runtime.suffix.lower() == '.webp':
        sheet.save(runtime, 'WEBP', lossless=True, method=6)
    else:
        sheet.save(runtime, 'PNG', optimize=True)
    print(f'processed {asset_id}: {columns}x{rows} frames at {frame_size}px; {src.relative_to(ROOT)} -> {runtime.relative_to(ROOT)}')


def main() -> None:
    if not MANIFEST.exists():
        print('No art/generated/assets.json; nothing to process.')
        return
    specs = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if not isinstance(specs, list):
        raise ValueError('assets.json must contain a JSON array')
    seen = set()
    for spec in specs:
        asset_id = spec['id']
        target = spec['target']
        if asset_id in seen:
            raise ValueError(f'duplicate asset id: {asset_id}')
        seen.add(asset_id)
        if not target.startswith('zte_') or not target.endswith(('_final.webp', '_final.png')):
            raise ValueError(f'invalid final target: {target}')
        if spec.get('kind') == 'sprite_sheet':
            process_sheet(spec)
        else:
            process(spec)


if __name__ == '__main__':
    main()
