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
| BLD-00-T0 | Street Stand T0 | Foundry / Street Stand — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_00_t0_final.webp` | DONE |
| BLD-00-T1 | Street Stand T1 | Foundry / Street Stand — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_00_t1_final.webp` | DONE |
| BLD-00-T2 | Street Stand T2 | Foundry / Street Stand — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_00_t2_final.webp` | DONE |
| BLD-00-T3 | Street Stand T3 | Foundry / Street Stand — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_00_t3_final.webp` | DONE |
| BLD-00-T4 | Street Stand T4 | Foundry / Street Stand — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_00_t4_final.webp` | DONE |
| BLD-00-T5 | Street Stand T5 | Foundry / Street Stand — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_00_t5_final.webp` | DONE |
| BLD-00-T6 | Street Stand T6 | Foundry / Street Stand — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_00_t6_final.webp` | DONE |
| BLD-01-T0 | Corner Shop T0 | Foundry / Corner Shop — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_01_t0_final.webp` | DONE |
| BLD-01-T1 | Corner Shop T1 | Foundry / Corner Shop — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_01_t1_final.webp` | DONE |
| BLD-01-T2 | Corner Shop T2 | Foundry / Corner Shop — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_01_t2_final.webp` | DONE |
| BLD-01-T3 | Corner Shop T3 | Foundry / Corner Shop — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_01_t3_final.webp` | DONE |
| BLD-01-T4 | Corner Shop T4 | Foundry / Corner Shop — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_01_t4_final.webp` | DONE |
| BLD-01-T5 | Corner Shop T5 | Foundry / Corner Shop — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_01_t5_final.webp` | DONE |
| BLD-01-T6 | Corner Shop T6 | Foundry / Corner Shop — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_01_t6_final.webp` | DONE |
| BLD-02-T0 | Furnace Stall T0 | Foundry / Furnace Stall — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_02_t0_final.webp` | DONE |
| BLD-02-T1 | Furnace Stall T1 | Foundry / Furnace Stall — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_02_t1_final.webp` | DONE |
| BLD-02-T2 | Furnace Stall T2 | Foundry / Furnace Stall — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_02_t2_final.webp` | DONE |
| BLD-02-T3 | Furnace Stall T3 | Foundry / Furnace Stall — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_02_t3_final.webp` | DONE |
| BLD-02-T4 | Furnace Stall T4 | Foundry / Furnace Stall — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_02_t4_final.webp` | RUNTIME |
| BLD-02-T5 | Furnace Stall T5 | Foundry / Furnace Stall — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_02_t5_final.webp` | RUNTIME |
| BLD-02-T6 | Furnace Stall T6 | Foundry / Furnace Stall — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_02_t6_final.webp` | RUNTIME |
| BLD-03-T0 | Assembly Hub T0 | Foundry / Assembly Hub — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_03_t0_final.webp` | RUNTIME |
| BLD-03-T1 | Assembly Hub T1 | Foundry / Assembly Hub — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_03_t1_final.webp` | RUNTIME |
| BLD-03-T2 | Assembly Hub T2 | Foundry / Assembly Hub — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_03_t2_final.webp` | TODO |
| BLD-03-T3 | Assembly Hub T3 | Foundry / Assembly Hub — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_03_t3_final.webp` | TODO |
| BLD-03-T4 | Assembly Hub T4 | Foundry / Assembly Hub — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_03_t4_final.webp` | TODO |
| BLD-03-T5 | Assembly Hub T5 | Foundry / Assembly Hub — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_03_t5_final.webp` | TODO |
| BLD-03-T6 | Assembly Hub T6 | Foundry / Assembly Hub — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_03_t6_final.webp` | TODO |
| BLD-04-T0 | Expansion Business 04 T0 | Expansion / Expansion Business 04 — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_04_t0_final.webp` | TODO |
| BLD-04-T1 | Expansion Business 04 T1 | Expansion / Expansion Business 04 — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_04_t1_final.webp` | TODO |
| BLD-04-T2 | Expansion Business 04 T2 | Expansion / Expansion Business 04 — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_04_t2_final.webp` | TODO |
| BLD-04-T3 | Expansion Business 04 T3 | Expansion / Expansion Business 04 — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_04_t3_final.webp` | TODO |
| BLD-04-T4 | Expansion Business 04 T4 | Expansion / Expansion Business 04 — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_04_t4_final.webp` | TODO |
| BLD-04-T5 | Expansion Business 04 T5 | Expansion / Expansion Business 04 — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_04_t5_final.webp` | TODO |
| BLD-04-T6 | Expansion Business 04 T6 | Expansion / Expansion Business 04 — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_04_t6_final.webp` | TODO |
| BLD-05-T0 | Expansion Business 05 T0 | Expansion / Expansion Business 05 — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_05_t0_final.webp` | TODO |
| BLD-05-T1 | Expansion Business 05 T1 | Expansion / Expansion Business 05 — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_05_t1_final.webp` | TODO |
| BLD-05-T2 | Expansion Business 05 T2 | Expansion / Expansion Business 05 — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_05_t2_final.webp` | TODO |
| BLD-05-T3 | Expansion Business 05 T3 | Expansion / Expansion Business 05 — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_05_t3_final.webp` | TODO |
| BLD-05-T4 | Expansion Business 05 T4 | Expansion / Expansion Business 05 — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_05_t4_final.webp` | TODO |
| BLD-05-T5 | Expansion Business 05 T5 | Expansion / Expansion Business 05 — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_05_t5_final.webp` | TODO |
| BLD-05-T6 | Expansion Business 05 T6 | Expansion / Expansion Business 05 — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_05_t6_final.webp` | TODO |
| BLD-06-T0 | Expansion Business 06 T0 | Expansion / Expansion Business 06 — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_06_t0_final.webp` | TODO |
| BLD-06-T1 | Expansion Business 06 T1 | Expansion / Expansion Business 06 — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_06_t1_final.webp` | TODO |
| BLD-06-T2 | Expansion Business 06 T2 | Expansion / Expansion Business 06 — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_06_t2_final.webp` | TODO |
| BLD-06-T3 | Expansion Business 06 T3 | Expansion / Expansion Business 06 — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_06_t3_final.webp` | TODO |
| BLD-06-T4 | Expansion Business 06 T4 | Expansion / Expansion Business 06 — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_06_t4_final.webp` | TODO |
| BLD-06-T5 | Expansion Business 06 T5 | Expansion / Expansion Business 06 — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_06_t5_final.webp` | TODO |
| BLD-06-T6 | Expansion Business 06 T6 | Expansion / Expansion Business 06 — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_06_t6_final.webp` | TODO |
| BLD-07-T0 | Expansion Business 07 T0 | Expansion / Expansion Business 07 — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_07_t0_final.webp` | TODO |
| BLD-07-T1 | Expansion Business 07 T1 | Expansion / Expansion Business 07 — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_07_t1_final.webp` | TODO |
| BLD-07-T2 | Expansion Business 07 T2 | Expansion / Expansion Business 07 — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_07_t2_final.webp` | TODO |
| BLD-07-T3 | Expansion Business 07 T3 | Expansion / Expansion Business 07 — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_07_t3_final.webp` | TODO |
| BLD-07-T4 | Expansion Business 07 T4 | Expansion / Expansion Business 07 — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_07_t4_final.webp` | TODO |
| BLD-07-T5 | Expansion Business 07 T5 | Expansion / Expansion Business 07 — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_07_t5_final.webp` | TODO |
| BLD-07-T6 | Expansion Business 07 T6 | Expansion / Expansion Business 07 — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_07_t6_final.webp` | TODO |
| BLD-08-T0 | Megastructure Business 08 T0 | Megastructure / Megastructure Business 08 — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_08_t0_final.webp` | TODO |
| BLD-08-T1 | Megastructure Business 08 T1 | Megastructure / Megastructure Business 08 — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_08_t1_final.webp` | TODO |
| BLD-08-T2 | Megastructure Business 08 T2 | Megastructure / Megastructure Business 08 — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_08_t2_final.webp` | TODO |
| BLD-08-T3 | Megastructure Business 08 T3 | Megastructure / Megastructure Business 08 — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_08_t3_final.webp` | TODO |
| BLD-08-T4 | Megastructure Business 08 T4 | Megastructure / Megastructure Business 08 — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_08_t4_final.webp` | TODO |
| BLD-08-T5 | Megastructure Business 08 T5 | Megastructure / Megastructure Business 08 — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_08_t5_final.webp` | TODO |
| BLD-08-T6 | Megastructure Business 08 T6 | Megastructure / Megastructure Business 08 — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_08_t6_final.webp` | TODO |
| BLD-09-T0 | Megastructure Business 09 T0 | Megastructure / Megastructure Business 09 — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_09_t0_final.webp` | TODO |
| BLD-09-T1 | Megastructure Business 09 T1 | Megastructure / Megastructure Business 09 — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_09_t1_final.webp` | TODO |
| BLD-09-T2 | Megastructure Business 09 T2 | Megastructure / Megastructure Business 09 — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_09_t2_final.webp` | TODO |
| BLD-09-T3 | Megastructure Business 09 T3 | Megastructure / Megastructure Business 09 — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_09_t3_final.webp` | TODO |
| BLD-09-T4 | Megastructure Business 09 T4 | Megastructure / Megastructure Business 09 — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_09_t4_final.webp` | TODO |
| BLD-09-T5 | Megastructure Business 09 T5 | Megastructure / Megastructure Business 09 — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_09_t5_final.webp` | TODO |
| BLD-09-T6 | Megastructure Business 09 T6 | Megastructure / Megastructure Business 09 — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_09_t6_final.webp` | TODO |
| BLD-10-T0 | Megastructure Business 10 T0 | Megastructure / Megastructure Business 10 — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_10_t0_final.webp` | TODO |
| BLD-10-T1 | Megastructure Business 10 T1 | Megastructure / Megastructure Business 10 — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_10_t1_final.webp` | TODO |
| BLD-10-T2 | Megastructure Business 10 T2 | Megastructure / Megastructure Business 10 — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_10_t2_final.webp` | TODO |
| BLD-10-T3 | Megastructure Business 10 T3 | Megastructure / Megastructure Business 10 — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_10_t3_final.webp` | TODO |
| BLD-10-T4 | Megastructure Business 10 T4 | Megastructure / Megastructure Business 10 — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_10_t4_final.webp` | TODO |
| BLD-10-T5 | Megastructure Business 10 T5 | Megastructure / Megastructure Business 10 — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_10_t5_final.webp` | TODO |
| BLD-10-T6 | Megastructure Business 10 T6 | Megastructure / Megastructure Business 10 — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_10_t6_final.webp` | TODO |
| BLD-11-T0 | Megastructure Business 11 T0 | Megastructure / Megastructure Business 11 — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_11_t0_final.webp` | TODO |
| BLD-11-T1 | Megastructure Business 11 T1 | Megastructure / Megastructure Business 11 — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_11_t1_final.webp` | TODO |
| BLD-11-T2 | Megastructure Business 11 T2 | Megastructure / Megastructure Business 11 — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_11_t2_final.webp` | TODO |
| BLD-11-T3 | Megastructure Business 11 T3 | Megastructure / Megastructure Business 11 — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_11_t3_final.webp` | TODO |
| BLD-11-T4 | Megastructure Business 11 T4 | Megastructure / Megastructure Business 11 — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_11_t4_final.webp` | TODO |
| BLD-11-T5 | Megastructure Business 11 T5 | Megastructure / Megastructure Business 11 — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_11_t5_final.webp` | TODO |
| BLD-11-T6 | Megastructure Business 11 T6 | Megastructure / Megastructure Business 11 — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_11_t6_final.webp` | TODO |
| BLD-12-T0 | Apex Business 12 T0 | Apex / Apex Business 12 — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_12_t0_final.webp` | TODO |
| BLD-12-T1 | Apex Business 12 T1 | Apex / Apex Business 12 — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_12_t1_final.webp` | TODO |
| BLD-12-T2 | Apex Business 12 T2 | Apex / Apex Business 12 — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_12_t2_final.webp` | TODO |
| BLD-12-T3 | Apex Business 12 T3 | Apex / Apex Business 12 — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_12_t3_final.webp` | TODO |
| BLD-12-T4 | Apex Business 12 T4 | Apex / Apex Business 12 — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_12_t4_final.webp` | TODO |
| BLD-12-T5 | Apex Business 12 T5 | Apex / Apex Business 12 — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_12_t5_final.webp` | TODO |
| BLD-12-T6 | Apex Business 12 T6 | Apex / Apex Business 12 — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_12_t6_final.webp` | TODO |
| BLD-13-T0 | Apex Business 13 T0 | Apex / Apex Business 13 — starter footprint, improvised materials, low verticality, one clear production cue. | `app/src/main/res/drawable-nodpi/zte_business_13_t0_final.webp` | TODO |
| BLD-13-T1 | Apex Business 13 T1 | Apex / Apex Business 13 — reinforced footprint, dedicated machinery, cleaner structure, stronger silhouette. | `app/src/main/res/drawable-nodpi/zte_business_13_t1_final.webp` | TODO |
| BLD-13-T2 | Apex Business 13 T2 | Apex / Apex Business 13 — commercialized/industrial expansion, second active subsystem, larger footprint. | `app/src/main/res/drawable-nodpi/zte_business_13_t2_final.webp` | TODO |
| BLD-13-T3 | Apex Business 13 T3 | Apex / Apex Business 13 — automated complex, visible logistics flow, more verticality and emissive accents. | `app/src/main/res/drawable-nodpi/zte_business_13_t3_final.webp` | TODO |
| BLD-13-T4 | Apex Business 13 T4 | Apex / Apex Business 13 — advanced district-scale facility, dense machinery, premium materials and strong landmark read. | `app/src/main/res/drawable-nodpi/zte_business_13_t4_final.webp` | TODO |
| BLD-13-T5 | Apex Business 13 T5 | Apex / Apex Business 13 — late-game megastructure, multi-stage production, large moving assemblies and energy routing. | `app/src/main/res/drawable-nodpi/zte_business_13_t5_final.webp` | TODO |
| BLD-13-T6 | Apex Business 13 T6 | Apex / Apex Business 13 — ultimate mastered structure, iconic silhouette, maximal verticality, prestige crown/hero treatment. | `app/src/main/res/drawable-nodpi/zte_business_13_t6_final.webp` | TODO |

## B. Power Core — 7 / 7 planned

| ID | Asset | Description | Final runtime target | Status |
|---|---|---|---|---|
| CORE-T0 | Power Core T0 | salvaged mechanical core on improvised cradle; weak pulse and exposed conduits. | `app/src/main/res/drawable-nodpi/zte_power_core_t0_final.webp` | TODO |
| CORE-T1 | Power Core T1 | reinforced industrial reactor; clear rotating/piston subsystem and stronger warm core. | `app/src/main/res/drawable-nodpi/zte_power_core_t1_final.webp` | TODO |
| CORE-T2 | Power Core T2 | automated district reactor; dual-energy routing and articulated service arms. | `app/src/main/res/drawable-nodpi/zte_power_core_t2_final.webp` | TODO |
| CORE-T3 | Power Core T3 | neon metropolitan core; holographic containment ring and cleaner premium shell. | `app/src/main/res/drawable-nodpi/zte_power_core_t3_final.webp` | TODO |
| CORE-T4 | Power Core T4 | orbital-grade power nexus; levitating ring stack, stronger cyan routing and larger footprint. | `app/src/main/res/drawable-nodpi/zte_power_core_t4_final.webp` | TODO |
| CORE-T5 | Power Core T5 | stellar collector core; multi-ring containment, stellar plasma motif and hero-scale silhouette. | `app/src/main/res/drawable-nodpi/zte_power_core_t5_final.webp` | TODO |
| CORE-T6 | Power Core T6 | Singularity Crown; ultimate reality-bending core with iconic crown geometry and prestige treatment. | `app/src/main/res/drawable-nodpi/zte_power_core_t6_final.webp` | TODO |

## C. Characters — 24 / 24 planned

| ID | Sheet | Description | Runtime target | Status |
|---|---|---|---|---|
| CHR-OP-IDLE | Foundry operator idle | idle breathing/look-around loop, 4–8 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_op_idle_final.webp` | TODO |
| CHR-OP-WALK | Foundry operator walk | walk cycle, 6–10 frames, consistent foot pivot; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_op_walk_final.webp` | TODO |
| CHR-OP-WORK | Foundry operator work | primary work/tool loop, 8–16 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_op_work_final.webp` | TODO |
| CHR-OP-CARRY | Foundry operator carry | carry crate/component movement cycle, 6–10 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_op_carry_final.webp` | TODO |
| CHR-OP-REPAIR | Foundry operator repair | repair/welding/diagnostic loop, 8–16 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_op_repair_final.webp` | TODO |
| CHR-OP-CELEB | Foundry operator celeb | short celebration/milestone one-shot, 8–12 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_op_celeb_final.webp` | TODO |
| CHR-TECH-IDLE | Technician idle | idle breathing/look-around loop, 4–8 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_tech_idle_final.webp` | TODO |
| CHR-TECH-WALK | Technician walk | walk cycle, 6–10 frames, consistent foot pivot; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_tech_walk_final.webp` | TODO |
| CHR-TECH-WORK | Technician work | primary work/tool loop, 8–16 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_tech_work_final.webp` | TODO |
| CHR-TECH-CARRY | Technician carry | carry crate/component movement cycle, 6–10 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_tech_carry_final.webp` | TODO |
| CHR-TECH-REPAIR | Technician repair | repair/welding/diagnostic loop, 8–16 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_tech_repair_final.webp` | TODO |
| CHR-TECH-CELEB | Technician celeb | short celebration/milestone one-shot, 8–12 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_tech_celeb_final.webp` | TODO |
| CHR-LOG-IDLE | Logistics worker idle | idle breathing/look-around loop, 4–8 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_log_idle_final.webp` | TODO |
| CHR-LOG-WALK | Logistics worker walk | walk cycle, 6–10 frames, consistent foot pivot; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_log_walk_final.webp` | TODO |
| CHR-LOG-WORK | Logistics worker work | primary work/tool loop, 8–16 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_log_work_final.webp` | TODO |
| CHR-LOG-CARRY | Logistics worker carry | carry crate/component movement cycle, 6–10 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_log_carry_final.webp` | TODO |
| CHR-LOG-REPAIR | Logistics worker repair | repair/welding/diagnostic loop, 8–16 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_log_repair_final.webp` | TODO |
| CHR-LOG-CELEB | Logistics worker celeb | short celebration/milestone one-shot, 8–12 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_log_celeb_final.webp` | TODO |
| CHR-ENG-IDLE | Engineer idle | idle breathing/look-around loop, 4–8 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_eng_idle_final.webp` | TODO |
| CHR-ENG-WALK | Engineer walk | walk cycle, 6–10 frames, consistent foot pivot; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_eng_walk_final.webp` | TODO |
| CHR-ENG-WORK | Engineer work | primary work/tool loop, 8–16 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_eng_work_final.webp` | TODO |
| CHR-ENG-CARRY | Engineer carry | carry crate/component movement cycle, 6–10 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_eng_carry_final.webp` | TODO |
| CHR-ENG-REPAIR | Engineer repair | repair/welding/diagnostic loop, 8–16 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_eng_repair_final.webp` | TODO |
| CHR-ENG-CELEB | Engineer celeb | short celebration/milestone one-shot, 8–12 frames; clothing evolves by era through palette/accessory variants without changing pivot. | `app/src/main/res/drawable-nodpi/zte_chr_eng_celeb_final.webp` | TODO |

