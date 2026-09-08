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

## Wave 83 — ACTIVE v16.1 experiment
- Trigger commit `153ab7be267a8a1c8169b0374bac86a411795af0`.
- GitHub Actions run `34189278981`, job `101943816015`, run number 83.
- Latest check: still `in_progress` at `Wait for Kaggle`; all setup/auth/kernel-launch steps green.
- Requested 56 tiers using `building-family-flux-v16.1-shape-first-source-locked`.
- Do not launch a redundant wave while 83 is active.
- On completion retrieve artifacts/logs and compare true semantic acceptance against run82's 0/4 exported families.

## Run 82 baseline
Run `34145936891`, artifact `10030821750`, workflow SUCCESS.
- v15.2 requested 56 tiers; 28 technically validated exports across BLD-05/08/10/11.
- Semantic review rejected all 28 because cranes/gantries/booms and site/platform bases survived.
- Geometric boom detector has material false negatives and is not semantic truth.
- Review: `docs/art/reviews/RUN_82_SEMANTIC_REVIEW.md`.

## Generation-quality directive
Optimize source quality first. QA is a safety net, not the production strategy. Measure semantic acceptance rate × validated sprites/GPU-hour, never raw candidate count.

## Building generator v16.1
File `tools/sprites/kaggle_building_family_factory_v16.py`; startup `KAGGLE_STARTUP=building-family-flux-v16.1-shape-first-source-locked`.
- Positive family design cards and dedicated shape/massing cards.
- T0 shape-first; T1→T6 conservative source-locked evolution.
- Six T0 anchors; strongest two receive full progression.
- Silhouette-aware source filtering.
- v15.2 structural live QA retained only as secondary guard.

## Character lane — v1.1 square atlas
File `tools/sprites/kaggle_character_sheet_factory_v1.py`.
- Commit `4a48168166d47cbe47afc870aa8a8b65480e2b0b`.
- Every candidate sheet exactly 1024×1024 RGBA, fixed 4×4 grid of 256×256 cells, unused cells transparent.
- Semantic/runtime/CI validation still required before strict DONE.

## FX lane — v1.1 temporal semantics
File `tools/sprites/kaggle_fx_sheet_factory_v1.py`; commit `8a837c11a37be85bad0f5380557e99089895f67f`.
- Engine marker/report: `procedural-fx-v1.1-temporal-qa`.
- Candidate atlas remains explicit `horizontal-8`, 8 × 256×256 = 2048×256; this is NOT treated as a runtime contract until integration is implemented/proven.
- FX-00 welding sparks, FX-05 cyan pulse, FX-06 warm pulse and FX-07 construction dust/debris are explicitly classified as **one-shot** effects.
- FX-01/02 flames and FX-03/04 smoke/steam are classified as loops.
- One-shot QA now requires an internal peak and strong final decay; report records `mode`, `peak_frame`, `decay_ratio`, cell/layout metadata and per-frame alpha mass.
- FX-07 now generates polygonal ballistic rubble fragments in addition to expanding dust, preventing it from degenerating into generic smoke.
- One-shot sparks/pulses now use an attack/decay envelope rather than generic loop-like intensity.
- Runtime visibility, semantic review and green CI remain mandatory before strict DONE.

## FX runtime audit
- Manifest does not prescribe atlas dimensions/slicing for FX-00..07; it explicitly allows raster only when Canvas cannot match quality cheaply.
- FX-08..17 are `RUNTIME`.
- Repository search found no existing `zte_fx_` raster loader contract. Do not promote 2048×256 strips by assumption.
- Before strict FX integration, establish the actual Compose/Canvas/runtime integration point and prove frame slicing/visibility, or implement the effects procedurally if that is the cleaner production solution.

## Workflow reliability
- QA parser supports actual `assets` schema.
- Commit `6ac102f3327078cebb71df51d0aa41da672fe439` limits future Kaggle polling to 135 minutes so time remains to retrieve evidence.

## Immediate next actions
1. Query wave 83 first.
2. When complete, verify v16.1 startup and inspect every candidate full-resolution for cranes, site cards, people, vehicles, text, detached props, architecture identity and real tier progression.
3. Promote only genuinely valid complete families; then runtime/reference integration, manifest/progress reconciliation and green Android CI before strict increment.
4. If wave83 remains active, identify the concrete Android/Compose visual-effects integration point for FX and design the minimal proven loader/procedural contract rather than inventing one.
5. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. Lock correct architectural mass before detail, preserve approved source identity, reject bad sources before expensive evolution, validate during generation, and keep final QA strict.