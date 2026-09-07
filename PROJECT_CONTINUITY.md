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

## Current trusted state — 2026-09-07 17:58 +02:00
- Strict ledger remains **112 / 235 DONE** pending evidence-based reconciliation.
- BLD-03-T2..T6 from run 75 remain integrated but not added to strict count without canonical/CI proof.
- Run 80 completed SUCCESS with 21 technical candidates but semantic review rejected 21/21; strict delta +0.

## High-throughput + live-validation policy
- Workflow default: 56 manifest tiers.
- `cancel-in-progress: false` protects expensive active GPU runs.
- Every exported sprite must be represented in QA evidence.
- Full candidates, contact sheets, reports and logs retained for 90 days.
- Buildings v15.1 perform contextual QA while generating: immediate rejection/regeneration of bad tiers and early branch abort.
- Character and FX lanes also perform per-frame/per-sheet QA before export.
- Strict semantic review, runtime integration and green Android CI remain mandatory.

## Wave 81 — still active
- Trigger commit: `bfd3ea0fea08c78fa36f0d3ab5c100a1608a2566`.
- GitHub Actions run: `34132705535`.
- Workflow job: `101776405808`.
- At 17:58 +02:00 it remains `in_progress` at `Wait for Kaggle`; setup/auth/kernel launch are green.
- Wave 81 uses the earlier v15 multi-branch generator because it cloned before v15.1 live-validation landed.
- Do not cancel or replace the active run. The next wave will use current `main` with live validation.

## Building generator — v15.1 live validation
Commit `608ab41178a8080da1c30b7269b6c5d6c38da5d6`.
- Up to 4 T0 anchors.
- Immediate starter QA.
- Every T1→T6 tier checked against prior accepted frames.
- Fresh-seed retry on contextual failure.
- Up to 3 contextual attempts per tier.
- Early branch abort after repeated failure.
- `branch-search-report.json` records context attempts, live rejections and early aborts.

## Character lane
- Factory: `tools/sprites/kaggle_character_sheet_factory_v1.py` (`5bec3b27922106c6d2120cf28b56a008aeb4b026`).
- Routed automatically after building/static backlog via `kaggle/github_mass_factory.py`.
- Identity anchor + img2img pose evolution, transparent isolation, fixed feet pivot, silhouette/cycle QA.
- `character-sheet-report.json` retained in workflow artifacts.

## FX lane — blocker removed
Created `tools/sprites/kaggle_fx_sheet_factory_v1.py` in commit `80f59093fbe5ece291ee4f057e1b780c7b2539e5`.
- Covers all manifest TODO FX sheets using deterministic procedural generation rather than wasting FLUX compute on simple transient effects.
- Produces 8-frame transparent sheets at 256px cells.
- Supports sparks, flames/plasma, smoke/steam/dust, energy pulses, electric arcs, scan sweep, thruster/trails, distortion/singularity and shimmer-style effects.
- Live validation occurs per frame: non-empty alpha, coverage bounds, no edge contact.
- Sheet QA checks adjacent duplicates and center drift.
- Up to 4 regeneration attempts per FX sheet before rejection.
- Emits `KAGGLE_FX_LIVE_PASS` / `KAGGLE_FX_LIVE_REJECT` and `fx-sheet-report.json`.

Routing commit `f1b3cdf8839d9dcb13cd6386f09252e29cbcc883` updates `kaggle/github_mass_factory.py` to route remaining FX backlog through the dedicated factory instead of failing unsupported.
Workflow commit `b0b95d0253715e37e2c1bde2ec64ed8e974a7f7b` preserves `fx-sheet-report.json` in the 90-day QA artifact.

## Immediate next actions
1. Query run `34132705535` first on the next intervention.
2. When wave 81 completes, retrieve logs, branch-search report, QA reports and all candidate PNGs; perform full-resolution semantic review.
3. Launch the next user-approved wave only after extracting wave-81 evidence; it will use v15.1 live validation.
4. Compare validated yield per GPU-hour against wave 81 using live rejection/abort metrics.
5. Promote only genuinely valid families, integrate runtime/references, reconcile manifest/progress and require green Android CI before strict increment.
6. Test the character and FX factories on Kaggle before relying on them for strict completion.
7. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Known unresolved targets
- Remaining building families after BLD-03.
- `TER-07` Expansion energy conduit unless superseded by accepted promotion.
- Character/FX candidate factories now exist, but still require real Kaggle test runs and semantic review before any strict DONE credit.

## Operating principle
Maximize **validated sprites per GPU-hour**. Validate early, regenerate locally, abort doomed work early, preserve evidence, and never weaken final semantic/runtime/CI gates.