## D. Vehicles — 18 / 18 planned

| ID | Asset | Description | Runtime target | Status |
|---|---|---|---|---|
| VEH-00 | Foundry hand cart / pallet mover | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_00_final.webp` | TODO |
| VEH-01 | Foundry forklift | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_01_final.webp` | TODO |
| VEH-02 | Foundry compact delivery van | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_02_final.webp` | TODO |
| VEH-03 | Foundry box truck | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_03_final.webp` | TODO |
| VEH-04 | Expansion electric utility van | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_04_final.webp` | TODO |
| VEH-05 | Expansion cargo truck | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_05_final.webp` | TODO |
| VEH-06 | Expansion courier bike | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_06_final.webp` | TODO |
| VEH-07 | Expansion autonomous loader | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_07_final.webp` | TODO |
| VEH-08 | Megastructure heavy hauler | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_08_final.webp` | TODO |
| VEH-09 | Megastructure maglev cargo pod | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_09_final.webp` | TODO |
| VEH-10 | Megastructure service drone | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_10_final.webp` | TODO |
| VEH-11 | Megastructure autonomous carrier | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_11_final.webp` | TODO |
| VEH-12 | Apex phase courier | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_12_final.webp` | TODO |
| VEH-13 | Apex anti-grav cargo skiff | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_13_final.webp` | TODO |
| VEH-14 | Apex stellar service craft | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_14_final.webp` | TODO |
| VEH-15 | Orbital shuttle | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_15_final.webp` | TODO |
| VEH-16 | Prestige executive hovercar | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_16_final.webp` | TODO |
| VEH-17 | Singularity logistics drone swarm | Final isolated vehicle sprite/sheet with contact shadow and direction/readability suitable for world traffic. | `app/src/main/res/drawable-nodpi/zte_vehicle_17_final.webp` | TODO |

## E. Machines — 28 / 28 planned

| ID | Machine set | Description | Runtime target | Status |
|---|---|---|---|---|
| MCH-00-0 | Street Stand machine 1 | Foundry business 00: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_00_0_final.webp` | TODO |
| MCH-00-1 | Street Stand machine 2 | Foundry business 00: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_00_1_final.webp` | TODO |
| MCH-01-0 | Corner Shop machine 1 | Foundry business 01: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_01_0_final.webp` | TODO |
| MCH-01-1 | Corner Shop machine 2 | Foundry business 01: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_01_1_final.webp` | TODO |
| MCH-02-0 | Furnace Stall machine 1 | Foundry business 02: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_02_0_final.webp` | TODO |
| MCH-02-1 | Furnace Stall machine 2 | Foundry business 02: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_02_1_final.webp` | TODO |
| MCH-03-0 | Assembly Hub machine 1 | Foundry business 03: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_03_0_final.webp` | TODO |
| MCH-03-1 | Assembly Hub machine 2 | Foundry business 03: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_03_1_final.webp` | TODO |
| MCH-04-0 | Expansion Business 04 machine 1 | Expansion business 04: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_04_0_final.webp` | TODO |
| MCH-04-1 | Expansion Business 04 machine 2 | Expansion business 04: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_04_1_final.webp` | TODO |
| MCH-05-0 | Expansion Business 05 machine 1 | Expansion business 05: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_05_0_final.webp` | TODO |
| MCH-05-1 | Expansion Business 05 machine 2 | Expansion business 05: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_05_1_final.webp` | TODO |
| MCH-06-0 | Expansion Business 06 machine 1 | Expansion business 06: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_06_0_final.webp` | TODO |
| MCH-06-1 | Expansion Business 06 machine 2 | Expansion business 06: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_06_1_final.webp` | TODO |
| MCH-07-0 | Expansion Business 07 machine 1 | Expansion business 07: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_07_0_final.webp` | TODO |
| MCH-07-1 | Expansion Business 07 machine 2 | Expansion business 07: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_07_1_final.webp` | TODO |
| MCH-08-0 | Megastructure Business 08 machine 1 | Megastructure business 08: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_08_0_final.webp` | TODO |
| MCH-08-1 | Megastructure Business 08 machine 2 | Megastructure business 08: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_08_1_final.webp` | TODO |
| MCH-09-0 | Megastructure Business 09 machine 1 | Megastructure business 09: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_09_0_final.webp` | TODO |
| MCH-09-1 | Megastructure Business 09 machine 2 | Megastructure business 09: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_09_1_final.webp` | TODO |
| MCH-10-0 | Megastructure Business 10 machine 1 | Megastructure business 10: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_10_0_final.webp` | TODO |
| MCH-10-1 | Megastructure Business 10 machine 2 | Megastructure business 10: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_10_1_final.webp` | TODO |
| MCH-11-0 | Megastructure Business 11 machine 1 | Megastructure business 11: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_11_0_final.webp` | TODO |
| MCH-11-1 | Megastructure Business 11 machine 2 | Megastructure business 11: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_11_1_final.webp` | TODO |
| MCH-12-0 | Apex Business 12 machine 1 | Apex business 12: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_12_0_final.webp` | TODO |
| MCH-12-1 | Apex Business 12 machine 2 | Apex business 12: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_12_1_final.webp` | TODO |
| MCH-13-0 | Apex Business 13 machine 1 | Apex business 13: primary production mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_13_0_final.webp` | TODO |
| MCH-13-1 | Apex Business 13 machine 2 | Apex business 13: secondary logistics/energy mechanism; isolated moving parts, loop-safe pivot and 6–16 frame budget if animated. | `app/src/main/res/drawable-nodpi/zte_machine_13_1_final.webp` | TODO |

