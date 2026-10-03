#!/usr/bin/env python3
"""Audit canonical character atlas registration and runtime exercise coverage."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RASTER = ROOT / "app/src/main/java/com/zerotoempire/game/CanonicalCharacterRaster.kt"
LAYER = ROOT / "app/src/main/java/com/zerotoempire/game/ReviewedCharacterLayer.kt"
DRAWABLES = ROOT / "app/src/main/res/drawable-nodpi"

ROLES = {
    "OPERATOR": "op",
    "TECHNICIAN": "tech",
    "LOGISTICS": "log",
    "ENGINEER": "eng",
}
ACTIONS = {
    "IDLE": "idle",
    "WALK": "walk",
    "WORK": "work",
    "CARRY": "carry",
    "REPAIR": "repair",
    "CELEBRATE": "celeb",
}

raster = RASTER.read_text(encoding="utf-8")
layer = LAYER.read_text(encoding="utf-8")
resource_variants = defaultdict(list)
for path in DRAWABLES.iterdir():
    if path.is_file() and path.suffix.lower() in {".png", ".webp", ".jpg", ".jpeg", ".gif", ".xml"}:
        resource_variants[path.stem].append(path.name)
duplicate_resource_names = {
    name: sorted(files) for name, files in resource_variants.items() if len(files) > 1
}
if duplicate_resource_names:
    raise SystemExit(f"ANDROID_DRAWABLE_DUPLICATE_NAMES={duplicate_resource_names}")

expected = {
    f"zte_chr_{role_slug}_{action_slug}_final"
    for role_slug in ROLES.values()
    for action_slug in ACTIONS.values()
}
registered = set(re.findall(r"R\.drawable\.(zte_chr_[a-z0-9_]+_final)", raster))
missing_registry = sorted(expected - registered)
extra_registry = sorted(registered - expected)
missing_files = sorted(name for name in expected if not (DRAWABLES / f"{name}.webp").is_file() and not (DRAWABLES / f"{name}.png").is_file())

placement_re = re.compile(
    r"CharacterPlacement\(ReviewedCharacterRole\.([A-Z]+),\s*"
    r"ReviewedCharacterAction\.([A-Z]+),"
)
exercised_pairs = set(placement_re.findall(layer))
exercised = {
    f"zte_chr_{ROLES[role]}_{ACTIONS[action]}_final"
    for role, action in exercised_pairs
    if role in ROLES and action in ACTIONS
}
unexercised = sorted(expected - exercised)

if missing_registry or extra_registry or missing_files:
    raise SystemExit(
        "CHARACTER_RUNTIME_AUDIT_FAIL "
        f"missing_registry={missing_registry} extra_registry={extra_registry} missing_files={missing_files}"
    )

print(f"CHARACTER_ATLASES_EXPECTED={len(expected)}")
print(f"CHARACTER_ATLASES_REGISTERED={len(registered)}")
print(f"CHARACTER_ATLASES_EXERCISED={len(exercised)}")
print(f"CHARACTER_ATLASES_UNEXERCISED={len(unexercised)}")
print("CHARACTER_ATLASES_UNEXERCISED_IDS=" + ",".join(unexercised))
print("CHARACTER_RUNTIME_REGISTRY_PASS=1")
