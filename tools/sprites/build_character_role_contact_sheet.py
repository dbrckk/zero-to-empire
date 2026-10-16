#!/usr/bin/env python3
"""Offline role-by-role contact sheet for *candidate review*, not art approval.

Read the complete verified source bank and exact SHA-matching head/motion audit.
Compose one Android-friendly PNG of first frames to expose visually inconsistent
faces, helmets and palettes. No artifact is moved to the Android app/runtime.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

COLUMNS = 6
ROLES = ("OP", "LOG", "ENG")
ACTIONS = ("IDLE", "WALK", "WORK", "CARRY", "REPAIR", "CELEB")
CELL_WIDTH = 216
CELL_HEIGHT = 242
PAD = 24
HEADER_HEIGHT = 90
ROLE_HEADER = 42
ROLE_GAP = 22
BG = (11, 20, 32)
CARD = (25, 39, 57)
PREVIEW_BG = (186, 200, 212)
TEXT = (239, 247, 255)
MUTED = (182, 200, 221)
ALERT = (255, 178, 118)
NORMAL = (92, 155, 169)
ROLE_LABELS = {"OP": "OPERATEUR", "LOG": "LOGISTIQUE", "ENG": "INGENIEUR"}
NAME_RE = re.compile(r"^CHR-(OP|LOG|ENG)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$")


def _font(size: int) -> ImageFont.ImageFont:
    for name in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def _load(bank_path: Path, audit_path: Path) -> tuple[dict, list[dict]]:
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    if (audit.get("review_only") is not True
            or audit.get("automatic_semantic_approval") is not False
            or audit.get("automatic_runtime_promotion") is not False
            or not isinstance(audit.get("assets"), list)
            or audit.get("candidate_count") != len(audit["assets"])):
        raise ValueError("Untrusted review-only audit")
    records = {r.get("id"): r for r in audit["assets"] if isinstance(r, dict)}
    if len(records) != len(audit["assets"]):
        raise ValueError("Duplicate or missing identity audit records")

    with zipfile.ZipFile(bank_path) as packed:
        names = packed.namelist()
        if names.count("candidate-bank-index.json") != 1:
            raise ValueError("Missing or duplicate bank metadata")
        meta = json.loads(packed.read("candidate-bank-index.json"))
        entries = meta.get("bank_entries")
        if (not isinstance(entries, list) or len(entries) != meta.get("candidate_count")
                or meta.get("automatic_semantic_approval") is not False
                or meta.get("automatic_runtime_promotion") is not False):
            raise ValueError("Untrusted candidate bank")
        seen, result = set(), []
        for entry in entries:
            aid = str(entry.get("id") or "")
            match = NAME_RE.fullmatch(aid)
            if match is None or aid in seen:
                raise ValueError("Invalid or duplicate character ID " + aid)
            seen.add(aid)
            expected_name = f"zte_chr_{match.group(1).lower()}_{match.group(2).lower()}_final.png"
            name = "candidates/" + expected_name
            if (entry.get("filename") != expected_name or names.count(name) != 1
                    or entry.get("strict_approved") is not False
                    or entry.get("runtime_promoted") is not False):
                raise ValueError("Missing or untrusted candidate PNG " + aid)
            blob = packed.read(name)
            if len(blob) > 20 * 1024 * 1024:
                raise ValueError("Excessive candidate atlas size")
            if (len(blob) != entry.get("bytes")
                    or hashlib.sha256(blob).hexdigest() != entry.get("sha256")):
                raise ValueError("Candidate SHA-256 mismatch " + aid)
            record = records.get(aid)
            if (not record or record.get("sha256") != entry["sha256"]
                    or record.get("strict_approved") is not False
                    or record.get("runtime_promoted") is not False
                    or not isinstance(record.get("new_identity_flags"), list)
                    or not isinstance(record.get("new_motion_flags"), list)
                    or not isinstance(record.get("head_identity_metrics"), dict)):
                raise ValueError("Stale or incomplete head/motion audit " + aid)
            with Image.open(io.BytesIO(blob)) as atlas:
                atlas.load()
                if atlas.size != (1024, 1024) or atlas.mode != "RGBA":
                    raise ValueError("Invalid candidate atlas dimensions " + aid)
                frame = atlas.crop((0, 0, 256, 256))
            if not frame.getchannel("A").getbbox():
                raise ValueError("Empty candidate first frame " + aid)
            result.append({
                "id": aid, "role": match.group(1), "action": match.group(2),
                "frame": frame, "reference": record["head_identity_metrics"].get("reference_id"),
                "head_deviation": record["head_identity_metrics"].get("mean_head_rgb_change"),
                "identity_flags": record["new_identity_flags"],
                "motion_flags": record["new_motion_flags"],
                "source_type": entry.get("source_type"),
            })
        if set(records) != seen:
            raise ValueError("Audit does not cover precisely the verified bank")
    return meta, result


def build(bank_path: Path, audit_path: Path, output_path: Path) -> dict:
    meta, rows = _load(bank_path, audit_path)
    row_groups = [sorted((r for r in rows if r["role"] == role),
                         key=lambda r: ACTIONS.index(r["action"]))
                  for role in ROLES]
    if any(not group for group in row_groups):
        raise ValueError("Expected candidates for each game character role")
    height = HEADER_HEIGHT + len(ROLES) * (ROLE_HEADER + CELL_HEIGHT + ROLE_GAP) + PAD
    width = PAD * 2 + COLUMNS * CELL_WIDTH
    result = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(result)
    hfont, font, small = _font(23), _font(16), _font(12)
    draw.text((PAD, 19), "ZERO TO EMPIRE  /  COHERENCE VISUELLE", font=hfont, fill=TEXT)
    draw.text((PAD, 53),
              f"{len(rows)} CANDIDATS  ·  {meta['strict_done']} STRICT DONE  ·  APERCU UNIQUEMENT",
              font=small, fill=MUTED)
    alert_count = 0
    for rindex, (role, entries) in enumerate(zip(ROLES, row_groups)):
        section_y = HEADER_HEIGHT + rindex * (ROLE_HEADER + CELL_HEIGHT + ROLE_GAP)
        draw.text((PAD, section_y + 5), ROLE_LABELS[role], font=hfont, fill=TEXT)
        draw.text((PAD + 180, section_y + 11),
                  "Comparer le meme visage, le casque et la tenue", font=small, fill=MUTED)
        for index, item in enumerate(entries):
            x, y = PAD + index * CELL_WIDTH, section_y + ROLE_HEADER
            warnings = item["identity_flags"]
            alert_count += bool(warnings)
            outline = ALERT if warnings else NORMAL
            draw.rounded_rectangle((x, y, x + CELL_WIDTH - 12, y + CELL_HEIGHT - 4),
                                   radius=9, fill=CARD, outline=outline, width=2 if warnings else 1)
            actor = Image.new("RGBA", (192, 186), (*PREVIEW_BG, 255))
            frame = item["frame"].resize((186, 186), Image.Resampling.LANCZOS)
            actor.alpha_composite(frame, ((192 - 186) // 2, 0))
            result.paste(actor.convert("RGB"), (x + 6, y + 5))
            draw.text((x + 11, y + 190), item["action"], font=font, fill=TEXT)
            if warnings:
                notice = "IDENTITE A REVOIR"
            elif item["motion_flags"]:
                notice = "MOUVEMENT A REVOIR"
            else:
                notice = "REVUE ARTISTIQUE"
            draw.text((x + 11, y + 215), notice, font=small,
                      fill=ALERT if warnings else MUTED)
            if item["source_type"] == "repo-local-original":
                draw.rectangle((x + 134, y + 191, x + 193, y + 206), fill=(60, 86, 113))
                draw.text((x + 136, y + 192), "LOCAL", font=small, fill=TEXT)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.save(output_path, "PNG", optimize=True)
    return {
        "review_only": True, "strict_done_added": 0,
        "asset_count": len(rows), "identity_attention_count": alert_count,
        "strict_done_unchanged": meta["strict_done"],
        "width": width, "height": height, "bytes": output_path.stat().st_size,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(build(args.bank, args.audit, args.output), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
