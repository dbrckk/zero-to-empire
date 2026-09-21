# BLD-13 semantic review — Kaggle run 35564401834

Date: 2026-09-21  
Verdict: **REJECT T0–T6**

All seven candidates passed technical QA, and v17.8 fixes the previous T4→T5 vertical-to-disc collapse: the measured aspect ratios remain stable from T3 through T6 (0.891, 0.883, 0.900, 0.930), while the branch search selected branch 6 with score 4.061.

The family still fails strict semantic/premium review:

- T0 contains visible generated title/text contamination ("Transcendent Nexus").
- T1–T2 are radial/starburst structures while T3–T6 abruptly switch to a four-pylon vertical citadel family. This is a family-identity discontinuity, not a coherent tier evolution.
- T5 contains obvious generated logo/pseudo-text/watermark contamination ("ATRA" and smaller lettering) plus detached foreground debris.
- Several tiers carry large baked cast shadows / site-like dark slabs that weaken clean runtime compositing.

## Next correction

- Keep one persistent architectural DNA from T0 through T6: central vertical nexus + connected side pylons must already be readable in early tiers.
- Forbid all readable text, logos, watermarks, signage and pseudo-brand marks; reject candidates with text-like contamination before semantic review.
- Avoid detached debris and baked ground/site shadows; export only the connected structure on transparent background.
- Preserve the successful late-tier aspect-ratio continuity gate.
- Add a family-continuity check across the T2→T3 transition so an anchor reset cannot silently replace the building family.

No runtime promotion and no strict DONE increment from run 35564401834.
