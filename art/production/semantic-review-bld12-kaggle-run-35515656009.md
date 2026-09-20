# BLD-12 semantic review — Kaggle run 35515656009

Date: 2026-09-20
Verdict: **REJECT**

7/7 passed technical QA, but T0-T5 still read as one circular Reality Engine wheel scaled upward. T6 finally changes to a different square containment architecture.

v17.6 changes generation strategy: T1 and T3 are fresh text-to-image anchor resets under the same family style/camera/material prompt. T2 evolves T1; T4-T6 evolve T3. At least two of the first three adjacent transitions must now have normalized silhouette IoU below 0.900.

No runtime promotion and no strict DONE increment from run 35515656009.
