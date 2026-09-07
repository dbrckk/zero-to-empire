#!/usr/bin/env python3
"""Building factory v16: positive-design source locking + live QA.

Goal: prevent semantic contamination at generation time instead of relying on
negative-prompt cleanup after the fact. Uses precise family design cards,
explicit tier blueprints, conservative img2img evolution, multi-anchor search,
and the v15.2 live geometric QA machinery.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('v15',HERE/'kaggle_building_family_factory_v15.py')
v15=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(v15)
v14=v15.v14

print('KAGGLE_STARTUP=building-family-flux-v16-positive-source-locked',flush=True)

# Make evolution preserve the approved anchor instead of reinventing the scene.
v14.STRENGTH.update({1:.24,2:.29,3:.34,4:.39,5:.44,6:.49})
v14.STEPS.update({0:7,1:6,2:6,3:7,4:7,5:8,6:8})

# Positive design cards deliberately avoid naming unwanted construction/civic motifs.
FAMILY={
 0:'compact street foundry kiosk; rectangular rust-steel shell; recessed amber furnace mouth; short roof exhaust; integrated side tool cabinet',
 1:'compact fabrication shop; chamfered graphite storefront; enclosed machining bay; low rear loading recess; roof ventilation box',
 2:'furnace works; broad low steel hall; two short enclosed heat stacks; central glowing furnace chamber; heavy ribbed wall panels',
 3:'assembly hub; long dark production hall; enclosed robotic spine visible through central bay; symmetric feeder modules attached to both sides',
 4:'precision CNC factory; low graphite rectangular shell; three recessed CNC bay doors; clean ribbed roof; small enclosed utility pod',
 5:'energy-cell works; square alloy production block; protected amber reactor core behind front grille; attached capacitor rooms; dense cable conduits',
 6:'coolant plant; silver graphite low hall; thick cyan coolant pipes integrated into walls; two compact heat exchangers; enclosed pump room',
 7:'automation works; wide low tech factory; paired enclosed robot cells; continuous roof service spine; symmetric attached production wings',
 8:'heavy forge; armored low production block; central orange forge chamber; thick buttressed walls; roof exhaust manifolds; massive enclosed press bay',
 9:'nanofabrication complex; clean pearl graphite block; sealed cyan process ring built into facade; compact filtration towers; symmetric cleanroom wings',
 10:'orbital component works; dark alloy factory block; enclosed circular assembly cradle built into center; radial service rooms attached to main shell',
 11:'actuator works; broad press-house factory; two enclosed articulated press frames inside facade bays; reinforced roof trusses contained within shell',
 12:'phase foundry; pearl alloy production block; enclosed luminous containment ring embedded in central chamber; symmetric shielded process wings',
 13:'stellar manufacturing works; dark pearl industrial base; four integrated reactor petals around a central enclosed process core; compact luminous roof crown'
}

TIER={
 0:'starter version: one storey, compact footprint, one primary production chamber, simple roofline, sparse integrated machinery',
 1:'reinforced version: same footprint and facade identity, thicker shell, one attached utility room, clearer production bay',
 2:'expanded version: wider main hall, second attached production module, denser wall conduits, still low industrial profile',
 3:'automated version: same factory enlarged, central enclosed automation volume, two attached process modules, modest vertical rise',
 4:'advanced version: broader integrated factory, symmetric attached wings, denser enclosed machinery, premium industrial cladding',
 5:'late-game version: very large connected production complex, multiple enclosed process halls, stronger vertical core, all machinery integrated into architecture',
 6:'ultimate version: monumental but unmistakably industrial factory, largest connected footprint, tall enclosed production core, compact integrated luminous crown'
}

STYLE=('premium AAA mobile strategy-game building asset; stylized 2.5D industrial architecture; '
       'single connected finished operating factory; clean 34-degree orthographic three-quarter view; '
       'graphite steel alloy materials; upper-left key light; cool fill; restrained amber and cyan emissive accents; '
       'isolated object centered on uniform neutral gray studio background reaching every image edge')


def prompts(i):
    family=FAMILY[i['family']]
    tier=TIER[i['tier']]
    short=f'{STYLE}. {family}. {tier}.'
    # Positive-only second encoder text: specify what must occupy the image, not what must be absent.
    detail=(f'Exactly one coherent industrial production building. Design identity: {family}. Evolution state: {tier}. '
            'Keep the same facade axis, roof direction, production core, material palette and attached-module logic across upgrades. '
            'All visible equipment is enclosed, wall-mounted, roof-mounted, or structurally integrated into the factory. '
            'The silhouette is compact, mechanically plausible, bottom-heavy and readable at mobile-game scale. '
            'The object ends cleanly at its structural footprint and the neutral gray studio background remains visible around the full silhouette.')
    return short,detail

v14.prompts=prompts
v15.prompts=prompts

# More anchor diversity, but only the best positive-design anchors are evolved.
v15.ANCHORS=6
v15.BRANCHES=2
v15.CONTEXT_RETRIES=4

if __name__=='__main__':
    v15.main()