## F. Props — 28 / 28 planned

| ID | Prop | Description | Runtime target | Status |
|---|---|---|---|---|
| PRP-00-A | Street Stand operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_00_a_final.webp` | TODO |
| PRP-00-B | Street Stand environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_00_b_final.webp` | TODO |
| PRP-01-A | Corner Shop operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_01_a_final.webp` | TODO |
| PRP-01-B | Corner Shop environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_01_b_final.webp` | TODO |
| PRP-02-A | Furnace Stall operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_02_a_final.webp` | TODO |
| PRP-02-B | Furnace Stall environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_02_b_final.webp` | TODO |
| PRP-03-A | Assembly Hub operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_03_a_final.webp` | TODO |
| PRP-03-B | Assembly Hub environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_03_b_final.webp` | TODO |
| PRP-04-A | Expansion Business 04 operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_04_a_final.webp` | TODO |
| PRP-04-B | Expansion Business 04 environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_04_b_final.webp` | TODO |
| PRP-05-A | Expansion Business 05 operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_05_a_final.webp` | TODO |
| PRP-05-B | Expansion Business 05 environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_05_b_final.webp` | TODO |
| PRP-06-A | Expansion Business 06 operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_06_a_final.webp` | TODO |
| PRP-06-B | Expansion Business 06 environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_06_b_final.webp` | TODO |
| PRP-07-A | Expansion Business 07 operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_07_a_final.webp` | TODO |
| PRP-07-B | Expansion Business 07 environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_07_b_final.webp` | TODO |
| PRP-08-A | Megastructure Business 08 operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_08_a_final.webp` | TODO |
| PRP-08-B | Megastructure Business 08 environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_08_b_final.webp` | TODO |
| PRP-09-A | Megastructure Business 09 operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_09_a_final.webp` | TODO |
| PRP-09-B | Megastructure Business 09 environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_09_b_final.webp` | TODO |
| PRP-10-A | Megastructure Business 10 operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_10_a_final.webp` | TODO |
| PRP-10-B | Megastructure Business 10 environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_10_b_final.webp` | TODO |
| PRP-11-A | Megastructure Business 11 operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_11_a_final.webp` | TODO |
| PRP-11-B | Megastructure Business 11 environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_11_b_final.webp` | TODO |
| PRP-12-A | Apex Business 12 operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_12_a_final.webp` | TODO |
| PRP-12-B | Apex Business 12 environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_12_b_final.webp` | TODO |
| PRP-13-A | Apex Business 13 operational prop | Business-specific crate/tool/storage/signage-without-text element that reinforces function and scale. | `app/src/main/res/drawable-nodpi/zte_prop_13_a_final.webp` | TODO |
| PRP-13-B | Apex Business 13 environmental prop | Business-specific pipe/terminal/barrier/garden/utility element for foreground dressing and occlusion. | `app/src/main/res/drawable-nodpi/zte_prop_13_b_final.webp` | TODO |

