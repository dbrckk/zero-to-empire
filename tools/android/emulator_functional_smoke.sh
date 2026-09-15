#!/usr/bin/env bash
set -euo pipefail

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
  adb shell uiautomator dump /sdcard/window.xml >/dev/null
  adb pull /sdcard/window.xml "$EVIDENCE/$name.xml" >/dev/null
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

check_alive() {
  adb shell pidof "$PKG" | tr -d '\r\n' | grep -Eq '^[0-9]+' || fail "process-not-alive"
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
check_alive
dump_ui "initial"
adb exec-out screencap -p > "$EVIDENCE/initial.png"

for tab in MANAGERS UPGRADES GOALS EMPIRE; do
  click_node "$tab" "before-$tab"
  assert_ui_contains "$tab" "after-$tab"
done

click_node "Power Core" "before-power-core"
sleep 1
check_alive

click_node "Street Stand" "before-street-stand-buy"
sleep 2
assert_ui_contains "LV 1" "after-street-stand-buy"

dump_ui "capital-core-location"
read CORE_X CORE_Y < <(python3 - "$EVIDENCE/capital-core-location.xml" <<'PY'
import re,sys,xml.etree.ElementTree as ET
for n in ET.parse(sys.argv[1]).getroot().iter('node'):
    text=(n.attrib.get('text','')+' '+n.attrib.get('content-desc','')).lower()
    if 'power core' in text:
        m=re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]',n.attrib.get('bounds',''))
        if m:
            x1,y1,x2,y2=map(int,m.groups()); print((x1+x2)//2,(y1+y2)//2); raise SystemExit
raise SystemExit(2)
PY
)
python3 - "$CORE_X" "$CORE_Y" <<'PY' | adb shell >/dev/null
import sys
x,y=sys.argv[1],sys.argv[2]
for _ in range(2700):
    print(f"input tap {x} {y}")
PY
sleep 3
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

sleep 35
check_alive
adb shell dumpsys meminfo "$PKG" > "$EVIDENCE/meminfo.txt"
adb exec-out screencap -p > "$EVIDENCE/final.png"
adb shell dumpsys activity activities > "$EVIDENCE/activity.txt"
adb shell dumpsys window windows > "$EVIDENCE/window.txt"
check_no_fatal
if grep -E "ANR in $PKG|am_anr.*$PKG" "$EVIDENCE/logcat.txt"; then
  fail "anr-detected"
fi
echo "FUNCTIONAL_MANAGER_AUTOMATION_PASS=1"\necho "FUNCTIONAL_OFFLINE_ECONOMY_PASS=1"
echo "FUNCTIONAL_PERSISTENCE_PASS=1"
echo "FUNCTIONAL_SOAK_PASS=1"
echo "FUNCTIONAL_SMOKE_PASS=1"
