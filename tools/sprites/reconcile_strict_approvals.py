#!/usr/bin/env python3
"""Restore explicit historical strict-DONE approvals after queue reconstruction.

The autofactory rebuilds the master queue from a conservative unresolved set. This
module reapplies only approvals backed by explicit review/promotion history and a
runtime file that still exists. It does not approve new generated candidates.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MASTER = ROOT / "art/production/master-asset-queue.json"

APPROVED_BUILDING_COMMITS = {
    "BLD-04": "8214b23253317680fa52cbfa7b8f8099cb722590",
    "BLD-05": "2c5e8da870270b5aaa9b56e15cbf64380e4e5ba8",
    "BLD-07": "8214b23253317680fa52cbfa7b8f8099cb722590",
    "BLD-08": "2660ef0a580c326df38a51411cbc69ac48a0546c",
    "BLD-09": "0c29c0a20a757f89fdb7b83d42410bcb8be9297a",
    "BLD-10": "8214b23253317680fa52cbfa7b8f8099cb722590",
    "BLD-11": "190f92445bb1b7bfb1a0da81241f0ceffc0363a0",
    "BLD-12": "583cab453ed8604ee833b6a1b14647071ee66796",
    "BLD-13": "16160493f22fe12b9ea6bf1a6d5d6eba781e5734",
}


def runtime_for(asset: dict) -> Path | None:
    aid = asset["id"]
    family, tier = aid.rsplit("-T", 1)
    if family == "BLD-08":
        preferred = ROOT / f"app/src/main/res/drawable-nodpi/zte_business_08_t{tier}_final.png"
        if preferred.is_file() and preferred.stat().st_size:
            asset["runtime"] = str(preferred.relative_to(ROOT))
            return preferred
    configured = ROOT / asset["runtime"]
    return configured if configured.is_file() and configured.stat().st_size else None


def main() -> int:
    queue = json.loads(MASTER.read_text(encoding="utf-8"))
    by_id = {a["id"]: a for a in queue["assets"]}
    restored: list[str] = []

    for family, commit in APPROVED_BUILDING_COMMITS.items():
        expected = [f"{family}-T{i}" for i in range(7)]
        missing = [aid for aid in expected if aid not in by_id]
        if missing:
            raise RuntimeError(f"{family}: missing queue IDs: {missing}")
        for aid in expected:
            asset = by_id[aid]
            runtime = runtime_for(asset)
            if runtime is None:
                raise RuntimeError(f"{aid}: approved runtime missing: {asset['runtime']}")
            if asset.get("strict_status") != "DONE":
                restored.append(aid)
            asset["strict_status"] = "DONE"
            asset["pipeline_status"] = "DONE"
            asset["lane"] = "strict-done"
            asset["generation_required"] = False
            asset["last_error"] = None
            asset["review_reason"] = (
                f"Preserved explicit strict-DONE approval; evidence commit {commit}; "
                "runtime existence revalidated."
            )

    strict_done = sum(a.get("strict_status") == "DONE" for a in queue["assets"])
    if strict_done > queue["target_total"]:
        raise RuntimeError(f"strict DONE overflow: {strict_done}")
    queue["strict_done_baseline"] = strict_done
    MASTER.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"STRICT_APPROVALS_RESTORED={len(restored)} STRICT_DONE={strict_done}/{queue['target_total']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
