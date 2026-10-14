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
adb exec-out screencap -p > "$OUT/11-engineer-game-scale.png"
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
shots=sorted(root.glob('*-*.png'))
if len(shots)!=11:
    raise SystemExit(f'Expected ten role gallery screenshots and one Android game-scale screenshot; got {len(shots)}')
for shot in shots:
    data=shot.read_bytes()
    if len(data)<10000 or not data.startswith(bytes.fromhex('89504e470d0a1a0a')):
        raise SystemExit(f'Empty/invalid emulator screenshot: {shot}')
    width,height=unpack('>II',data[16:24])
    if width<300 or height<500:
        raise SystemExit(f'Unexpected emulator image size: {shot}: {width}x{height}')
print('LOCAL_ORIGINAL_EMULATOR_SCREENSHOT_HEADERS_PASS=11')
print('LOCAL_ORIGINAL_ROLE_ENGINEER_STAGE_OPENED=1')
PY
printf '%s\n' 'LOCAL_ORIGINAL_ANDROID_GALLERY_LAUNCHED=1'   'STRICT_DONE_UNCHANGED_BY_EMULATOR=1'   'EMULATOR_REVIEW_IS_NOT_SEMANTIC_APPROVAL=1'   > "$OUT/ANDROID_REVIEW_ONLY.txt"
