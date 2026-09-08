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
V15_ANCHOR_SCORE=v15.anchor_score

print('KAGGLE_STARTUP=building-family-flux-v16.3-isolated-static-source',flush=True)

# Preserve an approved family anchor instead of reinventing the scene at every tier.
v14.STRENGTH.update({1:.20,2:.25,3:.30,4:.35,5:.40,6:.45})
v14.STEPS.update({0:9,1:7,2:7,3:8,4:8,5:9,6:9})

FAMILY={
 0:'street foundry kiosk, rectangular rust-steel shell, recessed amber furnace mouth, short enclosed roof exhaust housing',
 1:'fabrication shop, chamfered graphite shell, enclosed machining bay, low rear loading recess',
 2:'furnace works, broad low steel hall, twin short sealed heat-stack housings, central glowing furnace chamber',
 3:'assembly hub, long dark production hall, enclosed robotic spine, symmetric attached feeder bays',
 4:'precision CNC factory, low graphite rectangular shell, three recessed CNC bays, ribbed roof',
 5:'energy-cell works, square alloy block, protected amber reactor core, attached capacitor rooms',
 6:'coolant plant, silver graphite hall, integrated cyan coolant pipes, compact attached heat exchangers',
 7:'automation works, wide low tech factory, paired enclosed robot cells, attached production wings',
 8:'heavy forge, armored low production block, central orange forge chamber, enclosed press bay',
 9:'nanofabrication complex, pearl graphite block, sealed cyan process ring, symmetric cleanroom wings',
 10:'orbital component works, dark alloy factory block, enclosed circular assembly chamber, attached radial service rooms',
 11:'actuator works, broad press-house factory, enclosed articulated press frames, reinforced roof shell',
 12:'phase foundry, pearl alloy production block, enclosed luminous containment ring, shielded attached process wings',
 13:'stellar manufacturing works, dark pearl industrial base, four compact attached reactor housings, enclosed process core'
}

SHAPE={
 0:'low rectangular kiosk mass, one short roof cap, foundation exactly under wall footprint',
 1:'low chamfered workshop block, broad front face, foundation exactly under wall footprint',
 2:'broad low hall, twin compact roof housings, foundation exactly under wall footprint',
 3:'long horizontal hall, symmetric side volumes, foundation exactly under wall footprint',
 4:'low wide CNC block, flat ribbed roof, foundation exactly under wall footprint',
 5:'compact square block, protected central core, foundation exactly under wall footprint',
 6:'low horizontal plant, compact attached exchanger masses, foundation exactly under wall footprint',
 7:'very wide low factory, paired attached side wings, foundation exactly under wall footprint',
 8:'heavy low armored block, broad enclosed press bay, foundation exactly under wall footprint',
 9:'clean low block, symmetric attached wings around central ring, foundation exactly under wall footprint',
 10:'broad base, enclosed circular center, attached radial rooms, foundation exactly under wall footprint',
 11:'wide press-house block, contained internal frame volumes, foundation exactly under wall footprint',
 12:'broad shielded block, enclosed central ring, symmetric attached wings, foundation exactly under wall footprint',
 13:'broad industrial base, four compact attached roof housings, foundation exactly under wall footprint'
}

TIER={
 0:'starter, one storey, compact footprint, one primary production chamber, simple roofline',
 1:'reinforced, same identity, thicker shell, one attached utility room, clearer production bay',
 2:'expanded, wider main hall, second attached production module, denser integrated conduits',
 3:'automated, larger factory, enclosed automation volume, two attached process modules, modest vertical rise',
 4:'advanced, broader connected factory, symmetric attached wings, denser enclosed machinery',
 5:'late-game, very large connected production complex, multiple enclosed process halls, stronger vertical core',
 6:'ultimate, largest connected industrial footprint, tall enclosed production core, compact enclosed luminous roof reactor cap'
}

