# Run 81 semantic review — strict rejection

GitHub Actions run: `34132705535`
Kaggle engine: `v15-multibranch-semantic-safe`
Requested tiers: 56
Kaggle exports: 56
Families exported: BLD-04, BLD-05, BLD-08, BLD-09, BLD-10, BLD-11, BLD-12, BLD-13 (T0→T6 each)

## Technical result
Kaggle completed successfully. The kernel reported:
- `KAGGLE_BUILDING_SUCCESS=56`
- `KAGGLE_BUILDING_REJECTED=0`
- `KAGGLE_BUILDING_ATTEMPTED=56`
- `KAGGLE_FRESH_CANDIDATES=56`
- `QA_TOTAL=56 QA_AUTO_PASS=56 QA_REVIEW=0`
- `KAGGLE_EXPORT_COUNT=56`

The GitHub job conclusion was failure only because the workflow parsed the QA report using obsolete keys (`sprites` / `results`). The actual report schema stores entries under `assets`, so the workflow computed `QA_REPORT_TOTAL=0` despite 56 candidates. This is a CI-gate bug, not a generation failure.

## Branch-search result
- 32 T0 anchor attempts.
- 16 full branch attempts.
- 8/8 selected families passed v15 family metrics.
- Selected-family growth was strong (roughly 2.7×–3.5× T0→T6) and adjacent IoU remained high enough for family continuity.

## Full-resolution semantic review
**Decision: reject 56 / 56. Strict DONE delta: +0.**

The batch is materially better in family continuity and visible progression than runs 77–80, but a systematic semantic contaminant remains.

### Dominant rejection reasons
1. **Construction cranes / hoists / long orange boom arms** appear across nearly every family and many tiers. They become a repeating visual motif and violate the isolated final-building contract.
2. **Broad platform / slab / site-card bases** remain visible around many buildings. The assets read as miniature construction dioramas rather than clean isolated runtime buildings.
3. Several tiers include **loose site furniture / detached industrial props** near the footprint boundary.
4. Some late tiers preserve the same construction-site language instead of reading as a finished, occupied production facility.

### Positive evidence
- No longer a zero-yield pipeline.
- T0→T6 scale progression is clear.
- Family identity is much more coherent than run 77.
- Alpha extraction and technical framing are generally stable.
- Multi-anchor branch search is useful and should be retained.

## Required correction before promotion
- Keep v15 multi-anchor selection.
- Use v15.1 live per-tier validation for future waves.
- Strengthen generation language against cranes/hoists/scaffolding/site equipment.
- Add an explicit high-altitude thin-boom contamination heuristic so long crane arms can be rejected during generation, not only by human review.
- Tighten slab/site-card detection without rejecting legitimate connected lower building masses.
- Fix the GitHub QA parser to accept the actual `assets` schema.

No run-81 candidate is promoted to runtime.