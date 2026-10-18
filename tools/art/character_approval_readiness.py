#!/usr/bin/env python3
"""Audit character candidate readiness without granting semantic approval.

Reads only repository-owned production metadata. Exits nonzero for missing,
technically failed, or explicitly flagged candidates. Does not mutate the queue.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
QUEUE = ROOT / "art/production/master-asset-queue.json"
ANIM = ROOT / "art/incoming/chatgpt-original/animation-review.json"
RISK = ROOT / "art/incoming/chatgpt-original/visual-risk-qa.json"
OUT = ROOT / "art/production/character-approval-readiness.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    queue = load(QUEUE)
    animation = {a["id"]: a for a in load(ANIM)["assets"]}
    risks = {a["id"]: a for a in load(RISK)["assets"]}
    pending = [a for a in queue["assets"] if a["id"].startswith("CHR-") and a["strict_status"] != "DONE"]
    rows = []
    for a in pending:
        ident = a["id"]
        motion = animation.get(ident)
        risk = risks.get(ident)
        blockers = []
        if motion is None:
            blockers.append("missing_animation_review")
        elif not motion.get("technical_geometry_pass"):
            blockers.append("technical_geometry_failed")
        if risk is None:
            blockers.append("missing_visual_risk_assessment")
        else:
            if risk.get("risk_level") != "NOT_DETECTED" or risk.get("flags"):
                blockers.append("visual_risk_flagged")
        rows.append({
            "id": ident,
            "technical_candidate_ready": not blockers,
            "blocking_reasons": blockers,
            "visual_review_required": True,
            "runtime_review_required": True,
            "strict_status_unchanged": a["strict_status"],
        })
    report = {
        "schema_version": 1,
        "review_only": True,
        "target_total": queue["target_total"],
        "strict_done": sum(a["strict_status"] == "DONE" for a in queue["assets"]),
        "remaining_semantic_review": len(rows),
        "technically_ready_for_visual_review": sum(r["technical_candidate_ready"] for r in rows),
        "automatic_semantic_approvals": 0,
        "assets": rows,
    }
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"ASSET_READINESS={report['technically_ready_for_visual_review']}/{len(rows)}")
    print(f"STRICT_DONE={report['strict_done']}/{report['target_total']}")
    for row in rows:
        print(f"{row['id']}: {'READY_FOR_VISUAL_REVIEW' if row['technical_candidate_ready'] else ','.join(row['blocking_reasons'])}")
    return 1 if any(not r["technical_candidate_ready"] for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main())
