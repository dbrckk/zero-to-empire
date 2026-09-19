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
import numpy as np

HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('v15',HERE/'kaggle_building_family_factory_v15.py')
v15=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(v15)
v14=v15.v14
V15_ANCHOR_SCORE=v15.anchor_score

print('KAGGLE_STARTUP=building-family-flux-v16.6-structural-tier-evolution',flush=True)

# Phase A (T0-T3): preserve massing. Phase B (T4-T6): add detail/attached volumes
# without the high denoise that caused wave85 to invent a new ground/site plane.
v14.STRENGTH.update({1:.23,2:.28,3:.33,4:.38,5:.43,6:.48})
v14.STEPS.update({0:10,1:8,2:8,3:9,4:10,5:11,6:12})
v14.RETRIES.update({0:5,1:3,2:3,3:3,4:3,5:3,6:3})

FAMILY={
 0:'Street Stand, compact improvised street-production kiosk, rust steel panels, one warm production core, simple canopy and utility housing',
 1:'Corner Shop, neighborhood retail-production storefront, chamfered graphite facade, enclosed service bay, compact rear utility volume',
 2:'Workshop, mechanical fabrication workshop, broad low steel shell, visible enclosed tooling bay, short exhaust housing and reinforced doors',
 3:'Factory, industrial production plant, long dark hall, enclosed automation spine, attached loading/feeder bays and integrated machinery',
 4:'Tech Company, futuristic R&D headquarters and production campus, graphite glass-and-alloy shell, central data core, attached lab wings, restrained cyan systems',
 5:'Megacity, dense futuristic urban-production district represented as one connected megastructure block, stacked towers, transit core, civic-industrial modules',
 6:'Moon Colony, pressurized lunar industrial colony, connected habitat domes and utility blocks, sealed service tunnels, ice-white alloy shell with cyan life-support accents',
 7:'Mars Empire, monumental Martian industrial-government complex, connected red-alloy palace-factory mass, central command spire, enclosed production wings',
 8:'Dyson Network, stellar-energy collection and routing complex, connected energy-harvesting megastructure, enclosed ring segments and power-transfer hubs',
 9:'Galactic Exchange, interstellar trade and finance hub, connected premium station-complex, central exchange core, docking/logistics wings, cyan-violet accents',
 10:'Intergalactic Gateway, deep-space transit gateway complex, massive enclosed portal architecture fused to service structures and energy routing',
 11:'Cosmic Foundry, cosmic-scale fabrication facility, dark alloy megaforge, enclosed stellar furnace core, attached fabrication wings and heavy machinery',
 12:'Reality Engine, exotic-physics reality-processing machine complex, pearl alloy structure, enclosed luminous containment rings, symmetric shielded process wings',
 13:'Transcendent Nexus, apex civilization energy nexus, dark pearl-and-gold connected megastructure, central transcendent core, radial attached systems and prestige crown'
}
SHAPE={
 0:'small low kiosk mass with one canopy and compact rear utility box',
 1:'low storefront block with clear front facade and one attached service volume',
 2:'broad low workshop hall with one enclosed tooling bay and short roof housing',
 3:'long industrial hall with central production spine and attached loading bays',
 4:'wide low-to-midrise tech headquarters with central data core and symmetric lab wings',
 5:'dense connected urban megablock with several integrated vertical tower masses around one transit core',
 6:'connected lunar colony cluster with sealed domes and rectangular habitat/utility masses on one structural base',
 7:'broad monumental red-alloy complex with central command mass and paired enclosed production wings',
 8:'connected stellar-energy megastructure with central power hub and enclosed ring/collector masses',
 9:'premium connected exchange hub with central station block and symmetric logistics/docking wings',
 10:'massive gateway frame fused into a broad service complex, one dominant portal opening inside one connected mass',
 11:'heavy cosmic foundry block with central furnace core and large attached fabrication wings',
 12:'broad shielded reality-engine structure with enclosed central containment ring and symmetric process wings',
 13:'radial apex nexus with central core, integrated attached systems and a compact prestige crown'
}
TIER={
 0:'starter shell; one storey; one production chamber; compact baseline silhouette',
 1:'structural evolution: preserve the core shell but add one clearly visible attached utility wing and reinforced entrance volume',
 2:'structural evolution: add a second attached lab/production wing and broaden the connected footprint; silhouette must visibly differ from T1',
 3:'structural evolution: add a taller central automation/data-core volume plus enclosed side machinery; increase verticality as well as footprint',
 4:'district-scale evolution: add a second-storey research block and dense attached service modules while preserving the same facade axis and family DNA',
 5:'megastructure evolution: add a substantial central tower/core, larger symmetric lab wings and premium enclosed energy-routing machinery; unmistakably larger and richer than T4',
 6:'mastery evolution: apex Tech Company headquarters with a distinct prestige crown/data core, multi-level connected lab wings and maximum integrated machinery; clearly evolved from T5, never merely scaled'
}
STYLE=('premium AAA mobile strategy industrial asset, stylized 2.5D, 34-degree orthographic three-quarter camera, '
       'graphite steel alloys, upper-left key light, cool fill, restrained amber/cyan emissive accents, perfectly flat solid neutral gray background, no gradient, no vignette, no horizon, no shadow card')

