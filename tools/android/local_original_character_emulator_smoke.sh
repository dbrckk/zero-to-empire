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
    stage_count=$((stage_count + 1))
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
