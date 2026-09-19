# BLD-04 Kaggle semantic review — pass 4

Date: 2026-09-19
Source run: 35450072283
Result: **REJECT — family coherence passed, tier evolution failed**

## What improved
- All 7 candidates passed strict technical QA.
- Tech Company family identity is consistent across T0→T6.
- Camera, materials, isolation and transparent extraction are coherent.

## Why the family is still rejected
The sequence is effectively the same building enlarged from tier to tier. Visible ratio rises from 12.1% to 34.8%, but the architectural silhouette changes too little.

The canonical building-family contract requires growth in:
- footprint;
- verticality;
- machinery density;
- attached functional volumes;
- material/prestige complexity;
- premium silhouette.

Pure or near-pure scaling is not sufficient.

## Next pass
Use Kaggle v16.6:
- stronger but still bounded img2img evolution;
- explicit structural additions for every tier;
- automatic normalized-silhouette IoU ceiling so a resized clone is rejected before semantic review;
- candidate-only output, no runtime promotion.

Strict DONE is unchanged by this rejection.
