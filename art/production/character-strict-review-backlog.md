# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **219/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | — | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-WORK | OP | WORK | DISPATCHED | — | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | — | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-REPAIR | OP | REPAIR | DISPATCHED | — | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | — | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | — | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | — | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | — | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-REPAIR | LOG | REPAIR | DISPATCHED | — | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | — | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-IDLE | ENG | IDLE | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: frame-0-failed; retry-details=detached-artifact component=10558/10611 / detached-artifact component=10510/10546 / detached-artifact component=10538/10578 |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: frame-0-failed; retry-details=detached-artifact component=10723/10743 / detached-artifact component=10599/10643 / detached-artifact component=10547/10555 |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: frame-1-failed; retry-details=detached-artifact component=10566/10920 / detached-artifact component=10589/10916 / detached-artifact component=10754/10834 |
| CHR-ENG-CARRY | ENG | CARRY | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: carry-too-static mean-change=0.111<0.120; retry-details=edge contact |
| CHR-ENG-REPAIR | ENG | REPAIR | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: frame-4-failed; retry-details=detached-artifact component=10216/10261 / detached-artifact component=10492/10510 / bad border sd=21.7 / detached-artifact component=8753/8858 |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: frame-0-failed; retry-details=detached-artifact component=10331/10334 / detached-artifact component=10528/10565 / detached-artifact component=10593/10602 |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
