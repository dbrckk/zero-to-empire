# ZERO → EMPIRE — Era 1 Vertical Slice Production Spec

Status: canonical production brief for the first authored Ascendant City slice.
Companions: `AAA_WORLD_SPRITE_BIBLE.md`, `AAA_SPRITE_PRODUCTION_QUEUE.txt`.

## Objective

Prove the final world-art pipeline on one phone-screen district before mass-producing the remaining 98 business tiers. The target is a readable, lively premium mobile tycoon world with original ZERO → EMPIRE architecture. Do not copy layouts, buildings, characters, UI, props, or identifiable visual assets from another game.

## Camera lock

- Portrait-mobile 2.5D.
- Elevated three-quarter camera: 34° nominal; acceptable 30–38°.
- Building verticals remain vertical; ground axes share one consistent projection.
- Warm key from upper-left, cool ambient fill from upper-right/front.
- Bottom-center pivot for every world object.
- Masters: 2048×2048 transparent PNG, 8% safe padding minimum.
- Preview gates: 176 dp hero lot and 88 dp normal lot.

## Era 1 material language

Patched dark steel, corrugated sheet, cast concrete, exposed copper, worn painted safety metal, rubber belts, warm tungsten work lights. Cyan energy is scarce and functional. Gold marks premium/progression states. Avoid covering entire structures in neon.

## Vertical-slice scene composition

The first playable view must contain:

1. Business 00 hero foundry at T0/T1/T2.
2. Business 01 press at T0/T1.
3. Business 02 furnace at T0.
4. Business 03 fabrication bench at T0.
5. Era 1 Power Core plaza.
6. One mechanic and one courier world avatar.
7. One forklift and one hand cart.
8. Shared prop kit: small/heavy crate, barrier, industrial lamp, terminal, straight/elbow/junction pipe, vent, warning beacon.
9. Road, lot foundations and cheap energy/lighting FX remain procedural where this improves performance.

The four businesses must read as physical neighbors in one industrial district, not four UI cards floating over a background.

## Business 00 — Foundry / belt-piston line

### T0 — improvised bench
Silhouette: low asymmetrical workshop, one lean-to roof, visible belt table.
Static layers: base_ground, building_back, building_main, building_front, roof_static, machine_static, emissive_static, sign_static, foreground_occluder, contact_shadow.
Moving layers: machine_moving_a = belt; machine_moving_b = piston; steam optional.
Animation: belt 8 frames / 12 fps; piston 8 frames / 12 fps; occasional welding flash procedural.
Readability cue: exposed copper pipe and warm task lamp.

### T1 — workshop
Silhouette: wider two-bay workshop with taller central machine housing and exterior pipe stack.
Changes from T0 must be structural: second bay, stronger roofline, enclosed piston, crate dock. Do not merely recolor T0.
Animation: synchronized belt + piston; subtle warning beacon.

### T2 — machine hall
Silhouette: substantial factory block with raised central hall, two production lanes and roof exhaust assembly.
Changes: taller mass, doubled production frontage, enclosed material feed, service platform, stronger cyan machine status light.
Animation: dual belt motion with shared phase; piston bank; steam burst as intermittent secondary effect.

## Business 01 — Press

### T0
Compact scrap press under a reinforced canopy. Large readable vertical ram is the hero shape. One crate staging zone.
Animation: press down/hold/up, 10–12 frames, 10 fps.

### T1
Enclosed compact press building with stronger frame, side accumulator and safety beacon. Structural upgrade must remain obvious at 88 dp.

## Business 02 — Furnace T0

Small burner/furnace block with one cylindrical hot chamber and short exhaust. Warm orange internal heat is the identity accent; cyan remains secondary infrastructure light. Rotating/heat mechanism must be separable from static shell.

## Business 03 — Fabrication T0

Hand-assembly/fabrication shed with visible robotic-tool precursor or articulated work arm, material feeder and spark point. Keep silhouette different from Business 00: taller narrow tool mast instead of long belt profile.

## Power Core — Era 1

A physical district machine, not a UI medallion. Ground plinth + containment cradle + central energy object + two mechanical braces + cable/conduit sockets. Dark steel and copper dominate; white-gold core light is the focal point. Keep core, braces, emissive pulse, foreground occluder and contact shadow separable.

Idle animation: restrained 6–8 frame/pulse equivalent. Tap impact remains procedural so input feedback can scale cheaply. Reduced-motion mode must have a complete static frame.

## Characters

### Mechanic
Readable at 48–72 dp. Work jacket, gloves, compact tool, broad stance. Required: idle_a, walk_se, walk_sw, work. 256×256 frames, stable bottom-center pivot.

### Courier
Distinct slimmer silhouette, cargo satchel/container, brighter route marker accent. Required: idle_a, walk_se, walk_sw, carry.

Faces are secondary at world scale; silhouette, costume blocks and carried object must identify role.

## Vehicles

### Forklift
Chunky compact industrial forklift with visible forks and overhead guard. idle and 6–8 frame travel loop. Driver can be implied at small scale.

### Hand cart
Simple two-wheel/trolley cargo prop with loaded and empty variants. Static by default; movement can be transform-driven rather than frame-animated.

## Animation contract

- Shared world animation clock; deterministic per-ID phase offsets.
- Never create an independent permanent Compose infinite transition per lot.
- One primary production loop + maximum two subtle secondary motions visible per lot.
- Decorative motion stops in reduced-motion/battery-saver mode.
- Frame pivots and occupied volume remain stable.
- No per-frame trimming.
- Production sheets: left-to-right then top-to-bottom.

## Asset naming examples

`zte_business_00_t0_building_main_v001.png`
`zte_business_00_t0_machine_moving_a_v001.png`
`zte_business_00_t0_production_se_sheet_v001.png`
`zte_business_00_t0_production_se_sheet_v001.json`
`zte_power_core_e01_core_v001.png`
`zte_worker_mechanic_walk_se_sheet_v001.png`
`zte_vehicle_forklift_travel_se_sheet_v001.png`

## Integration rule

Authored art is progressively substituted into `BusinessArtIcon`/world rendering. Missing authored assets must fall back to the existing procedural art. No business IDs, levels, costs, income formulas, reward amounts, save keys/schema, ad policy, billing product IDs or entitlement behavior may change as part of art integration.

## Acceptance gates

A vertical slice is accepted only when:

- all four businesses are identifiable without labels at 88 dp;
- T0→T1→T2 for Business 00 is clearly structural;
- Business 00 and Business 03 cannot be confused by silhouette;
- Power Core reads as a world object before its label is seen;
- foreground/background overlap creates depth without hiding purchase affordance;
- no accidental matte/background exists around sprites;
- animations have stable pivots and no frame jitter;
- static reduced-motion rendering remains complete;
- 360dp-class phone composition remains readable;
- existing gameplay/economy/save/monetization tests remain unchanged and green.

## Production sequence

1. Generate/author Business 00 T0 master and layers.
2. Validate at 176 dp and 88 dp.
3. Produce T1 and T2 using the exact camera/light/pivot contract.
4. Produce Business 01 T0/T1, Business 02 T0, Business 03 T0.
5. Produce Power Core.
6. Produce mechanic/courier and forklift/hand cart.
7. Integrate static assets behind a procedural fallback router.
8. Add shared-clock animation sheets.
9. Run compact-phone/reduced-motion/performance QA.
10. Only after this slice passes, scale the same pipeline to the remaining tiers.
