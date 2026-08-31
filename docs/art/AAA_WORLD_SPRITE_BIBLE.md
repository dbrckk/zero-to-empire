# ZERO → EMPIRE — AAA WORLD & SPRITE PRODUCTION BIBLE

Status: authoritative art-direction reference for the Tycoon World UI rebuild.
Scope: visual identity, world layout, sprite generation, slicing, animation, export, naming, performance and QA.
Rule: this file is the source of truth for future sprite/image-generation work. Any generated art must be checked against it before integration.

## 1. Product vision

ZERO → EMPIRE must feel like a living premium tycoon game, not a dashboard. The reference bar is the readability, immediacy and visual density of successful mobile tycoon games such as Idle Bank Tycoon, but the world, characters, architecture, props, color language, economy fantasy and silhouettes must remain original to ZERO → EMPIRE.

The player fantasy is: start with a tiny improvised operation and physically watch it become a colossal technological empire. Progress must be visible in the world itself. Money numbers support the fantasy; the world is the fantasy.

Target screen composition on the Empire tab:
- 65–75% active world scene.
- 10–15% compact top HUD.
- 10–15% contextual controls/upgrade surfaces.
- Bottom navigation stays readable but visually subordinate to the world.

Do not recreate copyrighted layouts, characters, buildings or UI assets from another game. Borrow only broad principles: playable scene first, strong upgrade feedback, readable production loops, polished animation and clear touch targets.

## 2. Original world identity — The Ascendant City

The empire is one continuous city that evolves through 11 eras. Its visual DNA is “scrap-to-singularity”: rough industrial survival becomes precision infrastructure, then vertical megacity, then planetary and post-physical civilization.

The city is presented in a stylized 2.5D/isometric-diagonal perspective designed for portrait phones. Camera is fixed enough for touch accuracy, with gentle parallax and cinematic pushes only during milestones. The scene should look hand-authored, not like a generic flat vector dashboard.

Core visual motifs:
- asymmetrical hexagonal industrial geometry;
- luminous energy conduits connecting businesses;
- rounded but substantial architecture with bevels and material depth;
- readable warm production lights against cooler environment tones;
- a central Power Core physically embedded into the city;
- moving citizens, drones, cargo, sparks, vehicles and resource streams;
- visible construction/evolution when a business crosses a milestone.

Never make the entire scene neon. Premium contrast comes from dark mass + selective emissive accents + warm operational light + restrained bloom.

## 3. Era bible — 11 world states

Each era keeps the same world geography so the player recognizes ownership and growth, but replaces materials, skyline, traffic, lighting and ambient FX.

### Era 1 — Scrappy Start
Mood: improvised survival district.
Materials: corrugated steel, patched concrete, painted scrap, exposed cables.
Lighting: warm bulbs, welding flashes, cool moon ambience.
Population: hand carts, workers, small utility bots.
Skyline: low and irregular.
Signature: the Power Core is a jury-rigged generator with visible coils.

### Era 2 — Workshop Grid
Mood: organized industrial neighborhood.
Materials: cleaner steel, modular frames, painted safety lines.
Lighting: practical industrial lamps.
Population: forklifts, compact delivery drones.
Signature: first permanent energy conduit network.

### Era 3 — Commercial Rise
Mood: prosperous mixed-use district.
Materials: glass inserts, anodized metal, signage panels.
Lighting: storefront warmth + cool infrastructure glow.
Population: more pedestrians and service vehicles.
Signature: taller businesses and animated signage.

### Era 4 — Automation District
Mood: highly efficient smart-factory city.
Materials: white composites, dark graphite, cobalt machinery.
Lighting: precise strips and machine indicators.
Population: robotic arms, autonomous cargo carriers.
Signature: synchronized production lines.

### Era 5 — Neon Metropolis
Mood: dense vertical wealth.
Materials: black glass, polished alloy, holographic surfaces used sparingly.
Lighting: layered signage, aerial traffic trails.
Population: sky taxis and maintenance drones.
Signature: first strong vertical skyline.

### Era 6 — Hypercity
Mood: infrastructure operating at impossible scale.
Materials: monolithic metal-ceramic shells.
Lighting: structural energy channels.
Population: dense automated transit streams.
Signature: bridges and elevated logistics between businesses.

### Era 7 — Orbital Economy
Mood: city linked to orbital industry.
Materials: aerospace composites, gold thermal accents, pressure-shell geometry.
Lighting: clean high-intensity emissive cores.
Population: launch craft, orbital elevators in background.
Signature: sky layer becomes economically active.

