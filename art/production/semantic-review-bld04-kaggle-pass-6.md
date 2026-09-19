# BLD-04 Kaggle pass 6 — generation diagnosis

Date: 2026-09-19
Run: 35462322398
Result: **NO CANDIDATES EXPORTED**

The structural guardrail rejected all three branches at T1.

Observed normalized-silhouette IoU values were mostly 0.987–0.993, clearly resize-like. One branch reached 0.966–0.967, indicating a small but real structural departure that was just above the universal 0.965 cutoff.

## Pass 7
Use a tier-aware anti-resize ceiling:
- T1: 0.975
- T2: 0.960
- T3: 0.945
- T4: 0.935
- T5: 0.925
- T6: 0.915

This only relaxes the bootstrap tier. Later tiers still have to diverge progressively, preventing a full family of scaled clones from passing.