# Positive spatial formulation: describe what fills the lower silhouette instead of
# repeatedly naming a floor/site. The model should see one product-like object.
FOOTPRINT=(
 'The lowest visible silhouette is the building wall base itself: a compact solid rectangular or chamfered structural plinth contained directly beneath the walls. '
 'Its outer edge is flush with the exterior walls and never extends laterally beyond them. '
 'Outside that wall base, the image is perfectly uniform neutral gray with constant RGB value to every edge. '
 'Every tank, pipe, vent, bay and service module is fused to the main architectural mass. '
 'Show exactly one self-contained factory object, centered with generous gray clearance on all sides. '
 'No people, vehicles, loose equipment, emitted effects, signage, scenery or secondary objects.'
)

def prompts(i):
    fam=FAMILY[i['family']]; shape=SHAPE[i['family']]; tier=TIER[i['tier']]
    short=f'Centered isolated industrial factory product asset. {shape}. {tier}. One solid connected object on perfectly flat uniform neutral gray background.'
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

def v164_slab_score(alpha):
    """Detect a detached/site-like lower card from silhouette geometry.

    A real factory may legitimately become wider near its base. The forbidden
    pattern is a thin, abrupt lower shelf/card: several consecutive rows that
    jump materially wider than the rows immediately above and stay nearly flat.
    """
    sm=alpha.resize((128,128),v14.Image.Resampling.BILINEAR)
    px=sm.load()
    widths=[]
    for y in range(8,124):
        xs=[x for x in range(4,124) if px[x,y]>=32]
        widths.append((y, (xs[-1]-xs[0]+1)/120 if xs else 0.0))
    score=0.0
    for y,w in widths:
        if y < 82 or w < .76:
            continue
        above=[aw for ay,aw in widths if y-12 <= ay <= y-4 and aw>0]
        if not above:
            continue
        ref=float(np.median(above))
        # Require an abrupt lateral shelf, not merely a broad continuous wall.
        if w > ref*1.28 and (w-ref) > .12:
            score += 1.0
    # Normalize against the lower silhouette depth. A genuine thin card creates
    # a sustained shelf signal; ordinary wall widening should remain near zero.
    lower_rows=max(1,sum(1 for y,w in widths if y>=82 and w>0))
    return score/lower_rows

# Keep the strict no-site-card rule, but measure detached lateral expansion
# rather than treating a legitimate broad building base as a floor slab.
v14.slab_score=v164_slab_score

def normalized_silhouette_iou(a,b):
    """Compare shape after removing pure scale/position differences.
    Near-1.0 means the tier is basically the same silhouette resized.
    """
    ma=a.getchannel('A').point(lambda p:255 if p>=32 else 0)
    mb=b.getchannel('A').point(lambda p:255 if p>=32 else 0)
    ba=ma.getbbox(); bb=mb.getbbox()
    if not ba or not bb:
        return 0.0
    ca=ma.crop(ba).resize((128,128),v14.Image.Resampling.NEAREST)
    cb=mb.crop(bb).resize((128,128),v14.Image.Resampling.NEAREST)
    pa,pb=ca.load(),cb.load(); inter=union=0
    for y in range(128):
        for x in range(128):
            aa=pa[x,y]>0; bval=pb[x,y]>0
            inter += aa and bval
            union += aa or bval
    return inter/max(union,1)

def v164_live_gate(recs,new_final,new_cov,tier):
    ok,reasons=V15_LIVE_GATE(recs,new_final,new_cov,tier)
    if recs:
        ident=v14.iou(recs[-1][1],new_final)
        floor={1:.45,2:.42,3:.39,4:.36,5:.34,6:.32}[tier]
        if ident<floor and not any(r.startswith('adj-iou=') for r in reasons):
            reasons.append(f'footprint-iou={ident:.2f}<{floor:.2f}')
        norm=normalized_silhouette_iou(recs[-1][1],new_final)
        ceiling={1:.965,2:.955,3:.945,4:.935,5:.925,6:.915}[tier]
        if norm>ceiling:
            reasons.append(f'normalized-silhouette-iou={norm:.3f}>{ceiling:.3f}: tier is mostly a resize')
        print(f'KAGGLE_STRUCTURAL_EVOLUTION tier={tier} adj_iou={ident:.3f} normalized_iou={norm:.3f}',flush=True)
    return (not reasons),reasons

v14.prompts=prompts;v15.prompts=prompts
v15.anchor_score=v164_anchor_score
v15.live_gate=v164_live_gate
v15.ANCHORS=6;v15.BRANCHES=2;v15.CONTEXT_RETRIES=4

if __name__=='__main__':v15.main()
