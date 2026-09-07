# PROJECT CONTINUITY — Zero → Empire

> Persistent handoff file. Read this file before any new work on this repository and update it at every assistant intervention that changes goals, state, decisions, blockers, or next actions.

## Global continuity rule
- Keep a recent concrete record of changes, evidence, blockers and next objectives.
- Update this file at every material assistant intervention.
- Do not rely on chat history alone.
- Apply the same `PROJECT_CONTINUITY.md` convention to every actively worked repository.
- Never mark completion from intent or candidate generation alone.

## Primary objective
Bring **Zero → Empire** to full production completion. Immediate art objective: **235 / 235 canonical final sprites strict DONE**.

Canonical sources:
- `docs/art/FINAL_AAA_SPRITE_MANIFEST.md`
- `docs/art/FINAL_AAA_SPRITE_PROGRESS.md`

## Strict completion gate
A sprite is strict DONE only after individual production, semantic correctness, technical/alpha validation, final runtime commit/reference, actual runtime visibility, manifest/progress reconciliation and green Android CI. Candidate count is never DONE count.

## Current trusted state — 2026-09-07
- Strict ledger remains **112 / 235 DONE** pending evidence-based reconciliation.
- BLD-03-T2..T6 from run 75 remain integrated but not added to strict count without canonical/CI proof.
- Run 77: 21 technical candidates, 21/21 semantic rejection.
- Runs 78 and 79: 0 accepted candidates; their evidence drove retry, segmentation, prompt-length and monotonic-growth improvements.
- Active building generator: **v14 prompt-safe-monotonic**.

## User production directive — high throughput + real validation
The user explicitly wants **many more sprites produced and tested, while still requiring genuine validation**. Production policy is therefore changed from conservative small batches to high-throughput candidate generation with exhaustive QA evidence, without weakening strict DONE.

Implemented in workflow commit `31a2233126f2dd9eb7d3093edddd816abe486eac`:
1. Default requested batch increased from **28 to 56 attempts** for future waves.
2. Workflow concurrency now uses `cancel-in-progress: false` so a new approved pulse cannot destroy an expensive active GPU generation run.
3. Every exported `*_final.png` must be represented in the generated GitHub QA report; a coverage mismatch fails the QA step.
4. Both Kaggle-side and GitHub-side contact sheets/reports are retained.
5. Full candidate PNGs and kernel logs remain in the evidence artifact.
6. Evidence retention increased from **30 to 90 days** for later audits/re-review.
7. High throughput does **not** relax semantic review or strict DONE gates.

## Wave 80
- Run: `34125123246`; job `101751899400`.
- Trigger commit: `5202d20d7b99efffe2225604b4ee1f0b4f2cfede`.
- Wave 80 started under the previous 28-attempt configuration and remains in progress on Kaggle at the latest check.
- Do not interfere with it. The new 56-attempt/exhaustive-QA workflow applies to subsequent waves.

## Immediate next actions
1. Query wave 80 first on the next intervention.
2. When complete, retrieve logs + complete artifact and review every emitted sprite/family.
3. Promote only genuinely valid families; integrate and require green Android CI before incrementing strict DONE.
4. For the next user-approved wave, use the new **56-attempt** policy and retain exhaustive QA evidence.
5. Continue improving yield from measured rejection reasons rather than weakening gates.
6. Finish buildings, then static assets, characters and FX with equivalent high-throughput + exhaustive validation lanes until **235 / 235 strict DONE**.

## Known unresolved targets
- Remaining building families after BLD-03.
- `TER-07` Expansion energy conduit unless superseded by accepted promotion.
- Dedicated character/FX production lane still required when building/static backlog falls.

## Operating principle
Maximize **validated sprites per GPU-hour**, not raw images. Generate broadly, reject aggressively, preserve evidence, and only increase strict DONE after full integration and CI proof.