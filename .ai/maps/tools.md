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
android/
  audit_character_runtime.py
  character_preview_emulator_smoke.sh
  character_preview_pixel_audit.py
  emulator_functional_smoke.sh
  local_original_character_emulator_smoke.sh
  local_review_ui_target.py
  parse_emulator_performance.py
  test_ui_click_target.py
  test_ui_dump_retry.py
  test_ui_economy_probe.py
  ui_click_target.py
  ui_dump_retry.sh
  ui_economy_probe.py
  validate_manifest_policy.py
  validate_release_privacy.py
sprites/
  tests/
    test_archive_character_candidates.py
    test_asset_production_policy.py
    test_character_bank_mobile_review.py
    test_character_bank_motion_audit.py
    test_character_candidate_bank.py
    test_character_identity_polish_mobile_review.py
    test_character_identity_polish.py
    test_character_mobile_motion_storyboard.py
    test_character_provisional_idle_seed.py
    test_character_repair_pose_plan.py
    test_character_role_contact_sheet.py
  action_contact.py
  animation_batch_planner.py
  archive_character_candidates.py
  asset_queue_utils.py
  asset_wave_orchestrator.py
  audit_character_bank_motion.py
  audit_character_candidates.py
  audit_chatgpt_originals.py
  audit_complete_sprite_manifest.py
  autonomous_walk.py
  build_character_bank_mobile_review.py
  build_character_candidate_bank.py
  build_character_identity_polish.py
  build_character_mobile_motion_storyboard.py
  build_character_review_panels.py
  build_character_role_contact_sheet.py
  build_original_offline_review.py
  build_sprite_contact_sheet.py
  build_tech_review_board.py
  character_acceptance_policy.py
  character_anchor_pair_salvage.py
  character_approved_idle_fallback.py
  character_cargo_identity_lock.py
  character_ground_shadow_cleanup.py
  character_head_identity_lock.py
  character_identity_polish_mobile_review.py
  character_idle_breathing_fallback.py
  character_provisional_idle_seed.py
  character_rejection_evidence.py
  character_repair_pose_plan.py
  character_review_matrix.py
  character_semantic_gate.py
  colab_mass_factory.py
  export_tech_canonical_review.py
  focused_sprite_atlas.py
  generate_strict_review_backlog.py
  hf_public_flux_factory.py
  hf_sprite_factory.py
  hf_static_manifest_factory.py
  identity_locked_walk_candidate.py
  integrate_fx04_runtime.py
  integrate_fx05_runtime.py
  integrate_fx06_runtime.py
  integrate_fx07_runtime.py
  kaggle_building_family_factory_v11.py
  kaggle_building_family_factory_v13.py
  kaggle_building_family_factory_v14.py
  kaggle_building_family_factory_v15.py
  kaggle_building_family_factory_v16_10.py
  kaggle_building_family_factory_v16.py
  kaggle_building_family_factory_v17.py
  kaggle_building_family_factory.py
  kaggle_character_sheet_factory_v1.py
  kaggle_fx_sheet_factory_v1.py
  kaggle_sprite_factory.py
  lightning_autopilot_loop.sh
  lightning_install_autopilot.sh
  lightning_remote_runner.py
  lightning_studio_factory.py
  local_character_action_fx.py
  local_character_contact_gait.py
  local_character_material_finish.py
  manifest_batch_planner.py
  multi_provider_static_manifest_factory.py
  package_chatgpt_originals.py
  package_tech_actions_runtime.py
  patch_final_character_motion.py
  plan_sprite_batches.py
  pollinations_building_batch.py
  pollinations_building_factory.py
  pollinations_character_sheet_factory.py
  procedural_fx_factory.py
  procedural_terrain_factory.py
  process_final_sprites.py
  promote_ter07_v3.py
  reconcile_strict_approvals.py
  render_chatgpt_originals.py
  render_original_character_previews.py
  repair_shadowed_character_atlas.py
  rigged_tech_actions_v3.py
  rigged_tech_walk_v2.py
  soft_skin_deform.py
  tech_prop_mount.py
  temporal_sprite_audit.py
  ter07_energy_conduit_candidate.py
  test_action_contact.py
  test_animation_batch_planner.py
  test_audit_chatgpt_originals.py
  test_autonomous_walk.py
  test_character_action_gate.py
  test_character_anchor_pair_salvage.py
  test_character_approved_idle_fallback.py
  test_character_ground_shadow_cleanup.py
  test_character_head_identity_lock.py
  test_character_provider_reservation.py
  test_character_rejection_evidence.py
  test_character_review_matrix.py
  test_character_semantic_gate.py
  test_export_tech_canonical_review.py
  test_focused_sprite_atlas.py
  test_identity_locked_walk_candidate.py
  test_local_character_action_fx.py
  test_local_character_contact_gait.py
  test_package_tech_actions_runtime.py
  test_pollinations_character_sheet_factory.py
  test_rigged_tech_actions_v3.py
  test_rigged_tech_walk_v2.py
  test_soft_skin_deform.py
  test_tech_prop_mount.py
  test_temporal_sprite_audit.py
  test_verify_character_action_candidates.py
  test_verify_character_idle_candidates.py
  test_weight_transfer.py
  validate_animation_sheet.py
  validate_runtime_asset.py
  verify_character_action_candidates.py
  verify_character_idle_candidates.py
  verify_local_character_bundle.py
  weight_transfer.py
process_final_assets.py
validate_isolated_sprite.py
```

# Files

## File: android/audit_character_runtime.py
```python
#!/usr/bin/env python3
"""Audit canonical character atlas registration and runtime exercise coverage."""
⋮----
ROOT = Path(__file__).resolve().parents[2]
RASTER = ROOT / "app/src/main/java/com/zerotoempire/game/CanonicalCharacterRaster.kt"
LAYER = ROOT / "app/src/main/java/com/zerotoempire/game/ReviewedCharacterLayer.kt"
DRAWABLES = ROOT / "app/src/main/res/drawable-nodpi"
⋮----
ROLES = {
ACTIONS = {
⋮----
raster = RASTER.read_text(encoding="utf-8")
layer = LAYER.read_text(encoding="utf-8")
resource_variants = defaultdict(list)
⋮----
duplicate_resource_names = {
⋮----
expected = {
registered = set(re.findall(r"R\.drawable\.(zte_chr_[a-z0-9_]+_final)", raster))
missing_registry = sorted(expected - registered)
extra_registry = sorted(registered - expected)
missing_files = sorted(name for name in expected if not (DRAWABLES / f"{name}.webp").is_file() and not (DRAWABLES / f"{name}.png").is_file())
⋮----
placement_re = re.compile(
exercised_pairs = set(placement_re.findall(layer))
exercised = {
unexercised = sorted(expected - exercised)
```

## File: android/character_preview_emulator_smoke.sh
```bash
#!/usr/bin/env bash
# Validates only a debug APK inside an isolated emulator.
# Capture the actual Android UI, not a pre-rendered image/mockup.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/ui_dump_retry.sh"

PKG="com.zerotoempire.game"
OUT="/tmp/zte-character-preview"
mkdir -p "$OUT"

dump() {
  ui_dump_with_retry "$OUT/$1.xml" ||
    { echo "CHARACTER_PREVIEW_FAIL=hierarchy-$1" >&2; exit 1; }
}

assert_text() {
  local needle="$1" source="$2"
  python3 - "$OUT/$source.xml" "$needle" <<'PY'
import sys, xml.etree.ElementTree as ET
path, needle=sys.argv[1], sys.argv[2].casefold()
items=[(n.attrib.get('text','')+' '+n.attrib.get('content-desc','')).casefold()
       for n in ET.parse(path).getroot().iter('node')]
if not any(needle in s for s in items):
    raise SystemExit('CHARACTER_PREVIEW_MISSING_UI_TEXT='+needle)
print('CHARACTER_PREVIEW_TEXT_PASS='+needle)
PY
}

click() {
  local needle="$1" name="$2" xy x y
  dump "$name"
  xy=$(python3 "$SCRIPT_DIR/ui_click_target.py" "$OUT/$name.xml" "$needle")
  read -r x y <<<"$xy"
  [[ "$x" =~ ^[0-9]+$ && "$y" =~ ^[0-9]+$ ]] ||
    { echo "CHARACTER_PREVIEW_FAIL=coordinates-$needle" >&2; exit 1; }
  adb shell input tap "$x" "$y"
  sleep 1
}

# LazyColumn keeps only the currently visible action rows in its accessibility
# hierarchy. On narrow Android screens REPAIR and CELEBRATE are below the fold;
# scrolling to a button is necessary before resolving its clickable bounds.
click_action() {
  local action="$1" label="$2" name="$3" attempt xy x y
  # The action label may be visible while its button is clipped by the
  # viewport. A tap returning exit 0 does not prove Compose changed state.
  # Retry until the *state heading* reflects the selected action.
  for attempt in 0 1 2 3 4 5 6 7 8 9; do
    dump "$name-scroll-$attempt"
    if xy=$(python3 "$SCRIPT_DIR/ui_click_target.py" "$OUT/$name-scroll-$attempt.xml" "$label" 2>/dev/null); then
      read -r x y <<<"$xy"
      if [[ "$x" =~ ^[0-9]+$ && "$y" =~ ^[0-9]+$ &&
            "$y" -gt "$((height*8/100))" && "$y" -lt "$((height*91/100))" ]]; then
        adb shell input tap "$x" "$y"
        sleep 1
        dump "$name-after-tap-$attempt"
        if python3 - "$OUT/$name-after-tap-$attempt.xml" "$action" <<'PY'
import sys, xml.etree.ElementTree as ET
expected='TECH ACTION: '+sys.argv[2].upper()
root=ET.parse(sys.argv[1]).getroot()
labels=[n.attrib.get('text','') for n in root.iter('node')]
raise SystemExit(0 if expected in labels else 1)
PY
        then
          echo "CHARACTER_PREVIEW_ACTION_CONFIRMED=$action attempt=$attempt"
          return 0
        fi
        echo "CHARACTER_PREVIEW_ACTION_TAP_NOT_APPLIED=$action attempt=$attempt" >&2
      fi
    fi
    # Action selectors are inside a LazyColumn. After CELEBRATE or REPAIR,
    # earlier actions (IDLE/WALK/WORK) are above the fold. Scrolling only
    # downward makes the full six-action audit fail despite a healthy UI.
    # Search in the expected direction first, then reverse once if the
    # viewport was already beyond the desired row.
    local from_y to_y
    if [[ "$action" == "IDLE" || "$action" == "WALK" || "$action" == "WORK" ]]; then
      from_y="$((height*32/100))"
      to_y="$((height*73/100))"
    else
      from_y="$((height*73/100))"
      to_y="$((height*32/100))"
    fi
    if (( attempt >= 6 )); then
      local temp="$from_y"
      from_y="$to_y"
      to_y="$temp"
    fi
    adb shell input swipe "$((width/2))" "$from_y" "$((width/2))" "$to_y" 380
    sleep 1
  done
  echo "CHARACTER_PREVIEW_FAIL=action-selection-not-confirmed:$action" >&2
  return 1
}

APK="app/build/outputs/apk/debug/app-debug.apk"
test -s "$APK"
adb install -r "$APK" >/dev/null
adb logcat -c
adb shell am start -W -n "$PKG/.CharacterReviewActivity" > "$OUT/start.txt"
# A cold emulator may still be drawing the launcher after am start returns.
# Retry the *actual* QA heading rather than assuming the first hierarchy
# is the app's activity. Preserve each diagnostic dump for CI artifacts.
ready=false
for attempt in 1 2 3 4 5 6; do
  sleep 5
  if ! adb shell pidof "$PKG" | tr -d '\r\n' | grep -Eq '^[0-9]+$'; then
    echo "CHARACTER_PREVIEW_FAIL=app-process-died" >&2
    exit 1
  fi
  dump "opening-attempt-$attempt"
  # A System UI ANR dialog blocks accessibility even when our app is alive.
  # Dismiss it once with the system's "Wait" action, then relaunch QA.
  # Preserve the pre-recovery hierarchy as evidence; never count this as pass.
  if [[ "$attempt" -eq 1 ]] && grep -Eq "System UI (isn.t|isn&amp;apos;t) responding" "$OUT/opening-attempt-$attempt.xml"; then
    echo "CHARACTER_PREVIEW_SYSTEM_UI_ANR_RECOVERY=attempted" >&2
    python3 "$SCRIPT_DIR/ui_click_target.py" "$OUT/opening-attempt-$attempt.xml" "Wait" > "$OUT/system-ui-wait-coordinates.txt" || true
    if read -r wait_x wait_y < "$OUT/system-ui-wait-coordinates.txt" &&
       [[ "$wait_x" =~ ^[0-9]+$ && "$wait_y" =~ ^[0-9]+$ ]]; then
      adb shell input tap "$wait_x" "$wait_y" || true
      sleep 4
      adb shell am start -W -n "$PKG/.CharacterReviewActivity" > "$OUT/relaunch-after-system-ui-anr.txt" || true
    fi
  fi
  if python3 - "$OUT/opening-attempt-$attempt.xml" <<'PY'
import sys
import xml.etree.ElementTree as ET
root=ET.parse(sys.argv[1]).getroot()
raise SystemExit(0 if any(
    'animation qa' in (n.attrib.get('text','')+' '+n.attrib.get('content-desc','')).casefold()
    for n in root.iter('node')) else 1)
PY
  then
    cp "$OUT/opening-attempt-$attempt.xml" "$OUT/opening.xml"
    ready=true
    break
  fi
  echo "CHARACTER_PREVIEW_WAIT_FOR_GALLERY=$attempt"
done
if [[ "$ready" != true ]]; then
  adb shell dumpsys activity activities > "$OUT/activity-state.txt" || true
  adb shell dumpsys window > "$OUT/window-state.txt" || true
  adb logcat -d > "$OUT/logcat-startup.txt" || true
  adb exec-out screencap -p > "$OUT/gallery-startup-failure.png" || true
  echo "CHARACTER_PREVIEW_DIAGNOSTICS_BEGIN" >&2
  grep -E 'mResumedActivity|topResumedActivity|mFocusedApp|mCurrentFocus' "$OUT/activity-state.txt" "$OUT/window-state.txt" | tail -15 >&2 || true
  grep -E 'FATAL EXCEPTION|AndroidRuntime|ActivityTaskManager.*(Displayed|START)|am_crash' "$OUT/logcat-startup.txt" | tail -25 >&2 || true
  python3 - "$OUT/opening-attempt-6.xml" <<'PY'
import sys, xml.etree.ElementTree as ET
try:
    root=ET.parse(sys.argv[1]).getroot()
    values=[(n.attrib.get('package',''),n.attrib.get('text',''),n.attrib.get('content-desc',''))
            for n in root.iter('node')]
    print('CHARACTER_PREVIEW_VISIBLE_NODES='+repr(values[:40]),file=sys.stderr)
except Exception as exc:
    print('CHARACTER_PREVIEW_XML_DIAGNOSTIC='+repr(exc),file=sys.stderr)
PY
  echo "CHARACTER_PREVIEW_DIAGNOSTICS_END" >&2
  echo "CHARACTER_PREVIEW_FAIL=gallery-heading-not-visible" >&2
  exit 1
fi
assert_text "Animation QA" opening
assert_text "Pause" opening
adb exec-out screencap -p > "$OUT/gallery-playing.png"

click Pause before-pause
dump paused
assert_text Lecture paused
adb exec-out screencap -p > "$OUT/gallery-paused.png"

click "+1" before-step
dump after-step
assert_text Lecture after-step
adb exec-out screencap -p > "$OUT/gallery-step.png"

# Scroll lazily rendered roles into view; inspect actual TECH textures.
screen=$(adb shell wm size | tr -d '\r' | tail -n 1)
resolution=${screen##* }
width=${resolution%x*}
height=${resolution#*x}
[[ "$width" =~ ^[0-9]+$ && "$height" =~ ^[0-9]+$ ]] || {
  echo "CHARACTER_PREVIEW_FAIL=screen-dimensions:$screen" >&2; exit 1;
}
found=false
for attempt in 0 1 2 3 4 5; do
  dump "tech-scroll-$attempt"
  if grep -Fqi "TECHNICIAN" "$OUT/tech-scroll-$attempt.xml"; then
    found=true
    break
  fi
  adb shell input swipe "$((width/2))" "$((height*80/100))" "$((width/2))" "$((height*28/100))" 450
  sleep 1
done
if [[ "$found" != true ]]; then
  echo "CHARACTER_PREVIEW_FAIL=technician-not-visible-after-scroll" >&2
  exit 1
fi
assert_text TECHNICIAN "tech-scroll-$attempt"
adb exec-out screencap -p > "$OUT/tech-candidate-grid.png"

# The 96dp gallery proves only enlarged asset display. The next item uses
# ReviewedCharacterLayer itself at the actual 35–46dp city actor sizes.
# Locate its accessible heading, capture real Android pixels, and retain them
# for manual QA. This is not automatic semantic approval.
stage_found=false
for stage_attempt in 0 1 2 3 4 5 6 7; do
  dump "stage-scale-scroll-$stage_attempt"
  if grep -Fq "STAGE-SCALE CHARACTER LAYER" "$OUT/stage-scale-scroll-$stage_attempt.xml"; then
    stage_found=true
    break
  fi
  adb shell input swipe "$((width/2))" "$((height*82/100))" "$((width/2))" "$((height*25/100))" 450
  sleep 1
done
if [[ "$stage_found" != true ]]; then
  echo "CHARACTER_PREVIEW_FAIL=game-scale-stage-not-visible" >&2
  exit 1
fi
assert_text "STAGE-SCALE CHARACTER LAYER" "stage-scale-scroll-$stage_attempt"
# Android's LazyColumn can initially align the stage heading near the
# bottom of the screen. One swipe can reveal only the *empty upper half*
# of the 620dp stage, so frame the actual actors with bounded scroll+pixels.
actor_visible=false
for actor_attempt in 1 2 3 4 5; do
  adb shell input swipe "$((width/2))" "$((height*84/100))" "$((width/2))" "$((height*18/100))" 650
  sleep 2
  adb exec-out screencap -p > "$OUT/tech-game-scale-attempt-$actor_attempt.png"
  if python3 - "$OUT/tech-game-scale-attempt-$actor_attempt.png" <<'PY'
import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
w,h=im.size
# The dark stage gradient itself has low brightness and low saturation.
# The viewport must actually contain actors, not only the gallery heading
# or an empty upper area. Keep every screenshot for incident review.
crop=im.crop((int(w*.05),int(h*.54),int(w*.95),int(h*.85)))
colored=sum(1 for r,g,b in crop.getdata()
            if max(r,g,b)>=90 and max(r,g,b)-min(r,g,b)>35)
print('CHARACTER_PREVIEW_GAME_SCALE_COLORED_PIXELS='+str(colored))
raise SystemExit(0 if colored>=100 else 1)
PY
  then
    cp "$OUT/tech-game-scale-attempt-$actor_attempt.png" "$OUT/tech-game-scale-layer.png"
    actor_visible=true
    echo "CHARACTER_PREVIEW_GAME_SCALE_SCREENSHOT_PASS=1 attempt=$actor_attempt"
    break
  fi
  echo "CHARACTER_PREVIEW_WAIT_FOR_ACTORS=$actor_attempt" >&2
done
if [[ "$actor_visible" != true ]]; then
  echo "CHARACTER_PREVIEW_FAIL=game-scale-actors-not-visible" >&2
  exit 1
fi

# Exercise the new day/night QA comparison, not just the default night
# state. Keep both Android screenshots taken from the SAME scroll position
# so the pixel contrast comparison is meaningful. Never interpret this
# automated background check as aesthetic or semantic sprite approval.
daylight_toggle_visible=false
for daylight_attempt in 0 1 2 3 4 5 6; do
  dump "daylight-toggle-scroll-$daylight_attempt"
  # uiautomator can expose a label clipped to only a few pixels at
  # the top of the viewport. A grep hit is NOT a usable touch target:
  # the previous run tapped a 5px fragment and never changed modes.
  if python3 - "$OUT/daylight-toggle-scroll-$daylight_attempt.xml" "$height" <<'PY'
import re, sys, xml.etree.ElementTree as ET
root = ET.parse(sys.argv[1]).getroot()
height = int(sys.argv[2])
for node in root.iter('node'):
    if node.attrib.get('text') != 'Daylight stage':
        continue
    m = re.fullmatch(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]',
                     node.attrib.get('bounds', ''))
    if not m:
        continue
    x0, y0, x1, y1 = map(int, m.groups())
    if (x1 > x0 and y1-y0 >= max(24, height//100)
            and y0 >= height//20 and y1 <= height*93//100):
        print('CHARACTER_PREVIEW_DAYLIGHT_BUTTON_FULLY_VISIBLE=1')
        raise SystemExit(0)
raise SystemExit(1)
PY
  then
    daylight_toggle_visible=true
    break
  fi
  # Return towards the title if actor framing scrolled past the button.
  adb shell input swipe "$((width/2))" "$((height*24/100))" "$((width/2))" "$((height*75/100))" 420
  sleep 1
done
if [[ "$daylight_toggle_visible" != true ]]; then
  echo "CHARACTER_PREVIEW_FAIL=daylight-toggle-not-visible" >&2
  exit 1
fi
assert_text "NIGHT CONTRAST REVIEW" "daylight-toggle-scroll-$daylight_attempt"
adb exec-out screencap -p > "$OUT/tech-night-matched-viewport.png"
click "Daylight stage" before-daylight-toggle
dump daylight-active
assert_text "DAYLIGHT CONTRAST REVIEW" daylight-active
assert_text "Night stage" daylight-active
adb exec-out screencap -p > "$OUT/tech-daylight-matched-viewport.png"
python3 - "$OUT/tech-night-matched-viewport.png" "$OUT/tech-daylight-matched-viewport.png" <<'PY'
import sys
from PIL import Image, ImageStat
night = Image.open(sys.argv[1]).convert('RGB')
day = Image.open(sys.argv[2]).convert('RGB')
if night.size != day.size:
    raise SystemExit('CHARACTER_PREVIEW_FAIL=contrast-image-dimensions')
w, h = night.size
# The lower central screen shows the stage, with no toggle text. Median
# luminance resists variations from animated characters and shadows.
box = (int(w*.30), int(h*.60), int(w*.70), int(h*.82))
def med_brightness(im):
    med = ImageStat.Stat(im.crop(box).resize((40, 40))).median
    return sum(med)/3
dark, light = med_brightness(night), med_brightness(day)
print(f'CHARACTER_PREVIEW_DAY_NIGHT_LUMA night={dark:.1f} day={light:.1f}')
if dark >= 85 or light <= 90 or light-dark <= 55:
    raise SystemExit('CHARACTER_PREVIEW_FAIL=day-night-contrast-not-visible')
print('CHARACTER_PREVIEW_DAY_NIGHT_CONTRAST_PASS=1')
PY
click "Night stage" before-night-restore
dump night-restored
assert_text "NIGHT CONTRAST REVIEW" night-restored

# Prove the stage can isolate the two actual city TECH placements, switch
# their rendered atlas to a DIFFERENT action, and step that action's frame
# without scrolling back to the main gallery controls.
click "TECH only" before-tech-focus
dump tech-focused
assert_text "TECH ACTION: WALK" tech-focused
click_action REPAIR REPAIR before-tech-repair-selection
dump tech-repair-selected
assert_text "TECH ACTION: REPAIR" tech-repair-selected
click "Stage +1" before-tech-stage-step
dump tech-repair-stepped
assert_text "TECH ACTION: REPAIR" tech-repair-stepped
python3 - "$OUT/tech-repair-selected.xml" "$OUT/tech-repair-stepped.xml" <<'PY'
import re, sys
import xml.etree.ElementTree as ET
def stage_frame(path):
    root=ET.parse(path).getroot()
    values=[n.attrib.get('text','')+' '+n.attrib.get('content-desc','')
            for n in root.iter('node')]
    hits=[int(m.group(1)) for v in values
          if (m:=re.search(r'STAGE FRAME:\s*(\d+)', v))]
    if len(hits)!=1:
        raise SystemExit('CHARACTER_PREVIEW_FAIL=stage-frame-counter-not-visible')
    return hits[0]
before,after=(stage_frame(path) for path in sys.argv[1:3])
if after != (before+1)%1680:
    raise SystemExit('CHARACTER_PREVIEW_FAIL=stage-frame-step-not-applied')
print(f'CHARACTER_PREVIEW_STAGE_STEP_PASS=before:{before} after:{after}')
PY
# Inspect all six actions with the *real city renderer*, not just
# the enlarged grid. Preserve an emulator screenshot per action for
# frame-by-frame semantic review; selecting an action is not approval.
for action in IDLE WALK WORK CARRY REPAIR CELEBRATE; do
  click_action "$action" "$action" "before-tech-action-$action"
  dump "tech-action-$action"
  assert_text "TECH ACTION: $action" "tech-action-$action"
  adb exec-out screencap -p > "$OUT/tech-stage-$action.png"
  test -s "$OUT/tech-stage-$action.png"
  echo "CHARACTER_PREVIEW_TECH_ACTION_CAPTURE=$action"
done
echo "CHARACTER_PREVIEW_TECH_ACTION_SELECTOR_PASS=6"
# A nonempty screenshot is insufficient: reject six identical actor renders
# even when the dropdown labels have changed. Crop only the compact actor
# pixels beneath the 42dp QA caption, outside all interactive text.
python3 "$SCRIPT_DIR/character_preview_pixel_audit.py" "$OUT"

# Pixel-proof of temporal animation at 42dp, not just six static poses:
# step five moving actions four real Android frames while paused. Every
# screenshot and accessibility hierarchy remains in the CI artifact.
for moving_action in WALK WORK CARRY REPAIR CELEBRATE; do
  click_action "$moving_action" "$moving_action" "before-temporal-action-$moving_action"
  for tick in 0 1 2 3; do
    if [[ "$tick" -gt 0 ]]; then
      click "Stage +1" "before-temporal-step-$moving_action-$tick"
    fi
    dump "tech-action-$moving_action-frame-$tick"
    assert_text "TECH ACTION: $moving_action" "tech-action-$moving_action-frame-$tick"
    adb exec-out screencap -p > "$OUT/tech-stage-$moving_action-frame-$tick.png"
    test -s "$OUT/tech-stage-$moving_action-frame-$tick.png"
  done
done
python3 "$SCRIPT_DIR/character_preview_pixel_audit.py" --temporal "$OUT"

adb logcat -d > "$OUT/logcat.txt"
if grep -E "FATAL EXCEPTION|AndroidRuntime.*FATAL" "$OUT/logcat.txt"; then
  echo "CHARACTER_PREVIEW_FAIL=fatal_exception" >&2
  exit 1
fi
echo "CHARACTER_PREVIEW_EMULATOR_PASS=1"
```

## File: android/character_preview_pixel_audit.py
```python
#!/usr/bin/env python3
"""Debug-only: prove six TECH action screenshots contain distinct actor pixels.

The gate is deliberately semantic-neutral: changing action text is NOT proof
that the rendered sprite changed. This script crops the real 42dp night
preview by locating its XML caption, outside all action labels/buttons, then
checks that there is a nonempty actor and that each action differs visibly.
It cannot grant strict DONE or visual release approval.
"""
⋮----
ACTIONS = ("IDLE", "WALK", "WORK", "CARRY", "REPAIR", "CELEBRATE")
LABEL = "NIGHT · 42 dp"
BOUNDS = re.compile(r"^\[(\d+),(\d+)\]\[(\d+),(\d+)\]$")
MIN_VISIBLE_PIXELS = 120
MIN_DIFFERENT_PIXELS = 150
TOLERANCE = 25
⋮----
def review_crop(folder: Path, action: str, frame_label: str = "") -> tuple[Image.Image, int]
⋮----
# The same real-size crop validator is used by single-action and
# consecutive-frame Android screenshots, with identical clipping gates.
suffix = f"-{frame_label}" if frame_label else ""
xml = folder / f"tech-action-{action}{suffix}.xml"
shot = folder / f"tech-stage-{action}{suffix}.png"
root = ET.parse(xml).getroot()
text_values = [n.attrib.get("text", "") for n in root.iter("node")]
⋮----
frame_values = [v.split(":", 1)[1].strip() for v in text_values
⋮----
labels = [n for n in root.iter("node") if n.attrib.get("text") == LABEL]
⋮----
rect = BOUNDS.fullmatch(labels[0].attrib.get("bounds", ""))
⋮----
height = y1 - y0
⋮----
rgb = source.convert("RGB")
# A previously green emulator run had its 42dp actor cropped at the
# waist by the LazyColumn viewport. The old crop also included the
# Android navbar, which inflated the non-background pixel count.
# Prove the NIGHT and DAY preview panes extend below the whole sprite
# before comparing any action pixels. Coordinates scale with the actual
# Android caption size, not hard-coded emulator resolution.
⋮----
matches = [n for n in root.iter("node")
⋮----
bounds = BOUNDS.fullmatch(matches[0].attrib.get("bounds", ""))
⋮----
caption_px = cy1 - cy0
# The avatar is 39-42dp tall beneath this 14sp caption.
# The pane must still have its native background well below the
# shoes. A screenshot captured mid-scroll / below the viewport
# fails, even when it contains the actor's head and shoulders.
probe_x = cx0 - max(8, round(caption_px * .35))
probe_y = cy1 + round(caption_px * 3.25)
⋮----
sample = rgb.getpixel((probe_x, probe_y))
⋮----
half_width = round(height * 2.14)
⋮----
crop = rgb.crop((left, top, right, bottom))
base = crop.getpixel((0, 0))
visible = sum(
⋮----
def audit(folder: Path) -> None
⋮----
renders = [review_crop(folder, action) for action in ACTIONS]
⋮----
second = renders[other][0]
⋮----
different = sum(
⋮----
def audit_temporal(folder: Path) -> None
⋮----
"""Real Android 42dp pixel motion: prove five animated actions change frames.

    This is a technical motion gate only. Plausible weight, foot contact and
    human recognition still require semantic visual review.
    """
⋮----
samples = [review_crop(folder, action, f"frame-{i}") for i in range(4)]
frames = [number for _, number in samples]
⋮----
changed_counts = []
⋮----
changed = sum(
⋮----
args = sys.argv[1:]
```

## File: android/emulator_functional_smoke.sh
```bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/ui_dump_retry.sh"

PKG="com.zerotoempire.game"
ACT="$PKG/.MainActivity"
EVIDENCE="/tmp/zte-functional"
mkdir -p "$EVIDENCE"

fail() {
  echo "FUNCTIONAL_SMOKE_ERROR=$*" >&2
  timeout -k 5s 25s adb logcat -d > "$EVIDENCE/logcat-failure.txt" || true
  timeout -k 5s 25s adb exec-out screencap -p > "$EVIDENCE/failure.png" || true
  exit 1
}

dump_ui() {
  local name="$1"
  ui_dump_with_retry "$EVIDENCE/$name.xml" || fail "ui-hierarchy-unavailable:$name"
}

click_node() {
  local needle="$1"
  local dump_name="$2"
  local attempt
  for attempt in 1 2 3 4 5; do
    # A Pixel Launcher ANR can obscure otherwise healthy game navigation.
    # Recover the system dialog before probing; never bypass the target assertion.
    dismiss_launcher_anr_if_present
    dump_ui "$dump_name"
    if python3 - "$EVIDENCE/$dump_name.xml" "$needle" <<'PY_PROBE'
import sys,xml.etree.ElementTree as ET
needle=sys.argv[2].lower()
for node in ET.parse(sys.argv[1]).getroot().iter('node'):
    label=(node.attrib.get('text','')+' '+node.attrib.get('content-desc','')).lower()
    if needle in label and node.attrib.get('bounds','') not in ('','[0,0][0,0]'):
        raise SystemExit(0)
raise SystemExit(1)
PY_PROBE
    then
      break
    fi
    if (( attempt == 5 )); then
      fail "navigation-target-not-ready:$needle"
    fi
    echo "UI_WAIT_TARGET=$needle attempt=$attempt"
    sleep 2
  done
  python3 - "$EVIDENCE/$dump_name.xml" "$needle" <<'PY'
import re,sys,subprocess,xml.etree.ElementTree as ET
path,needle=sys.argv[1],sys.argv[2]
root=ET.parse(path).getroot()
needle_l=needle.lower()
matches=[]
for n in root.iter('node'):
    text=(n.attrib.get('text','')+' '+n.attrib.get('content-desc','')).strip()
    if needle_l in text.lower():
        b=n.attrib.get('bounds','')
        m=re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]',b)
        if m:
            x1,y1,x2,y2=map(int,m.groups())
            area=max(1,(x2-x1)*(y2-y1))
            matches.append((area,(x1+x2)//2,(y1+y2)//2,text,b))
if not matches:
    print(f'NODE_NOT_FOUND={needle}',file=sys.stderr);sys.exit(2)
matches.sort()
_,x,y,text,b=matches[0]
print(f'CLICK_NODE={needle} matched={text!r} bounds={b} at={x},{y}')
subprocess.run(['adb','shell','input','tap',str(x),str(y)],check=True)
PY
  sleep 1
}

click_resolved_node() {
  local needle="$1"
  local dump_name="$2"
  local coords x y
  dump_ui "$dump_name"
  coords=$(python3 "$SCRIPT_DIR/ui_click_target.py" "$EVIDENCE/$dump_name.xml" "$needle") || fail "click-target-not-found:$needle"
  read -r x y <<<"$coords"
  [[ "$x" =~ ^[0-9]+$ && "$y" =~ ^[0-9]+$ ]] || fail "invalid-click-target:$needle:$coords"
  echo "CLICK_RESOLVED_NODE=$needle at=$x,$y"
  adb shell input tap "$x" "$y"
  sleep 1
}

assert_ui_contains() {
  local needle="$1"
  local dump_name="$2"
  dump_ui "$dump_name"
  python3 - "$EVIDENCE/$dump_name.xml" "$needle" <<'PY'
import sys,xml.etree.ElementTree as ET
path,needle=sys.argv[1],sys.argv[2]
needle=needle.lower()
for n in ET.parse(path).getroot().iter('node'):
    text=(n.attrib.get('text','')+' '+n.attrib.get('content-desc','')).lower()
    if needle in text:
        print(f'UI_ASSERT_PASS={needle}')
        sys.exit(0)
print(f'UI_ASSERT_FAIL={needle}',file=sys.stderr)
sys.exit(2)
PY
}

assert_ui_not_contains() {
  local needle="$1"
  local dump_name="$2"
  dump_ui "$dump_name"
  python3 - "$EVIDENCE/$dump_name.xml" "$needle" <<'PY'
import sys,xml.etree.ElementTree as ET
path,needle=sys.argv[1],sys.argv[2]
needle=needle.lower()
for n in ET.parse(path).getroot().iter('node'):
    text=(n.attrib.get('text','')+' '+n.attrib.get('content-desc','')).lower()
    if needle in text:
        print(f'UI_ASSERT_UNEXPECTED={needle}',file=sys.stderr)
        sys.exit(2)
print(f'UI_ASSERT_ABSENT_PASS={needle}')
PY
}

complete_onboarding_if_present() {
  local step probe
  for step in 0 1 2 3 4 5; do
    probe="onboarding-step-$step"
    dump_ui "$probe"
    # An emulator-side Quickstep / Pixel Launcher ANR can cover the app.
    # Never misreport onboarding success merely because the game is hidden.
    if grep -Eq "(Pixel Launcher|Quickstep) isn.t responding" "$EVIDENCE/$probe.xml"; then
      dismiss_launcher_anr_if_present
      dump_ui "$probe"
      if grep -Eq "(Pixel Launcher|Quickstep) isn.t responding" "$EVIDENCE/$probe.xml"; then
        fail "system-dialog-obscures-onboarding:step=$step"
      fi
    fi
    if ! grep -Fq 'ZERO → EMPIRE' "$EVIDENCE/$probe.xml"; then
      # Require a real game navigation target, not just absence of a label:
      # a crash, lock screen or opaque system dialog must never pass here.
      grep -Fq 'MANAGERS' "$EVIDENCE/$probe.xml" ||
        fail "onboarding-ended-without-game-navigation:step=$step"
      echo "FUNCTIONAL_ONBOARDING_PASS=steps-$step"
      return 0
    fi
    if (( step >= 5 )); then
      fail "onboarding-exceeded-max-steps:5"
    fi
    if grep -Fq 'CONTINUE' "$EVIDENCE/$probe.xml"; then
      click_node "CONTINUE" "onboarding-before-continue-$step"
    elif grep -Fq 'BUILD MY EMPIRE' "$EVIDENCE/$probe.xml"; then
      click_resolved_node "BUILD MY EMPIRE" "onboarding-before-build-$step"
    else
      fail "onboarding-action-missing:step=$step"
    fi
  done
  fail "onboarding-unexpected-loop-exit"
}

check_alive() {
  adb shell pidof "$PKG" | tr -d '\r\n' | grep -Eq '^[0-9]+' || fail "process-not-alive"
}

dismiss_launcher_anr_if_present() {
  local attempt probe coords x y
  for attempt in 1 2 3 4 5 6; do
    probe="$EVIDENCE/system-dialog-$attempt.xml"
    if ! ui_dump_with_retry "$probe"; then
      return 0
    fi
    if ! grep -Eq "(Pixel Launcher|Quickstep) isn.t responding" "$probe"; then
      return 0
    fi
    echo "SYSTEM_FLAKE_DETECTED=launcher-or-quickstep-anr attempt=$attempt"
    coords=$(python3 "$SCRIPT_DIR/ui_click_target.py" "$probe" "Wait" 2>/dev/null || true)
    if [[ -n "$coords" ]]; then
      read -r x y <<<"$coords"
      if [[ "$x" =~ ^[0-9]+$ && "$y" =~ ^[0-9]+$ ]]; then
        adb shell input tap "$x" "$y"
        sleep 2
        continue
      fi
    fi
    # Android's standard ANR dialog uses KEYCODE_ENTER on the focused action
    # only as a last resort. Never force-stop the app under test here.
    adb shell input keyevent KEYCODE_BACK || true
    sleep 2
  done
  fail "system-launcher-anr-dialog-persisted"
}

check_no_fatal() {
  local attempt
  # adb occasionally drops the shell connection after this long emulator soak.
  # Retrying collection is safe; never ignore missing crash evidence.
  for attempt in 1 2 3; do
    if timeout -k 5s 25s adb logcat -d > "$EVIDENCE/logcat.txt"; then
      break
    fi
    echo "LOGCAT_RETRY=$attempt" >&2
    if (( attempt == 3 )); then
      fail "final-logcat-unavailable"
    fi
    sleep 2
  done
  if grep -E "FATAL EXCEPTION|AndroidRuntime.*FATAL|Process: $PKG.*has died" "$EVIDENCE/logcat.txt"; then
    fail "fatal-runtime-crash"
  fi
}

APK="app/build/outputs/apk/debug/app-debug.apk"
test -s "$APK" || fail "apk-missing"
adb install -r "$APK" >/dev/null
adb shell pm clear "$PKG" >/dev/null
adb logcat -c
adb shell am start -W -n "$ACT" > "$EVIDENCE/start.txt"
sleep 5
dismiss_launcher_anr_if_present
check_alive
dump_ui "initial"
adb exec-out screencap -p > "$EVIDENCE/initial.png"

# A fresh or restored emulator can enter the onboarding at different persisted
# points. Intermediate pages expose CONTINUE, while the final page exposes the
# explicit BUILD MY EMPIRE CTA. Accept only those known actions and keep the
# whole flow bounded to the five visual onboarding steps.
complete_onboarding_if_present

# Real screenshots from the running Android app. Keep them unaltered;
# debug-emulator previews are NOT a substitute for final production-AAB review.
mkdir -p "$EVIDENCE/play-store-preview"
for tab in MANAGERS UPGRADES GOALS EMPIRE; do
  click_node "$tab" "before-$tab"
  assert_ui_contains "$tab" "after-$tab"
  case "$tab" in
    MANAGERS) shot="02-managers" ;;
    UPGRADES) shot="03-upgrades" ;;
    GOALS) shot="04-goals" ;;
    EMPIRE) shot="01-empire" ;;
  esac
  adb exec-out screencap -p > "$EVIDENCE/play-store-preview/$shot.png" || fail "screenshot-capture-failed:$tab"
  test -s "$EVIDENCE/play-store-preview/$shot.png" || fail "empty-screenshot:$tab"
done
cat > "$EVIDENCE/play-store-preview/README.txt" <<'EOF'
ZERO -> EMPIRE. Unmodified Android emulator screenshots.
Captured from the real game in debug emulator smoke (Pixel 6, API 35).
These are Play listing composition candidates, not production-AAB images.
Review text readability, margins, Google Play policy and final version
before uploading screenshots to the Play Console.
EOF


# POWER CORE has a non-clickable text label layered over part of its clickable
# surface. Resolve the nearby clickable node and deliberately choose an uncovered
# point, then prove that one real UI tap increased visible capital.
click_resolved_node "Power Core" "before-power-core"
CAPITAL_BEFORE=$(python3 "$SCRIPT_DIR/ui_economy_probe.py" capital "$EVIDENCE/before-power-core.xml") || fail "capital-probe-failed:before-power-core"
dump_ui "after-power-core"
CAPITAL_AFTER=$(python3 "$SCRIPT_DIR/ui_economy_probe.py" capital "$EVIDENCE/after-power-core.xml") || fail "capital-probe-failed:after-power-core"
if ! python3 - "$CAPITAL_BEFORE" "$CAPITAL_AFTER" <<'PY'
import sys
raise SystemExit(0 if float(sys.argv[2]) > float(sys.argv[1]) else 1)
PY
then
  fail "power-core-tap-not-credited:before=$CAPITAL_BEFORE after=$CAPITAL_AFTER"
fi
echo "POWER_CORE_TAP_PASS=before=$CAPITAL_BEFORE after=$CAPITAL_AFTER"
check_alive

click_node "Street Stand" "before-street-stand-buy"
sleep 2
assert_ui_contains "LV 1" "after-street-stand-buy"

# The remaining smoke validates manager automation, offline earnings and durable
# persistence; it does not need to spend minutes grinding 2,500 synthetic taps.
# Seed only the debug APK after the real tap + purchase have been verified. The
# release source set contains no SmokeSeedReceiver, enforced by the release
# manifest allowlist in Android CI.
adb shell am force-stop "$PKG"
adb shell am broadcast \
  --include-stopped-packages \
  -a "$PKG.DEBUG_SMOKE_SEED" \
  -n "$PKG/.SmokeSeedReceiver" \
  --el cash 3000 > "$EVIDENCE/debug-seed.txt"
adb shell am force-stop "$PKG"
adb shell am start -W -n "$ACT" > "$EVIDENCE/debug-seed-restart.txt"
sleep 3
check_alive
dump_ui "after-debug-seed"
SEEDED_CAPITAL=$(python3 "$SCRIPT_DIR/ui_economy_probe.py" capital "$EVIDENCE/after-debug-seed.xml") || fail "capital-probe-failed:after-debug-seed"
if ! python3 - "$SEEDED_CAPITAL" <<'PY'
import sys
raise SystemExit(0 if float(sys.argv[1]) >= 2500.0 else 1)
PY
then
  fail "debug-seed-not-applied:capital=$SEEDED_CAPITAL"
fi
echo "DEBUG_SMOKE_SEED_PASS=capital=$SEEDED_CAPITAL"
assert_ui_contains "LV 1" "after-debug-seed-level"

click_node "MANAGERS" "before-manager-hire"
assert_ui_contains "Maya" "manager-visible"
assert_ui_contains "READY TO HIRE" "manager-affordable"
click_node "HIRE" "before-manager-hire-action"
sleep 2
assert_ui_contains "HIRED" "after-manager-hire"
click_node "EMPIRE" "return-empire-after-manager"

# Capture two idle UI snapshots with no player input. A hired manager should mutate
# the rendered economy state while the app remains foregrounded.
dump_ui "manager-auto-before"
sleep 8
dump_ui "manager-auto-after"
python3 - "$EVIDENCE/manager-auto-before.xml" "$EVIDENCE/manager-auto-after.xml" <<'PY'
import sys,xml.etree.ElementTree as ET
def visible(path):
    out=[]
    for n in ET.parse(path).getroot().iter('node'):
        s=(n.attrib.get('text','')+' '+n.attrib.get('content-desc','')).strip()
        if s: out.append(s)
    return out
before,after=visible(sys.argv[1]),visible(sys.argv[2])
if before == after:
    print("MANAGER_AUTOMATION_FAIL=no-visible-economy-change", file=sys.stderr)
    raise SystemExit(2)
print("MANAGER_AUTOMATION_PASS=1")
PY

dump_ui "before-offline"
adb shell input keyevent KEYCODE_HOME
sleep 33
adb shell am start -W -n "$ACT" > "$EVIDENCE/offline-return.txt"
sleep 3
check_alive
# Preserve the post-offline empire state as evidence before navigating away and
# require a visible economy delta. This validates that the offline interval was
# actually applied instead of merely restoring the same persisted snapshot.
dump_ui "after-offline-empire"
python3 - "$EVIDENCE/before-offline.xml" "$EVIDENCE/after-offline-empire.xml" <<'PY'
import sys,xml.etree.ElementTree as ET
def visible(path):
    ignored=("empire","managers","upgrades","goals","store")
    out=[]
    for n in ET.parse(path).getroot().iter('node'):
        s=(n.attrib.get('text','')+' '+n.attrib.get('content-desc','')).strip()
        if s and s.lower() not in ignored:
            out.append(s)
    return out
before,after=visible(sys.argv[1]),visible(sys.argv[2])
if before == after:
    print("OFFLINE_ECONOMY_FAIL=no-visible-delta", file=sys.stderr)
    raise SystemExit(2)
print("OFFLINE_ECONOMY_PASS=1")
PY
click_node "MANAGERS" "offline-manager-tab"
assert_ui_contains "HIRED" "offline-manager-still-hired"
click_node "EMPIRE" "offline-return-empire"

click_node "STORE" "before-store"
assert_ui_contains "EMPIRE STORE" "store-open"
assert_ui_contains "RESTORE PURCHASES" "store-contents"
adb exec-out screencap -p > "$EVIDENCE/play-store-preview/05-store.png" || fail "screenshot-capture-failed:store"
test -s "$EVIDENCE/play-store-preview/05-store.png" || fail "empty-screenshot:store"
click_node "CLOSE" "store-before-close"
sleep 1
check_alive

adb shell input keyevent KEYCODE_HOME
sleep 2
adb shell am start -W -n "$ACT" > "$EVIDENCE/relaunch.txt"
sleep 3
check_alive
assert_ui_contains "EMPIRE" "after-relaunch"

adb shell am force-stop "$PKG"
sleep 1
adb shell am start -W -n "$ACT" > "$EVIDENCE/restart.txt"
sleep 3
check_alive
assert_ui_contains "EMPIRE" "after-force-stop-restart"
assert_ui_contains "LV 1" "after-force-stop-restart-level"
# Manager ownership is durable state too; verify it survives a hard process restart,
# not only the normal background/foreground lifecycle.
click_node "MANAGERS" "restart-manager-tab"
assert_ui_contains "HIRED" "after-force-stop-restart-manager"
click_node "EMPIRE" "restart-return-empire"

# Run a second short background/restart cycle to catch one-shot timestamp or
# persistence bugs that only appear after offline state has already been consumed.
dump_ui "cycle2-before"
adb shell input keyevent KEYCODE_HOME
sleep 5
adb shell am force-stop "$PKG"
adb shell am start -W -n "$ACT" > "$EVIDENCE/cycle2-restart.txt"
sleep 3
check_alive
assert_ui_contains "LV 1" "cycle2-level"
click_node "MANAGERS" "cycle2-manager-tab"
assert_ui_contains "HIRED" "cycle2-manager"
click_node "EMPIRE" "cycle2-return-empire"
dump_ui "cycle2-after"

sleep 35
check_alive

# Final durability checkpoint: force-stop after the autosave interval and require
# both purchased business and hired manager to survive. This specifically proves
# that the periodic save path commits durable state, rather than the test passing
# only because an earlier lifecycle callback happened to save it.
dump_ui "pre-autosave-restart"
adb shell am force-stop "$PKG"
sleep 1
adb shell am start -W -n "$ACT" > "$EVIDENCE/autosave-restart.txt"
sleep 3
check_alive
assert_ui_contains "LV 1" "autosave-restart-level"
click_node "MANAGERS" "autosave-restart-manager-tab"
assert_ui_contains "HIRED" "autosave-restart-manager"
click_node "EMPIRE" "autosave-restart-return-empire"
dump_ui "post-autosave-restart"

# The separate Character Review launcher entry exists in DEBUG builds only.
# Exercise it on a real emulator to ensure a phone-only user can inspect
# animation frames, pause and step, with screenshot evidence for review.
adb shell am start -W -n "$PKG/.CharacterReviewActivity" > "$EVIDENCE/character-review-launch.txt"
sleep 3
check_alive
assert_ui_contains "Animation QA" "character-qa-open"
assert_ui_contains "Pause" "character-qa-playing"
adb exec-out screencap -p > "$EVIDENCE/character-qa-playing.png"
click_node "Pause" "character-qa-before-pause"
assert_ui_contains "Lecture" "character-qa-paused"
click_node "+1" "character-qa-before-step"
assert_ui_contains "Lecture" "character-qa-stepped"
adb exec-out screencap -p > "$EVIDENCE/character-qa-stepped.png"
echo "CHARACTER_QA_EMULATOR_PASS=1"
# Starting MainActivity while the debug review activity is topmost may merely
# deliver the intent to the review task and leave the game hidden. Restart the
# app explicitly, then assert that the real game navigation is visible.
timeout -k 5s 25s adb shell am force-stop "$PKG" || fail "character-qa-force-stop-timeout"
timeout -k 5s 35s adb shell am start -W -n "$ACT" > "$EVIDENCE/character-qa-return-to-game.txt" || fail "character-qa-main-start-timeout"
sleep 3
check_alive
assert_ui_contains "MANAGERS" "character-qa-return-main"
# Guard the actual measurement scene, not merely the presence of navigation.
# A resumed overlay or wrong activity can expose a MANAGERS label while the
# city stage is absent, making frame and memory comparisons meaningless.
assert_ui_contains "Power Core" "performance-scene-core"
assert_ui_contains "CAPITAL" "performance-scene-capital"
echo "PERF_SCENE_VERIFIED=real-empire-city"

# Observational performance evidence: sample the real game (not the separate
# Character Review screen) during a repeatable, short navigation window.
# The software-rendered CI emulator cannot establish production-device FPS.
# ADB gfxinfo unavailability is reported as no_profiledata, never as zero jank.
if timeout -k 5s 25s adb shell dumpsys gfxinfo "$PKG" reset > "$EVIDENCE/gfxinfo-reset.txt" 2> "$EVIDENCE/gfxinfo-reset-error.txt"; then
  # A single two-swipe run yielded only 22 eligible frames on the hosted
  # software renderer. Repeat the same bounded gesture pair to collect a more
  # useful observational sample without changing the tested game state.
  for cycle in 1 2 3; do
    timeout -k 5s 20s adb shell input swipe 540 1300 540 700 400 || echo "PERF_CAPTURE_WARN=scroll-forward-failed cycle=$cycle"
    timeout -k 5s 20s adb shell input swipe 540 700 540 1300 400 || echo "PERF_CAPTURE_WARN=scroll-back-failed cycle=$cycle"
  done
  # Preserve the actual screen used for the performance sample. This lets
  # reviewers distinguish a valid city viewport from an unexpected overlay,
  # rather than trusting only an earlier accessibility hierarchy assertion.
  timeout -k 5s 25s adb exec-out screencap -p > "$EVIDENCE/performance-scene.png" || fail "performance-scene-screenshot-unavailable"
  sleep 5
  if ! timeout -k 5s 25s adb shell dumpsys gfxinfo "$PKG" framestats > "$EVIDENCE/gfxinfo-framestats.txt" 2> "$EVIDENCE/gfxinfo-error.txt"; then
    echo "PERF_CAPTURE_WARN=gfxinfo-unavailable"
  fi
else
  echo "PERF_CAPTURE_WARN=gfxinfo-reset-unavailable"
fi
check_alive
timeout -k 5s 25s adb shell dumpsys meminfo "$PKG" > "$EVIDENCE/meminfo.txt" || fail "final-meminfo-unavailable"
python3 "$SCRIPT_DIR/parse_emulator_performance.py" \
  --gfxinfo "$EVIDENCE/gfxinfo-framestats.txt" \
  --meminfo "$EVIDENCE/meminfo.txt" \
  --output "$EVIDENCE/performance-summary.json" || fail "performance-summary-failed"
timeout -k 5s 25s adb exec-out screencap -p > "$EVIDENCE/final.png" || fail "final-screenshot-unavailable"
timeout -k 5s 25s adb shell dumpsys activity activities > "$EVIDENCE/activity.txt" || fail "final-activity-dump-unavailable"
timeout -k 5s 25s adb shell dumpsys window windows > "$EVIDENCE/window.txt" || fail "final-window-dump-unavailable"
check_no_fatal
if grep -E "ANR in $PKG|am_anr.*$PKG" "$EVIDENCE/logcat.txt"; then
  fail "anr-detected"
fi
echo "FUNCTIONAL_POWER_CORE_TAP_PASS=1"
echo "FUNCTIONAL_MANAGER_AUTOMATION_PASS=1"
echo "FUNCTIONAL_OFFLINE_ECONOMY_PASS=1"
echo "FUNCTIONAL_RESTART_STATE_PASS=1"
echo "FUNCTIONAL_PERSISTENCE_PASS=1"
echo "FUNCTIONAL_AUTOSAVE_DURABILITY_PASS=1"
echo "FUNCTIONAL_SOAK_PASS=1"
echo "FUNCTIONAL_SMOKE_PASS=1"
```

## File: android/local_original_character_emulator_smoke.sh
```bash
#!/usr/bin/env bash
# Exercise the exact first-party review APK inside an isolated Android emulator.
# Never alters canonical sprite progress or installs a production-package APK.
set -euo pipefail
OUT=/tmp/zte-original-review-evidence
mkdir -p "$OUT"
APK="$(cat /tmp/zte-review-apk-path.txt)"
test -s "$APK"
case "$APK" in *.apk) ;; *) echo 'Expected review APK filename'; exit 1;; esac
adb wait-for-device
test "$(adb shell getprop sys.boot_completed | tr -d '\r')" = 1
adb install -r "$APK" | tee "$OUT/install.txt"
adb shell pm list packages | grep -F 'package:com.zerotoempire.game.originalreview'
# Must be a separate debug application, never replace production DataStore.
if adb shell pm list packages | grep -Fx 'package:com.zerotoempire.game'; then
  echo 'Note: production installation exists separately; not touched.'
fi
adb shell am start -W -n  'com.zerotoempire.game.originalreview/com.zerotoempire.game.CharacterReviewActivity'  | tee "$OUT/launch.txt"
sleep 5
adb shell pidof com.zerotoempire.game.originalreview | tee "$OUT/process-id.txt"
adb exec-out screencap -p > "$OUT/01-role-grid.png"
# Verify the entire scrollable gallery, not only OP + the beginning of
# TECH. Nine swipes expose LOG, ENG and the actual 39/42dp stage near the end.
for n in 2 3 4 5 6 7 8 9 10; do
  adb shell input swipe 290 690 290 220 380
  sleep 1
  printf -v file '%02d-stage-scroll.png' "$n"
  adb exec-out screencap -p > "$OUT/$file"
  adb shell pidof com.zerotoempire.game.originalreview >/dev/null
done

read_ui() {
  adb shell uiautomator dump /sdcard/local-original-stage.xml >/dev/null
  adb pull /sdcard/local-original-stage.xml "$OUT/ui-stage.xml" >/dev/null
}
scroll_to_button() {
  local label="$1" coords="" x="" y=""
  for attempt in $(seq 1 20); do
    read_ui
    if coords="$(python3 tools/android/local_review_ui_target.py "$OUT/ui-stage.xml" "$label")"; then
      printf '%s\n' "$coords"
      return 0
    fi
    if [ "$attempt" -le 4 ]; then
      adb shell input swipe 290 690 290 220 320
    else
      adb shell input swipe 290 260 290 810 320
    fi
    sleep 1
  done
  echo "Android stage control not visible: $label" >&2
  return 1
}
# Exercise the actual Android game-scale gallery rather than only its large
# thumbnails. ENGINEER is a selectable Compose button, not its static header.
coords="$(scroll_to_button ENGINEER)"
read -r tap_x tap_y <<< "$coords"
adb shell input tap "$tap_x" "$tap_y"
sleep 2
adb shell pidof com.zerotoempire.game.originalreview >/dev/null
# After role selection the panel may expand below the visible fold; demand
# that the REAL GAME SIZE preview is on-screen before taking screen evidence.
stage_visible=false
for attempt in $(seq 1 12); do
  read_ui
  if python3 tools/android/local_review_ui_target.py "$OUT/ui-stage.xml" 'NIGHT · 42 dp' --allow-static-label >/dev/null; then
    stage_visible=true
    break
  fi
  adb shell input swipe 290 700 290 280 340
  sleep 1
done
test "$stage_visible" = true || { echo 'ENGINEER 42dp preview never visible' >&2; exit 1; }
# A label alone can appear on screen while the 42dp rendered sprite is still
# clipped below the Android navigation bar. Advance the LazyColumn so the
# complete character actually occupies the visible screenshot.
adb shell input swipe 290 1040 290 530 360
sleep 2
read_ui
stage_coords="$(python3 tools/android/local_review_ui_target.py "$OUT/ui-stage.xml" 'NIGHT · 42 dp' --allow-static-label)"
read -r stage_x stage_y <<< "$stage_coords"
if [ "$stage_y" -ge 1280 ]; then
  echo "42dp sprite may still be clipped beneath the navigation bar: y=$stage_y" >&2
  exit 1
fi
adb exec-out screencap -p > "$OUT/11-engineer-game-scale.png"
# Every authored role/action must be selectable and render at gameplay size
# on the actual emulator. Gallery thumbnails alone cannot prove this.
# Capture all 24 combinations, not merely the default ENGINEER/WALK.
stage_count=0
for role in OPERATOR TECHNICIAN LOGISTICS ENGINEER; do
  role_coords="$(scroll_to_button "$role")"
  read -r role_x role_y <<< "$role_coords"
  adb shell input tap "$role_x" "$role_y"
  sleep 1
  for action in IDLE WALK WORK CARRY REPAIR CELEBRATE; do
    action_coords="$(scroll_to_button "$action")"
    read -r action_x action_y <<< "$action_coords"
    adb shell input tap "$action_x" "$action_y"
    sleep 1
    # The selected label is above the six action buttons. On compact
    # phones it can be offscreen after tapping REPAIR/CELEBRATE; scroll back
    # to the stage rather than misreporting a valid selection as a failure.
    selected_visible=false
    for attempt in $(seq 1 8); do
      read_ui
      if python3 tools/android/local_review_ui_target.py "$OUT/ui-stage.xml" \
          "$role · $action" --allow-static-label >/dev/null; then
        selected_visible=true
        break
      fi
      adb shell input swipe 290 270 290 590 300
      sleep 1
    done
    if [ "$selected_visible" != true ]; then
      echo "Android role/action selection failed: $role $action" >&2
      exit 1
    fi
    adb shell pidof com.zerotoempire.game.originalreview >/dev/null
    adb exec-out screencap -p > "$OUT/atlas-$role-$action.png"
    # A single animated screenshot cannot establish stride continuity. Capture
    # each of OP WALK's eight *actual Android-rendered* atlas frames via Compose
    # pause/step controls at the real 39/42dp game scales. This is a functional
    # emulator interaction, never a new unit test or semantic approval.
    if [ "$role" = OPERATOR ] && [ "$action" = WALK ]; then
      pause_coords="$(scroll_to_button 'Pause stage')"
      read -r pause_x pause_y <<< "$pause_coords"
      adb shell input tap "$pause_x" "$pause_y"
      sleep 1
      step_coords="$(scroll_to_button 'Stage +1')"
      read -r step_x step_y <<< "$step_coords"
      previous_frame=""
      : > "$OUT/op-walk-eight-frame-sequence.txt"
      for pose in 0 1 2 3 4 5 6 7; do
        read_ui
        # Require both real-size preview labels in the exact image viewport.
        python3 tools/android/local_review_ui_target.py "$OUT/ui-stage.xml" \
          'NIGHT · 42 dp' --allow-static-label >/dev/null
        python3 tools/android/local_review_ui_target.py "$OUT/ui-stage.xml" \
          'DAY · 39 dp' --allow-static-label >/dev/null
        frame="$(python3 - "$OUT/ui-stage.xml" <<'PY_FRAME'
import re,sys,xml.etree.ElementTree as ET
root=ET.parse(sys.argv[1]).getroot()
matches=[]
for node in root.iter('node'):
    label=(node.get('text') or node.get('content-desc') or '').strip()
    m=re.fullmatch(r'STAGE FRAME: (\d+)',label)
    if m: matches.append(int(m.group(1)))
if len(matches)!=1:
    raise SystemExit(f'Expected exactly one on-screen STAGE FRAME label: {matches}')
print(matches[0])
PY_FRAME
)"
        if [ -n "$previous_frame" ] && [ "$frame" -ne $(((previous_frame + 1) % 1680)) ]; then
          echo "OP WALK frame step failed: $previous_frame -> $frame" >&2
          exit 1
        fi
        printf '%s %s\n' "$pose" "$frame" >> "$OUT/op-walk-eight-frame-sequence.txt"
        printf -v image_name 'op-walk-frame-%02d.png' "$pose"
        adb exec-out screencap -p > "$OUT/$image_name"
        previous_frame="$frame"
        if [ "$pose" -lt 7 ]; then
          adb shell input tap "$step_x" "$step_y"
          sleep .35
        fi
      done
      # The next roles must keep animating; reset the original gallery state.
      play_coords="$(scroll_to_button 'Play stage')"
      read -r play_x play_y <<< "$play_coords"
      adb shell input tap "$play_x" "$play_y"
      echo 'LOCAL_ORIGINAL_OP_WALK_ALL_8_ANDROID_POSES_CAPTURED=1' \
        > "$OUT/op-walk-eight-frame-pass.txt"
    fi
    stage_count=$((stage_count + 1))
  done
done
# A previous emulator artifact (run 38788683514) proved that actor 0 could
# be completely frozen while scenery and traffic kept moving. The debug-only
# control is idempotent: resuming it here is mandatory before motion evidence.
resume_coords="$(scroll_to_button 'Resume city clock')"
read -r resume_x resume_y <<< "$resume_coords"
adb shell input tap "$resume_x" "$resume_y"
sleep .25
# The game-sized thumbnail is not the 620dp city layer. Physically scroll
# to the real city canvas and capture two *unpaused* frames inside its bounds.
# The debug-only semantic label makes this a reliable viewport check instead
# of treating a screenshot of an off-screen, empty stage as positive evidence.
role_coords="$(scroll_to_button OPERATOR)"
read -r role_x role_y <<< "$role_coords"
adb shell input tap "$role_x" "$role_y"
action_coords="$(scroll_to_button WALK)"
read -r action_x action_y <<< "$action_coords"
adb shell input tap "$action_x" "$action_y"
sleep 1
stage_bounds=""
for attempt in $(seq 1 8); do
  read_ui
  if stage_bounds="$(python3 - "$OUT/ui-stage.xml" <<'PY_STAGE'
import re,sys,xml.etree.ElementTree as ET
tree=ET.parse(sys.argv[1]).getroot()
for node in tree.iter('node'):
    name=(node.get('content-desc') or node.get('text') or '').strip()
    if name!='REVIEW GAMEPLAY STAGE':
        continue
    match=re.fullmatch(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]',node.get('bounds',''))
    if not match:
        continue
    left,top,right,bottom=map(int,match.groups())
    # Require the upper part of the stage inside the viewport; otherwise
    # its first 650 pixels may be empty space above the actual actors.
    if (right-left)>=500 and top<=600 and min(bottom,1800)-max(top,80)>=650:
        print(left,top,right,bottom)
        break
else:
    raise SystemExit(1)
PY_STAGE
)"; then
    break
  fi
  adb shell input swipe 290 1460 290 400 400
  sleep 1
done
if [ -z "$stage_bounds" ]; then
  echo "Actual city character layer never entered the Android viewport" >&2
  exit 1
fi
printf '%s\n' "$stage_bounds" > "$OUT/op-walk-city-stage-bounds.txt"
# Observe Android Compose state, not the movement of unrelated scenery.
# Uiautomator is intentionally required to read PLAY (not PAUSE) and the
# exact active worldFrame at both ends of the screenshot interval.
read_city_clock() {
  read_ui
  python3 - "$OUT/ui-stage.xml" <<'PY_CLOCK'
import re,sys,xml.etree.ElementTree as ET
root=ET.parse(sys.argv[1]).getroot()
matches=[]
for node in root.iter('node'):
    label=(node.get('text') or node.get('content-desc') or '').strip()
    m=re.fullmatch(r'CITY CLOCK: (\d+) · (PLAY|PAUSE)',label)
    if m: matches.append((int(m.group(1)),m.group(2)))
if len(matches)!=1 or matches[0][1]!='PLAY':
    raise SystemExit(f'City review clock is paused, obscured or ambiguous: {matches}')
print(matches[0][0])
PY_CLOCK
}
clock_before="$(read_city_clock)"
adb shell pidof com.zerotoempire.game.originalreview >/dev/null
adb exec-out screencap -p > "$OUT/op-walk-city-stage-night-00.png"
sleep .7
adb exec-out screencap -p > "$OUT/op-walk-city-stage-night-01.png"
clock_after="$(read_city_clock)"
clock_delta=$(((clock_after - clock_before + 1680) % 1680))
if [ "$clock_delta" -lt 1 ] || [ "$clock_delta" -ge 200 ]; then
  echo "City clock did not advance while OP WALK was captured: $clock_before -> $clock_after" >&2
  exit 1
fi
printf 'PLAY %s %s %s\n' "$clock_before" "$clock_after" "$clock_delta" > "$OUT/op-walk-city-clock-proof.txt"
echo "LOCAL_ORIGINAL_CITY_REVIEW_CLOCK_ADVANCED=$clock_delta"
# The uiautomator stage bounds are CLIPPED when the LazyColumn is scrolled.
# Never use fractions of those bounds to locate an actor. Instead, locate
# the precise Compose semantics of each real CharacterAtlasFrame after
# selecting OPERATOR/WALK, scrolling further to find the lower actor.
for actor in 0 1; do
  actor_bounds=""
  for attempt in $(seq 1 12); do
    read_ui
    if actor_bounds="$(python3 - "$OUT/ui-stage.xml" "$actor" <<'PY_ACTOR'
import re,sys,xml.etree.ElementTree as ET
root=ET.parse(sys.argv[1]).getroot()
name=f'REVIEW OPERATOR WALK ACTOR {sys.argv[2]}'
matching=[n for n in root.iter('node')
          if (n.get('content-desc') or n.get('text') or '').strip()==name]
if len(matching)!=1:
    raise SystemExit(1)
bounds=matching[0].get('bounds','')
m=re.fullmatch(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]',bounds)
if not m:
    raise SystemExit(1)
left,top,right,bottom=map(int,m.groups())
if right-left<75 or bottom-top<75 or top<85 or bottom>1800:
    raise SystemExit(1)
print(left,top,right,bottom)
PY_ACTOR
)"; then
      break
    fi
    adb shell input swipe 290 1490 290 810 385
    sleep 1
  done
  if [ -z "$actor_bounds" ]; then
    echo "OP WALK actor $actor was not fully visible in the city stage" >&2
    exit 1
  fi
  printf '%s\n' "$actor_bounds" > "$OUT/op-walk-city-actor-$actor-bounds.txt"
  adb shell pidof com.zerotoempire.game.originalreview >/dev/null
  # The WALK source loops every 8 frames at 10fps. A single 0.7s
  # gap plus screenshot overhead can accidentally sample the *same* pose
  # on both sides of the 0.8s loop. Three staggered samples make this
  # geometric aliasing observable rather than blaming a healthy renderer.
  for pose in 0 1 2; do
    printf -v shot 'op-walk-city-actor-%s-%02d.png' "$actor" "$pose"
    adb exec-out screencap -p > "$OUT/$shot"
    if [ "$pose" -lt 2 ]; then sleep .29; fi
  done
done
test "$stage_count" -eq 24
echo "LOCAL_ORIGINAL_ANDROID_ALL_24_ROLE_ACTIONS_RENDERED=$stage_count" \
  > "$OUT/24-stage-coverage.txt"
# UI XML improves diagnosis; screenshots and active process are hard gates.
if adb shell uiautomator dump /sdcard/local-original-qa.xml; then
  adb pull /sdcard/local-original-qa.xml "$OUT/ui-hierarchy.xml" || true
else
  echo 'Optional uiautomator XML unavailable' > "$OUT/ui-dump-warning.txt"
fi
python3 - <<'PY'
from pathlib import Path
from struct import unpack
root=Path('/tmp/zte-original-review-evidence')
shots=sorted(p for p in root.glob('*.png') if p.name[:2].isdigit())
if len(shots)!=11:
    raise SystemExit(f'Expected ten role gallery screenshots and one Android game-scale screenshot; got {len(shots)}')
for shot in shots:
    data=shot.read_bytes()
    if len(data)<10000 or not data.startswith(bytes.fromhex('89504e470d0a1a0a')):
        raise SystemExit(f'Empty/invalid emulator screenshot: {shot}')
    width,height=unpack('>II',data[16:24])
    if width<300 or height<500:
        raise SystemExit(f'Unexpected emulator image size: {shot}: {width}x{height}')
# Decode exact screenshot pixels only inside the real city stage bounds.
# A valid PNG header alone cannot demonstrate a visibly animating actor.
from PIL import Image,ImageChops
stage_bounds=[int(v) for v in (root/'op-walk-city-stage-bounds.txt').read_text().split()]
if len(stage_bounds)!=4:
    raise SystemExit(f'Invalid Android city stage bounding rectangle: {stage_bounds}')
stage_shots=[root/f'op-walk-city-stage-night-{n:02d}.png' for n in range(2)]
if not all(s.is_file() for s in stage_shots):
    raise SystemExit('Missing actual OP WALK city stage animation captures')
images=[Image.open(s).convert('RGB') for s in stage_shots]
viewport=(stage_bounds[0],max(stage_bounds[1],80),stage_bounds[2],
          min(stage_bounds[3],images[0].height-80))
if viewport[3]-viewport[1]<650 or viewport[2]-viewport[0]<500:
    raise SystemExit(f'Clipped city stage viewport: {viewport}')
first=images[0].crop(viewport)
second=images[1].crop(viewport)
change=ImageChops.difference(first,second).convert('L').point(
    lambda value: 255 if value>14 else 0
)
active=sum(count for level,count in enumerate(change.histogram()) if level>0)
if active<60:
    raise SystemExit(f'City game-size OP WALK sprites did not visibly animate: {active} changed pixels')
# The full-stage difference could come entirely from moving traffic.
# Inspect each actual actor's accessible, pixel-exact measured bounds instead.
# The second operator can be below the fold and is captured after scrolling.
for index in range(2):
    bounds_path=root/f'op-walk-city-actor-{index}-bounds.txt'
    rect=[int(v) for v in bounds_path.read_text().split()]
    if len(rect)!=4:
        raise SystemExit(f'Invalid bounds for city actor {index}: {rect}')
    shots=[Image.open(root/f'op-walk-city-actor-{index}-{n:02d}.png').convert('RGB')
           for n in range(3)]
    if any(image.size!=shots[0].size for image in shots):
        raise SystemExit(f'Inconsistent screenshots of actor {index}')
    l,t,r,b=rect
    if r-l<75 or b-t<75 or l<0 or t<85 or r>shots[0].width or b>shots[0].height-80:
        raise SystemExit(f'Actor {index} clipped or invalid: {rect}')
    # Evaluate two staggered frame intervals within the true actor bounds.
    # A fixed 0.7s interval could coincide with the exact 0.8s WALK loop,
    # creating a false static-actor verdict; the city clock must also pass
    # its explicit PLAY + frame-progression gate earlier in this script.
    roi=(max(0,l-14),max(80,t-14),min(shots[0].width,r+14),
         min(shots[0].height-80,b+14))
    differences=[]
    for previous,current in zip(shots,shots[1:]):
        delta=ImageChops.difference(previous.crop(roi),current.crop(roi))
        thresholded=delta.convert('L').point(lambda value: 255 if value>14 else 0)
        differences.append(sum(count for value,count in enumerate(thresholded.histogram())
                               if value>0))
    if max(differences)<50:
        raise SystemExit(f'No pixels moving inside OP WALK actor {index}: {differences}')
    print(f'LOCAL_ORIGINAL_OP_WALK_ACTOR_{index}_MOTION_PASS={differences}_CHANGED_PIXELS')
print(f'LOCAL_ORIGINAL_ANDROID_CITY_STAGE_REAL_ACTOR_MOTION_PASS={active}_CHANGED_PIXELS')
# The independent OP WALK capture must exercise eight distinct UI frame indices.
poses=sorted(root.glob('op-walk-frame-*.png'))
if len(poses)!=8:
    raise SystemExit(f'Expected eight stepped OP WALK screenshots, got {len(poses)}')
for shot in poses:
    data=shot.read_bytes()
    if len(data)<10000 or not data.startswith(bytes.fromhex('89504e470d0a1a0a')):
        raise SystemExit(f'Invalid frame-by-frame Android screenshot: {shot}')
proof=(root/'op-walk-eight-frame-sequence.txt').read_text().splitlines()
if len(proof)!=8:
    raise SystemExit(f'Expected eight OP WALK frame indexes: {proof}')
indexes=[int(row.split()[1])%8 for row in proof]
if len(set(indexes))!=8 or any((indexes[i]-indexes[i-1])%8!=1 for i in range(1,8)):
    raise SystemExit(f'OP WALK frames were skipped/duplicated: {indexes}')
print('OP_WALK_ANDROID_8_FRAME_REAL_SCALE_PROOF_PASS=1')
extra=sorted(root.glob('atlas-*.png'))
if len(extra)!=24:
    raise SystemExit(f'Expected 24 gameplay-size role/action screenshots, got {len(extra)}')
for shot in extra:
    data=shot.read_bytes()
    if len(data)<10000 or not data.startswith(bytes.fromhex('89504e470d0a1a0a')):
        raise SystemExit(f'Invalid Android role/action screenshot: {shot}')
print('LOCAL_ORIGINAL_EMULATOR_SCREENSHOT_HEADERS_PASS=35')
print('LOCAL_ORIGINAL_ROLE_ENGINEER_STAGE_OPENED=1')
PY
printf '%s\n' 'LOCAL_ORIGINAL_ANDROID_GALLERY_LAUNCHED=1'   'STRICT_DONE_UNCHANGED_BY_EMULATOR=1'   'EMULATOR_REVIEW_IS_NOT_SEMANTIC_APPROVAL=1'   > "$OUT/ANDROID_REVIEW_ONLY.txt"
```

## File: android/local_review_ui_target.py
```python
#!/usr/bin/env python3
"""Locate actual Android Compose accessibility controls in uiautomator XML.

Only a review helper; never touches production assets or grants approval.
Usage: python tools/android/local_review_ui_target.py hierarchy.xml "ENGINEER"
Prints: "x y" for adb shell input tap, exiting 1 if not visible/clickable.
"""
⋮----
BOUNDS = re.compile(r"^\[(\d+),(\d+)\]\[(\d+),(\d+)\]$")
⋮----
def find(xml_path: Path, label: str, clickable_only: bool = True) -> tuple[int, int] | None
⋮----
root = ET.parse(xml_path).getroot()
# A label may also appear in a static header. Only target real controls.
⋮----
actual = (node.attrib.get("text") or node.attrib.get("content-desc") or "").strip()
⋮----
parents = []
# uiautomator sometimes puts "clickable" on a parent Button/View.
direct = node.attrib.get("clickable") == "true"
⋮----
# A bound of a nested label is still actionable only if a parent
# Compose semantics node encloses it and is clickable.
⋮----
pb = BOUNDS.fullmatch(candidate.attrib.get("bounds", ""))
nb = BOUNDS.fullmatch(node.attrib.get("bounds", ""))
⋮----
match = BOUNDS.fullmatch(node.attrib.get("bounds", ""))
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
⋮----
coord = find(args.xml, args.label, not args.allow_static_label)
```

## File: android/parse_emulator_performance.py
```python
#!/usr/bin/env python3
"""Summarize observational Android gfxinfo framestats + meminfo CI evidence.

Does not enforce FPS thresholds: emulator timing is not production-device FPS.
Missing/malformed samples are explicitly marked unavailable, never reported as zero.
"""
⋮----
def percentile(sorted_values, fraction)
⋮----
index = (len(sorted_values) - 1) * fraction
lower = int(index)
upper = min(lower + 1, len(sorted_values) - 1)
⋮----
def read_frames(raw)
⋮----
in_profile = False
fields = None
durations_ms = []
discarded_rows = 0
excluded_flagged_rows = 0
profile_sections = 0
⋮----
line = line_text.strip()
⋮----
in_profile = not in_profile
⋮----
fields = {field.strip(): n for n, field in enumerate(line.split(','))}
⋮----
columns = line.split(',')
⋮----
flags = int(columns[fields['Flags']])
start = int(columns[fields['IntendedVsync']])
end = int(columns[fields['FrameCompleted']])
⋮----
# Android gfxinfo documents only Flags=0 as eligible for frame timings.
# Every nonzero flag denotes a special/outlier/skipped frame and must
# be excluded to avoid misleading tail percentiles.
⋮----
duration_ns = end - start
⋮----
count = len(durations_ms)
⋮----
# Fewer than 60 eligible frames is a warning about diagnostic sample
# size, not a rendering regression or a release-quality FPS gate.
⋮----
# A diagnostic 60 Hz threshold, NOT a device-calibrated jank metric.
⋮----
def read_total_pss_kb(raw)
⋮----
# Android changes meminfo layout across API levels. App Summary has
# `TOTAL: ...`; the detailed table has `TOTAL ...`; either is in KiB.
⋮----
match = re.search(pattern, raw, re.MULTILINE)
⋮----
def main()
⋮----
parser = argparse.ArgumentParser(description=__doc__)
⋮----
args = parser.parse_args()
gfx = args.gfxinfo.read_text(errors='replace') if args.gfxinfo.is_file() else ''
mem = args.meminfo.read_text(errors='replace') if args.meminfo.is_file() else ''
summary = {
```

## File: android/test_ui_click_target.py
```python
MODULE_PATH = pathlib.Path(__file__).with_name("ui_click_target.py")
spec = importlib.util.spec_from_file_location("ui_click_target", MODULE_PATH)
click_target = importlib.util.module_from_spec(spec)
⋮----
class ClickTargetTest(unittest.TestCase)
⋮----
def write_xml(self, body: str) -> pathlib.Path
⋮----
handle = tempfile.NamedTemporaryFile("w", suffix=".xml", delete=False)
⋮----
def test_avoids_non_clickable_label_overlay(self)
⋮----
path = self.write_xml(
⋮----
def test_uses_direct_clickable_match(self)
⋮----
path = self.write_xml('<node text="HIRE" clickable="true" bounds="[20,20][120,80]" />')
⋮----
def test_fails_without_matching_clickable(self)
⋮----
path = self.write_xml('<node text="POWER CORE +1" clickable="false" bounds="[30,10][90,60]" />')
```

## File: android/test_ui_dump_retry.py
```python
ROOT = pathlib.Path(__file__).resolve().parents[2]
HELPER = ROOT / "tools" / "android" / "ui_dump_retry.sh"
⋮----
class UiDumpRetryTest(unittest.TestCase)
⋮----
def make_fake_adb(self, directory: pathlib.Path, *, failures_before_success: int) -> tuple[pathlib.Path, pathlib.Path]
⋮----
state = directory / "attempts.txt"
⋮----
fake_bin = directory / "bin"
⋮----
adb = fake_bin / "adb"
⋮----
def run_helper(self, fake_bin: pathlib.Path, output: pathlib.Path, attempts: int) -> subprocess.CompletedProcess[str]
⋮----
env = os.environ.copy()
⋮----
command = f"source {HELPER!s}; ui_dump_with_retry {output!s}"
⋮----
def test_retries_transient_null_root_and_writes_fresh_xml(self)
⋮----
directory = pathlib.Path(tmp)
⋮----
output = directory / "window.xml"
⋮----
result = self.run_helper(fake_bin, output, attempts=3)
⋮----
def test_fails_after_bounded_retries_without_stale_output(self)
```

## File: android/test_ui_economy_probe.py
```python
MODULE_PATH = pathlib.Path(__file__).with_name("ui_economy_probe.py")
spec = importlib.util.spec_from_file_location("ui_economy_probe", MODULE_PATH)
probe = importlib.util.module_from_spec(spec)
⋮----
class EconomyProbeTest(unittest.TestCase)
⋮----
def write_xml(self, texts: list[str]) -> pathlib.Path
⋮----
handle = tempfile.NamedTemporaryFile("w", suffix=".xml", delete=False)
nodes = "".join(f'<node text="{text}" content-desc="" />' for text in texts)
⋮----
def test_reads_plain_capital(self)
⋮----
path = self.write_xml(["CAPITAL", "801", "+1/s"])
⋮----
def test_reads_compact_capital(self)
⋮----
path = self.write_xml(["CAPITAL", "2.50K", "+24/s"])
⋮----
def test_money_suffixes(self)
⋮----
def test_rejects_missing_capital(self)
⋮----
path = self.write_xml(["NET WORTH", "801"])
```

## File: android/ui_click_target.py
```python
#!/usr/bin/env python3
⋮----
_BOUNDS_RE = re.compile(r"^\[(\d+),(\d+)\]\[(\d+),(\d+)\]$")
⋮----
def _bounds(node)
⋮----
match = _BOUNDS_RE.match(node.attrib.get("bounds", ""))
⋮----
def _text(node) -> str
⋮----
def _center(rect)
⋮----
def _area(rect) -> int
⋮----
def _overlaps(a, b) -> bool
⋮----
def _contains(rect, point) -> bool
⋮----
def _safe_point(clickable, overlays)
⋮----
fractions = (0.5, 0.05, 0.95, 0.15, 0.85)
points = [
⋮----
def find_click_target(path: pathlib.Path | str, needle: str) -> tuple[int, int]
⋮----
root = ET.parse(path).getroot()
needle_l = needle.lower()
nodes = list(root.iter("node"))
matches = [
⋮----
direct = [(node, rect) for node, rect in matches if node.attrib.get("clickable") == "true"]
⋮----
overlays = [rect for _, rect in matches]
nearby = []
⋮----
rect = _bounds(node)
⋮----
def main(argv: list[str]) -> int
```

## File: android/ui_dump_retry.sh
```bash
#!/usr/bin/env bash

ui_dump_with_retry() {
  local output="${1:?output path required}"
  local remote="${UI_DUMP_REMOTE_PATH:-/sdcard/window.xml}"
  local attempts="${UI_DUMP_ATTEMPTS:-5}"
  local delay_seconds="${UI_DUMP_RETRY_DELAY_SECONDS:-1}"
  local attempt=1
  local log="${output}.uiautomator.log"
  local command_timeout="${UI_DUMP_COMMAND_TIMEOUT_SECONDS:-35}"

  rm -f "$output" "$log"
  while (( attempt <= attempts )); do
    rm -f "$output"
    adb shell rm -f "$remote" >/dev/null 2>&1 || true

    if timeout "${command_timeout}s" adb shell uiautomator dump "$remote" >"$log" 2>&1; then
      # adb pull intermittently fails on slow API-35 CI emulators even after
      # uiautomator has successfully written the remote hierarchy.
      timeout "${command_timeout}s" adb exec-out cat "$remote" > "$output" 2>/dev/null || true
      if ! grep -q '</hierarchy>' "$output" 2>/dev/null; then
        timeout "${command_timeout}s" adb pull "$remote" "$output" >/dev/null 2>&1 || true
      fi
      if grep -q '</hierarchy>' "$output" 2>/dev/null; then
        rm -f "$log"
        return 0
      fi
    fi

    rm -f "$output"
    if (( attempt < attempts )); then
      sleep "$delay_seconds"
    fi
    attempt=$((attempt + 1))
  done

  echo "UI_DUMP_FAILED attempts=$attempts timeout_seconds=$command_timeout output=$output" >&2
  if [[ -s "$log" ]]; then
    cat "$log" >&2
  fi
  return 1
}
```

## File: android/ui_economy_probe.py
```python
#!/usr/bin/env python3
⋮----
_SUFFIXES = {
_MONEY_RE = re.compile(r"^\s*([0-9]+(?:\.[0-9]+)?)\s*(Qa|Qi|Sx|Sp|[KMBTON])?\s*$")
⋮----
def parse_money(text: str) -> float
⋮----
match = _MONEY_RE.match(text)
⋮----
def read_capital(path: pathlib.Path | str) -> float
⋮----
texts: list[str] = []
⋮----
text = node.attrib.get("text", "").strip()
⋮----
def main(argv: list[str]) -> int
```

## File: android/validate_manifest_policy.py
```python
#!/usr/bin/env python3
⋮----
path = sys.argv[1] if len(sys.argv) > 1 else "app/src/main/AndroidManifest.xml"
root = ET.parse(path).getroot()
A = "{http://schemas.android.com/apk/res/android}"
permissions = {n.get(A+"name") for n in root.findall("uses-permission")}
allowed = {"android.permission.INTERNET", "android.permission.ACCESS_NETWORK_STATE"}
unexpected = sorted(p for p in permissions if p and p not in allowed)
missing = sorted(allowed - permissions)
⋮----
app = root.find("application")
⋮----
activities = app.findall("activity")
launchers = []
⋮----
actions={x.get(A+"name") for x in intent.findall("action")}
cats={x.get(A+"name") for x in intent.findall("category")}
⋮----
# Backup is intentionally allowlisted to the single gameplay save file. Keep
# analytics/consent/commerce state out of cloud backup and device transfer.
⋮----
backup = ET.parse("app/src/main/res/xml/backup_rules.xml").getroot()
legacy = {(n.get("domain"), n.get("path")) for n in backup.findall("include")}
expected = {("file", "datastore/zero_empire_save_v2.preferences_pb")}
⋮----
extract = ET.parse("app/src/main/res/xml/data_extraction_rules.xml").getroot()
⋮----
node = extract.find(section)
⋮----
actual = {(n.get("domain"), n.get("path")) for n in node.findall("include")}
```

## File: android/validate_release_privacy.py
```python
#!/usr/bin/env python3
⋮----
ROOT = Path(__file__).resolve().parents[2]
⋮----
BUILD = ROOT / "app/build.gradle.kts"
COMMERCE = ROOT / "app/src/main/java/com/zerotoempire/game/CommerceUi.kt"
IN_APP_POLICY = ROOT / "app/src/main/java/com/zerotoempire/game/PrivacyPolicy.kt"
PUBLIC_POLICY = ROOT / "marketing/privacy-policy.md"
DATA_SAFETY = ROOT / "marketing/data-safety.md"
STORE_LISTING = ROOT / "marketing/play-store-listing.md"
⋮----
required_files = [BUILD, COMMERCE, IN_APP_POLICY, PUBLIC_POLICY, DATA_SAFETY, STORE_LISTING]
missing = [str(path.relative_to(ROOT)) for path in required_files if not path.is_file()]
⋮----
build = BUILD.read_text(encoding="utf-8")
commerce = COMMERCE.read_text(encoding="utf-8")
in_app = IN_APP_POLICY.read_text(encoding="utf-8")
public = PUBLIC_POLICY.read_text(encoding="utf-8")
data_safety = DATA_SAFETY.read_text(encoding="utf-8")
listing = STORE_LISTING.read_text(encoding="utf-8")
⋮----
sensitive_prefixes = (
⋮----
dependencies = re.findall(r'implementation\("([^"]+)"\)', build)
sensitive_dependencies = sorted(
⋮----
required_public_headings = (
⋮----
required_in_app_terms = (
```

## File: sprites/tests/test_archive_character_candidates.py
```python
#!/usr/bin/env python3
"""Offline candidate archive tests; no cloud/GPU credentials required."""
⋮----
class CandidateArchiveTests(unittest.TestCase)
⋮----
def setUp(self)
⋮----
def write_file(self, name, payload=None)
⋮----
target = self.root / "output" / "candidates" / name
⋮----
def write_qa(self, rows)
⋮----
def test_saves_only_real_qa_passing_candidates_with_hashes(self)
⋮----
passing = "zte_chr_op_celeb_final.png"
failing = "zte_chr_log_work_final.png"
⋮----
manifest = archive_candidates(self.root, self.bundle, 38815707999)
⋮----
def test_missing_passing_image_fails_closed(self)
⋮----
def test_invalid_signature_fails_closed(self)
⋮----
def test_duplicate_qa_rows_fail_closed(self)
⋮----
name = "zte_chr_op_walk_final.png"
⋮----
def write_clean_reject_evidence(self, statuses=None, generated=None)
⋮----
rows = statuses if statuses is not None else [
⋮----
def test_real_all_reject_collector_without_frame_qa_is_not_workflow_failure(self)
⋮----
# 38831389791: generated-targets.json count=0, three rejected
# character-sheet-report.json entries and NO github-qa-report.json.
⋮----
manifest = archive_candidates(self.root, self.bundle, 38831389791)
⋮----
def test_missing_frame_qa_with_png_fails_closed_even_if_rejects_claimed(self)
⋮----
def test_missing_frame_qa_without_rejection_proof_fails_closed(self)
⋮----
def test_malformed_all_rejected_proof_cannot_silently_skip_archive(self)
⋮----
invalid = [
⋮----
def test_missing_qa_reject_requires_zero_produced_target_manifest(self)
⋮----
def test_rejected_only_writes_no_release_asset(self)
⋮----
manifest = archive_candidates(self.root, self.bundle, 123)
```

## File: sprites/tests/test_asset_production_policy.py
```python
#!/usr/bin/env python3
"""Fast, dependency-free regression checks for asset production admission."""
⋮----
class ProductionFirstTests(unittest.TestCase)
⋮----
def test_relaxed_motion_admits_previous_static_rejections(self)
⋮----
def test_strict_floors_unchanged(self)
⋮----
def test_art_warnings_do_not_block_candidate(self)
⋮----
risk = {"risk_level": "BLOCKING", "flags": [
⋮----
def test_new_repair_algorithm_reopens_only_a_bounded_epoch(self)
⋮----
# The actual CHR-ENG-REPAIR master record had four rejected attempts
# in v1.21; an explicit new repair rig can receive another bounded
# attempt without deleting the old rejection/evidence history.
candidate = {
⋮----
dispatched = mark_dispatch({"assets": [candidate]},
⋮----
# A produced candidate must not be regenerated just because
# strict semantic review is still pending.
⋮----
def test_structural_risks_remain_blocking(self)
⋮----
def test_unknown_risk_is_not_silently_waived(self)
⋮----
risk = {"risk_level": "BLOCKING", "flags": ["NEW_TECHNICAL_RISK"]}
```

## File: sprites/tests/test_character_bank_mobile_review.py
```python
"""Offline visual review generator regressions, no Android/GPU/network needed."""
⋮----
class MobileCandidateReviewTests(unittest.TestCase)
⋮----
def setUp(self)
⋮----
rows = []
qa = []
counts = {"IDLE": 6, "WALK": 8, "WORK": 10,
⋮----
aid = f"CHR-{role}-{action}"
⋮----
frame = Image.new("RGBA",(1024,1024),(0,0,0,0))
painter = ImageDraw.Draw(frame)
⋮----
output = io.BytesIO()
⋮----
def save_bank(self)
⋮----
def test_mobile_review_embeds_verified_selected_and_original(self)
⋮----
d=build(self.bank,self.original,self.html)
⋮----
html=self.html.read_text()
⋮----
def test_mobile_review_includes_verified_motion_flags(self)
⋮----
audit = self.root / "motion-audit.json"
⋮----
html = self.html.read_text()
⋮----
def test_stale_motion_audit_must_not_be_misattached_to_new_png(self)
⋮----
audit = self.root / "stale-audit.json"
⋮----
def test_hash_tampering_fails_closed(self)
⋮----
def test_invalid_local_frame_geometry_fails_closed(self)
⋮----
def test_script_closing_in_review_flags_is_html_escaped(self)
⋮----
def test_unapproved_bank_is_required(self)
```

## File: sprites/tests/test_character_bank_motion_audit.py
```python
"""Regression tests: mobile motion warnings must never approve candidate artwork."""
⋮----
class MobileMotionAuditTests(unittest.TestCase)
⋮----
def setUp(self)
⋮----
def png(self, *, moving=False)
⋮----
atlas = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
brush = ImageDraw.Draw(atlas)
⋮----
move = (i % 2) * 45 if moving else 0
⋮----
buffer = io.BytesIO()
⋮----
def write_bank(self, *, moving=False, digest=None, approve=False)
⋮----
blob = self.png(moving=moving)
entry = {
data = dict(self.metadata, bank_entries=[entry])
⋮----
def test_still_work_requires_attention_but_is_not_automatically_approved(self)
⋮----
result = analyze(self.bank, self.report)
⋮----
item = result["assets"][0]
⋮----
def test_distinct_poses_have_higher_observable_motion(self)
⋮----
moved = analyze(self.bank, self.report)
⋮----
def write_pair(self, *, alternate_color=(8, 100, 160))
⋮----
def sprite(role, action, count, color)
⋮----
atlas = Image.new("RGBA", (1024, 1024))
pen = ImageDraw.Draw(atlas)
⋮----
out = io.BytesIO()
⋮----
filename = f"zte_chr_eng_{action.lower()}_final.png"
blob = sprite("ENG", action, count, color)
⋮----
data = dict(self.metadata, candidate_count=2, bank_entries=entries)
⋮----
def test_different_engineer_helmet_style_is_flagged_without_promotion(self)
⋮----
report = analyze(self.bank, self.report)
⋮----
work = next(row for row in report["assets"]
⋮----
def test_matching_engineer_head_is_not_falsely_flagged(self)
⋮----
def test_missing_or_empty_head_cannot_silently_pass_audit(self)
⋮----
index = json.loads(archive.read("candidate-bank-index.json"))
sprites = {row["filename"]: archive.read("candidates/" + row["filename"])
⋮----
empty = buffer.getvalue()
name = "zte_chr_eng_idle_final.png"
⋮----
def test_sha_mismatch_fails_closed(self)
⋮----
def test_strict_approved_metadata_fails_closed(self)
⋮----
def test_report_requires_review_only_bank(self)
⋮----
data = {name: existing.read(name) for name in existing.namelist()}
meta = json.loads(data["candidate-bank-index.json"])
```

## File: sprites/tests/test_character_candidate_bank.py
```python
"""Offline regressions for durable character bank; no GPU/network required."""
⋮----
class CharacterBankTests(unittest.TestCase)
⋮----
def setUp(self)
⋮----
def save_master(self)
⋮----
def png(self)
⋮----
picture = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
⋮----
buffer = io.BytesIO()
⋮----
def source(self, content=None, run_id=123, name=None, sha=None)
⋮----
content = content if content is not None else self.png()
name = name or self.filename
sha = sha if sha is not None else hashlib.sha256(content).hexdigest()
path = self.archives / f"zte-characters-{run_id}.zip"
index = {
⋮----
def test_complete_pack_contains_exact_verified_candidate_and_deferred_warnings(self)
⋮----
report = assemble(self.master, self.archives, self.output)
⋮----
saved = json.loads(z.read("candidate-bank-index.json"))
entry = saved["bank_entries"][0]
⋮----
def test_missing_source_does_not_inflate_progress(self)
⋮----
def test_dispatched_asset_not_counted_even_with_old_artifact(self)
⋮----
result = assemble(self.master, self.archives, self.output)
⋮----
def test_wrong_source_id_is_never_accepted(self)
⋮----
def test_mismatched_sha_fails_closed(self)
⋮----
def test_wrong_dimensions_fail_closed(self)
⋮----
buf = io.BytesIO()
⋮----
def authored_original(self)
⋮----
original = self.root / "original"
⋮----
manifest = []
qa = []
counts = {"IDLE": 6, "WALK": 8, "WORK": 10,
⋮----
asset_id = f"CHR-{role}-{action}"
⋮----
x = (i % 4) * 256
y = (i // 4) * 256
⋮----
def test_local_original_completes_candidate_scope_while_remote_is_dispatched(self)
⋮----
local = self.authored_original()
⋮----
master_before = self.master.read_bytes()
report = assemble(self.master, self.archives, self.output, local_original=local)
⋮----
entry = report["bank_entries"][0]
⋮----
def test_prefer_real_collected_candidate_to_local_original(self)
⋮----
def complete_eng_original(self)
⋮----
original = self.authored_original()
counts = {"IDLE": 6, "WORK": 10, "CARRY": 8,
⋮----
atlas = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
folder = original / "src_svg" / "ENG" / action
⋮----
def test_explicit_engineer_cohort_creates_separate_six_action_review_bank(self)
⋮----
local = self.complete_eng_original()
⋮----
normal_path = self.root / "canonical.zip"
normal = assemble(self.master, self.archives, normal_path,
⋮----
original_master = self.master.read_bytes()
preferred = assemble(
⋮----
name = f"zte_chr_eng_{action.lower()}_final.png"
⋮----
def test_engineer_coherent_option_rejects_incomplete_role_or_missing_source(self)
⋮----
def test_local_manifest_claims_do_not_waive_technical_frame_QA(self)
⋮----
def test_local_original_requires_all_editable_svg_frames(self)
⋮----
def test_local_original_fails_closed_when_qa_claims_artistic_approval(self)
⋮----
qa_file = local / "candidate-qa.json"
data = json.loads(qa_file.read_text())
```

## File: sprites/tests/test_character_identity_polish_mobile_review.py
```python
"""The offline identity viewer is an export-only review surface, not a publisher."""
⋮----
class MobileIdentityReviewTests(unittest.TestCase)
⋮----
def setUp(self)
⋮----
temp = tempfile.TemporaryDirectory()
⋮----
def test_self_contained_readable_and_no_runtime_promotion(self)
⋮----
result = write_mobile_review([self.row], self.file, 219)
⋮----
html = self.file.read_text(encoding="utf-8")
⋮----
def test_injection_attempt_in_label_is_encoded_before_script(self)
⋮----
changed = dict(self.row, id="CHR-ENG-WALK</script><script>alert(1)</script>")
⋮----
def test_duplicate_ids_and_invalid_frame_counts_block_output(self)
⋮----
def test_invalid_strict_done_not_misrepresented(self)
⋮----
def test_zero_safe_alternatives_displays_no_fake_candidate(self)
⋮----
result = write_mobile_review([], self.file, 219)
```

## File: sprites/tests/test_character_identity_polish.py
```python
"""Protect deterministic role face/helmet retouch proposals from silent approvals."""
⋮----
class CharacterIdentityPolishTests(unittest.TestCase)
⋮----
def setUp(self)
⋮----
temp = tempfile.TemporaryDirectory()
⋮----
atlas = Image.new("RGBA", (1024, 1024))
⋮----
frame = Image.new("RGBA", (256, 256))
artist = ImageDraw.Draw(frame)
⋮----
out = io.BytesIO()
⋮----
def write_atlases(self, *, same_head=False, bad_frame=None)
⋮----
reference_color = (252, 122, 14)
diverged_color = reference_color if same_head else (8, 180, 233)
data = [
⋮----
fname = "zte_chr_" + aid.split("-")[1].lower() + "_" + aid.split("-")[2].lower() + "_final.png"
blob = self.atlas(count, col, damage)
⋮----
def save(self)
⋮----
def test_proposes_complete_review_only_identity_retouch(self)
⋮----
result = build(self.bank, self.audit, self.output, self.report, self.comparison,
⋮----
row = result["alternatives"][0]
⋮----
blob = packed.read(row["path"])
⋮----
original = Image.open(io.BytesIO(self.blobs["zte_chr_op_work_final.png"]))
# The change is strictly restricted to head/neck; legs and
# lower torso of EVERY frame remain pixel-exact.
⋮----
a = original.crop(((i % 4) * 256, (i // 4) * 256 + 126,
b = sprite.crop(((i % 4) * 256, (i // 4) * 256 + 126,
⋮----
html = self.mobile.read_text(encoding="utf-8")
⋮----
def test_one_unsafe_pose_rejects_entire_proposal_not_just_one_frame(self)
⋮----
result = build(self.bank, self.audit, self.output, self.report,
⋮----
def test_mobile_motion_regression_rejects_entire_retouch(self)
⋮----
original = module.motion_stats
calls = [0]
⋮----
def deteriorated_second_atlas(blob, count)
⋮----
result = original(blob, count)
⋮----
report = build(self.bank, self.audit, self.output, self.report)
⋮----
def test_consistent_actions_are_not_needlessly_modified(self)
⋮----
result = build(self.bank, self.audit, self.output, self.report)
⋮----
def test_invalid_candidate_sha_fails_closed(self)
⋮----
def test_audit_reference_is_same_role_verified_and_not_forged(self)
⋮----
data = json.loads(self.audit.read_text())
row = next(x for x in data["assets"] if x["id"] == "CHR-OP-WORK")
⋮----
def test_audit_metric_cannot_be_forged_to_force_proposal(self)
⋮----
def test_forged_same_role_anchor_is_rejected(self)
⋮----
def test_self_anchor_cannot_claim_identity_warning(self)
⋮----
row = next(x for x in data["assets"] if x["id"] == "CHR-OP-WALK")
⋮----
def test_no_auto_promotion_even_when_source_falsely_claims_approval(self)
```

## File: sprites/tests/test_character_mobile_motion_storyboard.py
```python
"""42px gameplay storyboard is a provenance-verified review aid."""
⋮----
class GameplayMotionStoryboardTests(unittest.TestCase)
⋮----
save = RoleConsistencySheetTests.save
⋮----
def setUp(self)
⋮----
# Reuse synthetic OP/LOG/ENG candidate bank with SHA-matched audit.
⋮----
def test_frames_include_first_middle_and_loop_seam(self)
⋮----
def test_42px_both_lighting_conditions_and_no_promotion(self)
⋮----
report = build(self.bank, self.audit, self.output)
⋮----
def test_corrupt_audit_rejected_without_creating_output(self)
⋮----
data = json.loads(self.audit.read_text())
⋮----
def test_automatic_approval_forbidden(self)
```

## File: sprites/tests/test_character_provisional_idle_seed.py
```python
"""Engineer IDLE anchoring: provenance/technical-pass ONLY, never strict DONE."""
⋮----
class ProvisionalEngineerSeedTests(unittest.TestCase)
⋮----
def setUp(self)
⋮----
atlas = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
draw = ImageDraw.Draw(atlas)
⋮----
buffer = io.BytesIO()
⋮----
def save_state(self)
⋮----
def write_archive(self, *, run=38825860064, rows=None, approved=False)
⋮----
index = {
⋮----
def test_actual_review_only_seed_is_pinned_and_usable_as_visual_reference(self)
⋮----
meta = prepare(self.master, self.queue, self.archive, self.shipped, 38825860064)
⋮----
def test_prevent_wrong_collector_provenance_even_if_name_is_correct(self)
⋮----
def test_review_status_may_not_be_strict_done(self)
⋮----
def test_tampered_archived_bytes_cannot_supply_identity(self)
⋮----
def test_source_cannot_claim_semantic_approval(self)
⋮----
def test_no_identity_reference_if_source_image_is_corrupt(self)
⋮----
def test_modified_seed_is_rejected_at_kaggle_runtime(self)
⋮----
def test_missing_provisional_overlay_returns_no_seed_not_approval(self)
⋮----
def test_never_accept_unrequested_engineer_seed(self)
```

## File: sprites/tests/test_character_repair_pose_plan.py
```python
"""Repair animation should move the hands, not teleport the whole subject."""
⋮----
class RepairRigContinuityTests(unittest.TestCase)
⋮----
def test_full_ten_frame_cycle_retains_one_planted_foot_pivot(self)
⋮----
def test_strengths_are_bounded_and_allow_articulation(self)
⋮----
values = []
⋮----
strength = repair_strength(i, attempt, mode)
⋮----
def test_invalid_attempts_cannot_bypass_bounded_policy(self)
⋮----
def test_generator_uses_plan_and_preserves_original_qa_gates(self)
⋮----
generator = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text()
mass = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text()
kernel = Path("kaggle/github_mass_factory.py").read_text()
```

## File: sprites/tests/test_character_role_contact_sheet.py
```python
"""PNG contact sheet is an SHA-verified manual review aid, never promotion."""
⋮----
class RoleConsistencySheetTests(unittest.TestCase)
⋮----
def setUp(self)
⋮----
action = "WALK" if role != "ENG" else "IDLE"
asset_id = f"CHR-{role}-{action}"
filename = f"zte_chr_{role.lower()}_{action.lower()}_final.png"
atlas = Image.new("RGBA", (1024, 1024))
artist = ImageDraw.Draw(atlas)
⋮----
memory = io.BytesIO()
⋮----
blob = memory.getvalue()
⋮----
checksum = hashlib.sha256(blob).hexdigest()
⋮----
def save(self)
⋮----
def test_role_sheet_is_readable_png_and_does_not_approve_candidates(self)
⋮----
report = build(self.bank, self.audit, self.output)
⋮----
def test_sha_tampering_of_png_or_audit_fails_closed(self)
⋮----
def test_missing_audit_coverage_is_not_silently_ignored(self)
⋮----
def test_semantically_approved_candidate_or_audit_must_be_rejected(self)
⋮----
def test_cross_role_reference_fails_even_with_valid_sha(self)
⋮----
def test_forged_reference_distance_and_self_flags_fail_closed(self)
⋮----
def test_empty_first_frame_is_blocking_even_with_valid_hash(self)
⋮----
filename = self.entries[0]["filename"]
⋮----
digest = hashlib.sha256(self.blobs[filename]).hexdigest()
```

## File: sprites/action_contact.py
```python
"""Deterministic 512px rig-space interaction targets for TECH WORK and REPAIR.

No prompt-by-frame regeneration, remote model calls, or automatic art approval.
"""
⋮----
WORK_SCREEN_LOCAL = (34.0, -75.0, 107.0, -41.0)
REPAIR_TIP_LOCAL = (94.0, -72.0)
⋮----
def work_hands(t: float, root: tuple[float, float])
⋮----
"""Independent cyclic touch trajectories constrained to one screen."""
⋮----
phase = 2 * math.pi * (t % 1.0)
⋮----
def screen_bounds(root)
⋮----
def work_contact(p: dict) -> dict
⋮----
bounds = screen_bounds(p['root'])
def within(hand)
⋮----
def work_pulse(t: float) -> float
⋮----
"""Phase-locked emissive touch feedback, never random pixels."""
⋮----
def work_event_indices(frames: int, phase_origin_frame: int = 0) -> tuple[int, ...]
⋮----
"""Map WORK data-update events to visible glow maxima *after* cycle reindex.

    The asset builder and runtime sound/VFX timeline must share the same
    frame-phase mapping. Never fire an event during a visible pulse minimum.
    """
⋮----
result = []
⋮----
phase = lambda j: ((j + phase_origin_frame) % frames) / frames
now = work_pulse(phase(i))
before = work_pulse(phase(i-1))
after = work_pulse(phase(i+1))
⋮----
def repair_tip(root)
⋮----
def repair_contact(p: dict) -> dict
⋮----
distance = math.dist(p['handR'], repair_tip(p['root']))
⋮----
def repair_spark_intensity(t: float) -> float
⋮----
strength = max(0., math.sin(2 * math.pi * (t % 1.0)))
```

## File: sprites/animation_batch_planner.py
```python
#!/usr/bin/env python3
"""Plan unresolved animation assets from the authoritative 235-target queue.

This planner is READ-ONLY. It explicitly separates art generation from human
semantic review; an installed runtime sheet is not proof of strict DONE.
Frame sizes/counts match the actual Android runtime contracts, not aspirational
older production notes.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
MASTER = ROOT / "art/production/master-asset-queue.json"
INCOMING = ROOT / "art/incoming/final-sprites"
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
MAX_BATCH = 16
⋮----
# Canonical sources: process_final_sprites.py, CanonicalCharacterRaster.kt.
CHR_FRAMES = {
MCH_FRAMES = 8
⋮----
def frame_contract(asset_id: str) -> tuple[int, int, int, int, str]
⋮----
action = asset_id.rsplit("-", 1)[-1]
frames = CHR_FRAMES[action]
⋮----
frames = MCH_FRAMES
⋮----
def task_for(pipeline_status: str) -> str
⋮----
def items(kind: str, root: Path = ROOT) -> list[dict]
⋮----
master = json.loads((root / MASTER.relative_to(ROOT)).read_text(encoding="utf-8"))
assets = master.get("assets", [])
⋮----
by_id = {a["id"]: a for a in assets}
⋮----
planned: list[dict] = []
manifest_ids: set[str] = set()
⋮----
match = ROW.match(line)
⋮----
family = "CHR" if asset_id.startswith("CHR-") else "MCH" if asset_id.startswith("MCH-") else None
⋮----
record = by_id.get(asset_id)
⋮----
stem = Path(runtime).stem
candidate = root / INCOMING.relative_to(ROOT) / (stem + ".png")
runtime_path = root / runtime
pipeline_status = str(record.get("pipeline_status") or "")
⋮----
# Exactly the two historically rejected candidates should lead the repair
# queue; AWAITING_REVIEW items need human review, not another blind GPU run.
priority = {"regenerate": 0, "semantic-review": 1, "generate": 2}
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
⋮----
all_items = items(args.kind)
selected = all_items[:args.count]
```

## File: sprites/archive_character_candidates.py
```python
#!/usr/bin/env python3
"""Archive QA-passing character *candidates*, never strict runtime assets.

Input must be an artifact downloaded from a trusted completed collector run.
Only the actual PNG bytes present on disk and marked pass by the technical QA
are copied. Art warnings and exact SHA-256 hashes survive beyond artifact TTL.
"""
⋮----
NAME = re.compile(r"zte_chr_(?:op|tech|log|eng)_(?:idle|walk|work|carry|repair|celeb)_final\.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_PNG_BYTES = 100 * 1024 * 1024
MAX_ARCHIVE_BYTES = 500 * 1024 * 1024
⋮----
def archive_candidates(source: Path, destination: Path, source_run_id: int) -> dict
⋮----
qa_files = list(source.rglob("github-qa-report.json"))
⋮----
# A successful collector can observe a genuinely clean, all-rejected
# Kaggle batch. In that case it deliberately never ran frame QA:
# there were no candidate PNGs to inspect. Reject this exception
# unless the actual producer report proves every attempted target was
# rejected AND the output manifest confirms zero produced sprites.
# Never silently treat a missing QA report with real PNGs as success.
⋮----
producer_reports = list(source.rglob("character-sheet-report.json"))
generated_manifests = list(source.rglob("generated-targets.json"))
⋮----
producer_rows = json.loads(producer_reports[0].read_text(encoding="utf-8"))
generated = json.loads(generated_manifests[0].read_text(encoding="utf-8"))
⋮----
names = [str(r.get("id") or "") for r in producer_rows if isinstance(r, dict)]
⋮----
qa = json.loads(qa_files[0].read_text(encoding="utf-8"))
rows = qa.get("assets") if isinstance(qa, dict) else None
⋮----
accepted: list[tuple[Path, dict]] = []
seen: set[str] = set()
total_bytes = 0
⋮----
name = Path(str(row.get("file") or "")).name
⋮----
found = [p for p in source.rglob(name) if p.parent.name == "candidates" and p.is_file()]
⋮----
path = found[0]
size = path.stat().st_size
⋮----
manifest = {
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
manifest = archive_candidates(args.source, args.output, args.source_run_id)
```

## File: sprites/asset_queue_utils.py
```python
#!/usr/bin/env python3
"""Shared state helpers for the 235-asset autonomous production queue.

Explicitly reviewed building families are canonical strict-DONE state. The only
remaining unresolved production set is the 24 character sheets. ONB-00 is
outside the 235 production target.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
MASTER = ROOT / "art/production/master-asset-queue.json"
BUILDING_QUEUE = ROOT / "art/production/controlled-building-regen-queue.json"
CHARACTER_QUEUE = ROOT / "art/production/controlled-character-regen-queue.json"
STATE = ROOT / "art/production/autofactory-state.json"
SUMMARY = ROOT / "art/production/autofactory-summary.md"
⋮----
ROW = re.compile(
⋮----
TARGET_TOTAL = 235
STRICT_BASELINE = 211
MAX_ATTEMPTS = 8
⋮----
PERSISTED_ASSET_STATE_FIELDS = (
⋮----
BUILDING_PRIORITY = ["BLD-10", "BLD-05", "BLD-08",
CHARACTER_PRIORITY = ["CHR-OP", "CHR-TECH", "CHR-LOG", "CHR-ENG"]
⋮----
def load_json(path: Path, default: Any = None) -> Any
⋮----
def save_json(path: Path, value: Any) -> None
⋮----
def manifest_rows() -> list[dict[str, str]]
⋮----
rows: list[dict[str, str]] = []
⋮----
m = ROW.match(line)
⋮----
tier = asset_id.rsplit("T", 1)[1]
runtime = f"app/src/main/res/drawable-nodpi/zte_business_08_t{tier}_final.png"
⋮----
def unresolved_ids() -> set[str]
⋮----
ids = {r["id"] for r in manifest_rows() if r["id"].startswith("CHR-")}
⋮----
def default_asset(row: dict[str, str], unresolved: set[str]) -> dict[str, Any]
⋮----
asset_id = row["id"]
needs = asset_id in unresolved
⋮----
group = "-".join(asset_id.split("-")[:2])
⋮----
group = "FX-HISTORICAL"
⋮----
def ensure_master() -> dict[str, Any]
⋮----
existing = load_json(MASTER, {}) or {}
old = {x["id"]: x for x in existing.get("assets", []) if isinstance(x, dict) and x.get("id")}
unresolved = unresolved_ids()
assets: list[dict[str, Any]] = []
⋮----
base = default_asset(row, unresolved)
prev = old.get(row["id"])
⋮----
queue = {
⋮----
def sync_controlled_queues(queue: dict[str, Any]) -> None
⋮----
by_id = {x["id"]: x for x in queue["assets"]}
⋮----
bq = load_json(BUILDING_QUEUE, {}) or {}
⋮----
aid = str(item.get("id", "")).upper()
asset = by_id.get(aid)
⋮----
status = str(item.get("status", "")).upper()
⋮----
cq = load_json(CHARACTER_QUEUE, {}) or {}
⋮----
# A producer may regenerate an optional identity anchor for a sibling
# wave while the master has a distinct, unapproved IDLE candidate.
# Pending/rejected context evidence must not overwrite that older
# candidate or its artifact provenance. A newly produced IDLE candidate
# may replace it only with an actual collected review artifact.
⋮----
pollinations_only = status in {"PENDING_POLLINATIONS", "PROVIDER_ERROR"}
normalized_status = "REJECTED_SEMANTIC" if status in {"REJECTED", "REJECTED_SEMANTIC"} else status
⋮----
def stats(queue: dict[str, Any]) -> dict[str, Any]
⋮----
assets = queue["assets"]
strict_done = sum(x["strict_status"] == "DONE" for x in assets)
awaiting = sum(x["pipeline_status"] == "AWAITING_REVIEW" for x in assets)
blocked = sum(str(x["pipeline_status"]).startswith(("BLOCKED", "PAUSED_AUTOMATION")) for x in assets)
evidence = sum(x["pipeline_status"] in {"EVIDENCE_DISPATCHED", "AWAITING_REVIEW"} and x["lane"] == "fx-runtime-reconciliation" for x in assets)
production_processed = sum(
⋮----
def write_summary(queue: dict[str, Any], decision: dict[str, Any]) -> None
⋮----
s = stats(queue)
lines = [
```

## File: sprites/asset_wave_orchestrator.py
```python
#!/usr/bin/env python3
"""Autonomous producer for the 235-asset Zero -> Empire target.

This script only schedules production/evidence work. It never marks semantic
approval or strict DONE automatically.
"""
⋮----
TRIGGER_WORKFLOW = os.getenv("AUTOF_TRIGGER_WORKFLOW", "")
TRIGGER_CONCLUSION = os.getenv("AUTOF_TRIGGER_CONCLUSION", "")
TRIGGER_RUN_ID = os.getenv("AUTOF_TRIGGER_RUN_ID", "")
TRIGGER_DISPATCH_TOKEN = os.getenv("AUTOF_TRIGGER_DISPATCH_TOKEN", "")
CURRENT_DISPATCH_TOKEN = os.getenv("GITHUB_RUN_ID", "")
KAGGLE_BUSY = os.getenv("AUTOF_KAGGLE_BUSY", "0") == "1"
FX_BUSY = os.getenv("AUTOF_FX_BUSY", "0") == "1"
# New, mechanically coherent planted-foot REPAIR trajectory in PR #175:
# prior four attempts used deep-kneel/standing poses and high denoise.
# This is an algorithm change, so reopen a bounded four-attempt budget;
# never erase historical attempts, rejected evidence, or strict review.
CHARACTER_GENERATION_EPOCH = "production-first-v1.22-planted-repair-poses"
CHARACTER_EPOCH_ATTEMPT_LIMIT = 4
CHARACTER_BATCH_SIZE = 12
INFRA_FAILURE_LIMIT = 3
⋮----
# A character in one of these states already has a produced candidate/evidence.
# It must not be regenerated merely because strict semantic approval is pending.
CHARACTER_PRODUCED_STATUSES = {
⋮----
def by_id(queue: dict[str, Any]) -> dict[str, dict[str, Any]]
⋮----
def mirror_character_outcomes_from_controlled(queue: dict[str, Any], active: list[dict[str, Any]]) -> None
⋮----
controlled = load_json(CHARACTER_QUEUE, {}) or {}
outcomes = {
reasons = {
⋮----
status = outcomes.get(asset["id"])
⋮----
def update_from_trigger(queue: dict[str, Any]) -> None
⋮----
active = [
⋮----
controlled = load_json(path, {}) or {}
changed = False
⋮----
aid = str(item.get("id", "")).upper()
⋮----
asset = next((x for x in active if x["id"] == aid), None)
⋮----
changed = True
⋮----
target = [
⋮----
def active_pending(path: Path) -> list[dict[str, Any]]
⋮----
q = load_json(path, {}) or {}
⋮----
def character_retry_available(asset: dict[str, Any]) -> bool
⋮----
status = str(asset.get("pipeline_status", "")).upper()
⋮----
current_epoch = asset.get("generation_epoch") == CHARACTER_GENERATION_EPOCH
current_error = str(asset.get("last_error") or "")
⋮----
# A new generation epoch is an explicit algorithm/prompt change. Historical
# semantic attempts must not consume the new epoch's retry budget.
⋮----
total_attempts = int(asset.get("attempts") or 0)
⋮----
legacy_failure = "Legacy APK character sheet rejected" in str(asset.get("last_error") or "")
infra_retry = str(asset.get("last_error") or "").startswith("Kaggle producer")
stride_retry = "WALK lacks clear alternating stride" in str(asset.get("review_reason") or "")
⋮----
def mark_dispatch(queue: dict[str, Any], ids: list[str], generator: str) -> list[str]
⋮----
assets = by_id(queue)
eligible: list[str] = []
⋮----
x = assets.get(aid)
⋮----
attempts = int(x.get("attempts") or 0)
⋮----
# Once a fresh dispatch is accepted, historical retry/recovery errors
# are no longer the current state. Keep evidence in the rejection
# ledger, but do not surface stale errors as if the active wave failed.
⋮----
def prioritize_controlled_character_targets(ids: list[str]) -> int
⋮----
"""Put dispatched actions first and include one IDLE identity anchor per role.

    Strict-DONE IDLE sheets are allowed as context-only regeneration targets:
    they do not consume strict progress or become dispatched in the master
    queue, but producing them in the same Kaggle run gives semantic review a
    complete six-action family and lets promotion replace a legacy IDLE sheet
    with bytes from the exact same identity generation epoch.
    """
ordered_ids = list(dict.fromkeys(str(aid).upper() for aid in ids if aid))
selected = set(ordered_ids)
⋮----
targets = controlled.setdefault("targets", [])
by_target = {
⋮----
groups: list[str] = []
⋮----
parts = aid.split("-")
⋮----
group = "-".join(parts[:2])
⋮----
context_ids: list[str] = []
⋮----
idle = f"{group}-IDLE"
⋮----
item = by_target.get(idle)
⋮----
item = {
⋮----
item = by_target.get(aid)
⋮----
priority: list[str] = []
⋮----
rank = {aid: i for i, aid in enumerate(priority)}
⋮----
def building_family_ids(group: str) -> list[str]
⋮----
def prepare_building_group(queue: dict[str, Any], group: str) -> dict[str, Any]
⋮----
unresolved = [aid for aid in building_family_ids(group) if aid in assets and assets[aid]["strict_status"] != "DONE"]
⋮----
targets = [{"id": aid, "status": "PENDING_KAGGLE", "autofactory_context_only": aid not in unresolved} for aid in building_family_ids(group)]
⋮----
dispatched = mark_dispatch(queue, unresolved, "kaggle-building-family")
⋮----
def prepare_character_burst(queue: dict[str, Any], groups: list[str]) -> dict[str, Any]
⋮----
action_order = {"IDLE": 0, "WALK": 1, "WORK": 2, "CARRY": 3, "REPAIR": 4, "CELEB": 5}
targets: list[dict[str, Any]] = []
selected_groups: list[str] = []
producer_slots = 0
⋮----
group_assets = sorted(
⋮----
idle_id = f"{group}-IDLE"
idle_is_selected = any(x["id"] == idle_id for x in group_assets)
# An IDLE already awaiting review still needs its own same-run anchor
# slot when regenerating siblings. Otherwise the subsequent implicit
# context insertion can silently exceed the 12-sheet Kaggle capacity.
needs_idle_context = not idle_is_selected and idle_id in assets
group_cost = len(group_assets) + (1 if needs_idle_context else 0)
⋮----
# Keep role families together whenever possible. Splitting a six-action
# identity family across unrelated GPU runs weakens the semantic review
# evidence and can produce different faces/clothing for one role.
⋮----
available = CHARACTER_BATCH_SIZE - producer_slots - (1 if needs_idle_context else 0)
⋮----
chosen = group_assets[:available]
⋮----
# Keep the exact semantic rejection reason in the next producer
# overlay. Replacing the controlled queue without this evidence made
# queue_rejection_hint() forget why a previous ENG frame failed.
group_targets = [
⋮----
dispatched = mark_dispatch(queue, [x["id"] for x in targets], "kaggle-character-sheet")
producer_count = prioritize_controlled_character_targets(dispatched)
⋮----
def next_group(queue: dict[str, Any], lane: str, priority: list[str]) -> str | None
⋮----
groups = {
⋮----
def close_exhausted_character_dispatches(queue: dict[str, Any]) -> None
⋮----
master = by_id(queue)
⋮----
controlled_status = {
⋮----
# KAGGLE_BUSY is repository-wide, but only one async character wave owns
# the durable active token. A newer wave can supersede an older one via
# workflow concurrency; do not let the newer ENG wave keep stale OP/LOG
# dispatches locked merely because *some* Kaggle work is still active.
async_state = load_json(Path("art/production/kaggle-async-state.json"), {}) or {}
active_async_token = (
⋮----
asset = master.get(aid)
⋮----
asset_token = str(asset.get("dispatch_token") or "")
# Preserve only dispatches owned by the currently active async wave.
# If no active token is known, keep the conservative old behaviour.
⋮----
# A cancelled/superseded async producer can leave the master ledger in
# DISPATCHED even though no Kaggle run remains active. The controlled
# queue staying PENDING_KAGGLE is the durable evidence that no candidate
# was collected. Recover that orphaned dispatch so the next autofactory
# pass can retry it instead of deadlocking strict completion forever.
⋮----
def active_pollinations_repair() -> list[str]
⋮----
"""Honor a time-bounded independent repair lane; never replace its queue.

    The provider is allowed to fail/retry without Autofactory dispatching the
    same character to Kaggle or wiping its preserved source evidence.
    """
controlled=load_json(CHARACTER_QUEUE,{}) or {}
⋮----
end=controlled.get('reservation_expires_utc')
⋮----
expires=datetime.fromisoformat(end.replace('Z','+00:00'))
⋮----
blocked={'PENDING','PENDING_POLLINATIONS','BLOCKED','PROVIDER_ERROR',
⋮----
def pending_ids_from_controlled(path: Path, queue: dict[str, Any]) -> list[str]
⋮----
ids = [str(x.get("id", "")).upper() for x in active_pending(path)]
⋮----
def order_character_groups_by_retry(queue: dict[str, Any], groups: list[str]) -> list[str]
⋮----
"""Give untouched role families a chance before repeating failed GPU waves.

    Tie-breaks preserve the canonical role priority. A legacy generation epoch
    counts as zero use of the current algorithm, not a permanent penalty.
    """
def current_epoch_attempts(group: str) -> float
⋮----
eligible = [
⋮----
priority = {group: index for index, group in enumerate(CHARACTER_PRIORITY)}
⋮----
def make_decision(queue: dict[str, Any]) -> dict[str, Any]
⋮----
s = stats(queue)
⋮----
building_pending = pending_ids_from_controlled(BUILDING_QUEUE, queue)
⋮----
ids = mark_dispatch(queue, building_pending, "kaggle-building-family")
⋮----
group = next_group(queue, "kaggle-building-family", BUILDING_PRIORITY)
⋮----
prepared = prepare_building_group(queue, group)
⋮----
# Defer competing Kaggle character dispatches while the explicitly
# reserved Pollinations repair lane is active (other lanes remain free).
repair_ids=active_pollinations_repair()
⋮----
character_pending = pending_ids_from_controlled(CHARACTER_QUEUE, queue)
⋮----
ids = mark_dispatch(queue, character_pending[:CHARACTER_BATCH_SIZE], "kaggle-character-sheet")
⋮----
producer_count = prioritize_controlled_character_targets(ids)
⋮----
first_group = next_group(queue, "kaggle-character-sheet", CHARACTER_PRIORITY)
⋮----
candidate_groups = [
ordered = order_character_groups_by_retry(queue, candidate_groups)
burst_groups = ordered[:3]
⋮----
prepared = prepare_character_burst(queue, burst_groups)
⋮----
fx = [x for x in queue["assets"] if x["lane"] == "fx-runtime-reconciliation" and x["strict_status"] != "DONE" and x["pipeline_status"] == "PENDING_EVIDENCE" and int(x.get("attempts") or 0) < MAX_ATTEMPTS]
⋮----
refreshed = stats(queue)
⋮----
def main() -> int
⋮----
queue = ensure_master()
# Apply the producer callback while dispatched assets and their ownership
# token are still intact. Controlled-queue sync can otherwise change the
# master status first and make the correlated callback miss its assets.
⋮----
decision = make_decision(queue)
```

## File: sprites/audit_character_bank_motion.py
```python
#!/usr/bin/env python3
"""Heuristic 42px character motion audit, never a semantic approval gate.

Rank review effort using actual rendered animation changes rather than file
existence. Source atlas bytes, hashes and review-only provenance are verified.
"""
⋮----
FRAMES = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}
MOBILE_SIZE = 42
DAY = (189, 203, 211, 255)
NIGHT = (16, 27, 41, 255)
HEAD_ANCHOR_ACTION = {"OP": "WALK", "LOG": "WALK", "ENG": "IDLE", "TECH": "IDLE"}
# Conservative pre-screening: a distance is not proof that two faces differ.
HEAD_REVIEW_THRESHOLD = 11.0
HEAD_EXTREME_THRESHOLD = 30.0
⋮----
def composite(tile: Image.Image, color: tuple[int, ...]) -> Image.Image
⋮----
surface = Image.new("RGBA", tile.size, color)
⋮----
def change(first: Image.Image, second: Image.Image) -> float
⋮----
means = ImageStat.Stat(ImageChops.difference(first, second)).mean
⋮----
def motion_stats(blob: bytes, count: int) -> dict
⋮----
tiles = [
⋮----
images = [composite(tile, background) for tile in tiles]
⋮----
def head_thumbnail(blob: bytes) -> Image.Image
⋮----
"""Normalized first-frame helmet/face crop for review, not recognition.

    Foreground-based head positioning avoids treating a large handheld crate as
    the person's face. A fixed neutral composite makes alpha-crop edges
    comparable. A 64px color difference is merely a triage signal.
    """
⋮----
frame = source.crop((0, 0, 256, 256))
alpha = frame.getchannel("A")
bounds = alpha.getbbox()
⋮----
span = bottom - top
⋮----
upper = alpha.crop((0, top, 256, min(256, top + max(1, round(span * .28)))))
⋮----
pixels = upper.load()
⋮----
xmid = round(weighted_x / total)
cropped = frame.crop((xmid - 47, max(0, top - 5),
canvas = Image.new("RGBA", cropped.size, (170, 181, 193, 255))
⋮----
def head_difference(first: Image.Image, second: Image.Image) -> float
⋮----
"""RGB mean absolute difference of centered head thumbnails (0..255)."""
⋮----
def analyze(bank_path: Path, output_path: Path) -> dict
⋮----
metadata = json.loads(bank.read("candidate-bank-index.json"))
entries = metadata.get("bank_entries")
⋮----
asset_id = str(row.get("id") or "")
parts = asset_id.split("-")
⋮----
filename = "zte_chr_" + parts[1].lower() + "_" + parts[2].lower() + "_final.png"
⋮----
blob = bank.read("candidates/" + filename)
⋮----
metrics = motion_stats(blob, FRAMES[parts[2]])
⋮----
flags = []
⋮----
prior_flags = [str(x) for x in row.get("deferred_art_warnings") or []]
⋮----
# Compare each role with its coherent visual reference. OP/LOG usually
# have no unfinished IDLE in the bank; their WALK is the review reference.
# A technically accepted engineer IDLE is a baseline, not an approval.
role_anchor = {}
⋮----
candidates = sorted(asset_id for asset_id in first_heads
⋮----
preferred = "CHR-" + role + "-" + preferred_action
⋮----
role = row["id"].split("-")[1]
reference_id = role_anchor[role]
distance = head_difference(first_heads[reference_id], first_heads[row["id"]])
identity_flags = []
⋮----
ranked = sorted(
audit = {
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
data = analyze(args.bank, args.output)
```

## File: sprites/audit_character_candidates.py
```python
#!/usr/bin/env python3
"""Audit actual canonical character sprite sheets and render contact evidence.

Never grants artistic approval. Uses original PNG candidates in art/incoming;
a TECH preview from a separate generator cannot overwrite canonical evidence.
"""
⋮----
ROOT=Path(__file__).resolve().parents[2]
# Canonical incoming PNGs use the Kaggle producer's actual frame contract.
# The newer animation_batch_planner targets are aspirational and differ.
ACTION_FRAMES={"IDLE":6,"WALK":8,"WORK":10,"CARRY":8,"REPAIR":10,"CELEB":8}
TARGET_FRAMES={"IDLE":8,"WALK":8,"WORK":12,"CARRY":8,"REPAIR":12,"CELEB":10}
⋮----
def inspect(path:Path,asset_id:str)->dict
⋮----
expected=ACTION_FRAMES[action]
result={"asset_id":asset_id,"source_path":str(path),"exists":path.is_file(),
⋮----
cell=w//4
⋮----
rows=h//cell
capacity=4*rows
⋮----
rgba=img.convert("RGBA")
# Blank atlas cells are intentional padding, not extra animation
# frames; reject any nonblank frame after the producer's count.
⋮----
px=(n%4)*cell;py=(n//4)*cell
⋮----
alpha=rgba.getchannel("A")
⋮----
metrics=[]
semantic_frames=[]
⋮----
x=(i%4)*cell;y=(i//4)*cell
frame=rgba.crop((x,y,x+cell,y+cell))
⋮----
mask=frame.getchannel("A")
box=mask.getbbox()
⋮----
margin=min(l,t,cell-r,cell-b)
⋮----
# Unlike file format checks, these are *conservative risks*,
# not a proof of art quality, role identity or final approval.
⋮----
def contact(rows:list[dict],output:Path)->None
⋮----
thumb=112
canvas=Image.new("RGB",(800,len(rows)*148+50),(19,27,39))
d=ImageDraw.Draw(canvas)
⋮----
y=50+i*148
⋮----
risk=row.get("visual_risk",{})
message=("BLOCKING: "+",".join(risk.get("flags",[])[:1])
⋮----
img=original.convert("RGBA")
cell=img.width//4
⋮----
x=n%4*cell;y0=n//4*cell
tile=img.crop((x,y0,x+cell,y0+cell))
⋮----
ox=195+n*120+(thumb-tile.width)//2
oy=y+15+(thumb-tile.height)//2
⋮----
def main()->int
⋮----
parser=argparse.ArgumentParser()
⋮----
args=parser.parse_args()
report=build(json.loads(args.queue.read_text(encoding="utf-8")))
rows=[]
⋮----
asset_id=row["asset_id"]
stem="zte_chr_"+asset_id[4:].lower().replace("-","_")+"_final.png"
source=ROOT/"art/incoming/final-sprites"/stem
audit=inspect(source,asset_id)
⋮----
result={"format":"zte-canonical-character-visual-audit-v1",
```

## File: sprites/audit_chatgpt_originals.py
```python
#!/usr/bin/env python3
"""Risk-only visual QA for the 18 locally authored Zero to Empire atlases.

Designed to report and reproduce defects without modifying any sprites or
promoting manifest progress. Passing never means premium/semantic approval.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
⋮----
FRAME_COUNTS = {"IDLE":6,"WALK":8,"WORK":10,"CARRY":8,"REPAIR":10,"CELEB":8}
ROLES = ("OP","LOG","ENG")
# In this authored atlas the fixed service console starts to the right of
# the worker. Its large horizontal footprint must not masquerade as a cropped
# portrait. The main actor (head, torso, legs) occupies the left 202px.
ENG_REPAIR_ACTOR_GEOMETRY_RIGHT = 202
⋮----
def _verified_fixed_engineer_station(base: Path, count: int) -> bool
⋮----
"""Require every editable SVG to contain the identical fixed station.

    Without this provenance evidence we use the strict full-composite
    geometry assessment; imported or mismatched atlases get no exception.
    """
reference = None
⋮----
source = base / "src_svg" / "ENG" / "REPAIR" / f"{i:02d}.svg"
⋮----
root = ET.parse(source).getroot()
⋮----
stations = [
⋮----
socket = [
⋮----
markup = ET.tostring(stations[0], encoding="utf-8")
⋮----
reference = markup
⋮----
def inspect(atlas: Path, role: str, action: str) -> dict
⋮----
image = source.convert("RGBA")
count = FRAME_COUNTS[action]
frames = [
# ENG REPAIR is a deliberately composite *scene*: a separately authored
# fixed service console extends the overall width without clipping the
# engineer. Only its full-body silhouette/feet geometry is isolated; the
# entire atlas remains subject to palette, tool-motion and loop QA.
# This exception requires the matching, stationary editable SVG fixture.
station_verified = (
actor_frames = None
⋮----
actor_frames = []
⋮----
isolated = Image.new("RGBA", frame.size, (0, 0, 0, 0))
⋮----
flagged = clip_risk(frames, action, geometry_frames=actor_frames)
evidence = {
⋮----
raised = celebration_arm_reach_counts(frames)
⋮----
# The sprite can shift limbs even while its sprite bounding box stays
# fixed. Record a lower-body alpha-change proxy as rejection evidence.
lower = [
scores = []
⋮----
aa=list(a.getdata());bb=list(b.getdata())
inter=sum(x and y for x,y in zip(aa,bb))
union=sum(x or y for x,y in zip(aa,bb))
⋮----
# Include last-to-first transition: a sprite loop can be smooth
# internally but visibly snap at its playback boundary.
⋮----
# Reject a large wraparound jump relative to ordinary frame motion.
internal = sorted(scores[:-1])
typical = internal[len(internal)//2]
⋮----
# Detect a tool, raised arm or cargo handle popping at the wrap.
# This is a rejection signal, not semantic or visual approval.
upper = [
upper_changes = []
⋮----
aa = list(a.getdata())
bb = list(b.getdata())
intersection = sum(x and y for x, y in zip(aa, bb))
union = sum(x or y for x, y in zip(aa, bb))
⋮----
typical = sorted(upper_changes[:-1])[len(upper_changes[:-1]) // 2]
⋮----
def audit(base: Path) -> dict
⋮----
candidates=base/"candidates"
results=[]
⋮----
name=f"zte_chr_{role.lower()}_{action.lower()}_final.png"
result=inspect(candidates/name,role,action)
⋮----
# Same-role cross-action identity must be audited, not just adjacent
# frames within an action. All unfinished character art is authored here
# with one fixed role rig, so compare every action against its local IDLE.
# The comparison is reject-only and never grants strict approval.
⋮----
idle_path=candidates/f"zte_chr_{role.lower()}_idle_final.png"
⋮----
idle=image.convert("RGBA").crop((0,0,256,256))
anchor=_body_region_color_signature(idle,0,.28)
⋮----
action=row["id"].split("-")[-1]
⋮----
atlas=image.convert("RGBA")
frame=atlas.crop((0,0,256,256))
delta=palette_distance(anchor,_body_region_color_signature(frame,0,.28))
⋮----
blocked=sum(row["risk_level"]=="BLOCKING" for row in results)
⋮----
def main() -> int
⋮----
parser=argparse.ArgumentParser()
⋮----
args=parser.parse_args()
report=audit(args.base)
dest=args.base/"visual-risk-qa.json"
```

## File: sprites/audit_complete_sprite_manifest.py
```python
#!/usr/bin/env python3
⋮----
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
MASTER=ROOT/'art/production/master-asset-queue.json'
⋮----
EXPECTED_ROWS=236
⋮----
def main()
⋮----
ap=argparse.ArgumentParser()
⋮----
args=ap.parse_args()
⋮----
rows=[]
⋮----
cols=[c.strip() for c in line.split('|')[1:-1]]
⋮----
queue=json.loads(MASTER.read_text(encoding='utf-8'))
assets=queue.get('assets',[])
ids=[a.get('id') for a in assets]
excluded=set(queue.get('excluded_from_target',[]))
manifest_ids=[row[0] for row in rows]
⋮----
strict_by_id={a['id']:a.get('strict_status') for a in assets}
premature=[r[0] for r in rows
pending=[r[0] for r in rows
⋮----
seen=set(); report=[]; failed=[]
⋮----
p=Path(runtime.replace(chr(96),''))
⋮----
r=validate(aid,p)
⋮----
out=ROOT/'art/production/final-sprite-completion-audit.json'
```

## File: sprites/autonomous_walk.py
```python
#!/usr/bin/env python3
"""Deterministic, unattended walk-sprite generator for Zero to Empire.

Uses one identity-locked vector renderer from pose_studio.html and a cyclic,
world-space planted-foot trajectory. No Kaggle, prompts or UI operations.
Outputs are review candidates, NEVER strict DONE.
"""
⋮----
CANVAS = 512
GROUND = 446
ROOT_X = 252
HIP_Y = 270
KINEMATIC_REACH = 94 + 99 - 1
⋮----
@dataclass(frozen=True)
class WalkSettings
⋮----
asset_id: str = 'CHR-TECH-WALK'
frames: int = 24
fps: int = 12
stride: float = 92.0
clearance: float = 36.0
stance_fraction: float = 0.62
pelvis_bob: float = 3.5
arm_swing: float = 30.0
palette: str = 'cyan'
⋮----
def validate(self) -> None
⋮----
def ease_hermite(start: float, end: float, u: float, slope_u: float) -> float
⋮----
"""Cubic position and velocity matching at lift-off/touch-down."""
h00 = 2 * u**3 - 3 * u**2 + 1
h10 = u**3 - 2 * u**2 + u
h01 = -2 * u**3 + 3 * u**2
h11 = u**3 - u**2
⋮----
def foot_local(phase: float, settings: WalkSettings) -> tuple[float, float, bool]
⋮----
"""Foot trajectory relative to torso. During stance the planted foot does
    not move in world coordinates as the body advances at constant speed.
    """
⋮----
d = settings.stance_fraction
s = settings.stride
⋮----
u = (phase-d)/(1-d)
slope_u = -(s/d)*(1-d)
x = ease_hermite(-s/2, s/2, u, slope_u)
y = GROUND - settings.clearance*(math.sin(math.pi*u)**1.3)
⋮----
def foot_roll(phase: float, settings: WalkSettings) -> float
⋮----
"""Toe tilt in radians, continuous across toe-off and heel-strike.
    Negative = toe lifted before landing; positive = toe pointed down on push.
    Exact ankle/ground positions remain governed by foot_local().
    """
⋮----
u = phase / d
⋮----
u = (phase - d) / (1 - d)
⋮----
def pose(t: float, settings: WalkSettings) -> dict[str, Any]
⋮----
# Arms counter-swing to legs, with sub-pixel smooth motion.
opposite = settings.arm_swing*math.cos(2*math.pi*t)
⋮----
def length(a: dict, b: dict) -> float
⋮----
def pose_distance(a: dict, b: dict) -> float
⋮----
def verify_motion(settings: WalkSettings) -> dict[str, Any]
⋮----
"""Numerical QA is independent of the renderer and cannot approve art."""
samples = max(192, settings.frames*8)
points = [pose(i/samples,settings) for i in range(samples)]
⋮----
velocity = settings.stride / settings.stance_fraction
step = 1.0 / samples
⋮----
foot = p[side]
hip = {'x':p['root']['x']+hip_shift, 'y':p['root']['y']}
reach = length(hip,foot)
⋮----
# Stay inside one contiguous stance; avoid wrapping phase-snap.
nxt=points[(i+1)%samples][side]
# Absolute positions are relative to a torso moving at velocity 'velocity'.
dx=nxt['x']-foot['x'] + velocity*step
dy=nxt['y']-foot['y']
⋮----
poses=[pose(i/settings.frames, settings) for i in range(settings.frames)]
edges=[pose_distance(poses[i],poses[(i+1)%settings.frames]) for i in range(settings.frames)]
median=statistics.median(edges)
seam_ratio=edges[-1]/median if median else math.inf
q={
⋮----
def render(poses: list[dict[str,Any]], source_html: Path, palette: str) -> list[Image.Image]
⋮----
frames=[]
⋮----
browser=playwright.chromium.launch(headless=True,executable_path=shutil.which('chromium') or shutil.which('google-chrome'),args=['--no-sandbox'])
⋮----
page=browser.new_page(viewport={'width':600,'height':600})
failures=[]
⋮----
png_url=page.evaluate('''p => {const c=document.createElement('canvas');c.width=512;c.height=512;
⋮----
def check_alpha(frames: list[Image.Image]) -> dict[str,Any]
⋮----
touched=[]; empty=[]; bounds=[]
⋮----
box=im.getchannel('A').getbbox()
⋮----
def export(output:Path, settings:WalkSettings, html:Path, bundle: bool=True) -> dict
⋮----
frames_list=[pose(i/settings.frames,settings) for i in range(settings.frames)]
q=verify_motion(settings)
frames=render(frames_list,html,settings.palette)
qa_alpha=check_alpha(frames)
⋮----
# Silhouette seam is measured on the actual alpha pixels, not just IK joints.
⋮----
def silhouette_diff(a:Image.Image,b:Image.Image)->float
⋮----
x=np.asarray(a.getchannel('A'))>127
y=np.asarray(b.getchannel('A'))>127
union=np.count_nonzero(x|y)
⋮----
transitions=[silhouette_diff(frames[i],frames[(i+1)%len(frames)]) for i in range(len(frames))]
median_visual=statistics.median(transitions)
⋮----
atlas=Image.new('RGBA',(CANVAS*4,CANVAS*math.ceil(settings.frames/4)))
⋮----
out=output/'frames'/f'{settings.asset_id}-{i:02d}.png'
⋮----
thumbs=[]
⋮----
rgb=Image.new('RGB',(CANVAS,CANVAS),(28,36,47))
⋮----
review=Image.new('RGB',(256*8,256*math.ceil(settings.frames/8)),(24,32,44))
⋮----
editable={
⋮----
events = []
⋮----
contact = ('both' if p['lockL'] and p['lockR'] else
⋮----
manifest={
⋮----
def main()
⋮----
parser=argparse.ArgumentParser(description=__doc__)
⋮----
args=parser.parse_args()
settings=WalkSettings(asset_id=args.asset_id,frames=args.frames,fps=args.fps,stride=args.stride,clearance=args.clearance,stance_fraction=args.stance,palette=args.palette)
manifest=export(args.output, settings, args.studio)
qa=manifest['qa']
```

## File: sprites/build_character_bank_mobile_review.py
```python
#!/usr/bin/env python3
"""Generate a complete offline mobile comparison of the 16 review-only sprites.

Data sources: the published SHA-256 checked candidate-bank ZIP and the
reproducible in-repository 18 original SVG/PNG atlases. Never promotes assets.
"""
⋮----
PNG_NAME = re.compile(r"^zte_chr_(op|log|eng|tech)_(idle|walk|work|carry|repair|celeb)_final\.png$")
COUNTS = {"idle": 6, "walk": 8, "work": 10, "carry": 8, "repair": 10, "celeb": 8}
⋮----
HTML = r'''<!doctype html><html lang="fr"><head><meta charset="utf-8">
⋮----
originals = load_local_originals(local_path)
audit_by_id = None
⋮----
audit = json.loads(audit_path.read_text(encoding="utf-8"))
records = audit.get("assets")
⋮----
audit_by_id = {str(row.get("id")): row for row in records}
⋮----
meta = json.loads(bank.read("candidate-bank-index.json"))
rows = meta.get("bank_entries")
⋮----
bank_names = bank.namelist()
seen = set()
embedded = []
⋮----
aid = str(row.get("id") or "")
filename = str(row.get("filename") or "")
match = PNG_NAME.fullmatch(filename)
⋮----
source = bank.read("candidates/"+filename)
⋮----
motion_flags = []
identity_flags = []
identity_reference = None
⋮----
audit_record = audit_by_id.get(aid)
⋮----
motion_flags = [str(flag) for flag in (audit_record.get("new_motion_flags") or [])]
identity_flags = [str(flag) for flag in (audit_record.get("new_identity_flags") or [])]
identity_reference = (audit_record.get("head_identity_metrics") or {}).get("reference_id")
⋮----
payload = {
serialized = json.dumps(payload, ensure_ascii=False, separators=(",",":"))
# Avoid closing <script> from tainted machine-written warning text.
serialized = serialized.replace("<","\\u003c").replace(">","\\u003e").replace("&","\\u0026")
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
```

## File: sprites/build_character_candidate_bank.py
```python
#!/usr/bin/env python3
"""Assemble a traceable, review-only character bank from persistent Releases.

Every selected atlas must have the *same collector run* recorded on the
canonical queue and in the candidate archive, with matching SHA-256 bytes.
This is NOT automatic Android promotion or strict semantic approval.
"""
⋮----
ASSET_NAME = re.compile(r"^zte_chr_(?:op|tech|log|eng)_(?:idle|walk|work|carry|repair|celeb)_final\.png$")
ARCHIVE_NAME = re.compile(r"^zte-characters-([1-9][0-9]*)\.zip$")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
PRODUCED_STATES = frozenset({
MAX_ATLAS_BYTES = 100 * 1024 * 1024
FRAME_COUNTS = {"IDLE": 6, "WALK": 8, "WORK": 10,
CANONICAL_PRODUCED_STATES = PRODUCED_STATES
⋮----
def load_local_originals(source: Path | None) -> dict[str, dict]
⋮----
"""Validate 18 local authored originals, including per-frame editable SVG.

    This independent source is explicitly labelled as provisional. It is not
    used to mutate Kaggle/controlled queues or advance strict DONE.
    """
⋮----
manifest = json.loads((source / "creation-manifest.json").read_text(encoding="utf-8"))
qa = json.loads((source / "candidate-qa.json").read_text(encoding="utf-8"))
⋮----
original_rows = manifest.get("assets")
qa_rows = qa.get("assets")
⋮----
by_id = {row["id"]: row for row in original_rows}
by_qa = {row["id"]: row for row in qa_rows}
expected = {
⋮----
def validated_local_candidate(asset: dict, record: dict) -> tuple[bytes, dict]
⋮----
"""Verify actual raster geometry, manifest claims and editable SVG count."""
asset_id = asset["id"]
row = record["manifest"]
qa = record["qa"]
⋮----
frame_count = FRAME_COUNTS[action]
name = Path(asset["runtime"]).with_suffix(".png").name
⋮----
source = record["source"]
path = source / "candidates" / name
⋮----
results = inspect_sprite(path)
⋮----
svg_folder = source / "src_svg" / role / action
svgs = sorted(svg_folder.glob("*.svg"))
⋮----
blob = path.read_bytes()
⋮----
def open_archives(folder: Path) -> dict[int, dict]
⋮----
"""Read indexes only; candidate bytes are verified when actually selected."""
sources = {}
⋮----
match = ARCHIVE_NAME.fullmatch(path.name)
⋮----
run_id = int(match.group(1))
⋮----
index = json.loads(container.read("candidate-index.json"))
⋮----
by_name = {}
⋮----
name = str(record.get("filename") or "")
⋮----
data = json.loads(master.read_text(encoding="utf-8"))
assets = data["assets"]
target_total = data["target_total"]
⋮----
sources = open_archives(archive_folder)
originals = load_local_originals(local_original)
⋮----
strict_done = sum(x["strict_status"] == "DONE" for x in assets)
review_targets = [
⋮----
# Do not compose a character from two incompatible visual identities.
# The currently unfinished ENG role must be available as a complete
# six-action set before its entire bank cohort can be replaced.
actual_eng = {x["id"] for x in review_targets
expected_eng = {"CHR-ENG-" + action for action in FRAME_COUNTS}
⋮----
remaining_noncharacters = [
canonical_queue_produced = sum(
included: list[tuple[str, bytes]] = []
entries = []
missing = []
⋮----
status = str(asset.get("pipeline_status") or "").upper()
run_id = int(asset.get("review_artifact_run_id") or 0)
⋮----
source = sources.get(run_id)
source_details: dict
⋮----
# Separate, explicitly named review bank only: never change the
# canonical collector-first selection or the Android runtime.
⋮----
digest = hashlib.sha256(blob).hexdigest()
source_warnings = []
⋮----
recorded = source["index"][name]
⋮----
blob = container.read("candidates/" + name)
⋮----
source_details = {
source_warnings = recorded.get("deferred_art_warnings") or []
⋮----
# A real on-repo, authored 1024px/4-column/transparent source
# is preferable to an uncollected async GPU job. It is clearly
# identified as a local review candidate, not as Kaggle output.
⋮----
warnings = sorted(set(
⋮----
production_processed = strict_done + len(entries)
complete = not missing and not remaining_noncharacters and production_processed == target_total
report = {
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
d = assemble(args.master, args.archives, args.output, args.report,
```

## File: sprites/build_character_identity_polish.py
```python
#!/usr/bin/env python3
"""Make safe, deterministic, review-only head/helmet continuity alternatives.

Never replace the canonical candidate bank, an Android resource, or a strict
approval. Reuse the SHA-verified first-frame role reference from the exact
published candidate bank; all modified poses must pass the existing
conservative full-body head-registration guard. One rejected pose rejects
that whole *alternative*, avoiding flickering mixed-identity animations.
"""
⋮----
NAME = re.compile(r"^CHR-(OP|LOG|ENG|TECH)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$")
MAX_BLOB = 20 * 1024 * 1024
REQUIRED_FLAG = "CROSS_ACTION_HEAD_IDENTITY_REVIEW"
MAX_HEAD_AFTER = 8.0
MAX_REMAINING_ERROR_FRACTION = .65
⋮----
def _atlas(blob: bytes, asset_id: str) -> Image.Image
⋮----
def _frames(atlas: Image.Image, count: int) -> list[Image.Image]
⋮----
def _pack(frames: list[Image.Image]) -> bytes
⋮----
image = Image.new("RGBA", (1024, 1024))
⋮----
result = io.BytesIO()
⋮----
def _font(size: int) -> ImageFont.ImageFont
⋮----
def _comparison(rows: list[dict], destination: Path) -> None
⋮----
"""Provide a lightweight visual comparison without modifying the source."""
⋮----
canvas = Image.new("RGB", (width, header + height * len(rows) + 12),
pen = ImageDraw.Draw(canvas)
font = _font(17)
small = _font(12)
⋮----
y = header + n * height
⋮----
x = 16 + j * (unit + 12)
⋮----
background = Image.new("RGBA", (208, 208), (194, 207, 218, 255))
⋮----
"""An all-or-nothing alternative per action, fail-closed on provenance."""
audit = json.loads(audit_path.read_text(encoding="utf-8"))
audit_rows = audit.get("assets")
⋮----
by_audit = {x.get("id"): x for x in audit_rows if isinstance(x, dict)}
⋮----
names = bank.namelist()
⋮----
meta = json.loads(bank.read("candidate-bank-index.json"))
entries = meta.get("bank_entries")
⋮----
verified: dict[str, dict] = {}
⋮----
asset_id = str(entry.get("id") or "")
parsed = NAME.fullmatch(asset_id)
⋮----
fname = "zte_chr_" + parsed.group(1).lower() + "_" + parsed.group(2).lower() + "_final.png"
⋮----
blob = bank.read("candidates/" + fname)
sha = hashlib.sha256(blob).hexdigest()
⋮----
image = _atlas(blob, asset_id)
audit_row = by_audit.get(asset_id)
⋮----
# A plausible same-role atlas is not necessarily the intended reference.
# Lock every polish proposal to the audit's declared canonical role anchor,
# preventing stale or edited audit records from silently using another pose.
anchors = audit.get("head_identity_reference")
⋮----
role = record["role"]
reference_id = anchors.get(role)
reference = verified.get(reference_id)
metrics = record["audit"]["head_identity_metrics"]
⋮----
members: list[tuple[str, bytes]] = []
⋮----
flags = record["audit"]["new_identity_flags"]
⋮----
reference_id = record["audit"]["head_identity_metrics"].get("reference_id")
anchor = verified.get(reference_id)
⋮----
original = _frames(record["atlas"], FRAMES[record["action"]])
reference_frame = _frames(anchor["atlas"], FRAMES[anchor["action"]])[0]
before = head_difference(
recorded_before = record["audit"]["head_identity_metrics"].get("mean_head_rgb_change")
⋮----
fixed: list[Image.Image] = []
skip_reason = None
⋮----
skip_reason = f"frame-{number}: {why}"
⋮----
# Preserve feet, lower torso, arms and tools exactly. Head
# transfer must not masquerade as full-action regeneration.
box = frame.getchannel("A").getbbox()
⋮----
skip_reason = f"frame-{number}: empty-alpha"
⋮----
lower_y = min(255, box[1] + round((box[3] - box[1]) * .46))
⋮----
skip_reason = f"frame-{number}: lower-body-mutated"
⋮----
blob = _pack(fixed)
after = head_difference(head_thumbnail(anchor["blob"]), head_thumbnail(blob))
⋮----
# Recheck real 42px animation readability after head retouch. A
# head-color improvement cannot justify a newly static animation.
# The motion audit is a conservative warning, not semantic approval.
original_motion = motion_stats(record["blob"], len(original))
polished_motion = motion_stats(blob, len(fixed))
motion_warning = (
# A visually improved face cannot compensate for a regressed 42px
# action. Reject the complete alternative, rather than publishing
# a sprite known to have a motion regression for later selection.
⋮----
filename = asset_id.lower().replace("-", "_") + "_head-polish.png"
destination_name = "review-alternatives/" + filename
⋮----
report = {
⋮----
destination_index = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
⋮----
mobile = write_mobile_review(gallery_rows, mobile_review_path, meta["strict_done"])
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
report = build(args.bank, args.audit, args.output, args.report, args.comparison,
```

## File: sprites/build_character_mobile_motion_storyboard.py
```python
#!/usr/bin/env python3
"""Actual-gameplay-size animation storyboard, verified source candidates only.

Every 42px frame is rendered first against both daytime and nighttime game
backgrounds, *then* enlarged with nearest-neighbor for human inspection.
This avoids judging movement from attractive but misleading 256px source art.
"""
⋮----
SCALE = 3
PAD = 18
LABEL_WIDTH = 210
FRAME_GAP = 12
TILE_WIDTH = MOBILE_SIZE * SCALE
ROW_HEIGHT = 320
TITLE_HEIGHT = 104
BG = (12, 20, 33)
TEXT = (242, 248, 255)
MUTED = (173, 192, 212)
WARNING = (255, 173, 109)
FRAME_INDICES = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
DISPLAY_FRAMES = 4
⋮----
def _selected_frames(count: int) -> tuple[int, ...]
⋮----
"""Representative early/mid/late frames, including first and final seam."""
⋮----
def build(bank_path: Path, audit_path: Path, output_path: Path) -> dict
⋮----
width = PAD * 2 + LABEL_WIDTH + (TILE_WIDTH + FRAME_GAP) * DISPLAY_FRAMES
height = TITLE_HEIGHT + ROW_HEIGHT * len(rows) + PAD
output = Image.new("RGB", (width, height), BG)
painter = ImageDraw.Draw(output)
⋮----
top = TITLE_HEIGHT + position * ROW_HEIGHT
⋮----
name = f"candidates/zte_chr_{role.lower()}_{action.lower()}_final.png"
count = FRAMES[action]
⋮----
selected = _selected_frames(count)
frames = [
flagged = bool(row["identity_flags"] or row["motion_flags"])
⋮----
notice = ("IDENTITE" if row["identity_flags"] else
⋮----
x = PAD + LABEL_WIDTH + j * (TILE_WIDTH + FRAME_GAP)
⋮----
y = top + 31 + k * (TILE_WIDTH + 20)
rendered = composite(frame, bg)
zoomed = rendered.resize((TILE_WIDTH, TILE_WIDTH),
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
```

## File: sprites/build_character_review_panels.py
```python
#!/usr/bin/env python3
"""Make lossless action-by-action frame sheets for human character review.

Outputs are review evidence only. This tool never promotes or edits sprites.
"""
⋮----
ACTIONS = {"idle": 6, "walk": 8, "work": 10, "carry": 8, "repair": 10, "celeb": 8}
PATTERN = re.compile(r"^zte_chr_(op|tech|log|eng)_(idle|walk|work|carry|repair|celeb)_final\.png$")
CELL = 256
TILE = 276
ROW_HEIGHT = 306
LABEL_WIDTH = 154
HEADER_HEIGHT = 76
⋮----
def checkerboard() -> Image.Image
⋮----
result = Image.new("RGB", (CELL, CELL), (221, 225, 232))
draw = ImageDraw.Draw(result)
⋮----
def readable_font(size: int) -> ImageFont.ImageFont
⋮----
def face_center_x(frame: Image.Image, bbox: tuple[int, int, int, int]) -> int
⋮----
"""Locate the dominant head/helmet mass, not the wider tool/crate bbox.

    Looking at the top 6%-24% of the visible character reduces false shifts
    when an action adds a large prop beside the hands. This is only a crop
    heuristic; it never classifies identity or automatically approves a sheet.
    """
top = bbox[1] + round((bbox[3] - bbox[1]) * .06)
bottom = bbox[1] + round((bbox[3] - bbox[1]) * .24)
alpha = frame.getchannel("A")
⋮----
region = alpha.crop((0, max(0, top), CELL, min(CELL, bottom)))
pixels = region.load()
weighted_sum = 0
weight = 0
⋮----
def create_head_panel(role: str, assets: dict[str, Path], output: Path) -> None
⋮----
"""Magnify each frame's face/headgear for cross-action identity review.

    Visual evidence only: a matching crop does not prove animation or identity
    correctness. It is easier to read on Android than the wide full-frame sheet.
    """
⋮----
width = label_width + 10 * tile_width
height = header + len(ACTIONS) * row_height
panel = Image.new("RGB", (width, height), (26, 29, 36))
draw = ImageDraw.Draw(panel)
title_font = readable_font(20)
font = readable_font(14)
label_font = readable_font(18)
⋮----
y = header + row * row_height
⋮----
path = assets.get(action)
⋮----
atlas = src.convert("RGBA")
⋮----
f = atlas.crop(((index % 4) * CELL, (index // 4) * CELL,
bbox = f.getchannel("A").getbbox()
⋮----
xmid = face_center_x(f, bbox)
x0 = min(CELL - 96, max(0, xmid - 48))
y0 = min(CELL - 96, max(0, bbox[1] - 5))
head = f.crop((x0, y0, x0 + 96, y0 + 96)).resize(
background = checkerboard().resize((cell_width, cell_width))
⋮----
x = label_width + index * tile_width + 7
⋮----
"""Portrait 2-column contact sheet readable on an Android smartphone.

    Every frame retains its original 256x256 pixels, not a tiny thumbnail.
    Only review evidence is produced; a QA PASS is not semantic approval.
    """
frame_count = ACTIONS[action]
⋮----
width = columns * stride + 18
height = header + ((frame_count + columns - 1) // columns) * 308
image = Image.new("RGB", (width, height), (23, 27, 33))
draw = ImageDraw.Draw(image)
⋮----
record = qa.get(path.name, {})
status = "TECHNICAL PASS - VISUAL REVIEW REQUIRED" if record.get("pass") is True else (
⋮----
background = checkerboard()
⋮----
x = 15 + (index % columns) * stride
y = header + (index // columns) * 308 + 8
tile = atlas.crop(((index % 4) * CELL, (index // 4) * CELL,
opaque = background.copy()
⋮----
def _frame_alpha_iou(left: Image.Image, right: Image.Image) -> float
⋮----
"""Downsampled alpha overlap only; not an identity or action verdict."""
a = left.getchannel("A").resize((64, 64), Image.Resampling.BILINEAR)
b = right.getchannel("A").resize((64, 64), Image.Resampling.BILINEAR)
left_mask = [v >= 32 for v in a.getdata()]
right_mask = [v >= 32 for v in b.getdata()]
overlap = sum(x and y for x, y in zip(left_mask, right_mask))
union = sum(x or y for x, y in zip(left_mask, right_mask))
⋮----
def motion_review_evidence(frames: list[Image.Image], action: str) -> dict
⋮----
"""Measure animation loop cuts separately from the generator's frame QA.

    The closing transition (last -> first) is rendered continuously in the
    Android loop but was absent from previous adjacent-frame QA. A bad seam
    is flagged for human review, *never* promoted or auto-approved.
    """
⋮----
steps = [1 - _frame_alpha_iou(a, b) for a, b in zip(frames[:-1], frames[1:])]
loop_step = 1 - _frame_alpha_iou(frames[-1], frames[0])
mean_step = sum(steps) / len(steps)
seam_ratio = loop_step / max(.015, mean_step)
flags = []
⋮----
def create_panel(role: str, assets: dict[str, Path], output: Path, qa: dict[str, dict]) -> dict
⋮----
font = readable_font(15)
heading = readable_font(21)
labels = readable_font(18)
width = LABEL_WIDTH + 10 * TILE
height = HEADER_HEIGHT + len(ACTIONS) * ROW_HEIGHT
sheet = Image.new("RGB", (width, height), (24, 27, 34))
draw = ImageDraw.Draw(sheet)
⋮----
base = checkerboard()
status: dict = {}
⋮----
y = HEADER_HEIGHT + row * ROW_HEIGHT
⋮----
qa_row = qa.get(path.name, {}) if path else {}
is_pass = qa_row.get("pass") is True
label_color = (105, 202, 157) if is_pass else (236, 184, 97) if path else (166, 170, 179)
⋮----
issues = list(qa_row.get("issues", []) or [])
⋮----
rgba = src.convert("RGBA")
raw_frames = [
diagnostics = motion_review_evidence(raw_frames, action)
# Review candidates with the newest image-only risk rules, even
# when their GPU run used an older generator. These signals cannot
# alter an asset's canonical review or strict DONE state.
⋮----
visual_risk = clip_risk(raw_frames, action.upper())
⋮----
visual_risk = {
⋮----
fx = (frame_idx % 4) * CELL
fy = (frame_idx // 4) * CELL
tile = rgba.crop((fx, fy, fx + CELL, fy + CELL))
bx = LABEL_WIDTH + frame_idx * TILE + 10
by = y + 23
background = base.copy()
⋮----
def create_motion_preview(role: str, action: str, atlas_path: Path, output: Path) -> dict
⋮----
"""Animated mobile-size evidence, NEVER a replacement for lossless PNG.

    Loop playback exposes frozen gestures, teleporting tools and hard cuts that
    a long contact sheet can hide. GIF is color-quantized for portability, so
    review exact costume and pixels in the separately preserved full PNG atlas.
    """
⋮----
atlas = image.convert("RGBA")
frames = []
⋮----
header_font = readable_font(16)
body_font = readable_font(13)
frame_total = ACTIONS[action]
⋮----
sprite = atlas.crop((x, y, x + CELL, y + CELL))
tile = background.copy()
⋮----
visual = Image.new("RGB", (288, 320), (29, 33, 42))
⋮----
draw = ImageDraw.Draw(visual)
⋮----
durations = {"idle": 210, "walk": 115, "work": 145,
duration = durations[action]
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
qa: dict[str, dict] = {}
⋮----
data = json.loads(args.qa_report.read_text(encoding="utf-8"))
rows = data if isinstance(data, list) else data.get("assets", [])
qa = {str(row.get("file", "")): row for row in rows}
by_role: dict[str, dict[str, Path]] = {}
⋮----
match = PATTERN.fullmatch(path.name)
⋮----
results = []
⋮----
item = create_panel(role, assets, args.output_dir / f"review-frames-{role}.png", qa)
⋮----
mobile_files = {}
motion_files = {}
⋮----
filename = f"review-mobile-{role}-{action}.png"
⋮----
preview = f"review-motion-{role}-{action}.gif"
⋮----
summary = {"schema_version": 1, "review_only": True, "roles": results}
```

## File: sprites/build_character_role_contact_sheet.py
```python
#!/usr/bin/env python3
"""Offline role-by-role contact sheet for *candidate review*, not art approval.

Read the complete verified source bank and exact SHA-matching head/motion audit.
Compose one Android-friendly PNG of first frames to expose visually inconsistent
faces, helmets and palettes. No artifact is moved to the Android app/runtime.
"""
⋮----
COLUMNS = 6
ROLES = ("OP", "LOG", "ENG")
ACTIONS = ("IDLE", "WALK", "WORK", "CARRY", "REPAIR", "CELEB")
CELL_WIDTH = 216
CELL_HEIGHT = 242
PAD = 24
HEADER_HEIGHT = 90
ROLE_HEADER = 42
ROLE_GAP = 22
BG = (11, 20, 32)
CARD = (25, 39, 57)
PREVIEW_BG = (186, 200, 212)
TEXT = (239, 247, 255)
MUTED = (182, 200, 221)
ALERT = (255, 178, 118)
NORMAL = (92, 155, 169)
ROLE_LABELS = {"OP": "OPERATEUR", "LOG": "LOGISTIQUE", "ENG": "INGENIEUR"}
NAME_RE = re.compile(r"^CHR-(OP|LOG|ENG)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$")
⋮----
def _font(size: int) -> ImageFont.ImageFont
⋮----
def _load(bank_path: Path, audit_path: Path) -> tuple[dict, list[dict]]
⋮----
audit = json.loads(audit_path.read_text(encoding="utf-8"))
⋮----
records = {r.get("id"): r for r in audit["assets"] if isinstance(r, dict)}
⋮----
names = packed.namelist()
⋮----
meta = json.loads(packed.read("candidate-bank-index.json"))
entries = meta.get("bank_entries")
⋮----
aid = str(entry.get("id") or "")
match = NAME_RE.fullmatch(aid)
⋮----
expected_name = f"zte_chr_{match.group(1).lower()}_{match.group(2).lower()}_final.png"
name = "candidates/" + expected_name
⋮----
blob = packed.read(name)
⋮----
record = records.get(aid)
⋮----
frame = atlas.crop((0, 0, 256, 256))
⋮----
# A matching PNG hash is necessary but insufficient: reject an audit
# with a forged reference ID, nonsensical distance, or flags claiming
# a same-role match against another role. Otherwise the mobile sheet
# can misleadingly direct reviewers to the wrong character family.
anchors = audit.get("head_identity_reference")
⋮----
expected = anchors.get(role)
distance = item["head_deviation"]
⋮----
def build(bank_path: Path, audit_path: Path, output_path: Path) -> dict
⋮----
row_groups = [sorted((r for r in rows if r["role"] == role),
⋮----
height = HEADER_HEIGHT + len(ROLES) * (ROLE_HEADER + CELL_HEIGHT + ROLE_GAP) + PAD
width = PAD * 2 + COLUMNS * CELL_WIDTH
result = Image.new("RGB", (width, height), BG)
draw = ImageDraw.Draw(result)
⋮----
alert_count = 0
⋮----
section_y = HEADER_HEIGHT + rindex * (ROLE_HEADER + CELL_HEIGHT + ROLE_GAP)
⋮----
warnings = item["identity_flags"]
⋮----
outline = ALERT if warnings else NORMAL
⋮----
actor = Image.new("RGBA", (192, 186), (*PREVIEW_BG, 255))
frame = item["frame"].resize((186, 186), Image.Resampling.LANCZOS)
⋮----
notice = "IDENTITE A REVOIR"
⋮----
notice = "MOUVEMENT A REVOIR"
⋮----
notice = "REVUE ARTISTIQUE"
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
```

## File: sprites/build_original_offline_review.py
```python
#!/usr/bin/env python3
"""Offline Android-first sprite inspection; never changes strict DONE."""
⋮----
ROLES=("OP","LOG","ENG")
FRAMES={"IDLE":6,"WALK":8,"WORK":10,"CARRY":8,"REPAIR":10,"CELEB":8}
⋮----
HTML=r'''<!doctype html><html lang="fr"><head><meta charset="utf-8">
⋮----
def build(source:Path,destination:Path)->dict
⋮----
manifest=json.loads((source/'creation-manifest.json').read_text(encoding='utf-8'))
expected={f'CHR-{role}-{action}' for role in ROLES for action in FRAMES}
⋮----
media={}
⋮----
name=f'zte_chr_{role.lower()}_{action.lower()}_final.png'
src=source/'candidates'/name
gif=source/'previews'/f'{role.lower()}-{action.lower()}.gif'
⋮----
a=argparse.ArgumentParser()
⋮----
p=a.parse_args()
```

## File: sprites/build_sprite_contact_sheet.py
```python
#!/usr/bin/env python3
"""Build a compact visual QA sheet + machine-readable anomaly report.

This is deliberately deterministic and model-free: it does not decide semantic
correctness, but it catches common production defects and makes human semantic
review of large batches fast.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "art/incoming/final-sprites"
DEFAULT_OUT = ROOT / "art/production/batch-contact-sheet.png"
DEFAULT_REPORT = ROOT / "art/production/batch-qa-report.json"
FX_RE = re.compile(r"^zte_fx_(?:0[0-9]|1[0-7])_final\.png$")
CHR_RE = re.compile(r"^zte_chr_(?:op|tech|log|eng)_(idle|walk|work|carry|repair|celeb)_final\.png$")
CHR_EXPECTED = {"idle": 6, "walk": 8, "work": 10, "carry": 8, "repair": 10, "celeb": 8}
⋮----
def alpha_bbox(im: Image.Image)
⋮----
def inspect(path: Path) -> dict
⋮----
im = Image.open(path).convert("RGBA")
a = im.getchannel("A")
hist = a.histogram()
pixels = im.width * im.height
visible = sum(hist[8:]) / pixels
bbox = alpha_bbox(im)
issues: list[str] = []
edge_clear = True
bbox_ratio = 0.0 if not bbox else ((bbox[2]-bbox[0])*(bbox[3]-bbox[1]))/pixels
⋮----
x0=(i%4)*128; y0=(i//4)*128
cell=a.crop((x0,y0,x0+128,y0+128))
⋮----
edges=(cell.crop((0,0,128,4)),cell.crop((0,124,128,128)),cell.crop((0,0,4,128)),cell.crop((124,0,128,128)))
⋮----
expected=CHR_EXPECTED[m.group(1)]
⋮----
x0=(i%4)*256; y0=(i//4)*256
cell=a.crop((x0,y0,x0+256,y0+256))
bb=cell.getbbox()
⋮----
h=cell.histogram()
cov=sum(h[8:])/(256*256)
⋮----
edges=(cell.crop((0,0,256,8)),cell.crop((0,248,256,256)),cell.crop((0,0,8,256)),cell.crop((248,0,256,256)))
⋮----
pad = max(4, round(min(im.size)*0.04))
edge_clear = x0 >= pad and y0 >= pad and x1 <= im.width-pad and y1 <= im.height-pad
⋮----
def checker(size: tuple[int, int], block=16) -> Image.Image
⋮----
out = Image.new("RGB", size, (235,235,235))
d = ImageDraw.Draw(out)
⋮----
def make_sheet(paths: list[Path], results: list[dict], out: Path, cols=6)
⋮----
rows = max(1, math.ceil(len(paths)/cols))
sheet = Image.new("RGB", (cols*tile_w, rows*tile_h), (32,32,36))
draw = ImageDraw.Draw(sheet)
font = ImageFont.load_default()
⋮----
preview = im.copy()
⋮----
bg = checker((276,276))
px = (276-preview.width)//2
py = (276-preview.height)//2
⋮----
status = "PASS" if result["pass"] else "CHECK"
⋮----
msg = ", ".join(result["issues"])
⋮----
def main() -> int
⋮----
ap = argparse.ArgumentParser()
⋮----
args = ap.parse_args()
paths = [Path(x) for x in args.files] if args.files else sorted(args.input.glob(args.pattern))
paths = [p for p in paths if p.exists() and p.stat().st_size > 0]
⋮----
results = [inspect(p) for p in paths]
⋮----
report = {
```

## File: sprites/build_tech_review_board.py
```python
#!/usr/bin/env python3
"""Deterministic review-only TECH atlases visualization; never promotes assets.

Reads canonical-format 4x4 transparent PNG review candidates. Produces a
static side-by-side 42px day/night comparison and an animated GIF; both are
labeled explicitly as candidates, not Android screenshots or approved art.
"""
⋮----
ACTIONS = ('IDLE', 'WALK', 'WORK', 'CARRY', 'REPAIR', 'CELEB')
FRAMES = {'IDLE': 6, 'WALK': 8, 'WORK': 10, 'CARRY': 8, 'REPAIR': 10, 'CELEB': 8}
BG = (13, 22, 34)
TILE = (26, 38, 54)
INK = (229, 239, 245)
MUTED = (149, 174, 190)
AQUA = (76, 222, 228)
AMBER = (246, 182, 86)
⋮----
def font(n: int, bold: bool = False)
⋮----
name = 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
⋮----
path = Path(folder) / name
⋮----
def tiles(root: Path)
⋮----
report = json.loads((root / 'review-report.json').read_text(encoding='utf-8'))
expected = [f'CHR-TECH-{a}' for a in ACTIONS]
⋮----
records = {}
⋮----
action = item['asset_id'].split('-')[-1]
⋮----
atlas_path = root / item['staged_png']
⋮----
rgba = im.convert('RGBA')
frames = []
⋮----
frame = rgba.crop((x, y, x + 256, y + 256))
⋮----
def label(d, x, y, message, *, size=18, color=INK, bold=False)
⋮----
def checker(surface: Image.Image, xy, side, night: bool)
⋮----
base = (19, 32, 46, 255) if night else (203, 222, 232, 255)
alt = (24, 40, 55, 255) if night else (192, 214, 227, 255)
squares = Image.new('RGBA', (side, side), base)
d = ImageDraw.Draw(squares)
step = max(8, side // 5)
⋮----
def place(surface: Image.Image, frame: Image.Image, x, y, side)
⋮----
resized = frame.resize((side, side), Image.Resampling.LANCZOS)
⋮----
def board(records, out: Path)
⋮----
im = Image.new('RGBA', (W, H), BG + (255,))
d = ImageDraw.Draw(im)
⋮----
# Most discriminative frames of each rigged cycle, sampled without changing their order.
order = [0, len(frames)//4, len(frames)//2, 3*len(frames)//4]
⋮----
fx = x+22+k*132
⋮----
# Frame is rendered at a literal 42 px, centered on a 146 px test panel.
⋮----
ambiguity = item.get('automated_visual_risks', {}).get('foot_profile_ambiguous_frames', 0)
note = (f'Leg visibility flagged: {ambiguity}/{len(frames)}' if action in ('WALK', 'CARRY')
⋮----
def lower_limb_closeups(records, out: Path)
⋮----
"""Unretouched walking/carrying foot crops and literal 42px previews.

    A mass- or geometry-only gate cannot decide whether overlapping boots
    are visually understandable. This supplemental board preserves the
    exact candidate pixels and makes the ambiguous frames easy to inspect.
    It never infers a semantic pass, contact validity or release eligibility.
    """
⋮----
surface = Image.new('RGBA', (w, h), BG + (255,))
d = ImageDraw.Draw(surface)
⋮----
frame_box = (55, 120, 215, 248)
⋮----
base_y = 150 + row * 485
⋮----
# A fixed crop region across frames is essential: independently
# bounding every foot would conceal its movement/occlusion.
crop = frames[index].crop(frame_box).resize(
⋮----
def footfall_motion(records, out: Path)
⋮----
"""Loop all eight ORIGINAL canonical WALK/CARRY frames at fixed framing.

    Preview cadence is deliberately labeled as an inspection aid, not as the
    game's playback speed or semantic proof of foot-plant stability.
    """
frames_out = []
⋮----
surface = Image.new('RGBA', (1100, 526), BG + (255,))
⋮----
x = 24 + index * 548
⋮----
crop = frames[tick].crop((55, 120, 215, 248))
zoom = crop.resize((400, 320), Image.Resampling.NEAREST)
⋮----
# Conservative *physical-pixel* 42px preview, not dp.
⋮----
def animated(records, out: Path)
⋮----
still = []
⋮----
img = Image.new('RGB', (W,H), BG)
d=ImageDraw.Draw(img)
⋮----
x=18+i*170
⋮----
def main()
⋮----
ap=argparse.ArgumentParser()
⋮----
args=ap.parse_args()
⋮----
rec=tiles(args.source)
```

## File: sprites/character_acceptance_policy.py
```python
#!/usr/bin/env python3
"""Production-first admission policy for character *candidates*, not strict DONE.

Keep structural/technical defects blocking while recording artistic concerns as
advisories. A candidate accepted here is NOT approved for runtime promotion.
"""
⋮----
PRODUCTION_FIRST_MODE = "production-first"
⋮----
# Strict floors remain unchanged for the established review process. In the
# production-first lane an action must still have measurable nonzero motion.
STRICT_MEAN_FLOORS = {"WALK": 0.12, "WORK": 0.10, "CARRY": 0.12,
PRODUCTION_MEAN_FLOORS = {"WALK": 0.04, "WORK": 0.04, "CARRY": 0.04,
STRICT_LOWER_FLOORS = {"WALK": 0.22, "CARRY": 0.19}
PRODUCTION_LOWER_FLOORS = {"WALK": 0.05, "CARRY": 0.04}
⋮----
# These are visual-quality warnings, not evidence of invalid files or missing
# actors. Unknown/new blocking flags are intentionally NOT waived.
DEFERRED_ART_FLAGS = frozenset({
⋮----
def motion_floor(action: str, *, production_first: bool, lower_body: bool = False) -> float
⋮----
action = action.upper()
strict = STRICT_LOWER_FLOORS if lower_body else STRICT_MEAN_FLOORS
relaxed = PRODUCTION_LOWER_FLOORS if lower_body else PRODUCTION_MEAN_FLOORS
⋮----
def visual_risk_decision(risk: dict, *, production_first: bool) -> tuple[list[str], list[str]]
⋮----
"""Return (blocking_flags, deferred_review_flags) without approving art."""
flags = list(dict.fromkeys(risk.get("flags") or []))
⋮----
if not flags:  # Fail closed for an unknown blocking assessment.
```

## File: sprites/character_anchor_pair_salvage.py
```python
"""Conservative recovery of one full-body subject from two-person role anchors.

Works only on a known foreground segmentation mask. Never guesses a person's
identity, invents limbs or marks assets approved. Ambiguous overlaps remain
rejected and recorded rather than silently generating unusable role families.
"""
⋮----
def _components(mask: Image.Image)
⋮----
thumb=mask.convert("L").resize((256,256),Image.Resampling.NEAREST)
data=thumb.load()
seen=set()
found=[]
⋮----
queue=deque([(x,y)])
⋮----
area=0
bounds=[x,y,x+1,y+1]
⋮----
def salvage_two_full_body_subjects(raw:Image.Image, isolated:Image.Image)
⋮----
"""Return (RGB isolated character, evidence) or (None, rejection reason).

    This is deliberately narrow: two similarly sized, distinct, tall and
    horizontally separated foreground components must be visible. An
    overlapping double person or a disconnected machine is not recoverable.
    """
rgb=raw.convert("RGB")
⋮----
pairs=_components(isolated.getchannel("A"))
⋮----
width=box[2]-box[0]
height=box[3]-box[1]
⋮----
# Avoid cropping a second worker or important overlapping object.
⋮----
# Keep only the dominant full-height connected figure (ties go to the
# leftmost subject). Preserve its painterly pixels with no new synthesis.
chosen=first if first_n>second_n else min(first,second,key=lambda b:b[0])
scale=4
pad=12
left=max(0,chosen[0]*scale-pad)
top=max(0,chosen[1]*scale-pad)
right=min(1024,chosen[2]*scale+pad)
bottom=min(1024,chosen[3]*scale+pad)
⋮----
region=rgb.crop((left,top,right,bottom))
⋮----
# Median-of-corners neutral background approximates the original source
# without adding a second actor, halo, or painted prop.
corners=(rgb.getpixel((0,0)),rgb.getpixel((1023,0)),
bg=tuple(sorted(pixel[k] for pixel in corners)[1:3][0] for k in range(3))
canvas=Image.new("RGB",(1024,1024),bg)
x=(1024-region.width)//2
y=(1024-region.height)//2
```

## File: sprites/character_approved_idle_fallback.py
```python
"""Fallback role identity from an existing strict-DONE IDLE sprite.

This is ONLY a source for *new* GPU regeneration when fresh text-to-image
anchors fail repeatedly. It never returns a valid review decision, never
changes the manifest, never updates runtime resources and cannot invent an
unreviewed engineer IDLE. Source pixels must pass full-body and isolation QA
in the caller before use.
"""
⋮----
_ALLOWED = {"OP", "LOG", "TECH"}
_ITEM = re.compile(r"^\|\s*(CHR-(?:OP|LOG|TECH)-IDLE)\s*\|")
⋮----
"""Return a neutral 1024x1024 RGB seed or a specific rejection reason."""
role = role.upper()
⋮----
source_id = f"CHR-{role}-IDLE"
⋮----
statuses = []
⋮----
filename = sprite_dir / f"zte_chr_{role.lower()}_idle_final.png"
⋮----
frame = src.convert("RGBA").crop((0, 0, 256, 256))
⋮----
alpha = frame.getchannel("A").point(lambda a: 255 if a >= 64 else 0)
bbox = alpha.getbbox()
⋮----
# Reject a pair of separate foreground people, even if combined bbox
# is still tall. A large secondary connected alpha component cannot be
# treated as an approved single-character identity anchor.
foreground = alpha.load()
visited: set[tuple[int, int]] = set()
components: list[int] = []
⋮----
stack = [(xx, yy)]
⋮----
area = 0
⋮----
# Use the original, already-approved character pixels. Rescale without
# re-generating the face or drawing a new helmet/costume.
crop = frame.crop(bbox)
desired_height = 770
desired_width = round(width * desired_height / height)
⋮----
resized = crop.resize((desired_width, desired_height), Image.Resampling.LANCZOS)
background = Image.new("RGB", (1024, 1024), (139, 139, 139))
target_x = (1024 - desired_width) // 2
target_y = (1024 - desired_height) // 2
```

## File: sprites/character_cargo_identity_lock.py
```python
"""Conservative 256px sprite cargo/hand-region lock for CARRY actions.

The first action frame supplies the unchanged waist-and-cargo pixels. When
subsequent frames retain the same character scale, foot pivot and alignment,
copy that bounded region back with feathered vertical boundaries, leaving
leg/boot motion intact. This cannot establish semantics or grant strict DONE.
"""
⋮----
def lock_cargo_region(frame: Image.Image, first_frame: Image.Image)
⋮----
"""Return (candidate_rgba, applied_bool, diagnostic_reason)."""
⋮----
ref_box = reference.getchannel("A").getbbox()
dst_box = target.getchannel("A").getbbox()
⋮----
top = round(y0 + height * .38)
bottom = round(y0 + height * .72)
⋮----
mask = Image.new("L", (256, 256), 0)
brush = ImageDraw.Draw(mask)
feather = 8
⋮----
factor = min((y - top) / feather, (bottom - y - 1) / feather, 1)
```

## File: sprites/character_ground_shadow_cleanup.py
```python
"""Conservative cleanup of neutral gray ground-shadow pixels in character cells.

Never manufactures missing geometry, guesses limb positions, or approves a
sprite. Only apply when a broad bright neutral shadow extends visibly past
both lower legs. Dark/colored shadows stay for semantic review.
"""
⋮----
CELL_SIZE = (256, 256)
⋮----
def _remove_foot_gap_background(rgba: Image.Image) -> int
⋮----
"""Clear only confidently missegmented neutral background between boots.

    An AI-generated gray cast shadow can connect both boots and prevent the
    border flood-fill from reaching the open space between two lower legs.
    Resolve that gap from two separately visible feet in the final rows.
    No limb, boot or colored uniform pixel may be synthesized or repainted.
    """
bounds = rgba.getchannel("A").getbbox()
⋮----
height = bottom - top
⋮----
pixels = rgba.load()
feet = None
⋮----
xs = [x for x in range(left, right) if pixels[x, y][3] >= 120]
⋮----
runs = []
start = previous = xs[0]
⋮----
start = x
previous = x
⋮----
visible_feet = [(x0, x1) for x0, x1 in runs if x1 - x0 + 1 >= 9]
⋮----
feet = visible_feet
⋮----
upper_limit = top + round(.66 * height)
pending = deque((x, bottom - 2) for x in range(gap_left, gap_right + 1))
seen = set()
removable = []
⋮----
neutral_gray = (
⋮----
ys = [y for _, y in removable]
⋮----
def remove_baked_ground_shadow(frame: Image.Image) -> tuple[Image.Image, int]
⋮----
"""Return cleaned RGBA frame and the count of discarded gray pixels.

    A long, near-neutral cast shadow on a light gray AI generation background
    sometimes fuses to the boots in alpha. An outside-of-leg evidence check
    protects pale shoe materials from indiscriminate deletion.
    """
rgba = frame.convert("RGBA")
⋮----
# Knee-level silhouette estimates where the feet can legitimately extend.
knee_y = max(0, min(255, top + round(.79 * height)))
knee_xs = [
⋮----
start = max(0, bottom - round(.13 * height))
⋮----
candidates = []
outside = 0
⋮----
# Shadows seen in failed ENG/OP assets are flat neutral gray,
# unlike the dark textured shoes, coat and bright safety colors.
⋮----
# Don't alter white shoes, light trousers or ordinary pale details that
# stay inside the limb envelope. Ambiguous cases remain for manual review.
removed = 0
⋮----
# Even with a genuine exterior shadow, retain boots and pale cuffs
# inside the leg envelope rather than erasing every neutral pixel.
⋮----
# Most rejected ENG/LOG sprites instead have an enclosed gray region
# bridging the two boots. The outside-only pass cannot reach that shadow.
```

## File: sprites/character_head_identity_lock.py
```python
"""Conservative identity-preserving face/headgear transfer for sprite candidates.

A role's same-run IDLE frame is the visual reference; no external face model
or identity inference is involved. This never accepts semantics, never writes
runtime resources and skips poses whose full-body registration is unsafe.
"""
⋮----
FRAME_SIZE = (256, 256)
⋮----
def _head_anchor(frame: Image.Image)
⋮----
rgba = frame.convert("RGBA")
⋮----
alpha = rgba.getchannel("A")
bounds = alpha.getbbox()
⋮----
height = bottom - top
⋮----
# Centroid of the upper silhouette is less affected by a tool at waist
# height than the geometric centre of the entire character bounding box.
end = min(bottom, top + max(1, round(height * .25)))
mask = alpha.crop((left, top, right, end))
pix = mask.load()
count = weighted = 0
⋮----
centre_x = round(weighted / count) if count else (left + right) // 2
centre_y = top + round(height * .195)
⋮----
def lock_head_to_idle(frame: Image.Image, idle: Image.Image)
⋮----
"""Return (RGBA frame, applied bool, reason), no speculative approval.

    Only nearly upright, identically sized character silhouettes qualify.
    Crouching, high-arm silhouettes, small figures and strange framing retain
    the generated image for explicit manual review rather than a bad paste.
    """
target = frame.convert("RGBA")
reference = idle.convert("RGBA")
a = _head_anchor(reference)
b = _head_anchor(target)
⋮----
source_height = source_box[3] - source_box[1]
target_height = target_box[3] - target_box[1]
⋮----
piece = reference.crop((sx - width // 2, sy - height // 2,
target_head = target.crop((tx - width // 2, ty - height // 2,
# A copy from a different helmet profile, silhouette orientation or
# displaced head would form a ghost/double-face. Enforce close shape
# registration before compositing, then preserve manual review.
source_binary = [v >= 64 for v in piece.getchannel("A").getdata()]
target_binary = [v >= 64 for v in target_head.getchannel("A").getdata()]
overlap = sum(a and b for a, b in zip(source_binary, target_binary))
union = sum(a or b for a, b in zip(source_binary, target_binary))
⋮----
soft = Image.new("L", (width, height), 0)
⋮----
soft = soft.filter(ImageFilter.GaussianBlur(5))
mask = ImageChops.multiply(piece.getchannel("A"), soft)
⋮----
result = target.copy()
```

## File: sprites/character_identity_polish_mobile_review.py
```python
"""Offline Android animation comparison for *already verified* polish proposals.

Called only after the candidate bank, same-run reference atlas and all-frame
alternative have passed source/audit SHA-256 checks. This viewer never
updates game resources, certifies art or transmits the review notes.
"""
⋮----
HTML = r'''<!doctype html><html lang="fr"><head><meta charset="utf-8">
⋮----
"""rows must be supplied by the verified character identity polish builder."""
⋮----
seen: set[str] = set()
embedded: list[dict] = []
⋮----
asset_id = row["id"]
⋮----
payload = {"schemaVersion": 1, "reviewOnly": True,
serialized = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
serialized = (serialized.replace("<", "\\u003c")
```

## File: sprites/character_idle_breathing_fallback.py
```python
"""Identity-preserving emergency IDLE breathing from a validated 256px seed.

The six poses contain *only* pixels derived from the same isolated character.
No new face, helmet, costume, limbs, objects, or shadows are painted. This is a
candidate-only fallback for a failed stochastic IDLE, not semantic approval.
"""
⋮----
FRAME_SIZE=(256,256)
PHASES=(0.0,0.65,1.0,0.65,0.0,-0.35)
⋮----
def build_idle_breathing_frames(seed: Image.Image) -> list[Image.Image]
⋮----
"""Subtly expand the mid-torso while leaving the face/feet untouched."""
⋮----
base=seed.convert("RGBA")
bb=base.getchannel("A").getbbox()
⋮----
centre=(left+right)/2
height=bottom-top
mask=Image.new("L",FRAME_SIZE)
mp=mask.load()
⋮----
fraction=(y-top)/height
⋮----
weight=math.sin(math.pi*(fraction-.25)/.56)**1.5
opacity=round(255*weight)
⋮----
frames=[]
⋮----
# The geometric warp uses fractional pixels; torso-only compositing
# protects the helmet, face, boots, and the fixed Android foot pivot.
scale=1.0+.017*phase
warped=base.transform(
```

## File: sprites/character_provisional_idle_seed.py
```python
#!/usr/bin/env python3
"""Traceable *review-only* ENG IDLE reference for later GPU regeneration.

A technically QA-passing ENG-IDLE from the exact collector run in the current
canonical queue is a visual source, NOT a strict-DONE or runtime asset.
Preparing a seed never updates queue status or the application. The generator
independently runs its full subject/atlas checks before using these pixels.
"""
⋮----
SEED_DIR = Path("art/production/kaggle-provisional-idle-seed")
PNG_NAME = "zte_chr_eng_idle_final.png"
PROVENANCE = "provenance.json"
SOURCE_ID = "CHR-ENG-IDLE"
MAX_PNG_BYTES = 15 * 1024 * 1024
SINGLE_PERSON_MAX_RATIO = 0.90
⋮----
def _single_person_source(blob: bytes) -> Image.Image
⋮----
cell = source.crop((0, 0, 256, 256))
bbox = cell.getchannel("A").point(lambda alpha: 255 if alpha >= 64 else 0).getbbox()
⋮----
"""Pin a prior collector's technically passed PNG to its *current* queue ID."""
⋮----
queue = json.loads(queue_path.read_text(encoding="utf-8"))
pending = {str(row.get("id") or "") for row in queue.get("targets", [])
⋮----
master = json.loads(master_path.read_text(encoding="utf-8"))
rows = [row for row in master["assets"] if row.get("id") == SOURCE_ID]
⋮----
row = rows[0]
⋮----
names = archive.namelist()
⋮----
manifest = json.loads(archive.read("candidate-index.json"))
items = [item for item in manifest.get("assets", [])
⋮----
blob = archive.read("candidates/" + PNG_NAME)
digest = hashlib.sha256(blob).hexdigest()
⋮----
provenance = {
destination = target_directory / SEED_DIR
⋮----
def load_seed(role: str, root: Path) -> tuple[Image.Image | None, str]
⋮----
"""Load the original reviewed pixels into a neutral canvas, never approve."""
⋮----
folder = root / SEED_DIR
atlas_path = folder / PNG_NAME
evidence_path = folder / PROVENANCE
⋮----
evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
⋮----
blob = atlas_path.read_bytes()
⋮----
crop = _single_person_source(blob)
desired_height = 770
width = round(crop.width * desired_height / crop.height)
⋮----
resized = crop.resize((width, desired_height), Image.Resampling.LANCZOS)
image = Image.new("RGB", (1024, 1024), (139, 139, 139))
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
result = prepare(args.master, args.queue, args.archive,
```

## File: sprites/character_rejection_evidence.py
```python
"""Review-only sprites preserved when IDLE generation fails.

Rejected frames are never written to the incoming candidate directory.
They are strictly forensic evidence for the next GPU retry and manual QA.
"""
⋮----
IDLE_ID = re.compile(r"^CHR-(OP|TECH|LOG|ENG)-IDLE$")
CELL = 256
⋮----
"""Write unapproved frames and a provenance-readable rejection record."""
⋮----
root = Path(output_directory)
⋮----
atlas = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
⋮----
stem = asset_id.lower().replace("-", "_")
image_path = root / f"{stem}_rejected_review_only.png"
report_path = root / f"{stem}_rejected_review_only.json"
```

## File: sprites/character_repair_pose_plan.py
```python
"""Same-person ten-frame mechanical repair cycle: bounded poses, fixed stance.

This describes GPU *candidate generation* only, never QA approval or runtime.
The previous deep-kneel-to-standing pose sequence produced extreme silhouette
changes, failing the unchanged adjacent-alpha-IoU >= 0.28 structural gate.
The new poses focus action on arms/tool/torso while preserving scale, feet,
identity and the connected repair point throughout the animation.
"""
⋮----
REPAIR_POSES = (
⋮----
def repair_strength(frame_index: int, attempt: int, mode: str) -> float
⋮----
"""Bounded img2img denoising; preserve one subject across adjacent frames.

    The hand/tool scaffold supplies much of the pose, so reducing FLUX
    redraw strength should preserve consistent face/body silhouette. This
    does not waive the source, action, sheet or semantic review QA gates.
    """
⋮----
strength = .49 + attempt * .018
⋮----
strength = .48 + frame_index * .012 + attempt * .017
```

## File: sprites/character_review_matrix.py
```python
#!/usr/bin/env python3
"""Reproducible review plan for the remaining canonical CHR assets.

Never treats a generated candidate as approved; detects canonical-vs-preview
conflicts (notably CHR-TECH-WALK) and prioritizes real human/artistic review.
Pure stdlib, works on GitHub Actions and offline without Kaggle.
"""
⋮----
ACTIONS=("IDLE","WALK","WORK","CARRY","REPAIR","CELEB")
ROLES=("OP","TECH","LOG","ENG")
REVIEW={
# A review is more urgent when the asset is a walking foundation, or when a
# known semantic failure would otherwise be hidden by a different renderer.
ACTION_WEIGHT={"WALK":0,"CARRY":1,"WORK":2,"REPAIR":3,"IDLE":4,"CELEB":5}
ROLE_WEIGHT={"OP":0,"LOG":1,"ENG":2,"TECH":3}
⋮----
def build(queue:dict)->dict
⋮----
assets=queue.get("assets")
⋮----
ids=[a.get("id") for a in assets]
⋮----
done=sum(a.get("strict_status")=="DONE" for a in assets)
pending=[a for a in assets if a.get("strict_status")!="DONE"]
⋮----
rows=[]
⋮----
parts=a["id"].split("-")
⋮----
status=a.get("pipeline_status")
rejected=status in ("REJECTED_SEMANTIC","REJECTED")
reason=a.get("review_reason") or "No recorded specific defect"
# A standalone TECH review render is not the canonical Kaggle asset.
# Explicitly forbid silently equating the two.
alternate=(role=="TECH" and action in ("WALK","WORK","CARRY"))
priority=(0 if rejected else 1,ACTION_WEIGHT[action],ROLE_WEIGHT[role],a["id"])
⋮----
by_role=dict(Counter(r["role"] for r in rows))
⋮----
def markdown(report:dict)->str
⋮----
lines=[
⋮----
action=row["next_step"].replace("|","/")
⋮----
tech_pending=[row for row in report["items"] if row["role"]=="TECH"]
⋮----
rejected=[row["asset_id"] for row in tech_pending
detail=(
⋮----
def main()->int
⋮----
p=argparse.ArgumentParser()
⋮----
args=p.parse_args()
report=build(json.loads(args.queue.read_text(encoding="utf-8")))
```

## File: sprites/character_semantic_gate.py
```python
"""Image-only risk screening for full-body character animation candidates.

This detects obvious portrait/fragments and palette identity jumps, not artistry.
Even zero detected risks NEVER implies semantic or human visual approval.
"""
⋮----
def _runs(occupancy)
⋮----
count=0; active=False
⋮----
active=value
⋮----
def frame_geometry(frame:Image.Image)->dict
⋮----
rgba=frame.convert('RGBA')
alpha=rgba.getchannel('A')
opaque=alpha.point(lambda a:255 if a>=64 else 0)
bounds=opaque.getbbox()
⋮----
width=right-left; height=bottom-top
pixels=opaque.load()
y0=bottom-max(3,round(height*.18))
band_h=bottom-y0
occupancy=[
⋮----
runs=_runs(occupancy)
opaque_area=sum(pixels[x,y]>=128 for y in range(top,bottom)
ratio=height/max(width,1)
fill=opaque_area/max(width*height,1)
flags=[]
⋮----
def color_signature(frame:Image.Image)
⋮----
hist=[[0]*8 for _ in range(3)]
count=0
⋮----
def palette_distance(a,b)->float
⋮----
def celebration_arm_reach_counts(frames:list[Image.Image])->list[int]
⋮----
"""Measure arms raised *beside the head*, not head/shoulder width.

    The previous detector used the centre of the entire bounding box and
    interpreted the head itself as an upraised arm when a character stood
    off-centre. The v1.20 OP-CELEB candidate reported 8/8 active arm frames
    although every actual arm stayed down. Estimate a robust head midpoint
    from opaque pixels in the top of each frame and require upper silhouette
    mass beyond the helmet plus a lateral safety margin.

    This is a conservative reject-only proxy. Raised arms overlapping the
    head may be missed and still require explicit human review.
    """
counts=[]
⋮----
bounds=alpha.getbbox()
⋮----
height=bottom-top
⋮----
pix=alpha.load()
head_top=max(0,top+round(height*.04))
head_bottom=min(frame.height,top+round(height*.19))
head_xs=sorted(
⋮----
head_centre=head_xs[len(head_xs)//2]
lateral_margin=max(29,round(height*.15))
# Raised-fist evidence must reach helmet height. Counting through
# the shoulder band (down to 31% of body height) incorrectly treated
# a broad right shoulder as a raised arm on offset-head characters.
arm_y0=max(0,top+round(height*.04))
arm_y1=min(frame.height,top+round(height*.19))
count=sum(
⋮----
def idle_visual_activity(frames:list[Image.Image])->float
⋮----
"""Measure subtle blink/breathing changes without requiring body motion.

    Silhouette-only alpha overlap falsely rejects excellent six-frame IDLE
    animations with a fixed body and tiny facial or uniform detail changes.
    RGB + alpha differences are normalized over the visible character region.
    An exact repeated sprite still scores 0.0 and is rejected upstream.
    This is evidence of image activity only, never an artistic approval.
    """
⋮----
sampled=[
diff=0
total=0
⋮----
def head_structure_drift(frames:list[Image.Image])->float
⋮----
"""Pixel-structure drift of aligned face/headgear texture from frame zero.

    Plain RGB histograms miss cases where the entire face/helmet changes shape
    while retaining orange/white/graphite colors. Crop only the upper head
    instead of shoulders, hands or accessories; avoid model dependencies.
    This is a rejection risk, NOT face recognition or automatic approval.
    """
heads=[]
⋮----
bb=alpha.getbbox()
⋮----
band=alpha.crop((0,top,256,top+max(1,int((bottom-top)*.23))))
weighted=count=0
px=band.load()
⋮----
centre=round(weighted/count) if count else (left+right)//2
crop_x=max(0,min(188,centre-34))
crop_y=max(0,min(188,top-2))
⋮----
reference=heads[0]
result=0.0
⋮----
error=total=0
⋮----
result=max(result,error/total)
⋮----
def lower_ground_band_ratio(frame:Image.Image)->float
⋮----
"""Look for a suspicious solid ground bar beneath two narrower legs.

    A baked oval floor shadow often spans the full base of the character even
    when shoes are separated. A wide *connected horizontal run* near the bottom
    distinguishes it from naturally spread feet. This is a risk heuristic:
    passing this check is not proof of transparency or visual acceptability.
    """
alpha=frame.convert('RGBA').getchannel('A')
⋮----
pixels=alpha.load()
reference_top=max(top,bottom-round(height*.20))
reference_bottom=max(reference_top+2,bottom-round(height*.10))
needed=max(2,round((reference_bottom-reference_top)*.18))
leg_columns=[
⋮----
leg_span=max(leg_columns)-min(leg_columns)+1
# Connected dark shoes can have the *same alpha silhouette* as a cast
# floor shadow. The prior alpha-only heuristic blocked valid-looking ENG
# idle anchors, cascading into five skipped actions. Count only broad,
# nearly neutral, low-contrast ground-colored bands below the ankles.
# Preserve the strict rejection of genuine gray shadows; this is not an
# automatic semantic acceptance of the full sheet.
rgb=frame.convert('RGBA').load()
longest=0
⋮----
run=0
⋮----
neutral=(a>=96 and 70<=min(red,green,blue)<=235
⋮----
longest=max(longest,run)
⋮----
def _body_region_color_signature(frame:Image.Image,start:float,end:float)
⋮----
"""Masked RGB histogram of a stable vertical region relative to the sprite.

    The top 28% targets headgear/face; the 40%-73% region targets hands,
    equipment and carried cargo. This reports visual risk, not semantic truth.
    """
⋮----
bounds=rgba.getchannel('A').getbbox()
⋮----
height=bounds[3]-bounds[1]
top=max(0,bounds[1]+round(height*start))
bottom=min(rgba.height,max(top+1,bounds[1]+round(height*end)))
⋮----
def idle_distinct_head_clusters(frame:Image.Image)->int
⋮----
"""Count well-separated opaque heads in the top 2%-14% of the sprite.

    This detects two side-by-side workers whose shoulders touch into one
    connected silhouette. The whole-character connected-component and aspect
    checks previously missed these (LOG IDLE collector 38281126201). Limit
    this check to IDLE: raised arms or props can add upper clusters in actions.
    """
⋮----
bbox=alpha.getbbox()
⋮----
y0=top+round(height*.02)
y1=min(frame.height,top+round(height*.14))
⋮----
cutoff=max(3,round((y1-y0)*.20))
runs=[]
start=None
⋮----
present=count>=cutoff
⋮----
start=x
⋮----
center_a=(left_run[0]+left_run[1])/2
center_b=(right_run[0]+right_run[1])/2
⋮----
def _upper_head_centroid(frame:Image.Image)
⋮----
"""Approximate actor registration from the upper opaque head silhouette."""
⋮----
height=bbox[3]-bbox[1]
y0=max(0,bbox[1]+round(height*.04))
y1=min(frame.height,max(y0+1,bbox[1]+round(height*.25)))
region=alpha.crop((0,y0,frame.width,y1))
pixels=region.load()
sum_x=sum_y=count=0
⋮----
def _binary_alpha_iou(a:Image.Image,b:Image.Image)->float
⋮----
aa=a.getchannel('A').point(lambda v:255 if v>=32 else 0)
bb=b.getchannel('A').point(lambda v:255 if v>=32 else 0)
overlap=ImageChops.darker(aa,bb).histogram()[255]
union=ImageChops.lighter(aa,bb).histogram()[255]
⋮----
def action_translation_metrics(frames:list[Image.Image])->dict
⋮----
"""Detect apparent action motion due mainly to shifting the whole actor.

    A 256px WORK/REPAIR atlas can exceed the alpha-change threshold if the
    standing character slides horizontally, even with no raised forearms.
    Register the upper head silhouette and measure the pose-change remainder.
    This is a reject-only risk signal, never a semantic quality approval.
    """
⋮----
rgba=[f.convert('RGBA') for f in frames]
⋮----
anchors=[_upper_head_centroid(f) for f in rgba]
⋮----
first=anchors[0]
aligned=[]
⋮----
registered=Image.new('RGBA',frame.size,(0,0,0,0))
⋮----
raw=sum(1-_binary_alpha_iou(a,b) for a,b in zip(rgba,rgba[1:]))/(len(rgba)-1)
residual=sum(1-_binary_alpha_iou(a,b)
head_excursion=max(x for x,y in anchors)-min(x for x,y in anchors)
ratio=residual/max(raw,.001)
dominated=raw>=.15 and head_excursion>=12 and ratio<.43
⋮----
def clip_risk(frames:list[Image.Image],action:str|None=None,*,geometry_frames:list[Image.Image]|None=None)->dict
⋮----
"""Check full-frame action/palette risk, optionally isolating actor silhouette.

    Geometry-only overrides are for documented static-prop composites; all
    temporal, palette, head, ground and action checks still use full frames.
    This never grants visual or production approval.
    """
⋮----
dims=[frame_geometry(f) for f in (geometry_frames if geometry_frames is not None else frames)]
⋮----
signatures=[color_signature(frame) for frame in frames]
adjacent=[
median_aspect=statistics.median(f['aspect_ratio'] for f in dims)
median_height=statistics.median(f['bbox_height_fraction'] for f in dims)
flat=sum(f['aspect_ratio']<1.30 for f in dims)
no_feet=sum(f['bottom_segment_count']<2 for f in dims)
biggest=max(adjacent)
head_signatures=[_body_region_color_signature(f,0,.28) for f in frames]
head_changes=[
head_max=max(head_changes,default=0.0)
mid_signatures=[_body_region_color_signature(f,.40,.73) for f in frames]
mid_changes=[
mid_max=max(mid_changes,default=0.0)
head_shape_drift=(head_structure_drift(frames)
ground_band_ratios=[lower_ground_band_ratio(frame) for frame in frames]
ground_band_count=sum(value>=1.27 for value in ground_band_ratios)
idle_head_clusters=(
double_head_frames=sum(value>=2 for value in idle_head_clusters)
⋮----
action_pose_metrics={}
⋮----
action_pose_metrics=action_translation_metrics(frames)
⋮----
sizes=[f['bbox_height_fraction'] for f in dims]
# A single mysteriously shortened frame was accepted in LOG-WORK even
# though its neighbors retained normal full-body framing. Reject per-frame
# collapses instead of waiting for >=2 portrait fragments or a 2x jump.
min_relative_height=min(sizes)/max(statistics.median(sizes),.01)
⋮----
areas=[f['visible_alpha_area'] for f in dims]
mass_ratio=max(areas)/max(min(areas),1)
⋮----
blockers={'ACTION_TRANSLATION_DOMINATES_POSE_RISK',
blocking=bool(blockers.intersection(flags))
```

## File: sprites/colab_mass_factory.py
```python
#!/usr/bin/env python3
"""Google Colab high-throughput entrypoint for Zero -> Empire sprite production.

Designed for an interactive Colab GPU runtime. It clones/updates the repository,
routes to the highest-priority remaining sprite lane, and exports only fresh
candidates plus technical QA evidence. It never promotes assets to DONE.
"""
⋮----
WORK = Path('/content')
REPO = WORK / 'zero-to-empire'
OUT = WORK / 'sprite-output'
COUNT = int(os.getenv('SPRITE_COUNT', '56'))
SEED = int(os.getenv('SPRITE_SEED', str(int(time.time()) % 2_000_000_000)))
REPO_URL = os.getenv('ZERO_TO_EMPIRE_REPO', 'https://github.com/dbrckk/zero-to-empire.git')
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
⋮----
def digest(path: Path) -> str
⋮----
h = hashlib.sha256()
⋮----
def sh(*args)
⋮----
def ensure_repo()
⋮----
def ensure_gpu()
⋮----
gpu = subprocess.check_output(
⋮----
def ensure_flux()
⋮----
required = ['diffusers', 'transformers', 'accelerate', 'safetensors', 'torch', 'PIL']
missing = []
⋮----
def runtime_exists(runtime: str) -> bool
⋮----
def backlog()
⋮----
counts = {'BLD': 0, 'STATIC': 0, 'CHR': 0, 'FX': 0, 'SKIPPED_RUNTIME': 0}
manifest = REPO / 'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
⋮----
m = ROW.match(line)
⋮----
asset_id = m.group(1).strip()
runtime = m.group(4).strip()
⋮----
def main()
⋮----
incoming = REPO / 'art/incoming/final-sprites'
⋮----
before = {p.name: digest(p) for p in incoming.glob('*_final.png') if p.is_file()}
q = backlog()
⋮----
lane = 'BUILDING_FAMILIES'
effective = max(7, min(COUNT, 56))
cmd = ['python', '-u', 'tools/sprites/kaggle_building_family_factory_v16.py', '--count', str(effective), '--seed', str(SEED)]
⋮----
lane = 'STATIC'
effective = max(14, min(COUNT, 56))
cmd = ['python', '-u', 'tools/sprites/kaggle_sprite_factory.py', '--kind', 'ALL', '--count', str(effective), '--seed', str(SEED)]
⋮----
lane = 'CHARACTER_SHEETS'
effective = max(4, min(COUNT, 8))
cmd = ['python', '-u', 'tools/sprites/kaggle_character_sheet_factory_v1.py', '--count', str(effective), '--seed', str(SEED)]
⋮----
lane = 'FX_SHEETS'
effective = max(1, min(COUNT, 18))
cmd = ['python', '-u', 'tools/sprites/kaggle_fx_sheet_factory_v1.py', '--count', str(effective), '--seed', str(SEED)]
⋮----
fresh = [
⋮----
qa = OUT / 'batch-contact-sheet.png'
report = OUT / 'batch-qa-report.json'
⋮----
cdir = OUT / 'candidates'
⋮----
targets = []
⋮----
dst = cdir / f.name
⋮----
archive = shutil.make_archive(str(WORK / 'zero-to-empire-colab-sprites'), 'zip', OUT)
```

## File: sprites/export_tech_canonical_review.py
```python
#!/usr/bin/env python3
"""Stage all six canonical-format TECH animations from one deterministic textured rig.

These are visual-review CANDIDATES, never replacements for canonical PNG/WebP
or automatic strict-DONE promotions. The 24-frame articulated source is
downsampled to the existing Android 4x4 / action-frame-count contract.
"""
⋮----
ACTIONS = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}
SOURCE_FRAMES = 24
CELL = 256
⋮----
def digest(path: Path) -> str
⋮----
def selected_indices(count: int, source_count: int = SOURCE_FRAMES) -> list[int]
⋮----
result = [i * source_count // count for i in range(count)]
⋮----
def validate_index(source: Path, skin: Path) -> dict
⋮----
index = json.loads((source / "production-index.json").read_text(encoding="utf-8"))
⋮----
actions = {row.get("action"): row for row in index.get("actions", [])}
⋮----
row = actions[action]
⋮----
def stage_action(source: Path, output: Path, action: str, skin_sha: str) -> dict
⋮----
folder = source / action
manifest = json.loads((folder / "qa-manifest.json").read_text(encoding="utf-8"))
⋮----
qa = manifest.get("qa", {})
⋮----
chosen = selected_indices(ACTIONS[action])
atlas = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
frame_hashes = []
preview = []
⋮----
path = folder / "frames" / f"CHR-TECH-{action}-{index:02d}.png"
⋮----
frame = src.copy()
⋮----
scaled = frame.resize((CELL, CELL), Image.Resampling.LANCZOS)
⋮----
tile = Image.new("RGBA", (96, 96), (29, 37, 49, 255))
⋮----
stem = f"zte_chr_tech_{action.lower()}_final"
⋮----
png = output / (stem + ".png")
⋮----
technical = inspect(png, f"CHR-TECH-{action}")
⋮----
contact = Image.new("RGB", (96 * len(preview), 128), (29, 37, 49))
d = ImageDraw.Draw(contact)
⋮----
def stage(source: Path, skin: Path, output: Path) -> dict
⋮----
index = validate_index(source, skin)
items = [stage_action(source, output, action, index["source_skin_sha256"])
result = {
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser(description=__doc__)
⋮----
args = parser.parse_args()
result = stage(args.source, args.skin, args.output)
```

## File: sprites/focused_sprite_atlas.py
```python
"""Shared pivot-preserving framing for small-screen TECH preview sprites.

A *single* crop applies to every frame and every action. This prevents fake
camera motion and gives all animations the same world-space foot pivot. The
original 512px frames and canonical 128/256px variants are never modified.

All outputs are review-only; framing is NOT an artistic quality approval.
"""
⋮----
CANVAS = 512
PIVOT = (252, 449)
⋮----
"""Return a square alpha-safe view shared by *all* actions and poses.

    Bounds must cover nonzero alpha, not only opaque pixels; sparse transparent
    tool/VFX edges should not be cut to make a visually larger character.
    """
⋮----
x0=min(b[0] for b in bounds); y0=min(b[1] for b in bounds)
x1=max(b[2] for b in bounds); y1=max(b[3] for b in bounds)
⋮----
side=math.ceil((max(x1-x0,y1-y0)+2*margin)/16)*16
side=min(canvas,max(64,side))
left=max(0,min(canvas-side,round(pivot[0]-side/2)))
top=max(0,min(canvas-side,round((y0+y1-side)/2)))
crop=(left,top,left+side,top+side)
⋮----
side=crop[2]-crop[0]
⋮----
def framed_sprite(frame:Image.Image,crop:tuple[int,int,int,int],size:int)->Image.Image
⋮----
a=frame.getchannel('A').getbbox()
⋮----
def collect_frame_bounds(source:dict[str,dict],actions:tuple[str,...])->list
⋮----
bounds=[]
⋮----
bbox=im.getchannel('A').getbbox()
```

## File: sprites/generate_strict_review_backlog.py
```python
#!/usr/bin/env python3
"""Generate the strict character review backlog from the canonical master queue."""
⋮----
ROOT = Path(__file__).resolve().parents[2]
MASTER = ROOT / "art/production/master-asset-queue.json"
OUT = ROOT / "art/production/character-strict-review-backlog.md"
⋮----
def main() -> int
⋮----
queue = json.loads(MASTER.read_text(encoding="utf-8"))
remaining = [a for a in queue["assets"] if a.get("strict_status") != "DONE" and a["id"].startswith("CHR-")]
strict_done = sum(a.get("strict_status") == "DONE" for a in queue["assets"])
production = sum(
lines = [
⋮----
parts = asset["id"].split("-")
reason = asset.get("review_reason") or "Semantic review required; no specific automated defect recorded."
artifact_run = asset.get("review_artifact_run_id") or "—"
```

## File: sprites/hf_public_flux_factory.py
```python
#!/usr/bin/env python3
⋮----
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
REPORT=ROOT/'art/production/hf-public-flux-report.json'
⋮----
def fail(msg)
⋮----
def next_target()
⋮----
explicit=os.getenv('SPRITE_TARGET','').strip().upper()
rows=[]
⋮----
cols=[c.strip() for c in line.split('|')[1:-1]]
⋮----
def prompt_for(asset_id, desc)
⋮----
m=re.fullmatch(r'BLD-(\d{2})-T(\d)', asset_id)
⋮----
def isolate(im: Image.Image) -> Image.Image
⋮----
rgb=im.convert('RGB')
# Estimate background from border pixels and require low-variance border.
px=rgb.load(); w,h=rgb.size
samples=[]
⋮----
med=tuple(sorted(v[i] for v in samples)[len(samples)//2] for i in range(3))
dev=max(max(abs(v[i]-med[i]) for i in range(3)) for v in samples)
⋮----
src=rgb.load()
rgba=Image.new('RGBA',rgb.size,(0,0,0,0)); out=rgba.load()
⋮----
p=src[x,y]
d=max(abs(p[i]-med[i]) for i in range(3))
if d<=18: a=0
elif d>=42: a=255
else: a=round((d-18)*255/24)
⋮----
a=rgba.getchannel('A').filter(ImageFilter.MedianFilter(3))
⋮----
def main()
⋮----
row=next_target(); asset_id, name, desc, runtime, status=row
prompt=prompt_for(asset_id,desc)
token=os.getenv('HF_TOKEN') or None
client=Client('black-forest-labs/FLUX.1-schnell', hf_token=token, verbose=False)
api=client.view_api(return_format='dict')
⋮----
result=None; errors=[]
calls=[
⋮----
kwargs={k:v for k,v in call.items() if k!='args'}
result=client.predict(*call['args'], **kwargs)
⋮----
# Gradio commonly returns (image, seed) or a filepath.
candidate=result[0] if isinstance(result,(list,tuple)) else result
⋮----
candidate=candidate.get('path') or candidate.get('url')
⋮----
src=Path(str(candidate))
⋮----
im=Image.open(src)
isolated=isolate(im)
m=re.fullmatch(r'BLD-(\d{2})-T(\d)',asset_id)
stem=f'zte_business_{m.group(1)}_t{m.group(2)}_final'
⋮----
out=INCOMING/f'{stem}.png'
```

## File: sprites/hf_sprite_factory.py
```python
#!/usr/bin/env python3
"""Zero -> Empire free sprite generation worker."""
⋮----
ROOT = Path(__file__).resolve().parents[2]
INCOMING = ROOT / "art/incoming/final-sprites"
SPACE_URL = os.getenv("HF_SPACE_URL", "https://mcp-tools-z-image-turbo.hf.space").rstrip("/")
TOKEN = os.environ.get("HF_TOKEN", "").strip()
⋮----
def _headers(*, json_body: bool = False) -> dict[str, str]
⋮----
headers = {"User-Agent": "zero-to-empire-sprite-factory/2.0"}
⋮----
def _request(req: urllib.request.Request, timeout: int = 180) -> bytes
⋮----
body = exc.read().decode("utf-8", "replace")
⋮----
def generate(prompt: str) -> Path
⋮----
payload = {"data": [prompt, "1024x1024 ( 1:1 )", 42, 8, 3.0, True]}
post = urllib.request.Request(f"{SPACE_URL}/gradio_api/call/generate", data=json.dumps(payload).encode(), headers=_headers(json_body=True), method="POST")
response = json.loads(_request(post, timeout=60).decode())
event_id = response.get("event_id")
⋮----
get = urllib.request.Request(f"{SPACE_URL}/gradio_api/call/generate/{event_id}", headers=_headers(), method="GET")
sse = _request(get, timeout=240).decode("utf-8", "replace")
complete_data = None
current_event = None
⋮----
current_event = line.split(":", 1)[1].strip()
⋮----
complete_data = json.loads(line.split(":", 1)[1].strip())
⋮----
def find_url(value)
⋮----
url = value.get("url")
⋮----
found = find_url(child)
⋮----
image_url = find_url(complete_data)
⋮----
suffix = Path(image_url.split("?", 1)[0]).suffix.lower()
⋮----
suffix = ".img"
tmp = ROOT / ".sprite_factory_download"
⋮----
out = tmp / f"hf_master{suffix}"
⋮----
def black_to_alpha(src: Path) -> Image.Image
⋮----
im = Image.open(src).convert("RGB")
lum = im.convert("L")
alpha = lum.point(lambda p: 0 if p < 12 else min(255, int((p - 12) * 1.35))).filter(ImageFilter.GaussianBlur(0.35))
rgba = im.convert("RGBA")
⋮----
def _fit_frame(obj: Image.Image, target_side: int, scale: float, opacity: int, rotation: float = 0.0) -> Image.Image
⋮----
factor = min(target_side / obj.width, target_side / obj.height) * scale
frame = obj.resize((max(1, round(obj.width * factor)), max(1, round(obj.height * factor))), Image.Resampling.LANCZOS)
⋮----
frame = frame.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True)
⋮----
f = target_side / max(frame.size)
frame = frame.resize((max(1, round(frame.width * f)), max(1, round(frame.height * f))), Image.Resampling.LANCZOS)
⋮----
def _animated_sheet(master: Image.Image, *, label: str, target_side: int, scales, opacities, rotations, y_offsets) -> Image.Image
⋮----
bbox = master.getbbox()
⋮----
obj = master.crop(bbox)
sheet = Image.new("RGBA", (512, 256), (0, 0, 0, 0))
⋮----
frame = _fit_frame(obj, target_side, scale, opacity, rotation)
⋮----
x = x0 + (128 - frame.width) // 2
y = max(y0 + 6, min(y0 + (128 - frame.height) // 2 + yoff, y0 + 122 - frame.height))
⋮----
def make_fx00(master)
⋮----
def make_fx01(master)
⋮----
def make_fx02(master)
⋮----
def make_fx03(master)
⋮----
def make_fx04(master)
⋮----
def make_energy_pulse(master: Image.Image, label: str) -> Image.Image
⋮----
def make_fx05(master): return make_energy_pulse(master, "FX-05")
def make_fx06(master): return make_energy_pulse(master, "FX-06")
⋮----
def make_fx07(master)
⋮----
def validate_fx_sheet(sheet: Image.Image) -> None
⋮----
cell = sheet.crop((x0, y0, x0 + 128, y0 + 128))
⋮----
a = cell.getchannel("A")
edges = [a.crop((0,0,128,4)), a.crop((0,124,128,128)), a.crop((0,0,4,128)), a.crop((124,0,128,128))]
⋮----
SPECS = {
⋮----
def main() -> int
⋮----
target = os.getenv("SPRITE_TARGET", "FX-03").upper()
⋮----
sheet = maker(black_to_alpha(generate(prompt)))
⋮----
out = INCOMING / output_name
```

## File: sprites/hf_static_manifest_factory.py
```python
#!/usr/bin/env python3
"""Generate one static manifest asset through the free HF Space.

Supported fast GPU lane: buildings, Power Core, vehicles, props and static
terrain/infrastructure modules. Animation sheets remain on dedicated workers.

Exit code 75 means the free GPU quota is exhausted. Batch workflows use this to
stop immediately instead of wasting runner time retrying every remaining asset.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
INCOMING = ROOT / "art/incoming/final-sprites"
SPACE_URL = os.getenv("HF_SPACE_URL", "https://mcp-tools-z-image-turbo.hf.space").rstrip("/")
TOKEN = os.environ.get("HF_TOKEN", "").strip()
ASSET_ID = os.environ.get("SPRITE_TARGET", "").strip().upper()
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
SUPPORTED = ("BLD-", "CORE-", "VEH-", "PRP-", "TER-")
TARGET_SIDE = {"BLD": 2048, "CORE": 1536, "VEH": 1536, "PRP": 1024, "TER": 1024}
QUOTA_EXIT = 75
⋮----
def headers(json_body=False)
⋮----
h = {"User-Agent": "zero-to-empire-manifest-factory/1.4"}
⋮----
def request(req, timeout=240)
⋮----
body = exc.read().decode("utf-8", "replace")
low = body.lower()
⋮----
def manifest_item(asset_id: str)
⋮----
m = ROW.match(line)
⋮----
def prompt_for(asset_id, name, description)
⋮----
kind = asset_id.split("-", 1)[0]
contract = {
⋮----
def generate(prompt: str) -> Image.Image
⋮----
payload = {"data": [prompt, "1024x1024 ( 1:1 )", 42, 8, 3.0, True]}
req = urllib.request.Request(f"{SPACE_URL}/gradio_api/call/generate", data=json.dumps(payload).encode(), headers=headers(True), method="POST")
event_id = json.loads(request(req, 60).decode()).get("event_id")
⋮----
req = urllib.request.Request(f"{SPACE_URL}/gradio_api/call/generate/{event_id}", headers=headers(), method="GET")
sse = request(req, 240).decode("utf-8", "replace")
data = None
event = None
⋮----
event = line.split(":", 1)[1].strip()
⋮----
data = json.loads(line.split(":", 1)[1].strip())
⋮----
low = sse.lower()
⋮----
def find_url(v)
⋮----
u = v.get("url")
⋮----
r = find_url(child)
⋮----
url = find_url(data)
⋮----
raw = request(urllib.request.Request(url, headers=headers(), method="GET"), 120)
tmp = ROOT / ".sprite_factory_download"
⋮----
safe_id = re.sub(r"[^A-Za-z0-9_.-]+", "_", ASSET_ID or "static")
p = tmp / f"{safe_id}.img"
⋮----
def main()
⋮----
kind=rid.split("-",1)[0]
final = normalize(isolate(generate(prompt_for(rid,name,desc))), TARGET_SIDE[kind])
⋮----
out=INCOMING/(Path(runtime).stem+".png")
```

## File: sprites/identity_locked_walk_candidate.py
```python
#!/usr/bin/env python3
"""Deterministic identity-preserving WALK alternative, NOT approved game art.

Reuses one canonical FULL-BODY source frame for the entire 8-frame loop.
Conservative, smoothed gait mesh motion changes boots/legs and counter-swings
sleeves without asking an independent text-to-image generator to redraw faces.
All output goes to build/; never overwrite the canonical sprite or runtime.
This is an experimental review candidate: geometry is not skeletal animation.
"""
⋮----
ROLES={"OP":2,"LOG":0,"ENG":0,"TECH":0}
SIZE=256
N_FRAMES=8
⋮----
"""Vectorized bilinear sampling without transparent-edge dark fringes."""
⋮----
sx=np.clip(src_x,0,width-1)
sy=np.clip(src_y,0,height-1)
x0=np.floor(sx).astype(np.int32);y0=np.floor(sy).astype(np.int32)
x1=np.minimum(x0+1,width-1);y1=np.minimum(y0+1,height-1)
u=(sx-x0)[...,None];v=(sy-y0)[...,None]
prem=source.astype(np.float32)/255.
⋮----
interp=(prem[y0,x0]*(1-u)*(1-v)+prem[y0,x1]*u*(1-v)
alpha=interp[:,:,3:4]
rgb=np.where(alpha>1e-5,interp[:,:,:3]/np.maximum(alpha,1e-5),0)
⋮----
def warp(anchor:Image.Image,t:float,amplitude:float=14)->Image.Image
⋮----
"""Continuously blended ankle-led stride and sleeve counter-motion."""
⋮----
array=np.asarray(anchor)
⋮----
phase=math.tau*(t%1.)
# Earlier mesh split the legs sharply at x=128 starting above the hips,
# creating a triangular tear/open gap through the crotch on real OP frame
# 3. Start deformation below the thighs and feather the left/right blend.
lower=np.clip((yy-156)/82,0,1)**1.3
side=np.tanh((xx-128)/19)
lateral=amplitude*math.sin(phase)*lower*side
swing=np.maximum(0,np.sin(phase)*(-side))
foot_lift=2.5*swing*lower
upper=np.clip((yy-58)/60,0,1)*np.clip((155-yy)/43,0,1)
outward=np.clip((np.abs(xx-128)-21)/16,0,1)
arms=-4*math.sin(phase)*side*upper*outward
# Second quadrature channel prevents duplicate poses at mirrored
# sine phases, without moving the planted boots or changing costume.
torso_breath=.85*math.cos(phase)*np.clip((182-yy)/88,0,1)
rgba=sample_premultiplied(array,xx-lateral-arms,
⋮----
def source_frame(path:Path,source_index:int)->Image.Image
⋮----
x=source_index%4*SIZE;y=source_index//4*SIZE
frame=atlas.crop((x,y,x+SIZE,y+SIZE))
bounds=frame.getchannel('A').getbbox()
⋮----
def render(source:Path,role:str,out:Path,amplitude:float=14)->dict
⋮----
role=role.upper()
⋮----
original=source_frame(source,ROLES[role])
⋮----
raw_frames=[warp(anchor,n/N_FRAMES,amplitude) for n in range(N_FRAMES)]
cleaned=[remove_baked_ground_shadow(frame) for frame in raw_frames]
frames=[item[0] for item in cleaned]
removed_frame_shadow=sum(item[1] for item in cleaned)
risk=clip_risk(frames,'WALK')
⋮----
sheet=Image.new("RGBA",(1024,1024))
⋮----
dest=out/f"CHR-{role}-WALK-identity-locked-REVIEW.png"
⋮----
grid=Image.new("RGB",(SIZE*N_FRAMES,SIZE),(25,34,46))
⋮----
source_digest=hashlib.sha256(source.read_bytes()).hexdigest()
candidate_digest=hashlib.sha256(dest.read_bytes()).hexdigest()
report={
⋮----
def main()
⋮----
parser=argparse.ArgumentParser()
⋮----
args=parser.parse_args()
path=args.source or Path("art/incoming/final-sprites")/f"zte_chr_{args.role.lower()}_walk_final.png"
```

## File: sprites/integrate_fx04_runtime.py
```python
#!/usr/bin/env python3
"""Idempotently integrate FX-04 steam vent into purchase feedback."""
⋮----
ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "app/src/main/java/com/zerotoempire/game/PurchaseImpactVfx.kt"
text = PATH.read_text()
⋮----
anchor = '''    val dustSheet = remember(context) {
replacement = anchor + '''    val steamSheet = remember(context) {
⋮----
text = text.replace(anchor, replacement, 1)
⋮----
anchor2 = '''        if (!reduced) {
steam = '''        val steamFrame = when {
⋮----
text = text.replace(anchor2, steam, 1)
```

## File: sprites/integrate_fx05_runtime.py
```python
#!/usr/bin/env python3
"""Idempotently wire validated FX-05 cyan energy pulse into the power-core plaza."""
⋮----
ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "app/src/main/java/com/zerotoempire/game/AscendantCityWorld.kt"
⋮----
def main() -> None
⋮----
text = PATH.read_text()
⋮----
old_sheet = "    val pulseSheet = remember { ImageBitmap.imageResource(context.resources, R.drawable.zte_fx_06_final) }\n"
new_sheet = (
⋮----
text = text.replace(old_sheet, new_sheet, 1)
⋮----
old_state = "    var pulseToken by remember { mutableIntStateOf(0) }\n    var pulseFrame by remember { mutableIntStateOf(-1) }\n\n"
new_state = (
⋮----
text = text.replace(old_state, new_state, 1)
⋮----
old_surface = """        Surface(
new_surface = """        Canvas(Modifier.size(110.dp)) {
⋮----
text = text.replace(old_surface, new_surface, 1)
```

## File: sprites/integrate_fx06_runtime.py
```python
#!/usr/bin/env python3
"""Idempotently wire the validated FX-06 warm pulse sheet into the power-core tap UI."""
⋮----
ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "app/src/main/java/com/zerotoempire/game/AscendantCityWorld.kt"
⋮----
IMPORT_ANCHOR = "package com.zerotoempire.game\n\n"
RUNTIME_IMPORTS = """import android.provider.Settings\nimport androidx.compose.runtime.LaunchedEffect\nimport androidx.compose.runtime.getValue\nimport androidx.compose.runtime.mutableIntStateOf\nimport androidx.compose.runtime.setValue\nimport androidx.compose.ui.graphics.ImageBitmap\nimport androidx.compose.ui.platform.LocalContext\nimport androidx.compose.ui.res.imageResource\nimport androidx.compose.ui.unit.IntOffset\nimport androidx.compose.ui.unit.IntSize\nimport kotlinx.coroutines.delay\n"""
⋮----
OLD = '''@Composable
⋮----
NEW = '''@Composable
⋮----
def main() -> None
⋮----
text = PATH.read_text()
⋮----
text = text.replace(IMPORT_ANCHOR, IMPORT_ANCHOR + RUNTIME_IMPORTS, 1)
text = text.replace(OLD, NEW, 1)
```

## File: sprites/integrate_fx07_runtime.py
```python
#!/usr/bin/env python3
"""Idempotently wire FX-07 construction dust/debris into purchase impact feedback."""
⋮----
ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "app/src/main/java/com/zerotoempire/game/PurchaseImpactVfx.kt"
⋮----
def main() -> None
⋮----
text = PATH.read_text()
⋮----
text = text.replace(
⋮----
anchor = '''        drawImage(
replacement = anchor + '''
⋮----
text = text.replace(anchor, replacement, 1)
```

## File: sprites/kaggle_building_family_factory_v11.py
```python
#!/usr/bin/env python3
"""Strict sequential FLUX building-family factory.

v11: run-77 hardening: monotonic display scale, stricter starter tiers,
anti-slab/alpha-hole guards, lower img2img drift, and family-growth QA.
"""
⋮----
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
BLD=re.compile(r'^BLD-(\d{2})-T([0-6])$')
⋮----
DNA={
DELTA={
# Run-77 families 04/06/07 are deliberately deprioritized until the new guard proves itself.
PRIORITY=(5,8,9,10,12,13,11,4,6,7,3,0,1,2)
STRENGTH={1:.30,2:.36,3:.42,4:.48,5:.54,6:.60}
TARGET_SCALE={0:.54,1:.59,2:.64,3:.69,4:.74,5:.79,6:.84}
⋮----
def rows()
⋮----
m=ROW.match(line)
⋮----
bm=BLD.fullmatch(aid)
⋮----
def select(items,count)
⋮----
by={}
⋮----
rank={f:n for n,f in enumerate(PRIORITY)};out=[]
⋮----
g=sorted(by[fam],key=lambda x:x['tier'])
⋮----
def prompts(i)
⋮----
tier=i['tier'];starter=(tier==0)
s=(f"AAA premium 2.5D strategy building family {i['family']:02d} tier {tier}. "
d=(f"Premium mobile strategy building master. Fixed family DNA: {DNA[i['family']]}. {DELTA[tier]}. "
⋮----
def load_encode()
⋮----
t=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda')
p=FluxPipeline.from_pretrained(FLUX,text_encoder_2=t,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda')
⋮----
def load_render()
⋮----
tr=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda')
base=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=tr,torch_dtype=torch.float16,device_map='cuda')
⋮----
img=FluxImg2ImgPipeline.from_pipe(base);img.vae.to(device='cuda',dtype=torch.float16)
⋮----
def border(im)
⋮----
rgb=im.convert('RGB');w,h=rgb.size;step=max(1,min(w,h)//128);pts=[]
⋮----
vals=[sum(p)/3 for p in pts];mean=sum(vals)/len(vals);sd=(sum((v-mean)**2 for v in vals)/len(vals))**.5
q=sorted(pts,key=sum)[len(pts)//3:2*len(pts)//3];bg=tuple(sum(p[k] for p in q)//len(q) for k in range(3))
⋮----
def isolate(im)
⋮----
rgb=im.convert('RGB');w,h=rgb.size;bg,sd,chroma=border(rgb)
⋮----
px=rgb.load();mask=Image.new('L',(w,h));mp=mask.load()
⋮----
p=px[x,y];d=((p[0]-bg[0])**2+(p[1]-bg[1])**2+(p[2]-bg[2])**2)**.5
⋮----
mask=mask.filter(ImageFilter.GaussianBlur(.55));out=rgb.convert('RGBA');out.putalpha(mask);return out
⋮----
def components(alpha)
⋮----
sm=alpha.resize((128,128),Image.Resampling.BILINEAR);px=sm.load();seen=set();out=[]
⋮----
q=deque([(x,y)]);seen.add((x,y));pts=[]
⋮----
def internal_hole_ratio(alpha)
⋮----
# Estimate transparent holes fully enclosed by foreground on a small binary mask.
sm=alpha.resize((96,96),Image.Resampling.BILINEAR).point(lambda p:255 if p>=48 else 0)
px=sm.load();seen=set();q=deque()
⋮----
holes=sum(1 for y in range(96) for x in range(96) if px[x,y]==0 and (x,y) not in seen)
fg=sum(1 for y in range(96) for x in range(96) if px[x,y]>0)
⋮----
def slab_score(alpha)
⋮----
bb=alpha.getbbox()
⋮----
a=alpha.crop(bb).resize((128,128),Image.Resampling.BILINEAR);px=a.load()
rows=[]
⋮----
# Persistent near-full-width lower silhouette is usually a baked floor/platform.
⋮----
def finish(raw,tier)
⋮----
m=isolate(raw);cs=components(m.getchannel('A'))
⋮----
xs=[p[0] for p in cs[0]];ys=[p[1] for p in cs[0]];w,h=m.size
box=(max(0,int(min(xs)*w/128)-30),max(0,int(min(ys)*h/128)-30),min(w,int((max(xs)+1)*w/128)+30),min(h,int((max(ys)+1)*h/128)+30))
crop=m.crop(box);bb=crop.getbbox()
⋮----
crop=crop.crop(bb);a0=crop.getchannel('A')
holes=internal_hole_ratio(a0);slab=slab_score(a0)
⋮----
side=2048;target=TARGET_SCALE[tier]
scale=min(side*target/crop.width,side*(target-.03)/crop.height)
crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
out=Image.new('RGBA',(side,side));out.alpha_composite(crop,((side-crop.width)//2,side-int(side*.09)-crop.height))
a=out.getchannel('A');cov=sum(a.histogram()[8:])/(side*side)
⋮----
pad=int(side*.07)
⋮----
def mask64(im):return im.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
⋮----
def iou(a,b)
⋮----
A=mask64(a);B=mask64(b);pa=A.load();pb=B.load();inter=union=0
⋮----
aa=pa[x,y]>0;bb=pb[x,y]>0;inter+=aa and bb;union+=aa or bb
⋮----
def centroid(im)
⋮----
a=mask64(im);px=a.load();pts=[(x,y) for y in range(64) for x in range(64) if px[x,y]>0]
⋮----
def bbox_size(im)
⋮----
bb=im.getchannel('A').getbbox();return (0,0) if not bb else (bb[2]-bb[0],bb[3]-bb[1])
⋮----
def family_qa(recs)
⋮----
adj=[iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
⋮----
centers=[centroid(r[1]) for r in recs];drift=max(((x-centers[0][0])**2+(y-centers[0][1])**2)**.5 for x,y in centers)
⋮----
sizes=[bbox_size(r[1]) for r in recs];areas=[w*h for w,h in sizes]
⋮----
def main()
⋮----
ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=42);ap.add_argument('--seed',type=int,default=43117);args=ap.parse_args()
items=select(list(rows()),max(1,args.count));print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
⋮----
INCOMING.mkdir(parents=True,exist_ok=True);emb={};t,enc=load_encode()
⋮----
del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=load_render();by={}
⋮----
accepted=[];rejected=0
⋮----
group.sort(key=lambda x:x['tier']);recs=[];previous=None;failed=False
⋮----
pe,ppe=emb[i['id']];gen=torch.Generator(device='cuda').manual_seed(args.seed+fam*1000+i['tier']*17)
⋮----
raw=base(height=1024,width=1024,num_inference_steps=6,guidance_scale=0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',generator=gen).images[0];mode='anchor'
⋮----
raw=img(image=previous,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=STRENGTH.get(i['tier'],.45),num_inference_steps=10,guidance_scale=0,output_type='pil',generator=gen).images[0];mode='img2img'
final,cov=finish(raw,i['tier']);recs.append((i,final,cov));previous=raw.convert('RGB')
⋮----
print(f"KAGGLE_REJECTED={i['id']} stage=render reason={type(e).__name__}: {e}",flush=True);failed=True;rejected+=1;break
⋮----
p=INCOMING/f"{i['stem']}.png";final.save(p,'PNG',optimize=True);accepted.append(i['id'])
```

## File: sprites/kaggle_building_family_factory_v13.py
```python
#!/usr/bin/env python3
"""Zero -> Empire FLUX building-family factory v13.

Goals: preserve family identity, force visible T0->T6 growth, and produce clean
transparent masters without deleting internal grey/metallic surfaces.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / 'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING = ROOT / 'art/incoming/final-sprites'
FLUX = 'aniketppanchal/flux.1-schnell-nf4-pkg'
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
BLD = re.compile(r'^BLD-(\d{2})-T([0-6])$')
⋮----
DNA = {
DELTA = {
# Start with families that showed some useful evolution in previous runs. Known
# pathological 04/06/07 remain late until the new segmentation path is proven.
PRIORITY = (13, 5, 8, 9, 10, 12, 11, 4, 6, 7, 3, 0, 1, 2)
STRENGTH = {1:.34, 2:.42, 3:.50, 4:.58, 5:.66, 6:.72}
STEPS = {0:5, 1:4, 2:4, 3:5, 4:5, 5:6, 6:6}
RETRIES = {0:4, 1:3, 2:3, 3:3, 4:3, 5:3, 6:3}
⋮----
def rows()
⋮----
m = ROW.match(line)
⋮----
bm = BLD.fullmatch(aid)
⋮----
def select(items, count)
⋮----
by = {}
⋮----
rank = {f:n for n,f in enumerate(PRIORITY)}
out = []
⋮----
group = sorted(by[fam], key=lambda x:x['tier'])
⋮----
def prompts(i)
⋮----
identity = f"AAA premium mobile 2.5D strategy building. Same persistent family {i['family']:02d}. Fixed DNA: {DNA[i['family']]}. {DELTA[i['tier']]}. "
camera = "Exactly one connected building, 34 degree three-quarter orthographic camera, same orientation and camera center at every tier, bottom-center grounding, upper-left key light, cool fill, restrained cyan or warm emissives. "
isolation = "Studio cutout render on a perfectly flat uniform neutral medium-gray background touching every image edge. Background only, no visible floor. No platform card, terrain slab, road, horizon, scenery, vignette, gradient or cast ground plane. "
integrity = "Preserve facade, production core, roof orientation and structural anchors from the previous tier. Every new part is physically attached to the main building. No people, workers, vehicles, arrows, signs, labels, readable text, pseudo-text, letters, numbers, logos, watermark, UI, detached props, particles, debris, loose cables or disconnected pieces. Materials are continuous and intact. "
starter = "Tier zero is unmistakably early-game and compact: one storey, low silhouette, sparse machinery, no tower, crane, gantry, upper deck or megastructure mass. " if i['tier'] == 0 else ""
⋮----
def load_encode()
⋮----
t5 = T5EncoderModel.from_pretrained(FLUX, subfolder='text_encoder_2', torch_dtype=torch.float16, device_map='cuda')
pipe = FluxPipeline.from_pretrained(FLUX, text_encoder_2=t5, transformer=None, vae=None, torch_dtype=torch.float16, device_map='cuda')
⋮----
def load_render()
⋮----
tr = FluxTransformer2DModel.from_pretrained(FLUX, subfolder='transformer', torch_dtype=torch.float16, device_map='cuda')
base = FluxPipeline.from_pretrained(FLUX, text_encoder=None, text_encoder_2=None, tokenizer=None, tokenizer_2=None, transformer=tr, torch_dtype=torch.float16, device_map='cuda')
⋮----
img = FluxImg2ImgPipeline.from_pipe(base)
⋮----
def border_stats(im)
⋮----
rgb = im.convert('RGB'); w,h = rgb.size; step = max(1, min(w,h)//128); pts=[]
⋮----
vals = [sum(p)/3 for p in pts]; mean = sum(vals)/len(vals)
sd = (sum((v-mean)**2 for v in vals)/len(vals))**.5
q = sorted(pts, key=sum)[len(pts)//3:2*len(pts)//3]
bg = tuple(sum(p[k] for p in q)//len(q) for k in range(3))
⋮----
def edge_connected_alpha(im)
⋮----
"""Remove only background-like pixels connected to image edges.

    Unlike global chroma-distance masking this cannot punch transparent holes into
    enclosed metallic surfaces merely because their colour resembles the studio bg.
    """
rgb = im.convert('RGB'); w,h = rgb.size
⋮----
# Segment on 256px proxy for speed and topology, then upscale softly.
proxy = rgb.resize((256,256), Image.Resampling.BILINEAR)
px = proxy.load(); W=H=256
def dist(p)
seen=set(); q=deque()
⋮----
# Local tolerance permits gentle background compression/noise while preventing
# traversal through stronger object edges.
⋮----
p=q.popleft()
⋮----
alpha = Image.new('L',(W,H),255); ap=alpha.load()
⋮----
# Slight erosion of background boundary removes halos without eating internals.
alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.55))
alpha = alpha.resize((w,h), Image.Resampling.BILINEAR)
out = rgb.convert('RGBA'); out.putalpha(alpha)
⋮----
def components(alpha)
⋮----
sm=alpha.resize((128,128),Image.Resampling.BILINEAR); px=sm.load(); seen=set(); out=[]
⋮----
q=deque([(x,y)]); seen.add((x,y)); pts=[]
⋮----
def ground_slab_score(alpha)
⋮----
sm=alpha.resize((128,128),Image.Resampling.BILINEAR); px=sm.load(); rows=[]
⋮----
def internal_hole_score(alpha)
⋮----
sm=alpha.resize((96,96),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0); px=sm.load()
exterior=set(); q=deque()
⋮----
inner={(x,y) for y in range(96) for x in range(96) if px[x,y]==0}-exterior
largest=0
⋮----
start=inner.pop(); comp={start}; q=deque([start])
⋮----
largest=max(largest,len(comp))
⋮----
def finish(raw,tier)
⋮----
m=edge_connected_alpha(raw); a0=m.getchannel('A'); cs=components(a0)
⋮----
dominance=len(cs[0])/sum(map(len,cs))
⋮----
slab=ground_slab_score(a0)
⋮----
hole=internal_hole_score(a0)
# Small windows/cavities are legitimate; only large accidental holes fail.
⋮----
xs=[p[0] for p in cs[0]]; ys=[p[1] for p in cs[0]]; w,h=m.size
box=(max(0,int(min(xs)*w/128)-36),max(0,int(min(ys)*h/128)-36),min(w,int((max(xs)+1)*w/128)+36),min(h,int((max(ys)+1)*h/128)+36))
crop=m.crop(box); bb=crop.getbbox()
⋮----
crop=crop.crop(bb); side=2048
maxw=.70 if tier==0 else .78; maxh=.60 if tier==0 else .78
scale=min(side*maxw/crop.width, side*maxh/crop.height)
crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
out=Image.new('RGBA',(side,side)); out.alpha_composite(crop,((side-crop.width)//2,side-int(side*.10)-crop.height))
a=out.getchannel('A'); cov=sum(a.histogram()[8:])/(side*side)
⋮----
pad=int(side*.08)
⋮----
def mask64(im): return im.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
⋮----
def iou(a,b)
⋮----
A=mask64(a);B=mask64(b);pa=A.load();pb=B.load();inter=union=0
⋮----
aa=pa[x,y]>0; bb=pb[x,y]>0; inter+=aa and bb; union+=aa or bb
⋮----
def bbox_metrics(im)
⋮----
bb=mask64(im).getbbox()
⋮----
def family_qa(recs)
⋮----
adj=[iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
⋮----
cov=[r[2] for r in recs]
severe_drops=sum(1 for a,b in zip(cov,cov[1:]) if b<a*.90)
⋮----
growth=cov[-1]/max(cov[0],1e-9)
⋮----
boxes=[bbox_metrics(r[1]) for r in recs]; cx0=boxes[0][2]
drift=max(abs(b[2]-cx0) for b in boxes)
⋮----
def render_with_retries(i, previous, pe, ppe, base, img, seed)
⋮----
errors=[]
⋮----
attempt_seed=seed + attempt*7919
gen=torch.Generator(device='cuda').manual_seed(attempt_seed)
⋮----
raw=base(height=1024,width=1024,num_inference_steps=STEPS[i['tier']],guidance_scale=0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',generator=gen).images[0]
mode='anchor'
⋮----
strength=min(.78,max(.28,STRENGTH.get(i['tier'],.5)+(attempt-1)*.035))
raw=img(image=previous,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=strength,num_inference_steps=STEPS[i['tier']],guidance_scale=0,output_type='pil',generator=gen).images[0]
mode=f'img2img-s{strength:.2f}'
⋮----
def main()
⋮----
ap=argparse.ArgumentParser(); ap.add_argument('--count',type=int,default=28); ap.add_argument('--seed',type=int,default=43117); args=ap.parse_args()
items=select(list(rows()),max(1,args.count)); print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
⋮----
emb={}; t5,enc=load_encode()
⋮----
tr,base,img=load_render(); by={}
⋮----
accepted=[]; rejected=0
⋮----
group.sort(key=lambda x:x['tier']); recs=[]; previous=None; failed=False
⋮----
print(f"KAGGLE_REJECTED={i['id']} stage=render reason={e}",flush=True); failed=True; rejected+=1; break
⋮----
p=INCOMING/f"{i['stem']}.png"; final.save(p,'PNG',optimize=True); accepted.append(i['id'])
```

## File: sprites/kaggle_building_family_factory_v14.py
```python
#!/usr/bin/env python3
"""FLUX building-family factory v14: short prompts + monotonic tier envelopes."""
⋮----
ROOT=Path(__file__).resolve().parents[2]; MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'; INCOMING=ROOT/'art/incoming/final-sprites'; BUILD_QUEUE=ROOT/'art/production/controlled-building-regen-queue.json'
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'; ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$"); BLD=re.compile(r'^BLD-(\d{2})-T([0-6])$')
DNA={0:'micro foundry kiosk, rust steel, amber furnace',1:'fabrication shop, chamfered storefront, loading bay',2:'furnace works, steel shell, twin stacks',3:'assembly hub, dark hall, robotic spine, feeder bays',4:'precision factory, graphite shell, CNC bays',5:'energy-cell works, square alloy shell, amber core',6:'coolant plant, silver graphite shell, cyan pipes',7:'automation works, wide tech factory, twin gantries',8:'heavy forge, armored base, warm forge core',9:'nanofab complex, pearl graphite block, cyan ring',10:'orbital works, dark alloy base, circular cradle',11:'actuator works, press house, articulated frames',12:'phase foundry, pearl alloy base, containment ring',13:'stellar works, dark pearl base, four-part crown'}
TIER={0:'tiny one-storey starter; no tower or crane',1:'small reinforced upgrade; one attached module',2:'medium industrial upgrade; wider footprint',3:'large automated upgrade; compact central tower',4:'advanced upgrade; two attached wings',5:'megastructure; large upper assembly',6:'ultimate; tall prestige crown and heroic machinery'}
PRIORITY=(13,5,8,9,10,12,11,4,6,7,3,0,1,2); STRENGTH={1:.34,2:.42,3:.50,4:.58,5:.66,6:.72}; STEPS={0:5,1:4,2:4,3:5,4:5,5:6,6:6}; RETRIES={0:4,1:3,2:3,3:3,4:3,5:3,6:3}
ENV={0:(.50,.44),1:(.56,.50),2:(.62,.56),3:(.68,.62),4:(.74,.68),5:(.80,.74),6:(.84,.80)}
def rows()
⋮----
catalog={}
⋮----
m=ROW.match(line)
⋮----
aid,_,_,runtime,status=[x.strip() for x in m.groups()]; bm=BLD.fullmatch(aid)
⋮----
q=json.loads(BUILD_QUEUE.read_text(encoding='utf-8')); controlled=[]
⋮----
aid=str(item.get('id','')).upper()
⋮----
def select(items,count)
⋮----
by={}
⋮----
rank={f:n for n,f in enumerate(PRIORITY)}; out=[]
⋮----
g=sorted(by[fam],key=lambda x:x['tier'])
⋮----
def prompts(i)
⋮----
# Intentionally short: keep all semantic constraints inside CLIP/T5 limits.
short=f"AAA 2.5D strategy building. {DNA[i['family']]}. {TIER[i['tier']]}. One connected isolated building. Gray studio background."
detail=(f"Same family upgraded in place. {DNA[i['family']]}. {TIER[i['tier']]}. 34-degree orthographic view. "
⋮----
def load_encode()
⋮----
t=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda'); p=FluxPipeline.from_pretrained(FLUX,text_encoder_2=t,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda'); return t,p
def load_render()
⋮----
tr=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda'); base=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=tr,torch_dtype=torch.float16,device_map='cuda'); base.vae.to(device='cuda',dtype=torch.float16); img=FluxImg2ImgPipeline.from_pipe(base); img.vae.to(device='cuda',dtype=torch.float16); return tr,base,img
def border(im)
⋮----
rgb=im.convert('RGB');w,h=rgb.size;step=max(1,min(w,h)//128);pts=[]
⋮----
vals=[sum(p)/3 for p in pts];mean=sum(vals)/len(vals);sd=(sum((v-mean)**2 for v in vals)/len(vals))**.5;q=sorted(pts,key=sum)[len(pts)//3:2*len(pts)//3];bg=tuple(sum(p[k] for p in q)//len(q) for k in range(3));return bg,sd,max(bg)-min(bg)
def isolate(im)
⋮----
rgb=im.convert('RGB');w,h=rgb.size;bg,sd,chroma=border(rgb)
⋮----
px=rgb.load(); seen=set(); q=deque();
⋮----
def dist(p):return ((p[0]-bg[0])**2+(p[1]-bg[1])**2+(p[2]-bg[2])**2)**.5
⋮----
p=q.popleft()
⋮----
mask=Image.new('L',(w,h),255);mp=mask.load()
⋮----
mask=mask.filter(ImageFilter.GaussianBlur(.7));out=rgb.convert('RGBA');out.putalpha(mask);return out
def comps(alpha)
⋮----
sm=alpha.resize((128,128),Image.Resampling.BILINEAR);px=sm.load();seen=set();out=[]
⋮----
q=deque([(x,y)]);seen.add((x,y));pts=[]
⋮----
def slab_score(alpha)
⋮----
sm=alpha.resize((128,128),Image.Resampling.BILINEAR);px=sm.load();rows=[sum(px[x,y]>=32 for x in range(6,122))/116 for y in range(78,124)];return sum(v>.76 for v in rows)/len(rows)
def finish(raw,tier)
⋮----
m=isolate(raw);cs=comps(m.getchannel('A'))
⋮----
xs=[p[0] for p in cs[0]];ys=[p[1] for p in cs[0]];w,h=m.size;box=(max(0,int(min(xs)*w/128)-24),max(0,int(min(ys)*h/128)-24),min(w,int((max(xs)+1)*w/128)+24),min(h,int((max(ys)+1)*h/128)+24));crop=m.crop(box);bb=crop.getbbox()
⋮----
crop=crop.crop(bb);side=2048;mw,mh=ENV[tier];scale=min(side*mw/crop.width,side*mh/crop.height);crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS);out=Image.new('RGBA',(side,side));out.alpha_composite(crop,((side-crop.width)//2,side-int(side*.08)-crop.height));a=out.getchannel('A');cov=sum(a.histogram()[8:])/(side*side)
⋮----
pad=int(side*.06)
⋮----
def mask64(im):return im.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
def iou(a,b)
⋮----
A=mask64(a);B=mask64(b);pa=A.load();pb=B.load();inter=union=0
⋮----
for x in range(64):aa=pa[x,y]>0;bb=pb[x,y]>0;inter+=aa and bb;union+=aa or bb
⋮----
def bbox(im)
⋮----
b=mask64(im).getbbox();return (0,0,0,0) if not b else (b[2]-b[0],b[3]-b[1],(b[0]+b[2])/2,(b[1]+b[3])/2)
def family_qa(recs)
⋮----
adj=[iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
⋮----
cov=[r[2] for r in recs]
⋮----
drops=sum(b<a*.90 for a,b in zip(cov,cov[1:]))
⋮----
boxes=[bbox(r[1]) for r in recs];cx=boxes[0][2]
⋮----
def render(i,prev,pe,ppe,base,img,seed)
⋮----
errs=[]
⋮----
gen=torch.Generator(device='cuda').manual_seed(seed+attempt*7919)
⋮----
if prev is None:raw=base(height=1024,width=1024,num_inference_steps=STEPS[i['tier']],guidance_scale=0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',generator=gen).images[0];mode='anchor'
⋮----
s=min(.80,max(.12,STRENGTH[i['tier']]+(attempt-1)*.04));raw=img(image=prev,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=s,num_inference_steps=STEPS[i['tier']],guidance_scale=0,output_type='pil',generator=gen).images[0];mode=f'img2img-s{s:.2f}'
⋮----
def main()
⋮----
ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=28);ap.add_argument('--seed',type=int,default=43117);args=ap.parse_args();items=select(list(rows()),max(1,args.count));print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
⋮----
INCOMING.mkdir(parents=True,exist_ok=True);emb={};t,enc=load_encode()
⋮----
del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=load_render();by={}
⋮----
accepted=[];rejected=0
⋮----
group.sort(key=lambda x:x['tier']);recs=[];prev=None;failed=False
⋮----
except Exception as e:print(f"KAGGLE_REJECTED={i['id']} stage=render reason={e}",flush=True);failed=True;break
⋮----
p=INCOMING/f"{i['stem']}.png";final.save(p,'PNG',optimize=True);accepted.append(i['id']);print(f"KAGGLE_VALIDATED={p.relative_to(ROOT)} coverage={cov:.1%} {why}",flush=True)
```

## File: sprites/kaggle_building_family_factory_v15.py
```python
#!/usr/bin/env python3
"""Building factory v15.2: multi-anchor search with live semantic/technical QA."""
⋮----
HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('v14',HERE/'kaggle_building_family_factory_v14.py')
v14=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(v14)
⋮----
ANCHORS=4
BRANCHES=2
CONTEXT_RETRIES=3
⋮----
def prompts(i)
⋮----
dna=v14.DNA[i['family']]; tier=v14.TIER[i['tier']]
short=(f"AAA mobile isometric FINISHED INDUSTRIAL FACTORY. {dna}. {tier}. One connected completed production building only. Flat gray studio background.")
detail=(f"Finished operating factory upgraded in place. {dna}. {tier}. 34-degree orthographic view. Preserve facade, production core and roof direction; all additions attached. "
⋮----
def boom_score(final)
⋮----
"""Detect crane-like thin long horizontal structures high above the main mass."""
a=np.array(final.getchannel('A'))>24
⋮----
x0,x1=xs.min(),xs.max(); y0,y1=ys.min(),ys.max(); w=max(1,x1-x0+1); h=max(1,y1-y0+1)
top_end=y0+max(1,int(h*.42)); rows=[]
⋮----
xx=np.where(a[y,x0:x1+1])[0]
⋮----
span=xx[-1]-xx[0]+1
⋮----
best=cur=0
⋮----
cur=cur+1 if hit else 0; best=max(best,cur)
# A crane boom tends to be long but only a few pixels thick; substantial roof masses are thicker.
thin_limit=max(4,int(h*.065))
⋮----
def anchor_score(final,cov)
⋮----
slab=v14.slab_score(final.getchannel('A')); boom=boom_score(final); target_penalty=abs(cov-.105)
⋮----
def live_gate(recs,new_final,new_cov,tier)
⋮----
reasons=[]
slab=v14.slab_score(new_final.getchannel('A'))
boom=boom_score(new_final)
⋮----
box=v14.bbox(new_final)
⋮----
prev=recs[-1][1]; prev_cov=recs[-1][2]
ident=v14.iou(prev,new_final)
⋮----
start_cx=v14.bbox(recs[0][1])[2]
⋮----
start=recs[0][2]; minimum={4:1.28,5:1.45,6:1.70}[tier]
⋮----
def branch_score(recs)
⋮----
cov=[r[2] for r in recs]; adj=[v14.iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
boxes=[v14.bbox(r[1]) for r in recs]; cx=boxes[0][2]; drift=max(abs(b[2]-cx) for b in boxes)
slabs=max(v14.slab_score(r[1].getchannel('A')) for r in recs)
booms=max(boom_score(r[1]) for r in recs)
growth=cov[-1]/max(cov[0],1e-6)
score=min(adj)*2.0 + min(growth,3.0) - drift*.05 - slabs*3.2 - booms*1.8
⋮----
def render_contextual(i,prev,recs,pe,ppe,base,img,seed,report)
⋮----
last=[]
⋮----
msg=','.join(reasons);last.append(msg);report['live_rejections']+=1
⋮----
def main()
⋮----
ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=56);ap.add_argument('--seed',type=int,default=73117);args=ap.parse_args()
items=v14.select(list(v14.rows()),max(1,args.count));print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
⋮----
v14.INCOMING.mkdir(parents=True,exist_ok=True);emb={};t,enc=v14.load_encode()
⋮----
del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=v14.load_render();by={}
⋮----
report={'engine':'v15.2-live-semantic-validation','anchor_attempts':0,'branch_attempts':0,'context_attempts':0,'live_rejections':0,'early_aborts':0,'families':[]}
accepted=[];rejected=0
⋮----
group.sort(key=lambda x:x['tier']);t0=group[0];pe0,ppe0=emb[t0['id']];anchors=[]
⋮----
sc=anchor_score(final,cov);slab=v14.slab_score(final.getchannel('A'));boom=boom_score(final)
⋮----
anchors.sort(key=lambda x:x[0],reverse=True);branches=[]
⋮----
report['branch_attempts']+=1;recs=[(t0,final0,cov0)];prev=raw0;failed=False
⋮----
report['early_aborts']+=1;print(f'KAGGLE_BRANCH_EARLY_ABORT=BLD-{fam:02d} branch={a+1} tier={i["tier"]} reason={e}',flush=True);failed=True;break
⋮----
branches.sort(key=lambda x:x[0],reverse=True);famrec={'family':fam,'anchors_generated':len(anchors),'branches_completed':len(branches)}
⋮----
p=v14.INCOMING/f"{i['stem']}.png";final.save(p,'PNG',optimize=True);accepted.append(i['id']);print(f'KAGGLE_VALIDATED={p.relative_to(v14.ROOT)} coverage={cov:.1%} selected_branch={a+1} score={bscore:.3f}',flush=True)
```

## File: sprites/kaggle_building_family_factory_v16_10.py
```python
#!/usr/bin/env python3
"""Building factory v16.4: footprint-locked two-phase family evolution.

Wave85 proved that prose-only anti-ground instructions are insufficient. v16.4
changes the source dynamics: very conservative tier evolution, a hard lower-mass
footprint prior, and tier-specific growth that adds attached mass without asking
FLUX for a surrounding site. Live QA remains strict; this version does not weaken
slab acceptance to manufacture yield.
"""
⋮----
HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('v15',HERE/'kaggle_building_family_factory_v15.py')
v15=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(v15)
v14=v15.v14
V15_ANCHOR_SCORE=v15.anchor_score
⋮----
# Phase A (T0-T3): preserve massing. Phase B (T4-T6): add detail/attached volumes
# without the high denoise that caused wave85 to invent a new ground/site plane.
⋮----
FAMILY={
SHAPE={
TIER={
STYLE=('premium AAA mobile strategy industrial asset, stylized 2.5D, 34-degree orthographic three-quarter camera, '
⋮----
# Positive spatial formulation: describe what fills the lower silhouette instead of
# repeatedly naming a floor/site. The model should see one product-like object.
FOOTPRINT=(
⋮----
def prompts(i)
⋮----
fam=FAMILY[i['family']]; shape=SHAPE[i['family']]; tier=TIER[i['tier']]
short=f'Centered isolated industrial factory product asset. {shape}. {tier}. One solid connected object on perfectly flat uniform neutral gray background.'
⋮----
phase='Build only the primary architectural massing. Prefer large contiguous wall/roof shapes over small decorative pieces.'
⋮----
phase='Preserve the approved massing and silhouette. Add detail inside or directly onto existing walls/roof; do not redesign the object footprint.'
detail=(f'{STYLE}. Family DNA: {fam}. Tier instruction: {tier}. {phase} '
⋮----
def silhouette_metrics(final)
⋮----
m=v14.mask64(final); b=m.getbbox()
⋮----
x0,y0,x1,y1=b; w=max(1,x1-x0);h=max(1,y1-y0);px=m.load();total=upper=lower=top=0
split=y0+int(h*.48);top_end=y0+max(1,int(h*.22));base0=y0+int(h*.72);base_rows=[]
⋮----
row=0
⋮----
def v164_anchor_score(final,cov)
⋮----
base=V15_ANCHOR_SCORE(final,cov);s=silhouette_metrics(final);pen=0.
⋮----
# Prefer a substantial building base, but not a nearly full-width thin card.
⋮----
score=base-pen
⋮----
# Preserve strict slab gate. Add a tier-dependent adjacent-identity floor so late
# tiers cannot replace the source with a fresh scene even if coverage grows.
V15_LIVE_GATE=v15.live_gate
⋮----
def v164_slab_score(alpha)
⋮----
"""Detect a detached/site-like lower card from silhouette geometry.

    A real factory may legitimately become wider near its base. The forbidden
    pattern is a thin, abrupt lower shelf/card: several consecutive rows that
    jump materially wider than the rows immediately above and stay nearly flat.
    """
sm=alpha.resize((128,128),v14.Image.Resampling.BILINEAR)
px=sm.load()
widths=[]
⋮----
xs=[x for x in range(4,124) if px[x,y]>=32]
⋮----
score=0.0
⋮----
above=[aw for ay,aw in widths if y-12 <= ay <= y-4 and aw>0]
⋮----
ref=float(np.median(above))
# Require an abrupt lateral shelf, not merely a broad continuous wall.
⋮----
# Normalize against the lower silhouette depth. A genuine thin card creates
# a sustained shelf signal; ordinary wall widening should remain near zero.
lower_rows=max(1,sum(1 for y,w in widths if y>=82 and w>0))
⋮----
# Keep the strict no-site-card rule, but measure detached lateral expansion
# rather than treating a legitimate broad building base as a floor slab.
⋮----
def normalized_silhouette_iou(a,b)
⋮----
"""Compare shape after removing pure scale/position differences.
    Near-1.0 means the tier is basically the same silhouette resized.
    """
ma=a.getchannel('A').point(lambda p:255 if p>=32 else 0)
mb=b.getchannel('A').point(lambda p:255 if p>=32 else 0)
ba=ma.getbbox(); bb=mb.getbbox()
⋮----
ca=ma.crop(ba).resize((128,128),v14.Image.Resampling.NEAREST)
cb=mb.crop(bb).resize((128,128),v14.Image.Resampling.NEAREST)
pa,pb=ca.load(),cb.load(); inter=union=0
⋮----
aa=pa[x,y]>0; bval=pb[x,y]>0
⋮----
def alpha_halo_ratio(final)
⋮----
"""Ratio of low-alpha fringe pixels to solid sprite pixels.
    Large values usually indicate cast-shadow/site-smear that survived cutout.
    """
a=np.asarray(final.getchannel('A'),dtype=np.uint8)
solid=np.count_nonzero(a>=160)
fringe=np.count_nonzero((a>=8)&(a<96))
⋮----
def v164_live_gate(recs,new_final,new_cov,tier)
⋮----
ident=v14.iou(recs[-1][1],new_final)
floor={1:.45,2:.42,3:.39,4:.36,5:.34,6:.32}[tier]
⋮----
norm=normalized_silhouette_iou(recs[-1][1],new_final)
anchor_norm=normalized_silhouette_iou(recs[0][1],new_final)
ceiling={1:.975,2:.960,3:.945,4:.935,5:.925,6:.915}[tier]
anchor_ceiling={1:.985,2:.955,3:.925,4:.895,5:.865,6:.835}[tier]
# Early tiers must visibly change from the previous tier. Late tiers may
# refine an already-evolved silhouette, but only if cumulative departure
# from T0 is strong enough. This prevents clone ladders without forcing
# every prestige/detail tier to redesign the footprint from scratch.
⋮----
halo=alpha_halo_ratio(new_final)
```

## File: sprites/kaggle_building_family_factory_v16.py
```python
#!/usr/bin/env python3
"""Building factory v17: family-aware structural tier evolution.

Fixes the clone-ladder failure seen on BLD-12 by making every tier prompt describe
an architectural massing change, not a scale/detail pass. It deliberately reuses
v16.10's strict technical/semantic gates; this module changes generation pressure,
not acceptance criteria.
"""
⋮----
HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('v1610', HERE / 'kaggle_building_family_factory_v16_10.py')
v1610 = importlib.util.module_from_spec(SPEC)
⋮----
v15 = v1610.v15
v14 = v1610.v14
⋮----
# More image-to-image freedom than v16.10. The strict v16.10 live gate remains
# active, so extra freedom cannot silently promote unrelated scenes/site cards.
⋮----
TIER = {
⋮----
# Family-specific evolution nouns stop the generic Tech Company vocabulary from
# leaking into Reality Engine, Moon Colony, Foundry, Gateway, etc.
EVOLUTION = {
⋮----
REALITY_TIER = {
⋮----
REALITY_STRENGTH = {1:.56, 2:.64, 3:.72, 4:.75, 5:.79, 6:.80}
⋮----
FAMILY_TIER = {
⋮----
def tier_instruction(family,tier)
⋮----
REJECTION_LEDGER = HERE.parents[1] / 'art' / 'production' / 'generation-rejection-ledger.json'
⋮----
TRANSCENDENT_TIER = {
⋮----
def rejection_hints(i)
⋮----
hints=[]
⋮----
data=json.loads(REJECTION_LEDGER.read_text(encoding='utf-8'))
aid=str(i['id']).upper()
⋮----
prefix=str(row.get('target_prefix','')).upper()
hint=str(row.get('prompt_hint','')).strip()
⋮----
# Newer evidence is more specific. Keep enough room for contamination bans;
# the previous 30-word cap truncated the newest BLD-13 rejection memory.
merged=' '.join(hints[-2:])
⋮----
CLIP_FAMILY = {
⋮----
def prompts(i)
⋮----
family = i['family']
tier = i['tier']
fam = v1610.FAMILY[family]
instruction = tier_instruction(family,tier)
memory = rejection_hints(i)
⋮----
short = (
⋮----
detail = (
⋮----
ORIGINAL_RENDER = v14.render
⋮----
def family_aware_render(i, prev, pe, ppe, base, img, seed)
⋮----
"""Give BLD-12 enough img2img freedom to produce real structural evolution."""
tier = int(i['tier'])
family=int(i['family'])
⋮----
# High-risk families may need an early text-to-image reset to break clone ladders.
# BLD-13 deliberately does NOT reset at T3: run 35564401834 proved that the
# mid-family reset can replace the architectural DNA between T2 and T3.
reset_tiers={12:{1,3},13:{1}}
⋮----
old = v14.STRENGTH[tier]
⋮----
def architectural_band_fill(final, lo, hi)
⋮----
"""Mask fill inside the sprite bbox for a relative vertical band."""
alpha=np.asarray(final.getchannel('A'),dtype=np.uint8)
⋮----
h=max(1,y1-y0)
ya=y0+int(lo*h); yb=max(ya+1,y0+int(hi*h))
band=alpha[ya:yb,x0:x1]>=32
⋮----
V15_BRANCH_SCORE=v15.branch_score
⋮----
def branch_score(recs)
⋮----
family=int(recs[0][0]['family'])
# Families repeatedly rejected for opaque site-card/platform contamination.
# Reject those candidates before semantic review instead of wasting a full batch.
⋮----
signatures=[]
⋮----
upper=architectural_band_fill(final,.20,.50)
lower=architectural_band_fill(final,.58,.88)
⋮----
offenders=[x for x in signatures if x[2]>.76 and x[1]<.58]
⋮----
details=','.join(f'{aid}(upper={upper:.2f},lower={lower:.2f})' for aid,upper,lower in offenders)
⋮----
adj=[v1610.normalized_silhouette_iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
anchor=[v1610.normalized_silhouette_iou(recs[0][1],recs[n][1]) for n in range(1,len(recs))]
⋮----
# Generic guard against the common failure where apparent progression is
# mostly canvas occupancy/scale while the normalized silhouette stays the same.
generic_failures=[]
⋮----
failures=[]
⋮----
aspects=[]
⋮----
bb=im.getchannel('A').getbbox()
```

## File: sprites/kaggle_building_family_factory_v17.py
```python
#!/usr/bin/env python3
"""Building factory v17: family-aware structural tier evolution.

Fixes the clone-ladder failure seen on BLD-12 by making every tier prompt describe
an architectural massing change, not a scale/detail pass. It deliberately reuses
v16.10's strict technical/semantic gates; this module changes generation pressure,
not acceptance criteria.
"""
⋮----
HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('v1610', HERE / 'kaggle_building_family_factory_v16_10.py')
v1610 = importlib.util.module_from_spec(SPEC)
⋮----
v15 = v1610.v15
v14 = v1610.v14
⋮----
# More image-to-image freedom than v16.10. The strict v16.10 live gate remains
# active, so extra freedom cannot silently promote unrelated scenes/site cards.
⋮----
TIER = {
⋮----
# Family-specific evolution nouns stop the generic Tech Company vocabulary from
# leaking into Reality Engine, Moon Colony, Foundry, Gateway, etc.
EVOLUTION = {
⋮----
REALITY_TIER = {
⋮----
REALITY_STRENGTH = {1:.56, 2:.64, 3:.72, 4:.75, 5:.79, 6:.80}
⋮----
FAMILY_TIER = {
⋮----
def tier_instruction(family,tier)
⋮----
REJECTION_LEDGER = HERE.parents[1] / 'art' / 'production' / 'generation-rejection-ledger.json'
⋮----
TRANSCENDENT_TIER = {
⋮----
def rejection_hints(i)
⋮----
hints=[]
⋮----
data=json.loads(REJECTION_LEDGER.read_text(encoding='utf-8'))
aid=str(i['id']).upper()
⋮----
prefix=str(row.get('target_prefix','')).upper()
hint=str(row.get('prompt_hint','')).strip()
⋮----
# Newer evidence is more specific. Keep enough room for contamination bans;
# the previous 30-word cap truncated the newest BLD-13 rejection memory.
merged=' '.join(hints[-2:])
⋮----
CLIP_FAMILY = {
⋮----
def prompts(i)
⋮----
family = i['family']
tier = i['tier']
fam = v1610.FAMILY[family]
instruction = tier_instruction(family,tier)
memory = rejection_hints(i)
⋮----
short = (
⋮----
detail = (
⋮----
ORIGINAL_RENDER = v14.render
⋮----
def family_aware_render(i, prev, pe, ppe, base, img, seed)
⋮----
"""Give BLD-12 enough img2img freedom to produce real structural evolution."""
tier = int(i['tier'])
family=int(i['family'])
⋮----
# High-risk families may need an early text-to-image reset to break clone ladders.
# BLD-13 deliberately does NOT reset at T3: run 35564401834 proved that the
# mid-family reset can replace the architectural DNA between T2 and T3.
reset_tiers={12:{1,3},13:{1}}
⋮----
old = v14.STRENGTH[tier]
⋮----
def architectural_band_fill(final, lo, hi)
⋮----
"""Mask fill inside the sprite bbox for a relative vertical band."""
alpha=np.asarray(final.getchannel('A'),dtype=np.uint8)
⋮----
h=max(1,y1-y0)
ya=y0+int(lo*h); yb=max(ya+1,y0+int(hi*h))
band=alpha[ya:yb,x0:x1]>=32
⋮----
V15_BRANCH_SCORE=v15.branch_score
⋮----
def branch_score(recs)
⋮----
family=int(recs[0][0]['family'])
# Families repeatedly rejected for opaque site-card/platform contamination.
# Reject those candidates before semantic review instead of wasting a full batch.
⋮----
signatures=[]
⋮----
upper=architectural_band_fill(final,.20,.50)
lower=architectural_band_fill(final,.58,.88)
⋮----
offenders=[x for x in signatures if x[2]>.76 and x[1]<.58]
⋮----
details=','.join(f'{aid}(upper={upper:.2f},lower={lower:.2f})' for aid,upper,lower in offenders)
⋮----
adj=[v1610.normalized_silhouette_iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
anchor=[v1610.normalized_silhouette_iou(recs[0][1],recs[n][1]) for n in range(1,len(recs))]
⋮----
# Generic guard against the common failure where apparent progression is
# mostly canvas occupancy/scale while the normalized silhouette stays the same.
generic_failures=[]
⋮----
failures=[]
⋮----
aspects=[]
⋮----
bb=im.getchannel('A').getbbox()
```

## File: sprites/kaggle_building_family_factory.py
```python
#!/usr/bin/env python3
"""Robust sequential FLUX building-family factory for Zero -> Empire."""
⋮----
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
BLD=re.compile(r'^BLD-(\d{2})-T([0-6])$')
DNA={
DELTA={0:'starter: very small one-storey shell, low roofline, sparse machinery, no tower or gantry',1:'reinforced: retain starter shell, add one attached machinery enclosure and roof ribs',2:'industrial: retain prior structure, widen footprint, add second attached subsystem and service deck',3:'automated: retain anchors, add compact central automation tower and attached logistics conduit',4:'advanced: retain base and tower, add two attached machinery wings and denser routing',5:'megastructure: retain all prior structure, add large upper production assembly and energy routing',6:'ultimate: retain entire evolved structure, add tall central prestige crown and heroic attached machinery'}
PRIORITY=(13,5,8,9,10,12,11,4,6,7,3,0,1,2)
STRENGTH={1:.34,2:.42,3:.50,4:.58,5:.66,6:.72}
STEPS={0:5,1:4,2:4,3:5,4:5,5:6,6:6}
RETRIES={0:4,1:2,2:2,3:2,4:2,5:2,6:2}
⋮----
def rows()
⋮----
m=ROW.match(line)
⋮----
bm=BLD.fullmatch(aid)
⋮----
def select(items,count)
⋮----
by={}
⋮----
rank={f:n for n,f in enumerate(PRIORITY)}; out=[]
⋮----
g=sorted(by[fam],key=lambda x:x['tier'])
⋮----
def prompts(i)
⋮----
base=(f"AAA premium mobile 2.5D strategy building, family {i['family']:02d}, tier {i['tier']}. "
composition=("Same building upgraded in place; preserve facade, production core, roof orientation and structural anchors. "
isolation=("CUTOUT PRODUCT RENDER on a perfectly flat uniform neutral medium-gray studio background touching every image edge. "
negatives=("No people, workers, vehicles, roads, arrows, labels, signs, readable text, pseudo-text, letters, numbers, logos, watermark, UI, "
tier0=("Tier zero must be unmistakably early-game: tiny one-storey footprint, low roofline, sparse machinery, no crane, no tower, no landmark mass. " if i['tier']==0 else "")
⋮----
def load_encode()
⋮----
t=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda')
p=FluxPipeline.from_pretrained(FLUX,text_encoder_2=t,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda')
⋮----
def load_render()
⋮----
tr=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda')
base=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=tr,torch_dtype=torch.float16,device_map='cuda')
⋮----
img=FluxImg2ImgPipeline.from_pipe(base); img.vae.to(device='cuda',dtype=torch.float16)
⋮----
def border(im)
⋮----
rgb=im.convert('RGB');w,h=rgb.size;step=max(1,min(w,h)//128);pts=[]
⋮----
vals=[sum(p)/3 for p in pts];mean=sum(vals)/len(vals);sd=(sum((v-mean)**2 for v in vals)/len(vals))**.5
q=sorted(pts,key=sum)[len(pts)//3:2*len(pts)//3]
bg=tuple(sum(p[k] for p in q)//len(q) for k in range(3))
⋮----
def isolate(im)
⋮----
rgb=im.convert('RGB');w,h=rgb.size;bg,sd,chroma=border(rgb)
⋮----
px=rgb.load();mask=Image.new('L',(w,h));mp=mask.load()
⋮----
p=px[x,y];d=((p[0]-bg[0])**2+(p[1]-bg[1])**2+(p[2]-bg[2])**2)**.5
⋮----
mask=mask.filter(ImageFilter.GaussianBlur(.65));out=rgb.convert('RGBA');out.putalpha(mask);return out
⋮----
def components(alpha)
⋮----
sm=alpha.resize((128,128),Image.Resampling.BILINEAR);px=sm.load();seen=set();out=[]
⋮----
q=deque([(x,y)]);seen.add((x,y));pts=[]
⋮----
def ground_slab_score(alpha)
⋮----
sm=alpha.resize((128,128),Image.Resampling.BILINEAR);px=sm.load();rows=[]
⋮----
def internal_hole_score(alpha)
⋮----
sm=alpha.resize((96,96),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
px=sm.load(); seen=set(); holes=[]
q=deque()
⋮----
p=q.popleft()
⋮----
all_clear={(x,y) for y in range(96) for x in range(96) if px[x,y]==0}
inner=all_clear-seen
⋮----
start=inner.pop(); comp={start};q=deque([start])
⋮----
def finish(raw,tier)
⋮----
m=isolate(raw);cs=components(m.getchannel('A'))
⋮----
a0=m.getchannel('A')
slab=ground_slab_score(a0)
⋮----
hole=internal_hole_score(a0)
⋮----
xs=[p[0] for p in cs[0]];ys=[p[1] for p in cs[0]];w,h=m.size
box=(max(0,int(min(xs)*w/128)-30),max(0,int(min(ys)*h/128)-30),min(w,int((max(xs)+1)*w/128)+30),min(h,int((max(ys)+1)*h/128)+30))
crop=m.crop(box);bb=crop.getbbox()
⋮----
crop=crop.crop(bb);side=2048
maxw=.72 if tier==0 else .78; maxh=.62 if tier==0 else .78
scale=min(side*maxw/crop.width,side*maxh/crop.height)
crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
out=Image.new('RGBA',(side,side));out.alpha_composite(crop,((side-crop.width)//2,side-int(side*.10)-crop.height))
a=out.getchannel('A');cov=sum(a.histogram()[8:])/(side*side)
lo=.055 if tier==0 else .07
⋮----
pad=int(side*.08)
⋮----
def mask64(im): return im.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
def iou(a,b)
⋮----
A=mask64(a);B=mask64(b);pa=A.load();pb=B.load();inter=union=0
⋮----
aa=pa[x,y]>0;bb=pb[x,y]>0;inter+=aa and bb;union+=aa or bb
⋮----
def bbox_metrics(im)
⋮----
bb=mask64(im).getbbox()
⋮----
def family_qa(recs)
⋮----
adj=[iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
⋮----
cov=[r[2] for r in recs]
drops=sum(1 for a,b in zip(cov,cov[1:]) if b<a*.92)
⋮----
boxes=[bbox_metrics(r[1]) for r in recs]
cx0=boxes[0][2]; max_center=max(abs(b[2]-cx0) for b in boxes)
⋮----
def render_with_retries(i,previous,pe,ppe,base,img,seed)
⋮----
errors=[]
⋮----
attempt_seed=seed+attempt*7919
gen=torch.Generator(device='cuda').manual_seed(attempt_seed)
⋮----
raw=base(height=1024,width=1024,num_inference_steps=STEPS[i['tier']],guidance_scale=0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',generator=gen).images[0];mode='anchor'
⋮----
strength=min(.78,max(.28,STRENGTH.get(i['tier'],.5)+(attempt-.5)*.04))
raw=img(image=previous,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=strength,num_inference_steps=STEPS[i['tier']],guidance_scale=0,output_type='pil',generator=gen).images[0];mode=f'img2img-s{strength:.2f}'
⋮----
def main()
⋮----
ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=28);ap.add_argument('--seed',type=int,default=43117);args=ap.parse_args()
items=select(list(rows()),max(1,args.count));print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
⋮----
INCOMING.mkdir(parents=True,exist_ok=True);emb={};t,enc=load_encode()
⋮----
del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=load_render();by={}
⋮----
accepted=[];rejected=0
⋮----
group.sort(key=lambda x:x['tier']);recs=[];previous=None;failed=False
⋮----
print(f"KAGGLE_REJECTED={i['id']} stage=render reason={e}",flush=True);failed=True;rejected+=1;break
⋮----
p=INCOMING/f"{i['stem']}.png";final.save(p,'PNG',optimize=True);accepted.append(i['id']);print(f"KAGGLE_VALIDATED={p.relative_to(ROOT)} coverage={cov:.1%} {why}",flush=True)
```

## File: sprites/kaggle_character_sheet_factory_v1.py
```python
#!/usr/bin/env python3
"""Dedicated FLUX character-sheet factory for Zero -> Empire.

Produces one coherent animation sheet per manifest CHR-* target. The first frame
is text-to-image; later frames are conservative img2img pose variations to keep
identity/clothing/camera stable. Output remains candidate-only until semantic QA.
"""
⋮----
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
REPORT=Path('/kaggle/working/output/character-sheet-report.json')
QUEUE=ROOT/'art/production/controlled-character-regen-queue.json'
REJECTION_LEDGER=ROOT/'art/production/generation-rejection-ledger.json'
⋮----
def production_first_enabled()
⋮----
"""Use relaxed *candidate* admission only for explicitly designated waves."""
forced=os.environ.get('ZTE_ASSET_ACCEPTANCE_MODE','').strip().lower()
⋮----
queue=json.loads(QUEUE.read_text(encoding='utf-8'))
⋮----
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
CHR=re.compile(r'^CHR-(OP|TECH|LOG|ENG)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$')
ROLE={
ACTION={
ACTION_SEMANTIC={
POSE_HINT={
⋮----
def rows()
⋮----
catalog={}
⋮----
m=ROW.match(line)
⋮----
cm=CHR.fullmatch(aid)
⋮----
q=json.loads(QUEUE.read_text(encoding='utf-8'))
controlled=[]
⋮----
aid=str(item.get('id','')).upper()
⋮----
def queue_rejection_hint(i)
⋮----
row=next((x for x in q.get('targets',[]) if str(x.get('id','')).upper()==i['id']),None)
⋮----
reason=str(row.get('review_reason') or '').lower()
⋮----
rules=[]
mapping=(
⋮----
def compact_rejection_hints(memory_hints,queue_hint,max_words=72)
⋮----
# 86+ historical failures accumulate repeated, occasionally contradictory
# advice. When simply taking the last 72 words, the newest *specific* defect
# could be cut off by generic queue mapping. Prioritize the most recent
# reviewed action defect, then targeted queue diagnosis, then older context.
⋮----
newest=memory_hints[-1] if memory_hints else ''
previous=list(reversed(memory_hints[:-1]))
selected=[];seen=set()
⋮----
hint=' '.join(str(hint or '').split())
⋮----
remain=max_words-len(selected)
⋮----
def rejection_hints(i)
⋮----
hints=[]
⋮----
data=json.loads(REJECTION_LEDGER.read_text(encoding='utf-8'))
⋮----
exact=str(row.get('id','')).upper()
prefix=str(row.get('target_prefix','')).upper()
role=str(row.get('role','')).upper()
action=str(row.get('action','')).upper()
⋮----
matched=exact==i['id']
⋮----
matched=i['id'].startswith(prefix)
⋮----
matched=bool(role and role==i['role'] and (not action or action==i['action']))
⋮----
hint=str(row.get('prompt_hint','')).strip()
⋮----
qhint=queue_rejection_hint(i)
⋮----
def anchor_prompt_pair(role)
⋮----
role_short={
core=f"2.5D game sprite, one {role_short}, full body, three-quarter view, neutral relaxed stance, isolated"
detail=(
⋮----
def semantic_scaffold(source,action,frame_index=0)
⋮----
# v1.16 articulated-stride: deform the canonical source itself instead of
# painting foreign leg geometry that Flux can reinterpret as background props.
# Upper body stays pixel-identical; only the lower-body bands are displaced.
out=source.copy()
⋮----
phase=(0,1,2,1,0,-1,-2,-1)[frame_index%8]
hip_y=int(h*.56); knee_y=int(h*.73)
lower=out.crop((0,hip_y,w,h))
# Progressive shear creates alternating foot travel while preserving texture,
# palette and identity from the same canonical character.
shear=phase*.075
lower=lower.transform(lower.size,Image.Transform.AFFINE,(1,shear,-shear*(knee_y-hip_y),0,1,0),resample=Image.Resampling.BICUBIC)
⋮----
# The affine transform introduces dark fill along the lower border. Rebuild
# a uniform neutral margin so border-based segmentation remains reliable.
margin=max(24,int(min(w,h)*.055))
bg=source.convert('RGB').getpixel((0,0))
draw=ImageDraw.Draw(out)
⋮----
# Preserve one anchored upper-body/crate identity while adding deterministic
# lower-body travel. This makes the carrying stride readable without asking
# the diffusion model to redesign the person or luggage each frame.
⋮----
hip_y=int(h*.58); knee_y=int(h*.75)
⋮----
shear=phase*.060
lower=lower.transform(
⋮----
clean=ImageDraw.Draw(out)
⋮----
draw=ImageDraw.Draw(out,'RGBA')
⋮----
# The original giant detached console encouraged floating and morphing
# equipment. Keep a single same-sized wrist-connected handheld tool, while
# articulating the wrist in a ten-frame press/operate/release cycle. Its
# working tip remains near the same fixed target instead of teleporting.
phase=(0,6,12,18,12,0,-6,-12,-18,-6)[frame_index%10]
tip_delta=round(phase*.25)
⋮----
# Keep the compact diagnostic probe consistent but move it through a
# gradual inspect/contact/withdraw cycle connected to the same arm. The
# endpoint stays close to the fixed repair point in every pose.
phase=(0,8,16,23,16,0,-8,-16,-8,0)[frame_index%10]
tip_delta=round(phase*.3)
⋮----
def prompt_pair(i,pose,mode='default')
⋮----
# Keep CLIP deliberately tiny: tokenizer expansion makes word-count estimates
# optimistic. T5 carries the descriptive detail and rejection-memory hints.
role=i['role'];action=i['action']
⋮----
core=(f"2.5D game sprite, one {role_short}, full body, "
⋮----
core_words=core.split()
⋮----
core=' '.join(core_words[:42])
detail=(f"AAA stylized painterly 2.5D mobile game character. {ROLE[role]}. "
⋮----
def retry_mode(reason,attempt)
⋮----
r=(reason or '').lower()
⋮----
def load_encode()
⋮----
t=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda')
p=FluxPipeline.from_pretrained(FLUX,text_encoder_2=t,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda')
⋮----
def load_render()
⋮----
tr=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda')
base=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=tr,torch_dtype=torch.float16,device_map='cuda')
⋮----
img=FluxImg2ImgPipeline.from_pipe(base); img.vae.to(device='cuda',dtype=torch.float16)
⋮----
def border_bg(im)
⋮----
rgb=im.convert('RGB');w,h=rgb.size;step=max(1,min(w,h)//96);pts=[]
⋮----
vals=[sum(p)/3 for p in pts];mean=sum(vals)/len(vals);sd=(sum((v-mean)**2 for v in vals)/len(vals))**.5
q=sorted(pts,key=sum)[len(pts)//3:2*len(pts)//3];bg=tuple(sum(p[k] for p in q)//len(q) for k in range(3))
⋮----
def isolate(im)
⋮----
rgb=im.convert('RGB');w,h=rgb.size;bg=border_bg(rgb);px=rgb.load();seen=set();q=deque()
⋮----
def dist(p):return ((p[0]-bg[0])**2+(p[1]-bg[1])**2+(p[2]-bg[2])**2)**.5
⋮----
p=q.popleft()
⋮----
mask=Image.new('L',(w,h),255);mp=mask.load()
⋮----
mask=mask.filter(ImageFilter.GaussianBlur(.65));out=rgb.convert('RGBA');out.putalpha(mask)
⋮----
def validate_source_full_body(bb,w,h,action)
⋮----
left,top,right,bottom=bb;cw=max(0,right-left);ch=max(0,bottom-top)
⋮----
edge=max(8,round(h*.018))
⋮----
min_ratio=.42 if action=='REPAIR' else .55
⋮----
def finish_frame(raw,action)
⋮----
m=isolate(raw);a=m.getchannel('A');bb=a.getbbox()
⋮----
w,h=m.size;pad=max(8,w//40)
⋮----
crop=m.crop(bb);cw,ch=crop.size
# Two side-by-side people produce an abnormally wide full-body silhouette.
# Allow wide action poses/gear up to 1.08; downstream identity/coverage QA still rejects real duplicates.
# Reject before resizing so technical QA cannot normalize a multi-person frame into a valid-looking cell.
⋮----
scale=min(176/cw,218/ch); crop=crop.resize((max(1,round(cw*scale)),max(1,round(ch*scale))),Image.Resampling.LANCZOS)
cell=Image.new('RGBA',(256,256));x=(256-crop.width)//2;y=238-crop.height;cell.alpha_composite(crop,(x,y))
⋮----
# Reject detached generated props/background fragments. After isolation a valid
# character should form one dominant connected silhouette; small antialiased
# islands are tolerated, but a second substantial component is semantic noise.
aa=cell.getchannel('A')
binary=aa.point(lambda p:255 if p>=32 else 0)
seen=set();components=[]
pix=binary.load()
⋮----
stack=[(sx,sy)];seen.add((sx,sy));n=0
⋮----
cov=sum(aa.histogram()[8:])/(256*256)
⋮----
def validated_single_role_anchor(source)
⋮----
# Validate the source *before* costly multi-frame diffusion. Two conjoined
# workers with touching shoulders previously passed connected-component and
# aspect checks; reject their distinct helmet silhouettes immediately.
⋮----
def alpha_iou(a,b)
⋮----
A=a.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
B=b.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
pa,pb=A.load(),B.load();inter=union=0
⋮----
aa=pa[x,y]>0;bb=pb[x,y]>0;inter+=aa and bb;union+=aa or bb
⋮----
def sheet_qa(frames,action=None)
⋮----
production_first=production_first_enabled()
⋮----
ious=[alpha_iou(frames[n-1],frames[n]) for n in range(1,len(frames))]
⋮----
bottoms=[];centers=[]
⋮----
bb=f.getchannel('A').getbbox()
⋮----
def lower_body_motion(frames)
⋮----
vals=[]
⋮----
A=frames[n-1].getchannel('A')
B=frames[n].getchannel('A')
ba=A.getbbox();bb=B.getbbox()
⋮----
top=max(0,min(ba[1]+int((ba[3]-ba[1])*.55),bb[1]+int((bb[3]-bb[1])*.55)))
a=A.crop((0,top,256,256)).resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
b=B.crop((0,top,256,256)).resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
pa,pb=a.load(),b.load();inter=union=0
⋮----
aa=pa[x,y]>0;bbb=pb[x,y]>0;inter+=aa and bbb;union+=aa or bbb
⋮----
def upper_body_transition_changes(frames)
⋮----
# For CELEB, a large whole-body alpha change can come from a morphing
# prop, outfit or leg rather than an expressive arm gesture. Analyze the
# top 45% of the body's visible silhouette separately for readability.
changes=[]
⋮----
boxes=[f.getchannel('A').getbbox() for f in (previous,current)]
⋮----
limit=min(255,max(int(b[1]+(b[3]-b[1])*.45) for b in boxes))
area=(0,0,256,max(16,limit))
a=previous.crop(area)
b=current.crop(area)
⋮----
def walk_consistency_qa(frames)
⋮----
# Guard against semantic false positives where motion is large only because the
# model flips viewpoint or redesigns the character between cells.
ref=frames[0]
ref_sig=appearance_signature(ref)
distances=[appearance_distance(ref,f) for f in frames[1:]]
⋮----
# Adjacent silhouettes must remain recognisably the same person even while the
# legs alternate. A very low IoU indicates a viewpoint/identity jump.
adj=[alpha_iou(frames[n-1],frames[n]) for n in range(1,len(frames))]
⋮----
def action_qa(frames,action)
⋮----
# Per-action motion floor prevents technically valid but visually frozen atlases
# from reaching manual semantic review.
⋮----
mean_change=(sum(1-x for x in ious)/len(ious)) if ious else 0.0
⋮----
motion=lower_body_motion(frames)
⋮----
# Visible facial blinking or breathing can be excellent idle animation with
# nearly identical alpha silhouettes. Earlier .025 alpha-only floor blocked
# a usable ENG reference (.010) and needlessly skipped its three actions.
activity=idle_visual_activity(frames)
⋮----
floor=motion_floor(action,production_first=production_first) if action in {'WORK','CARRY','REPAIR','CELEB'} else .05
⋮----
carry_floor=motion_floor('CARRY',production_first=production_first,lower_body=True)
⋮----
changes=upper_body_transition_changes(frames)
# Arm movement should progress across multiple frames, not originate from
# one terminal animation jump or from isolated lower-body changes.
expressive=sum(delta>=.15 for delta in changes)
⋮----
arms=celebration_arm_reach_counts(frames)
active=sum(count>=28 for count in arms)
⋮----
def appearance_signature(cell)
⋮----
rgba=cell.convert('RGBA');a=rgba.getchannel('A');bb=a.getbbox()
⋮----
x0,y0,x1,y1=bb;h=max(1,y1-y0)
bands=((y0,y0+int(.38*h)),(y0+int(.38*h),y0+int(.78*h)))
out=[]
⋮----
crop=rgba.crop((x0,ya,x1,max(ya+1,yb)))
ca=crop.getchannel('A');pix=list(crop.convert('RGB').getdata());mask=list(ca.getdata())
vals=[p for p,m in zip(pix,mask) if m>=48]
⋮----
def appearance_distance(a,b)
⋮----
def make_sheet(frames)
⋮----
# Canonical character deliverable: fixed 1024x1024 transparent atlas.
# 256px cells in a 4x4 grid preserve stable runtime slicing; unused cells stay transparent.
⋮----
out=Image.new('RGBA',(1024,1024),(0,0,0,0))
⋮----
def keep_rejected_idle_for_review(item,frames,reason)
⋮----
"""Keep rejected IDLE pixels as evidence, separate from final-sprites."""
⋮----
result=save_rejected_idle_preview(
⋮----
# Failure to record optional diagnostics must never make the entire
# multi-role GPU wave unusable.
⋮----
def main()
⋮----
ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=8);ap.add_argument('--seed',type=int,default=19417);args=ap.parse_args()
items=rows()[:max(1,args.count)];print('KAGGLE_CHARACTER_PLAN='+','.join(i['id'] for i in items),flush=True)
⋮----
encs={};anchor_encs={};t,enc=load_encode()
roles=[]
⋮----
hints=POSE_HINT[i['action']][:ACTION[i['action']][1]]
⋮----
variants={}
⋮----
del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=load_render();report=[];role_anchor={};role_reference_cell={};anchor_failures={};role_anchor_salvage={}
# When the strict-completion batch includes an IDLE identity anchor, every
# sibling action must share the SAME successfully validated anchor. If the
# IDLE atlas is rejected, rendering unrelated actions would burn GPU time
# yet be ineligible for coherent-role strict promotion.
required_idle_roles={item['role'] for item in items if item['action']=='IDLE'}
verified_idle_roles=set()
⋮----
failures=[]
# If a technically passed, exact-run engineer IDLE was already collected,
# use its reviewed *pixels* as the same-role visual identity source instead
# of spending four text-to-image anchors that often yield two workers.
# The overlay is SHA-256/provenance locked and explicitly review-only; it
# still must pass the generator's full single-subject safety checks.
⋮----
coverage=validated_single_role_anchor(provisional)
⋮----
# A single malformed text-to-image role anchor previously poisoned all six
# character actions. Reject multi-subject/cropped source images before any
# action frame is generated, and try independent deterministic seeds.
⋮----
gen_anchor=torch.Generator(device='cuda').manual_seed(args.seed+700000+ri*50000+anchor_attempt*104729)
⋮----
raw=base(height=1024,width=1024,num_inference_steps=6,guidance_scale=0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',generator=gen_anchor).images[0]
candidate=raw.convert('RGB')
⋮----
coverage=validated_single_role_anchor(candidate)
⋮----
reason=str(anchor_error).lower()
⋮----
# FLUX can yield two side-by-side workers even with a "one person"
# prompt. When two independently tall figures have no overlap, retain
# one original foreground without repainting faces or inventing limbs.
# Ambiguous duplicates still fail rather than contaminating all actions.
⋮----
coverage=validated_single_role_anchor(single)
candidate=single
⋮----
# Reuse only a strict-DONE OP/LOG/TECH IDLE as a visual identity SOURCE,
# never as a newly approved role action. Reject invalid/multi-person seed.
⋮----
coverage=validated_single_role_anchor(fallback)
⋮----
def try_role_seed_idle_fallback(item,failed_reason,failed_frames)
⋮----
# In the old pipeline a single failed IDLE frame discarded the five
# sibling actions without even trying them. Reuse the already validated
# single-person anchor to make six conservative breathing poses, then run
# the EXACT same technical and image-risk checks as GPU output. This only
# creates a manual-review candidate; it NEVER marks semantic strict DONE.
⋮----
recovered=build_idle_breathing_frames(seed)
⋮----
risk=clip_risk(recovered,'IDLE')
⋮----
sheet=make_sheet(recovered)
dst=INCOMING/f"{item['stem']}.png"
⋮----
rejected_preview=keep_rejected_idle_for_review(item,failed_frames,failed_reason)
⋮----
why='required-role-idle-candidate-rejected'
⋮----
frames=[];anchor_raw=None;fail=None;retry_reasons=[];head_lock_frames=0
⋮----
ok=False;last_reason=''
⋮----
mode=retry_mode(last_reason,attempt)
⋮----
gen=torch.Generator(device='cuda').manual_seed(args.seed+idx*10000+fi*211+attempt*7919)
⋮----
shared=role_anchor[i['role']]
⋮----
source=semantic_scaffold(shared,i['action'],fi)
⋮----
first_strength={
⋮----
strength=min(first_strength[2],first_strength[0]+attempt*first_strength[1])
⋮----
strength=repair_strength(fi,attempt,mode)
elif mode=='identity' and i['action']!='WALK':strength=max(.26,strength-.035)
⋮----
# The role anchor already passed full-body validation. On an
# edge-contact retry, favor preserving its intact shape rather than
# introducing a larger pose displacement with stronger diffusion.
strength=min(strength,.23)
⋮----
raw=img(image=source,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=strength,num_inference_steps=6,guidance_scale=0,output_type='pil',generator=gen).images[0]
⋮----
anchor_raw=raw.convert('RGB')
⋮----
strength=min(.46,.34+fi*.008+attempt*.018)
⋮----
strength=min(.72,.54+fi*.018+attempt*.025)
⋮----
# v1.18: keep the role identity and clothing materially closer to the
# canonical anchor. The deterministic crate scaffold already supplies
# the carry semantic, so high denoise only encourages face/body drift
# and oversized/duplicated luggage.
strength=min(.54,.41+fi*.012+attempt*.018)
⋮----
strength=min(.76,.56+fi*.018+attempt*.03)
⋮----
strength=min(.38,.24+fi*.012+attempt*.02)
⋮----
strength=max(.24,strength-.035)
⋮----
strength=min(strength,.21)
source=semantic_scaffold(anchor_raw,i['action'],fi)
⋮----
# Freeze only correctly registered faces/headgear against the validated
# same-wave IDLE reference. Raised-arm/crouching poses are bypassed.
# This is candidate visual stabilization, never semantic approval.
⋮----
frames.append(frame);ok=True;print(f"KAGGLE_CHR_FRAME={i['id']} frame={fi} attempt={attempt+1} mode={mode} cov={cov:.2f}",flush=True);break
⋮----
last_reason=str(e);retry_reasons.append(last_reason);print(f"KAGGLE_CHR_RETRY={i['id']} frame={fi} attempt={attempt+1} mode={mode} reason={e}",flush=True)
if not ok:fail=f'frame-{fi}-failed';break
⋮----
preview=keep_rejected_idle_for_review(i,frames,fail)
⋮----
preview=keep_rejected_idle_for_review(i,frames,why)
⋮----
preview=keep_rejected_idle_for_review(i,frames,action_why)
⋮----
visual_risk=clip_risk(frames,i['action'])
⋮----
# One bizarre empty head/hand crop must not abort a 12-sheet GPU kernel,
# dropping valid siblings and their producer report. Explicitly reject
# this candidate and preserve exact diagnostics for the next attempt.
reason=f'candidate-visual-qa-error:{type(exc).__name__}:{str(exc)[:180]}'
⋮----
preview=keep_rejected_idle_for_review(i,frames,reason)
⋮----
risk_reason='image-risk:'+','.join(blocking_visual_flags)
⋮----
preview=keep_rejected_idle_for_review(i,frames,risk_reason)
⋮----
why=why+' '+action_why
identity_distance=0.0
ref=role_reference_cell.get(i['role'])
⋮----
identity_distance=appearance_distance(ref,frames[0])
⋮----
why=f'cross-animation-appearance-drift={identity_distance:.1f}'
⋮----
sheet=make_sheet(frames)
⋮----
p=INCOMING/f"{i['stem']}.png";sheet.save(p,'PNG',optimize=True)
```

## File: sprites/kaggle_fx_sheet_factory_v1.py
```python
#!/usr/bin/env python3
"""Validated procedural FX-sheet factory for Zero -> Empire.
Candidate-only: outputs must still pass semantic/runtime/CI gates before strict DONE.
"""
⋮----
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'; OUT=Path('/kaggle/working/output')
ROW=re.compile(r'^\|\s*(FX-\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$')
FRAMES=8
RENDER_CELL=256
RUNTIME_CELL=128
RUNTIME_COLS=4
RUNTIME_ROWS=2
ONE_SHOT={'FX-00','FX-05','FX-06','FX-07'}
LOOP={'FX-01','FX-02','FX-03','FX-04'}
⋮----
def rows()
⋮----
m=ROW.match(line)
⋮----
def rgba(): return Image.new('RGBA',(RENDER_CELL,RENDER_CELL),(0,0,0,0))
def glow(layer,r): return layer.filter(ImageFilter.GaussianBlur(r))
def add(dst,src): return Image.alpha_composite(dst,src)
⋮----
def particle_frame(kind,t,rng,item_id='')
⋮----
im=rgba();d=ImageDraw.Draw(im);cx=cy=RENDER_CELL//2
env=max(0.0,math.sin(math.pi*min(1.0,max(0.0,t))))
⋮----
count=max(4,round(26*env))
⋮----
a=rng.uniform(-2.8,-.35); L=rng.uniform(18,70)*(0.45+0.55*env); x=cx+rng.uniform(-8,8); y=cy+rng.uniform(-4,8); x2=x+math.cos(a)*L; y2=y+math.sin(a)*L
⋮----
phase=(j/7+t)%1; w=22+10*math.sin(phase*math.pi); h=72+34*math.sin(phase*math.pi); x=cx+rng.uniform(-18,18); y=cy+38-h*.55
⋮----
dust_alpha=round(150*env)
⋮----
phase=min(1.0,j/14+t*.72); r=7+27*phase; x=cx+rng.uniform(-48,48)*(0.3+phase); y=cy+48-50*phase+rng.uniform(-8,8)
⋮----
direction=rng.uniform(math.pi*.12,math.pi*.88); speed=rng.uniform(30,82); flight=t
x=cx+math.cos(direction)*speed*flight+rng.uniform(-8,8)
y=cy+38-math.sin(direction)*speed*flight+58*(flight**2)
rr=rng.randint(3,7); col=rng.choice(((116,105,88,round(230*env)),(145,126,96,round(220*env)),(91,91,88,round(220*env))))
pts=[(x-rr,y),(x-rr*.25,y-rr),(x+rr,y-rr*.25),(x+rr*.55,y+rr),(x-rr*.5,y+rr*.65)]
⋮----
phase=(j/9+t)%1; r=10+34*phase; x=cx+rng.uniform(-35,35)*(0.4+phase); y=cy+55-95*phase+rng.uniform(-10,10)
col=(210,225,235,110) if 'steam' in kind else (120,125,130,100)
⋮----
rr=24+72*env; col=(70,225,255,round(220*env)) if 'cyan' in kind else (255,185,70,round(220*env))
⋮----
pts=[(cx-78,cy+rng.uniform(-16,16))]
⋮----
y=38+180*t; d.rectangle((34,y-4,222,y+4),fill=(80,235,255,190)); d.rectangle((54,42,202,214),outline=(80,235,255,75),width=2)
⋮----
L=80+40*math.sin(math.pi*t); d.polygon([(cx-18,cy-35),(cx+18,cy-35),(cx+8,cy+L),(cx-8,cy+L)],fill=(80,210,255,165)); d.ellipse((cx-22,cy-42,cx+22,cy-15),fill=(210,250,255,230))
⋮----
rr=24+65*t; d.ellipse((cx-rr,cy-rr,cx+rr,cy+rr),outline=(255,220,120,180),width=6)
⋮----
def metrics(im)
⋮----
a=im.getchannel('A'); box=a.getbbox()
⋮----
x0,y0,x1,y1=box; data=list(a.getdata());cov=sum(1 for v in data if v>12)/(RENDER_CELL*RENDER_CELL); mass=sum(data)
edge=(x0<8 or y0<8 or x1>RENDER_CELL-8 or y1>RENDER_CELL-8)
⋮----
def temporal_qa(item,report)
⋮----
masses=[m['alpha_mass'] for m in report]; peak=max(range(len(masses)),key=masses.__getitem__)
⋮----
def sheet_for(item,seed)
⋮----
frames=[]; report=[]
⋮----
rng=random.Random(seed+i*7919+int(item['id'].split('-')[1])*100003); f=particle_frame(item['name'].lower(),i/(FRAMES-1),rng,item['id']); m=metrics(f)
⋮----
sig=[]; centers=[]
⋮----
a=f.getchannel('A').resize((32,32)); sig.append(bytes(a.getdata())); b=m['bbox']; centers.append(((b[0]+b[2])/2,(b[1]+b[3])/2))
dup=sum(sig[i]==sig[i-1] for i in range(1,len(sig)))
drift=max(math.hypot(x-RENDER_CELL/2,y-RENDER_CELL/2) for x,y in centers)
⋮----
temporal=temporal_qa(item,report)
sheet=Image.new('RGBA',(RUNTIME_COLS*RUNTIME_CELL,RUNTIME_ROWS*RUNTIME_CELL),(0,0,0,0))
⋮----
runtime=f.resize((RUNTIME_CELL,RUNTIME_CELL),Image.Resampling.LANCZOS)
⋮----
def main()
⋮----
ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=18);ap.add_argument('--seed',type=int,default=90210);args=ap.parse_args()
⋮----
rep={'engine':'procedural-fx-v1.2-runtime-atlas','attempted':0,'accepted':0,'rejected':0,'runtime_contract':'8 frames; 4x2 atlas; 128x128 runtime cell; 512x256 texture; matches existing ElectricArc/DroneThruster loaders','items':[]}
⋮----
rep['attempted']+=1; accepted=None; errors=[]
⋮----
sheet,m=sheet_for(item,args.seed+attempt*104729); accepted=(sheet,m,attempt); print(f'KAGGLE_FX_LIVE_PASS={item["id"]} attempt={attempt+1} mode={m["mode"]}',flush=True);break
⋮----
sheet,m,attempt=accepted; p=INCOMING/f"{item['stem']}.png"; sheet.save(p,'PNG',optimize=True); rep['accepted']+=1;rep['items'].append({'id':item['id'],'accepted':True,'attempt':attempt+1,**m}); print(f'KAGGLE_VALIDATED={p.relative_to(ROOT)} atlas=512x256 layout=4x2',flush=True)
```

## File: sprites/kaggle_sprite_factory.py
```python
#!/usr/bin/env python3
"""High-throughput static Zero -> Empire FLUX candidate factory.

The factory deliberately handles only manifest assets that can be reviewed as one
isolated static master. Character and FX sheets stay on their dedicated animation
pipelines; building tiers require a separate family-coherent generator.
"""
⋮----
ROOT=Path(__file__).resolve().parents[2];MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md';INCOMING=ROOT/'art/incoming/final-sprites'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
SUPPORTED=('MCH-','TER-','PRP-','VEH-','CORE-');PRIORITY={'MCH':0,'TER':1,'PRP':2,'VEH':3,'CORE':4};TARGET_SIDE={'MCH':1024,'TER':1024,'CORE':1536,'VEH':1536,'PRP':1024};FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
MACHINE_PRIMARY=[
MACHINE_SECONDARY=[
TERRAIN_SUBJECTS={
def manifest_rows()
⋮----
order=0
⋮----
m=ROW.match(line)
⋮----
def concrete_subject(i)
⋮----
m=re.fullmatch(r'MCH-(\d{2})-([01])',i['id']);idx=int(m.group(1));variant=int(m.group(2));return (MACHINE_PRIMARY if variant==0 else MACHINE_SECONDARY)[idx]
⋮----
m=re.fullmatch(r'PRP-(\d{2})-([AB])',i['id']);idx=int(m.group(1));v=m.group(2)
a=['rugged closed supply crate','compact closed retail stock crate','heatproof closed tool chest','closed assembly parts bin','closed industrial logistics crate','sealed component case','reinforced tool locker','closed automation parts crate','high-tech cargo case','energy-cell storage box','precision maintenance chest','orbital supply container','phase-tech component crate','prestige equipment case'];b=['90-degree utility pipe elbow fitting','compact safety barrier','90-degree insulated service pipe elbow fitting','small control terminal','utility bollard','cable junction pedestal','compact pipe manifold','service terminal','90-degree coolant pipe elbow fitting','power distribution post','sensor bollard','orbital service terminal','90-degree phase conduit elbow fitting','prestige light bollard'];return (a if v=='A' else b)[min(idx,13)]
⋮----
exact={'VEH-09':'ONE futuristic enclosed MAGLEV FREIGHT CAPSULE, ZERO wheels, continuous smooth magnetic levitation hull, four flush glowing rectangular magnetic lift emitters, large visible air gap beneath the entire hull, long cargo-container proportions, no road styling, rail, track or platform','VEH-16':'one compact two-passenger prestige anti-gravity coupe, low sleek teardrop capsule, panoramic dark glass canopy, completely blank unbranded featureless nose with no ornament at all, one continuous smooth rounded belly, thin cyan levitation light seam painted flush into the lower hull, large open empty air gap beneath the complete hull, pearl white and glossy black premium finish, zero wheels, wheel arches, legs, feet, struts, landing gear, skids, rails, blades, bars or pods','VEH-17':'a tight coordinated swarm of five distinct small singularity logistics drones in one compact formation, all five drones fully visible, no mothership'};return exact.get(i['id'],i['name'])
⋮----
def prompt_for(i)
⋮----
s=concrete_subject(i)
⋮----
noun={'PRP':'prop','VEH':'vehicle composition','CORE':'reactor'}[i['kind']];return f"Create exactly {s}. One centered {noun}, fully visible, isolated on pure black. No environment, floor, road, pedestal, text, logo, labels or UI. Premium stylized 2.5D mobile strategy asset, 34 degree three-quarter camera, upper-left key, cool fill, restrained cyan/amber accents. Manifest intent: {i['description']}. Generous empty black edge space."
def load_encode()
⋮----
print('KAGGLE_FLUX_LOAD=encoder',flush=True);text2=T5EncoderModel.from_pretrained(FLUX,subfolder='text_encoder_2',torch_dtype=torch.float16,device_map='cuda');pipe=FluxPipeline.from_pretrained(FLUX,text_encoder_2=text2,transformer=None,vae=None,torch_dtype=torch.float16,device_map='cuda');return text2,pipe
def load_diffuse()
⋮----
print('KAGGLE_FLUX_LOAD=transformer',flush=True);tr=FluxTransformer2DModel.from_pretrained(FLUX,subfolder='transformer',torch_dtype=torch.float16,device_map='cuda');pipe=FluxPipeline.from_pretrained(FLUX,text_encoder=None,text_encoder_2=None,tokenizer=None,tokenizer_2=None,transformer=tr,vae=None,torch_dtype=torch.float16,device_map='cuda');return tr,pipe
def load_decode()
def border_background(im)
⋮----
rgb=im.convert('RGB');w,h=rgb.size;s=max(1,min(w,h)//128);pts=[]
⋮----
pts.sort(key=sum);q=pts[:max(16,len(pts)//3)];return tuple(sum(p[i] for p in q)//len(q) for i in range(3))
def isolate(im)
⋮----
rgb=im.convert('RGB');w,h=rgb.size;bg=border_background(rgb);px=rgb.load();dist=Image.new('L',(w,h));dp=dist.load()
⋮----
mask=dist.point(lambda p:0 if p<20 else 255 if p>58 else int((p-20)*255/38));mp=mask.load();seen=set();q=deque()
⋮----
mask=mask.filter(ImageFilter.GaussianBlur(.6));rgba=rgb.convert('RGBA');rgba.putalpha(mask);return rgba
def components(alpha,threshold=32)
⋮----
small=alpha.resize((128,128),Image.Resampling.BILINEAR);px=small.load();seen=set();comps=[]
⋮----
q=deque([(x,y)]);seen.add((x,y));pts=[]
⋮----
def finish(image,item)
⋮----
master=isolate(image);comps=components(master.getchannel('A'))
⋮----
total=sum(map(len,comps));allow=item['id']=='VEH-17';dominant=len(comps[0])/total;important=sum(len(c)/total>=.08 for c in comps)
⋮----
selected=comps if allow else comps[:1];xs=[x for c in selected for x,y in c];ys=[y for c in selected for x,y in c];w,h=master.size
crop=master.crop((max(0,int(min(xs)*w/128)-25),max(0,int(min(ys)*h/128)-25),min(w,int((max(xs)+1)*w/128)+25),min(h,int((max(ys)+1)*h/128)+25)));bbox=crop.getbbox()
⋮----
crop=crop.crop(bbox);side=TARGET_SIDE[item['kind']];subject_fraction=.76 if item['kind']=='TER' else .68;scale=min(side*subject_fraction/crop.width,side*subject_fraction/crop.height);crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS);out=Image.new('RGBA',(side,side));bottom=.12 if item['kind']!='TER' else .10;out.alpha_composite(crop,((side-crop.width)//2,side-int(side*bottom)-crop.height));a=out.getchannel('A');lo,hi=a.getextrema();visible=sum(a.histogram()[8:])/(side*side)
maxcov=.58 if item['kind'] in ('MCH','TER','PRP') else .70
⋮----
pad=int(side*.06)
⋮----
def main()
⋮----
ap=argparse.ArgumentParser();ap.add_argument('--kind',choices=['ALL','MCH','TER','PRP','VEH','CORE'],default='ALL');ap.add_argument('--count',type=int,default=30);ap.add_argument('--seed',type=int,default=12217);args=ap.parse_args();items=[x for x in manifest_rows() if args.kind=='ALL' or x['kind']==args.kind];items.sort(key=lambda x:(PRIORITY[x['kind']],x['order']));items=items[:max(1,args.count)];print(f'KAGGLE_PLAN={len(items)} targets={",".join(x["id"] for x in items)} engine=FLUX.1-schnell-NF4-batched-v2',flush=True)
⋮----
INCOMING.mkdir(parents=True,exist_ok=True);encoded=[];text2,enc=load_encode()
⋮----
del text2,enc;gc.collect();torch.cuda.empty_cache();tr,diff=load_diffuse();latents=[]
⋮----
pe=pe.cuda();ppe=ppe.cuda();packed=diff(height=1024,width=1024,num_inference_steps=4,guidance_scale=0.0,prompt_embeds=pe,pooled_prompt_embeds=ppe,output_type='latent',max_sequence_length=384,generator=torch.Generator(device='cuda').manual_seed(args.seed+index)).images;latents.append((item,packed.cpu()));print(f"KAGGLE_DIFFUSED={item['id']}",flush=True)
⋮----
del tr,diff,encoded;gc.collect();torch.cuda.empty_cache();dec=load_decode();ok=rej=0
⋮----
packed=packed.cuda();lat=dec._unpack_latents(packed,height=1024,width=1024,vae_scale_factor=dec.vae_scale_factor)/dec.vae.config.scaling_factor+dec.vae.config.shift_factor
with torch.no_grad():tensor=dec.vae.decode(lat,return_dict=False)[0]
image=dec.image_processor.postprocess(tensor)[0];final,cov=finish(image,item);out=INCOMING/f"{item['stem']}.png";final.save(out,'PNG',optimize=True);ok+=1;print(f'KAGGLE_VALIDATED={out.relative_to(ROOT)} coverage={cov:.1%}',flush=True)
```

## File: sprites/lightning_autopilot_loop.sh
```bash
#!/usr/bin/env bash
set -u

REPO="$HOME/zero-to-empire"
LOG="$HOME/zte-lightning-autopilot.log"
LOCK="$HOME/.zte-lightning-autopilot.lock"
INTERVAL="${LIGHTNING_SPRITE_INTERVAL_SECONDS:-300}"

mkdir -p "$REPO"
exec 9>"$LOCK"
if ! flock -n 9; then
  echo "$(date -Is) AUTOPILOT_ALREADY_RUNNING" >> "$LOG"
  exit 0
fi

echo "$(date -Is) AUTOPILOT_STARTED interval=${INTERVAL}s" >> "$LOG"

while true; do
  {
    echo "$(date -Is) WAVE_START"
    cd "$REPO"
    git fetch origin main
    git reset --hard origin/main
    export SPRITE_COUNT="${SPRITE_COUNT:-56}"
    export SPRITE_SEED="$(date +%s)"
    python -u tools/sprites/lightning_studio_factory.py
    rc=$?
    echo "$(date -Is) WAVE_END rc=$rc"
  } >> "$LOG" 2>&1
  sleep "$INTERVAL"
done
```

## File: sprites/lightning_install_autopilot.sh
```bash
#!/usr/bin/env bash
set -euo pipefail

REPO="$HOME/zero-to-empire"
START_DIR="$HOME/.lightning_studio"
START_FILE="$START_DIR/on_start.sh"
LOG="$HOME/zte-lightning-autopilot.log"

if [ -d "$REPO/.git" ]; then
  git -C "$REPO" fetch origin main
  git -C "$REPO" reset --hard origin/main
else
  rm -rf "$REPO"
  git clone --depth 1 https://github.com/dbrckk/zero-to-empire.git "$REPO"
fi

mkdir -p "$START_DIR"
cat > "$START_FILE" <<'EOF'
#!/usr/bin/env bash
set -u
REPO="$HOME/zero-to-empire"
if [ -d "$REPO/.git" ]; then
  git -C "$REPO" fetch origin main >/dev/null 2>&1 || true
  git -C "$REPO" reset --hard origin/main >/dev/null 2>&1 || true
else
  git clone --depth 1 https://github.com/dbrckk/zero-to-empire.git "$REPO" >/dev/null 2>&1 || true
fi
if [ -f "$REPO/tools/sprites/lightning_autopilot_loop.sh" ]; then
  nohup bash "$REPO/tools/sprites/lightning_autopilot_loop.sh" >/dev/null 2>&1 &
fi
EOF
chmod +x "$START_FILE"

python - <<'PY'
from lightning_sdk import Studio
s = Studio()
s.auto_sleep = False
try:
    urls = s.add_ports(8765)
    if urls:
        try:
            print('LIGHTNING_OUTPUT_URL=' + urls[0].urls[0])
        except Exception:
            print('LIGHTNING_PORT_8765_EXPOSED=1')
except Exception as exc:
    print('LIGHTNING_PORT_WARNING=' + str(exc))
PY

pkill -f 'http.server 8765' >/dev/null 2>&1 || true
mkdir -p "$REPO/.lightning-output"
nohup python -m http.server 8765 --directory "$REPO/.lightning-output" >> "$LOG" 2>&1 &

nohup bash "$REPO/tools/sprites/lightning_autopilot_loop.sh" >/dev/null 2>&1 &

echo "AUTOPILOT_INSTALLED=1"
echo "AUTOPILOT_LOG=$LOG"

python - <<'PY'
from lightning_sdk import Machine, Studio
s = Studio()
print('CURRENT_MACHINE=' + str(s.machine))
if 'CPU' in str(s.machine).upper():
    candidates = []
    for name in ('T4','L4','L40S'):
        m = getattr(Machine, name, None)
        if m is not None:
            candidates.append((name, m))
    last = None
    for name, machine in candidates:
        try:
            print('TRY_SWITCH_MACHINE=' + name, flush=True)
            s.switch_machine(machine)
            print('SWITCHED_MACHINE=' + name, flush=True)
            break
        except Exception as exc:
            last = exc
            print('SWITCH_FAILED_' + name + '=' + str(exc), flush=True)
    else:
        if last is not None:
            print('GPU_SWITCH_REQUIRED_MANUALLY=1')
PY
```

## File: sprites/lightning_remote_runner.py
```python
#!/usr/bin/env python3
"""Control a Lightning AI Studio from CI and retrieve strict QA-only outputs."""
⋮----
STUDIO_NAME = os.getenv("LIGHTNING_STUDIO_NAME", "zero-to-empire-sprites")
REMOTE_REPO = "zero-to-empire"
LOCAL_OUT = Path("lightning-output")
⋮----
def resolve_scope() -> tuple[str, str]
⋮----
username = os.getenv("LIGHTNING_USERNAME")
teamspace = os.getenv("LIGHTNING_TEAMSPACE")
⋮----
user = User()
username = username or user.name
spaces = list(user.teamspaces)
⋮----
teamspace = teamspace or spaces[0].name
⋮----
def main() -> None
⋮----
studio = Studio(
⋮----
prep = r'''set -euo pipefail
```

## File: sprites/lightning_studio_factory.py
```python
#!/usr/bin/env python3
"""Run one strict candidate-generation wave inside a Lightning AI Studio.

This script never promotes assets into the canonical manifest. It only exports
fresh generated candidates plus technical QA evidence for later semantic review.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".lightning-output"
INCOMING = ROOT / "art/incoming/final-sprites"
COUNT = int(os.getenv("SPRITE_COUNT", "56"))
SEED = int(os.getenv("SPRITE_SEED", str(int(time.time()) % 2_000_000_000)))
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
⋮----
def digest(path: Path) -> str
⋮----
h = hashlib.sha256()
⋮----
def require_gpu() -> None
⋮----
out = subprocess.check_output(
⋮----
def ensure_deps() -> None
⋮----
required = ["diffusers", "transformers", "accelerate", "safetensors", "torch", "PIL"]
missing = []
⋮----
def backlog() -> dict[str, int]
⋮----
counts = {"BLD": 0, "STATIC": 0, "CHR": 0, "FX": 0, "SKIPPED_RUNTIME": 0}
manifest = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
⋮----
m = ROW.match(line)
⋮----
asset_id = m.group(1).strip()
runtime = m.group(4).strip()
⋮----
def choose_command(q: dict[str, int]) -> tuple[str, int, list[str]]
⋮----
n = max(7, min(COUNT, 56))
⋮----
n = max(14, min(COUNT, 56))
⋮----
n = max(4, min(COUNT, 8))
⋮----
n = max(1, min(COUNT, 18))
⋮----
def main() -> None
⋮----
before = {p.name: digest(p) for p in INCOMING.glob("*_final.png") if p.is_file()}
q = backlog()
⋮----
fresh = [
⋮----
qa = OUT / "batch-contact-sheet.png"
report = OUT / "batch-qa-report.json"
⋮----
cdir = OUT / "candidates"
⋮----
targets = []
⋮----
dst = cdir / src.name
```

## File: sprites/local_character_action_fx.py
```python
"""Hand-authored action lighting and physically attached VFX for original sprites.

Pure SVG geometry: no text, logos, detached effects or external image models.
Every glow is attached to an invariant tool tip, wrist or cargo fastener.
Review-only visuals; never marks an asset strict DONE.
"""
⋮----
ROLE_LIGHT={
⋮----
# Endpoints are defined in wrist-local sprite coordinates, matching the
# ACTUAL authored props in render_chatgpt_originals.py. Both SVG geometry
# and lighting use one rigid rotation; there are no free-floating effects.
TOOL_TIP_OFFSETS={
⋮----
def tool_angle(action:str,phase:float,*,role:str|None=None)->float
⋮----
# Engineer's long mechanical ratchet needs an unmistakable torque arc
# at the 42px Android gameplay scale; preserve other roles' timings.
⋮----
# A continuous forward/back ratchet cycle with ten meaningful
# intermediate turns. A sine parked the wrist near two extrema and
# produced consecutive near-identical frames on the 42px display.
cycle=(phase/(2.0*math.pi)) % 1.0
⋮----
# Deliberate pitch while the right hand sweeps the diagnostic tablet;
# visible against either stage background at mobile 42px scale.
⋮----
sweep = 18.0 if action=='REPAIR' else 3.0
⋮----
def tool_tip(role:str,action:str,phase:float,*,tool_x:float,tool_y:float)->tuple[float,float]
⋮----
angle=math.radians(tool_angle(action,phase,role=role))
⋮----
"""Return an SVG group for a 256px sprite; empty for unsupported actions.

    WORK/REPAIR emissions are integrated with the tool's existing shaft;
    CELEB lights are on suit cuffs, never confetti; CARRY lights are rivets.
    The sinusoidal envelope closes exactly at the loop boundary.
    """
⋮----
envelope=.5+.5*math.cos(phase)
glow=f'<defs><radialGradient id="fx-{role.lower()}"><stop offset="0" stop-color="{highlight}" stop-opacity=".86"/><stop offset=".45" stop-color="{accent}" stop-opacity=".46"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs>'
⋮----
x=max(12.0,min(233.0,x))
y=max(12.0,min(233.0,y))
pulse=round(.61+.39*envelope,3)
radius=round(8+2.2*envelope,2)
core=(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{radius}" fill="url(#fx-{role.lower()})"/>'
⋮----
y=129+bounce
⋮----
lift=(1-math.cos(phase))/2
y=140-109*lift+bounce
lx=75-4*lift
rx=174+5*lift
```

## File: sprites/local_character_contact_gait.py
```python
"""Locally authored 2.5D contact-aware locomotion rig for OP / LOG / ENG.

No remote art generation. This is an editable candidate pose source and does
not approve sprites or replace Android resources.
"""
⋮----
STANCE_FRACTION = .60
FLOOR_ANKLE_Y = 226.0
UPPER_LEG = 37.5
LOWER_LEG = 38.5
⋮----
@dataclass(frozen=True)
class FootPose
⋮----
hip_x: float
hip_y: float
knee_x: float
knee_y: float
ankle_x: float
ankle_y: float
boot_angle: float
planted: bool
cycle: float
⋮----
def _ease(t: float) -> float
⋮----
t = max(0.0, min(1.0, t))
⋮----
def foot_pose(phase: float, side: str, action: str, bounce: float = 0.0, *, profile: str = "standard") -> FootPose
⋮----
"""Cyclic stance/swing path with locked stance Y and projected knee IK.

    Frame coordinates: 256x256, +Y downward. During the support fraction,
    the sole stays on a constant ground-height line; during recovery it lifts
    smoothly and advances. Feet alternate exactly half a stride apart. Knee
    lateral excursion is attenuated for a 3/4 projection, avoiding the bowed
    2D hinge produced by naïve screen-space IK.
    """
⋮----
# OP-specific stance/swing profile. A small phase offset prevents eight
# source frames from hiding heel lift behind a pair of flat planted boots.
# Standard WALK and all CARRY geometry remain byte-for-byte equivalent.
operator = profile == "op-walk"
engineer = profile == "eng-walk"
specialized = operator or engineer
stance_fraction = .58 if specialized else STANCE_FRACTION
phase_offset = .10 if operator else (.075 if engineer else 0.0)
cycle = (phase/(2*math.pi)+(0 if side == "L" else .5)+phase_offset) % 1.0
reach = 19.0 if operator else (20.0 if engineer else (14.0 if action == "WALK" else 12.0))
clearance = 21.0 if operator else (22.0 if engineer else (16.0 if action == "WALK" else 12.0))
⋮----
progress = _ease(cycle/stance_fraction)
# OP's planted ankle travels at a uniform ground-relative speed
# during support; keep the original eased gait for all other profiles.
foot_dx = (reach*(1.0-2.0*cycle/stance_fraction)
lift = 0.0
angle = 0.0 if specialized else -4.0 + 8.0*progress
planted = True
⋮----
progress = (cycle-stance_fraction)/(1.0-stance_fraction)
foot_dx = reach*(-1.0+2.0*_ease(progress))
lift = clearance*math.sin(math.pi*progress)**1.4
angle = 4.0-8.0*_ease(progress)
planted = False
⋮----
hip_x = (103.0 if side == "L" else 150.0) if specialized else (106.0 if side == "L" else 146.0)
hip_y = 155.0+bounce
ankle_x = hip_x+foot_dx
ankle_y = FLOOR_ANKLE_Y-lift
⋮----
length = math.hypot(dx,dy)
⋮----
along = (UPPER_LEG**2-LOWER_LEG**2+length**2)/(2.0*length)
perpendicular = math.sqrt(max(0.0,UPPER_LEG**2-along**2))
# In the airborne recovery the knee bends predominantly forward
# (into depth), not sideways. A fully planar hinge previously pushed the
# knee pads 20px outside the shin and looked like an exaggerated bow-leg.
# This blend is periodic and smoothly returns to outward stance contour
# at toe-off and heel-strike.
contour = 1.0 if side == "L" else -1.0
perspective_bend = .48 if planted else .48-.75*math.sin(math.pi*progress)
knee_x = hip_x+dx*along/length+contour*(-dy/length)*perpendicular*perspective_bend
knee_y = hip_y+dy*along/length+contour*(dx/length)*perpendicular*perspective_bend
⋮----
def torso_weight_shift(phase: float, action: str) -> float
⋮----
"""Counter-sway toward the grounded stance foot, scaled for cargo."""
```

## File: sprites/local_character_material_finish.py
```python
"""Deterministic alpha-safe material lighting for ChatGPT original sprite rig.

All work is local, editable and repeatable. The operation does not change
pixel alpha, silhouette, timing, frame pivots or candidate review status.
"""
⋮----
CELL=256
⋮----
@lru_cache(maxsize=1)
def _lighting_fields()
⋮----
warm=Image.new("RGB",(CELL,CELL))
cool=Image.new("RGB",(CELL,CELL))
top=Image.new("L",(CELL,CELL))
wp=[];cp=[];tp=[]
⋮----
lx=(CELL-1-x)/(CELL-1)
ly=(CELL-1-y)/(CELL-1)
w=max(0.0,1.0-((x-63)**2/(210**2)+(y-31)**2/(276**2)))
c=max(0.0,(x-124)/150)*.7
⋮----
def finish_frame(frame:Image.Image)->Image.Image
⋮----
"""Apply restrained warm key, cool bounce and alpha-edge rim to RGBA frame."""
⋮----
src=frame.convert("RGBA")
alpha=src.getchannel("A")
⋮----
rgb=src.convert("RGB")
light=ImageChops.multiply(rgb,Image.merge("RGB",(top,top,top)))
light=ImageChops.add(light,warm,scale=1.0,offset=0)
light=ImageChops.add(light,cool,scale=1.0,offset=0)
displaced=ImageChops.offset(alpha,2,1)
rim=ImageChops.subtract(alpha,displaced).filter(ImageFilter.GaussianBlur(.75))
rim=rim.point(lambda px:min(255,round(px*.23)))
rim_color=Image.new("RGB",(CELL,CELL),(246,210,169))
light=Image.composite(rim_color,light,rim)
out=light.convert("RGBA")
```

## File: sprites/manifest_batch_planner.py
```python
#!/usr/bin/env python3
"""Build candidate-only static GPU batches from the canonical sprite manifest.

Animation-heavy character/machine sheets and terrain stay outside this generic static lane.
The canonical manifest status is authoritative: a TODO row remains eligible even when stale
candidate/runtime files exist from an older pre-semantic-finalization workflow.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
SUPPORTED = ("BLD-", "CORE-", "VEH-", "PRP-")
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
FAST_PRIORITY = {"PRP": 0, "VEH": 1, "CORE": 2, "BLD": 3}
MAX_BATCH = 36
⋮----
def rows()
⋮----
order = 0
⋮----
m = ROW.match(line)
⋮----
kind = asset_id.split("-", 1)[0]
⋮----
def main() -> int
⋮----
p = argparse.ArgumentParser()
⋮----
args = p.parse_args()
⋮----
items = [
⋮----
items = items[: args.count]
```

## File: sprites/multi_provider_static_manifest_factory.py
```python
#!/usr/bin/env python3
"""Generate one static manifest sprite with provider failover.

Order:
1. Hugging Face ZeroGPU when available.
2. Cloudflare Workers AI FLUX.1 Schnell when HF quota/network is unavailable.

The existing isolation, normalization and technical QA contract stays authoritative.
"""
⋮----
CF_ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "").strip()
CF_API_TOKEN = os.environ.get("CLOUDFLARE_API_TOKEN", "").strip()
CF_MODEL = os.environ.get("CLOUDFLARE_IMAGE_MODEL", "@cf/black-forest-labs/flux-1-schnell").strip()
⋮----
def cloudflare_generate(prompt: str) -> Image.Image
⋮----
model_path = CF_MODEL.replace("@cf/", "@cf/")
url = f"https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT_ID}/ai/run/{model_path}"
payload = json.dumps({"prompt": prompt[:2048], "steps": 8}).encode("utf-8")
req = urllib.request.Request(
⋮----
body = json.loads(response.read().decode("utf-8"))
⋮----
detail = exc.read().decode("utf-8", "replace")
# Cloudflare returns HTTP 429 / Workers AI code 4006 when the daily free
# neuron allocation is exhausted. This is a provider-availability state,
# not an asset rejection. Preserve the same rc=75 contract used by HF so
# the shard stops immediately instead of spending requests on every target.
low = detail.lower()
⋮----
image_b64 = (body.get("result") or {}).get("image")
⋮----
def generate_with_failover(prompt: str) -> Image.Image
⋮----
hf_error = None
⋮----
hf_error = "HF quota exhausted"
except Exception as exc:  # provider/network failure -> secondary provider
hf_error = str(exc)
⋮----
def main() -> None
⋮----
asset_id = factory.ASSET_ID
⋮----
kind = rid.split("-", 1)[0]
raw = generate_with_failover(factory.prompt_for(rid, name, desc))
final = factory.normalize(factory.isolate(raw), factory.TARGET_SIDE[kind])
⋮----
out = factory.INCOMING / (Path(runtime).stem + ".png")
```

## File: sprites/package_chatgpt_originals.py
```python
#!/usr/bin/env python3
"""Package first-party editable role sprites for *read-only* Android review.

Only the 18 already-committed original candidate atlases are consumed. No new
images or external model calls, no copies to Android res/, no strict promotion.
"""
⋮----
ROLES = ("OP", "LOG", "ENG")
ACTIONS = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}
⋮----
def make_bundle(source: Path, output: Path) -> dict
⋮----
original=json.loads((source/"creation-manifest.json").read_text(encoding="utf8"))
expected={f"CHR-{role}-{action}" for role in ROLES for action in ACTIONS}
⋮----
rows=[]
svg_count=0
⋮----
ident=f"CHR-{role}-{action}"
name=f"zte_chr_{role.lower()}_{action.lower()}_final.png"
p=source/"candidates"/name
data=p.read_bytes()
⋮----
svg=source/"src_svg"/role/action/f"{frame:02d}.svg"
payload=svg.read_bytes()
⋮----
report={"schema_version":1,"review_only":True,"strict_done_increased":False,
⋮----
def main() -> int
⋮----
parser=argparse.ArgumentParser()
⋮----
a=parser.parse_args()
result=make_bundle(a.source,a.output)
```

## File: sprites/package_tech_actions_runtime.py
```python
#!/usr/bin/env python3
"""Package six TECH animation candidates as pivot-stable preview atlases.

This is a staging/export step. It NEVER alters canonical queues or approves art.
"""
⋮----
ACTIONS=('WALK','CARRY','IDLE','WORK','REPAIR','CELEB')
SIDE=512
SIZES=(128,256)
⋮----
def sha(path:Path)->str
⋮----
def ensure(ok:bool,message:str)->None
⋮----
def verify(root:Path)
⋮----
index=json.loads((root/'production-index.json').read_text(encoding='utf-8'))
⋮----
items=index.get('actions',[])
⋮----
by_action={x['action']:x for x in items}
shared=index['source_skin_sha256']
validated={}
⋮----
asset='CHR-TECH-'+action
record=by_action[action]
⋮----
folder=root/action
m=json.loads((folder/'qa-manifest.json').read_text(encoding='utf-8'))
features=m.get('renderer_features',{})
⋮----
qa=m['qa']
⋮----
count=int(m['frames']); fps=int(m['fps'])
⋮----
expected_origin=round(count*5/24) if action=='WORK' else 0
⋮----
transfer=m.get('weight_transfer',{})
expected_transfer=action in ('WALK','CARRY')
⋮----
arm_height=qa.get('celebration_min_arm_raise_px')
⋮----
wrist_span=qa.get('celebration_min_wrist_span_px')
⋮----
tool=qa.get('repair_torch_length_range_px')
⋮----
poses=json.loads((folder/'frame-poses.json').read_text(encoding='utf-8'))
events=json.loads((folder/'footstep-events.json').read_text(encoding='utf-8'))
⋮----
expected=list(work_event_indices(count,expected_origin))
actual=[i for i,event in enumerate(events)
⋮----
expected=[i for i in range(count)
⋮----
frames=sorted((folder/'frames').glob('*.png'))
⋮----
def review_html(data:dict)->str
⋮----
sources=json.dumps({name:{'src':a['variants']['128']['path'],
template='''<!doctype html><html lang="fr"><head><meta charset="utf-8">
⋮----
def render_contact_shadow(p:dict)->Image.Image
⋮----
"""Optional frame-aligned ground-shadow atlas, isolated from character pixels."""
layer=Image.new('RGBA',(SIDE,SIDE))
⋮----
locked=p.get(contact,False)
height=max(0,449-y)
strength=100 if locked else max(18,round(62-height*.65))
radius=34 if locked else max(20,round(30-height*.13))
mask=Image.new('RGBA',(SIDE,SIDE))
⋮----
layer=Image.alpha_composite(layer,mask.filter(ImageFilter.GaussianBlur(4)))
⋮----
def game_scale_metrics(frame:Image.Image, side:int=96)->dict
⋮----
"""Objective 96px silhouette sanity check, NOT an artistic approval."""
tiny=frame.resize((side,side),Image.Resampling.LANCZOS)
alpha=tiny.getchannel('A')
opaque=sum(alpha.histogram()[128:])
binary=alpha.point(lambda v: 255 if v>=128 else 0)
bbox=binary.getbbox()
⋮----
margin=min(x0,y0,side-x1,side-y1)
⋮----
def verify_temporal_evidence(index:dict,records:dict,report_path:Path)->dict
⋮----
"""Bind temporal QA to the exact ordered RGBA frames being packaged."""
report=json.loads(report_path.read_text(encoding='utf-8'))
⋮----
actions=report.get('actions',{})
⋮----
entry=actions[action]
⋮----
chain=hashlib.sha256()
⋮----
def package(source:Path,output:Path,temporal_report:Path|None=None)->dict
⋮----
shared_view=shared_crop(collect_frame_bounds(records,ACTIONS))
evidence=(verify_temporal_evidence(index,records,temporal_report)
⋮----
exported={'format':'zte-tech-actions-runtime-v1','strict_status':'NEEDS_REVIEW',
overview=Image.new('RGB',(900,672),(23,29,40))
draw=ImageDraw.Draw(overview)
contact96=Image.new('RGB',(120+96*8,40+108*6),(25,33,45))
contact_draw=ImageDraw.Draw(contact96)
contact_focus=Image.new('RGB',contact96.size,(25,33,45))
focus_draw=ImageDraw.Draw(contact_focus)
⋮----
rec=records[action]; count=rec['count'];cols=6;rows=math.ceil(count/cols)
pics=[];bounds=[];game_scale=[]
⋮----
frame=image.copy()
alpha=frame.getchannel('A')
b=alpha.point(lambda px:255 if px>=128 else 0).getbbox()
⋮----
img=pics[(j*count)//8].resize((96,96),Image.Resampling.LANCZOS)
⋮----
zoomed=framed_sprite(pics[(j*count)//8],shared_view,96)
⋮----
variants={};shadow_variants={}
shadow_frames=[render_contact_shadow(p) for p in rec['poses']]
⋮----
folder=output/'atlases';folder.mkdir(exist_ok=True)
atlas=Image.new('RGBA',(size*cols,size*rows))
⋮----
scaled=im.resize((size,size),Image.Resampling.LANCZOS)
⋮----
path=folder/f'{action.lower()}-{size}.png'
⋮----
shadow_atlas=Image.new('RGBA',(size*cols,size*rows))
⋮----
shadow_path=folder/f'{action.lower()}-shadow-{size}.png'
⋮----
focused_variants={};focused_shadow_variants={}
⋮----
folder=output/'focused-atlases';folder.mkdir(exist_ok=True)
focus_atlas=Image.new('RGBA',(size*cols,size*rows))
focus_shadow_atlas=Image.new('RGBA',(size*cols,size*rows))
⋮----
focused=framed_sprite(frame,shared_view,size)
⋮----
# Shadows are soft blur fields, not part of the strict
# character silhouette. They use the identical camera.
shadow=shadow_frames[i].crop(shared_view).resize(
⋮----
focus_path=folder/f'{action.lower()}-focused-{size}.png'
⋮----
shadow_path=folder/f'{action.lower()}-focused-shadow-{size}.png'
⋮----
xx=450*(idx%2);yy=224*(idx//2)
icon=pics[0].resize((190,190),Image.Resampling.LANCZOS)
⋮----
union=[min(b[0] for b in bounds),min(b[1] for b in bounds),
events_dir=output/'events';events_dir.mkdir(exist_ok=True)
events_file=events_dir/f'{action.lower()}.json'
⋮----
def main()
⋮----
parser=argparse.ArgumentParser(description=__doc__)
⋮----
args=parser.parse_args()
result=package(args.source,args.output,args.temporal_report)
```

## File: sprites/patch_final_character_motion.py
```python
#!/usr/bin/env python3
⋮----
p=Path('tools/sprites/kaggle_character_sheet_factory_v1.py')
s=p.read_text(encoding='utf-8')
⋮----
old_repair="'REPAIR':['half-kneel and reach tool toward low repair point','tool pressed to low repair point, free hand bracing','tool moves horizontally across repair point, no sparks','lean closer and inspect repair point','tool contacts mid-height repair point','free hand adjusts component while tool stays ready','pull back and inspect with torso upright','second tool contact at mid height','rise from half-kneel while lowering tool','neutral repair-ready stance']"
new_repair="'REPAIR':['deep half-kneel, torso leaned far forward, right arm fully extended with tool toward low repair point','tool pressed low, free hand bracing wide, shoulders rotated toward repair','tool sweeps clearly left across low repair point, torso follows, no sparks','pull tool back to chest and lean close to inspect, elbow strongly bent','rise to wide crouch, tool reaches diagonally to mid-height repair point','free hand reaches high to adjust component while tool hand stays low','pull both arms back, torso upright and weight shifted onto rear leg','second strong tool contact at mid height with opposite shoulder forward','rise from crouch while lowering tool beside thigh, free arm extended for balance','standing repair-ready stance, both arms lowered and feet apart']"
old_celeb="'CELEB':['neutral stance both arms down','right arm begins lifting, elbow bent','right fist reaches shoulder height, torso opens','right fist fully overhead, weight shifts to left leg','small overhead fist pump with opposite arm bent','arm lowers to shoulder height, weight recenters','arm lowers beside body','return to neutral stance']"
new_celeb="'CELEB':['neutral stance both arms down, feet apart','right arm lifts outward to forty-five degrees, elbow bent, left arm stays down','right fist at shoulder height, left arm swings outward, torso rotates right','right fist fully overhead, left arm bent across chest, weight shifts strongly to left leg','both arms clearly raised, right fist high and left fist at shoulder, torso leaning left','right arm drops to shoulder height while left arm extends outward, weight shifts right','right arm lowers diagonally while left arm returns down, torso recenters','return to neutral stance with both arms fully down and feet apart']"
old_strength="""elif i['action']=='REPAIR':
new_strength="""elif i['action']=='REPAIR':
⋮----
s=s.replace('character-sheet-flux-v1.7-action-motion-retry','character-sheet-flux-v1.8-final-motion-guard')
s=s.replace(old_repair,new_repair).replace(old_celeb,new_celeb).replace(old_strength,new_strength)
```

## File: sprites/plan_sprite_batches.py
```python
#!/usr/bin/env python3
"""Build deterministic production lanes from the canonical AAA sprite manifest.

The planner is generation-backend agnostic. It groups remaining assets by the
cheapest safe production path and, critically, treats already-materialized art
as integration work even when the human ledger is stale.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
INCOMING = ROOT / "art/incoming/final-sprites"
OUT = ROOT / "art/production"
ROW = re.compile(
⋮----
BATCH_SIZE = {
⋮----
@dataclass(frozen=True)
class Asset
⋮----
id: str
asset: str
description: str
runtime: str
status: str
lane: str
materialized: bool
⋮----
def is_materialized(runtime: str) -> bool
⋮----
runtime_path = ROOT / runtime
stem = Path(runtime).stem
candidate = INCOMING / f"{stem}.png"
⋮----
def classify(asset_id: str, description: str, status: str, runtime: str, materialized: bool) -> str
⋮----
# An installed but semantically rejected/review-pending character must not
# be counted as an ordinary integration-only task.
⋮----
aid = asset_id.upper()
text = f"{description} {runtime}".lower()
⋮----
def chunks(items: list[Asset], n: int) -> list[list[Asset]]
⋮----
def main() -> int
⋮----
rows: list[Asset] = []
⋮----
m = ROW.match(raw.strip())
⋮----
d = m.groupdict()
materialized = is_materialized(d["runtime"])
⋮----
onboarding = [a for a in rows if a.id == "ONB-00"]
⋮----
# ONB-00 is intentionally outside the canonical strict 235-asset objective.
rows = [a for a in rows if a.id != "ONB-00"]
⋮----
remaining = [a for a in rows if a.status != "DONE"]
lanes: dict[str, list[Asset]] = {name: [] for name in BATCH_SIZE}
⋮----
building_families: dict[str, list[str]] = {}
character_groups: dict[str, list[str]] = {}
⋮----
family="-".join(a.id.split("-")[:2])
⋮----
parts=a.id.split("-")
group="-".join(parts[:2])
⋮----
plan = {
⋮----
batches = chunks(assets, BATCH_SIZE[lane])
⋮----
md = [
```

## File: sprites/pollinations_building_batch.py
```python
#!/usr/bin/env python3
⋮----
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
QUEUE=ROOT/'art/production/controlled-building-regen-queue.json'
PROD=ROOT/'art/production'
INCOMING=ROOT/'art/incoming/final-sprites'
RUNTIME=ROOT/'app/src/main/res/drawable-nodpi'
⋮----
import pollinations_building_factory as pf  # noqa
⋮----
def manifest_rows()
⋮----
out={}
⋮----
cols=[c.strip() for c in line.split('|')[1:-1]]
⋮----
def pending_rows()
⋮----
rows=manifest_rows()
⋮----
q=json.loads(QUEUE.read_text(encoding='utf-8'))
out=[]
⋮----
aid=str(item.get('id','')).upper()
⋮----
def mark_runtime(asset_id:str)
⋮----
lines=MANIFEST.read_text(encoding='utf-8').splitlines()
out=[]; changed=0
⋮----
cols[4]='RUNTIME'; line='| '+' | '.join(cols)+' |'; changed+=1
⋮----
def mark_queue(asset_id:str,status:str,seed:int)
⋮----
found=False
⋮----
found=True
⋮----
def run(cmd,env=None)
⋮----
def main()
⋮----
count=max(1,min(int(os.getenv('POLLINATIONS_BATCH_COUNT','8')),8))
attempts=max(1,min(int(os.getenv('POLLINATIONS_ATTEMPTS','3')),4))
base=int(os.getenv('POLLINATIONS_BASE_SEED','73117'))
⋮----
candidate_only = queued or os.getenv('POLLINATIONS_CANDIDATE_ONLY','').lower() in {'1','true','yes'}
summary={
⋮----
session=new_session('u2net')
⋮----
targets=initial[:count]
⋮----
families={row[0].split('-T')[0] for row in targets}
⋮----
family_attempts=[]
⋮----
seed=(base + attempt*7919) % 2147483647
⋮----
generated=pf.generate_family(targets,seed=seed,session=session)
all_ok=True
qa_rows=[]
⋮----
aid=row[0]
qa=PROD/f'pollinations-{aid.lower()}-qa.json'
contact=PROD/f'pollinations-{aid.lower()}-contact.png'
q=run([sys.executable,'tools/sprites/build_sprite_contact_sheet.py','--files',str(out.relative_to(ROOT)),'--output',str(contact.relative_to(ROOT)),'--report',str(qa.relative_to(ROOT))])
qd=json.loads(qa.read_text()) if qa.exists() else {}
rows_qa=qd.get('assets',[])
passed=(q.returncode==0 and len(rows_qa)==1 and rows_qa[0].get('pass'))
⋮----
all_ok=False
⋮----
ok=False
attempts_log=[]
⋮----
seed=((base if candidate_only else base + slot*1009) + attempt*7919) % 2147483647
stem=None
⋮----
rp=PROD/f'pollinations-{aid.lower()}-report.json'
⋮----
stem=out.stem
⋮----
qrows=qd.get('assets',[])
⋮----
ok=True
⋮----
env=os.environ.copy(); env['SPRITE_TARGETS']=stem
fin=run([sys.executable,'tools/sprites/process_final_sprites.py'],env=env)
runtime=RUNTIME/f'{stem}.webp'
⋮----
rqa=PROD/f'pollinations-{aid.lower()}-runtime-qa.json'
rv=run([sys.executable,'tools/sprites/validate_runtime_asset.py','--asset-id',aid,'--path',str(runtime.relative_to(ROOT)),'--report',str(rqa.relative_to(ROOT))])
⋮----
data=json.loads(rqa.read_text()) if rqa.exists() else {'issues':['runtime-validator-failed']}
```

## File: sprites/pollinations_building_factory.py
```python
#!/usr/bin/env python3
⋮----
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
REPORT=ROOT/'art/production/pollinations-report.json'
⋮----
FAMILY_IDENTITY={
⋮----
TIER_LANGUAGE={
⋮----
def fetch_image(prompt:str, seed:int, width:int=1024, height:int=1024)
⋮----
q=urllib.parse.quote(prompt,safe='')
url=f'https://image.pollinations.ai/prompt/{q}?model=flux&width={width}&height={height}&seed={int(seed)}&nologo=true&private=true&enhance=false&safe=true'
tmp=Path(f'/tmp/pollinations-board-{int(seed)}-{width}x{height}.png')
req=urllib.request.Request(url,headers={'User-Agent':'zero-to-empire-github-actions/1.0'})
⋮----
data=r.read()
⋮----
def generate_family(rows, seed=73117, session=None)
⋮----
parsed=[]
family=None
⋮----
aid=row[0]
m=re.fullmatch(r'BLD-(\d{2})-T(\d)',aid)
⋮----
family=int(fam)
⋮----
identity=FAMILY_IDENTITY.get(family,f'industrial business family {family}')
tiers='; '.join(f'T{tier}: {TIER_LANGUAGE[tier]}' for tier,_ in parsed)
prompt=(
raw=fetch_image(prompt,seed,1024,1024)
outputs=[]
⋮----
col=idx%4; r=idx//4
crop=raw.crop((col*256,r*512,(col+1)*256,(r+1)*512))
isolated=isolate(crop,session=session)
⋮----
fam=f'{family:02d}'
stem=f'zte_business_{fam}_t{tier}_final'
⋮----
out=INCOMING/f'{stem}.png'
⋮----
report={
rp=ROOT/'art/production'/f'pollinations-{aid.lower()}-report.json'
⋮----
def fail(msg)
⋮----
def next_target()
⋮----
explicit=os.getenv('SPRITE_TARGET','').strip().upper()
rows=[]
⋮----
cols=[c.strip() for c in line.split('|')[1:-1]]
⋮----
def isolate(im, session=None)
⋮----
# CPU background removal via U²-Net/rembg. This is deterministic post-
# processing on the GitHub runner; downstream QA thresholds remain unchanged.
⋮----
src=im.convert('RGBA')
⋮----
cut=remove(src, session=session, alpha_matting=False)
⋮----
cut=Image.open(cut).convert('RGBA')
⋮----
cut=cut.convert('RGBA')
⋮----
a=cut.getchannel('A')
# Hard-clean tiny matte haze so component analysis reflects real subject.
a=a.point(lambda v: 0 if v<24 else 255 if v>224 else v)
⋮----
# Keep the dominant connected alpha component; detached props/debris are
# rejected at source rather than hidden by a relaxed QA gate.
binary=a.point(lambda v:255 if v>=64 else 0)
bp=binary.load()
seen=set(); comps=[]
⋮----
comp=[]; stack=[(x,y)]; seen.add((x,y))
⋮----
keep=set(max(comps,key=len))
cleaned=Image.new('RGBA',(w,h),(0,0,0,0))
srcpx=cut.load(); dst=cleaned.load()
⋮----
bbox=cleaned.getchannel('A').getbbox()
⋮----
subject=cleaned.crop(bbox)
⋮----
# Preserve enough detail while guaranteeing safe transparent margins.
side=max(768, int(max(sw,sh)/0.68))
side=min(2048, side)
⋮----
scale=(side*0.68)/max(sw,sh)
subject=subject.resize((max(1,round(sw*scale)),max(1,round(sh*scale))),Image.Resampling.LANCZOS)
⋮----
canvas=Image.new('RGBA',(side,side),(0,0,0,0))
⋮----
def generate(row, seed=73117, session=None, report_path: Path | None = None)
⋮----
fam_i=int(fam); tier_i=int(tier)
identity=FAMILY_IDENTITY.get(fam_i,f'industrial business family {fam_i}')
tier_language=TIER_LANGUAGE[tier_i]
⋮----
url=f'https://image.pollinations.ai/prompt/{q}?model=flux&width=1024&height=1024&seed={int(seed)}&nologo=true&private=true&enhance=false&safe=true'
tmp=Path(f'/tmp/pollinations-{aid.lower()}-{int(seed)}.png')
⋮----
try: im=Image.open(tmp)
⋮----
isolated=isolate(im, session=session)
⋮----
rp=report_path or REPORT
⋮----
def main()
⋮----
row=next_target()
seed=int(os.getenv('POLLINATIONS_SEED','73117'))
```

## File: sprites/pollinations_character_sheet_factory.py
```python
#!/usr/bin/env python3
⋮----
# Support both execution as a script and importlib-based tooling from tools/assets.
⋮----
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
OUT=ROOT/'art/production'
QUEUE=OUT/'controlled-character-regen-queue.json'
# Each generation strategy owns its own cache: never reuse pre-v3 body
# fragments/identity-drifts as successful images of a different strategy.
STANDALONE_CACHE_EPOCH='full-body-per-frame-v3'
⋮----
ROLES={
ACTIONS={
POSES={
⋮----
def pending()
⋮----
requested={x.strip().upper() for x in os.getenv('POLLINATIONS_CHR_TARGET_IDS','').split(',') if x.strip()}
manifest={}
⋮----
p=[x.strip() for x in line.split('|')[1:-1]]
⋮----
aid=p[0]; z=aid.split('-')
⋮----
runtime=p[3].replace(chr(96),'')
⋮----
q=json.loads(QUEUE.read_text(encoding='utf-8'))
out=[]
⋮----
aid=str(item.get('id','')).upper()
⋮----
# A controlled queue is authoritative, including when all targets are
# BLOCKED, already reviewed, or reserved by another provider. Falling
# through to unrelated manifest TODOs would bypass the reservation.
⋮----
def candidate_destination(item)
⋮----
"""Controlled semantic repairs are immutable staged candidates, not runtime art.

    The original Kaggle/legacy sheet remains untouched until an explicit
    accepted review and separately verified runtime promotion.
    """
q=json.loads(QUEUE.read_text(encoding='utf-8')) if QUEUE.is_file() else {}
⋮----
def mark_queue(aid,status,seed=None,producer=None,producer_run_id=None)
⋮----
def fetch(prompt,seed)
⋮----
q=urllib.parse.quote(prompt,safe='')
last=None
⋮----
s=(seed+n*7919) % 2147483647
url=f'https://image.pollinations.ai/prompt/{q}?model=flux&width=1024&height=1024&seed={s}&nologo=true&private=true&enhance=false&safe=true'
req=urllib.request.Request(url,headers={'User-Agent':'zero-to-empire-github-actions/1.0','Accept':'image/*'})
⋮----
data=r.read()
⋮----
p=Path('/tmp')/f'chr-sheet-{s}.png'
⋮----
last=e
⋮----
def validate_source_full_body(bb,w,h,action=None,standalone=False)
⋮----
cw=max(0,right-left); ch=max(0,bottom-top)
⋮----
# Cropped head/torso fragments were historically normalized into plausible
# 256px cells. Reject source crops before resizing can hide the defect.
edge=max(4,round(h*.018))
⋮----
min_height=.65 if standalone else (.42 if action=='REPAIR' else .55)
⋮----
def safe_source_margin(image)
⋮----
"""Pad an *already complete* source, never hallucinate missing body parts.

    A fully isolated sprite may have only 8px of empty source margin,
    though both feet are visibly present. Reframe its existing pixels on
    transparent space before imposing conservative full-body constraints.
    If ANY actual alpha touches an edge, fail instead of hiding truncation.
    """
⋮----
bb=image.getchannel('A').getbbox()
⋮----
soft=max(4,round(h*.018))
⋮----
pad=round(min(w,h)*.075)
padded=Image.new('RGBA',(w+2*pad,h+2*pad))
⋮----
def cutout(raw, action=None, standalone=False)
⋮----
im=remove(raw,alpha_matting=False).convert('RGBA')
a=im.getchannel('A').point(lambda v:0 if v<24 else 255 if v>224 else v)
⋮----
mask=a.point(lambda v:255 if v>=64 else 0)
px=mask.load(); seen=set(); comps=[]
⋮----
stack=[(x,y)]; seen.add((x,y)); comp=[]
⋮----
keep=set(max(comps,key=len))
clean=Image.new('RGBA',(w,h),(0,0,0,0))
src=im.load(); dst=clean.load()
⋮----
clean=safe_source_margin(clean)
⋮----
bb=clean.getchannel('A').getbbox()
⋮----
crop=clean.crop(bb); cw,ch=crop.size
⋮----
s=min(176/cw,218/ch)
crop=crop.resize((max(1,round(cw*s)),max(1,round(ch*s))),Image.Resampling.LANCZOS)
cell=Image.new('RGBA',(256,256),(0,0,0,0))
x=(256-crop.width)//2; y=238-crop.height
⋮----
aa=cell.getchannel('A')
cov=sum(aa.histogram()[8:])/(256*256)
⋮----
def iou(a,b)
⋮----
A=a.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
B=b.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
pa,pb=A.load(),B.load(); inter=union=0
⋮----
aa=pa[x,y]>0; bb=pb[x,y]>0
⋮----
def lower_body_motion(frames)
⋮----
vals=[]
⋮----
A=frames[n-1].getchannel('A')
B=frames[n].getchannel('A')
ba=A.getbbox(); bb=B.getbbox()
⋮----
top=max(0,min(ba[1]+int((ba[3]-ba[1])*.55),bb[1]+int((bb[3]-bb[1])*.55)))
a=A.crop((0,top,256,256)).resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
b=B.crop((0,top,256,256)).resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
pa,pb=a.load(),b.load(); inter=union=0
⋮----
aa=pa[x,y]>0; bbb=pb[x,y]>0
⋮----
def actionqa(frames,action)
⋮----
vals=[iou(frames[n-1],frames[n]) for n in range(1,len(frames))]
mean_change=(sum(1-x for x in vals)/len(vals)) if vals else 0.0
⋮----
motion=lower_body_motion(frames)
⋮----
floors={'WORK':.10,'CARRY':.12,'REPAIR':.09,'CELEB':.10,'IDLE':.025}
floor=floors.get(action,.05)
⋮----
def appearance_hist(frame)
⋮----
# Coarse foreground RGB histogram: catches role/wardrobe/identity drift that
# silhouette IoU alone cannot detect.
rgb=frame.convert('RGB'); alpha=frame.getchannel('A')
bins=[0]*512; total=0
⋮----
def hist_similarity(a,b)
⋮----
# Histogram intersection in [0,1].
⋮----
def sheetqa(frames)
⋮----
h0=appearance_hist(frames[0])
sims=[hist_similarity(h0,appearance_hist(f)) for f in frames[1:]]
⋮----
bad=[n+1 for n,v in enumerate(sims) if v<.58]
⋮----
bottoms=[]; centers=[]
⋮----
bb=frame.getchannel('A').getbbox()
⋮----
def sheet_prompt(item)
⋮----
action=item['action']; fc=ACTIONS[action][1]
poses=', '.join(POSES[action][:fc])
framing = (
⋮----
def repair_frame_prompt(item, pose)
⋮----
def walk_frame_prompt(item, pose)
⋮----
def generate_walk_frames(item, seed)
⋮----
frames=[]
cache_dir=OUT/'pollinations-frame-cache'/item['id']
⋮----
cache_file=cache_dir/f'{n:02d}.png'
⋮----
frame=Image.open(cache_file).convert('RGBA')
cov=sum(frame.getchannel('A').histogram()[8:])/(256*256)
⋮----
rev_file=cache_dir/f'{n:02d}.rev'
⋮----
revision=int(rev_file.read_text(encoding='utf-8').strip()) if rev_file.is_file() else 0
⋮----
revision=0
frame_seed=(27191 + sum((i+1)*ord(ch) for i,ch in enumerate(item['id']))*1013 + n*104729 + revision*1000003) % 2147483647
raw=fetch(walk_frame_prompt(item,pose),frame_seed)
⋮----
def generate_repair_frames(item, seed)
⋮----
frame_seed=(19417 + sum((i+1)*ord(ch) for i,ch in enumerate(item['id']))*1009 + n*104729 + revision*1000003) % 2147483647
raw=fetch(repair_frame_prompt(item,pose),frame_seed)
⋮----
# Explicit immutable appearance descriptors for independent remote requests.
# Opaque face protection deliberately reduces identity drift between poses.
ROLE_IDENTITY_ANCHORS={
⋮----
def independent_frame_prompt(item,pose)
⋮----
"""Explicitly request ONE complete subject, never a sheet or sprite atlas."""
action=item['action']
props={
⋮----
def require_standalone_body(frame)
⋮----
"""Do not cache obvious portrait/torso fragments as valid whole-body poses.

    Risk screening only: cannot detect missing props or grant semantic approval.
    """
geometry=frame_geometry(frame)
bad=set(geometry.get('risk_flags',[])) & {
⋮----
def generate_independent_frames(item,seed)
⋮----
"""Produce each pose separately; never split one tall image into limbs."""
⋮----
cache_dir=OUT/'pollinations-frame-cache'/item['id']/STANDALONE_CACHE_EPOCH
⋮----
# Old v3 caches can still contain cropped torsos. Never
# trust them on restart or retry the exact same bad seed.
⋮----
current=int(rev_file.read_text(encoding='utf-8')) if rev_file.is_file() else 0
⋮----
current=0
⋮----
frame_seed=(seed+sum((i+1)*ord(ch) for i,ch in enumerate(item['id']))*1009+
raw=fetch(independent_frame_prompt(item,pose),frame_seed)
⋮----
def extract_frames(raw,frame_count,action=None)
⋮----
raw=raw.resize((1024,1024),Image.Resampling.LANCZOS)
⋮----
x=(n%4)*256; y=(n//4)*256
cell_raw=raw.crop((x,y,x+256,y+256))
⋮----
def main()
⋮----
items=pending()[:max(1,min(int(os.getenv('POLLINATIONS_CHR_BATCH','1')),2))]
⋮----
attempts=max(1,min(int(os.getenv('POLLINATIONS_CHR_ATTEMPTS','2')),3))
base=int(os.getenv('POLLINATIONS_CHR_SEED','19417'))
⋮----
rep=[]
⋮----
fc=ACTIONS[it['action']][1]
done=False; last=''
⋮----
seed=(base+ix*100000+att*10007) % 2147483647
screen=None
⋮----
frames=generate_repair_frames(it,seed)
⋮----
frames=generate_walk_frames(it,seed)
⋮----
frames=generate_independent_frames(it,seed)
# The atlas may be formed ONLY after each standalone frame
# passes full-body risk screening and continuity checks.
screen=clip_risk(frames)
⋮----
why=f'{why} {action_why}'
sheet=Image.new('RGBA',(1024,1024),(0,0,0,0))
⋮----
p=candidate_destination(it)
⋮----
canonical=INCOMING/f"{it['stem']}.png"
original_sha256=(
⋮----
producer_run_id=os.getenv('GITHUB_RUN_ID') or None
⋮----
done=True
⋮----
last=str(e)
# Never retry the same known-bad cached pixels. A producer
# outage mid-sequence is different: retain the valid prefix.
bad_frames=[]
⋮----
bad_frames=[int(x) for x in last.rsplit(' frames=',1)[1].split(',') if x.strip()]
⋮----
bad_frames=[i for i,entry in enumerate(screen.get('frames',[]))
⋮----
bad_frames=list(range(1,fc))
⋮----
cache_dir=OUT/'pollinations-frame-cache'/it['id']
⋮----
cache_dir=cache_dir/STANDALONE_CACHE_EPOCH
cache_file=cache_dir/f'{bad:02d}.png'
⋮----
rev_file=cache_file.with_suffix('.rev')
⋮----
revision=int(rev_file.read_text(encoding='utf-8').strip())+1 if rev_file.is_file() else 1
⋮----
revision=1
⋮----
provider_error = (
```

## File: sprites/procedural_fx_factory.py
```python
#!/usr/bin/env python3
"""Instant deterministic small-FX factory for Zero -> Empire.

Generates FX-00..FX-03 as native 8-frame 4x2 transparent sheets without GPU.
Supports one target via SPRITE_TARGET or a comma-separated batch via
SPRITE_TARGETS. Batch mode avoids repeated runner/process startup overhead.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
INCOMING = ROOT / "art/incoming/final-sprites"
CELL = 128
COLS = 4
FRAMES = 8
SIZE = (512, 256)
PAD = 6
SUPPORTED = ("FX-00", "FX-01", "FX-02", "FX-03")
⋮----
def layer() -> Image.Image
⋮----
def composite_glow(base: Image.Image, glow: Image.Image, radius: float) -> None
⋮----
blurred = glow.filter(ImageFilter.GaussianBlur(radius))
⋮----
def sparks(frame: int) -> Image.Image
⋮----
rng = random.Random(7000 + frame)
im = layer()
glow = layer()
d = ImageDraw.Draw(glow)
⋮----
phase = frame / 7.0
core_r = max(2, round(3 + 4 * math.sin(math.pi * phase)))
⋮----
count = 8 + min(frame, 4) * 2
reach = 18 + frame * 5
⋮----
a = (2 * math.pi * i / count) + rng.uniform(-0.16, 0.16)
r0 = 6 + rng.uniform(0, 6)
r1 = reach * rng.uniform(0.55, 1.0)
⋮----
col = (255, rng.randint(155, 225), rng.randint(35, 80), max(35, 245 - frame*24))
⋮----
rr = 1 if i % 2 else 2
⋮----
def flame(frame: int, plasma: bool) -> Image.Image
⋮----
rng = random.Random((9200 if plasma else 8100) + frame)
⋮----
g = ImageDraw.Draw(glow)
⋮----
cx = 64 + math.sin(frame * 1.7) * (2.5 if plasma else 1.8)
base_y = 94
height = (78 if plasma else 58) * (0.82 + 0.18 * math.sin(math.pi * (phase + .15)))
width = 30 if plasma else 22
⋮----
t = j / (10 if plasma else 7)
y = base_y - t * height
wobble = math.sin(t * 7.0 + frame * .9) * (5.5 * t) + rng.uniform(-2.5, 2.5)
rx = max(3, width * (1 - .62*t) * rng.uniform(.72, 1.08))
ry = max(4, (14 if plasma else 11) * (1 - .30*t) * rng.uniform(.8, 1.2))
⋮----
c = (110, 230, 255, 185)
⋮----
c = (255, 118, 18, 230)
⋮----
c = (255, 194, 42, 235)
⋮----
c = (255, 245, 205, 230)
⋮----
core_w = 13 if plasma else 9
core_h = 24 if plasma else 17
⋮----
def smoke(frame: int) -> Image.Image
⋮----
rng = random.Random(10300 + frame)
⋮----
soft = layer()
d = ImageDraw.Draw(soft)
p = frame / 7.0
cx = 64 + math.sin(frame * 0.8) * 3
cy = 80 - 22 * p
count = 7 + frame
⋮----
a = rng.uniform(0, math.tau)
radius = rng.uniform(5, 18 + 9*p)
x = cx + math.cos(a) * radius * rng.uniform(.3, 1.0)
y = cy + math.sin(a) * radius * .58
rr = rng.uniform(8, 16) * (0.72 + .6*p)
alpha = int((155 - frame*11) * rng.uniform(.65, 1.0))
gray = rng.randint(105, 148)
⋮----
blurred = soft.filter(ImageFilter.GaussianBlur(4.1 + p*2.2))
⋮----
def ensure_padding(im: Image.Image) -> Image.Image
⋮----
bbox = im.getbbox()
⋮----
crop = im.crop(bbox)
max_side = CELL - 2*PAD
scale = min(max_side / crop.width, max_side / crop.height, 1.0)
crop = crop.resize((max(1, round(crop.width*scale)), max(1, round(crop.height*scale))), Image.Resampling.LANCZOS)
out = layer()
⋮----
def validate(sheet: Image.Image) -> None
⋮----
cell = sheet.crop((x0, y0, x0+CELL, y0+CELL))
⋮----
a = cell.getchannel("A")
edges = [a.crop((0,0,CELL,4)), a.crop((0,CELL-4,CELL,CELL)), a.crop((0,0,4,CELL)), a.crop((CELL-4,0,CELL,CELL))]
⋮----
def build(target: str) -> Image.Image
⋮----
makers = {
⋮----
sheet = Image.new("RGBA", SIZE, (0,0,0,0))
⋮----
f = ensure_padding(makers[target](i))
⋮----
def targets_from_env() -> list[str]
⋮----
raw = os.getenv("SPRITE_TARGETS", "").strip()
⋮----
targets = [part.strip().upper() for part in raw.split(",") if part.strip()]
⋮----
targets = [os.getenv("SPRITE_TARGET", "FX-03").upper()]
invalid = [target for target in targets if target not in SUPPORTED]
⋮----
def main() -> int
⋮----
targets = targets_from_env()
⋮----
num = target.split("-")[-1]
out = INCOMING / f"zte_fx_{num}_final.png"
```

## File: sprites/procedural_terrain_factory.py
```python
#!/usr/bin/env python3
"""Deterministically author the 14 terrain/infrastructure masters without GPU.

These are 1024x1024 RGBA isometric world tiles/connectors. The factory keeps a
large transparent exterior margin, a consistent 34-degree-ish 2.5D read and
category-specific industrial details. Technical validation is strict; semantic
AAA acceptance remains a separate inspection gate.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
INCOMING = ROOT / "art/incoming/final-sprites"
RUNTIME = ROOT / "app/src/main/res/drawable-nodpi"
SIDE = 1024
⋮----
MARGIN = 64
⋮----
NAMES = {
⋮----
ERA = {
⋮----
def diamond() -> list[tuple[int, int]]
⋮----
def era_for(i: int) -> int
⋮----
def inside_diamond(x: int, y: int) -> bool
⋮----
def add_texture(base: Image.Image, i: int, base_rgb: tuple[int,int,int]) -> None
⋮----
rng = random.Random(7100+i)
px = base.load()
⋮----
x = rng.randrange(CX-RX, CX+RX)
y = rng.randrange(CY-RY, CY+RY)
⋮----
delta = rng.randint(-13, 13)
⋮----
a = rng.randint(16, 42)
⋮----
def iso_line(draw: ImageDraw.ImageDraw, p1, p2, fill, width=8)
⋮----
def render(i: int) -> Image.Image
⋮----
era = era_for(i)
⋮----
im = Image.new("RGBA", (SIDE,SIDE), (0,0,0,0))
d = ImageDraw.Draw(im, "RGBA")
poly = diamond()
⋮----
# Shared inset border improves tile readability without baked UI semantics.
inset = [(CX, CY-RY+28),(CX+RX-50,CY),(CX,CY+RY-28),(CX-RX+50,CY)]
⋮----
rng=random.Random(900+i)
⋮----
x=rng.randint(CX-290,CX+290); y=rng.randint(CY-130,CY+130)
⋮----
pts=[(x,y),(x+rng.randint(-35,35),y+rng.randint(8,28)),(x+rng.randint(-55,55),y+rng.randint(20,45))]
⋮----
road=(48,50,53,255) if era<2 else (40,47,56,255)
⋮----
x1=CX+k; y1=CY-k//3
⋮----
wide=38 if i in (11,13) else 26
⋮----
x=CX+k; y=CY-k//3
⋮----
glow=Image.new("RGBA", im.size,(0,0,0,0)); gd=ImageDraw.Draw(glow,"RGBA")
⋮----
glow=glow.filter(ImageFilter.GaussianBlur(15)); im.alpha_composite(glow)
⋮----
pad=[(CX,CY-150),(CX+265,CY-5),(CX,CY+150),(CX-265,CY+5)]
⋮----
pad=[(CX,CY-165),(CX+290,CY-10),(CX,CY+165),(CX-290,CY+10)]
⋮----
# Upper-left highlight + lower-right shadow preserve shared lighting contract.
⋮----
def validate(im: Image.Image, i: int) -> None
⋮----
a=im.getchannel("A")
bbox=a.getbbox()
⋮----
coverage=sum(a.histogram()[8:])/(SIDE*SIDE)
⋮----
def main() -> int
⋮----
im=render(i); validate(im,i)
stem=f"zte_terrain_{i:02d}_final"
png=INCOMING/f"{stem}.png"; webp=RUNTIME/f"{stem}.webp"
```

## File: sprites/process_final_sprites.py
```python
#!/usr/bin/env python3
"""Technically finalize authored/generated Zero -> Empire sprite candidates.

Input: art/incoming/final-sprites/*.png
Output: app/src/main/res/drawable-nodpi/<same-stem>.webp

Single-sprite candidates are normalized onto a square runtime canvas. Small FX
sprite sheets use their manifest-native 4x2 / 512x256 layout and are validated
cell-by-cell instead of being mistaken for a contact sheet.

Set SPRITE_TARGET or SPRITE_TARGETS to process only newly produced assets. This
prevents every batch from re-validating and re-encoding the full accumulated
catalog.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
INCOMING = ROOT / "art/incoming/final-sprites"
OUT = ROOT / "app/src/main/res/drawable-nodpi"
MIN_DIM = 512
MAX_DIM = 2048
MIN_PADDING_RATIO = 0.04
TARGET_PADDING_RATIO = 0.08
ALPHA_CLEAN_THRESHOLD = 8
MAX_ALPHA_COVERAGE = 0.70
MAX_MAJOR_COMPONENTS = 1
COARSE_SIZE = 128
FX_SHEET_RE = re.compile(r"^zte_fx_(?:0[0-9]|1[0-7])_final$")
CHR_SHEET_RE = re.compile(r"^zte_chr_(?:op|tech|log|eng)_(idle|walk|work|carry|repair|celeb)_final$")
FX_SHEET_SIZE = (512, 256)
FX_CELL = 128
FX_FRAMES = 8
FX_PADDING = 4
CHR_SHEET_SIZE = (1024, 1024)
CHR_CELL = 256
CHR_COLS = 4
CHR_ROWS = 4
CHR_PADDING = 8
CHR_EXPECTED_FRAMES = {
CHR_MIN_CELL_COVERAGE = 0.10
CHR_MAX_CELL_COVERAGE = 0.48
⋮----
def fail(msg: str) -> None
⋮----
def alpha_coverage(alpha: Image.Image) -> float
⋮----
hist = alpha.histogram()
visible = sum(hist[ALPHA_CLEAN_THRESHOLD:])
⋮----
def major_components(alpha: Image.Image) -> int
⋮----
"""Count large disconnected visible regions on a coarse alpha mask."""
small = alpha.resize((COARSE_SIZE, COARSE_SIZE), Image.Resampling.BILINEAR)
px = small.load()
seen = set()
major = 0
min_area = int(COARSE_SIZE * COARSE_SIZE * 0.012)
⋮----
q = deque([(x, y)])
⋮----
area = 0
⋮----
def clean_alpha(im: Image.Image) -> Image.Image
⋮----
rgba = im.convert("RGBA")
alpha = rgba.getchannel("A")
alpha = alpha.point(lambda a: 0 if a < ALPHA_CLEAN_THRESHOLD else a)
⋮----
def validate_fx_sheet(path: Path, im: Image.Image) -> None
⋮----
alpha = im.getchannel("A")
⋮----
x0 = (i % 4) * FX_CELL
y0 = (i // 4) * FX_CELL
cell_a = alpha.crop((x0, y0, x0 + FX_CELL, y0 + FX_CELL))
⋮----
edges = (
⋮----
out = OUT / f"{path.stem}.webp"
⋮----
size_kib = out.stat().st_size / 1024.0
⋮----
def validate_character_sheet(path: Path, im: Image.Image, action: str) -> None
⋮----
expected = CHR_EXPECTED_FRAMES[action]
⋮----
active = 0
⋮----
x0 = (i % CHR_COLS) * CHR_CELL
y0 = (i // CHR_COLS) * CHR_CELL
cell_a = alpha.crop((x0, y0, x0 + CHR_CELL, y0 + CHR_CELL))
bbox = cell_a.getbbox()
⋮----
hist = cell_a.histogram()
visible = sum(hist[ALPHA_CLEAN_THRESHOLD:]) / float(CHR_CELL * CHR_CELL)
⋮----
def process_single_sprite(path: Path, im: Image.Image) -> None
⋮----
coverage = alpha_coverage(alpha)
⋮----
components = major_components(alpha)
⋮----
bbox = alpha.getbbox()
⋮----
required_x = max(8, int(w * MIN_PADDING_RATIO))
required_y = max(8, int(h * MIN_PADDING_RATIO))
⋮----
subject = im.crop(bbox)
⋮----
subject_max = max(sw, sh)
target_pad = max(32, int(subject_max * TARGET_PADDING_RATIO))
canvas_side = min(MAX_DIM, max(MIN_DIM, subject_max + 2 * target_pad))
max_subject = int(canvas_side * 0.84)
⋮----
scale = max_subject / max(sw, sh)
subject = subject.resize((max(1, round(sw * scale)), max(1, round(sh * scale))), Image.Resampling.LANCZOS)
⋮----
canvas = Image.new("RGBA", (canvas_side, canvas_side), (0, 0, 0, 0))
x = (canvas_side - sw) // 2
bottom_pad = max(24, int(canvas_side * TARGET_PADDING_RATIO))
y = max(0, canvas_side - bottom_pad - sh)
⋮----
out_alpha = canvas.getchannel("A")
⋮----
def process(path: Path) -> None
⋮----
im = clean_alpha(Image.open(path))
⋮----
chr_match = CHR_SHEET_RE.fullmatch(path.stem)
⋮----
def requested_stems() -> set[str]
⋮----
raw = os.getenv("SPRITE_TARGETS") or os.getenv("SPRITE_TARGET") or ""
⋮----
stems: set[str] = set()
⋮----
target = target.strip().upper()
⋮----
m = re.fullmatch(r"FX-(\d{2})", target)
⋮----
m = re.fullmatch(r"BLD-(\d{2})-T(\d)", target)
⋮----
def main() -> None
⋮----
files = sorted(INCOMING.glob("*.png")) if INCOMING.exists() else []
wanted = requested_stems()
⋮----
by_stem = {p.stem: p for p in files}
missing = wanted - by_stem.keys()
⋮----
files = [by_stem[stem] for stem in sorted(wanted)]
```

## File: sprites/promote_ter07_v3.py
```python
#!/usr/bin/env python3
"""Promote the explicitly reviewed TER-07 v3 candidate to Android runtime.

This script is intentionally single-purpose. It refuses to generate art and only
converts the already reviewed candidate to the canonical lossless WebP target.
"""
⋮----
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'art/production/ter07/zte_terrain_07_candidate_v3.png'
REPORT=ROOT/'art/production/ter07/report.json'
TARGET=ROOT/'app/src/main/res/drawable-nodpi/zte_terrain_07_final.webp'
SIDE=1024
⋮----
def sha256(path:Path)->str
⋮----
h=hashlib.sha256()
⋮----
def validate(im:Image.Image)
⋮----
a=im.getchannel('A')
bbox=a.getbbox()
⋮----
coverage=sum(a.histogram()[8:])/(SIDE*SIDE)
margin=min(bbox[0],bbox[1],SIDE-bbox[2],SIDE-bbox[3])
w=bbox[2]-bbox[0];h=bbox[3]-bbox[1]
aspect=max(w,h)/max(1,min(w,h))
⋮----
def main()
⋮----
report=json.loads(REPORT.read_text(encoding='utf-8'))
⋮----
im=Image.open(SOURCE).convert('RGBA')
metrics=validate(im)
⋮----
runtime=runtime.convert('RGBA')
runtime_metrics=validate(runtime)
⋮----
evidence={
out=ROOT/'art/production/ter07/runtime-promotion-v3.json'
```

## File: sprites/reconcile_strict_approvals.py
```python
#!/usr/bin/env python3
"""Restore explicit historical strict-DONE approvals after queue reconstruction.

The autofactory rebuilds the master queue from a conservative unresolved set. This
module reapplies only approvals backed by explicit review/promotion history and a
runtime file that still exists. It does not approve new generated candidates.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
MASTER = ROOT / "art/production/master-asset-queue.json"
⋮----
APPROVED_BUILDING_COMMITS = {
⋮----
def runtime_for(asset: dict) -> Path | None
⋮----
aid = asset["id"]
⋮----
preferred = ROOT / f"app/src/main/res/drawable-nodpi/zte_business_08_t{tier}_final.png"
⋮----
configured = ROOT / asset["runtime"]
⋮----
def main() -> int
⋮----
queue = json.loads(MASTER.read_text(encoding="utf-8"))
by_id = {a["id"]: a for a in queue["assets"]}
restored: list[str] = []
⋮----
expected = [f"{family}-T{i}" for i in range(7)]
missing = [aid for aid in expected if aid not in by_id]
⋮----
asset = by_id[aid]
runtime = runtime_for(asset)
⋮----
strict_done = sum(a.get("strict_status") == "DONE" for a in queue["assets"])
```

## File: sprites/render_chatgpt_originals.py
```python
#!/usr/bin/env python3
"""Original role-consistent 2.5D character sprite atlases, authored in ChatGPT.

All art is generated locally, with one fixed vector rig and no network model calls.
The output is review-only and NEVER grants strict DONE. Frames: 256x256,
4-column RGBA atlas: 1024x1024, no ground shadow. Role IDLE can accompany
unresolved sibling actions as a continuity anchor without replacing strict DONE.
"""
⋮----
FRAME=256
ACTIONS={'IDLE':6,'WALK':8,'WORK':10,'CARRY':8,'REPAIR':10,'CELEB':8}
ROLES={
⋮----
# A physical repair socket is fixed in world/frame space, rather than glued to
# the wrist. Invert the same rigid endpoint transform used by action_fx so the
# engineered tool contacts the actual bolt throughout its ratcheting cycle.
ENG_REPAIR_TARGET=(218.0,129.0)
⋮----
def engineer_repair_wrist(phase:float)->tuple[float,float]
⋮----
theta=math.radians(tool_angle('REPAIR',phase,role='ENG'))
rotated_x=dx*math.cos(theta)-dy*math.sin(theta)
rotated_y=dx*math.sin(theta)+dy*math.cos(theta)
⋮----
def engineer_work_wrist(phase:float,bounce:float)->tuple[float,float]
⋮----
# Separate wide diagnostic scan sweep. The held tablet, right hand and
# illuminated sensor share exactly one trajectory, not three approximations.
⋮----
# SVG drawn in painter's order: back arm and legs -> torso -> head -> front hands.
def svg_frame(role:str, action:str, index:int, count:int)->str
⋮----
p=ROLES[role]; phase=2*math.pi*index/count; motion=math.sin(phase); bounce=0.0
⋮----
bounce=2.8*(1-math.cos(phase*2))/2
elif action=='IDLE':bounce=1.8*math.sin(phase)
⋮----
bounce=3.6*math.sin(phase)
⋮----
# Torque transfers through the knees and shoulders while BOTH boots stay
# planted. The socket/tool remain locked to world space, not to this bob.
bounce=5.1*math.sin(phase)
else:bounce=1.6*math.sin(phase)
# Always keep same facial shape, helmet model, costume palette and 3/4 view.
s=[]
def add(v):s.append(v)
def line(x1,y1,x2,y2,color,width,outline=3)
def hand(x,y)
def joint_arm(side, pose)
⋮----
# x shoulder, elbow, hand; design ergonomic positions for each action.
shoulder=(95 if side=='L' else 154,106+bounce)
⋮----
lift=(1-math.cos(phase))/2
handpos=((75-4*lift,140-109*lift+bounce) if side=='L' else (174+5*lift,140-109*lift+bounce))
elbow=((76,126-53*lift+bounce) if side=='L' else (171,126-53*lift+bounce))
⋮----
handpos=((89,132+bounce) if side=='L' else (166,132+bounce))
elbow=((78,125+bounce) if side=='L' else (172,122+bounce))
⋮----
# One slow, physically connected tool cycle. Earlier 22px reach/24px
# vertical pumping made the tool look like it floated and clipped the face.
reach=math.sin(phase); pump=math.cos(phase)
# WORK: broad horizontal fabrication stroke. REPAIR: compact diagonal
# inspection/twist. Both use exactly the same wrist coordinates as the
# physical tool and attached light below; no disconnected props.
reach_px=15 if pose=='WORK' else 8
pump_px=12 if pose=='WORK' else 7
handpos=((80+2*reach,146-3*pump+bounce) if side=='L'
elbow=((82,132+bounce) if side=='L'
⋮----
handpos=engineer_work_wrist(phase,bounce)
elbow=(165+11*math.sin(phase-.18),115+7*math.cos(phase-.18)+.30*bounce)
⋮----
handpos=engineer_repair_wrist(phase)
# Braced elbow drives the ratchet against a world-fixed socket instead
# of letting the entire character remain static during the torque cycle.
elbow=(167+9.5*math.sin(phase-.35),
⋮----
swing=motion*(-1 if side=='L' else 1)
⋮----
# A visibly reciprocal arm drive balances the stronger planted-foot
# engineer gait; it remains distinct from tool/carry arm poses.
opposite=math.cos(phase+.45)
handpos=((84-12*opposite,147+14*opposite+bounce) if side=='L'
elbow=((83-6*opposite,124+7*opposite+bounce) if side=='L'
⋮----
# Reciprocal opposing arm motion: front arm rises as opposite boot leads.
# Earlier both wrists bobbed in the same vertical direction.
opposite=math.cos(phase)
handpos=((84-10*opposite,147+11*opposite+bounce) if side=='L'
elbow=((83-5*opposite,124+5*opposite+bounce) if side=='L'
⋮----
handpos=((84+8*swing,147+10*swing+bounce) if side=='L' else (170+8*swing,148-10*swing+bounce))
elbow=((83+4*swing,124+5*swing+bounce) if side=='L' else (171+4*swing,127-5*swing+bounce))
⋮----
elbow=((81,129+bounce) if side=='L' else (170,126+bounce))
handpos=((79,149+bounce) if side=='L' else (176,144+bounce))
⋮----
sleeve=line(shoulder_x,shoulder_y,ex,ey,'url(#jacket)',17,3)
⋮----
# highlighted overarm and stitched safety cuff
⋮----
# Locally authored planted-foot gait: 60% support, 40% lifted
# recovery, damped 3/4-view two-bone knees, and reciprocal L/R steps.
# Grounded ankles keep exactly the same Y even as pelvis bob changes.
leg_poses=[]
⋮----
leg=foot_pose(phase,side,action,bounce,profile=('op-walk' if role=='OP' and action=='WALK' else
⋮----
boot_angle=leg.boot_angle
⋮----
hipx=106 if side=='L' else 146
yhip=155+bounce
knee_x=hipx+(2 if side=='L' else -2)
knee_y=190+(.48*bounce if role=='ENG' and action in ('WORK','REPAIR') else bounce)
ankle_x=hipx
ankle_y=(226 if role=='ENG' and action in ('WORK','REPAIR') else 226+bounce)
boot_angle=0.0
⋮----
# no floor shadow; transparency is exact outside figure
# back ponytail / hair only LOG
⋮----
# Engineer-only free-standing diagnostics column. It has a fixed ground
# support, a real repairable fastener, and stays independent of torso bounce.
# The wrist/tool/VFX endpoint locks to the highlighted fastener below.
⋮----
# Readable bolted service hatch and warning strip at phone scale.
⋮----
# boots and 2 articulated segments per leg
⋮----
# Real editable ankle/boot contact telemetry; no automatic art approval.
gait_profile='op-walk' if role=='OP' else 'eng-walk'
gait_attr='data-op-walk-foot' if role=='OP' else 'data-eng-walk-foot'
foot=foot_pose(phase,side,action,bounce,profile=gait_profile)
⋮----
# knee armor pad and seam
⋮----
if side=='L': toe=ax-9
else:toe=ax+9
# Heel-strike and toe-off flex the same boot art around its ankle.
⋮----
add('</g>')  # close the per-leg pose-evidence group
⋮----
add('</g>')  # close world-planted repair boot evidence group
⋮----
add('</g>')  # close world-planted diagnostic work boots
# Weight shifts toward stance foot; cargo carry sway remains restrained.
# The hands, equipment, torso, helmet and face all receive the exact same
# transform, avoiding drift in object contact or character identity.
repair_body_evidence=(f' data-eng-repair-body-bounce="{bounce:.2f}"'
⋮----
# BACK arm
⋮----
# main torso, premium tapered silhouette, safety accents
⋮----
# Original workwear material pass: cropped shoulder armor, woven fabric,
# laminated vest segments and two retention fasteners. All follow the same
# torso/bounce transform and remain invariant across the six actions.
⋮----
dx=0 if side=='L' else 59
⋮----
# A subtle chest-harness fits inside the jacket; it is neither a text logo
# nor a detached floating decoration and stays attached while the arms move.
⋮----
# belt buckles and pockets
⋮----
# neck + head, same exact proportions across all actions
⋮----
# ear, cheek and neck shading
⋮----
# OP goggles conceal the eyelids, so an IDLE blink is expressed by a
# brief lens reflection shift, never by a floating eye outside the visor.
# Lens geometry remains identical across all other action families.
lens_shift=(1.5 if action=='IDLE' and index in (2,3) else 0.0)
⋮----
# A blink must replace the open eyes, not paint a horizontal stroke over
# still-visible pupils. This is an actual facial expression transition.
⋮----
# unique helmet per role (seams, raised ridge and front peak)
⋮----
# ACTION EQUIPMENT. All objects are authored here as editable SVG
# geometry, with invariant shape within each animation and hand contact.
⋮----
by=121+bounce
⋮----
# A bolted cast-metal ore bin (not a generic cardboard package).
⋮----
# Warehouse parcel with tape and readable strapped corners.
⋮----
# Engineer's sealed field-instrument case, cyan latch lights.
⋮----
# Two hand grips overlap the left/right handle in every phase.
⋮----
# The exact same right-hand joint drives the held equipment. One cycle
# and stable local geometry prevent fake floating tools and prop morphing.
tool_x=176+(15 if action=='WORK' else 8)*math.sin(phase)
tool_y=123+(12 if action=='WORK' else 7)*math.cos(phase)+bounce
⋮----
repair_marker=' data-repair-tool="ENG"' if role=='ENG' and action=='REPAIR' else ''
work_marker=' data-work-tool="ENG"' if role=='ENG' and action=='WORK' else ''
⋮----
# Physical articulated torque wrench, not an electronic scanner.
# Tip geometry is centred on the *exact* fixed socket offset (43,-13).
⋮----
# foreground right arm and hand over equipment, never floating
⋮----
# Physically attached local vector action lighting. Equipment highlights are
# driven by the very same right-wrist tool transform as the authored prop.
# No detached generated particles or external model are introduced.
# The rigid light must use the same wrist coordinates as the actual tool.
fx_tool_x=176+(15 if action=='WORK' else 8)*math.sin(phase)
fx_tool_y=123+(12 if action=='WORK' else 7)*math.cos(phase)+bounce
⋮----
# Both arms raised over ~half a cycle; no detached particle VFX.
⋮----
# reflective micro-detail texture, unique per role but invariant per frame
⋮----
add('</g>')  # balanced upper-body weight-transfer group
⋮----
def render_atlas(role,action,outdir,save_svgs=False)
⋮----
# Pure SVG pose/unit tests need no Cairo dependency; only pixel rendering does.
⋮----
count=ACTIONS[action]; atlas=Image.new('RGBA',(1024,1024),(0,0,0,0))
⋮----
svg=svg_frame(role,action,i,count)
png=cairosvg.svg2png(bytestring=svg.encode('utf8'),output_width=768,output_height=768)
rgba=Image.open(io.BytesIO(png)).convert('RGBA').resize((FRAME,FRAME),Image.Resampling.LANCZOS)
# Final material illumination is deterministic and preserves exact alpha;
# editable SVG geometry remains the authoritative rig/source for all frames.
rgba=finish_frame(rgba)
x=(i%4)*FRAME;y=(i//4)*FRAME;atlas.alpha_composite(rgba,(x,y))
⋮----
src=outdir/'src_svg'/role/action;src.mkdir(parents=True,exist_ok=True)
⋮----
name=f'zte_chr_{role.lower()}_{action.lower()}_final.png'
path=outdir/'candidates'/name;path.parent.mkdir(parents=True,exist_ok=True);atlas.save(path,optimize=True)
⋮----
def main()
⋮----
parser=argparse.ArgumentParser()
⋮----
args=parser.parse_args();outdir=pathlib.Path(args.output_dir);outdir.mkdir(parents=True,exist_ok=True)
results=[]
⋮----
report={'version':'chatgpt-original-character-rig-v13-engineer-diagnostic-sweep','strict_done_added':0,'review_only':True,
```

## File: sprites/render_original_character_previews.py
```python
#!/usr/bin/env python3
"""Android-friendly animated previews for original ChatGPT-authored sprites.

All evidence is review-only. This never reads or changes the canonical
235-row master queue or Android runtime assets, and never promotes PNGs.
"""
⋮----
FRAMES = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}
ROLES = ("OP", "LOG", "ENG")
DURATION_MS = {"IDLE": 185, "WALK": 105, "WORK": 125, "CARRY": 115,
⋮----
def frames_from_atlas(path: Path, count: int) -> list[Image.Image]
⋮----
result = [source.crop(((i % 4)*256, (i // 4)*256,
⋮----
def checker() -> Image.Image
⋮----
im = Image.new("RGB", (256, 256), "#b0b6c1")
d = ImageDraw.Draw(im)
⋮----
def compose(frame: Image.Image, backdrop: Image.Image) -> Image.Image
⋮----
cell = backdrop.copy()
⋮----
def fingerprint(frame: Image.Image) -> str
⋮----
def change_ratio(a: Image.Image, b: Image.Image) -> float
⋮----
# RGB plus silhouette activity, computed over the occupied image region
# to distinguish a blink from identical idle frames.
aa = a.resize((64, 64), Image.Resampling.BILINEAR).convert("RGBA")
bb = b.resize((64, 64), Image.Resampling.BILINEAR).convert("RGBA")
⋮----
activity = 0
count = 0
⋮----
def produce(source: Path) -> dict
⋮----
manifest = json.loads((source/"creation-manifest.json").read_text(encoding="utf8"))
expected = {f"CHR-{role}-{action}" for role in ROLES for action in FRAMES}
⋮----
preview = source/"previews"
⋮----
atlas = Image.new("RGB", (6*190, 3*223), "#202732")
draw = ImageDraw.Draw(atlas)
background = checker()
# Portrait boards remain legible on 320dp Android phones. The actual
# rendered figure stays 42/39 pixels, matching city-stage gameplay scale.
# These are review references, never automated approval decisions.
mobile_boards = {
analysis = []
⋮----
asset_id = f"CHR-{role}-{action}"
filename = f"zte_chr_{role.lower()}_{action.lower()}_final.png"
cells = frames_from_atlas(source/"candidates"/filename, FRAMES[action])
distinct = len({fingerprint(f) for f in cells})
⋮----
# WALK/CARRY need eight physically different stride phases, not
# a repeated sinusoidal snapshot with fake foot movement.
⋮----
rendered = [compose(f, background) for f in cells]
board = mobile_boards[role]
marker = ImageDraw.Draw(board)
top = col * 132
⋮----
tiny = cells[0].resize((side, side), Image.Resampling.LANCZOS)
⋮----
gif_path = preview/f"{role.lower()}-{action.lower()}.gif"
⋮----
small = rendered[0].resize((186, 186), Image.Resampling.LANCZOS)
pos = (col*190+2, row*223+30)
⋮----
all_frames = cells[1:] + cells[:1]
ratios = [change_ratio(a, b) for a, b in zip(cells, all_frames)]
# A smooth animation needs an equally smooth last-to-first loop.
# Previously only distinct hashes were checked: a sudden reset
# could still pass every geometry and motion test.
internal_median = statistics.median(ratios[:-1])
seam = ratios[-1]
seam_ratio = round(seam / max(internal_median, .0001), 4)
abrupt_loop_reset = seam > .045 and seam_ratio > 1.9
boxes = [f.getchannel("A").getbbox() for f in cells]
min_margin = min(min(x, y, 256-x2, 256-y2)
⋮----
result = {
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
result = produce(args.output_dir)
```

## File: sprites/repair_shadowed_character_atlas.py
```python
#!/usr/bin/env python3
"""Repair AI-generated neutral ground shadows in an already collected atlas.

Produces an independent review-only candidate and a provenance JSON report.
Does not touch canonical runtime assets, queues, or strict DONE status.
"""
⋮----
ACTION_FRAMES = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}
CHARACTER_ID = re.compile(r"^CHR-(OP|TECH|LOG|ENG)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$")
⋮----
def digest(path: Path) -> str
⋮----
def main() -> None
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
match = CHARACTER_ID.fullmatch(args.asset_id)
⋮----
action = match.group(2)
expected = ACTION_FRAMES[action]
⋮----
source = image.convert("RGBA")
result = Image.new("RGBA", (1024, 1024))
details = []
⋮----
frame = source.crop((x, y, x + 256, y + 256))
⋮----
total = sum(item["removed_gray_pixels"] for item in details)
⋮----
evidence = {
```

## File: sprites/rigged_tech_actions_v3.py
```python
#!/usr/bin/env python3
"""Automated multi-action TECH sprite production with a single textured IK rig.

All outputs remain technical review candidates. This script cannot mark DONE.
No Kaggle, generative frame redraw, interaction, or remote model is required.
"""
⋮----
ACTIONS = ("WALK", "CARRY", "IDLE", "WORK", "REPAIR", "CELEB")
GROUND = core.GROUND
CANVAS = core.CANVAS
ROOT_X = core.ROOT_X
HIP_Y = core.HIP_Y
# Deliberate depth-lane offset for the FAR boot in review-only moving cycles.
# 22 source pixels project to ~1.8px at a 42dp sprite, reducing total
# occlusion at crossover without changing stance velocity or Y grounding.
# Static actions and the shipped legacy WALK renderer are untouched.
FAR_FOOT_LANE_PX = 22.0
# The back foot belongs to a deeper 2.5D ground lane, projected 14 source
# pixels higher than the near lane. The offset is CONSTANT through the
# entire footstep cycle: it cannot induce an extra foot slide. This is
# a review-only camera-space projection, not a raised/hovering shoe.
FAR_FOOT_DEPTH_Y_PX = 14.0
⋮----
# Reversible, REVIEW-ONLY material lift for the dark graphite uniform.
# Pixels at 39-42dp lose most of their shadow detail in the night city.
# Gamma 0.76 restores midtone separation while keeping pure black/white,
# all alpha, joint geometry, props and the original skin file unchanged.
TECH_REVIEW_MATERIAL_GAMMA = 0.76
⋮----
def grade_review_kit(kit: dict[str, Image.Image]) -> dict[str, Image.Image]
⋮----
"""Create lifted review textures without ever mutating the source atlas."""
gamma = TECH_REVIEW_MATERIAL_GAMMA
⋮----
lut = [round(255 * ((i / 255) ** gamma)) for i in range(256)]
result = {}
far_lower_leg = {
# A second, subtler material pass establishes depth without changing
# either leg's pose, ground contact, silhouette or source texture alpha.
# Only the FAR lower limb receives a cooler steel-blue bounce light.
# This is deliberately a diffuse material shift, NOT neon footwear:
# it should be judged at 39-42dp against the ungraded near leg.
far_red = [max(0, min(255, round(i * 0.82))) for i in range(256)]
far_green = [max(0, min(255, round(i * 0.94 + 5))) for i in range(256)]
far_blue = [max(0, min(255, round(i * 1.07 + 13))) for i in range(256)]
⋮----
def spine_lean(t: float, action: str) -> float
⋮----
"""Cyclic, phase-coupled spine bend in radians. Foot/hip world anchors
    are not modified, so contact geometry stays deterministic and reversible.
    """
phase = 2 * math.pi * (t % 1.0)
⋮----
def pose_for(t: float, action: str) -> dict
⋮----
phase = 2 * math.pi * t
⋮----
p = transfer_pose(core.pose(t),t,action)
# Preserve footstep phases and stance-lock flags while projecting
# the FAR foot into a slightly deeper 2.5D ground lane. Both X/Y
# offsets stay constant over the cycle, so the foot remains planted
# relative to its own lane. Re-solving knee IK connects the actual
# thigh/calf to the displaced ankle instead of floating a boot image.
⋮----
hands = {
⋮----
def draw_cargo(layer: Image.Image, p: dict, t: float) -> None
⋮----
"""A readable industrial crate physically supported by both wrists.

    Review-only enlargement for real 39–42dp Android sprites. Repositioning
    the shell MUST NOT move either wrist: handle centers are exact, invariant
    rig coordinates. The same solid crate remains attached across all frames.
    """
⋮----
d = ImageDraw.Draw(layer, "RGBA")
# Larger luggage-sized load instead of a tiny tablet-sized block.
# Its warm material and angled lid distinguish CARRY from WORK/REPAIR.
⋮----
# Vertical ribs preserve a physical cargo silhouette at 96px.
⋮----
# Hardware latch: small neutral/metal feature, not an electronic screen.
⋮----
# x=root+10 and y=root-95 imply wrist anchors x+19/y+40 and
# x+93/y+40, exactly pose_for(CARRY)'s two fixed handle centers.
⋮----
def draw_console(layer: Image.Image, p: dict, t: float) -> None
⋮----
h = 8 + round(7 * (.5 + .5 * math.sin(2 * math.pi * t + n)))
⋮----
def draw_work_touch(layer: Image.Image, p: dict, t: float) -> None
⋮----
"""Readable front-layer contacts always anchored to both gloves."""
⋮----
pulse = work_pulse(t)
⋮----
alpha=round((125 if index==0 else 160)*pulse)
⋮----
def draw_repair(layer: Image.Image, p: dict, t: float) -> None
⋮----
xx = x + 12 + n * 10
⋮----
# REPAIR is physically a welding/maintenance station, not another
# cyan telemetry console like WORK. Warm industrial seam light makes
# the action distinguishable even when shrunk to the 96px QA thumbnail.
⋮----
tip = tuple(round(v) for v in repair_tip(p["root"]))
# Keep the welding torch physically attached to the animated wrist.
hand = (round(p["handR"][0]), round(p["handR"][1]))
⋮----
def draw_repair_sparks(layer: Image.Image, p: dict, t: float) -> None
⋮----
"""Weld at the actual contact seam, with an unmistakable warm arc.

    WORK keeps blue data-interface feedback while REPAIR emits a pulsed,
    warm metalworking arc and short-lived sparks. All particles are tied
    deterministically to the SAME torch tip (no floating secondary prop).
    The seam position, rig, costume and collision contacts are unchanged.
    """
⋮----
tip = (x, y)
⋮----
intensity = repair_spark_intensity(t)
⋮----
angle = 2 * math.pi * n / 11 + 0.15 * math.sin(phase)
radius = (9 + 23 * intensity) * (0.70 + ((n * 7) % 6) / 9)
px = round(x + math.cos(angle) * radius)
py = round(y + math.sin(angle) * radius)
tone = (255, 236, 161) if n % 3 == 0 else (255, 166, 62)
alpha = round((230 if n % 3 == 0 else 195) * intensity)
⋮----
def draw_celebration(layer: Image.Image, p: dict, t: float) -> None
⋮----
"""Both raised wrists emit restrained identity-locked tech celebration VFX.

    Every mote is derived from a hand anchor and cyclic phase (never random),
    so particles cannot drift off the rig or create frame 24→1 discontinuity.
    """
d=ImageDraw.Draw(layer,"RGBA")
phase=2*math.pi*(t % 1.0)
⋮----
# A bright readable wrist ring, suitable for 96px game previews.
ring=9+2*math.sin(phase+side*math.pi)
⋮----
a=2*math.pi*(n/9 + (t % 1.0)*(.35 if side==0 else -.3))
radius=23+8*math.sin(phase+n*.7+side)
px=round(x+math.cos(a)*radius)
py=round(y+math.sin(a)*radius-3)
alpha=round(150+65*(.5+.5*math.sin(2*a+phase)))
color=(78,219,249,alpha) if (n+side)%3 else (252,198,110,alpha)
⋮----
def draw_idle_readout(layer: Image.Image, p: dict, t: float) -> None
⋮----
energy = .5 + .5 * math.sin(2 * math.pi * t)
⋮----
def draw_frame(action: str, t: float, kit: dict)
⋮----
p = pose_for(t, action)
under = {
overlay = {"CELEB":draw_celebration,"WORK":draw_work_touch,
⋮----
def action_qa(action: str, poses: list, base_qa: dict) -> dict
⋮----
violations = []
⋮----
a = float(p.get("torso_lean_rad", 0.0))
⋮----
def rotated_shoulder(dx, dy)
shoulders = {"handL": rotated_shoulder(-24, -86),
⋮----
distance = math.dist(shoulder, p[hand])
⋮----
motion = {
work_bad = [i for i,p in enumerate(poses)
repair_lengths = [repair_contact(p)["torch_length_px"] for p in poses
tool_bad = [i for i,p in enumerate(poses) if action=="REPAIR"
interaction_ok = not work_bad and not tool_bad
support_bad=[]
⋮----
mount=mount_geometry(action,p["root"])
⋮----
support_ok=not support_bad
stationary = action in ("IDLE", "WORK", "REPAIR", "CELEB")
grounded = all(q["lockL"] and q["lockR"] for q in poses) if stationary else True
grip_ok = (all(
raised_arm_heights=[]
⋮----
a=p.get("torso_lean_rad",0.)
⋮----
shoulders=((x-24*ca+86*sa,y-24*sa-86*ca),
⋮----
raised_arm_pass=(min(raised_arm_heights)>=65 if raised_arm_heights else True)
arm_spans=[p["handR"][0]-p["handL"][0] for p in poses] if action=="CELEB" else []
wide_arms_pass=(min(arm_spans)>=135 if arm_spans else True)
legible_motion = (action not in ("WORK", "REPAIR", "CELEB")
supports = [p.get("support_bias") for p in poses]
amplitude = max(abs(p.get("weight_transfer_px",0)) for p in poses)
transfer_ok = (all(v is not None and math.isfinite(v) and abs(v)<=1.00001
kinetic = (not violations and grounded and grip_ok and legible_motion and
⋮----
def build_action(skin: Path, out: Path, action: str, frames: int = 24, fps: int = 12)
⋮----
kit = grade_review_kit(core.load_kit(skin))
⋮----
asset_id = f"CHR-TECH-{action}"
# Rotate WORK's loop start to a low-motion seam, without interpolating,
# dropping or duplicating frames. All action overlays use the same phase.
phase_origin_frame = round(frames * (5/24)) if action == "WORK" else 0
⋮----
phase = ((i + phase_origin_frame) % frames) / frames
⋮----
cols = 6
rows = math.ceil(frames / cols)
atlas = Image.new("RGBA", (CANVAS * cols, CANVAS * rows))
sheet = Image.new("RGB", (192 * cols, 192 * rows), (27, 34, 45))
game_sheet = Image.new("RGB", (96 * cols, 96 * rows), (27, 34, 45))
thumbs = []
⋮----
bg = Image.new("RGBA", (CANVAS, CANVAS), (26, 34, 45, 255))
⋮----
preview = bg.convert("RGB")
thumb = preview.resize((192, 192), Image.Resampling.LANCZOS)
⋮----
qa = action_qa(action, poses, core.check(images, poses, boots))
footfalls = action in ("WALK", "CARRY")
work_indices = work_event_indices(frames, phase_origin_frame) if action == 'WORK' else ()
events = [{
manifest = {
⋮----
# Shared runtime-pack contract; preserve legacy filename for existing consumers.
⋮----
bundle = out.parent / f"{asset_id}-modular-v3-review.zip"
⋮----
def main()
⋮----
parser = argparse.ArgumentParser(description=__doc__)
⋮----
args = parser.parse_args()
actions = ACTIONS if args.all else (args.action,)
summaries = []
⋮----
out = args.output / action if args.all else args.output
⋮----
index = {
```

## File: sprites/rigged_tech_walk_v2.py
```python
#!/usr/bin/env python3
"""Produce a single-identity, modular-textured animated TECH walk, with joint caps.

Self-contained apart from a packed RGBA skin atlas and Pillow/numpy. Never writes
master queues or strict DONE. Uses deterministic foot trajectories and two-bone IK.
"""
⋮----
PART_NAMES = ('head', 'torso', 'pelvis', 'backpack', 'upper_arm_far',
⋮----
def foot_local(t: float)
⋮----
u = (t-STANCE)/(1-STANCE)
slope = -STRIDE/STANCE*(1-STANCE)
# Hermite recovers stance velocity at both ends of swing.
⋮----
def foot_roll(t: float) -> float
⋮----
u=t/STANCE
⋮----
u=(t-STANCE)/(1-STANCE)
⋮----
def pose(t: float) -> dict[str,Any]
⋮----
root=(ROOT_X,HIP_Y+3.5*math.cos(4*math.pi*t))
⋮----
swing=30*math.cos(2*math.pi*t)
⋮----
def ik(a,b,l1,l2,sign=1)
⋮----
length=math.hypot(dx,dy) or 1.e-5
d=max(abs(l1-l2)+.001,min(l1+l2-.001,length))
⋮----
along=(l1*l1-l2*l2+d*d)/(2*d)
h=math.sqrt(max(0,l1*l1-along*along))
⋮----
def load_kit(atlas:Path) -> dict[str,Image.Image]
⋮----
rgba=image.convert('RGBA')
kit={}
⋮----
tile=rgba.crop(((i%4)*256,(i//4)*256,(i%4+1)*256,(i//4+1)*256))
bbox=tile.getchannel('A').getbbox()
⋮----
image=kit[name]
cut=round(image.height*.72)
⋮----
def paste(layer,img,x,y)
⋮----
def rotated_limb(layer,img,a,b,occupancy=.87,width_mul=1)
⋮----
"""Warp proximal-to-distal textured rigid piece around an exact IK bone."""
dist=math.dist(a,b)
height=max(1,round(dist/occupancy))
width=max(1,round(height*img.width/img.height*width_mul))
sprite=img.resize((width,height),Image.Resampling.LANCZOS)
# generous rotation canvas prevents cut-offs for all joint orientations
side=max(184,round(height*3.5))
center=side//2
stage=Image.new('RGBA',(side,side))
⋮----
angle=90-math.degrees(math.atan2(b[1]-a[1],b[0]-a[0]))
stage=stage.rotate(angle,resample=Image.Resampling.BICUBIC)
⋮----
def fabric_hinge(layer, start, hinge, end, radius=12, near=True)
⋮----
"""Flexible cloth gusset behind the rigid knee/elbow cap.

    Each fold follows the exact IK bone vectors; no free-floating redraw.
    Kept optional to preserve the proven legacy WALK pixels.
    """
⋮----
d=math.hypot(tx,ty)
⋮----
cross=ux*vy-uy*vx
bend=math.acos(max(-1.,min(1.,ux*vx+uy*vy)))
scale=2;r=float(radius)
side=round((r*2.8+12)*scale)*2
local=Image.new('RGBA',(side,side))
draw=ImageDraw.Draw(local,'RGBA')
cx=cy=side//2
def xy(x,y):return (round(cx+x*scale),round(cy+y*scale))
cloth=(35,45,55,245) if near else (23,31,40,225)
⋮----
yy=(-.70+i*.53)*r;slope=cross*.30*r
⋮----
theta=math.degrees(math.atan2(ty,tx))-90
rotated=local.rotate(-theta,resample=Image.Resampling.BICUBIC)
rotated=rotated.resize((side//scale,side//scale),Image.Resampling.LANCZOS)
⋮----
def ankle_gaiter(layer,knee,ankle,near=True)
⋮----
"""Short boot/cloth overlap beneath the sole-aligned rigid shoe."""
⋮----
norm=math.hypot(dx,dy)
⋮----
x=ankle[0]-dx*19;y=ankle[1]-dy*19;r=9 if near else 8
pts=[(x+dy*r,y-dx*r),(x-dy*r,y+dx*r),
draw=ImageDraw.Draw(layer,'RGBA')
⋮----
a=(x-dx*12+dy*r*.75,y-dy*12-dx*r*.75)
b=(x-dx*12-dy*r*.75,y-dy*12+dx*r*.75)
⋮----
def joint_cap(layer,p,r=14,depth='near')
⋮----
"""Soft metallic overlap at hinge hides segment gaps without redrawing identity."""
size=2*round(r+7)
⋮----
cx=cy=(size-1)/2
d=((xx-cx)/r)**2+((yy-cy)/(r*.79))**2
feather=np.clip((1-d)*12,0,1)
light=np.clip((cy-yy)/size+.3,0,1)
main=np.zeros((size,size,4),dtype='uint8')
tint=1.0 if depth=='near' else .8
⋮----
cap=Image.fromarray(main,'RGBA')
draw=ImageDraw.Draw(cap,'RGBA')
⋮----
def render_boot(layer,img,foot,angle,far_edge_light=False) -> dict[str,float]
⋮----
"""Place sole at demanded contact Y, instead of guessing boot ankle offset."""
width=69
height=round(width*img.height/img.width)
shoe=img.resize((width,height),Image.Resampling.LANCZOS)
pivot=(round(width*.26),round(height*.30))
side=max(160,round(max(width,height)*2.5))
base=Image.new('RGBA',(side,side))
⋮----
turn=base.rotate(-math.degrees(angle),resample=Image.Resampling.BICUBIC)
bbox=turn.getchannel('A').getbbox()
⋮----
# Anchor visually consistent ankle X while sole follows the foot path.
px=round(foot[0]-center)
py=round(foot[1]-bbox[3])
⋮----
# Review-only far-side boot material edge at 39-42dp. A 6 source-pixel
# exterior rim becomes ~0.5 physical pixels at game scale.
# The shoe texture and sole contact remain exact and unchanged.
# The brighter material edge is beneath the shoe, so it never paints
# over its lace/metal texture or adds a second floating foot.
alpha = turn.getchannel('A')
exterior = ImageChops.subtract(
exterior = exterior.point(lambda value: round(value * 0.34))
edge = Image.new('RGBA', turn.size, (126, 151, 159, 0))
⋮----
def draw_frame(t:float,kit:dict,pose_override=None,prop_underlay=None,prop_overlay=None,joint_fabric=False,soft_deform=False,far_boot_edge_light=False)
⋮----
p=pose(t) if pose_override is None else pose_override
⋮----
canvas=Image.new('RGBA',(CANVAS,CANVAS))
⋮----
kneeL=ik(lhip,p['left'],94,99,1)
kneeR=ik(rhip,p['right'],94,99,1)
# Small, deterministic spine flexion rotates all upper-body parts around
# one hip pivot while planted feet stay fixed in world space.
lean=float(p.get('torso_lean_rad',0.0))
⋮----
def spine(dx,dy):return (x+dx*cos_a-dy*sin_a,y+dx*sin_a+dy*cos_a)
def torso_piece(sprite,size,local_center,rotate=True)
⋮----
img=sprite.resize(size,Image.Resampling.LANCZOS)
⋮----
img=img.rotate(-math.degrees(lean),expand=True,resample=Image.Resampling.BICUBIC)
⋮----
elbowL=ik(shoulderL,p['handL'],59,59,-1)
elbowR=ik(shoulderR,p['handR'],59,59,-1)
# Warp the SAME cached atlas pieces along mildly curved limb strips.
# The optional path never modifies the rig and can be disabled for exact
# compatibility with the historical production renderer.
def segment(texture,a,b,occupancy,width_mul,bend)
bend_l=signed_joint_bend(lhip,kneeL,p['left'])
bend_r=signed_joint_bend(rhip,kneeR,p['right'])
bend_arm_l=signed_joint_bend(shoulderL,elbowL,p['handL'],3.4)
bend_arm_r=signed_joint_bend(shoulderR,elbowR,p['handR'],3.4)
⋮----
bootL=render_boot(canvas,kit['shin_boot_far_boot'],p['left'],p['rollL'],far_edge_light=far_boot_edge_light)
⋮----
bootR=render_boot(canvas,kit['shin_boot_near_boot'],p['right'],p['rollR'])
⋮----
# Counter-rotated head avoids unnatural nodding when the chest leans.
⋮----
def check(frames:list[Image.Image],poses:list[dict],boots:list[dict])
⋮----
arr=[np.array(f.getchannel('A'))>=128 for f in frames]
diff=[]
⋮----
b=arr[(i+1)%len(arr)]
union=np.count_nonzero(a|b)
⋮----
median=statistics.median(diff)
bounds=[f.getchannel('A').getbbox() for f in frames]
clip=[i for i,b in enumerate(bounds) if b is None or b[0]<6 or b[1]<6 or b[2]>CANVAS-6 or b[3]>CANVAS-6]
soles=[b[s]['sole_error_px'] for b in boots for s in ('left','right')]
penetration=[i for i,p in enumerate(poses) if p['left'][1]>GROUND+1e-5 or p['right'][1]>GROUND+1e-5]
ratio=diff[-1]/median if median else 999
pass_geometry=not clip and not penetration and max(soles)<=1.0 and .40<ratio<1.9
⋮----
def build(atlas:Path,out:Path,frames=24,fps=12)
⋮----
kit=load_kit(atlas)
⋮----
images=[]; poses=[]; boots=[]
⋮----
cols=6; rows=math.ceil(frames/cols)
atlas_img=Image.new('RGBA',(CANVAS*cols,CANVAS*rows))
thumbs=[]
⋮----
bg=Image.new('RGBA',(CANVAS,CANVAS),(26,34,45,255))
⋮----
contact=Image.new('RGB',(192*cols,192*rows),(27,34,45))
⋮----
qa=check(images,poses,boots)
events=[{'frame':i,'footstep':('right' if i==0 else 'left' if i==frames//2 else None),
manifest={'asset_id':'CHR-TECH-WALK','build':'modular-skin-v2-IK-joint-guards',
⋮----
bundle=out.parent/'CHR-TECH-WALK-modular-v2-review.zip'
⋮----
def main()
⋮----
parser=argparse.ArgumentParser(description=__doc__)
⋮----
args=parser.parse_args()
```

## File: sprites/soft_skin_deform.py
```python
"""Deterministic bend-aware texture deformation for 2D IK character limbs.

Inverse mapping of an atlas piece onto a mildly curved strip. No generative calls,
no identity drift and no changes to the rig's hard anatomical joint positions.
Requires Pillow and NumPy only.
"""
⋮----
def signed_joint_bend(start, hinge, end, maximum=5.0)
⋮----
"""Signed lateral offset in pixels, bounded by hinge deflection."""
⋮----
cross = (ux*vy - uy*vx) / (lu*lv)
⋮----
"""Draw atlas texture along a gently curved IK bone with bilinear sampling.

    The lateral bend is zero at both skeletal endpoints and largest mid-bone.
    Unlike a straight rigid sprite this curves *the original texture pixels*.
    No source image is changed and the path is deterministic.
    """
⋮----
dist=math.hypot(dx,dy)
⋮----
height=max(2,round(dist/occupancy))
width=max(2,round(height*texture.width/texture.height*width_mul))
scaled=np.asarray(texture.resize((width,height),Image.Resampling.LANCZOS),dtype=np.float32)/255.0
# Original rigid layout places top of the image 7% above joint A.
head=-.07*height
tail=.93*height
p0=(start[0]+ux*head,start[1]+uy*head)
p1=(start[0]+ux*tail,start[1]+uy*tail)
pad=width/2+abs(bend_px)+3
x0=max(0,math.floor(min(p0[0],p1[0])-pad));x1=min(layer.width,math.ceil(max(p0[0],p1[0])+pad))
y0=max(0,math.floor(min(p0[1],p1[1])-pad));y1=min(layer.height,math.ceil(max(p0[1],p1[1])+pad))
⋮----
along=xx*ux+yy*uy
side=xx*nx+yy*ny
t=along/dist
along_clipped=np.clip(t,0,1)
bulge=bend_px*np.sin(np.pi*along_clipped)
width_factor=1-taper*(2*along_clipped-1)**2
src_x=(side-bulge)/width_factor+(width-1)/2
src_y=along-head
valid=(src_x>=0)&(src_x<=width-1)&(src_y>=0)&(src_y<=height-1)
xi=np.clip(np.floor(src_x).astype(np.int32),0,width-1)
yi=np.clip(np.floor(src_y).astype(np.int32),0,height-1)
xj=np.minimum(xi+1,width-1)
yj=np.minimum(yi+1,height-1)
wx=np.clip(src_x-xi,0,1)[...,None]
wy=np.clip(src_y-yi,0,1)[...,None]
# Premultiplied-alpha bilinear filtering avoids dark seams/haloes.
rgba=scaled.copy()
⋮----
sampled=((1-wx)*(1-wy)*rgba[yi,xi]+wx*(1-wy)*rgba[yi,xj]
alpha=sampled[...,3:4]
rgb=np.divide(sampled[...,:3],np.maximum(alpha,1e-6))
sampled=np.concatenate((rgb,alpha),axis=-1)
⋮----
pixels=np.uint8(np.clip(np.round(sampled*255),0,255))
patch=Image.fromarray(pixels,'RGBA')
```

## File: sprites/tech_prop_mount.py
```python
"""Physical support brackets for TECH interaction props (512px rig coordinates).

WORK's console and REPAIR's service panel were visually floating. Both
now have deterministic folding mounts running from the technician's belt
to a socket *inside* the associated prop.

This is lightweight 2D staging, not a simulated rig or visual approval.
"""
⋮----
SUPPORTS = {
# Bounds of the static graphics as painted in rigged_tech_actions_v3.py.
PANEL_BOUNDS = {
⋮----
def mount_geometry(action: str, root: tuple[float,float]) -> dict
⋮----
"""Expose geometry for scene/contact assertions and compositor reuse."""
⋮----
offsets=SUPPORTS[action]
points=tuple((x+dx,y+dy) for dx,dy in offsets)
distances=[math.dist(a,b) for a,b in zip(points,points[1:])]
⋮----
end=points[-1]
⋮----
def draw_mount(layer:Image.Image,pose:dict,action:str)->dict
⋮----
"""Draw as prop underlay so the torso naturally occludes its belt socket."""
⋮----
geo=mount_geometry(action,pose["root"])
⋮----
def pix(p):return (round(p[0]),round(p[1]))
d=ImageDraw.Draw(layer,"RGBA")
coords=[pix(p0),pix(p1),pix(p2)]
⋮----
# Parallel power conductor with a limited cyan reflection.
⋮----
r=9 if n==1 else 7
```

## File: sprites/temporal_sprite_audit.py
```python
#!/usr/bin/env python3
"""Audit real rendered TECH animation frames at gameplay scale.

Objective regression signals only, NEVER artistic or semantic approval.
No canonical queue mutations; strict DONE is expressly forbidden.
"""
⋮----
ACTIONS=('WALK','CARRY','IDLE','WORK','REPAIR','CELEB')
SIDE=96
⋮----
def opaque_palette_signature(rgba:np.ndarray)->np.ndarray
⋮----
"""Three normalized 8-bin opaque-channel histograms, invariant to limb position.

    Unlike a median per-pixel difference, this catches partial recoloring of
    garments while tolerating legitimate repositioning and transparent effects.
    """
stable=rgba[:,:,3]>=220
rgb=rgba[:,:,:3][stable]
⋮----
quant=np.minimum(rgb.astype(np.uint16)//32,7)
⋮----
def opaque_palette_distance(left:np.ndarray,right:np.ndarray)->float
⋮----
"""Average total variation across R/G/B channel distributions [0,1]."""
⋮----
def inspect_clip(root:Path,action:str,frames_expected:int=24) -> dict
⋮----
directory=root/action
manifest=json.loads((directory/'qa-manifest.json').read_text(encoding='utf-8'))
⋮----
qa=manifest.get('qa',{})
⋮----
frames=[directory/'frames'/f'CHR-TECH-{action}-{i:02d}.png' for i in range(frames_expected)]
extra=list((directory/'frames').glob('*.png'))
⋮----
masks=[];areas=[];bbox=[];digests=[];rgba_frames=[];palettes=[]
⋮----
img=source.resize((SIDE,SIDE),Image.Resampling.LANCZOS)
rgba=np.asarray(img.convert('RGBA'),dtype=np.uint8)
alpha=rgba[:,:,3]
original_bounds=source.getchannel('A').getbbox()
⋮----
mask=alpha>=128
⋮----
b=(int(xx.min()),int(yy.min()),int(xx.max()+1),int(yy.max()+1))
⋮----
ordered_digest=hashlib.sha256(''.join(digests).encode('ascii')).hexdigest()
⋮----
differences=[];area_jump=[];color_jumps=[];palette_jumps=[]
⋮----
j=(i+1)%frames_expected
b=masks[j]
union=int(np.count_nonzero(a|b))
diff=float(np.count_nonzero(a^b)/union) if union else 1.0
⋮----
# Robust chromatic continuity across the overlapping opaque interior.
# This distinguishes a texture/color flash from legitimate pose motion,
# and ignores detached transparent VFX/background pixels.
stable=(rgba_frames[i][:,:,3]>=220)&(rgba_frames[j][:,:,3]>=220)
⋮----
rgb_a=rgba_frames[i][:,:,:3].astype(np.int16)
rgb_b=rgba_frames[j][:,:,:3].astype(np.int16)
changed=np.mean(np.abs(rgb_a-rgb_b),axis=2)[stable]
⋮----
median=statistics.median(differences)
⋮----
seam_ratio=differences[-1]/median
max_ratio=max(differences)/median
color_baseline=statistics.median(color_jumps)
max_color_jump=max(color_jumps)
# Empirically calibrated on the six source clips at 96px; genuine
# intentional tiny glow changes affect a minority of stable pixels.
rgb_limit=max(42.,color_baseline*6.+15.)
problems=[]
⋮----
palette_baseline=statistics.median(palette_jumps)
palette_limit=max(.18,palette_baseline*5.+.08)
⋮----
def audit(root:Path,output:Path,skin:Path|None=None)->dict
⋮----
index=json.loads((root/'production-index.json').read_text(encoding='utf-8'))
⋮----
items=index.get('actions',[])
⋮----
frames={}
⋮----
m=json.loads((root/a/'qa-manifest.json').read_text())
⋮----
results={a:inspect_clip(root,a,frames[a]) for a in ACTIONS}
source_hashes={r['source_skin_sha256'] for r in results.values()}
⋮----
actual=hashlib.sha256(skin.read_bytes()).hexdigest()
⋮----
report={'format':'zte-temporal-qa-v1','strict_status':'NEEDS_REVIEW',
⋮----
writer=csv.writer(f)
⋮----
vals=results[a]['per_transition_disagreement']
⋮----
image=Image.new('RGB',(1160,80+len(ACTIONS)*102),(23,31,43))
d=ImageDraw.Draw(image)
⋮----
y=67+index*102
info=results[a]
vals=info['per_transition_disagreement']
maximum=max(.16,max(vals)*1.12)
⋮----
x=130+i*41
h=max(2,round((v/maximum)*67))
⋮----
def main()
⋮----
parser=argparse.ArgumentParser(description=__doc__)
⋮----
args=parser.parse_args()
report=audit(args.source,args.output,args.skin)
```

## File: sprites/ter07_energy_conduit_candidate.py
```python
#!/usr/bin/env python3
"""Author a candidate-only 2.5D semantic replacement for TER-07.

TER-07 is an Expansion-era energy conduit connector, not a terrain platform.
This v3 candidate adds material depth, bevels and an extruded junction while
remaining isolated on transparency. It never writes the runtime asset.
"""
⋮----
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'art/production/ter07'
SIDE=1024
⋮----
P0=(170.0,720.0)
P1=(854.0,322.0)
DEPTH=(18.0,25.0)
⋮----
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def mul(v,s): return (v[0]*s,v[1]*s)
⋮----
def unit_and_normal(a,b)
⋮----
dx=b[0]-a[0]; dy=b[1]-a[1]
length=math.hypot(dx,dy)
u=(dx/length,dy/length)
n=(-u[1],u[0])
⋮----
def pt(t,side=0.0,depth=0.0)
⋮----
p=add(P0,mul(U,t))
p=add(p,mul(N,side))
p=add(p,mul(DEPTH,depth))
⋮----
def strip_poly(start,end,half_width,depth=0.0)
⋮----
def quad_extrude(poly,depth_vec)
⋮----
def draw_side_faces(draw,top_poly,depth_vec,fill)
⋮----
lower=[add(p,depth_vec) for p in top_poly]
# Only visible lower/right side faces in the shared 2.5D light.
⋮----
j=(i+1)%4
⋮----
def render()
⋮----
im=Image.new('RGBA',(SIDE,SIDE),(0,0,0,0))
⋮----
# Controlled cyan bloom, restricted to the connector footprint.
glow=Image.new('RGBA',(SIDE,SIDE),(0,0,0,0))
gd=ImageDraw.Draw(glow,'RGBA')
⋮----
glow=glow.filter(ImageFilter.GaussianBlur(23))
⋮----
d=ImageDraw.Draw(im,'RGBA')
⋮----
start=pt(16)
end=pt(LENGTH-16)
outer=strip_poly(start,end,58)
⋮----
# Top bevel and recessed channel.
bevel=strip_poly(pt(28),pt(LENGTH-28),49)
⋮----
trench=strip_poly(pt(38),pt(LENGTH-38),36)
⋮----
# Lower-right channel lip adds depth without becoming a floor card.
lip_a=[pt(38,-36),pt(LENGTH-38,-36),pt(LENGTH-38,-27),pt(38,-27)]
⋮----
# Twin recessed energy rails, with shadow, emissive core and hot highlight.
⋮----
a=pt(48,side)
b=pt(LENGTH-48,side)
shadow_a=add(a,(5,7)); shadow_b=add(b,(5,7))
⋮----
# Attached structural clamps. Their lower halves are darker to reinforce extrusion.
⋮----
c=pt(t)
a=add(c,mul(N,-51)); b=add(c,mul(N,51))
⋮----
# Bolted energy coupler: dark socket -> cyan lens -> white pin highlight.
r=13
⋮----
# Inline junction box, integrated in the conduit and visibly extruded.
c=pt(LENGTH*.52)
hu=49; hn=49
top=[
depth=mul(DEPTH,1.15)
lower=[add(p,depth) for p in top]
# Visible junction side faces.
⋮----
inner_hu=31; inner_hn=30
inner=[
⋮----
# Recessed reactor lens and small material bolts.
r=16
⋮----
p=add(add(c,mul(U,du)),mul(N,dn))
⋮----
# Shared upper-left key highlight and lower-right occlusion edge.
⋮----
# End caps make this a modular connector, not an arbitrary strip.
⋮----
a=add(c,mul(N,-56)); b=add(c,mul(N,56))
⋮----
def validate(im)
⋮----
a=im.getchannel('A')
bbox=a.getbbox()
⋮----
margin=min(bbox[0],bbox[1],SIDE-bbox[2],SIDE-bbox[3])
⋮----
coverage=sum(a.histogram()[8:])/(SIDE*SIDE)
⋮----
w=bbox[2]-bbox[0]; h=bbox[3]-bbox[1]
aspect=max(w,h)/max(1,min(w,h))
⋮----
def main()
⋮----
im=render()
metrics=validate(im)
png=OUT/'zte_terrain_07_candidate_v3.png'
⋮----
report={
```

## File: sprites/test_action_contact.py
```python
"""Regression tests for contact-driven WORK/REPAIR effects and safety gate."""
⋮----
class ContactTests(unittest.TestCase)
⋮----
def test_work_hands_remain_inside_one_visible_screen(self)
⋮----
t=i/512
root=(252,270+1.8*math.sin(2*math.pi*t))
⋮----
touch=work_contact({'root':root,'handL':left,'handR':right})
⋮----
def test_work_events_are_at_visual_peak_after_reindex(self)
⋮----
origin=round(count*5/24)
picks=work_event_indices(count,origin)
⋮----
p=work_pulse(((frame+origin)%count)/count)
prev=work_pulse(((frame-1+origin)%count)/count)
nxt=work_pulse(((frame+1+origin)%count)/count)
⋮----
# Match the renderer's tie tolerance for equal-height peaks.
⋮----
def test_repair_tool_physically_connects_to_wrist(self)
⋮----
phase=2*math.pi*t
root=(252,270+1.8*math.sin(phase))
hand=(root[0]+58+12*math.sin(phase),root[1]-54+11*math.cos(phase))
contact=repair_contact({'root':root,'handR':hand})
⋮----
def test_contact_rejects_disconnected_hands(self)
⋮----
base={'root':(252,270),'handL':(0,0),'handR':(0,0)}
⋮----
def test_weld_sparks_are_periodic_and_phase_gated(self)
⋮----
t=i/256
```

## File: sprites/test_animation_batch_planner.py
```python
"""Contract tests for pending animation planning without GPU or queue mutation."""
⋮----
class AnimationBatchPlannerTests(unittest.TestCase)
⋮----
def test_frame_contract_matches_existing_android_runtime(self)
⋮----
def test_promotion_is_never_inferred_from_existing_webp(self)
⋮----
def test_exactly_pending_master_character_ids_are_planned(self)
⋮----
queue=json.loads(MASTER.read_text(encoding="utf-8"))
expected={
plans=items("ALL")
⋮----
def test_invalid_candidates_are_repaired_before_review(self)
⋮----
ranks={"regenerate":0,"semantic-review":1,"generate":2}
⋮----
def test_plan_is_read_only(self)
⋮----
files=[MASTER,MANIFEST]
before=[hashlib.sha256(p.read_bytes()).hexdigest() for p in files]
⋮----
after=[hashlib.sha256(p.read_bytes()).hexdigest() for p in files]
```

## File: sprites/test_audit_chatgpt_originals.py
```python
"""Regression coverage for character motion audit loop closure."""
⋮----
class CharacterLoopSeamTests(unittest.TestCase)
⋮----
def test_walk_reports_last_to_first_change(self)
⋮----
atlas = Image.new("RGBA", (1024, 1024))
⋮----
frame = Image.new("RGBA", (256, 256))
draw = ImageDraw.Draw(frame)
# Last frame intentionally returns to first, giving a zero
# seam change despite motion between intermediate frames.
offset = 0 if index in (0, 7) else 10 + index * 5
⋮----
path = Path(temp) / "walk.png"
⋮----
result = inspect(path, "ENG", "WALK")
⋮----
def test_walk_flags_disproportionate_loop_snap(self)
⋮----
# Seven nearby poses followed by a distant final pose.
offset = index * 2 if index < 7 else 95
⋮----
path = Path(temp) / "walk-snap.png"
⋮----
def test_repair_detects_tool_snap_even_with_stationary_legs(self)
⋮----
x = 40 + index if index < 9 else 170
⋮----
path = Path(temp) / "repair-tool-snap.png"
⋮----
result = inspect(path, "ENG", "REPAIR")
⋮----
def test_carry_reports_wraparound_too(self)
⋮----
draw = ImageDraw.Draw(atlas)
⋮----
path = Path(temp) / "carry.png"
⋮----
result = inspect(path, "LOG", "CARRY")
```

## File: sprites/test_autonomous_walk.py
```python
"""Unattended walk generator regression tests. Run: python -m unittest ..."""
⋮----
class WalkGeometryTests(unittest.TestCase)
⋮----
def test_cyclic_pose_and_left_right_symmetry(self)
⋮----
cfg = WalkSettings()
⋮----
a=pose(phase,cfg)
b=pose(phase+1,cfg)
⋮----
l=foot_local(phase+.5,cfg)
r=foot_local(phase,cfg)
⋮----
def test_planted_feet_exact_world_lock(self)
⋮----
cfg=WalkSettings()
speed=cfg.stride/cfg.stance_fraction
⋮----
t=i/1000
u=(t+phase_offset)%1
⋮----
first=pose(t,cfg)[side]
second=pose(t+.0005,cfg)[side]
⋮----
def test_pose_physical_envelope(self)
⋮----
qa=verify_motion(WalkSettings())
⋮----
def test_heel_toe_continuity_and_symmetry(self)
⋮----
eps=1e-7
⋮----
t=i/200
p=pose(t,cfg)
⋮----
def test_reject_unphysical_config(self)
⋮----
class BuildTests(unittest.TestCase)
⋮----
def test_real_export_and_safety_gate(self)
⋮----
studio=Path(__file__).parent/'pose_studio.html'
if not studio.exists():studio=Path(__file__).parent/'index.html'
⋮----
cfg=WalkSettings(frames=8)
root=Path(work)/'build'
manifest=export(root,cfg,studio)
⋮----
events=json.loads((root/'frame-events.json').read_text())
⋮----
frame_poses=json.loads((root/'frame-poses.json').read_text())
⋮----
project=json.loads((root/'project.json').read_text())
```

## File: sprites/test_character_action_gate.py
```python
"""Exercise the real lightweight character action QA without loading Flux/GPU.

The production module imports PyTorch/diffusers at module load. Extract only
its pure PIL functions through Python AST, so these tests execute the exact
shipping action gate without requiring Kaggle or model downloads.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
⋮----
FUNCTIONS = {
⋮----
def load_shipping_action_gate()
⋮----
source = (ROOT / "tools" / "sprites" / "kaggle_character_sheet_factory_v1.py").read_text(
tree = ast.parse(source)
selected = [
⋮----
module = ast.fix_missing_locations(ast.Module(body=selected, type_ignores=[]))
namespace = {
⋮----
"production_first_enabled": lambda: False,  # Legacy strict regression suite
⋮----
def worker()
⋮----
im = Image.new("RGBA", (256, 256))
d = ImageDraw.Draw(im)
⋮----
class ProductionActionQATests(unittest.TestCase)
⋮----
@classmethod
    def setUpClass(cls)
⋮----
def test_exactly_frozen_idle_is_rejected(self)
⋮----
frozen = worker()
⋮----
def test_subtle_eye_blink_idle_is_retained_for_manual_review(self)
⋮----
frames = []
⋮----
frame = worker()
⋮----
def test_stationary_carry_does_not_pass_for_a_walk_cycle(self)
⋮----
static = worker()
⋮----
def test_single_last_frame_arm_jerk_is_not_celebration(self)
⋮----
neutral = worker()
last = worker()
⋮----
def test_static_walk_is_rejected(self)
⋮----
same = worker()
```

## File: sprites/test_character_anchor_pair_salvage.py
```python
"""Synthetic multi-person role-anchor recovery tests; no semantic approval."""
⋮----
def pair(second=True, overlapping=False, second_short=False)
⋮----
bg=(219,219,219)
image=Image.new('RGB',(1024,1024),bg)
alpha=Image.new('L',(1024,1024))
draw=ImageDraw.Draw(image)
mask=ImageDraw.Draw(alpha)
left=(120,90,315,800)
right=(270 if overlapping else 670,100,480 if overlapping else 850,
⋮----
isolated=image.convert('RGBA')
⋮----
class PairAnchorRecoveryTests(unittest.TestCase)
⋮----
def test_one_person_is_kept_from_two_separate_full_bodies(self)
⋮----
def test_single_person_is_not_falsely_salvaged(self)
⋮----
def test_overlap_is_left_for_manual_rejection(self)
⋮----
def test_short_detached_panel_is_not_treated_as_another_worker(self)
```

## File: sprites/test_character_approved_idle_fallback.py
```python
"""Tests for approved legacy IDLE anchoring; no external models or GPU."""
⋮----
def approved_atlas(path: Path, doubled: bool = False)
⋮----
atlas = Image.new("RGBA", (1024, 1024))
d = ImageDraw.Draw(atlas)
⋮----
class ApprovedIdleFallbackTests(unittest.TestCase)
⋮----
def test_reuses_exact_existing_strict_done_visual_reference(self)
⋮----
root = Path(tmp)
m = root / "manifest.md"
⋮----
original = root / "zte_chr_log_idle_final.png"
⋮----
def test_runtimes_unapproved_idle_never_becomes_reference(self)
⋮----
def test_rejects_duplicate_person_in_single_cell(self)
⋮----
manifest = root / "manifest.md"
```

## File: sprites/test_character_ground_shadow_cleanup.py
```python
"""Ground shadow cleanup regressions; image-only recovery, no approvals."""
⋮----
def character(shadow: bool = True, white_shoes: bool = False)
⋮----
image = Image.new("RGBA", (256, 256))
d = ImageDraw.Draw(image)
⋮----
sole = (204, 204, 205, 255) if white_shoes else (48, 55, 70, 255)
⋮----
class GroundShadowCleanupTests(unittest.TestCase)
⋮----
def test_long_neutral_shadow_removed_without_erasing_dark_boots(self)
⋮----
source=character()
⋮----
def test_without_shadow_has_no_changes(self)
⋮----
source=character(shadow=False)
⋮----
def test_pale_shoes_do_not_get_erased_without_external_shadow(self)
⋮----
source=character(shadow=False, white_shoes=True)
⋮----
def test_darker_shadow_trapped_between_boots_is_removed(self)
⋮----
original = character(shadow=False)
trapped = Image.new("RGBA", (256, 256))
draw = ImageDraw.Draw(trapped)
⋮----
before_face = trapped.getpixel((128, 42))
before_boot = trapped.getpixel((105, 228))
⋮----
def test_gray_pants_with_connected_feet_are_not_split(self)
⋮----
source = Image.new("RGBA", (256, 256))
draw = ImageDraw.Draw(source)
⋮----
def test_wrong_shape_is_left_untouched(self)
⋮----
source=Image.new("RGBA", (128, 128), (225, 225, 225, 255))
```

## File: sprites/test_character_head_identity_lock.py
```python
"""Image-only headgear identity registration checks; no GPU or semantic approval."""
⋮----
def make_person(helmet=(245, 88, 38, 255), raised_arm=False)
⋮----
frame = Image.new("RGBA", (256, 256))
draw = ImageDraw.Draw(frame)
⋮----
class HeadIdentityLockTests(unittest.TestCase)
⋮----
def test_identical_upright_reference_restores_stable_headgear(self)
⋮----
anchor = make_person((241, 71, 40, 255))
target = make_person((23, 218, 228, 255))
⋮----
# Center of the head stays a real part of the same IDLE reference.
⋮----
def test_raised_arm_with_unreliable_top_alignment_is_not_pasted(self)
⋮----
source = make_person()
target = make_person((12, 225, 234, 255), raised_arm=True)
⋮----
def test_wide_incompatible_head_shape_is_not_pasted(self)
⋮----
target = make_person((25, 223, 234, 255))
# Keep the rest of the body while replacing the helmet silhouette
# with an oversized incompatible rectangular obstruction.
⋮----
def test_empty_frames_cannot_be_identity_references(self)
⋮----
image = Image.new("RGBA", (256, 256))
```

## File: sprites/test_character_provider_reservation.py
```python
"""Prevent Kaggle/Autofactory from stealing a live provider-specific repair."""
⋮----
class ReservationTests(unittest.TestCase)
⋮----
def test_external_repair_excludes_concurrent_kaggle_character_dispatch(self)
⋮----
p=Path(d)/'queue.json'
⋮----
answer=worker.make_decision({
⋮----
def test_expired_or_other_provider_has_no_lock(self)
⋮----
def test_injected_invalid_or_missing_reservation_does_not_block(self)
```

## File: sprites/test_character_rejection_evidence.py
```python
"""Synthetic tests for opt-in review evidence; never creates approval."""
⋮----
class RejectionEvidenceTests(unittest.TestCase)
⋮----
def setUp(self)
⋮----
def test_rejected_idle_keeps_exact_frames_and_no_approval(self)
⋮----
frames=[]
⋮----
frame=Image.new("RGBA", (256, 256))
⋮----
result=save_rejected_idle_preview(frames,"CHR-ENG-IDLE",
⋮----
data=json.loads(report_path.read_text())
⋮----
cell=atlas.crop(((index%4)*256,(index//4)*256,
⋮----
def test_non_idle_asset_and_no_frames_never_write_preview(self)
⋮----
frames=[Image.new("RGBA",(256,256)) for _ in range(6)]
⋮----
def test_bad_dimensions_are_not_silently_published(self)
```

## File: sprites/test_character_review_matrix.py
```python
def fake_queue()
⋮----
actions=['WALK','WORK','CARRY','REPAIR','CELEB']
ids=['CHR-OP-'+a for a in actions]
⋮----
assets=[{'id':'DONE-'+str(i),'strict_status':'DONE'} for i in range(216)]
⋮----
class MatrixTests(unittest.TestCase)
⋮----
def test_exact_pending_roles_and_no_auto_promotion(self)
⋮----
report=build(fake_queue())
⋮----
def test_semantic_rejection_before_technical_success(self)
⋮----
text=markdown(report)
⋮----
def test_live_markdown_does_not_repeat_stale_tech_rejection_after_promotion(self)
⋮----
q=fake_queue()
⋮----
report=build(q)
⋮----
def test_cannot_inflate_canonical_queue(self)
⋮----
def test_deterministic_order_and_source_immutability(self)
⋮----
first=build(q)
second=build(q)
```

## File: sprites/test_character_semantic_gate.py
```python
"""Synthetic visual failure tests, no external models and no automatic approval."""
⋮----
def person(i=0,color=(80,144,187,255))
⋮----
frame=Image.new('RGBA',(256,256))
d=ImageDraw.Draw(frame)
⋮----
def portrait(i=0)
⋮----
class SemanticGateTests(unittest.TestCase)
⋮----
def test_consistent_full_body_is_not_blocked(self)
⋮----
result=clip_risk([person(i%3) for i in range(8)])
⋮----
def test_portraits_and_fragments_block(self)
⋮----
result=clip_risk([portrait(i%2) for i in range(8)])
⋮----
def test_unrelated_costume_palettes_are_detected(self)
⋮----
frames=[person(0,(210,30,45,255)) if i%2 else
result=clip_risk(frames)
⋮----
def test_conjoined_double_workers_are_detected_even_with_one_body_component(self)
⋮----
draw=ImageDraw.Draw(frame)
# Two separate helmet/head shapes, shoulders and torsos fused into a
# single continuous shape: the old component/width check passed it.
⋮----
result=clip_risk([frame.copy() for _ in range(6)],'IDLE')
⋮----
def test_one_realistic_idle_head_does_not_trigger_multi_head_gate(self)
⋮----
frames=[person(i%2) for i in range(6)]
⋮----
def test_two_people_in_one_cell_cause_visible_mass_jump(self)
⋮----
pair=Image.new('RGBA',(256,256))
⋮----
frames=[person() for _ in range(7)]+[pair]
⋮----
def test_empty_frame_fails_hard(self)
⋮----
frames=[person() for _ in range(7)]+[Image.new('RGBA',(256,256))]
⋮----
def test_persistent_flat_floor_shadow_blocks_candidate(self)
⋮----
clean=[person(i%2) for i in range(8)]
⋮----
shadowed=[]
⋮----
with_shadow=frame.copy()
⋮----
report=clip_risk(shadowed,'IDLE')
⋮----
def test_connected_dark_boot_silhouette_is_not_labeled_gray_cast_shadow(self)
⋮----
frames=[]
⋮----
frame=person()
# Long dark continuous sole reproduces the geometry that the
# alpha-only ground-band risk falsely classified as a gray shadow.
⋮----
report=clip_risk(frames,'IDLE')
⋮----
def test_one_long_ground_contact_is_not_a_persistent_shadow(self)
⋮----
frames=[person(i%2) for i in range(8)]
⋮----
report=clip_risk(frames,'WORK')
⋮----
def test_one_collapsed_work_frame_blocks_even_if_nine_others_are_full_body(self)
⋮----
normal=person()
tiny=normal.crop((0,16,256,229)).resize((256,164))
short=Image.new('RGBA',(256,256))
⋮----
frames=[normal.copy() for _ in range(10)]
⋮----
result=clip_risk(frames,'WORK')
⋮----
def test_alternating_helmet_or_face_color_blocks_identity(self)
⋮----
color=(245,65,35,255) if index%2 else (30,235,224,255)
⋮----
result=clip_risk(frames,'IDLE')
⋮----
def test_morphing_crate_palette_blocks_carrying(self)
⋮----
color=(230,50,32,255) if index%2 else (15,225,226,255)
⋮----
result=clip_risk(frames,'CARRY')
⋮----
# The same synthetic color change is not proof that a different
# non-prop action should be blocked on mid-body content alone.
⋮----
def test_face_helmet_morph_blocks_work_even_when_color_palette_matches(self)
⋮----
reference=person()
altered=person()
draw=ImageDraw.Draw(altered)
⋮----
frames=[reference.copy() for _ in range(10)]
⋮----
def test_off_center_head_does_not_count_as_raised_arm(self)
⋮----
# Regression for v1.20 OP-CELEB: the helmet is left of the centre of
# a standing figure's full bbox. The old detector counted the helmet
# and shoulders as if both hands were raised in all eight frames.
⋮----
counts=celebration_arm_reach_counts([frame.copy() for _ in range(8)])
⋮----
raised=frame.copy()
⋮----
def test_celebration_counts_actual_raised_arm_frames_not_final_sparkle(self)
⋮----
def simple(raised=False)
neutral=simple()
cheering=simple(True)
# The historical LOG-CELEB produced mostly neutral poses, then a
# final-frame effect. It must not pass as progressive arm animation.
false_loop=[neutral.copy() for _ in range(7)]+[cheering]
counts=celebration_arm_reach_counts(false_loop)
⋮----
progressive=[neutral.copy() for _ in range(3)]+[cheering.copy() for _ in range(5)]
scores=celebration_arm_reach_counts(progressive)
⋮----
def test_idles_with_subtle_eye_blinks_have_visible_activity(self)
⋮----
base=person()
⋮----
frame=base.copy()
⋮----
def test_idle_visual_activity_requires_multiple_nonempty_frames(self)
⋮----
def test_same_palette_is_identical(self)
⋮----
signature=color_signature(person())
```

## File: sprites/test_export_tech_canonical_review.py
```python
"""Offline tests for canonical TECH candidate staging: no network/auto-promotion."""
⋮----
class TechCanonicalReviewTests(unittest.TestCase)
⋮----
def test_phase_indices_are_stable_distinct_and_bounded(self)
⋮----
def fixture(self, root: Path, action: str = "CARRY") -> tuple[Path, Path]
⋮----
source = root / "source"
skin = root / "skin.webp"
⋮----
skin_hash = hashlib.sha256(skin.read_bytes()).hexdigest()
actions = ("WALK", "CARRY", "IDLE", "WORK", "REPAIR", "CELEB")
index = {
⋮----
folder = source / action
⋮----
manifest = {
⋮----
# 24 actual full-body 512px RGBA frames. The silhouette is game-size legible.
⋮----
im = Image.new("RGBA", (512, 512))
d = ImageDraw.Draw(im)
⋮----
def test_real_staged_pixels_preserve_review_and_padding(self)
⋮----
root = Path(tmp)
⋮----
output = root / "review"
result = stage_action(source, output, "CARRY", digest(skin))
⋮----
def test_refuse_unreviewable_metadata_and_missing_pixels(self)
⋮----
bad = root / "bad-skin"
⋮----
qa = source / "CARRY" / "qa-manifest.json"
data = json.loads(qa.read_text())
⋮----
def test_unsupported_action_is_rejected(self)
```

## File: sprites/test_focused_sprite_atlas.py
```python
"""Offline framing tests: no build artifacts or user review necessary."""
⋮----
class FramingTests(unittest.TestCase)
⋮----
def test_shared_camera_for_six_animation_unions(self)
⋮----
union=[(163,47,357,467),(171,47,368,467),(167,49,341,459),
crop=shared_crop(union)
⋮----
def test_metadata_preserves_exact_world_pivot(self)
⋮----
crop=(28,33,476,481)
⋮----
pt=view_pivot(crop,size)
⋮----
def test_framed_sprite_does_not_clip_visual_effects(self)
⋮----
image=Image.new('RGBA',(CANVAS,CANVAS))
d=ImageDraw.Draw(image)
⋮----
crop=shared_crop([image.getchannel('A').getbbox()])
⋮----
got=framed_sprite(image,crop,size)
⋮----
def test_invalid_camera_bounds_and_pivots_are_rejected(self)
⋮----
# Out-of-range pivot must be rejected rather than silently
# selecting an unrelated camera; clipping is also a valid rejection.
⋮----
def test_full_extent_uses_legacy_safe_fallback(self)
⋮----
crop=shared_crop([(0,0,512,512)])
⋮----
image=Image.new('RGBA',(512,512))
⋮----
result=framed_sprite(image,crop,96)
```

## File: sprites/test_identity_locked_walk_candidate.py
```python
"""Regression tests for alternative identity-locked WALK review candidates."""
⋮----
ROOT=Path(__file__).resolve().parents[2]
⋮----
class IdentityLockedWalkTests(unittest.TestCase)
⋮----
def test_four_real_assets_are_not_overwritten_and_only_staged(self)
⋮----
source=(ROOT/'art/incoming/final-sprites'/
⋮----
digest=hashlib.sha256(source.read_bytes()).hexdigest()
report=render(source,role,Path(tmp))
⋮----
atlas=Image.open(report['candidate_path'])
⋮----
cells=[atlas.crop((i%4*256,i//4*256,i%4*256+256,i//4*256+256))
⋮----
first=source_frame(source,ROLES[role])
# Skeleton changes occur below the neck; identity pixels at
# the crown remain unchanged, modulo tiny breathing motion.
⋮----
bounds=cell.getchannel('A').getbbox()
⋮----
def test_cycle_deterministic_and_source_identity_immutable(self)
⋮----
source=ROOT/'art/incoming/final-sprites/zte_chr_op_walk_final.png'
first=source_frame(source,ROLES['OP'])
data=first.tobytes()
⋮----
one=warp(first,t)
two=warp(first,t)
⋮----
def test_refuses_bad_inputs(self)
```

## File: sprites/test_local_character_action_fx.py
```python
"""Regressions for editable first-party sprite effects: no semantic approval."""
⋮----
ROOT=Path(__file__).resolve().parents[2]
⋮----
class LocalActionFxTests(unittest.TestCase)
⋮----
def test_every_role_has_distinct_integrated_action_effects(self)
⋮----
fx=action_fx(role,action,.9,tool_x=182,tool_y=132,bounce=2)
root=ET.fromstring('<svg xmlns="http://www.w3.org/2000/svg">'+fx+'</svg>')
namespaces={'svg':'http://www.w3.org/2000/svg'}
nodes=root.findall('.//svg:g',namespaces)
⋮----
def test_action_highlights_close_the_loop(self)
⋮----
a=action_fx(role,action,0,tool_x=180,tool_y=123)
b=action_fx(role,action,2*math.pi,tool_x=180,tool_y=123)
⋮----
def test_raster_effects_do_not_escape_frame_or_create_fake_labels(self)
⋮----
markup=action_fx(role,action,1.9,tool_x=191,tool_y=125)
⋮----
# Explicit clamp prevents highlights crossing right side.
⋮----
def test_repair_is_a_distinct_compact_hand_tool_cycle(self)
⋮----
# WORK and REPAIR used to have identical 15px x 12px hand strokes,
# which made the two actions indistinguishable at gameplay size.
source=(ROOT/'tools/sprites/render_chatgpt_originals.py').read_text(encoding='utf8')
⋮----
wrist="176+(15 if action=='WORK' else 8)*math.sin(phase)"
vertical="123+(12 if action=='WORK' else 7)*math.cos(phase)+bounce"
⋮----
def test_engineer_repair_wrench_rotates_about_fixed_real_socket(self)
⋮----
swings = []
stations = []
ns = "{http://www.w3.org/2000/svg}"
⋮----
phase = 2 * math.pi * index / 10
wrist = engineer_repair_wrist(phase)
tip = tool_tip("ENG", "REPAIR", phase,
⋮----
angle = tool_angle("REPAIR", phase, role="ENG")
⋮----
svg = ET.fromstring(svg_frame("ENG", "REPAIR", index, 10))
station = [e for e in svg.iter()
wrench = [e for e in svg.iter()
⋮----
def test_engineer_work_scans_with_shared_tool_light_and_planted_boots(self)
⋮----
points = []
angles = []
⋮----
bounce = 3.6 * math.sin(phase)
⋮----
tree = ET.fromstring(svg_frame("ENG", "WORK", index, 10))
tools = [node for node in tree.iter()
⋮----
transform = tools[0].get("transform")
coords = transform.split("translate(")[1].split(")")[0].split(",")
⋮----
angle = tool_angle("WORK", phase, role="ENG")
⋮----
# The real work light travels with the physical sensor tip.
tip = tool_tip("ENG", "WORK", phase,
⋮----
feet = [node for node in tree.iter()
⋮----
markup = svg_frame(role, "WORK", 3, 10)
⋮----
def test_engineer_repair_torso_loads_but_both_feet_stay_planted(self)
⋮----
motions = []
⋮----
feet = [e for e in svg.iter()
⋮----
motion = [e for e in svg.iter()
⋮----
fixed = [e for e in svg.iter()
⋮----
svg = svg_frame(role, "REPAIR", 3, 10)
⋮----
def test_idle_and_walk_have_no_unattached_decorations(self)
⋮----
def test_bad_role_action_rejected(self)
⋮----
def test_renderer_invokes_attached_effects_after_hand(self)
⋮----
text=(ROOT/'tools/sprites/render_chatgpt_originals.py').read_text(encoding='utf8')
⋮----
# The renderer's VFX metadata is versioned independently of its
# physically attached tool/wrist geometry. Keep metadata validation,
# without pinning the obsolete v1 implementation label.
```

## File: sprites/test_local_character_contact_gait.py
```python
"""Pixel-independent gait contract for locally authored WALK/CARRY candidates."""
⋮----
class ContactGaitTests(unittest.TestCase)
⋮----
def test_stance_feet_are_anchored_vertically_even_while_torso_bobs(self)
⋮----
phase=2*math.pi*i/80
bounce=1.4*(1-math.cos(phase*2))
leg=foot_pose(phase,side,action,bounce)
⋮----
def test_exact_half_cycle_leg_antiphase(self)
⋮----
phase=i*2*math.pi/24
l=foot_pose(phase,"L",action)
r=foot_pose(phase+math.pi,"R",action)
⋮----
def test_swing_clears_ground_without_crossed_legs(self)
⋮----
raised=0
⋮----
phase=2*math.pi*i/48
left=foot_pose(phase,"L",action)
right=foot_pose(phase,"R",action)
⋮----
def test_swing_knees_turn_forward_instead_of_overshooting_silhouette(self)
⋮----
pose=foot_pose(phase,side,action)
⋮----
# The lifted knee should remain within one compact
# 3/4-view shin offset, not splay outside the worker.
⋮----
def test_loop_is_periodic_without_coordinate_jumps(self)
⋮----
first=foot_pose(0,side,action)
last=foot_pose(2*math.pi,side,action)
⋮----
def test_engineer_gait_exaggerates_readable_steps_without_crossed_legs(self)
⋮----
ankles = {"L": [], "R": []}
lift = {"L": [], "R": []}
stance_counts = {"L": 0, "R": 0}
⋮----
phase = 2 * math.pi * index / 8
poses = {}
⋮----
pose = foot_pose(phase, side, "WALK", profile="eng-walk")
⋮----
start = foot_pose(0, side, "WALK", profile="eng-walk")
end = foot_pose(2 * math.pi, side, "WALK", profile="eng-walk")
⋮----
def test_engineer_stride_has_stable_ground_contact_across_dense_cycle(self)
⋮----
# Catch contact glitches between the eight exported sprite samples.
# The planted sole must never rise or rotate; the recovering boot
# must clear the ground without crossing the opposite ankle.
⋮----
phase = 2 * math.pi * i / 240
left = foot_pose(phase, "L", "WALK", profile="eng-walk")
right = foot_pose(phase, "R", "WALK", profile="eng-walk")
⋮----
# Cyclic geometry, including knee and boot, must close cleanly.
a = foot_pose(0, side, "WALK", profile="eng-walk")
b = foot_pose(2 * math.pi, side, "WALK", profile="eng-walk")
⋮----
def test_loaded_carry_has_less_sway_than_unladen_walk(self)
```

## File: sprites/test_package_tech_actions_runtime.py
```python
"""Regression tests for six TECH runtime review atlases.

Run AFTER the six-clip generator in CI; independently audit its real pixels.
"""
⋮----
FIXTURE=Path('build/tech-actions-v3').resolve()
⋮----
class RuntimePackTests(unittest.TestCase)
⋮----
def setUp(self)
⋮----
def test_six_atlases_keep_the_review_gate(self)
⋮----
out=Path(temp)/'runtime'
temporal_dir=Path(temp)/'temporal'
⋮----
report_file=temporal_dir/'temporal-qa.json'
manifest=package(FIXTURE,out,temporal_report=report_file)
⋮----
bad=json.loads(report_file.read_text())
⋮----
bad_file=Path(temp)/'stale-temporal.json'
⋮----
focus=manifest['focused_camera']
⋮----
variant=item['focused_variants'][str(size)]
shadow=item['optional_shadow_layer']['focused_variants'][str(size)]
⋮----
crop=variant['shared_crop_bounds_px']
expected_pivot=[round((252-crop[0])*size/(crop[2]-crop[0]),3),
⋮----
# Published runtime clips must retain a valid attachment
# gate for WORK and REPAIR, not just an on-screen hand marker.
⋮----
var=item['variants'][str(size)]
⋮----
shadow=item['optional_shadow_layer']['variants'][str(size)]
⋮----
player=(out/'review-player.html').read_text()
⋮----
def test_game_scale_check_rejects_clipped_or_empty_frames(self)
⋮----
empty=Image.new('RGBA',(512,512))
⋮----
clipped=Image.new('RGBA',(512,512))
⋮----
def test_source_contract_has_shared_skin_and_event_timeline(self)
⋮----
def test_reject_approved_or_corrupted_index(self)
⋮----
root=Path(temp)
source=json.loads((FIXTURE/'production-index.json').read_text())
⋮----
def test_reject_missing_review_marker(self)
⋮----
def test_refuse_desynchronized_visual_events(self)
⋮----
events=json.loads((FIXTURE/action/'footstep-events.json').read_text())
changed=next(i for i,e in enumerate(events) if e.get('vfx_event')==event_kind)
⋮----
def test_reject_narrow_celebration_pose(self)
⋮----
manifest=json.loads((FIXTURE/'CELEB'/'qa-manifest.json').read_text())
⋮----
def test_reject_celebration_below_overhead_qa_threshold(self)
⋮----
def test_reject_detached_mount_even_when_contact_with_screen_passes(self)
⋮----
root=Path(tmp)
⋮----
manifest=json.loads((FIXTURE/action/'qa-manifest.json').read_text())
⋮----
def test_reject_mismatched_work_and_repair_contacts(self)
⋮----
def test_reject_mismatched_phase_and_transfer_provenance(self)
⋮----
def test_reject_missing_fabric_renderer_provenance(self)
⋮----
manifest=json.loads((FIXTURE/'WORK'/'qa-manifest.json').read_text())
⋮----
def test_reject_soft_deformation_disabled_in_manifest(self)
⋮----
manifest=json.loads((FIXTURE/'WALK'/'qa-manifest.json').read_text())
⋮----
def test_reject_falsely_approved_visual_qa(self)
⋮----
qa=json.loads((FIXTURE/'WALK'/'qa-manifest.json').read_text())
```

## File: sprites/test_pollinations_character_sheet_factory.py
```python
"""Offline regression checks: generation MUST return separate full-body frames."""
⋮----
def full_body()
⋮----
frame=Image.new('RGBA',(256,256))
d=ImageDraw.Draw(frame)
⋮----
class IndependentFrameTests(unittest.TestCase)
⋮----
def test_prompt_never_requests_multi_pose_atlas(self)
⋮----
item={'id':'CHR-LOG-'+action,'role':'LOG','action':action}
prompt=factory.independent_frame_prompt(item,'left foot forward')
⋮----
def test_each_pose_is_its_own_image_not_an_atlas_slice(self)
⋮----
item={'id':'CHR-LOG-CARRY','role':'LOG','action':'CARRY'}
requests=[]
def fetch(prompt,seed)
def extract(raw,action,standalone=False)
⋮----
# A source image saved before the new generation strategy must
# never contaminate a modern identity-locked animation.
old=Path(tmp)/'pollinations-frame-cache'/'CHR-LOG-CARRY'
⋮----
first=factory.generate_independent_frames(item,49017)
⋮----
again=factory.generate_independent_frames(item,49017)
⋮----
self.assertEqual(len(requests),8) # cache, no web calls
⋮----
def test_margin_padding_does_not_erase_missing_body_parts(self)
⋮----
near_edge=Image.new('RGBA',(768,768))
d=ImageDraw.Draw(near_edge)
⋮----
padded=factory.safe_source_margin(near_edge)
⋮----
bb=padded.getchannel('A').getbbox()
⋮----
cropped=near_edge.copy()
⋮----
def test_reserved_repair_stages_candidate_without_overwriting_canonical(self)
⋮----
item={'id':'CHR-LOG-CARRY','role':'LOG','action':'CARRY',
⋮----
historical=factory.INCOMING/'zte_chr_log_carry_final.png'
⋮----
target=factory.candidate_destination(item)
⋮----
def test_blocked_controlled_queue_cannot_fall_back_to_manifest_todos(self)
⋮----
root=Path(tmp)
manifest=root/'manifest.md'
⋮----
queue=root/'controlled.json'
⋮----
def test_unexpected_action_cannot_use_generic_fallback(self)
```

## File: sprites/test_rigged_tech_actions_v3.py
```python
"""Regression checks for unattended six-animation TECH rig and non-bypassable review."""
⋮----
KIT = Path(__file__).with_name("skin-tech-v1.webp")
⋮----
class MultiActionGeometryTests(unittest.TestCase)
⋮----
def test_each_action_is_strictly_periodic(self)
⋮----
a = pose_for(phase, action)
b = pose_for(phase + 1, action)
⋮----
def test_action_spine_cycle_and_contact_are_stable(self)
⋮----
t=i/96
before=pose_for(t,action)
after=pose_for(t+1,action)
lean=spine_lean(t,action)
⋮----
anchor=(x+dx*co-dy*si,y+dx*si+dy*co)
⋮----
def test_far_foot_depth_lane_preserves_contacts_and_near_foot(self)
⋮----
p=pose_for(t,action)
base=core.pose(t)
⋮----
q=pose_for(t+1,action)
⋮----
def test_stationary_actions_keep_feet_grounded_and_hands_reachable(self)
⋮----
p = pose_for(i / 48, action)
⋮----
def test_carry_grip_is_fixed_relative_to_crate(self)
⋮----
p = pose_for(i / 48, "CARRY")
⋮----
def test_carry_is_a_visible_amber_crate_with_both_handle_anchors(self)
⋮----
# Pixel test: a tiny cyan console must never masquerade as cargo.
⋮----
pose = pose_for(t, "CARRY")
layer = Image.new("RGBA", (512, 512))
⋮----
cargo = layer.crop((l, top, l + 128, top + 90))
amber = sum(
blue = sum(
⋮----
def test_action_motion_is_not_identical_across_frames(self)
⋮----
hand = [pose_for(i / 24, action)["handR"] for i in range(24)]
⋮----
def test_celebration_is_overhead_and_periodic(self)
⋮----
t=i/192
p=pose_for(t,"CELEB")
⋮----
angle=p["torso_lean_rad"]
⋮----
shoulder=(x+dx*co-dy*si,y+dx*si+dy*co)
⋮----
q=pose_for(t+1,"CELEB")
⋮----
def test_action_contacts_and_overlaid_feedback_are_phase_correct(self)
⋮----
work=pose_for(t,"WORK")
contact=work_contact(work)
⋮----
repair=pose_for(t,"REPAIR")
⋮----
def test_invalid_action_and_impossible_settings_rejected(self)
⋮----
root = Path(tmp)
⋮----
class MultiActionRendererTests(unittest.TestCase)
⋮----
@classmethod
    def setUpClass(cls)
⋮----
def test_deterministic_unique_per_action(self)
⋮----
def test_work_repair_brackets_really_show_at_96px(self)
⋮----
# Geometry-only tests could pass if the bracket were fully hidden
# behind the torso. Compare the rendered output with a reversible
# support-free control at the actual 96px gameplay resolution.
⋮----
before=np.asarray(
after=np.asarray(
changed=int(np.count_nonzero(
⋮----
def test_six_actions_use_reversible_joint_fabric(self)
⋮----
# Compare output against the SAME action/props rendered with the
# old joint treatment; no pose, timing or event changes are permitted.
⋮----
# One-identity, repeatable output with fabric enabled.
⋮----
# WALK has no action props, making a strict binary before/after valid.
sample=.125
⋮----
def test_each_export_remains_a_review_candidate(self)
⋮----
out = Path(tmp) / action
⋮----
qa = manifest["qa"]
⋮----
events = json.loads((out / "animation-events.json").read_text())
⋮----
phase_origin=manifest["phase_origin_frame"]
⋮----
enabled=repair_spark_intensity(
⋮----
expected=list(work_event_indices(8,manifest["phase_origin_frame"]))
actual=[i for i,e in enumerate(events)
```

## File: sprites/test_rigged_tech_walk_v2.py
```python
"""Offline, deterministic modular textured walk regression suite."""
⋮----
KIT=Path(__file__).with_name('skin-tech-v1.webp')
⋮----
KIT=Path('/mnt/data/tech-modular-v1.webp')
⋮----
class RigMathTests(unittest.TestCase)
⋮----
def test_closed_loop_and_foot_contact(self)
⋮----
p=a
⋮----
def test_world_space_stance_lock(self)
⋮----
speed=92/.62
⋮----
t=j/1000
phase=(t+offset)%1
⋮----
p=foot_local(t+offset)
q=foot_local(t+offset+.0001)
⋮----
def test_inverse_kinematics_lengths(self)
⋮----
p=pose(t)
⋮----
joint=ik(hip,foot,94,99,sgn)
⋮----
class RenderTests(unittest.TestCase)
⋮----
@classmethod
 def setUpClass(cls): cls.kit=load_kit(KIT)
⋮----
def test_all_twelve_pieces_present(self)
⋮----
def test_stable_identity_alpha_and_dimensions(self)
⋮----
def test_optional_spine_flex_is_safe_and_backward_compatible(self)
⋮----
# The old WALK output must remain pixel-for-pixel unchanged when no spine
# control is supplied; existing runtime art must not silently regress.
⋮----
neutral=pose(t);neutral['torso_lean_rad']=0.0
⋮----
tilted=pose(t);tilted['torso_lean_rad']=.05
⋮----
bad=pose(.125);bad['torso_lean_rad']=invalid
⋮----
def test_optional_joint_fabric_is_deterministic_and_review_only(self)
⋮----
# Keep existing production textures unchanged by default.
⋮----
bbox=textile.getchannel('A').getbbox()
⋮----
def test_build_export_review_gate(self)
⋮----
out=Path(tmp)/'render'
⋮----
qa=manifest['qa']
⋮----
def test_reject_invalid_config(self)
```

## File: sprites/test_soft_skin_deform.py
```python
"""Tests for deterministic, opt-in bending of TECH modular atlas textures."""
⋮----
KIT = Path(__file__).with_name("skin-tech-v1.webp")
⋮----
class DeformedSkinTests(unittest.TestCase)
⋮----
@classmethod
    def setUpClass(cls)
⋮----
def test_bend_orientation_and_continuity(self)
⋮----
def test_reject_invalid_curves_and_textures(self)
⋮----
def test_opt_in_preserves_exact_legacy_pixels(self)
⋮----
def test_24_frame_walk_geometry_and_review_lock(self)
⋮----
frames=[];positions=[];boots=[]
⋮----
qa=core.check(frames,positions,boots)
⋮----
def test_six_action_renderer_is_deterministic_not_clipped(self)
⋮----
box=a.getchannel("A").getbbox()
⋮----
# The WALK candidate must be soft deformed, unlike the explicit old path.
source=pose_for(.125,"WALK")
```

## File: sprites/test_tech_prop_mount.py
```python
"""Safety and frame-stability checks for mounted WORK/REPAIR hardware."""
⋮----
class TechPropMountTests(unittest.TestCase)
⋮----
def test_all_512_phase_samples_keep_belt_and_device_connected(self)
⋮----
p=pose_for(i/512,action)
g=mount_geometry(action,p['root'])
⋮----
def test_mount_follows_idle_bob_without_world_drift(self)
⋮----
t=i/128
a=mount_geometry(action,pose_for(t,action)['root'])
b=mount_geometry(action,pose_for(t+1,action)['root'])
⋮----
def test_software_draw_is_deterministic_and_not_clipped(self)
⋮----
pose=pose_for(.125,action)
images=[]
⋮----
frame=Image.new('RGBA',(512,512))
geom=draw_mount(frame,pose,action)
⋮----
bbox=frame.getchannel('A').getbbox()
⋮----
def test_reject_invalid_roots_actions_canvases(self)
```

## File: sprites/test_temporal_sprite_audit.py
```python
"""Synthetic regression tests for 96px frame-to-frame TECH audit."""
⋮----
class TemporalAuditTests(unittest.TestCase)
⋮----
def setUp(self)
⋮----
directory=self.root/a
⋮----
record={'asset_id':'CHR-TECH-'+a,'frames':self.frames,
⋮----
index={'strict_status':'NEEDS_REVIEW','review_required':True,
⋮----
def tearDown(self)
⋮----
def save_frame(self,a,i,blank=False,jump=False)
⋮----
image=Image.new('RGBA',(512,512))
⋮----
d=ImageDraw.Draw(image)
displacement=round(13*math.sin(2*math.pi*i/self.frames))
⋮----
x=252+displacement
⋮----
# Track deterministic frame identity without changing the binary alpha.
⋮----
def test_six_valid_clips_export_review_only_evidence(self)
⋮----
report=audit(self.root,Path(self.work.name)/'report')
⋮----
def test_empty_and_clipped_frames_are_rejected(self)
⋮----
image=Image.open(self.root/'WORK/frames/CHR-TECH-WORK-06.png')
⋮----
def test_duplicate_content_is_rejected(self)
⋮----
original=(self.root/'IDLE/frames/CHR-TECH-IDLE-00.png').read_bytes()
⋮----
def test_temporal_spike_and_bad_seam_are_rejected(self)
⋮----
# A full pose jump may eliminate opaque overlap before silhouette
# metrics are reached; both detections are correct hard failures.
⋮----
def test_single_frame_color_flash_is_detected_even_with_same_alpha(self)
⋮----
path=self.root/'WORK/frames/CHR-TECH-WORK-09.png'
⋮----
rgba=image.convert('RGBA')
⋮----
# Deliberately invert garment and skin RGB without moving even
# one silhouette/alpha pixel; geometry-only QA must not pass it.
corrupted=Image.merge('RGBA',tuple(
⋮----
def test_partial_costume_recolor_is_caught_even_when_rgb_median_is_zero(self)
⋮----
# Recolor <50% of stable garment pixels: the RGB median alone
# stays unchanged, but the location-invariant palette must detect it.
⋮----
original=np.asarray(image.convert('RGBA')).copy()
modified=original.copy()
⋮----
selected=(original[:,:,3]>=220)&(xx>252)
⋮----
def test_optional_real_skin_digest_matches_output_provenance(self)
⋮----
source=Path(self.work.name)/'skin.webp'
⋮----
digest=hashlib.sha256(source.read_bytes()).hexdigest()
index_path=self.root/'production-index.json'
index=json.loads(index_path.read_text())
⋮----
path=self.root/action/'qa-manifest.json'
data=json.loads(path.read_text())
⋮----
accepted=audit(self.root,Path(self.work.name)/'good',skin=source)
⋮----
def test_review_and_identity_guards_are_enforced(self)
⋮----
file=self.root/'REPAIR/qa-manifest.json'
record=json.loads(file.read_text())
```

## File: sprites/test_verify_character_action_candidates.py
```python
"""Synthetic regressions for WORK/REPAIR translation-only atlas rejection."""
⋮----
def figure(offset: int = 0, raised_hand: int = 0) -> Image.Image
⋮----
frame = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
d = ImageDraw.Draw(frame)
dx = offset
⋮----
def atlas(frames: list[Image.Image]) -> Image.Image
⋮----
output = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
⋮----
class CharacterActionCollectorTests(unittest.TestCase)
⋮----
def test_rejects_ten_frames_of_standing_character_sliding_sideways(self)
⋮----
offsets = (0, 4, 8, 12, 16, 20, 16, 12, 8, 4)
frames = [figure(offset) for offset in offsets]
metrics = action_translation_metrics(frames)
⋮----
target = Path(temp) / "zte_chr_op_work_final.png"
⋮----
qa = {"assets": [{"file": target.name, "pass": True, "issues": []}]}
result = annotate_report(Path(temp), qa)
⋮----
def test_true_arm_pose_variation_is_not_mistaken_for_actor_translation(self)
⋮----
frames = [figure(0, raised_hand=i * 4) for i in range(10)]
⋮----
def test_eight_frames_without_overhead_arms_cannot_pass_celebration(self)
⋮----
# Regression for the real collector 38296422676 OP-CELEB: visual
# variations from torso/helmet redrawing do not equal raised fists.
frames = [figure() for _ in range(8)]
⋮----
name = "zte_chr_op_celeb_final.png"
⋮----
qa = {"assets": [{"file": name, "pass": True, "issues": []}]}
⋮----
row = result["assets"][0]
⋮----
def test_several_overhead_arm_frames_do_not_trigger_false_celebration_block(self)
⋮----
frames = []
⋮----
frame = figure()
⋮----
path = Path(temp) / "zte_chr_log_celeb_final.png"
⋮----
evidence = check_action_atlas(path, "celeb")
⋮----
def test_production_first_defers_missing_celebration_gesture(self)
⋮----
# Production candidates may be visually weak, but must remain explicitly
# unapproved and retain the missing-gesture evidence for future polish.
⋮----
result = annotate_report(Path(temp), qa, production_first=True)
⋮----
def test_production_first_still_rejects_invalid_atlas_dimensions(self)
⋮----
name = "zte_chr_op_work_final.png"
⋮----
row = annotate_report(Path(temp), qa, production_first=True)["assets"][0]
⋮----
def test_bad_work_atlas_is_rejected_without_aborting_sibling_candidates(self)
⋮----
target = Path(temp) / "zte_chr_eng_repair_final.png"
⋮----
qa = {"assets": [
```

## File: sprites/test_verify_character_idle_candidates.py
```python
"""Offline collector fallback QA checks, without model/GPU or strict promotion."""
⋮----
def atlas(two_heads: bool) -> Image.Image
⋮----
im = Image.new("RGBA", (1024, 1024))
⋮----
tile = Image.new("RGBA", (256, 256))
painter = ImageDraw.Draw(tile)
⋮----
class CollectorSingleSubjectQA(unittest.TestCase)
⋮----
def test_realistic_two_worker_pair_overrides_producer_pass(self)
⋮----
directory = Path(tmp)
⋮----
report = {"assets": [
output = annotate_report(directory, report)
⋮----
again = annotate_report(directory, output)
⋮----
def test_production_first_does_not_waive_multiple_workers(self)
⋮----
name = "zte_chr_log_idle_final.png"
⋮----
report = {"assets": [{"file": name, "pass": True, "issues": []}]}
row = annotate_report(Path(tmp), report, production_first=True)["assets"][0]
⋮----
def test_missing_idle_candidate_fails_closed(self)
⋮----
output = annotate_report(Path(tmp), report)
⋮----
def test_non_idle_status_is_never_altered(self)
```

## File: sprites/test_weight_transfer.py
```python
"""Pure tests for cyclic IK-supported gait loading (no sprite approvals)."""
⋮----
class WeightTransferTests(unittest.TestCase)
⋮----
def test_load_is_smooth_periodic_and_bounded(self)
⋮----
t=i/2000
⋮----
def test_foot_depth_lane_preserves_ground_contact_and_grips(self)
⋮----
t=i/384
old=core.pose(t)
new=pose_for(t,action)
⋮----
# Walking wrists preserve their original relative gait
# swing as the root receives its stance-driven offset.
⋮----
# CARRY intentionally overrides the walking arm swing:
# compare grips to the transported load, NOT old WALK arms.
⋮----
hip=(new['root'][0]+offset,new['root'][1])
⋮----
def test_wrist_reach_and_cyclic_shift(self)
⋮----
max_jump=0
poses=[pose_for(i/192,action) for i in range(192)]
⋮----
lean=p['torso_lean_rad']
⋮----
shoulder=(x+dx*math.cos(lean)-dy*math.sin(lean),
⋮----
nxt=poses[(i+1)%len(poses)]
jump=abs(p['weight_transfer_px']-nxt['weight_transfer_px'])
max_jump=max(max_jump,jump)
⋮----
def test_deterministic_and_no_source_mutation(self)
⋮----
p=core.pose(.1875)
original=p.copy()
result=transfer_pose(p,.1875,'WALK')
```

## File: sprites/validate_animation_sheet.py
```python
#!/usr/bin/env python3
"""Validate one CHR/MCH animation sheet against the deterministic production contract."""
⋮----
ROOT = Path(__file__).resolve().parents[2]
⋮----
def fail(msg: str) -> None
⋮----
def dominant_ratio(alpha: Image.Image) -> float
⋮----
small = alpha.resize((96, 96), Image.Resampling.BILINEAR)
px = small.load(); seen=set(); areas=[]
⋮----
q=deque([(x,y)]); seen.add((x,y)); area=0
⋮----
def main() -> int
⋮----
p=argparse.ArgumentParser()
⋮----
args=p.parse_args()
rows=math.ceil(args.frames/args.columns)
expected=(args.columns*args.cell, rows*args.cell)
im=Image.open(args.sheet).convert("RGBA")
⋮----
alpha=im.getchannel("A")
⋮----
reports=[]
pivots=[]
⋮----
x=(i%args.columns)*args.cell; y=(i//args.columns)*args.cell
cell=alpha.crop((x,y,x+args.cell,y+args.cell))
bbox=cell.getbbox()
⋮----
coverage=sum(cell.histogram()[8:])/(args.cell*args.cell)
⋮----
dom=dominant_ratio(cell)
⋮----
pivot_x=(x0+x1)/2/args.cell
pivot_y=y1/args.cell
⋮----
# Character feet/base pivots must stay stable enough to avoid visible jitter.
xs=[p[0] for p in pivots]; ys=[p[1] for p in pivots]
max_jitter=max(max(xs)-min(xs), max(ys)-min(ys))
limit=.12 if args.family=="CHR" else .16
⋮----
result={"sheet":str(args.sheet),"family":args.family,"frames":args.frames,"cell":args.cell,"grid":[args.columns,rows],"pivot_jitter":round(max_jitter,4),"frames_report":reports}
```

## File: sprites/validate_runtime_asset.py
```python
#!/usr/bin/env python3
⋮----
ALPHA=8
CHR_RE=re.compile(r"^CHR-(OP|TECH|LOG|ENG)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$")
CHR_FRAMES={"IDLE":6,"WALK":8,"WORK":10,"CARRY":8,"REPAIR":10,"CELEB":8}
⋮----
def major_components(alpha: Image.Image)->int
⋮----
small=alpha.resize((128,128),Image.Resampling.BILINEAR)
px=small.load(); seen=set(); major=0; min_area=int(128*128*.012)
⋮----
q=deque([(x,y)]); seen.add((x,y)); area=0
⋮----
def validate(asset_id:str,path:Path)->dict
⋮----
issues=[]
⋮----
try: im=Image.open(path).convert("RGBA")
⋮----
a=im.getchannel("A"); lo,hi=a.getextrema()
⋮----
x0=(i%4)*128; y0=(i//4)*128
cell=a.crop((x0,y0,x0+128,y0+128))
⋮----
edges=(cell.crop((0,0,128,4)),cell.crop((0,124,128,128)),cell.crop((0,0,4,128)),cell.crop((124,0,128,128)))
⋮----
expected=CHR_FRAMES[m.group(2)]
⋮----
x0=(i%4)*256; y0=(i//4)*256
cell=a.crop((x0,y0,x0+256,y0+256)); bb=cell.getbbox()
⋮----
h=cell.histogram(); cov=sum(h[8:])/(256*256)
⋮----
edges=(cell.crop((0,0,256,8)),cell.crop((0,248,256,256)),cell.crop((0,0,8,256)),cell.crop((248,0,256,256)))
⋮----
hist=a.histogram(); coverage=sum(hist[ALPHA:])/(im.width*im.height)
⋮----
comps=major_components(a)
⋮----
def main()
⋮----
ap=argparse.ArgumentParser()
⋮----
a=ap.parse_args()
result=validate(a.asset_id,a.path)
```

## File: sprites/verify_character_action_candidates.py
```python
#!/usr/bin/env python3
"""Collector-side action-motion audit, independent of Kaggle generator version.

A technical atlas passes only if no obvious image-only identity/motion risks
were detected. Every pass still needs explicit artistic and Android review.
This annotates a derived QA report; source sprites and strict DONE stay intact.
"""
⋮----
ACTION_FILENAME = re.compile(r"^zte_chr_(op|log|eng|tech)_(work|repair|celeb)_final\.png$")
ATLAS_SIZE = (1024, 1024)
CELL_SIZE = 256
ACTION_FRAME_COUNTS = {"work": 10, "repair": 10, "celeb": 8}
⋮----
def check_action_atlas(path: Path, action: str, *, production_first: bool = False) -> dict
⋮----
rgba = file.convert("RGBA")
frames = [
risk = clip_risk(frames, action.upper())
flags = list(risk["flags"])
evidence = {"action_pose_metrics": risk.get("action_pose_metrics", {})}
⋮----
# Recheck generated CELEB sheets independently of the historical
# producer's arm detector: the v1.20 OP artifact falsely passed with
# eight helmet/shoulder pixels mislabeled as a raised-arm gesture.
scores = celebration_arm_reach_counts(frames)
active = sum(n >= 28 for n in scores)
⋮----
raw_risk = "BLOCKING" if (
⋮----
def annotate_report(candidates_dir: Path, report: dict, *, production_first: bool = False) -> dict
⋮----
name = Path(str(row.get("file") or "")).name
match = ACTION_FILENAME.fullmatch(name)
⋮----
details = check_action_atlas(candidates_dir / name, match.group(2), production_first=production_first)
⋮----
details = {
⋮----
issues = [str(v) for v in row.get("issues", [])]
⋮----
issue = "action-visual-risk:" + str(flag)
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
qa = json.loads(args.qa_report.read_text(encoding="utf-8"))
qa = annotate_report(args.candidates, qa, production_first=args.production_first)
```

## File: sprites/verify_character_idle_candidates.py
```python
#!/usr/bin/env python3
"""Fail-closed visual risk screening for generated IDLE candidate atlases.

Runs on the GitHub collector after producer output download, regardless of
which generator snapshot ran on Kaggle. Mutates only a derived QA JSON report,
never source sprites, strict status, or runtime resource files.
"""
⋮----
IDLE_FILENAME = re.compile(r"^zte_chr_(op|log|eng|tech)_idle_final\.png$")
FRAME = 256
ATLAS = (1024, 1024)
⋮----
def check_idle_atlas(path: Path, *, production_first: bool = False) -> dict
⋮----
atlas = file.convert("RGBA")
frames = [
risk = clip_risk(frames, "IDLE")
⋮----
def annotate_report(candidates_dir: Path, report: dict, *, production_first: bool = False) -> dict
⋮----
name = Path(str(row.get("file") or "")).name
⋮----
details = check_idle_atlas(candidates_dir / name, production_first=production_first)
⋮----
details = {
⋮----
issues = [str(x) for x in row.get("issues", [])]
⋮----
issue = "idle-visual-risk:" + flag
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
qa = json.loads(args.qa_report.read_text(encoding="utf-8"))
qa = annotate_report(args.candidates, qa, production_first=args.production_first)
⋮----
details = row.get("idle_identity_risk")
```

## File: sprites/verify_local_character_bundle.py
```python
#!/usr/bin/env python3
"""Technical verification of locally authored character atlases.

Image/format checks cannot approve artistic semantics or mark strict DONE.
No network, GPU, image generation, repository mutation, or zip extraction.
"""
⋮----
FRAME_COUNTS = {"IDLE": 6, "WALK": 8, "WORK": 10, "CARRY": 8, "REPAIR": 10, "CELEB": 8}
IDS = {f"CHR-{role}-{action}" for role in ("OP", "LOG", "ENG") for action in FRAME_COUNTS}
ARCHIVE_LIMIT = 80 * 1024 * 1024
ENTRY_LIMIT = 12 * 1024 * 1024
TOTAL_LIMIT = 240 * 1024 * 1024
⋮----
def verify(path: Path) -> dict
⋮----
problems: list[str] = []
detail: list[dict] = []
⋮----
files: dict[str, zipfile.ZipInfo] = {}
total = 0
⋮----
name = info.filename
posix = PurePosixPath(name)
⋮----
manifest = json.loads(archive.read("manifest.json"))
entries = manifest.get("entries", [])
actual_ids = [item.get("id") for item in entries]
⋮----
aid = item.get("id", "")
⋮----
frame_count = FRAME_COUNTS[action]
name = f"zte_chr_{role.lower()}_{action.lower()}_final.png"
errors = []
⋮----
data = archive.read("atlases/" + name)
sha = hashlib.sha256(data).hexdigest()
⋮----
rgba = image.convert("RGBA")
frames = []
margin = 256
⋮----
tile = rgba.crop((x, y, x + 256, y + 256))
box = tile.getchannel("A").getbbox()
⋮----
margin = min(margin, box[0], box[1], 256 - box[2], 256 - box[3])
⋮----
svg_name = f"svg_source/{role}/{action}/{index:02}.svg"
⋮----
def main() -> int
⋮----
parser = argparse.ArgumentParser()
⋮----
args = parser.parse_args()
⋮----
result = verify(args.pack)
⋮----
result = {"technical_preflight_pass": False, "errors": [str(err)],
```

## File: sprites/weight_transfer.py
```python
"""Deterministic, foot-locked character weight transfer for modular TECH sprites.

No image generation, no manual pose editing, no production queue mutation.
The support-weight envelope is continuous at contact transitions. Applying
pelvis sway never changes a foot target or the original footstep timeline.
"""
⋮----
STANCE_FRACTION = 0.62
AMPLITUDES_PX = {'WALK': 4.0, 'CARRY': 2.2}
⋮----
def stance_load(t: float, offset: float = 0.0, stance: float = STANCE_FRACTION) -> float
⋮----
"""Smooth loading/unloading of a planted foot, zero throughout its swing."""
⋮----
u = (t + offset) % 1.0
⋮----
def support_bias(t: float) -> float
⋮----
"""Signed loading right (+1) versus left (-1); periodic over one cycle."""
right = stance_load(t)
left = stance_load(t, 0.5)
denom = left + right
⋮----
def transfer_pose(source: dict[str, Any], t: float, action: str) -> dict[str, Any]
⋮----
"""Translate only hips/torso and both wrists, while feet remain world-locked.

    The renderer's two-bone knee IK compensates for the body's motion.
    Returns a fresh dictionary; does not mutate the input pose or skin.
    """
⋮----
bias = support_bias(t)
dx = AMPLITUDES_PX[action] * bias
⋮----
p = dict(source)
```

## File: process_final_assets.py
```python
ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / 'art/generated'
PROCESSED = ROOT / 'art/processed'
RUNTIME = ROOT / 'app/src/main/res/drawable-nodpi'
MANIFEST = INBOX / 'assets.json'
⋮----
def trim_alpha(im: Image.Image) -> Image.Image
⋮----
alpha = im.getchannel('A')
bbox = alpha.getbbox()
⋮----
def pad_square(im: Image.Image, padding_ratio: float = 0.10) -> Image.Image
⋮----
side = max(w, h)
pad = max(16, round(side * padding_ratio))
canvas_side = side + pad * 2
out = Image.new('RGBA', (canvas_side, canvas_side), (0, 0, 0, 0))
# bottom-centre placement preserves the world pivot while retaining safety padding.
x = (canvas_side - w) // 2
y = canvas_side - pad - h
⋮----
def alpha_quality(im: Image.Image) -> None
⋮----
a = im.getchannel('A')
⋮----
# Reject images that are effectively opaque rectangles. Generated sheets/backgrounds must not pass.
transparent = sum(1 for p in a.get_flattened_data() if p <= 8)
⋮----
def process(spec: dict) -> None
⋮----
src = INBOX / spec['source']
asset_id = spec['id']
target = spec['target']
size = int(spec.get('runtime_size', 512))
⋮----
im = opened.convert('RGBA')
⋮----
im = trim_alpha(im)
im = pad_square(im, float(spec.get('padding_ratio', 0.10)))
⋮----
canvas = Image.new('RGBA', (size, size), (0, 0, 0, 0))
x = (size - im.width) // 2
y = size - max(8, round(size * 0.08)) - im.height
y = max(0, y)
⋮----
preview = PROCESSED / f'{asset_id}.png'
⋮----
runtime = RUNTIME / target
⋮----
def process_sheet(spec: dict) -> None
⋮----
columns = int(spec['columns'])
rows = int(spec['rows'])
frame_size = int(spec['frame_size'])
padding_ratio = float(spec.get('padding_ratio', 0.10))
⋮----
source = opened.convert('RGBA')
⋮----
sheet = Image.new('RGBA', (columns * frame_size, rows * frame_size), (0, 0, 0, 0))
⋮----
top = round(row * source.height / rows)
bottom = round((row + 1) * source.height / rows)
⋮----
left = round(column * source.width / columns)
right = round((column + 1) * source.width / columns)
frame = trim_alpha(source.crop((left, top, right, bottom)))
frame = pad_square(frame, padding_ratio)
⋮----
cell = Image.new('RGBA', (frame_size, frame_size), (0, 0, 0, 0))
⋮----
def main() -> None
⋮----
specs = json.loads(MANIFEST.read_text(encoding='utf-8'))
⋮----
seen = set()
```

## File: validate_isolated_sprite.py
```python
ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / 'art/generated'
MANIFEST = INBOX / 'assets.json'
⋮----
def connected_components(alpha: Image.Image, threshold: int = 24)
⋮----
# Downsample for deterministic/cheap component analysis.
max_side = 256
scale = min(1.0, max_side / max(alpha.size))
⋮----
alpha = alpha.resize((max(1, round(alpha.width * scale)), max(1, round(alpha.height * scale))))
⋮----
px = alpha.load()
seen = bytearray(w * h)
comps = []
⋮----
def idx(x, y)
⋮----
i = idx(x, y)
⋮----
q = deque([(x, y)])
⋮----
count = 0
minx = maxx = x
miny = maxy = y
⋮----
ni = idx(nx, ny)
⋮----
def validate(path: Path) -> None
⋮----
im = opened.convert('RGBA')
alpha = im.getchannel('A')
⋮----
transparent_ratio = sum(1 for p in alpha.get_flattened_data() if p <= 8) / (im.width * im.height)
⋮----
bbox = alpha.getbbox()
⋮----
margin = min(left, top, im.width-right, im.height-bottom)
⋮----
comps = connected_components(alpha)
⋮----
total = sum(c[0] for c in comps)
major = [c for c in comps if c[0] / total >= 0.08]
⋮----
ratios = ', '.join(f'{c[0]/total:.1%}' for c in major[:6])
⋮----
# A single subject should normally form one dominant occupancy region rather than many equal cells.
dominant = comps[0][0] / total
⋮----
def validate_sheet(path: Path, spec: dict) -> None
⋮----
sheet = opened.convert('RGBA')
columns = int(spec['columns'])
rows = int(spec['rows'])
expected = int(spec['frame_count'])
⋮----
alpha = sheet.getchannel('A')
transparent_ratio = sum(1 for p in alpha.get_flattened_data() if p <= 8) / (sheet.width * sheet.height)
⋮----
top = round(row * sheet.height / rows)
bottom = round((row + 1) * sheet.height / rows)
⋮----
left = round(column * sheet.width / columns)
right = round((column + 1) * sheet.width / columns)
frame_alpha = sheet.crop((left, top, right, bottom)).getchannel('A')
⋮----
comps = connected_components(frame_alpha)
total = sum(component[0] for component in comps)
⋮----
def main() -> None
⋮----
specs = json.loads(MANIFEST.read_text(encoding='utf-8'))
⋮----
path = INBOX / spec['source']
```