### Era 8 — Planetary Network
Mood: civilization-scale logistics.
Materials: ultra-clean adaptive surfaces.
Lighting: broad energy routing patterns.
Population: large drones, atmospheric freight.
Signature: distant planetary infrastructure visible on horizon.

### Era 9 — Quantum Dominion
Mood: reality-bending precision.
Materials: dark metamaterial, crystalline energy structures.
Lighting: violet/cyan phase effects with restrained use.
Population: teleport-like cargo transfer, phase drones.
Signature: parts of buildings appear suspended or spatially offset.

### Era 10 — Stellar Empire
Mood: energy economy at star scale.
Materials: radiant alloys, solar collector structures.
Lighting: warm stellar gold balanced by deep-space blue.
Population: high-altitude starcraft silhouettes.
Signature: Power Core becomes a miniature stellar containment structure.

### Era 11 — Singularity Crown
Mood: post-industrial transcendent capital.
Materials: near-seamless dark iridescent surfaces, white-gold energy, crystalline computation.
Lighting: elegant and calm, not noisy.
Population: sparse purposeful autonomous entities.
Signature: city architecture forms one coherent crown around the Power Core.

## 4. World layout for portrait mobile

Use a vertically scrollable district map rather than a stack of rectangular business cards.

Coordinate concept:
- Top: distant skyline / era landmark.
- Upper-mid: production lots 10–13.
- Mid: production lots 5–9.
- Lower-mid: production lots 0–4.
- Lower focal point: Power Core plaza.
- Foreground: road/rail/cargo path used for ambient traversal.

Every business lot must have:
1. ground footprint;
2. main building/sprite;
3. one looping production element;
4. one optional worker/vehicle route;
5. one upgrade badge anchor;
6. one income pop anchor;
7. one manager portrait anchor when automated;
8. a clear touch hitbox independent of transparent pixels.

Avoid placing labels over the most visually interesting part of a building. Information chips should hug edges of lots and collapse when not needed.

## 5. The 14 business lots

Business IDs remain canonical. Art can evolve without changing economy IDs or save data.

For production planning use four visual families matching existing code groups:
- IDs 0–3: Foundry District — tactile, scrappy, mechanical.
- IDs 4–7: Expansion District — logistics, commerce, infrastructure.
- IDs 8–11: Megastructure District — vertical, automated, monumental.
- IDs 12–13: Apex District — planetary/stellar/singularity-scale.

Each business gets seven visual tiers corresponding to progression milestones already used by the game. Tier changes must be more than recolors: silhouette, footprint, machinery density, verticality and ambient activity all increase.

Tier intent:
- T0: barely operational.
- T1: stable small operation.
- T2: professional facility.
- T3: automated complex.
- T4: district landmark.
- T5: megastructure.
- T6: mastery/crown form.

The exact current business names remain sourced from game data. Do not rename gameplay entities in art code simply to fit the concept.

## 6. Sprite-generation master specification

All generated production art must be created as layered masters with transparent background where applicable. Never generate only a flattened final image if animation is expected.

### Building master canvas
Preferred master: 2048×2048 PNG or layered source equivalent.
Working subject footprint: 80% maximum of canvas.
Transparent safety padding: at least 8% on all sides.
Perspective: consistent 2.5D three-quarter view; camera elevated approximately 30–38 degrees; dominant front face readable at phone size.
Light direction: upper-left key, soft cool fill from environment, selective emissive light from machinery.
No baked UI labels, currency, text, logos or level numbers.
No hard rectangular background.
No external drop shadow baked into the master unless it is an intrinsic contact shadow layer.

### Character master canvas
Preferred master: 1024×1024 per direction/pose or 2048×2048 sheet.
Readable head/body silhouette at 48–72 dp on device.
Avoid tiny facial features that disappear on mobile.
Separate accessories that may animate: arm/tool, carried box, tablet, helmet light.

### Props
512×512 or 1024×1024 masters depending on importance.
Examples: crates, terminals, drones, generators, signs, cargo pods, lamp posts, barriers, construction modules.

### FX
Prefer procedural Compose/Canvas for cheap particles, glow, rings and sparks when possible.
Use sprite FX only for distinctive authored phenomena such as portal distortion, steam plume, electrical arc sequence or holographic emblem.

## 7. Mandatory layer decomposition

Every complex business sprite intended for animation should be designed so it can be split into named layers. Minimum layer set:

