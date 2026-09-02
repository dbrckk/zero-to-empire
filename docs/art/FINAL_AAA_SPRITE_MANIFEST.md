# FINAL AAA SPRITE MANIFEST — Zero → Empire

**Purpose:** single source of truth for every final production sprite/sprite-sheet allowed to count toward art completion.

## Counting rule
A row is `DONE` only when the asset is individually authored/generated, cleaned, transparent, free of baked UI/text/logo artifacts, visually consistent with the 2.5D camera/light, optimized for Android, committed under the final runtime path, actually referenced by runtime code, visible in-game, and the Android CI for that commit is green. Source SVGs, concept sheets, collages, Compose/Canvas placeholders, temporary vectors, reference crops and non-integrated rasters are **not DONE**.

Statuses: `TODO` → `ART` → `CLEAN` → `RUNTIME` → `DONE`. `BLOCKED` may be used with a note.

## Locked scope v1
**Total final deliverables: 235** = 98 building masters + 7 Power Core + 24 character sheets + 18 vehicle sprites/sheets + 28 machine sheets + 28 prop sprites + 14 terrain/infrastructure sprites + 18 FX sheets.

If a new runtime sprite is later required, it must be added here first and the denominator updated explicitly.

## Global production contract
- Buildings: 2048×2048 transparent master, runtime WebP/PNG, bottom-center pivot, 8% safety padding.
- Characters: 1024×1024 per final sheet/pose set or 2048 sheet, pivot between feet.
- Vehicles: 1024–2048 transparent, contact-center pivot and separate shadow when useful.
- Machines/props: 512–1024 transparent; moving parts must be isolated when animation requires it.
- Major animation frames: 512×512; characters/props: 256×256; small FX: 128×128; >=4 px frame padding.
- No baked currency, level numbers, UI panels, readable brand text, watermarks, or background rectangles.
- Lighting: upper-left key, cool fill, selective warm/cyan emissive accents.
- Camera: portrait-friendly 2.5D 3/4, consistent 30–38° family.
- Reduced-motion/low-power runtime must be able to freeze decorative loops.

## A. Buildings — 98 / 98 planned

| ID | Asset | Description | Final runtime target | Status |
|---|---|---|---|---|
| BLD-00-T0 | Street Stand T0 | Foundry / Street Stand — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_00_t0_final.webp` | ART |
| BLD-00-T1 | Street Stand T1 | Foundry / Street Stand — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_00_t1_final.webp` | ART |
| BLD-00-T2 | Street Stand T2 | Foundry / Street Stand — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_00_t2_final.webp` | ART |
| BLD-00-T3 | Street Stand T3 | Foundry / Street Stand — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_00_t3_final.webp` | ART |
| BLD-00-T4 | Street Stand T4 | Foundry / Street Stand — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_00_t4_final.webp` | TODO |
| BLD-00-T5 | Street Stand T5 | Foundry / Street Stand — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_00_t5_final.webp` | TODO |
| BLD-00-T6 | Street Stand T6 | Foundry / Street Stand — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_00_t6_final.webp` | TODO |

> Remaining locked-scope entries continue unchanged from the established v1 manifest: BLD-01-T0 through BLD-13-T6, 7 Power Core assets, 24 character sheets, 18 vehicle assets, 28 machine sheets, 28 props, 14 terrain/infrastructure sprites, and 18 FX sheets. Total remains 235.
