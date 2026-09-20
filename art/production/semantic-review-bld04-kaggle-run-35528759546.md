# BLD-04 semantic review — Kaggle run 35528759546

Date: 2026-09-20
Verdict: **REJECT T0–T6**

## Technical result
- 7/7 candidates passed technical QA;
- selected branch score 4.425;
- normalized silhouette metrics showed some structural variation.

## Semantic blockers
- the family still reads primarily as the same cyan office block scaled upward;
- every tier includes a surrounding site/platform rather than an isolated building;
- trees, paths, landscaping and outdoor props remain fused into the asset;
- T5/T6 add more site decoration instead of a premium architectural mastery transition.

## v18.1 correction
- family-specific BLD-04 tier grammar;
- front-loaded CLIP rule: building only, no site, no trees, no paths, no outdoor props;
- shorter T5 prompt to avoid truncating the no-site contract;
- rejection-memory hint from this run.

No runtime promotion and no strict DONE increment.
