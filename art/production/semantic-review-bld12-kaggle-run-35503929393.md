# BLD-12 semantic review — Kaggle run 35503929393

Date: 2026-09-20  
Verdict: **REJECT**

## Technical result
All seven Reality Engine candidates passed the existing technical QA and were exported for semantic review.

## Semantic rejection
T0 through T5 are still predominantly the same low circular containment-ring silhouette enlarged and incrementally decorated. The required structural evolution is not present. T6 finally changes massing, but one late discontinuity does not make the seven-tier progression acceptable.

Measured normalized silhouette IoU:
- T0→T1: 0.973
- T1→T2: 0.952
- T2→T3: 0.939
- T3→T4: 0.933
- T4→T5: 0.924
- T5→T6: 0.896
- T0→T3: 0.957
- T0→T5: 0.912
- T0→T6: 0.870

The old thresholds were being passed by very small silhouette changes just below each per-tier ceiling.

## v17.2 correction
- add Reality Engine-specific structural instructions for every tier;
- increase img2img freedom only for BLD-12, leaving other families unchanged;
- require cumulative departure from T0 at T3, T5 and T6;
- require at least three substantial adjacent structural transitions;
- preserve all existing technical, no-site-card, halo and manual semantic-promotion gates.

No runtime promotion and no strict DONE increment from this rejected run.
