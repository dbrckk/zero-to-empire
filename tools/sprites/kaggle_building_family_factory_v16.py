#!/usr/bin/env python3
"""Building factory v16.4: footprint-locked two-phase family evolution.

Wave85 proved that prose-only anti-ground instructions are insufficient. v16.4
changes the source dynamics: very conservative tier evolution, a hard lower-mass
footprint prior, and tier-specific growth that adds attached mass without asking
FLUX for a surrounding site. Live QA remains strict; this version does not weaken
slab acceptance to manufacture yield.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('v15',HERE/'kaggle_building_family_factory_v15.py')
v15=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(v15)
v14=v15.v14
V15_ANCHOR_SCORE=v15.anchor_score

print('KAGGLE_STARTUP=building-family-flux-v16.4-footprint-locked-two-phase',flush=True)

# Phase A (T0-T3): preserve massing. Phase B (T4-T6): add detail/attached volumes
# without the high denoise that caused wave85 to invent a new ground/site plane.
v14.STRENGTH.update({1:.16,2:.19,3:.22,4:.24,5:.26,6:.28})
v14.STEPS.update({0:10,1:7,2:7,3:8,4:8,5:9,6:10})
v14.RETRIES.update({0:5,1:3,2:3,3:3,4:3,5:3,6:3})

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
 0:'low rectangular kiosk mass',1:'low chamfered workshop block',2:'broad low hall with twin compact roof housings',
 3:'long horizontal hall with symmetric side volumes',4:'low wide CNC block with flat ribbed roof',
 5:'compact square block with protected central core',6:'low horizontal plant with attached exchanger masses',
 7:'very wide low factory with paired attached side wings',8:'heavy low armored block with broad enclosed press bay',
 9:'clean low block with symmetric attached wings around central ring',10:'broad block with enclosed circular center and attached radial rooms',
 11:'wide press-house block with contained internal frame volumes',12:'broad shielded block with enclosed central ring and symmetric attached wings',
 13:'broad industrial block with four compact attached roof housings'
}
TIER={
 0:'starter shell; one storey; one production chamber',
 1:'massing phase; reinforce the same walls and add one small attached utility volume',
 2:'massing phase; widen only the occupied building shell and add one attached production volume',
 3:'massing phase; extend the connected hall and add an enclosed automation volume',
 4:'detail phase; keep the established footprint silhouette and enrich attached machinery and wall articulation',
 5:'detail phase; keep the established footprint silhouette and add enclosed process density plus a modest central rise',
 6:'detail phase; preserve the established footprint and add a compact enclosed roof core plus integrated high-tier machinery'
}
STYLE=('premium AAA mobile strategy industrial asset, stylized 2.5D, 34-degree orthographic three-quarter camera, '
       'graphite steel alloys, upper-left key light, cool fill, restrained amber/cyan emissive accents, neutral gray studio sweep')

# Positive spatial formulation: describe what fills the lower silhouette instead of
# repeatedly naming a floor/site. The model should see one product-like object.
FOOTPRINT=(
 'The lowest visible silhouette is the building wall base itself: a compact solid rectangular or chamfered structural plinth contained directly beneath the walls. '
 'Its outer edge is flush with the exterior walls and never extends laterally beyond them. '
 'Outside that wall base, the image is uninterrupted neutral gray studio background. '
 'Every tank, pipe, vent, bay and service module is fused to the main architectural mass. '
 'Show exactly one self-contained factory object, centered with generous gray clearance on all sides. '
 'No people, vehicles, loose equipment, emitted effects, signage, scenery or secondary objects.'
)

def prompts(i):
    fam=FAMILY[i['family']]; shape=SHAPE[i['family']]; tier=TIER[i['tier']]
    short=f'Centered isolated industrial factory product asset. {shape}. {tier}. One solid connected object on neutral gray studio.'
    if i['tier']<=3:
        phase='Build only the primary architectural massing. Prefer large contiguous wall/roof shapes over small decorative pieces.'
    else:
        phase='Preserve the approved massing and silhouette. Add detail inside or directly onto existing walls/roof; do not redesign the object footprint.'
    detail=(f'{STYLE}. Family DNA: {fam}. Tier instruction: {tier}. {phase} '
            f'Keep the same facade axis, roof direction, production core and material identity. {FOOTPRINT}')
    return short,detail

def silhouette_metrics(final):
    m=v14.mask64(final); b=m.getbbox()
    if not b:return {'aspect':0.,'upper':1.,'lower':0.,'top_spike':1.,'base_fill':0.}
    x0,y0,x1,y1=b; w=max(1,x1-x0);h=max(1,y1-y0);px=m.load();total=upper=lower=top=0
    split=y0+int(h*.48);top_end=y0+max(1,int(h*.22));base0=y0+int(h*.72);base_rows=[]
    for y in range(y0,y1):
        row=0
        for x in range(x0,x1):
            if px[x,y]<=0:continue
            row+=1;total+=1
            if y<split:upper+=1
            else:lower+=1
            if y<top_end:top+=1
        if y>=base0:base_rows.append(row/w)
    return {'aspect':w/h,'upper':upper/max(total,1),'lower':lower/max(total,1),'top_spike':top/max(total,1),
            'base_fill':sum(base_rows)/max(len(base_rows),1)}

def v164_anchor_score(final,cov):
    base=V15_ANCHOR_SCORE(final,cov);s=silhouette_metrics(final);pen=0.
    if s['aspect']<.88:pen+=(.88-s['aspect'])*1.8
    if s['upper']>.48:pen+=(s['upper']-.48)*2.8
    if s['top_spike']>.12:pen+=(s['top_spike']-.12)*3.2
    if s['lower']<.52:pen+=(.52-s['lower'])*2.2
    # Prefer a substantial building base, but not a nearly full-width thin card.
    if s['base_fill']<.38:pen+=(.38-s['base_fill'])*1.2
    score=base-pen
    print(f"KAGGLE_V164_SHAPE aspect={s['aspect']:.2f} upper={s['upper']:.2f} lower={s['lower']:.2f} top={s['top_spike']:.2f} basefill={s['base_fill']:.2f} score={score:.3f}",flush=True)
    return score

# Preserve strict slab gate. Add a tier-dependent adjacent-identity floor so late
# tiers cannot replace the source with a fresh scene even if coverage grows.
V15_LIVE_GATE=v15.live_gate
def v164_live_gate(recs,new_final,new_cov,tier):
    ok,reasons=V15_LIVE_GATE(recs,new_final,new_cov,tier)
    if recs:
        ident=v14.iou(recs[-1][1],new_final)
        floor={1:.48,2:.45,3:.42,4:.40,5:.38,6:.36}[tier]
        if ident<floor and not any(r.startswith('adj-iou=') for r in reasons):reasons.append(f'footprint-iou={ident:.2f}<{floor:.2f}')
    return (not reasons),reasons

v14.prompts=prompts;v15.prompts=prompts
v15.anchor_score=v164_anchor_score
v15.live_gate=v164_live_gate
v15.ANCHORS=6;v15.BRANCHES=2;v15.CONTEXT_RETRIES=4

if __name__=='__main__':v15.main()
