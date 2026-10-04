# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **216/235**
- Strict DONE: **216/235**
- Semantic review remaining: **19**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review note |
|---|---|---|---|---|
| CHR-OP-WALK | OP | WALK | DISPATCHED | Kaggle generator rejected candidate: frame-0-failed |
| CHR-OP-WORK | OP | WORK | DISPATCHED | Kaggle generator rejected candidate: frame-0-failed |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | Kaggle generator rejected candidate: frame-0-failed |
| CHR-OP-REPAIR | OP | REPAIR | REJECTED_SEMANTIC | Semantic review 2026-10-04 of v1.12 Kaggle run 37225678575: rejected; face/headgear/body identity drifts across frames, repair objects change from panel to multiple unrelated machines, and no single stable repair point/tool contact is maintained. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | Kaggle generator rejected candidate: frame-0-failed |
| CHR-TECH-WALK | TECH | WALK | DISPATCHED | Kaggle generator rejected candidate: duplicate-adjacent-frame |
| CHR-TECH-WORK | TECH | WORK | DISPATCHED | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; identity/headgear and accessories drift between frames and the sequence lacks one consistent visible tool contacting a stable work point. |
| CHR-TECH-CARRY | TECH | CARRY | DISPATCHED | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; identity and headgear drift, the crate appears only in some frames or changes form, and there is no coherent two-hand carrying stride. |
| CHR-LOG-WALK | LOG | WALK | DISPATCHED | Kaggle generator rejected candidate: walk-too-static lower-motion=0.164 |
| CHR-LOG-WORK | LOG | WORK | DISPATCHED | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; face/headgear/body details vary significantly and the frames remain mostly neutral standing without one readable repeated work interaction. |
| CHR-LOG-CARRY | LOG | CARRY | DISPATCHED | Semantic review 2026-10-04 of Kaggle v1.10 run 37159562177: rejected; severe identity/headgear drift, front/back turntable changes, and the crate is inconsistent or absent instead of being held with both hands through a carrying stride. |
| CHR-LOG-REPAIR | LOG | REPAIR | REJECTED_SEMANTIC | Semantic review 2026-10-04 of v1.12 Kaggle run 37225678575: rejected; cells behave like front/back turntable pairs with large face/headgear/clothing changes, multiple people per cell appearance, and no coherent repair motion on one stable target. |
| CHR-LOG-CELEB | LOG | CELEB | DISPATCHED | Kaggle generator rejected candidate: celeb-too-static mean-change=0.090<0.100 |
| CHR-ENG-IDLE | ENG | IDLE | REJECTED_SEMANTIC | Kaggle generator rejected candidate: frame-0-failed |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | Kaggle generator rejected candidate: frame-0-failed |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | Kaggle generator rejected candidate: frame-0-failed |
| CHR-ENG-CARRY | ENG | CARRY | REJECTED_SEMANTIC | Kaggle generator rejected candidate: frame-0-failed |
| CHR-ENG-REPAIR | ENG | REPAIR | REJECTED_SEMANTIC | Kaggle generator rejected candidate: frame-0-failed |
| CHR-ENG-CELEB | ENG | CELEB | REJECTED_SEMANTIC | Kaggle generator rejected candidate: frame-0-failed |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
