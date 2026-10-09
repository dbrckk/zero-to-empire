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
sleep 4
adb shell pidof "$PKG" | tr -d '\r\n' | grep -Eq '^[0-9]+$'
dump opening
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