- `base_ground`
- `building_back`
- `building_main`
- `building_front`
- `roof_static`
- `machine_static`
- `machine_moving_a`
- `machine_moving_b`
- `emissive_static`
- `emissive_pulse`
- `sign_static`
- `sign_glow`
- `foreground_occluder`
- `contact_shadow`

Optional layers:
- `door`
- `elevator`
- `fan`
- `conveyor`
- `vehicle`
- `worker`
- `smoke`
- `steam`
- `hologram`
- `energy_core`
- `construction_overlay`
- `mastery_crown`

The reason for this decomposition is to animate parts independently without redrawing the full sprite each frame. A fan can rotate, a conveyor can scroll, an emissive core can pulse and a door can open while the expensive building body remains static.

## 8. Sprite-sheet slicing contract

When frame-by-frame animation is required, use deterministic grids so later slicing is trivial.

Default animation sheet:
- PNG with transparent background.
- Frame size: 512×512 for major building animation; 256×256 for characters/props; 128×128 for small FX.
- Padding between frames: 4 px transparent minimum.
- All frames use identical canvas dimensions.
- Pivot must remain at the exact same pixel coordinate in every frame.
- Frames ordered left-to-right, then top-to-bottom.
- No trimming per frame before export.
- No variable frame sizes.

Naming:
`zte_<category>_<id>_<tier>_<animation>_<direction>_sheet_v###.png`

Examples:
- `zte_business_03_t2_production_se_sheet_v001.png`
- `zte_worker_foundry_t0_walk_se_sheet_v001.png`
- `zte_fx_quantum_portal_t0_loop_na_sheet_v001.png`

Companion metadata file when sheets are introduced:
`<same_name>.json`

Metadata fields:
```json
{
  "frameWidth": 512,
  "frameHeight": 512,
  "columns": 6,
  "rows": 2,
  "frameCount": 12,
  "fps": 12,
  "loop": true,
  "pivotX": 256,
  "pivotY": 410,
  "hitbox": [96, 118, 320, 310],
  "events": [{"frame": 7, "name": "production_pulse"}]
}
```

Animation frame budgets:
- idle micro-loop: 4–8 frames at 6–10 fps;
- production action: 8–16 frames at 10–15 fps;
- worker walk: 6–10 frames at 10–14 fps;
- construction/evolution reveal: 10–20 frames or procedural tween, one-shot;
- premium hero event: up to 24 frames only if memory budget remains safe.

Avoid 30–60 fps sprite sheets. Mobile polish comes from timing/easing, not huge texture memory.

## 9. Pivot and anchor standard

Buildings: pivot at bottom-center of the ground footprint.
Characters: pivot between feet.
Vehicles: pivot center of wheelbase/contact footprint.
Flying drones: pivot visual center, with separate shadow anchor projected to ground.
FX: pivot at effect origin.

Normalized anchor recommendations:
- income pop: (0.50, 0.18)
- upgrade badge: (0.82, 0.22)
- manager badge: (0.18, 0.20)
- production FX: authored per business
- ground connection: (0.50, 0.88)

These anchors must stay stable across animation frames and, where possible, across visual tiers.

## 10. Core animation language

AAA target means layered motion, not everything moving at once.

Every active lot should have one primary loop and at most two subtle secondary loops visible simultaneously.

Primary loops by family:
- Foundry: piston, belt, press, welding cycle.
- Expansion: cargo flow, shutters, scanner, vehicle docking.
- Megastructure: elevator, energy routing, orbital ring, robotic service arms.
- Apex: containment field, phase ring, stellar collector or reality distortion.

Secondary motion examples:
- small fan rotation;
- indicator chase;
- steam burst every several seconds;
- worker passing through;
- sign shimmer;
- cable pulse.

Do not run independent infinite transitions for every element in a LazyColumn. Prefer one world clock/phase and derive offsets from stable IDs. Battery saver/reduced-motion must freeze decorative loops and preserve gameplay readability.

## 11. Character system

Characters make the city feel alive. They are not decorative stickers; they communicate scale and automation.

Base civilian/worker archetypes:
- mechanic;
- courier;
- technician;
- analyst;
- engineer;
- logistics operator;
- executive;
- autonomous service bot.

Managers remain visually distinctive portraits but should also gain a tiny world avatar/marker once hired. World avatar identity can be simplified while preserving silhouette/color cues from the portrait.

