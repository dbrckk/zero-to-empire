# BLD-07 Kaggle semantic review — run 35499130912

Date: 2026-09-20  
Verdict: **REJECT**

## What improved
- all seven candidates passed technical QA;
- coherent Mars Empire palette/camera/material family;
- prior baked pseudo-text is largely removed;
- no obvious character/vehicle clutter;
- tier scale and central-spire progression are readable.

## Rejection
The family still violates the building-only isolation contract. Every tier is dominated by a broad square perimeter deck / structural site plinth extending around the architectural mass. T5/T6 make this especially clear. T6 also introduces a small flag/symbol detail that is not needed for the canonical blank-facade architectural read.

This is not a transparency failure: the unwanted deck is fully connected/opaque, so ordinary connected-component and halo QA cannot remove it.

## Quantified signature
A mask-band comparison against accepted BLD-11 shows the failure clearly.

Rejected BLD-07 run 35499130912:
- lower architectural band fill: approximately 0.78–0.84;
- upper architectural band fill: approximately 0.29–0.53;
- visual result: narrow tower/mass sitting on a broad deck.

Accepted BLD-11 run 35473600052:
- lower band fill: approximately 0.80–0.83;
- upper band fill: approximately 0.67–0.86;
- visual result: the broad lower mass continues upward as architecture rather than becoming a site card.

## Generator correction
v17.1 adds a family-specific final branch gate for BLD-07:
- if lower-band fill > 0.76 while upper-band fill < 0.58 on any tier, reject the entire family branch;
- this forces palace/factory wings and connected architectural mass to rise with the command structure instead of using a perimeter deck;
- semantic/manual promotion remains mandatory.

No runtime promotion and no strict DONE increment.
