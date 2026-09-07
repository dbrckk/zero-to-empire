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

## Current trusted state — 2026-09-07 19:05 +02:00
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

## Wave 82
- Trigger commit: `44ecebae70c3a52ca5a33d3d8f72c30783efafb4`.
- GitHub Actions run: `34145936891`.
- Requested 56 tiers.
- It was triggered with v15.2 live semantic validation before v16 landed; do not discard an already-running expensive run merely to hot-swap generators.
- v15.2 adds live boom/slab detection, fresh-seed tier retries and early branch abort.

## Generation-quality directive — prevent invalidation at source
The user explicitly requires image generation itself to be substantially better so later semantic invalidation becomes exceptional rather than normal. The pipeline must therefore optimize **source quality first**, with QA acting as a safety net rather than the primary filter.

## Building generator v16 — positive source locking
Created `tools/sprites/kaggle_building_family_factory_v16.py` in commit `074ca0297aebfa8fce485e2456b4705f885950ef`, then tightened encoder-safe prompts in `4e9f4f5612015a823917f744f0e918072049fd32`.
Router switched future building waves to v16 in commit `81f469593636623cb4751d7385743fb50e19b01b`.
Startup marker: `KAGGLE_STARTUP=building-family-flux-v16-positive-source-locked`.

v16 generation policy:
1. **Positive design cards per building family.** Each of the 14 families has a concrete architectural identity and integrated production mechanism instead of generic “industrial” language.
2. **Positive tier blueprints.** T0→T6 specify concrete attached industrial expansion, avoiding vague prestige/hero wording that previously drifted toward civic towers or construction motifs.
3. **No long negative-object lists in prompts.** FLUX Schnell can make repeatedly named forbidden concepts salient; v16 describes only the desired finished object and integrated machinery.
4. **Encoder-aware prompting.** CLIP receives a deliberately short identity/tier prompt; complete design constraints go to T5. Critical concepts no longer fall beyond CLIP’s short context window.
5. **Source locking via conservative img2img.** Tier strengths reduced to `.24,.29,.34,.39,.44,.49` so accepted family identity is preserved instead of being re-invented every upgrade.
6. **More deliberate inference.** Generation steps increased to 6–8 depending on tier.
7. **Six T0 anchors** are generated per family; only the strongest two are evolved, increasing source diversity before expensive progression.
8. v15.2 live geometric QA remains underneath v16: bad anchors/tiers can still be rejected, regenerated and early-aborted.
9. Full-resolution semantic review remains mandatory, but the target is now for it to confirm quality rather than routinely reject entire batches.

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
2. If wave 82 completes, inspect every candidate and measure whether v15.2 eliminated boom/slab contamination.
3. Regardless of wave-82 outcome, subsequent building waves use **v16 positive source locking** from current `main`.
4. Measure semantic acceptance rate, not just candidate count. If v16 still shows a recurrent motif, change the family design card/positive blueprint before generating another large batch.
5. Promote only genuinely valid families; integrate runtime/references, reconcile manifest/progress and require green Android CI before strict increment.
6. Continue buildings → statics → characters → FX until **235 / 235 strict DONE**.

## Operating principle
Generate the right asset first. Use precise positive design specifications, preserve approved source identity, validate during generation, and keep final QA strict. Optimize for **semantic acceptance rate × validated sprites per GPU-hour**, never raw image count alone.