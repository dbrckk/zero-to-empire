#!/usr/bin/env python3
"""Building factory v17: family-aware structural tier evolution.

Fixes the clone-ladder failure seen on BLD-12 by making every tier prompt describe
an architectural massing change, not a scale/detail pass. It deliberately reuses
v16.10's strict technical/semantic gates; this module changes generation pressure,
not acceptance criteria.
"""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('v1610', HERE / 'kaggle_building_family_factory_v16_10.py')
v1610 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v1610)
v15 = v1610.v15
v14 = v1610.v14

print('KAGGLE_STARTUP=building-family-flux-v18.1-no-site-frontload', flush=True)

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
    1: 'major first redesign: extend two large fused rectangular process wings far beyond the starter ring and raise a clearly taller central containment housing; outer silhouette must visibly change in width and height, never merely scale the starter',
    2: 'major second redesign: add a second offset containment ring stage plus substantial rear shield blocks and one forward process module; produce a distinctly stepped footprint, not another circular enlargement',
    3: 'major vertical redesign: raise a tall central reality-core tower through the ring, add two low fused machinery blocks and break the pure circular silhouette; unmistakable height and footprint change from T2',
    4: 'add a second elevated containment stage and four connected shield/process blocks, creating a stepped multi-level silhouette',
    5: 'megastructure form: dominant elevated exotic-physics core, enlarged twin process wings, secondary ring architecture and dense fused energy-routing masses',
    6: 'apex reality engine: multi-level central core with distinct crown, nested containment architecture and large integrated side systems; unmistakably evolved from T5',
}

REALITY_STRENGTH = {1:.56, 2:.64, 3:.72, 4:.75, 5:.79, 6:.80}


FAMILY_TIER = {
    4: {
        0:'compact single-storey R&D headquarters with one central data core and two short fused lab wings',
        1:'add one visibly larger fused laboratory wing and reinforce the central data core; wider silhouette, same headquarters identity',
        2:'add the opposite fused lab wing plus an enclosed utility/data annex; broaden footprint without creating a campus',
        3:'raise a taller central automation/data-core block above the low lab wings; clear height change and stronger central landmark',
        4:'add a second-storey research block bridging the fused lab wings; denser service modules remain attached to one building',
        5:'evolve into a multi-level advanced R&D headquarters with a dominant central tower, larger symmetric lab wings and integrated energy-routing machinery',
        6:'apex tech headquarters: prestige data-core crown, multi-level fused research wings and maximum integrated machinery, one iconic connected building',
    },
    5: {
        0:'compact connected urban-production block with two low tower masses around one enclosed transit core',
        1:'add one taller fused tower mass and a connected industrial podium section; retain one urban megablock',
        2:'add a second unequal tower and an enclosed cross-block transit spine; clearly denser skyline silhouette',
        3:'raise the central transit/production tower and fuse two lower civic-industrial masses into a stepped urban block',
        4:'district-scale vertical expansion with three integrated tower heights, stacked production decks and one enclosed transit hub',
        5:'late-game megacity block with dominant central skyscraper, multiple fused secondary towers and dense integrated logistics/energy layers',
        6:'apex urban-production megastructure with monumental central tower crown, multi-level fused city-block masses and maximum vertical skyline complexity',
    },
    6: {
        0:'small pressurized lunar outpost with one sealed habitat dome fused to one rectangular utility block',
        1:'add a second connected habitat module and short sealed service tunnel; preserve low lunar-colony silhouette',
        2:'add a larger utility/processing block and another sealed dome on the opposite side; wider connected colony footprint',
        3:'raise a taller central life-support/command module above the connected domes and utility blocks',
        4:'advanced lunar colony with multiple fused habitat domes, two-storey command core and dense enclosed service connections',
        5:'large lunar industrial colony with dominant command/life-support tower, expanded fused habitat clusters and integrated processing wings',
        6:'apex lunar colony with maximum vertical command core, multiple connected domes and monumental enclosed industrial infrastructure; one sealed connected complex',
    },
    7: {
        0:'compact Martian palace-factory with low central command mass and two short fused production wings',
        1:'extend one large enclosed red-alloy production wing and reinforce the central command mass',
        2:'add the opposite fused production wing plus a taller enclosed industrial block; broader palace-factory silhouette',
        3:'raise a distinct central command spire while keeping the paired production wings low and fused',
        4:'monumental Martian complex with enlarged command keep, multi-level fused factory wings and integrated enclosed machinery',
        5:'late-game red-alloy palace-factory with dominant command spire, massive fused industrial wings and dense prestige machinery',
        6:'apex Mars Empire complex with monumental command crown, maximum connected palace-factory massing and iconic red-alloy silhouette',
    },
    8: {
        0:'compact stellar-energy hub with one central power core and two short enclosed collector arms',
        1:'add a larger fused collector arc and one connected routing hub; visibly wider energy structure',
        2:'add the opposite enclosed collector arc to form a partial ring around the persistent central hub',
        3:'raise a taller central power-transfer core through the partial ring and add lower fused routing masses',
        4:'advanced Dyson network node with multiple enclosed ring segments, elevated central hub and dense connected transfer structures',
        5:'large stellar-energy megastructure with dominant central power tower, broad fused collector-ring segments and multiple integrated routing hubs',
        6:'apex Dyson network node with monumental central energy core, maximum connected collector architecture and iconic multi-level ring silhouette',
    },
    9: {
        0:'compact galactic exchange station with one central trade core and two short fused logistics wings',
        1:'extend one enclosed docking/logistics wing and reinforce the central exchange hall',
        2:'add the opposite fused logistics wing plus a larger connected cargo-routing block; broader station footprint',
        3:'raise a taller central exchange tower above the low logistics wings; clear vertical landmark',
        4:'advanced exchange hub with multi-level central station, enlarged fused docking wings and dense enclosed cargo-routing structures',
        5:'late-game interstellar trade hub with dominant exchange tower, massive connected logistics wings and premium integrated finance/transport systems',
        6:'apex galactic exchange with monumental central crown, maximum fused docking/logistics architecture and iconic connected station silhouette',
    },
    10: {
        0:'compact intergalactic gateway with one dominant enclosed portal frame fused to a low service block',
        1:'thicken the same portal frame and add one large fused service wing; gateway remains the dominant feature',
        2:'add the opposite fused service wing plus integrated energy-routing housings around the persistent portal frame',
        3:'raise a taller portal crown and central energy spine while preserving the same gateway opening and connected service mass',
        4:'advanced transit gateway with monumental portal frame, multi-level fused service complex and dense integrated routing machinery',
        5:'late-game gateway megastructure with dominant enlarged portal architecture, massive connected service wings and premium energy-routing systems',
        6:'apex intergalactic gateway with iconic monumental portal crown, maximum fused support architecture and unmistakable persistent gateway identity',
    },
}

