# AAA Manager Portrait Production Spec

Status: **PRE-PRODUCTION — NOT PART OF THE 236-SPRITE STRICT COUNT**

This document defines original Zero to Empire manager portraits. It may use external idle-game analysis only as an abstract production reference for activity, hierarchy and polish. No reference-game character, costume, pose, branding, mesh, texture, layout or code may be copied.

## Runtime target

- 14 unique managers matching `Managers.catalog`.
- Square source master: **1024×1024**.
- Runtime export: **512×512 WebP/PNG**, transparent or authored portrait-card background as specified by the resolver.
- Must remain recognizable at the live Managers-tab size of **62 dp**.
- Face/helmet/head silhouette occupies roughly 32–42% of portrait height.
- Strong value separation between face, costume and background.
- One dominant accent plus one supporting accent; avoid neon-on-neon flattening.
- No baked text, logos, UI labels, watermark, signature, fake frame text or currency symbols.
- No generic photorealism; art must remain consistent with Zero to Empire's stylized 2.5D / premium sci-fi progression.
- No direct resemblance to known IP characters or the Idle Bank reference APK.

## Shared lighting language

- Key light: upper-left/front, soft but directional.
- Rim: role accent, strongest on shoulders/head silhouette.
- Fill: cool neutral, never enough to flatten facial planes.
- Background: controlled radial/architectural depth; manager remains primary focal point.
- Materials evolve with the empire: cloth/leather → technical polymers/metals → lunar/planetary composites → stellar/reality materials.
- Endgame glow is restrained and physically localized; avoid full-image bloom.

## Character roster

| ID | Manager | Title | Core silhouette | Material / visual cue | Accent |
|---:|---|---|---|---|---|
| 0 | Maya | Street Hustler | cap/jacket, forward entrepreneurial stance | worn premium streetwear, small commerce device | green + warm gold |
| 1 | Noah | Retail Operator | smart glasses, structured retail jacket | clean fabric, compact inventory tablet | blue + cyan |
| 2 | Ava | Production Chief | protective industrial collar / headset | brushed steel, heat-safe textile | orange + amber |
| 3 | Leo | Factory Director | hard industrial helmet, broad executive shoulders | dark engineered alloy, factory insignia shapes without text | violet + cyan |
| 4 | Nova | Tech Visionary | asymmetric tech eyewear / slim high collar | glass, dark polymer, micro-emissive seams | cyan + mint |
| 5 | Atlas | City Architect | architectural collar / projection tool | graphite, urban glass, blueprint-like light geometry without text | blue + electric cyan |
| 6 | Luna | Lunar Governor | pressure-suit executive silhouette | white ceramic/composite, lunar silver | ice white + cyan |
| 7 | Ares | Martian Chancellor | angular planetary armor-jacket | red composite, copper/bronze engineering details | red + amber |
| 8 | Sol | Stellar Engineer | solar crown/tool halo integrated into suit | gold ceramic, heat-shield metal | solar gold + orange |
| 9 | Orion | Galactic Broker | elegant asymmetric finance/exchange silhouette | dark luxury alloy, holographic market geometry without charts/text | violet + cyan |
| 10 | Vega | Intergalactic Navigator | navigator visor / star-map collar | deep navy alloy, optical glass | cyan + indigo |
| 11 | Lyra | Cosmic Fabricator | fabrication crown / articulated shoulder tool | pale alloy, violet fabrication fields | violet + cyan |
| 12 | Axiom | Reality Systems Architect | precise geometric headpiece / reality lattice | black-violet metamaterial, controlled magenta energy | magenta + amber |
| 13 | Zenith | Transcendence Director | calm apex silhouette, minimal crown/halo | white-gold transcendent composite, sparse violet edge energy | gold + violet |

## Composition rules

1. Head and torso must read immediately before secondary props.
2. Every manager must have a unique outer silhouette at 62 dp.
3. Props are limited to one primary profession cue and at most one secondary cue.
4. Hands/props may not obscure both sides of the face.
5. Avoid identical three-quarter poses across the roster; vary shoulder angle, head turn and prop placement while retaining UI consistency.
6. Background detail must be at least one value step quieter than the face/costume.
7. Skin, hair, age presentation and face structure should vary across the roster without relying on stereotypes.
8. Later managers must feel more advanced through material language and silhouette, not merely by adding more glow.

## Production and review states

A manager portrait follows:

`CANDIDATE → TECHNICAL → ART_REVIEW → RUNTIME → APPROVED`

**CANDIDATE**
- Generated/authored source exists.
- It is not considered production-ready.

**TECHNICAL**
- dimensions and encoding correct;
- no corruption;
- alpha/background contract correct;
- safe crop at 62 dp;
- no baked text/watermark.

**ART_REVIEW**
- manager identity matches this spec;
- face/hands/props are anatomically coherent for the chosen stylization;
- no duplicated/warped accessories;
- lighting/materials are coherent;
- silhouette is distinct from every already-approved manager;
- passes 62 dp readability review.

**RUNTIME**
- exact reviewed export is referenced by the manager portrait resolver;
- Managers tab shows the correct manager ID;
- no clipping in compact/large font configurations;
- reduced-motion rules remain valid if any overlay animation exists.

**APPROVED**
- technical + semantic/art + runtime evidence persisted;
- Android CI green on the exact runtime commit;
- screenshot/contact-sheet review shows no regression against previously approved managers.

## Automatic rejection conditions

Reject a candidate if any of the following is present:

- extra/missing fingers that are visually salient at runtime;
- malformed face, eyes, teeth or glasses;
- duplicated tools/accessories;
- unreadable silhouette at 62 dp;
- pseudo-text, random glyphs, watermark or logo;
- background rectangle/halo that looks like an accidental generation plate;
- inconsistent perspective between head/body/prop;
- uncontrolled bloom hiding material detail;
- generic costume that does not communicate the manager's profession/progression;
- near-duplicate pose/costume of another Zero to Empire manager;
- visual imitation of a reference game's named character.

## First production wave

Produce and review only **IDs 0–3 (Maya, Noah, Ava, Leo)** first.

Reason:
- they are encountered earliest;
- they define the roster's grounded visual baseline;
- mistakes in lighting, face scale or runtime crop can be corrected before generating the ten later managers;
- later managers can then escalate materials and technology from a stable baseline.

The first wave is complete only when all four pass full-resolution art review and are proven readable in the live Managers tab.
