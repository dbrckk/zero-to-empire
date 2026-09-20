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

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('v1610', HERE / 'kaggle_building_family_factory_v16_10.py')
v1610 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v1610)
v15 = v1610.v15
v14 = v1610.v14

print('KAGGLE_STARTUP=building-family-flux-v17-family-aware-structural-evolution', flush=True)

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


def prompts(i):
    family = i['family']
    tier = i['tier']
    fam = v1610.FAMILY[family]
    shape = v1610.SHAPE[family]
    evolution = EVOLUTION[family]
    instruction = TIER[tier]
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


v14.prompts = prompts
v15.prompts = prompts

if __name__ == '__main__':
    v15.main()
