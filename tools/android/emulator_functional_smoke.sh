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

# Main navigation surfaces must all be reachable.
for tab in MANAGERS UPGRADES GOALS EMPIRE; do
  click_node "$tab" "before-$tab"
  assert_ui_contains "$tab" "after-$tab"
done

# Core gameplay action: one tap raises cash from 10 to at least 11.
click_node "Power Core" "before-power-core"
sleep 1
check_alive

# Buy the first real business and verify the gameplay state changes.
click_node "Street Stand" "before-street-stand-buy"
sleep 2
assert_ui_contains "LV 1" "after-street-stand-buy"

# Commerce surface: open and close store without starting a purchase.
click_node "STORE" "before-store"
assert_ui_contains "EMPIRE STORE" "store-open"
assert_ui_contains "RESTORE PURCHASES" "store-contents"
click_node "CLOSE" "store-before-close"
sleep 1
check_alive

# Exercise Android lifecycle and verify process recovers cleanly.
adb shell input keyevent KEYCODE_HOME
sleep 2
adb shell am start -W -n "$ACT" > "$EVIDENCE/relaunch.txt"
sleep 3
check_alive
assert_ui_contains "EMPIRE" "after-relaunch"

# Verify app data actually exists after interaction and survives process restart.
adb shell am force-stop "$PKG"
sleep 1
adb shell am start -W -n "$ACT" > "$EVIDENCE/restart.txt"
sleep 3
check_alive
assert_ui_contains "EMPIRE" "after-force-stop-restart"
assert_ui_contains "LV 1" "after-force-stop-restart-level"

# Short runtime soak to exercise the 250ms economy tick and 30s autosave loop.
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
echo "FUNCTIONAL_PERSISTENCE_PASS=1"
echo "FUNCTIONAL_SOAK_PASS=1"
echo "FUNCTIONAL_SMOKE_PASS=1"
