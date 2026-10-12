#!/usr/bin/env python3
"""Collector-side action-motion audit, independent of Kaggle generator version.

A technical atlas passes only if no obvious image-only identity/motion risks
were detected. Every pass still needs explicit artistic and Android review.
This annotates a derived QA report; source sprites and strict DONE stay intact.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from PIL import Image

from character_semantic_gate import clip_risk

ACTION_FILENAME = re.compile(r"^zte_chr_(op|log|eng|tech)_(work|repair)_final\.png$")
ATLAS_SIZE = (1024, 1024)
CELL_SIZE = 256
FRAME_COUNT = 10


def check_action_atlas(path: Path, action: str) -> dict:
    with Image.open(path) as file:
        if file.size != ATLAS_SIZE:
            raise ValueError(f"wrong-action-atlas-shape={file.size}")
        rgba = file.convert("RGBA")
    frames = [
        rgba.crop(((i % 4) * CELL_SIZE, (i // 4) * CELL_SIZE,
                   ((i % 4) + 1) * CELL_SIZE, ((i // 4) + 1) * CELL_SIZE))
        for i in range(FRAME_COUNT)
    ]
    risk = clip_risk(frames, action.upper())
    return {
        "risk_level": risk["risk_level"],
        "flags": risk["flags"],
        "action_pose_metrics": risk.get("action_pose_metrics", {}),
        "image_only_semantic_approval": False,
    }


def annotate_report(candidates_dir: Path, report: dict) -> dict:
    if not isinstance(report, dict) or not isinstance(report.get("assets"), list):
        raise ValueError("Expected build_sprite_contact_sheet assets report")
    for row in report["assets"]:
        name = Path(str(row.get("file") or "")).name
        match = ACTION_FILENAME.fullmatch(name)
        if match is None:
            continue
        try:
            details = check_action_atlas(candidates_dir / name, match.group(2))
        except (OSError, ValueError, IndexError) as exc:
            details = {
                "risk_level": "BLOCKING",
                "flags": ["ACTION_VISUAL_QA_ERROR"],
                "error": f"{type(exc).__name__}:{str(exc)[:180]}",
                "image_only_semantic_approval": False,
            }
        row["action_visual_risk"] = details
        if details["risk_level"] == "BLOCKING":
            row["pass"] = False
            issues = [str(v) for v in row.get("issues", [])]
            for flag in details["flags"]:
                issue = "action-visual-risk:" + str(flag)
                if issue not in issues:
                    issues.append(issue)
            row["issues"] = issues
    report["automatic_pass"] = sum(row.get("pass") is True for row in report["assets"])
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
        if "action_visual_risk" not in row:
            continue
        print("COLLECTOR_ACTION_RISK=" + json.dumps({
            "file": row.get("file"), "pass": row.get("pass"),
            "flags": row["action_visual_risk"].get("flags"),
            "pose_metrics": row["action_visual_risk"].get("action_pose_metrics"),
        }, sort_keys=True), flush=True)
    print("COLLECTOR_ACTION_RISK_AUDIT_COMPLETE=1", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