def tier_instruction(family,tier):
    if family == 12:
        return REALITY_TIER[tier]
    if family == 13:
        return TRANSCENDENT_TIER[tier]
    return FAMILY_TIER.get(family, TIER)[tier]

REJECTION_LEDGER = HERE.parents[1] / 'art' / 'production' / 'generation-rejection-ledger.json'

TRANSCENDENT_TIER = {
    0: 'compact transcendent core with four short integrated radial systems and a low prestige crown; small readable starter silhouette',
    1: 'first redesign: add two large fused side pylons and a taller crown so width and height both change; avoid a pure circular starburst',
    2: 'second redesign: elongated cross-axis nexus with offset attached systems and a clearly taller central energy spine; not a scaled ring',
    3: 'vertical evolution: tall central transcendent tower with four lower fused buttress blocks and one secondary enclosed energy stage',
    4: 'advanced redesign: multi-level nexus with a dominant vertical core, broad connected side masses and an elevated crown; break radial symmetry enough to create a stepped silhouette',
    5: 'continue the T4 vertical architecture: substantially taller central transcendent core, larger fused lateral energy citadels and denser multi-level crown; preserve the vertical stepped massing, never revert to a flat radial disc',
    6: 'continue T5 into the final vertical apex: maximum-height transcendent core, monumental fused side citadels, multi-level prestige crown and integrated energy routing; remain recognizably descended from T4/T5, never revert to a circular disc',
}

def rejection_hints(i):
    if not REJECTION_LEDGER.is_file():
        return ''
    hints=[]
    try:
        data=json.loads(REJECTION_LEDGER.read_text(encoding='utf-8'))
        aid=str(i['id']).upper()
        for row in data.get('entries',[]):
            prefix=str(row.get('target_prefix','')).upper()
            hint=str(row.get('prompt_hint','')).strip()
            if prefix and aid.startswith(prefix) and hint and hint not in hints:
                hints.append(hint)
    except Exception as e:
        print('KAGGLE_BLD_REJECTION_MEMORY_SKIP='+str(e), flush=True)
    merged=' '.join(hints[-2:])
    return ' '.join(merged.split()[:30])


CLIP_FAMILY = {
    0:'street production kiosk',1:'corner production shop',2:'fabrication workshop',
    3:'industrial factory',4:'tech headquarters',5:'urban production megablock',
    6:'lunar industrial colony',7:'Martian palace-factory',8:'stellar energy complex',
    9:'galactic exchange hub',10:'intergalactic gateway',11:'cosmic foundry',
    12:'reality engine',13:'transcendent energy nexus',
}

