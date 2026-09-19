# BLD-04 semantic review — Kaggle run 35468753204

Verdict: **REJECT**

Technical isolation is substantially improved: the seven candidates are clean, centered, connected building objects and the prior vehicle/person/site-smear failures are absent.

The family still fails the progression contract. T0 through T6 read primarily as the same rectangular glass headquarters scaled progressively taller/larger. The requested attached utility/lab wings, broadened footprint, automation core, district-scale block, megastructure core and mastery crown do not create sufficiently distinct architectural silhouettes.

No candidate is promoted to runtime and no asset is marked DONE.

## Generator diagnosis

The current prompt contains a direct contradiction for T4-T6: tier text asks for substantial new blocks/wings while the phase instruction says to preserve the approved massing and silhouette and not redesign the footprint. The model follows the conservative instruction and produces a clone ladder.

The TIER dictionary is also Tech-Company-specific at T6 (`apex Tech Company headquarters`) even though the same dictionary is used by every building family. This should be made family-neutral before generating later families.

## Required next generator change

- Keep camera/material/facade-axis DNA stable, not the exact silhouette.
- Require one large fused architectural addition per tier, with explicit left/right/vertical massing changes.
- Make all tier instructions family-neutral.
- Keep the existing no-site/no-vehicle/no-person and alpha-halo gates.
- Preserve manual semantic promotion.
