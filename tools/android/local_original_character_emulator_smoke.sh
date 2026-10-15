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
if right-left<32 or bottom-top<32 or top<85 or bottom>1800:
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
  adb exec-out screencap -p > "$OUT/op-walk-city-actor-$actor-00.png"
  sleep .7
  adb exec-out screencap -p > "$OUT/op-walk-city-actor-$actor-01.png"
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
    pair=[Image.open(root/f'op-walk-city-actor-{index}-{n:02d}.png').convert('RGB')
          for n in range(2)]
    if any(image.size!=pair[0].size for image in pair):
        raise SystemExit(f'Inconsistent screenshots of actor {index}')
    l,t,r,b=rect
    if r-l<32 or b-t<32 or l<0 or t<85 or r>pair[0].width or b>pair[0].height-80:
        raise SystemExit(f'Actor {index} clipped or invalid: {rect}')
    # Allow the moving actor up to 32 device pixels of travel over .7sec.
    roi=(max(0,l-32),max(80,t-32),min(pair[0].width,r+32),
         min(pair[0].height-80,b+32))
    local=ImageChops.difference(pair[0].crop(roi),pair[1].crop(roi))
    detected=local.convert('L').point(lambda value: 255 if value>14 else 0)
    changed=sum(count for value,count in enumerate(detected.histogram()) if value>0)
    if changed<50:
        raise SystemExit(f'No actual pixels moving inside OP WALK actor {index}: {changed}')
    print(f'LOCAL_ORIGINAL_OP_WALK_ACTOR_{index}_MOTION_PASS={changed}_CHANGED_PIXELS')
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
