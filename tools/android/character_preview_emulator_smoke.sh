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
click "REPAIR" before-tech-repair-selection
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
  click "$action" "before-tech-action-$action"
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
  click "$moving_action" "before-temporal-action-$moving_action"
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