## G. Terrain & infrastructure — 14 / 14 planned

| ID | Asset | Description | Runtime target | Status |
|---|---|---|---|---|
| TER-00 | Foundry cracked industrial ground tile | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_00_final.webp` | TODO |
| TER-01 | Foundry road/curb connector | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_01_final.webp` | TODO |
| TER-02 | Foundry rail/cargo strip | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_02_final.webp` | TODO |
| TER-03 | Foundry conduit trench | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_03_final.webp` | TODO |
| TER-04 | Expansion clean commercial pavement | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_04_final.webp` | TODO |
| TER-05 | Expansion multi-lane road connector | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_05_final.webp` | TODO |
| TER-06 | Expansion loading pad | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_06_final.webp` | TODO |
| TER-07 | Expansion energy conduit | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_07_final.webp` | TODO |
| TER-08 | Megastructure reinforced platform | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_08_final.webp` | TODO |
| TER-09 | Megastructure maglev/rail connector | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_09_final.webp` | TODO |
| TER-10 | Megastructure elevated service deck | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_10_final.webp` | TODO |
| TER-11 | Megastructure energy spine | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_11_final.webp` | TODO |
| TER-12 | Apex phase platform | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_12_final.webp` | TODO |
| TER-13 | Apex singularity/stellar connector | Seam-safe world tile/connector with transparent edges where required and no baked UI. | `app/src/main/res/drawable-nodpi/zte_terrain_13_final.webp` | TODO |

## H. FX sprite sheets — 18 / 18 planned

| ID | Asset | Description | Runtime target | Status |
|---|---|---|---|---|
| FX-00 | warm welding sparks | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_00_final.webp` | TODO |
| FX-01 | small furnace flame | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_01_final.webp` | TODO |
| FX-02 | large furnace/plasma flame | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_02_final.webp` | TODO |
| FX-03 | industrial smoke puff | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_03_final.webp` | TODO |
| FX-04 | steam vent | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_04_final.webp` | TODO |
| FX-05 | cyan energy pulse | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_05_final.webp` | TODO |
| FX-06 | warm energy pulse | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_06_final.webp` | TODO |
| FX-07 | construction dust/debris | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_07_final.webp` | TODO |
| FX-08 | upgrade construction flash | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_08_final.webp` | TODO |
| FX-09 | income pickup sparkle | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_09_final.webp` | TODO |
| FX-10 | electric arc | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_10_final.webp` | TODO |
| FX-11 | hologram scan sweep | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_11_final.webp` | TODO |
| FX-12 | drone thruster | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_12_final.webp` | TODO |
| FX-13 | phase distortion | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_13_final.webp` | TODO |
| FX-14 | orbital ion trail | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_14_final.webp` | TODO |
| FX-15 | stellar flare | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_15_final.webp` | TODO |
| FX-16 | singularity lens pulse | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_16_final.webp` | TODO |
| FX-17 | mastery crown shimmer | Small transparent loop/one-shot sheet; only raster when Canvas cannot match quality cheaply. | `app/src/main/res/drawable-nodpi/zte_fx_17_final.webp` | TODO |

## Progress ledger
- **DONE: 0 / 235**
- Buildings: **0 / 98**
- Power Core: **0 / 7**
- Characters: **0 / 24**
- Vehicles: **0 / 18**
- Machines: **0 / 28**
- Props: **0 / 28**
- Terrain/infrastructure: **0 / 14**
- FX: **0 / 18**

### Next production target
`BLD-00-T0 — Street Stand T0`.
