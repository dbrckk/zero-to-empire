# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **223/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | 38185962170 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.105 |
| CHR-OP-WORK | OP | WORK | AWAITING_REVIEW | 38185962170 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | 38185962170 | Kaggle generator rejected candidate: frame-4-failed; retry-details=detached-artifact component=3930/8360 / detached-artifact component=3800/9305 / detached-artifact component=3794/9110 / detached-artifact component=3872/9238 |
| CHR-OP-REPAIR | OP | REPAIR | DISPATCHED | 38185962170 | Kaggle generator rejected candidate: identity/silhouette jump=0.10; retry-details=edge contact |
| CHR-OP-CELEB | OP | CELEB | AWAITING_REVIEW | 38185962170 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-WALK | LOG | WALK | REJECTED_SEMANTIC | 38185962170 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.112 |
| CHR-LOG-WORK | LOG | WORK | AWAITING_REVIEW | 38185962170 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-CARRY | LOG | CARRY | AWAITING_REVIEW | 38185962170 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-REPAIR | LOG | REPAIR | REJECTED_SEMANTIC | 38185962170 | Kaggle generator rejected candidate: image-risk:LOWER_LIMB_STRUCTURE_UNVERIFIED,PALETTE_IDENTITY_DISCONTINUITY_RISK; retry-details=edge contact |
| CHR-LOG-CELEB | LOG | CELEB | REJECTED_SEMANTIC | 38185962170 | Kaggle generator rejected candidate: frame-3-failed; retry-details=edge contact |
| CHR-ENG-IDLE | ENG | IDLE | DISPATCHED | 38170795132 | Kaggle generator rejected candidate: frame-0-failed; retry-details=detached-artifact component=10558/10611 / detached-artifact component=10510/10546 / detached-artifact component=10538/10578 |
| CHR-ENG-WALK | ENG | WALK | DISPATCHED | 38170795132 | Kaggle generator rejected candidate: frame-0-failed; retry-details=detached-artifact component=10723/10743 / detached-artifact component=10599/10643 / detached-artifact component=10547/10555 |
| CHR-ENG-WORK | ENG | WORK | DISPATCHED | 38170795132 | Kaggle generator rejected candidate: frame-1-failed; retry-details=detached-artifact component=10566/10920 / detached-artifact component=10589/10916 / detached-artifact component=10754/10834 |
| CHR-ENG-CARRY | ENG | CARRY | DISPATCHED | 38170795132 | Kaggle generator rejected candidate: carry-too-static mean-change=0.111<0.120; retry-details=edge contact |
| CHR-ENG-REPAIR | ENG | REPAIR | DISPATCHED | 38170795132 | Kaggle generator rejected candidate: frame-4-failed; retry-details=detached-artifact component=10216/10261 / detached-artifact component=10492/10510 / bad border sd=21.7 / detached-artifact component=8753/8858 |
| CHR-ENG-CELEB | ENG | CELEB | DISPATCHED | 38170795132 | Kaggle generator rejected candidate: frame-0-failed; retry-details=detached-artifact component=10331/10334 / detached-artifact component=10528/10565 / detached-artifact component=10593/10602 |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
