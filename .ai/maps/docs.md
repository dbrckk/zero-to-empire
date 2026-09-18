This file is a merged representation of a subset of the codebase, containing specifically included files and files not matching ignore patterns, combined into a single document by Repomix.
The content has been processed where content has been compressed (code blocks are separated by ⋮---- delimiter).

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: **/*.{py,js,mjs,cjs,ts,tsx,jsx,java,kt,kts,gd,groovy,gradle,toml,json,yaml,yml,sql,sh}
- Files matching these patterns are excluded: .ai/**, **/node_modules/**, **/.gradle/**, **/build/**, **/dist/**, **/.venv/**, **/__pycache__/**, **/.pytest_cache/**, **/.git/**, **/coverage/**, **/*.lock, **/*.min.js, **/*.map, assets/**, art/**, art_sources/**, marketing/**, colab/**, kaggle/**, discovery-cache.json, health-snapshot.json, history.json
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Content has been compressed - code blocks are separated by ⋮---- delimiter
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
ASCENDANT_CITY_ERA1_SPRITE_MANIFEST.json
```

# Files

## File: ASCENDANT_CITY_ERA1_SPRITE_MANIFEST.json
```json
{
  "schemaVersion": 1,
  "world": "Ascendant City",
  "era": 1,
  "eraName": "Scrappy Start",
  "sourceBible": "docs/AAA_WORLD_SPRITE_BIBLE.md",
  "artDirection": {
    "camera": "2.5D three-quarter, elevated 30-38 degrees, portrait-mobile readable",
    "masterCanvas": 2048,
    "background": "transparent",
    "keyLight": "upper-left warm-neutral",
    "fillLight": "cool environment fill",
    "materials": ["corrugated steel", "patched concrete", "painted scrap", "exposed cable", "oxidized alloy"],
    "accentRule": "dark physical mass first; cyan energy and warm amber operational light only as selective accents",
    "forbidden": ["baked UI text", "currency symbols", "logos", "rectangular background", "full-scene neon wash", "copied layouts or assets from other tycoon games"]
  },
  "runtimeRules": {
    "maxPrimaryLoopsPerVisibleLot": 1,
    "maxSecondaryLoopsPerVisibleLot": 2,
    "reducedMotion": "freeze decorative loops while keeping state readability",
    "lowPower": "same as reduced motion",
    "sharedClock": true,
    "touchHitboxIndependentFromTransparentPixels": true
  },
  "assets": [
    {
      "businessId": 0,
      "workingName": "Scrap Intake Yard",
      "family": "Foundry District",
      "tier": 0,
      "silhouette": "low asymmetrical scrap shed with angled roof, receiving hopper, exposed belt and compact generator",
      "heroRead": "large receiving hopper at left, moving belt across center, warm sorting lamp at right",
      "primaryLoop": "conveyor belt carrying scrap chunks toward the sorting press",
      "secondaryLoops": ["small exhaust fan", "occasional welding spark"],
      "layers": ["base_ground", "contact_shadow", "building_back", "building_main", "building_front", "roof_static", "machine_static", "conveyor", "machine_moving_a", "emissive_static", "emissive_pulse", "sign_static", "foreground_occluder"],
      "anchors": {"pivot": [0.5, 0.88], "income": [0.5, 0.18], "upgrade": [0.82, 0.22], "manager": [0.18, 0.20]},
      "animation": {"idleFrames": 6, "idleFps": 8, "productionFrames": 12, "productionFps": 12, "eventFrame": 8},
      "exportBase": "zte_business_00_t0"
    },
    {
      "businessId": 1,
      "workingName": "Patchwork Press",
      "family": "Foundry District",
      "tier": 0,
      "silhouette": "compact hydraulic press housed in a welded frame with pressure tank and cable bundles",
      "heroRead": "vertical press ram, broad steel platen, amber pressure gauge cluster",
      "primaryLoop": "press ram descends, compresses, rebounds with a short vibration settle",
      "secondaryLoops": ["pressure gauge needle twitch", "steam puff after compression"],
      "layers": ["base_ground", "contact_shadow", "building_back", "building_main", "building_front", "machine_static", "machine_moving_a", "machine_moving_b", "steam", "emissive_static", "emissive_pulse", "foreground_occluder"],
      "anchors": {"pivot": [0.5, 0.88], "income": [0.5, 0.16], "upgrade": [0.84, 0.21], "manager": [0.16, 0.21]},
      "animation": {"idleFrames": 4, "idleFps": 6, "productionFrames": 10, "productionFps": 12, "eventFrame": 6},
      "exportBase": "zte_business_01_t0"
    },
    {
      "businessId": 2,
      "workingName": "Jury-Rig Foundry",
      "family": "Foundry District",
      "tier": 0,
      "silhouette": "short furnace block with crooked chimney, crucible bay and external pipe cage",
      "heroRead": "bright furnace mouth below center, chimney at rear, crucible rail in foreground",
      "primaryLoop": "furnace breathes brighter as crucible rail advances and retracts",
      "secondaryLoops": ["chimney smoke pulse", "tiny molten drip glow"],
      "layers": ["base_ground", "contact_shadow", "building_back", "building_main", "building_front", "roof_static", "machine_static", "machine_moving_a", "emissive_static", "emissive_pulse", "smoke", "foreground_occluder"],
      "anchors": {"pivot": [0.5, 0.89], "income": [0.52, 0.15], "upgrade": [0.82, 0.20], "manager": [0.17, 0.20]},
      "animation": {"idleFrames": 6, "idleFps": 8, "productionFrames": 12, "productionFps": 12, "eventFrame": 7},
      "exportBase": "zte_business_02_t0"
    },
    {
      "businessId": 3,
      "workingName": "Micro-Grid Workshop",
      "family": "Foundry District",
      "tier": 0,
      "silhouette": "modular workshop around a crude generator coil with battery racks and overhead cable gantry",
      "heroRead": "central coil, two uneven battery stacks, cable gantry framing the silhouette",
      "primaryLoop": "generator coil charges from dim cyan to bright cyan and discharges into ground conduits",
      "secondaryLoops": ["battery indicator chase", "small roof fan"],
      "layers": ["base_ground", "contact_shadow", "building_back", "building_main", "building_front", "roof_static", "machine_static", "machine_moving_a", "emissive_static", "emissive_pulse", "energy_core", "foreground_occluder"],
      "anchors": {"pivot": [0.5, 0.89], "income": [0.5, 0.14], "upgrade": [0.83, 0.21], "manager": [0.17, 0.21]},
      "animation": {"idleFrames": 6, "idleFps": 8, "productionFrames": 10, "productionFps": 10, "eventFrame": 6},
      "exportBase": "zte_business_03_t0"
    }
  ],
  "sheetContract": {
    "buildingFrame": [512, 512],
    "paddingPx": 4,
    "order": "left-to-right then top-to-bottom",
    "fixedPivotAcrossFrames": true,
    "noPerFrameTrim": true,
    "metadataSidecar": true,
    "metadataFields": ["frameWidth", "frameHeight", "columns", "rows", "frameCount", "fps", "loop", "pivotX", "pivotY", "hitbox", "events"]
  },
  "qa": [
    "Readable at 88dp hero-lot size on a 360dp-wide phone",
    "Readable silhouette without emissive FX",
    "No text baked into art",
    "Contact shadow isolated",
    "Moving parts do not require repainting the full building",
    "Pivot stable across every frame",
    "Transparent padding preserved",
    "Looks original to Zero to Empire and not derivative of a specific competitor asset"
  ]
}
```
