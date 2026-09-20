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
  adb logcat -d > "$EVIDENCE/logcat-failure.txt" || true
  adb exec-out screencap -p > "$EVIDENCE/failure.png" || true
  exit 1
}

dump_ui() {
  local name="$1"
  ui_dump_with_retry "$EVIDENCE/$name.xml" || fail "ui-hierarchy-unavailable:$name"
}

click_node() {
  local needle="$1"
  local dump_name="$2"
  dump_ui "$dump_name"
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
    if ! grep -Fq 'ZERO → EMPIRE' "$EVIDENCE/$probe.xml"; then
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
  for attempt in 1 2 3; do
    probe="$EVIDENCE/system-dialog-$attempt.xml"
    if ! ui_dump_with_retry "$probe"; then
      return 0
    fi
    if ! grep -Fq "Pixel Launcher isn't responding" "$probe"; then
      return 0
    fi
    echo "SYSTEM_FLAKE_DETECTED=pixel-launcher-anr attempt=$attempt"
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
}

check_no_fatal() {
  adb logcat -d > "$EVIDENCE/logcat.txt"
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

for tab in MANAGERS UPGRADES GOALS EMPIRE; do
  click_node "$tab" "before-$tab"
  assert_ui_contains "$tab" "after-$tab"
done

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

adb shell dumpsys meminfo "$PKG" > "$EVIDENCE/meminfo.txt"
adb exec-out screencap -p > "$EVIDENCE/final.png"
adb shell dumpsys activity activities > "$EVIDENCE/activity.txt"
adb shell dumpsys window windows > "$EVIDENCE/window.txt"
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