Character animation set:
- idle A/B;
- walk SE/SW where needed;
- work/use-terminal;
- carry item;
- celebrate milestone;
- optional inspect/repair.

Characters must never block purchase taps. Their render layer can overlap buildings while pointer input remains bound to the lot.

## 12. UI art direction

HUD should feel integrated with the world rather than made of giant cards.

Top HUD:
- one compact translucent/opaque premium bar;
- cash/net worth largest value;
- income/s nearby;
- gems and boost as compact chips;
- no giant statistic grid above gameplay.

Business interaction:
- tap building → compact bottom sheet or anchored upgrade panel;
- upgrade button strong and tactile;
- cost and next visual milestone visible;
- buy mode selector remains accessible but compact;
- manager automation shown directly on lot.

Goals/store/boost:
- floating side buttons or compact upper-corner shortcuts;
- avoid covering central world action;
- notification badges small and purposeful.

Bottom navigation:
- Empire, Managers, Upgrades, Goals;
- icons should be custom consistent glyphs, not unrelated Unicode characters in final art;
- selected state uses shape + brightness, not only color.

## 13. Material and lighting rules

Material hierarchy:
1. matte structural mass;
2. metallic edge/trim;
3. glass or dark translucent panel;
4. emissive operational detail;
5. rare premium gold/mastery accent.

Gold is a reward/mastery material, not the default for every object.
Cyan means energy/infrastructure.
Violet means quantum/advanced systems.
Green means positive/operational state.
Red/orange reserved for warning, heat, construction sparks and high-energy machinery.

Use contact shadows to ground sprites. Use ambient occlusion-like darkening at intersections. Avoid flat gradients with no material cues.

## 14. Depth stack

Recommended world render order:
1. sky/background matte;
2. distant skyline;
3. rear infrastructure;
4. rear business lots;
5. mid roads/rails;
6. main business bodies;
7. characters/vehicles sorted by ground Y;
8. foreground business parts/occluders;
9. local FX;
10. world-space badges;
11. HUD/navigation;
12. milestone/era cinematic overlay.

This allows a worker to walk “behind” a front awning or machine, which adds significant perceived depth.

## 15. Power Core redesign

The Power Core remains a major game mechanic but becomes a physical city landmark rather than a separate 200 dp dashboard card.

World form:
- central plaza/reactor;
- tap anywhere on the core hit area to inject capital;
- tap triggers compression, light pulse, radial conduit activation and nearby city response;
- combo can appear as a temporary world-space label;
- higher eras physically replace the reactor shell.

Tap feedback sequence:
0 ms: touch compression and haptic;
40–120 ms: core flash;
80–240 ms: energy ring/conduit pulse;
150–450 ms: income pop and nearby machinery response;
450–700 ms: settle.

Reduced motion: keep immediate luminance/scale confirmation, remove traveling particles and camera movement.

## 16. Business evolution presentation

A milestone should visibly transform the lot.

Preferred sequence:
- brief highlight/outline;
- construction drones or energy scaffold;
- old tier dims/dissolves behind transformation mask;
- new silhouette reveals from ground upward;
- machinery starts;
- final mastery flash and income label.

Duration target: 650–1100 ms depending on significance. Do not interrupt input longer than necessary.

Tier evolution must preserve the lot’s positional footprint so the world does not jump unexpectedly.

## 17. Asset directory contract

When raster assets are added, use:

`app/src/main/res/drawable-nodpi/world/` only if Android resource organization supports it cleanly; otherwise use Android-compatible resource directories plus a parallel source-art folder outside packaged resources.

Recommended repository structure for source art:

```
art_source/
  world/
    era_01/
    era_02/
    ...
    era_11/
  businesses/
    b00/
      t0/
      ...
      t6/
    ...
    b13/
  characters/
  props/
  fx/
  ui/
  atlases/
```

Runtime exported assets:

```
app/src/main/res/drawable-nodpi/
  zte_world_...
  zte_business_...
  zte_character_...
  zte_prop_...
  zte_fx_...
```

If Android resource naming requires flattening, preserve the same prefixes and IDs.

## 18. Generation prompt template

Future image-generation prompts for a business must include all of the following:

“Original premium mobile tycoon game asset for ZERO → EMPIRE; stylized 2.5D three-quarter perspective; portrait-mobile readability; [ERA]; [BUSINESS FUNCTION]; [TIER]; strong readable silhouette; layered industrial architecture; matte structural mass, metallic trim, selective emissive details; upper-left key light, cool environmental fill; transparent background; centered stable ground footprint; no text, no logo, no UI, no watermark; animation-ready separation of [LIST MOVING PARTS]; unique original design, do not imitate or reproduce another game’s specific asset.”

