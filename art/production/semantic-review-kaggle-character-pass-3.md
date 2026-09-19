# Semantic review — Kaggle character pass 3

Date: 2026-09-19
Source run: 35448527236
Status: **REJECTED — retry required**

## CHR-OP-IDLE
Verdict: **REJECT**

Positive:
- identity continuity is substantially better than the Pollinations passes;
- one worker is preserved across the six frames;
- pivot and silhouette are technically stable.

Reject reasons:
- rendering is too photorealistic for the canonical stylized 2.5D game-art direction;
- pose variation is too weak to read as a deliberate premium idle loop at gameplay size.

Action:
- retry with explicit non-photorealistic / painterly 3D game-render language;
- keep identity-anchored img2img.

## CHR-OP-WALK
Verdict: **REJECT**

Reject reasons:
- every frame contains two workers;
- technical alpha/IoU QA incorrectly accepted the merged two-person silhouette.

Action:
- add a pre-resize silhouette width/height gate to reject multi-subject frames;
- retry only after that gate is active;
- keep candidate-only until another semantic review.

## Promotion effect
No character asset from this run is promoted to runtime or strict DONE.
Character strict progress remains **0 / 24**.
