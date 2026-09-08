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

## Current trusted state — 2026-09-08 07:05 +02:00
- Strict ledger remains **112 / 235 DONE** pending evidence-based reconciliation.
- BLD-03-T2..T6 from run 75 remain integrated but not added to strict count without canonical/CI proof.
- Run 80: 21 technical candidates, semantic rejection 21/21; strict delta +0.
- Run 81: 56/56 technical candidates, semantic rejection 56/56; strict delta +0.
- Run 82: 28/56 exported after live QA, but semantic rejection 28/28; strict delta +0.

## Run 82 — completed and reviewed
GitHub Actions run `34145936891`, artifact `10030821750`, workflow SUCCESS.
- Generator: `v15.2-live-semantic-validation`.
- 56 tiers requested; 28 technically validated exports.
- Accepted technical families: BLD-05, BLD-08, BLD-10, BLD-11 (7 tiers each).
- Rejected before export: BLD-04, BLD-09, BLD-12, BLD-13.
- 32 anchor attempts, 16 branch attempts, 117 contextual attempts, 42 live rejections, 10 early branch aborts.
- Kernel generation reached ~8,489 s (~141.5 min).
- Semantic review of the contact sheet rejected all 28 exports. Every accepted family still visibly contains orange/yellow construction cranes, gantries/booms or temporary site equipment; broad site/platform bases also remain.
- Critical detector failure: branch report can say `max-boom=0.00` while large cranes are visually obvious. Geometric `boom_score()` has false negatives and cannot be treated as semantic crane validation.
- Review document: `docs/art/reviews/RUN_82_SEMANTIC_REVIEW.md`, commit `b7d205f0fb5e2b1ef3cf0cae8c8c39c519472d78`.
- No run82 candidate promoted.

## Wave 83 — launched with source-quality architecture
- Trigger commit: `153ab7be267a8a1c8169b0374bac86a411795af0`.
- GitHub Actions run: `34189278981`, run number 83.
- At launch it is queued.
- Generator requested: `building-family-flux-v16.1-shape-first-source-locked`.
- Requested count: 56.
- This is the first production wave intended to test v16.1 rather than attempting to repair v15.x outputs after generation.

## Generation-quality directive — prevent invalidation at source
The user explicitly requires image generation itself to be substantially better so later semantic invalidation becomes exceptional rather than normal. Optimize **source quality first**, with QA acting as a safety net rather than the primary filter.

## Building generator v16.1 — shape-first positive source locking
File: `tools/sprites/kaggle_building_family_factory_v16.py`.
Startup marker: `KAGGLE_STARTUP=building-family-flux-v16.1-shape-first-source-locked`.
Future building waves are routed to it by `81f469593636623cb4751d7385743fb50e19b01b`.

v16.1 generation policy:
1. Positive family design cards give each building a concrete industrial identity.
2. Dedicated SHAPE cards define architectural massing before machinery detail.
3. T0 is generated from shape/massing first; T1→T6 evolve that approved source and add attached/integrated industrial detail.
4. No long forbidden-object lists that make unwanted motifs salient.
5. Encoder-aware prompts: CLIP gets shape+tier essentials; T5 gets complete positive specification.
6. Source locking strengths `.22,.27,.32,.37,.42,.47` preserve identity.
7. T0 uses 8 inference steps; later tiers 6–8.
8. Six T0 anchors; only strongest two receive full progression.
9. v15.2 structural live QA remains underneath as a secondary safety net, not as semantic truth.
10. T0 silhouette filter prefers aspect >= .82, upper mass <= .50, top spike <= .14 and lower mass >= .50.

## Workflow reliability
- QA parser supports actual `assets` report schema.
- Commit `6ac102f3327078cebb71df51d0aa41da672fe439` limits future Kaggle polling to 135 minutes inside the 180-minute job so time remains to retrieve partial outputs/logs/evidence.

## Character lane
- `tools/sprites/kaggle_character_sheet_factory_v1.py`.
- Identity anchor + img2img pose evolution, transparent isolation, fixed feet pivot, silhouette/cycle QA.

## FX lane
- `tools/sprites/kaggle_fx_sheet_factory_v1.py`.
- Procedural transparent sheets with live per-frame and sheet-level QA.

## Immediate next actions
1. Query wave 83 first on the next intervention.
2. When complete, verify startup marker is v16.1 and inspect every exported family visually/full resolution.
3. Primary experiment metric: crane/site contamination rate and actual semantic family acceptance versus run82's 0/4 exported families.
4. If v16.1 still generates cranes at T0, do not merely tighten `boom_score`; change source generation/model conditioning before another mass wave.
5. Promote only genuinely valid complete families, integrate runtime/references, reconcile manifest/progress and require green Android CI before strict increment.
6. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. Lock correct architectural mass before detail, preserve approved source identity, reject bad sources before expensive evolution, validate during generation, and keep final QA strict. Optimize for **semantic acceptance rate × validated sprites per GPU-hour**, never raw image count alone.