STYLE=('premium AAA mobile strategy asset; stylized 2.5D industrial factory; 34-degree orthographic three-quarter view; '
       'graphite steel alloys; upper-left key light; cool fill; restrained amber and cyan emissive accents; '
       'single static architectural object only; clean studio product render')

STATIC_CONTRACT=(
    'The visible object must end exactly at its structural foundation edge. '
    'Keep neutral gray studio background visible immediately around every side of the foundation. '
    'All pipes, tanks, vents, machinery and service modules must be physically attached to the building. '
    'Render no surrounding pavement, floor tile, site pad, road, terrain patch, cast-shadow card, barrels, crates, tools, vehicles, workers or detached props. '
    'Render no emitted smoke, steam, flame, sparks or particles; those belong to separate runtime FX. '
    'No text, labels, flags, signs or decorative scenery.'
)


def prompts(i):
    family=FAMILY[i['family']]
    shape=SHAPE[i['family']]
    tier=TIER[i['tier']]
    if i['tier']==0:
        short=f'Isolated static industrial factory sprite. {shape}. Starter one-storey factory. Gray studio background.'
        detail=(f'{STYLE}. Create one finished operating starter factory with this architectural massing: {shape}. '
                f'Family identity: {family}. Keep the silhouette low, broad, bottom-heavy and compact. '
                'Use one connected structural footprint and simple integrated roof equipment. '
                f'{STATIC_CONTRACT}')
    else:
        short=f'Isolated static industrial factory upgrade. {shape}. {tier}. Same factory identity. Gray studio background.'
        detail=(f'{STYLE}. Upgrade the same approved factory in place. Design identity: {family}. Evolution state: {tier}. '
                f'Preserve this source massing: {shape}. Keep the same facade axis, roof direction, production core and material palette. '
                'Add only attached architectural volumes and structurally integrated production equipment. '
                'Maintain a compact mechanically plausible bottom-heavy silhouette and one connected structural footprint. '
                f'{STATIC_CONTRACT}')
    return short,detail


def silhouette_metrics(final):
    """Return cheap shape features used before expensive branch evolution."""
    m=v14.mask64(final)
    b=m.getbbox()
    if not b:
        return {'aspect':0.0,'upper':1.0,'lower':0.0,'top_spike':1.0}
    x0,y0,x1,y1=b; w=max(1,x1-x0); h=max(1,y1-y0)
    px=m.load(); total=upper=lower=top=0
    split=y0 + int(h*.48); top_end=y0 + max(1,int(h*.22))
    for y in range(y0,y1):
        for x in range(x0,x1):
            if px[x,y] <= 0: continue
            total += 1
            if y < split: upper += 1
            else: lower += 1
            if y < top_end: top += 1
    return {
        'aspect': w/h,
        'upper': upper/max(total,1),
        'lower': lower/max(total,1),
        'top_spike': top/max(total,1),
    }


def v16_anchor_score(final,cov):
    """Prefer low, bottom-heavy industrial starters before evolving a family."""
    base=V15_ANCHOR_SCORE(final,cov)
    s=silhouette_metrics(final)
    penalty=0.0
    if s['aspect'] < .82: penalty += (.82-s['aspect'])*1.6
    if s['upper'] > .50: penalty += (s['upper']-.50)*2.5
    if s['top_spike'] > .14: penalty += (s['top_spike']-.14)*3.0
    if s['lower'] < .50: penalty += (.50-s['lower'])*2.0
    score=base-penalty
    print(f"KAGGLE_V16_SILHOUETTE aspect={s['aspect']:.2f} upper={s['upper']:.2f} lower={s['lower']:.2f} top={s['top_spike']:.2f} score={score:.3f}",flush=True)
    return score

v14.prompts=prompts
v15.prompts=prompts
v15.anchor_score=v16_anchor_score

# More anchor diversity; only the strongest anchors receive expensive tier evolution.
v15.ANCHORS=6
v15.BRANCHES=2
v15.CONTEXT_RETRIES=4

if __name__=='__main__':
    v15.main()
