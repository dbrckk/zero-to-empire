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

# Preserve an approved family anchor instead of reinventing the scene at every tier.
v14.STRENGTH.update({1:.24,2:.29,3:.34,4:.39,5:.44,6:.49})
v14.STEPS.update({0:7,1:6,2:6,3:7,4:7,5:8,6:8})

FAMILY={
 0:'street foundry kiosk, rectangular rust-steel shell, recessed amber furnace mouth, short roof exhaust',
 1:'fabrication shop, chamfered graphite shell, enclosed machining bay, low rear loading recess',
 2:'furnace works, broad low steel hall, twin short heat stacks, central glowing furnace chamber',
 3:'assembly hub, long dark production hall, enclosed robotic spine, symmetric attached feeder bays',
 4:'precision CNC factory, low graphite rectangular shell, three recessed CNC bays, ribbed roof',
 5:'energy-cell works, square alloy block, protected amber reactor core, attached capacitor rooms',
 6:'coolant plant, silver graphite hall, integrated cyan coolant pipes, compact heat exchangers',
 7:'automation works, wide low tech factory, paired enclosed robot cells, attached production wings',
 8:'heavy forge, armored low production block, central orange forge chamber, enclosed press bay',
 9:'nanofabrication complex, pearl graphite block, sealed cyan process ring, symmetric cleanroom wings',
 10:'orbital component works, dark alloy factory block, enclosed circular assembly cradle, radial service rooms',
 11:'actuator works, broad press-house factory, enclosed articulated press frames, reinforced roof shell',
 12:'phase foundry, pearl alloy production block, enclosed luminous containment ring, shielded process wings',
 13:'stellar manufacturing works, dark pearl industrial base, four integrated reactor petals, enclosed process core'
}

TIER={
 0:'starter, one storey, compact footprint, one primary production chamber, simple roofline',
 1:'reinforced, same identity, thicker shell, one attached utility room, clearer production bay',
 2:'expanded, wider main hall, second attached production module, denser integrated conduits',
 3:'automated, larger factory, enclosed automation volume, two attached process modules, modest vertical rise',
 4:'advanced, broader connected factory, symmetric attached wings, denser enclosed machinery',
 5:'late-game, very large connected production complex, multiple enclosed process halls, stronger vertical core',
 6:'ultimate, largest connected industrial footprint, tall enclosed production core, compact luminous roof crown'
}

STYLE=('premium AAA mobile strategy asset; stylized 2.5D industrial factory; 34-degree orthographic three-quarter view; '
       'graphite steel alloys; upper-left key light; cool fill; restrained amber and cyan emissive accents')


def prompts(i):
    family=FAMILY[i['family']]
    tier=TIER[i['tier']]
    # CLIP gets only the highest-value concepts so nothing critical falls beyond its short context window.
    short=f'Industrial factory sprite. {family}. {tier}. Isolated on uniform gray studio background.'
    # T5 receives the complete positive design specification.
    detail=(f'{STYLE}. Exactly one finished operating industrial production building. '
            f'Design identity: {family}. Evolution state: {tier}. '
            'Keep the same facade axis, roof direction, production core, material palette and attached-module logic across upgrades. '
            'All visible equipment is enclosed, wall-mounted, roof-mounted, or structurally integrated into the factory. '
            'Use compact mechanically plausible massing with a bottom-heavy mobile-readable silhouette. '
            'End the building cleanly at its structural footprint with neutral gray studio background visible around the entire silhouette.')
    return short,detail

v14.prompts=prompts
v15.prompts=prompts

# More anchor diversity; only the strongest anchors receive expensive tier evolution.
v15.ANCHORS=6
v15.BRANCHES=2
v15.CONTEXT_RETRIES=4

if __name__=='__main__':
    v15.main()
