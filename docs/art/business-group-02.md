# Business Group 02 — AAA Art Direction

Businesses 5–8 are treated as the second visual escalation tier of Zero to Empire. They must clearly feel beyond the terrestrial/industrial scale of Group 01 while remaining readable at mobile icon sizes.

## 5. Tech Company
- Identity: violet + cyan, glass/metal, clean high-tech campus.
- Base silhouette: compact monolithic headquarters with luminous data core.
- Lv25: roof light-bar and stronger emissive facade.
- Lv100: orbital/data nodes and secondary illuminated modules.
- Lv250: wider campus extensions and energy lattice.
- Lv500: prestige ring, denser vertical accents, crown lighting.
- Lv1000/Mastered: ascendant halo, gold-white highlights, full network aura.
- Idle: data-core pulse, rotating radial links, subtle facade breathing.
- Unlock: dark shell -> cyan scan -> violet core ignition -> full reveal.

## 6. Megacity
- Identity: neon violet skyline with cyan/gold windows.
- Base silhouette: multi-tower urban cluster.
- Lv25: taller secondary towers and first skybridge.
- Lv100: denser skyline and transit nodes.
- Lv250: orbital traffic lights and holographic banner.
- Lv500: vertical energy spines and crown tower expansion.
- Lv1000/Mastered: full city aura, orbital light traffic and prestige halo.
- Idle: window shimmer, traffic/orbit nodes, breathing skyline glow.
- Unlock: city grid boots sector by sector from darkness.

## 7. Moon Colony
- Identity: ice-cyan, white, brushed lunar steel.
- Base silhouette: three linked habitat domes on lunar regolith.
- Lv25: active antenna and connector illumination.
- Lv100: secondary habitat ring and landing markers.
- Lv250: additional orbital communication effects.
- Lv500: large protective energy arc and expanded platform.
- Lv1000/Mastered: crystalline halo, white emissive mastery nodes.
- Idle: rotating dish, dome reflections, slow communication sweep.
- Unlock: lunar dust silhouette -> dome pressure lights -> antenna sweep -> reveal.

## 8. Mars Empire
- Identity: red-orange + imperial gold.
- Base silhouette: fortified Martian palace/industrial citadel.
- Lv25: gold perimeter power line and stronger central reactor.
- Lv100: expanded side wings and red energy nodes.
- Lv250: orbital sentinels and imperial crest lighting.
- Lv500: large outer ring and stronger citadel aura.
- Lv1000/Mastered: gold mastery halo, crown lights, planetary dominance treatment.
- Idle: reactor pulse, orbiting red nodes, warm atmospheric breathing.
- Unlock: red dust shadow -> reactor ignition -> palace outline -> imperial reveal.

## Shared visual rules
- Six progression states: Base, Lv25, Lv100, Lv250, Lv500, Lv1000/Mastered.
- Silhouette must change structurally, not only via glow.
- Full-motion mode keeps all particles, orbit nodes and pulses.
- Reduced-motion keeps a static premium frame with no infinite motion dependency.
- Power-save reduces orbiters, particles and decorative layers while preserving identity.
- Must remain recognizable at 50–64dp and look premium at hero size.
- All art is generated procedurally in Compose/Canvas and uses no third-party copyrighted assets.

## Runtime integration
- `BusinessGroup02Art.kt` renders the primary assets.
- `BusinessGroup02Evolution.kt` adds structural progression overlays.
- `EmpireArtCompat.kt` routes IDs 4–7 to the Group 02 renderers using the real business level.
- Android CI validates unit tests, debug and optimized release R8 builds.
