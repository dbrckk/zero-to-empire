# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **223/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | 38201816567 | Fresh kaggle-character-sheet dispatch 38220212953 is active; semantic review remains required after candidate collection. |
| CHR-OP-WORK | OP | WORK | DISPATCHED | 38185962170 | Fresh kaggle-character-sheet dispatch 38220212953 is active; semantic review remains required after candidate collection. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | 38201816567 | Fresh kaggle-character-sheet dispatch 38220212953 is active; semantic review remains required after candidate collection. |
| CHR-OP-REPAIR | OP | REPAIR | DISPATCHED | 38201816567 | Fresh kaggle-character-sheet dispatch 38220212953 is active; semantic review remains required after candidate collection. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | 38185962170 | Fresh kaggle-character-sheet dispatch 38220212953 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WALK | LOG | WALK | REJECTED_SEMANTIC | 38220177038 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.109 |
| CHR-LOG-WORK | LOG | WORK | AWAITING_REVIEW | 38220177038 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-CARRY | LOG | CARRY | REJECTED_SEMANTIC | 38220177038 | Kaggle generator rejected candidate: carry-too-static mean-change=0.065<0.120 |
| CHR-LOG-REPAIR | LOG | REPAIR | AWAITING_REVIEW | 38220177038 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-LOG-CELEB | LOG | CELEB | AWAITING_REVIEW | 38220177038 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-IDLE | ENG | IDLE | AWAITING_REVIEW | 38201816567 | Visually plausible standalone ENG IDLE from collector 38201816567, but HOLD semantic approval until full six-action same-identity family and Android runtime evidence; current in-flight wave 38201875119 may supply a newer same-run reference. |
| CHR-ENG-WALK | ENG | WALK | DISPATCHED | 38220177038 | Fresh kaggle-character-sheet dispatch 38220212953 is active; semantic review remains required after candidate collection. |
| CHR-ENG-WORK | ENG | WORK | DISPATCHED | 38201816567 | Fresh kaggle-character-sheet dispatch 38220212953 is active; semantic review remains required after candidate collection. |
| CHR-ENG-CARRY | ENG | CARRY | DISPATCHED | 38220177038 | Fresh kaggle-character-sheet dispatch 38220212953 is active; semantic review remains required after candidate collection. |
| CHR-ENG-REPAIR | ENG | REPAIR | DISPATCHED | 38201816567 | Fresh kaggle-character-sheet dispatch 38220212953 is active; semantic review remains required after candidate collection. |
| CHR-ENG-CELEB | ENG | CELEB | DISPATCHED | 38220177038 | Fresh kaggle-character-sheet dispatch 38220212953 is active; semantic review remains required after candidate collection. |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
