# BLD-13 semantic review — Kaggle run 35524194030

Date: 2026-09-20  
Verdict: **REJECT T0–T6**

v17.7 successfully fixed the early radial scale ladder: T1 and T3 create real structural breaks, and T3/T4 establish a strong vertical nexus.

The remaining defect is late-tier continuity. T5 abruptly reverts from the vertical T4 architecture to a broad flat radial disc, with T6 continuing that new disc family. The alpha-bbox height/width ratio falls from about 1.107 at T4 to 0.761 at T5.

## v17.8 correction
- remove the T5 text-to-image reset;
- T5 evolves directly from T4 and T6 from T5;
- prompts explicitly preserve the tall central core and lateral citadels;
- add a late-tier aspect-ratio continuity gate to reject vertical-to-disc collapse.

No runtime promotion and no strict DONE increment from run 35524194030.
