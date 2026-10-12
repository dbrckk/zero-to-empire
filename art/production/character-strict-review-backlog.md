# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **223/235**
- Strict DONE: **219/235**
- Semantic review remaining: **16**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review artifact run | Review note |
|---|---|---|---|---:|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | 38223743012 | Fresh kaggle-character-sheet dispatch 38223788230 is active; semantic review remains required after candidate collection. |
| CHR-OP-WORK | OP | WORK | DISPATCHED | 38223743012 | Fresh kaggle-character-sheet dispatch 38223788230 is active; semantic review remains required after candidate collection. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | 38223743012 | Fresh kaggle-character-sheet dispatch 38223788230 is active; semantic review remains required after candidate collection. |
| CHR-OP-REPAIR | OP | REPAIR | DISPATCHED | 38223743012 | Fresh kaggle-character-sheet dispatch 38223788230 is active; semantic review remains required after candidate collection. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | 38223743012 | Fresh kaggle-character-sheet dispatch 38223788230 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | 38220177038 | Fresh kaggle-character-sheet dispatch 38223788230 is active; semantic review remains required after candidate collection. |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | 38220177038 | Fresh kaggle-character-sheet dispatch 38223788230 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | 38220177038 | Fresh kaggle-character-sheet dispatch 38223788230 is active; semantic review remains required after candidate collection. |
| CHR-LOG-REPAIR | LOG | REPAIR | DISPATCHED | 38220177038 | Fresh kaggle-character-sheet dispatch 38223788230 is active; semantic review remains required after candidate collection. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | 38220177038 | Fresh kaggle-character-sheet dispatch 38223788230 is active; semantic review remains required after candidate collection. |
| CHR-ENG-IDLE | ENG | IDLE | AWAITING_REVIEW | 38223743012 | Visually plausible standalone ENG IDLE from collector 38201816567, but HOLD semantic approval until full six-action same-identity family and Android runtime evidence; current in-flight wave 38201875119 may supply a newer same-run reference. |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | 38223743012 | Kaggle generator rejected candidate: walk-too-static lower-motion=0.196 |
| CHR-ENG-WORK | ENG | WORK | AWAITING_REVIEW | 38223743012 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-CARRY | ENG | CARRY | AWAITING_REVIEW | 38223743012 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-REPAIR | ENG | REPAIR | AWAITING_REVIEW | 38223743012 | Fresh Kaggle candidate produced; strict semantic review is required before runtime promotion. |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | 38223743012 | Kaggle generator rejected candidate: celeb-upper-silhouette-jump=0.630>0.450 |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
