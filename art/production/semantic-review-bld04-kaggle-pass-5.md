# BLD-04 Kaggle pass 5 — technical generation diagnosis

Date: 2026-09-19
Run: 35451313535
Result: **NO CANDIDATES EXPORTED — guardrail worked**

The run generated valid T0 anchors but every T1 contextual attempt was rejected by the new normalized-silhouette gate.

Observed T1 normalized silhouette IoU:
- 0.988
- 0.976
- 0.982
- 0.980
- 0.989
- 0.990
- 0.989
- 0.989

Threshold: 0.965.

This confirms the model was still producing the same silhouette at effective img2img strength around 0.19. The guardrail therefore prevented another scaled-clone family from reaching semantic review.

## Pass 6 change
Increase structural img2img strength substantially while retaining:
- family/footprint continuity gates;
- anti-slab checks;
- normalized-silhouette anti-resize gate;
- candidate-only output;
- no runtime or DONE promotion.
