# Run 77 — strict semantic review

Date: 2026-09-07
Workflow: `Kaggle Mass Sprite Factory` run `34102566634`
Artifact: `kaggle-sprite-batch` / id `10012165066`
Generated candidates: 21
Automatic technical QA: 21/21 PASS
Strict semantic promotion: **0/21 ACCEPTED**

## Decision
Reject the complete run. Do not promote any run-77 candidate and do not increment strict DONE.

Technical alpha/dimension/edge checks were green, but full-resolution visual review exposed semantic, isolation, composition and tier-progression failures that the automatic QA did not detect.

## BLD-04 — reject T0 through T6
Target family: precision fabrication works / graphite factory / three CNC bays / logistics dock.

Observed failures:
- T0 already reads as a large finished warehouse rather than a compact starter facility.
- Full-resolution T0 contains people, multiple vehicles/trucks, loose props, readable/pseudo-readable markings and a large ground slab.
- Family progression from T0 through T4 is mostly small variation of the same low rectangular warehouse.
- T5 changes composition rather than clearly evolving the same structure.
- T6 jumps to a substantially different vertical building instead of reading as a controlled final evolution of the same architectural DNA.
- The required monotonic starter → reinforced → industrial → automated → advanced → megastructure → ultimate hierarchy is not reliable.

Result: `BLD-04-T0` … `BLD-04-T6` REJECTED.

## BLD-06 — reject T0 through T6
Target family: coolant process plant / silver-graphite pump house / twin reservoirs / cyan pipes.

Observed failures:
- Large opaque/semantically baked ground platform and background remnants remain attached to the silhouette.
- Full-resolution T0 shows visible isolation damage/holes in a foreground tank and irregular white background residue.
- T0 through T5 remain near-static low process-plant variants with weak footprint/verticality growth.
- T6 changes into a markedly different tower-heavy composition rather than preserving a convincing additive family evolution.
- Progression metrics are non-monotonic; the final family does not communicate seven clearly increasing production tiers.

Result: `BLD-06-T0` … `BLD-06-T6` REJECTED.

## BLD-07 — reject T0 through T6
Target family: automation power works / wide high-tech factory / twin gantries / power manifold.

Observed failures:
- T0 is already a dense multi-storey industrial complex with a major crane/gantry and tower elements; this directly violates the required starter tier: compact, low verticality, bare shell, no tower.
- T0 also contains broad baked ground/shadow residue and detached/vehicle-like lower components.
- T1 through T6 mostly reshuffle cranes/towers on an already late-game silhouette rather than building a controlled upgrade hierarchy.
- Tier scale and complexity are not sufficiently monotonic, and the family begins too advanced for later tiers to have meaningful headroom.

Result: `BLD-07-T0` … `BLD-07-T6` REJECTED.

## Generator implications
Run-77 proves that the current automatic QA is still insufficient for building families. The next generator iteration must harden at least these gates:

1. Detect/reject people and vehicles in building masters.
2. Detect/reject large rectangular/irregular ground slabs and background remnants even when alpha edge tests pass.
3. Detect internal alpha holes/isolation damage inside major structural components.
4. Enforce a strict T0 complexity ceiling: single-storey/compact/low verticality/no large crane/no tower.
5. Enforce monotonic tier growth using silhouette/bbox/height/structural-complexity metrics instead of technical transparency alone.
6. Enforce family identity continuity so T6 cannot become a new unrelated building.
7. Prefer sequential/additive evolution with controlled anchors, but reject a sequence when early tiers are already too complex or later tiers collapse/recompose.

## Next action
Modify the building-family generator/QA before spending another full wave on the same failure mode. Then regenerate the next coherent family batch and repeat technical QA → full-resolution semantic QA → selective promotion → runtime integration → Android CI.
