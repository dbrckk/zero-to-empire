#!/usr/bin/env python3
"""Cross-check pending strict character IDs against all locally authored motion loops.

Read-only review: checks source coverage and per-loop technical motion evidence;
NEVER grants semantic or Android runtime approval.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8"))

def audit():
    q=load("art/production/master-asset-queue.json")
    m=load("art/incoming/chatgpt-original/creation-manifest.json")
    a=load("art/incoming/chatgpt-original/animation-review.json")
    risk=load("art/incoming/chatgpt-original/visual-risk-qa.json")
    manifest={x["id"]:x for x in m["assets"]}
    motion={x["id"]:x for x in a["assets"]}
    risks={x["id"]:x for x in risk["assets"]}
    pending=[x for x in q["assets"] if x["id"].startswith("CHR-") and x["strict_status"]!="DONE"]
    rows=[]
    for item in pending:
        ident=item["id"]
        source=manifest.get(ident)
        evidence=motion.get(ident)
        visual=risks.get(ident)
        problems=[]
        if not source: problems.append("MISSING_SOURCE_MANIFEST")
        else:
            path=ROOT/"art/incoming/chatgpt-original/candidates"/source["file"]
            if not path.is_file(): problems.append("MISSING_ATLAS")
            if source.get("strict_approved") is not False: problems.append("CANDIDATE_APPROVAL_FLAG_CHANGED")
        if not evidence: problems.append("MISSING_MOTION_EVIDENCE")
        else:
            if evidence["frames"]!=source["frames"] if source else False:
                problems.append("FRAME_COUNT_MISMATCH")
            if evidence["distinct_frame_hashes"]!=evidence["frames"]:
                problems.append("REPEATED_FRAMES")
            if not evidence.get("technical_geometry_pass"):
                problems.append("GEOMETRY_FAILURE")
            if evidence.get("abrupt_loop_reset_risk"):
                problems.append("ABRUPT_LOOP_RESET")
            if evidence.get("loop_seam_to_median_ratio",999)>2:
                problems.append("LOOP_SEAM_OUTLIER")
        if not visual or visual.get("risk_level")!="NOT_DETECTED" or visual.get("flags"):
            problems.append("VISUAL_RISK_REVIEW_REQUIRED")
        rows.append({"id":ident,"source_atlas":source["file"] if source else None,
                     "frames":evidence["frames"] if evidence else None,
                     "unique_frames":evidence["distinct_frame_hashes"] if evidence else None,
                     "loop_seam_ratio":evidence["loop_seam_to_median_ratio"] if evidence else None,
                     "technical_motion_ready":not problems,
                     "issues":problems,"semantic_approved":False,
                     "android_runtime_approved":False,"strict_status":item["strict_status"]})
    return {"schema_version":1,"review_only":True,"strict_done":sum(x["strict_status"]=="DONE" for x in q["assets"]),
            "target_total":q["target_total"],"pending_count":len(rows),
            "motion_technical_ready":sum(x["technical_motion_ready"] for x in rows),
            "semantic_approved_by_this_audit":0,"items":rows}

def main():
    report=audit()
    out=ROOT/"art/production/character-motion-evidence.json"
    out.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(f"MOTION_READY={report['motion_technical_ready']}/{report['pending_count']}")
    print(f"STRICT_DONE={report['strict_done']}/{report['target_total']}")
    for row in report["items"]:
        print(row["id"],"READY" if row["technical_motion_ready"] else ",".join(row["issues"]))
    return 0 if report["motion_technical_ready"]==report["pending_count"] else 1

if __name__=="__main__":
    raise SystemExit(main())
