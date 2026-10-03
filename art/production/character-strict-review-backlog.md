# Character strict-review backlog

Generated from `art/production/master-asset-queue.json` after production completion.

- Production processed: **222/235**
- Strict DONE: **214/235**
- Semantic review remaining: **21**
- This report does **not** grant strict approval or runtime promotion.

| Asset | Role | Action | Technical status | Review note |
|---|---|---|---|---|
| CHR-OP-IDLE | OP | IDLE | DISPATCHED | Identity/headgear consistency passed; IDLE candidate still requires strict semantic review before runtime promotion. |
| CHR-OP-WALK | OP | WALK | DISPATCHED | Identity/headgear consistency passed, but WALK lacks clear alternating stride. v1.5 requires explicit leg poses and automatic lower-body motion. |
| CHR-OP-WORK | OP | WORK | DISPATCHED | Fresh generated candidate is available; strict semantic review is still required before runtime promotion. |
| CHR-OP-CARRY | OP | CARRY | DISPATCHED | Fresh generated candidate is available; strict semantic review is still required before runtime promotion. |
| CHR-OP-REPAIR | OP | REPAIR | DISPATCHED | Semantic review required; no specific automated defect recorded. |
| CHR-OP-CELEB | OP | CELEB | DISPATCHED | Semantic review required; no specific automated defect recorded. |
| CHR-TECH-IDLE | TECH | IDLE | CANDIDATE | Fresh identity-locked candidate produced; semantic review is still required. |
| CHR-TECH-WALK | TECH | WALK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; poses read as standing/turntable frames rather than a coherent alternating walk cycle, with visible head/identity drift. |
| CHR-TECH-WORK | TECH | WORK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; technically valid atlas is too static and the work/tool action is not readable at gameplay size. |
| CHR-TECH-CARRY | TECH | CARRY | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; no crate/component is consistently visible between both hands and the sequence reads as static standing rather than carrying. |
| CHR-LOG-WALK | LOG | WALK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; large identity/clothing drift across frames and no coherent alternating walk cycle. |
| CHR-LOG-WORK | LOG | WORK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; action is too static and lacks a clearly readable work/tool interaction. |
| CHR-LOG-CARRY | LOG | CARRY | CANDIDATE | Fresh generated candidate is available; strict semantic review is still required before runtime promotion. |
| CHR-LOG-REPAIR | LOG | REPAIR | CANDIDATE | Fresh generated candidate is available; strict semantic review is still required before runtime promotion. |
| CHR-LOG-CELEB | LOG | CELEB | CANDIDATE | Fresh generated candidate is available; strict semantic review is still required before runtime promotion. |
| CHR-ENG-IDLE | ENG | IDLE | CANDIDATE | Fresh generated candidate is available; strict semantic review is still required before runtime promotion. |
| CHR-ENG-WALK | ENG | WALK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; sequence behaves like a front/back turntable with identity/clothing drift rather than a stable three-quarter walk cycle. |
| CHR-ENG-WORK | ENG | WORK | REJECTED_SEMANTIC | Semantic review 2026-10-03: rejected; action remains mostly static with weak or absent readable work motion. |
| CHR-ENG-CARRY | ENG | CARRY | CANDIDATE | Fresh generated candidate is available; strict semantic review is still required before runtime promotion. |
| CHR-ENG-REPAIR | ENG | REPAIR | CANDIDATE | Fresh generated candidate is available; strict semantic review is still required before runtime promotion. |
| CHR-ENG-CELEB | ENG | CELEB | CANDIDATE | Fresh generated candidate is available; strict semantic review is still required before runtime promotion. |

## Review rule

A reviewer must inspect identity continuity, full-body framing, role/clothing consistency, action readability, animation motion, and runtime suitability. Only explicit reviewed approvals may change `strict_status` to `DONE`.
