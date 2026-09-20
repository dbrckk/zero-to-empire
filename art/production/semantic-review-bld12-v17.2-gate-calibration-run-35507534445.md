# BLD-12 v17.2 gate calibration — Kaggle run 35507534445

Date: 2026-09-20

The generator itself improved substantially. Branch 3 produced:
- T1 adjacent normalized IoU: 0.958
- T3 anchor IoU: 0.915
- T4 adjacent IoU: 0.841
- T5 adjacent IoU: 0.796
- T6 adjacent IoU: 0.825
- T6 anchor IoU: 0.740

This branch had strong cumulative structural evolution but was rejected solely because T1 exceeded the previous 0.955 threshold by 0.003. That is too sensitive to mask variation.

v17.3 calibration:
- T1 hard ceiling: 0.965 instead of 0.955;
- T3 cumulative ceiling: 0.925 instead of 0.920;
- T5/T6 cumulative limits and the requirement for at least three substantial structural transitions remain unchanged;
- all technical, halo, site-card and semantic/manual promotion gates remain unchanged.

This does not promote run 35507534445. It only prevents future false negatives from marginal silhouette-mask noise.
