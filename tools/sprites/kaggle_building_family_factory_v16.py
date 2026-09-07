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

print('KAGGLE_STARTUP=building-family-flux-v16.1-shape-first-source-locked',flush=True)

# Preserve an approved family anchor instead of reinventing the scene at every tier.
v14.STRENGTH.update({1:.22,2:.27,3:.32,4:.37,5:.42,6:.47})
v14.STEPS.update({0:8,1:6,2:6,3:7,4:7,5:8,6:8})

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

SHAPE={
 0:'low rectangular kiosk mass, one short roof cap',
 1:'low chamfered workshop block, broad front face',
 2:'broad low hall, twin compact roof stacks',
 3:'long horizontal hall, symmetric side volumes',
 4:'low wide CNC block, flat ribbed roof',
 5:'compact square block, protected central core',
 6:'low horizontal plant, compact exchanger masses',
 7:'very wide low factory, paired side wings',
 8:'heavy low armored block, broad enclosed press bay',
 9:'clean low block, symmetric wings around central ring',
 10:'broad base, enclosed circular center, attached radial rooms',
 11:'wide press-house block, contained internal frame volumes',
 12:'broad shielded block, enclosed central ring, symmetric wings',
 13:'broad industrial base, four compact integrated roof petals'
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
    shape=SHAPE[i['family']]
    tier=TIER[i['tier']]
    if i['tier']==0:
        # Phase 1: lock massing and family identity before introducing richer machinery detail.
        short=f'Industrial factory sprite. {shape}. Starter one-storey factory. Uniform gray studio background.'
        detail=(f'{STYLE}. Create one finished operating starter factory with this architectural massing: {shape}. '
                f'Family identity: {family}. Keep the silhouette low, broad, bottom-heavy and compact. '
                'Use one connected structural footprint and simple integrated roof equipment. '
                'Neutral gray studio background remains clearly visible around the complete silhouette.')
    else:
        # Phase 2: evolve the approved shape conservatively and add only integrated industrial detail.
        short=f'Industrial factory upgrade. {shape}. {tier}. Same factory identity. Gray studio background.'
        detail=(f'{STYLE}. Upgrade the same approved factory in place. Design identity: {family}. Evolution state: {tier}. '
                f'Preserve this source massing: {shape}. Keep the same facade axis, roof direction, production core and material palette. '
                'Add only attached architectural volumes and structurally integrated production equipment. '
                'Maintain a compact mechanically plausible bottom-heavy silhouette and one connected structural footprint. '
                'Neutral gray studio background remains visible around the entire building.')
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
    base=v15.anchor_score(final,cov)
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
