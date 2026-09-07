# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read this file before any new work on this repository and update it at every assistant intervention that changes goals, state, decisions, blockers, or next actions.

## Global continuity rule
- This repository must always keep a recent, concrete record of the latest changes and the next objectives.
- The assistant must update this file whenever it works on the repository and before ending an intervention that materially changes project state.
- Do not rely on chat history as the only source of continuity.
- Apply the same `PROJECT_CONTINUITY.md` convention to every actively worked repository going forward.
- Never mark an objective complete from intent alone: record the commit/run/CI evidence that proves completion.

## Primary objective
Bring **Zero → Empire** to full production completion, with the current immediate art objective being **100% of the canonical final sprite manifest**.

Canonical art sources:
- `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`
- `docs/art/FINAL_AAA_SPRITE_PROGRESS.md`

Locked scope: **235 final deliverables**.

## Non-negotiable sprite completion gate
An asset is not strict `DONE` until it is individually authored/generated, semantically correct, technically clean, transparent where required, committed to the final runtime path, actually referenced/visible in runtime, and validated by green Android CI. Candidate sheets, concept collages, technically valid but semantically wrong generations, or merely integrated files do not increment strict DONE.

## Current handoff — 2026-09-07
### Last known repository head before this continuity file
`fce86ce05bd492bb86165c3fe2b79841a86f8e40` — `perf: harden building family generation and skip integrated assets`.

### Recent material changes
1. Run 75 produced a reviewed `BLD-03` Assembly Hub continuation and commit `e14b6897e32a557736a4e9c06d55b925864993d1` integrated `BLD-03-T2` through `BLD-03-T6` runtime/master files.
2. Those five files must not be counted as strict DONE solely because they were integrated; reconcile manifest/progress/runtime references and require green Android CI evidence first.
3. Commit `1325aa0fef2ab336c87a1f421d652c008d8f02d4` launched **Kaggle Mass Sprite Factory run 77**.
4. GitHub Actions run `34102566634` / wave 77 completed successfully and produced a fresh technically validated QA artifact `kaggle-sprite-batch` (artifact id `10012165066`).
5. Wave 77 still requires semantic/full-resolution review and selective promotion. Technical success alone is not art approval.
6. The current building generator was hardened to `building-family-flux-v10-coherence-safe`; it skips runtime assets already present, lowers img2img strength to preserve family identity, prioritizes proven families, and strengthens rejection of detached/background/text contamination.
7. Scheduled static GPU planning run `34110783613` on head `fce86ce...` completed successfully.

## Current trusted counters
The committed progress ledger currently reports **112 / 235 strict DONE**. Do not silently inflate this number from run 75 or run 77 until their strict promotion gate is fully satisfied and the canonical ledger is reconciled.

## Immediate next actions — ordered
1. Download and inspect wave 77 artifact `10012165066` at full resolution.
2. Perform strict semantic QA against the manifest for every emitted candidate; reject anything with wrong family identity, insufficient T0→T6 progression, text/UI/background contamination, detached components, wrong camera, or wrong target semantics.
3. Promote only accepted candidates to final runtime/master paths and wire them into active runtime references.
4. Reconcile `FINAL_AAA_SPRITE_MANIFEST.md` and `FINAL_AAA_SPRITE_PROGRESS.md` with the actual promoted state.
5. Run/verify Android CI and increment strict DONE only after green evidence.
6. Continue additional Kaggle sprite waves on explicit `Go` / `Continue`, prioritizing remaining TODO assets and avoiding already integrated runtime targets.
7. Repeat generate → technical QA → semantic QA → promotion → runtime integration → green CI until **235 / 235 strict DONE**.

## Known unresolved art targets
- Remaining building families/tiers after `BLD-03`, with coherent family identity and unmistakable monotonic T0→T6 growth.
- `TER-07` Expansion energy conduit remains unresolved in the canonical manifest unless superseded by a later accepted promotion.
- Any other TODO/ART/RUNTIME item in the canonical manifest must be resolved through the same strict gate.

## Operating principle
Quality beats nominal throughput. A failed/rejected generation wave is valid QA evidence but is **not progress toward DONE**. Never replace a correct strict counter with an optimistic candidate count.
