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

## Current trusted state — 2026-09-08
- Strict ledger remains **112 / 235 DONE** pending evidence-based reconciliation.
- Run 80: 21 technical candidates, semantic rejection 21/21; strict delta +0.
- Run 81: 56/56 technical candidates, semantic rejection 56/56; strict delta +0.
- Run 82: 28/56 exported after live QA, semantic rejection 28/28; strict delta +0.

## Run 82 — completed and reviewed
GitHub Actions run `34145936891`, artifact `10030821750`, workflow SUCCESS.
- Generator: `v15.2-live-semantic-validation`.
- 56 tiers requested; 28 technically validated exports.
- Accepted technical families: BLD-05, BLD-08, BLD-10, BLD-11.
- 117 contextual attempts, 42 live rejections, 10 early branch aborts.
- Semantic review rejected all 28 because construction cranes/gantries/booms and site/platform bases survived.
- Geometric boom detector has material false negatives and is not semantic truth.
- Review: `docs/art/reviews/RUN_82_SEMANTIC_REVIEW.md`.

## Wave 83 — ACTIVE v16.1 experiment
- Trigger commit `153ab7be267a8a1c8169b0374bac86a411795af0`.
- GitHub Actions run `34189278981`, job `101943816015`, run number 83.
- Latest check: `in_progress` at `Wait for Kaggle`; setup/auth/kernel launch all green.
- Requested 56 tiers using `building-family-flux-v16.1-shape-first-source-locked`.
- Do not launch a redundant wave while 83 is active.
- On completion, retrieve artifacts/logs and compare true semantic acceptance against run82's 0/4 exported families.

## Generation-quality directive
Optimize source quality first. QA is a safety net, not the production strategy. Measure semantic acceptance rate × validated sprites/GPU-hour, never raw candidate count.

## Building generator v16.1
File `tools/sprites/kaggle_building_family_factory_v16.py`; startup `KAGGLE_STARTUP=building-family-flux-v16.1-shape-first-source-locked`.
- Positive family design cards.
- Dedicated shape/massing cards before machinery detail.
- T0 shape-first; T1→T6 conservative source-locked evolution.
- Encoder-aware prompts.
- Six T0 anchors, strongest two receive full progression.
- Silhouette-aware source filtering.
- v15.2 structural live QA retained as secondary guard only.

## Character lane — v1.1 square atlas fix
File `tools/sprites/kaggle_character_sheet_factory_v1.py`.
- Commit `4a48168166d47cbe47afc870aa8a8b65480e2b0b` fixes a known contract mismatch before the lane is exercised.
- Startup marker now `character-sheet-flux-v1.1-identity-pivot-square-atlas`.
- Every candidate sheet is exactly **1024×1024 RGBA**, matching the manifest contract.
- Fixed 4×4 grid of 256×256 cells; unused cells remain transparent.
- Supports current 6/8/10-frame actions without variable atlas heights.
- Report now records atlas/cell dimensions and generation asserts exact 1024×1024 before export.
- Semantic/runtime/CI validation still required before strict DONE.

## FX lane
- `tools/sprites/kaggle_fx_sheet_factory_v1.py`.
- Procedural transparent sheets with live per-frame and sheet-level QA.
- Before strict integration, verify runtime frame slicing/layout expectations against current 2048×256 strips.

## Workflow reliability
- QA parser supports actual `assets` schema.
- Commit `6ac102f3327078cebb71df51d0aa41da672fe439` limits future Kaggle polling to 135 minutes so time remains to retrieve evidence.

## Immediate next actions
1. Query wave 83 first.
2. When complete, verify v16.1 startup and inspect every candidate full-resolution for cranes, site cards, people, vehicles, text, detached props, architecture identity and real tier progression.
3. Promote only genuinely valid complete families; then runtime/reference integration, manifest/progress reconciliation and green Android CI before strict increment.
4. If wave83 remains active, continue non-conflicting pipeline hardening; next priority is FX runtime atlas/layout verification.
5. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. Lock correct architectural mass before detail, preserve approved source identity, reject bad sources before expensive evolution, validate during generation, and keep final QA strict.