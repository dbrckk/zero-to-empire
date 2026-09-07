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

## Current trusted state — 2026-09-07 20:26 +02:00
- Strict ledger remains **112 / 235 DONE** pending evidence-based reconciliation.
- BLD-03-T2..T6 from run 75 remain integrated but not added to strict count without canonical/CI proof.
- Run 80: 21 technical candidates, semantic rejection 21/21; strict delta +0.
- Run 81: 56/56 technical candidates across 8 complete families, semantic rejection 56/56 due mainly to crane/boom contamination and broad site-card bases; strict delta +0.

## Run 81 evidence
GitHub Actions run `34132705535`, artifact `10026804547`.
- 56 exports across BLD-04,05,08,09,10,11,12,13 T0→T6.
- Multi-branch continuity and visible tier growth were strong.
- Dominant semantic failure was source-generation bias toward construction-site motifs, not lack of raw yield.
- Workflow QA parser bug (`assets` schema) fixed in commit `6321ddc31fea331f46ed83310926dfe2e45f2e24`.
- Semantic review: `docs/art/reviews/RUN_81_SEMANTIC_REVIEW.md`.

## Wave 82 — active checkpoint
- Trigger commit: `44ecebae70c3a52ca5a33d3d8f72c30783efafb4`.
- GitHub Actions run: `34145936891`, job `101817872065`.
- Requested 56 tiers.
- At 20:26 +02:00 it remains `in_progress` at `Wait for Kaggle`; setup/auth/kernel launch are green.
- It was triggered with v15.2 live semantic validation before v16/v16.1 landed; do not discard the active run merely to hot-swap generators.
- Job logs are not yet downloadable while the live blob is unavailable; inspect artifacts/logs immediately after completion.

## Generation-quality directive — prevent invalidation at source
The user explicitly requires image generation itself to be substantially better so later semantic invalidation becomes exceptional rather than normal. The pipeline must therefore optimize **source quality first**, with QA acting as a safety net rather than the primary filter.

## Building generator v16.1 — shape-first positive source locking
Created from v16 and upgraded in commit `cd9e125482f4df2426803f3feda05cc423e423b2`.
Startup marker: `KAGGLE_STARTUP=building-family-flux-v16.1-shape-first-source-locked`.
Future building waves are routed to `tools/sprites/kaggle_building_family_factory_v16.py` by commit `81f469593636623cb4751d7385743fb50e19b01b`.

v16.1 generation policy:
1. **Positive family design cards** give each building a concrete industrial identity instead of generic industrial wording.
2. **Dedicated SHAPE cards** define only architectural massing for each family: broad/low blocks, attached wings, compact roof masses, enclosed centers.
3. **Two-phase prompting.** T0 is generated from shape/massing first with deliberately sparse machinery detail. T1→T6 then evolve that approved source and introduce only attached/integrated industrial detail.
4. **No long forbidden-object lists.** Desired geometry and architecture are described positively so construction motifs are not made salient by the prompt itself.
5. **Encoder-aware prompts.** CLIP receives only family shape + tier essentials; T5 receives the complete positive specification.
6. **Stronger source locking.** Img2img strengths reduced further to `.22,.27,.32,.37,.42,.47` for T1→T6 so upgrades preserve the approved source instead of re-inventing the scene.
7. **More deliberate T0 search.** T0 uses 8 inference steps; later tiers 6–8.
8. **Six T0 anchors** per family; only the strongest two receive expensive full progression.
9. v15.2 live boom/slab/context QA remains underneath v16.1 for retries and early branch abort.
10. Strict semantic review remains mandatory, but target behavior is confirmation rather than routine rejection.

## v16.1 silhouette-aware source filtering
- Every T0 anchor is analyzed before expensive branch evolution using its 64×64 alpha silhouette.
- Metrics: width/height aspect ratio, upper-mass fraction, lower-mass fraction and top-spike fraction.
- Thresholds were tightened in v16.1: prefer aspect >= .82, upper mass <= .50, top spike <= .14 and lower mass >= .50.
- Narrow/tall, top-heavy or spike-dominated starters are heavily penalized before branch selection.
- Logs emit `KAGGLE_V16_SILHOUETTE ...` for empirical threshold tuning.

## Character lane
- Factory: `tools/sprites/kaggle_character_sheet_factory_v1.py` (`5bec3b27922106c6d2120cf28b56a008aeb4b026`).
- Routed automatically after building/static backlog.
- Identity anchor + img2img pose evolution, transparent isolation, fixed feet pivot, silhouette/cycle QA.

## FX lane
- Factory: `tools/sprites/kaggle_fx_sheet_factory_v1.py` (`80f59093fbe5ece291ee4f057e1b780c7b2539e5`).
- Routed automatically after character/static backlog.
- Procedural transparent sheets with live per-frame and sheet-level QA.

## Immediate next actions
1. Query wave 82 first on the next intervention.
2. When wave 82 completes, retrieve logs/artifacts and measure whether v15.2 reduced crane/boom/slab contamination.
3. Subsequent building waves use **v16.1 shape-first positive source locking + silhouette-aware anchor filtering** from current `main`.
4. Measure semantic acceptance rate, not just candidate count; recurrent motifs must trigger source-generation changes before another large batch.
5. Promote only genuinely valid families; integrate runtime/references, reconcile manifest/progress and require green Android CI before strict increment.
6. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. Lock the correct architectural mass before adding detail, preserve approved source identity, reject bad source silhouettes before expensive evolution, validate during generation, and keep final QA strict. Optimize for **semantic acceptance rate × validated sprites per GPU-hour**, never raw image count alone.
