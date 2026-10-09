#!/usr/bin/env python3
"""Reproducible review plan for the 19 remaining CHR assets.

Never treats a generated candidate as approved; detects canonical-vs-preview
conflicts (notably CHR-TECH-WALK) and prioritizes real human/artistic review.
Pure stdlib, works on GitHub Actions and offline without Kaggle.
"""
from __future__ import annotations
import argparse
import json
from collections import Counter
from pathlib import Path

ACTIONS=("IDLE","WALK","WORK","CARRY","REPAIR","CELEB")
ROLES=("OP","TECH","LOG","ENG")
REVIEW={
 "IDLE":("headgear, identity and clothing match the role","breathing and gaze readable, no sliding feet"),
 "WALK":("same face, clothing and facing through the stride","alternating foot contacts, fixed world pivot, loop seam"),
 "WORK":("one consistent tool/workstation, both hands visible","hand-to-device contact and work-cycle legibility"),
 "CARRY":("same crate and material, hands gripping correctly","crate remains supported during steps and turns"),
 "REPAIR":("one tool touches a stable repair point","visible welding/diagnostic contact and controlled VFX"),
 "CELEB":("recognizable same character with no unintended prop","expressive readable gesture, loop/one-shot behavior"),
}
# A review is more urgent when the asset is a walking foundation, or when a
# known semantic failure would otherwise be hidden by a different renderer.
ACTION_WEIGHT={"WALK":0,"CARRY":1,"WORK":2,"REPAIR":3,"IDLE":4,"CELEB":5}
ROLE_WEIGHT={"OP":0,"LOG":1,"ENG":2,"TECH":3}


def build(queue:dict)->dict:
    assets=queue.get("assets")
    if not isinstance(assets,list) or not isinstance(queue.get("target_total"),int):
        raise ValueError("Invalid canonical queue")
    ids=[a.get("id") for a in assets]
    if len(ids)!=len(set(ids)) or len(assets)!=queue["target_total"]:
        raise ValueError("Queue contains duplicate IDs or unexpected total")
    done=sum(a.get("strict_status")=="DONE" for a in assets)
    pending=[a for a in assets if a.get("strict_status")!="DONE"]
    if any(not a["id"].startswith("CHR-") for a in pending):
        raise ValueError("Unexpected non-character pending asset")
    rows=[]
    for a in pending:
        parts=a["id"].split("-")
        if len(parts)!=3 or parts[1] not in ROLES or parts[2] not in ACTIONS:
            raise ValueError("Unknown character identity/action "+a["id"])
        _,role,action=parts
        status=a.get("pipeline_status")
        rejected=status in ("REJECTED_SEMANTIC","REJECTED")
        reason=a.get("review_reason") or "No recorded specific defect"
        # A standalone TECH review render is not the canonical Kaggle asset.
        # Explicitly forbid silently equating the two.
        alternate=(role=="TECH" and action in ("WALK","WORK","CARRY"))
        priority=(0 if rejected else 1,ACTION_WEIGHT[action],ROLE_WEIGHT[role],a["id"])
        rows.append({
            "asset_id":a["id"],"role":role,"action":action,
            "canonical_pipeline_status":status,
            "strict_status":a.get("strict_status"),
            "recorded_reason":reason,
            "canonical_last_generator":a.get("last_generator"),
            "canonical_last_run_id":a.get("last_run_id"),
            "alternate_tech_renderer_available":alternate,
            "alternate_is_not_canonical_approval":True,
            "candidate_evidence_verified":False,
            "human_visual_review_pass":False,
            "semantic_review_pass":False,
            "review_priority":list(priority[:3]),
            "identity_check":REVIEW[action][0],
            "motion_check":REVIEW[action][1],
            "next_step":("Locate and inspect original rejected candidate; compare independent TECH rig "
                         "without replacing canonical evidence" if rejected else
                         "Locate candidate source artifact, verify frame count and inspect entire sequence"),
        })
    rows.sort(key=lambda r:(r["review_priority"],r["asset_id"]))
    by_role=dict(Counter(r["role"] for r in rows))
    return {
        "format":"zte-character-review-matrix-v1",
        "target_total":len(assets),"strict_done":done,"pending_count":len(rows),
        "strict_done_unchanged":True,
        "human_approval_required":True,
        "auto_promotion_permitted":False,
        "limitations":["No original Kaggle frames are bundled in this report",
                       "A separate TECH renderer does not clear a rejected canonical candidate",
                       "Prioritization is a review plan, not an aesthetic quality score"],
        "by_role":by_role,"items":rows,
    }


def markdown(report:dict)->str:
    lines=[
        "# Character review matrix — canonical assets",
        "",
        f"**Strict DONE:** {report['strict_done']}/{report['target_total']}; "
        f"**awaiting review:** {report['pending_count']}.",
        "",
        "This document does not promote or approve any asset. Verify actual source frames first.",
        "",
        "| Priority | Asset | Canonical status | Source run | Review action |",
        "|---:|---|---|---|---|",
    ]
    for n,row in enumerate(report["items"],1):
        action=row["next_step"].replace("|","/")
        lines.append(f"| {n} | `{row['asset_id']}` | "
                     f"{row['canonical_pipeline_status']} | "
                     f"{row['canonical_last_run_id'] or 'unavailable'} | {action} |")
    lines+=["","## Per-action acceptance criteria",""]
    for action,checks in REVIEW.items():
        lines.append(f"- **{action}**: {checks[0]}; {checks[1]}.")
    lines+=["","## Important evidence separation","",
            "The modular TECH pipeline has independently produced review candidates for WALK, WORK and CARRY. "
            "Its successful technical checks do **not** rewrite the canonical Kaggle result, "
            "which still records a semantic rejection for `CHR-TECH-WALK`. "
            "Human review must inspect the actual images and their provenance before any status change.",
            ""]
    return "\n".join(lines)


def main()->int:
    p=argparse.ArgumentParser()
    p.add_argument("--queue",type=Path,default=Path("art/production/master-asset-queue.json"))
    p.add_argument("--out-json",type=Path,default=Path("art/production/character-review-matrix.json"))
    p.add_argument("--out-md",type=Path,default=Path("art/production/character-review-matrix.md"))
    args=p.parse_args()
    report=build(json.loads(args.queue.read_text(encoding="utf-8")))
    args.out_json.parent.mkdir(parents=True,exist_ok=True)
    args.out_md.parent.mkdir(parents=True,exist_ok=True)
    args.out_json.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    args.out_md.write_text(markdown(report),encoding="utf-8")
    print(f"STRICT_DONE={report['strict_done']}/{report['target_total']} PENDING={report['pending_count']}")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
