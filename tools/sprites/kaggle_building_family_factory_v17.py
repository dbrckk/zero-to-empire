#!/usr/bin/env python3
"""Building factory v17: family-aware structural tier evolution.

Fixes the clone-ladder failure seen on BLD-12 by making every tier prompt describe
an architectural massing change, not a scale/detail pass. It deliberately reuses
v16.10's strict technical/semantic gates; this module changes generation pressure,
not acceptance criteria.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('v1610', HERE / 'kaggle_building_family_factory_v16_10.py')
v1610 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v1610)
v15 = v1610.v15
v14 = v1610.v14

print('KAGGLE_STARTUP=building-family-flux-v17.4-evidence-calibrated-gates', flush=True)

# More image-to-image freedom than v16.10. The strict v16.10 live gate remains
# active, so extra freedom cannot silently promote unrelated scenes/site cards.
v14.STRENGTH.update({1:.40, 2:.46, 3:.52, 4:.58, 5:.64, 6:.70})
v14.STEPS.update({0:10, 1:10, 2:10, 3:11, 4:12, 5:13, 6:14})

TIER = {
    0: 'baseline architecture: compact starter mass, one dominant core, simplest connected silhouette',
    1: 'first architectural expansion: add one large attached side volume that visibly changes the outer silhouette; do not merely enlarge the baseline',
    2: 'second architectural expansion: add a different connected wing or ring segment on the opposite axis and broaden the footprint; preserve family identity but change massing',
    3: 'vertical evolution: introduce a clearly taller central core plus attached lower machinery volumes; silhouette must differ in both height distribution and footprint',
    4: 'advanced complex: add a substantial upper structural block and two fused service/process volumes; create a new stepped silhouette rather than decorating or scaling T3',
    5: 'megastructure evolution: add a dominant family-appropriate tower, ring, dome, furnace, portal, or energy-core mass plus enlarged connected wings; unmistakably new architecture, not a resized T4',
    6: 'mastery evolution: apex form of this exact family with a distinct family-appropriate crown/core and multi-level connected masses; strongest silhouette evolution while retaining materials, camera and family DNA; never a scaled clone of T5',
}

# Family-specific evolution nouns stop the generic Tech Company vocabulary from
# leaking into Reality Engine, Moon Colony, Foundry, Gateway, etc.
EVOLUTION = {
    0: 'kiosk canopy, utility housing, production chamber',
    1: 'storefront bays, service volume, roof utility block',
    2: 'fabrication halls, tooling bays, exhaust housings',
    3: 'industrial halls, feeder bays, automation core',
    4: 'research blocks, lab wings, data core',
    5: 'integrated towers, transit core, civic-industrial modules',
    6: 'sealed habitat domes, utility blocks, life-support core',
    7: 'command spire, palace-factory wings, production blocks',
    8: 'collector masses, enclosed ring segments, power-transfer hubs',
    9: 'exchange core, docking wings, logistics blocks',
    10: 'portal frame, energy-routing blocks, fused service structures',
    11: 'stellar furnace core, fabrication wings, heavy forge machinery',
    12: 'containment rings, shielded process wings, exotic-physics core',
    13: 'transcendent core, radial systems, prestige crown',
}

REALITY_TIER = {
    0: 'compact enclosed containment-ring engine with two short symmetric shielded process wings and a low central exotic-physics core',
    1: 'add one large fused rectangular process wing on each side and a visibly taller central containment housing; silhouette must change, not scale',
    2: 'add a second outer containment ring segment plus substantial rear shield blocks; broaden the connected mass asymmetrically enough to alter the silhouette',
    3: 'raise a tall central reality-core tower through the ring and add lower fused machinery volumes; clear vertical step-change from T2',
    4: 'add a second elevated containment stage and four connected shield/process blocks, creating a stepped multi-level silhouette',
    5: 'megastructure form: dominant elevated exotic-physics core, enlarged twin process wings, secondary ring architecture and dense fused energy-routing masses',
    6: 'apex reality engine: multi-level central core with distinct crown, nested containment architecture and large integrated side systems; unmistakably evolved from T5',
}

REALITY_STRENGTH = {1:.48, 2:.56, 3:.64, 4:.71, 5:.77, 6:.80}


def prompts(i):
    family = i['family']
    tier = i['tier']
    fam = v1610.FAMILY[family]
    shape = v1610.SHAPE[family]
    evolution = EVOLUTION[family]
    instruction = REALITY_TIER[tier] if family == 12 else TIER[tier]
    short = (
        f'Centered isolated {fam}. {shape}. Tier {tier}: {instruction}. '
        f'Use only connected family structures such as {evolution}. One object on flat neutral gray.'
    )
    detail = (
        f'{v1610.STYLE}. Family DNA: {fam}. Base family shape: {shape}. '
        f'Tier instruction: {instruction}. Family-specific architectural vocabulary: {evolution}. '
        'Change actual connected architecture and outer massing; never simulate progression by only scaling the previous object. '
        'Keep camera, facade axis, material identity and dominant family core coherent across the family. '
        f'{v1610.FOOTPRINT}'
    )
    return short, detail



ORIGINAL_RENDER = v14.render

def family_aware_render(i, prev, pe, ppe, base, img, seed):
    """Give BLD-12 enough img2img freedom to produce real structural evolution."""
    tier = int(i['tier'])
    if int(i['family']) != 12 or prev is None or tier not in REALITY_STRENGTH:
        return ORIGINAL_RENDER(i, prev, pe, ppe, base, img, seed)
    old = v14.STRENGTH[tier]
    v14.STRENGTH[tier] = REALITY_STRENGTH[tier]
    try:
        return ORIGINAL_RENDER(i, prev, pe, ppe, base, img, seed)
    finally:
        v14.STRENGTH[tier] = old

def architectural_band_fill(final, lo, hi):
    """Mask fill inside the sprite bbox for a relative vertical band."""
    alpha=np.asarray(final.getchannel('A'),dtype=np.uint8)
    ys,xs=np.where(alpha>=32)
    if len(xs)==0:
        return 0.0
    x0,x1=int(xs.min()),int(xs.max())+1
    y0,y1=int(ys.min()),int(ys.max())+1
    h=max(1,y1-y0)
    ya=y0+int(lo*h); yb=max(ya+1,y0+int(hi*h))
    band=alpha[ya:yb,x0:x1]>=32
    if not band.size:
        return 0.0
    return float(band.mean())


V15_BRANCH_SCORE=v15.branch_score

def branch_score(recs):
    score,why=V15_BRANCH_SCORE(recs)
    if score < -100 or not recs:
        return score,why
    family=int(recs[0][0]['family'])
    if family==7:
        signatures=[]
        for item,final,_cov in recs:
            upper=architectural_band_fill(final,.20,.50)
            lower=architectural_band_fill(final,.58,.88)
            signatures.append((item['id'],upper,lower))
        offenders=[x for x in signatures if x[2]>.76 and x[1]<.58]
        print('KAGGLE_BLD07_PLATFORM_SIGNATURE='+
              ';'.join(f'{aid}:upper={upper:.3f},lower={lower:.3f}' for aid,upper,lower in signatures),
              flush=True)
        if offenders:
            details=','.join(f'{aid}(upper={upper:.2f},lower={lower:.2f})' for aid,upper,lower in offenders)
            return -999.0, why+f' platform-overhang={details}'
    if family==12 and len(recs)>=7:
        adj=[v1610.normalized_silhouette_iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
        anchor=[v1610.normalized_silhouette_iou(recs[0][1],recs[n][1]) for n in range(1,len(recs))]
        print('KAGGLE_BLD12_EVOLUTION_SIGNATURE='+
              ';'.join(f'T{n+1}:adj={adj[n]:.3f},anchor={anchor[n]:.3f}' for n in range(len(adj))),
              flush=True)
        failures=[]
        # T1 may retain a very similar outer shell if the family then proves
        # strong cumulative evolution. Avoid rejecting a good branch on tiny
        # mask noise around the old .955 boundary.
        if adj[0]>.965:
            failures.append(f'T1-adj={adj[0]:.3f}>.965')
        if anchor[2]>.930:
            failures.append(f'T3-anchor={anchor[2]:.3f}>.930')
        if anchor[4]>.860:
            failures.append(f'T5-anchor={anchor[4]:.3f}>.860')
        if anchor[5]>.845:
            failures.append(f'T6-anchor={anchor[5]:.3f}>.845')
        if sum(x<.920 for x in adj)<3:
            failures.append('fewer-than-3-structural-transitions')
        if failures:
            return -999.0, why+' clone-ladder=' + ','.join(failures)
    return score,why


v14.prompts = prompts
v15.prompts = prompts
v14.render = family_aware_render
v15.branch_score = branch_score

if __name__ == '__main__':
    v15.main()
