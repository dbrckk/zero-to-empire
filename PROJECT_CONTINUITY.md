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

## Current handoff — 2026-09-07 15:30 +02:00
### Current trusted state
- Strict committed progress ledger remains **112 / 235 DONE** until strict reconciliation proves a higher number.
- `BLD-03-T2` through `BLD-03-T6` were integrated by run 75 (`e14b6897...`) but still require canonical reconciliation/green-CI proof before increasing strict DONE.
- Run 77 (`34102566634`) produced 21 technically valid building candidates; semantic review rejected 21/21.
- Run 78 (`34116344191`) produced no fresh accepted candidates and motivated retry/QA changes.
- Run 79 (`34121697907`) produced 0 fresh accepted candidates and motivated prompt-length plus monotonic-envelope corrections.

### Active generator
- Canonical building generator is **v14 prompt-safe-monotonic** at `tools/sprites/kaggle_building_family_factory_v14.py`.
- `kaggle/github_mass_factory.py` routes BUILDING_FAMILIES directly to v14.
- v14 uses short prompts, edge-connected background segmentation, tier-specific final envelopes, adaptive retries and family-level identity/growth/drift QA.

### Wave 80 — live checkpoint
- Trigger commit: `5202d20d7b99efffe2225604b4ee1f0b4f2cfede`.
- GitHub Actions run: `34125123246`.
- Workflow job: `101751899400`.
- Requested batch: 28 manifest tiers.
- At **2026-09-07 15:30 +02:00**, the job is still `in_progress` at step **Wait for Kaggle**.
- Steps already green: setup, checkout, credentials, runner dependencies, Kaggle authentication, kernel preparation, and kernel push/start.
- Artifact download, kernel-success gate, fresh-candidate gate and QA-evidence upload are still pending because the Kaggle kernel has not finished.
- Do **not** trigger a concurrent sprite pulse while run 80 is active: workflow concurrency can cancel the active GPU run and waste the current generation attempt.

## Immediate next actions — ordered
1. On the next intervention, query run `34125123246` first.
2. As soon as it completes, retrieve the kernel log and QA artifact.
3. Inspect every emitted candidate/family at full resolution; do not promote from technical QA alone.
4. Promote only coherent complete families with correct identity, isolation and unmistakable T0→T6 progression.
5. Integrate accepted masters/runtime assets, reconcile manifest/progress and require green Android CI before increasing strict DONE.
6. If v14 yields no promotable family, derive the next generator change from wave-80 evidence rather than repeating unchanged settings.
7. Continue through buildings, remaining static assets, characters and FX until **235 / 235 strict DONE**.

## Known unresolved art targets
- Remaining building families/tiers after `BLD-03`.
- `TER-07` Expansion energy conduit unless superseded by a later accepted promotion.
- Character/FX backlog requires its dedicated production lane once buildings no longer dominate routing.
- Every TODO/ART/RUNTIME manifest item remains subject to the strict completion gate.

## Operating principle
Quality beats nominal throughput. Failed/rejected generation is QA evidence, not DONE progress. Never replace the strict counter with candidate counts.