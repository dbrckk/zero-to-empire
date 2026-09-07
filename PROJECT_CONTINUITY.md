# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read this file before any new work on this repository and update it at every assistant intervention that changes goals, state, decisions, blockers, or next actions.

## Global continuity rule
- This repository must always keep a recent, concrete record of the latest changes and the next objectives.
- The assistant must update this file whenever it works on the repository and before ending an intervention that materially changes project state.
- Do not rely on chat history as the only source of continuity.
- Apply the same `PROJECT_CONTINUITY.md` convention to every actively worked repository going forward.
- Never mark an objective complete from intent alone: record the commit/run/CI evidence that proves completion.

## Primary objective
Bring **Zero → Empire** to full production completion, with the immediate art objective being **100% of the canonical final sprite manifest**.

Canonical art sources:
- `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`
- `docs/art/FINAL_AAA_SPRITE_PROGRESS.md`

Locked scope: **235 final deliverables**.

## Non-negotiable sprite completion gate
An asset is not strict `DONE` until it is individually authored/generated, semantically correct, technically clean, transparent where required, committed to the final runtime path, actually referenced/visible in runtime, and validated by green Android CI. Candidate sheets, concept collages, technically valid but semantically wrong generations, or merely integrated files do not increment strict DONE.

## Current handoff — 2026-09-07
### Current trusted state
- Strict committed progress ledger remains **112 / 235 DONE** until strict reconciliation proves a higher number.
- `BLD-03-T2` through `BLD-03-T6` were integrated by run 75 (`e14b6897...`) but must still be reconciled against canonical manifest/progress and green CI before increasing strict DONE.
- Run 77 (`34102566634`) produced 21 technically valid building candidates; full-resolution semantic review rejected **21 / 21**. Review: `docs/art/reviews/RUN_77_SEMANTIC_REVIEW.md`.
- Run 78 (`34116344191`) produced no fresh accepted candidates; its failure evidence was used to improve retries and QA. Review: `docs/art/reviews/RUN_78_PIPELINE_REVIEW.md`.
- **Wave 79** GitHub Actions run `34121697907` was launched from commit `604d2cc4...` and is currently still executing the Kaggle GPU wait step. Do not trigger another pulse while it is active because workflow concurrency cancels in-progress runs.

### Generator evolution
- Canonical v12 retry-normalized generator was introduced after run 78.
- New **v13 edge-segmentation** generator added at `tools/sprites/kaggle_building_family_factory_v13.py` in commit `388dcd6070b28db7fd7b475711c9d682b0a40c38`.
- `kaggle/github_mass_factory.py` now routes future building waves through v13 in commit `0053152494757c468b64ee9083202c37714e377d`.
- Wave 79 itself started before those two commits, so it remains a v12 run. v13 applies beginning with the next user-approved wave after wave 79 finishes.

### v13 production improvements
1. **Edge-connected background segmentation** replaces global background-colour deletion. Only background-like pixels connected to the image borders are removed. This prevents grey/silver internal building materials from being accidentally punched out as alpha holes.
2. Segmentation runs on a 256×256 topology proxy and is softly upscaled, reducing CPU cost while preserving clean edges.
3. Background traversal has a bounded colour-distance tolerance, so object edges stop the flood even when the object shares neutral tones with the studio background.
4. T0 remains constrained to a smaller frame envelope and explicitly prohibits towers, cranes, gantries and late-game mass.
5. Later tiers receive up to three retries, while T0 keeps four retries.
6. Family QA retains identity IoU, monotonic coverage/growth, horizontal drift and T0→T6 evolution gates.
7. Ground-slab detection is stricter; detached-component dominance is stricter; internal-hole rejection is relaxed only enough to permit legitimate windows/cavities now that segmentation itself is safer.
8. Future Kaggle metadata identifies the engine as `v7 edge-segmentation`, making run provenance explicit.

## Immediate next actions — ordered
1. Let wave 79 complete without launching another concurrent pulse.
2. Retrieve its artifact/log immediately once complete.
3. Inspect every emitted candidate at full resolution and perform strict semantic family review.
4. Promote only coherent accepted families; integrate runtime paths/references and require green Android CI before incrementing strict DONE.
5. If wave 79 yields no promotable family, launch the next user-approved wave with **v13 edge-segmentation** rather than rerunning v12 unchanged.
6. Continue building families until the building backlog is exhausted, then route remaining static assets, characters and FX through dedicated strict production lanes.
7. Repeat generate → technical QA → semantic QA → promotion → runtime integration → green CI until **235 / 235 strict DONE**.

## Known unresolved art targets
- Remaining building families/tiers after `BLD-03`, with coherent family identity and unmistakable monotonic T0→T6 growth.
- `TER-07` Expansion energy conduit remains unresolved unless superseded by a later accepted promotion.
- Character/FX backlog still requires its dedicated sheet-production lane once buildings no longer dominate routing.
- Any TODO/ART/RUNTIME item in the canonical manifest must pass the same strict completion gate.

## Operating principle
Quality beats nominal throughput. A failed/rejected generation wave is valid QA evidence but is **not progress toward DONE**. Optimize the generator from failure evidence, then retry. Never replace a strict counter with an optimistic candidate count.
