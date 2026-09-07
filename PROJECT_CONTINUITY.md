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
- `BLD-03-T2` through `BLD-03-T6` were integrated by run 75 (`e14b6897...`) but still require canonical reconciliation/green-CI proof before increasing strict DONE.
- Run 77 (`34102566634`) produced 21 technically valid building candidates; semantic review rejected 21/21.
- Run 78 (`34116344191`) produced no fresh accepted candidates and motivated retry/QA changes.
- Run 79 (`34121697907`) also produced **0 fresh candidates**. It was not an auth/infrastructure failure: the generator completed its planned families, then rejected them all through QA and exited because no fresh files were emitted.

### Run 79 root-cause evidence
1. Prompt warnings show repeated **CLIP 77-token truncation** and T5 `max_sequence_length=256` truncation. Critical negative constraints were therefore being dropped before inference.
2. BLD-08 rendered T0→T6 but coverage grew only **22.1% → 25.7%** and was correctly rejected for insufficient growth.
3. BLD-09 rendered T0→T6 but coverage grew only **25.0% → 28.8%** and was correctly rejected for insufficient growth.
4. The v12/v13 post-processing normalized most non-T0 tiers into nearly the same display envelope, partially cancelling the visible tier growth requested from FLUX.
5. Strict DONE delta from run 79: **+0**.

### Generator evolution after run 79
- Added **v14 prompt-safe-monotonic** generator at `tools/sprites/kaggle_building_family_factory_v14.py` (`572f1c381d683b2cc732872144fe1a59ab842033`).
- `kaggle/github_mass_factory.py` routes future building waves through v14 (`071444d69928a94ce3a896a9ac81a5994b37f6d9`).
- v14 keeps semantic prompts intentionally short so the family DNA, tier instruction, isolation contract and key negatives survive CLIP/T5 limits.
- v14 preserves edge-connected background segmentation so neutral metallic interior materials are less likely to be deleted as background.
- v14 introduces explicit monotonic final envelopes by tier: T0 is deliberately small and each tier gets a progressively larger permitted canvas footprint through T6.
- v14 keeps adaptive retries, family identity IoU, growth, non-monotonicity, drift, slab, padding and detached-structure gates.
- Family growth gate is now stricter because the output normalization itself deliberately exposes tier scale growth instead of hiding it.

### Wave 80
- Explicit user `Go` authorizes the next generation wave.
- Trigger commit: `5202d20d7b99efffe2225604b4ee1f0b4f2cfede`.
- Generator: `building-family-flux-v14-prompt-safe-monotonic`.
- Requested batch count: 28 manifest tiers.
- Objective: preserve prompt constraints and force unmistakable T0→T6 growth while retaining strict semantic QA.

## Immediate next actions — ordered
1. Track wave 80 to completion.
2. Retrieve its artifact/log and inspect every emitted candidate at full resolution.
3. Promote only coherent complete families with correct family identity, clean isolation and unmistakable starter→ultimate progression.
4. Integrate accepted masters/runtime assets, reconcile manifest/progress and require green Android CI before increasing strict DONE.
5. If v14 still produces no promotable family, use wave-80 evidence to adjust generation strategy rather than repeating unchanged seeds/settings.
6. Once building backlog is exhausted, route remaining static assets, characters and FX through equally strict dedicated production lanes.
7. Repeat generate → technical QA → semantic QA → promotion → runtime integration → green CI until **235 / 235 strict DONE**.

## Known unresolved art targets
- Remaining building families/tiers after `BLD-03`, with coherent family identity and unmistakable monotonic T0→T6 growth.
- `TER-07` Expansion energy conduit remains unresolved unless superseded by a later accepted promotion.
- Character/FX backlog still requires its dedicated sheet-production lane once buildings no longer dominate routing.
- Any TODO/ART/RUNTIME item in the canonical manifest must pass the same strict completion gate.

## Operating principle
Quality beats nominal throughput. A failed/rejected generation wave is valid QA evidence but is **not progress toward DONE**. Optimize the generator from failure evidence, then retry. Never replace a strict counter with an optimistic candidate count.
