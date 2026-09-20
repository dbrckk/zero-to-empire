# BLD-12 gate calibration — Kaggle run 35508938195

Date: 2026-09-20

Run 220 used v17.2 and produced three complete branches but exported no candidate because all branch scores were forced to -999 by the structural gate.

Most relevant branch (branch 4):
- T1 adjacent normalized IoU: 0.963
- T2 adjacent: 0.899
- T3 adjacent: 0.893
- T4 adjacent: 0.908
- T5 adjacent: 0.880
- T6 adjacent: 0.849
- T3 anchor IoU: 0.927
- T5 anchor IoU: 0.855
- T6 anchor IoU: 0.841

This branch contains five substantial adjacent structural transitions (<0.920), so it is not a clone ladder. The old T3 and T6 cumulative ceilings rejected it by 0.002 and 0.001 respectively.

v17.4 calibration:
- T3 anchor ceiling: 0.930
- T6 anchor ceiling: 0.845
- T1 ceiling remains 0.965
- T5 ceiling remains 0.860
- at least three substantial adjacent transitions remains mandatory
- all technical/no-site/halo/manual-semantic gates remain mandatory

No candidate from run 35508938195 is promoted.
