# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **223/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | 38367845734 | Fresh kaggle-character-sheet dispatch 38809325110 is active; semantic review remains required after candidate collection. |
| CHR-OP-WORK | OP | WORK | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | 38367845734 | Fresh kaggle-character-sheet dispatch 38809325110 is active; semantic review remains required after candidate collection. |
| CHR-OP-REPAIR | OP | REPAIR | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | 38427591142 | Fresh kaggle-character-sheet dispatch 38809325110 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | 38367845734 | Fresh kaggle-character-sheet dispatch 38809325110 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | 38367845734 | Fresh kaggle-character-sheet dispatch 38809325110 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | 38367845734 | Fresh kaggle-character-sheet dispatch 38809325110 is active; semantic review remains required after candidate collection. |
| CHR-LOG-REPAIR | LOG | REPAIR | DISPATCHED | 38367845734 | Fresh kaggle-character-sheet dispatch 38809325110 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | 38367845734 | Fresh kaggle-character-sheet dispatch 38809325110 is active; semantic review remains required after candidate collection. |
| CHR-ENG-IDLE | ENG | IDLE | AWAITING_REVIEW | 38427591142 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | 38427591142 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.087 |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | 38427591142 | Kaggle generator rejected candidate: work-too-static mean-change=0.083<0.100; retry-details=edge contact |
| CHR-ENG-CARRY | ENG | CARRY | AWAITING_REVIEW | 38309355566 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-REPAIR | ENG | REPAIR | REJECTED_SEMANTIC | 38427591142 | Kaggle generator rejected candidate: image-risk:FACE_HEADGEAR_STRUCTURE_DRIFT_RISK |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | 38427591142 | Kaggle generator rejected candidate: celeb-too-static mean-change=0.096<0.100 |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
