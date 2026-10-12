#!/usr/bin/env python3
"""Fail-closed visual risk screening for generated IDLE candidate atlases.

Runs on the GitHub collector after producer output download, regardless of
which generator snapshot ran on Kaggle. Mutates only a derived QA JSON report,
never source sprites, strict status, or runtime resource files.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from PIL import Image

from character_semantic_gate import clip_risk, idle_distinct_head_clusters

IDLE_FILENAME = re.compile(r"^zte_chr_(op|log|eng|tech)_idle_final\.png$")
FRAME = 256
ATLAS = (1024, 1024)


def check_idle_atlas(path: Path) -> dict:
    with Image.open(path) as file:
        if file.size != ATLAS:
            raise ValueError(f"wrong-idle-atlas-shape={file.size}")
        atlas = file.convert("RGBA")
    frames = [
        atlas.crop(((index % 4) * FRAME, (index // 4) * FRAME,
                    ((index % 4) + 1) * FRAME, ((index // 4) + 1) * FRAME))
        for index in range(6)
    ]
    risk = clip_risk(frames, "IDLE")
    return {
        "risk_level": risk["risk_level"],
        "flags": risk["flags"],
        "head_counts": [idle_distinct_head_clusters(frame) for frame in frames],
        "image_only_semantic_approval": False,
    }


def annotate_report(candidates_dir: Path, report: dict) -> dict:
    if not isinstance(report, dict) or not isinstance(report.get("assets"), list):
        raise ValueError("Expected build_sprite_contact_sheet assets report")
    for row in report["assets"]:
        name = Path(str(row.get("file") or "")).name
        if not IDLE_FILENAME.fullmatch(name):
            continue
        try:
            details = check_idle_atlas(candidates_dir / name)
        except (OSError, ValueError, IndexError) as exc:
            details = {
                "risk_level": "BLOCKING",
                "flags": ["IDLE_VISUAL_QA_ERROR"],
                "error": f"{type(exc).__name__}:{str(exc)[:180]}",
                "head_counts": [],
                "image_only_semantic_approval": False,
            }
        row["idle_identity_risk"] = details
        if details["risk_level"] == "BLOCKING":
            row["pass"] = False
            issues = [str(x) for x in row.get("issues", [])]
            for flag in details["flags"]:
                issue = "idle-visual-risk:" + flag
                if issue not in issues:
                    issues.append(issue)
            row["issues"] = issues
    report["automatic_pass"] = sum(x.get("pass") is True for x in report["assets"])
    report["needs_review"] = len(report["assets"]) - report["automatic_pass"]
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--qa-report", type=Path, required=True)
    args = parser.parse_args()
    qa = json.loads(args.qa_report.read_text(encoding="utf-8"))
    qa = annotate_report(args.candidates, qa)
    args.qa_report.write_text(json.dumps(qa, indent=2) + "\n", encoding="utf-8")
    for row in qa["assets"]:
        details = row.get("idle_identity_risk")
        if details:
            print("COLLECTOR_IDLE_RISK=" + json.dumps({
                "file": row.get("file"),
                "pass": row.get("pass"),
                "head_counts": details.get("head_counts"),
                "flags": details.get("flags")
            }, sort_keys=True), flush=True)
    print("COLLECTOR_IDLE_RISK_AUDIT_COMPLETE=1", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
