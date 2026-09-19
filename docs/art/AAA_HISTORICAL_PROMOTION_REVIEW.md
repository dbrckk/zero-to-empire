# AAA historical promotion review queue

This queue protects the visual-quality bar. It lists assets that were promoted by generic/automatic technical workflows at some point and therefore require explicit confirmation that a later semantic/art review, runtime visibility check, and green Android CI justify keeping `DONE`.

**Rule:** technical validity (dimensions, transparency, alpha coverage, padding, file presence) is necessary but is not sufficient for `DONE`. Until explicit review evidence is confirmed, treat these entries as needing reconciliation rather than assuming they meet the AAA art-direction bar.

## Building families requiring evidence reconciliation

- BLD-02-T4 through BLD-02-T6
- BLD-03-T0 through BLD-03-T1
- BLD-04-T0 through BLD-13-T6

These families must preserve recognizable family identity while showing clear T0 → T6 growth in footprint, verticality, machinery density, materials and premium silhouette. Near-duplicate tiers, baked text/backgrounds, non-monotonic progression, generic architecture and perspective drift are rejection conditions.

## FX requiring evidence reconciliation

- FX-00 through FX-08
- FX-17

Each must have correct 4×2 / 8-frame runtime structure where applicable, clean padding, semantic match to its manifest role, active runtime visibility and reduced-motion behavior.

## Terrain requiring evidence reconciliation

- TER-07

The sprite must read as the required energy-conduit connector, remain seam-safe and isolated, and be visibly integrated in the correct terrain layer.

## Resolved example

- ONB-00 was initially promoted by generic runtime reconciliation, but later received an explicit authored integration plus a dedicated visual cleanup/review. Keep its dedicated provenance evidence rather than relying on the generic promotion.

## Promotion policy

A future `DONE` transition requires all of the following:

1. technical QA passes;
2. full-resolution semantic/art review passes against `AAA_WORLD_SPRITE_BIBLE.md`;
3. no baked text, watermark, rectangular background or detached artifact;
4. family/tier progression is coherent where applicable;
5. runtime code references the exact final asset and it is visible in gameplay;
6. Android CI is green on a commit containing that exact runtime;
7. review evidence is persisted under `art/production/` or an equivalent canonical review record.

Automatic candidate-generation/finalization workflows may advance only to `RUNTIME`. They must never set `DONE`.
