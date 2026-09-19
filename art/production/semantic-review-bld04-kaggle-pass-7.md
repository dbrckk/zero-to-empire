# BLD-04 Kaggle pass 7 — semantic review

Date: 2026-09-19
Run: 35464303648
Result: **REJECT — progression improved, isolation failed**

## Positive
- All seven candidates passed technical QA.
- Family identity is consistent.
- T0→T6 now shows clearer structural evolution than prior passes.
- Camera/material language remains coherent.

## Rejection reasons
The canonical master contract requires one isolated building object with no surrounding site or secondary objects.

Observed across the family:
- pavement/foundation pads extending well outside the building walls;
- vans/cars and loose equipment in multiple tiers;
- people in T5;
- detached site furniture/props;
- T6 contains a large low-alpha mask/shadow smear on the right;
- later tiers drift toward a campus/site diorama instead of a clean building sprite.

## Pass 8
- redefine BLD-04 as one enclosed headquarters building, never a campus;
- explicitly ban pavement, parking, road, yard, plaza, foundation pad, display plinth, ground plane and cast shadow;
- reinforce no people/vehicles/loose props;
- add automatic low-alpha halo rejection for shadow/site-smear artifacts;
- remain candidate-only; no runtime or DONE promotion.