def prompts(i):
    family = i['family']
    tier = i['tier']
    fam = v1610.FAMILY[family]
    instruction = tier_instruction(family,tier)
    memory = rejection_hints(i)

    short = (
        f"isolated stylized 2.5D {CLIP_FAMILY[family]}, tier {tier}. {instruction}. "
        "building only, one connected mass, no site, no trees, no paths, no outdoor props, orthographic, neutral gray"
    )
    if len(short.split()) > 58:
        raise RuntimeError(f'building CLIP prompt too long: {len(short.split())} words for {i["id"]}')

    detail = (
        f"AAA stylized 2.5D strategy building. Family: {fam}. Tier: {instruction}. "
        f"{memory} Building only: one connected architectural mass on flat neutral gray. "
        "No site, trees, paths, pavement, yard, platform, ground shadow, text, people, vehicles, props or scenery. "
        "Preserve family materials, camera, facade axis and core identity."
    )
    return short, detail



ORIGINAL_RENDER = v14.render

def family_aware_render(i, prev, pe, ppe, base, img, seed):
    """Give BLD-12 enough img2img freedom to produce real structural evolution."""
    tier = int(i['tier'])
    family=int(i['family'])
    if family not in {12,13}:
        return ORIGINAL_RENDER(i, prev, pe, ppe, base, img, seed)

    # High-risk radial families need periodic text-to-image resets. This keeps
    # family materials/camera while breaking the tendency to only enlarge a ring.
    reset_tiers={12:{1,3},13:{1,3}}
    if tier in reset_tiers[family]:
        print(f"KAGGLE_BLD_ANCHOR_RESET={i['id']} family={family}", flush=True)
        return ORIGINAL_RENDER(i, None, pe, ppe, base, img, seed + 17000 + family*211 + tier*101)

    if prev is None or tier not in REALITY_STRENGTH:
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
    if len(recs)>=7:
        adj=[v1610.normalized_silhouette_iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
        anchor=[v1610.normalized_silhouette_iou(recs[0][1],recs[n][1]) for n in range(1,len(recs))]
        print('KAGGLE_GENERIC_EVOLUTION_SIGNATURE='+
              ';'.join(f'T{n+1}:adj={adj[n]:.3f},anchor={anchor[n]:.3f}' for n in range(len(adj))),
              flush=True)

        # Generic guard against the common failure where apparent progression is
        # mostly canvas occupancy/scale while the normalized silhouette stays the same.
        generic_failures=[]
        if anchor[1]>.930 and sum(x<.900 for x in adj[:4])<2:
            generic_failures.append(f'early-scale-ladder:T2-anchor={anchor[1]:.3f}')
        if adj[0]>.975 and adj[1]>.940:
            generic_failures.append(f'near-clone-opening:T1={adj[0]:.3f},T2={adj[1]:.3f}')
        if generic_failures:
            return -999.0, why+' generic-scale-gate=' + ','.join(generic_failures)

        if family==12:
            failures=[]
            if adj[0]>.965:
                failures.append(f'T1-adj={adj[0]:.3f}>.965')
            if anchor[2]>.930:
                failures.append(f'T3-anchor={anchor[2]:.3f}>.930')
            if anchor[4]>.860:
                failures.append(f'T5-anchor={anchor[4]:.3f}>.860')
            if anchor[5]>.845:
                failures.append(f'T6-anchor={anchor[5]:.3f}>.845')
            if sum(x<.920 for x in adj)<4:
                failures.append('fewer-than-4-structural-transitions')
            if sum(x<.900 for x in adj[:3])<2:
                failures.append('weak-early-tier-evolution')
            if failures:
                return -999.0, why+' clone-ladder=' + ','.join(failures)

        if family==13:
            failures=[]
            if anchor[1]>.900:
                failures.append(f'T2-anchor={anchor[1]:.3f}>.900')
            if sum(x<.880 for x in adj[:4])<2:
                failures.append('insufficient-transcendent-early-redesign')
            aspects=[]
            for _,im,_ in recs:
                bb=im.getchannel('A').getbbox()
                aspects.append(((bb[3]-bb[1])/(bb[2]-bb[0])) if bb and bb[2]>bb[0] else 0.0)
            print('KAGGLE_BLD13_ASPECT='+';'.join(f'T{n}:{x:.3f}' for n,x in enumerate(aspects)),flush=True)
            if aspects[4]>=.95 and aspects[5]<.90:
                failures.append(f'T5-vertical-collapse={aspects[4]:.3f}->{aspects[5]:.3f}')
            if abs(aspects[5]-aspects[4])>.28:
                failures.append(f'T4-T5-aspect-jump={aspects[4]:.3f}->{aspects[5]:.3f}')
            if failures:
                return -999.0, why+' transcendent-ladder=' + ','.join(failures)
    return score,why


v14.prompts = prompts
v15.prompts = prompts
v14.render = family_aware_render
v15.branch_score = branch_score

if __name__ == '__main__':
    v15.main()
