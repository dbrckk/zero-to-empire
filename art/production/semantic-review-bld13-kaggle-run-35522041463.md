# BLD-13 semantic review — Kaggle run 35522041463

Date: 2026-09-20  
Verdict: **REJECT T0–T6**

All seven candidates passed technical QA, but the family reads primarily as the same radial/starburst nexus enlarged and decorated tier by tier. Normalized silhouette evidence confirms the issue: T0→T1 ≈ 0.974, T1→T2 ≈ 0.943 and T2 remains ≈ 0.936 versus the T0 anchor.

## v17.7 correction
- generic normalized-silhouette scale-ladder gate for every seven-tier building family;
- family-specific BLD-13 prompt grammar with side pylons, vertical core stages and stepped massing;
- text-to-image anchor resets at T1, T3 and T5 for BLD-13;
- automatic use of the rejection-memory ledger in building prompts;
- BLD-13-specific early-evolution thresholds.

No runtime promotion and no strict DONE increment from run 35522041463.