For sprite sheets also specify:
“identical frame canvas, fixed camera, fixed pivot, transparent background, no frame trimming, consistent scale, [N] frames, left-to-right sequence.”

## 19. Acceptance criteria for every generated sprite

A sprite is rejected if any of these fail:
- silhouette unreadable at target phone size;
- inconsistent camera/perspective with neighboring lots;
- lighting direction inconsistent;
- moving parts fused into body when animation is expected;
- background accidentally baked in;
- excessive empty padding or clipped glow;
- text/gibberish labels generated into art;
- no stable pivot;
- visual tier looks only recolored rather than upgraded;
- too visually similar to a third-party game asset;
- poor transparency edges/halos;
- excessive micro-detail that aliases on phone;
- loop produces visible jump;
- asset causes excessive memory/GPU cost.

## 20. Performance budgets

Target: smooth gameplay on ordinary Android hardware while preserving premium appearance.

Rules:
- atlas compatible assets where useful;
- avoid decoding giant 4K images at runtime for small sprites;
- prefer static building body + animated sublayers;
- reuse world animation phase clocks;
- off-screen district animation should pause or reduce substantially;
- low-power/reduced-motion removes particles and decorative loops;
- major full-screen effects are transient, never permanent;
- test compact screens below 360 dp width;
- do not add expensive blur layers to every lot.

Texture guidance:
- visible major building at normal zoom: runtime target around 512–1024 px effective resolution;
- small props: 128–512 px;
- characters: 256–512 px sheets depending on frame count;
- aggressively avoid multiple 2048 sheets simultaneously resident when unnecessary.

## 21. Animation QA checklist

For each animation verify:
- frame order correct;
- pivot stable to within 1 px;
- no transparent-edge flicker;
- loop seam clean;
- no unintended scale breathing;
- frame timing feels mechanical/physical rather than linear slideshow;
- important motion readable at 1× phone scale;
- animation stops correctly off-screen/reduced-motion;
- no touch target movement;
- no visual desync that implies wrong economy timing.

## 22. Implementation roadmap — Tycoon World UI 10-step rebuild

1. World shell: replace dashboard-first Empire layout with a playable city scene and compact HUD.
2. Era 1 district: build complete Scrappy Start scene with first visible lots and Power Core plaza.
3. Lot interaction: world-space business selection, upgrade panel, buy modes and affordability feedback.
4. Sprite pipeline: introduce first layered/generated production sprites, slicing metadata and runtime loader/renderer.
5. Living city: workers, cargo, drones, production loops and depth sorting.
6. Visual evolution: seven tiers per business with construction/milestone transitions.
7. Era evolution: environment/skyline/material changes for all 11 eras.
8. Manager integration: manager world presence, automation indicators and premium portraits connected to lots.
9. Cinematic polish: camera emphasis, impact FX, audio/haptics synchronization, reduced-motion variants.
10. Device QA/final art pass: small phones, performance, texture memory, clipping, contrast, touch targets and final APK validation.

## 23. Non-negotiable gameplay safety

The visual rebuild must not silently alter:
- business costs;
- income formulas;
- tap rewards;
- prestige rewards;
- reward/ad amounts;
- billing products;
- save schema or DataStore name;
- progression thresholds unless explicitly approved as a gameplay change.

World visuals read existing state; they do not redefine economy state.

## 24. Source-of-truth rule for future work

Before generating, slicing or coding a new visual asset, consult this file and answer internally:
1. Which era/family/tier does it belong to?
2. What is its stable pivot?
3. Which layers move independently?
4. Does it need frames or can motion be procedural?
5. What is the exact export naming convention?
6. What is its reduced-motion behavior?
7. Does it remain original rather than copying a third-party game?
8. Can it render smoothly on a portrait Android phone?

If any answer is unclear, define it in this file before mass-producing sprites.

## 25. Definition of AAA for ZERO → EMPIRE

AAA here does not mean console photorealism. It means every visible element has deliberate art direction, material depth, hierarchy, animation purpose, responsive touch feedback and consistent world logic. The player should understand progression by looking at the city before reading numbers.

Final visual target: when a player opens the Empire tab, the first impression should be “my empire is alive and growing,” not “I am looking at a finance dashboard.”
