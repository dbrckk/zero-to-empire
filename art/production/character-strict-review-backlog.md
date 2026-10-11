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
| CHR-ENG-IDLE | ENG | IDLE | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: frame-0-failed |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: frame-0-failed |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: frame-1-failed |
| CHR-ENG-CARRY | ENG | CARRY | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: carry-too-static mean-change=0.111<0.120 |
| CHR-ENG-REPAIR | ENG | REPAIR | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: frame-4-failed |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | 38170795132 | Kaggle generator rejected candidate: frame-0-failed |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
