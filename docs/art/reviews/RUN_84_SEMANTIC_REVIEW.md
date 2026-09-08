# Run 84 Semantic Review

## Evidence
- Original GitHub run: `34200990117` (collector timeout while Kaggle still RUNNING).
- Recovery run: `34219375395` (SUCCESS).
- Recovery artifact: `10053866830` (`kaggle-recovered-sprite-batch`, ~33.6 MB).
- Generator startup confirmed: `building-family-flux-v16.2-shape-first-recursion-safe`.
- No recursion failure. `KAGGLE_V16_SILHOUETTE` scoring executed normally.

## Technical result
- 48 anchors, 16 branch attempts, 128 context attempts.
- 61 live rejections, 13 early aborts.
- 21 technically valid candidates exported.
- Accepted technical families: BLD-11, BLD-12, BLD-13 (T0-T6 each).
- `KAGGLE_BUILDING_SUCCESS=21`, `KAGGLE_BUILDING_REJECTED=35`, `KAGGLE_FRESH_CANDIDATES=21`.

## Semantic result
**0 / 21 promoted. Strict delta: +0.**

### BLD-11 — reject family
- Strong improvement over run82: no dominant crane/gantry contamination.
- Still invalid as isolated final sprite family: broad square floor/site slab remains under the structure.
- T5/T6 bake visible exhaust/flame/smoke into the static building sprite.
- Detached shadow/blob residue appears outside the main object footprint.
- Small loose roof/ground props remain.

### BLD-12 — reject family
- Coherent industrial identity and progression; cranes are absent.
- Broad ground/platform slab remains part of the rendered object.
- T6 contains stray thin line/fragment residue around the base.
- Smoke is baked into the static sprite rather than handled as an FX/runtime layer.
- External equipment reads partially as site dressing instead of strictly integrated architecture.

### BLD-13 — reject family
- Best semantic family of run84: coherent factory identity, strong source locking, no crane construction-site bias.
- T0 still contains loose service props/barrel-like objects under/around the structure.
- A large cast-shadow/ground patch remains outside the structural foundation silhouette.
- Later tiers preserve the shadow/ground treatment and increasingly dense exterior details.
- Not clean enough for the canonical one-object transparent-sprite contract.

## Comparison to run82
Run82: 4 technically accepted families, all semantically rejected primarily because of cranes/gantries/site construction motifs.
Run84: 3 technically accepted families, all semantically rejected, but **crane/gantry contamination is substantially reduced**. The dominant remaining defects are now ground pads/cast shadows, detached residue, loose props, and baked exhaust/smoke.

## Generator conclusion
The v16 shape-first/source-locking direction is validated as an improvement, but source generation must become cleaner before another large batch. Do not merely tighten post-hoc QA. The next generator should explicitly produce a static isolated architectural object whose alpha silhouette ends at the structural foundation, with all utilities physically attached and no emitted smoke/flame or loose site objects.
