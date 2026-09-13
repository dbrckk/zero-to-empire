#!/usr/bin/env python3
"""Build a compact visual QA sheet + machine-readable anomaly report.

This is deliberately deterministic and model-free: it does not decide semantic
correctness, but it catches common production defects and makes human semantic
review of large batches fast.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "art/incoming/final-sprites"
DEFAULT_OUT = ROOT / "art/production/batch-contact-sheet.png"
DEFAULT_REPORT = ROOT / "art/production/batch-qa-report.json"
FX_RE = re.compile(r"^zte_fx_(?:0[0-9]|1[0-7])_final\.png$")
CHR_RE = re.compile(r"^zte_chr_(?:op|tech|log|eng)_(idle|walk|work|carry|repair|celeb)_final\.png$")
CHR_EXPECTED = {"idle": 6, "walk": 8, "work": 10, "carry": 8, "repair": 10, "celeb": 8}


def alpha_bbox(im: Image.Image):
    return im.getchannel("A").getbbox()


def inspect(path: Path) -> dict:
    im = Image.open(path).convert("RGBA")
    a = im.getchannel("A")
    hist = a.histogram()
    pixels = im.width * im.height
    visible = sum(hist[8:]) / pixels
    bbox = alpha_bbox(im)
    issues: list[str] = []
    edge_clear = True
    bbox_ratio = 0.0 if not bbox else ((bbox[2]-bbox[0])*(bbox[3]-bbox[1]))/pixels

    if FX_RE.fullmatch(path.name):
        if im.size != (512, 256):
            issues.append("bad-fx-atlas-size")
        else:
            for i in range(8):
                x0=(i%4)*128; y0=(i//4)*128
                cell=a.crop((x0,y0,x0+128,y0+128))
                if cell.getbbox() is None:
                    issues.append(f"fx-frame-{i}-empty")
                    continue
                edges=(cell.crop((0,0,128,4)),cell.crop((0,124,128,128)),cell.crop((0,0,4,128)),cell.crop((124,0,128,128)))
                if any(e.getbbox() is not None for e in edges):
                    issues.append(f"fx-frame-{i}-unsafe-padding")
    elif (m := CHR_RE.fullmatch(path.name)):
        if im.size != (1024, 1024):
            issues.append("bad-character-atlas-size")
        else:
            expected=CHR_EXPECTED[m.group(1)]
            for i in range(16):
                x0=(i%4)*256; y0=(i//4)*256
                cell=a.crop((x0,y0,x0+256,y0+256))
                bb=cell.getbbox()
                if i < expected:
                    if bb is None:
                        issues.append(f"chr-frame-{i}-empty")
                        continue
                    h=cell.histogram()
                    cov=sum(h[8:])/(256*256)
                    if not .10 <= cov <= .48:
                        issues.append(f"chr-frame-{i}-coverage")
                    edges=(cell.crop((0,0,256,8)),cell.crop((0,248,256,256)),cell.crop((0,0,8,256)),cell.crop((248,0,256,256)))
                    if any(e.getbbox() is not None for e in edges):
                        issues.append(f"chr-frame-{i}-unsafe-padding")
                elif bb is not None:
                    issues.append(f"chr-unused-cell-{i}-not-empty")
    else:
        if not bbox:
            issues.append("empty-alpha")
        else:
            x0, y0, x1, y1 = bbox
            pad = max(4, round(min(im.size)*0.04))
            edge_clear = x0 >= pad and y0 >= pad and x1 <= im.width-pad and y1 <= im.height-pad
            if not edge_clear:
                issues.append("unsafe-edge-padding")
            if visible < .015:
                issues.append("subject-too-small")
            if visible > .70:
                issues.append("coverage-too-high")
            if bbox_ratio > .82:
                issues.append("bbox-too-large")
        if im.width != im.height:
            issues.append("non-square-static-master")
        if im.width < 512 or im.height < 512:
            issues.append("master-too-small")

    lo, hi = a.getextrema()
    if hi == 0 and "empty-alpha" not in issues:
        issues.append("empty-alpha")
    if lo == 255:
        issues.append("no-transparency")
    return {
        "file": path.name,
        "width": im.width,
        "height": im.height,
        "visible_ratio": round(visible, 5),
        "bbox_ratio": round(bbox_ratio, 5),
        "edge_clear": edge_clear,
        "issues": issues,
        "pass": not issues,
    }


def checker(size: tuple[int, int], block=16) -> Image.Image:
    w, h = size
    out = Image.new("RGB", size, (235,235,235))
    d = ImageDraw.Draw(out)
    for y in range(0,h,block):
        for x in range(0,w,block):
            if (x//block + y//block) % 2:
                d.rectangle((x,y,min(x+block-1,w-1),min(y+block-1,h-1)), fill=(205,205,205))
    return out


def make_sheet(paths: list[Path], results: list[dict], out: Path, cols=6):
    tile_w, tile_h = 300, 350
    rows = max(1, math.ceil(len(paths)/cols))
    sheet = Image.new("RGB", (cols*tile_w, rows*tile_h), (32,32,36))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for i, (path, result) in enumerate(zip(paths, results)):
        col, row = i % cols, i // cols
        ox, oy = col*tile_w, row*tile_h
        im = Image.open(path).convert("RGBA")
        preview = im.copy()
        preview.thumbnail((268,268), Image.Resampling.LANCZOS)
        bg = checker((276,276))
        px = (276-preview.width)//2
        py = (276-preview.height)//2
        bg.paste(preview, (px,py), preview)
        sheet.paste(bg, (ox+12,oy+12))
        status = "PASS" if result["pass"] else "CHECK"
        draw.text((ox+12,oy+296), f"{status}  {path.stem}", font=font, fill=(245,245,245))
        draw.text((ox+12,oy+312), f"vis={result['visible_ratio']:.1%} bbox={result['bbox_ratio']:.1%}", font=font, fill=(210,210,210))
        if result["issues"]:
            msg = ", ".join(result["issues"])
            draw.text((ox+12,oy+328), msg[:44], font=font, fill=(245,210,180))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, "PNG", optimize=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    ap.add_argument("--output", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    ap.add_argument("--pattern", default="*_final.png")
    ap.add_argument("--files", nargs="*", default=[])
    args = ap.parse_args()
    paths = [Path(x) for x in args.files] if args.files else sorted(args.input.glob(args.pattern))
    paths = [p for p in paths if p.exists() and p.stat().st_size > 0]
    if not paths:
        raise SystemExit("no sprite candidates for contact sheet")
    results = [inspect(p) for p in paths]
    make_sheet(paths, results, args.output)
    report = {
        "total": len(results),
        "automatic_pass": sum(r["pass"] for r in results),
        "needs_review": sum(not r["pass"] for r in results),
        "assets": results,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"CONTACT_SHEET={args.output}")
    print(f"QA_REPORT={args.report}")
    print(f"QA_TOTAL={report['total']} QA_AUTO_PASS={report['automatic_pass']} QA_REVIEW={report['needs_review']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
