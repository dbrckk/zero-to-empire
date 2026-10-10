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
adb logcat -d > "$OUT/logcat.txt"
if grep -E "FATAL EXCEPTION|AndroidRuntime.*FATAL" "$OUT/logcat.txt"; then
  echo "CHARACTER_PREVIEW_FAIL=fatal_exception" >&2
  exit 1
fi
echo "CHARACTER_PREVIEW_EMULATOR_PASS=1"
