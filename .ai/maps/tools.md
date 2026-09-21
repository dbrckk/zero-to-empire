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
  emulator_functional_smoke.sh
  test_ui_click_target.py
  test_ui_dump_retry.py
  test_ui_economy_probe.py
  ui_click_target.py
  ui_dump_retry.sh
  ui_economy_probe.py
  validate_manifest_policy.py
  validate_release_privacy.py
sprites/
  animation_batch_planner.py
  asset_queue_utils.py
  asset_wave_orchestrator.py
  audit_complete_sprite_manifest.py
  build_sprite_contact_sheet.py
  colab_mass_factory.py
  hf_public_flux_factory.py
  hf_sprite_factory.py
  hf_static_manifest_factory.py
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
  manifest_batch_planner.py
  multi_provider_static_manifest_factory.py
  plan_sprite_batches.py
  pollinations_building_batch.py
  pollinations_building_factory.py
  pollinations_character_sheet_factory.py
  procedural_fx_factory.py
  procedural_terrain_factory.py
  process_final_sprites.py
  promote_ter07_v3.py
  ter07_energy_conduit_candidate.py
  validate_animation_sheet.py
  validate_runtime_asset.py
process_final_assets.py
validate_isolated_sprite.py
```

# Files

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

  rm -f "$output" "$log"
  while (( attempt <= attempts )); do
    rm -f "$output"
    adb shell rm -f "$remote" >/dev/null 2>&1 || true

    if adb shell uiautomator dump "$remote" >"$log" 2>&1 && \
       adb pull "$remote" "$output" >/dev/null 2>&1 && \
       [[ -s "$output" ]]; then
      rm -f "$log"
      return 0
    fi

    rm -f "$output"
    if (( attempt < attempts )); then
      sleep "$delay_seconds"
    fi
    attempt=$((attempt + 1))
  done

  echo "UI_DUMP_FAILED attempts=$attempts output=$output" >&2
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

## File: sprites/animation_batch_planner.py
```python
#!/usr/bin/env python3
"""Plan animation-heavy CHR/MCH deliverables from the canonical sprite manifest.

This does not generate art. It turns vague manifest frame budgets into a stable
production contract so future GPU workers and validators agree on frame count,
cell size, sheet geometry, pivot rules and loop behavior before consuming quota.
"""
⋮----
ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/art/FINAL_AAA_SPRITE_MANIFEST.md"
INCOMING = ROOT / "art/incoming/final-sprites"
ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
MAX_BATCH = 16
⋮----
# Fixed targets chosen inside the manifest budgets. Keeping a deterministic count
# makes sheet validation and runtime animation timing reproducible.
CHR_FRAMES = {
MCH_FRAMES = 8
⋮----
def frame_contract(asset_id: str) -> tuple[int, int, int, int, str]
⋮----
action = asset_id.rsplit("-", 1)[-1]
frames = CHR_FRAMES[action]
cell = 256
columns = 4
pivot = "feet-center"
⋮----
frames = MCH_FRAMES
cell = 512
⋮----
pivot = "machine-base-center"
rows = math.ceil(frames / columns)
⋮----
def items(kind: str)
⋮----
order = 0
⋮----
m = ROW.match(line)
⋮----
family = "CHR" if asset_id.startswith("CHR-") else "MCH" if asset_id.startswith("MCH-") else None
⋮----
stem = Path(runtime).stem
candidate = INCOMING / f"{stem}.png"
runtime_path = ROOT / runtime
⋮----
def main() -> int
⋮----
p = argparse.ArgumentParser()
⋮----
args = p.parse_args()
⋮----
planned = list(items(args.kind))[: args.count]
```

## File: sprites/asset_queue_utils.py
```python
#!/usr/bin/env python3
"""Shared state helpers for the 235-asset autonomous production queue.

The master queue deliberately does not trust per-row DONE values from the legacy
manifest while historical semantic review is open. The strict baseline is defined by the reviewed ledger. BLD-02, BLD-03, BLD-11, BLD-12 and all historical FX have now been explicitly reconciled; unresolved work remains only in other building families and 24 character sheets.
ONB-00 is outside the 235 production target.
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
STRICT_BASELINE = 155
MAX_ATTEMPTS = 8
⋮----
# Prioritize unresolved families with the highest expected semantic-pass yield.
# Repeatedly failing site-card/platform families stay at the back until their
# specialized generator guards have more evidence.
BUILDING_PRIORITY = ["BLD-09", "BLD-10", "BLD-06", "BLD-05", "BLD-08",
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
def unresolved_ids() -> set[str]
⋮----
ids: set[str] = set()
⋮----
def default_asset(row: dict[str, str], unresolved: set[str]) -> dict[str, Any]
⋮----
asset_id = row["id"]
needs = asset_id in unresolved
⋮----
group = "-".join(asset_id.split("-")[:2])
⋮----
role = asset_id.split("-")[1]
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
KAGGLE_BUSY = os.getenv("AUTOF_KAGGLE_BUSY", "0") == "1"
FX_BUSY = os.getenv("AUTOF_FX_BUSY", "0") == "1"
⋮----
def by_id(queue: dict[str, Any]) -> dict[str, dict[str, Any]]
⋮----
def update_from_trigger(queue: dict[str, Any]) -> None
⋮----
# Producer failures must never strand assets in DISPATCHED forever. The
# workflow_run event is authoritative: put the active Kaggle lane back into
# the controlled queue so the next autofactory cycle can retry it, subject
# to the per-asset attempt budget.
⋮----
active = [
⋮----
# The producer writes AWAITING_REVIEW into the controlled queue.
# sync_controlled_queues() below will import that exact state.
⋮----
# Keep the specialized controlled queues aligned with master state.
⋮----
controlled = load_json(path, {}) or {}
changed = False
⋮----
aid = str(item.get("id", "")).upper()
⋮----
changed = True
⋮----
target = [
⋮----
def active_pending(path: Path) -> list[dict[str, Any]]
⋮----
q = load_json(path, {}) or {}
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
def building_family_ids(group: str) -> list[str]
⋮----
def prepare_building_group(queue: dict[str, Any], group: str) -> dict[str, Any]
⋮----
unresolved = [aid for aid in building_family_ids(group) if aid in assets and assets[aid]["strict_status"] != "DONE"]
⋮----
targets = []
⋮----
dispatched = mark_dispatch(queue, unresolved, "kaggle-building-family")
⋮----
def prepare_character_group(queue: dict[str, Any], group: str) -> dict[str, Any]
⋮----
action_order={"IDLE":0,"WALK":1,"WORK":2,"CARRY":3,"REPAIR":4,"CELEB":5}
group_assets = sorted(
⋮----
dispatched = mark_dispatch(queue, [x["id"] for x in targets[:2]], "kaggle-character-sheet")
⋮----
def next_group(queue: dict[str, Any], lane: str, priority: list[str]) -> str | None
⋮----
groups = {
⋮----
def pending_ids_from_controlled(path: Path, queue: dict[str, Any]) -> list[str]
⋮----
ids = [str(x.get("id", "")).upper() for x in active_pending(path)]
master = by_id(queue)
⋮----
def make_decision(queue: dict[str, Any]) -> dict[str, Any]
⋮----
s = stats(queue)
⋮----
# Existing controlled building work always has priority because the Kaggle
# router itself prioritizes CONTROLLED_BLD over CONTROLLED_CHR.
building_pending = pending_ids_from_controlled(BUILDING_QUEUE, queue)
⋮----
ids = mark_dispatch(queue, building_pending, "kaggle-building-family")
⋮----
group = next_group(queue, "kaggle-building-family", BUILDING_PRIORITY)
⋮----
prepared = prepare_building_group(queue, group)
⋮----
character_pending = pending_ids_from_controlled(CHARACTER_QUEUE, queue)
⋮----
ids = mark_dispatch(queue, character_pending[:2], "kaggle-character-sheet")
⋮----
group = next_group(queue, "kaggle-character-sheet", CHARACTER_PRIORITY)
⋮----
prepared = prepare_character_group(queue, group)
⋮----
fx = [
⋮----
refreshed = stats(queue)
⋮----
def main() -> int
⋮----
queue = ensure_master()
⋮----
decision = make_decision(queue)
```

## File: sprites/audit_complete_sprite_manifest.py
```python
#!/usr/bin/env python3
⋮----
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
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
pending=[r[0] for r in rows if r[4].upper()!='DONE']
⋮----
seen=set(); report=[]; failed=[]
⋮----
p=Path(runtime.replace(chr(96),''))
⋮----
r=validate(aid,p)
⋮----
out=ROOT/'art/production/final-sprite-completion-audit.json'
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
FLUX='aniketppanchal/flux.1-schnell-nf4-pkg'
ROW=re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|$")
CHR=re.compile(r'^CHR-(OP|TECH|LOG|ENG)-(IDLE|WALK|WORK|CARRY|REPAIR|CELEB)$')
ROLE={
ACTION={
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
def rejection_hints(i)
⋮----
hints=[]
⋮----
data=json.loads(REJECTION_LEDGER.read_text(encoding='utf-8'))
⋮----
prefix=str(row.get('target_prefix','')).upper()
role=str(row.get('role','')).upper()
⋮----
hint=str(row.get('prompt_hint','')).strip()
⋮----
merged=' '.join(hints[-2:])
words=merged.split()
⋮----
def prompt_pair(i,pose,mode='default')
⋮----
# Keep CLIP deliberately tiny: tokenizer expansion makes word-count estimates
# optimistic. T5 carries the descriptive detail and rejection-memory hints.
role=i['role'];action=i['action']
role_short={
core=(f"stylized 2.5D game sprite, one {role_short}, full body, "
⋮----
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
def finish_frame(raw)
⋮----
m=isolate(raw);a=m.getchannel('A');bb=a.getbbox()
⋮----
w,h=m.size;pad=max(8,w//40)
⋮----
crop=m.crop(bb);cw,ch=crop.size
⋮----
# Two side-by-side people produce an abnormally wide full-body silhouette.
# Reject before resizing so technical QA cannot normalize a multi-person frame into a valid-looking cell.
⋮----
scale=min(176/cw,218/ch); crop=crop.resize((max(1,round(cw*scale)),max(1,round(ch*scale))),Image.Resampling.LANCZOS)
cell=Image.new('RGBA',(256,256));x=(256-crop.width)//2;y=238-crop.height;cell.alpha_composite(crop,(x,y))
aa=cell.getchannel('A');cov=sum(aa.histogram()[8:])/(256*256)
⋮----
def alpha_iou(a,b)
⋮----
A=a.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
B=b.getchannel('A').resize((64,64),Image.Resampling.BILINEAR).point(lambda p:255 if p>=32 else 0)
pa,pb=A.load(),B.load();inter=union=0
⋮----
aa=pa[x,y]>0;bb=pb[x,y]>0;inter+=aa and bb;union+=aa or bb
⋮----
def sheet_qa(frames)
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
def action_qa(frames,action)
⋮----
# Per-action motion floor prevents technically valid but visually frozen atlases
# from reaching manual semantic review.
⋮----
mean_change=(sum(1-x for x in ious)/len(ious)) if ious else 0.0
⋮----
motion=lower_body_motion(frames)
⋮----
floors={'WORK':.075,'CARRY':.10,'REPAIR':.075,'CELEB':.09,'IDLE':.025}
floor=floors.get(action,.05)
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
def main()
⋮----
ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=8);ap.add_argument('--seed',type=int,default=19417);args=ap.parse_args()
items=rows()[:max(1,args.count)];print('KAGGLE_CHARACTER_PLAN='+','.join(i['id'] for i in items),flush=True)
⋮----
encs={};t,enc=load_encode()
⋮----
hints=POSE_HINT[i['action']][:ACTION[i['action']][1]]
⋮----
variants={}
⋮----
del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=load_render();report=[];role_anchor={};role_reference_cell={}
⋮----
frames=[];anchor_raw=None;fail=None;retry_reasons=[]
⋮----
ok=False;last_reason=''
⋮----
mode=retry_mode(last_reason,attempt)
⋮----
gen=torch.Generator(device='cuda').manual_seed(args.seed+idx*10000+fi*211+attempt*7919)
⋮----
shared=role_anchor.get(i['role'])
⋮----
raw=base(height=1024,width=1024,num_inference_steps=5,guidance_scale=0,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),output_type='pil',generator=gen).images[0]
anchor_raw=raw.convert('RGB')
⋮----
# Start every later animation for this role from the exact same person.
# Moderate img2img freedom changes pose while preserving face/headgear/clothes.
strength=(min(.62,.54+attempt*.035) if i['action']=='WALK' else min(.44,.32+attempt*.03))
if mode=='identity' and i['action']!='WALK':strength=max(.28,strength-.04)
raw=img(image=shared,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=strength,num_inference_steps=6,guidance_scale=0,output_type='pil',generator=gen).images[0]
⋮----
strength=(min(.64,.50+fi*.018+attempt*.025) if i['action']=='WALK' else min(.48,.29+fi*.015+attempt*.025))
if mode in {'single','identity'} and i['action']!='WALK':strength=max(.24,strength-.035)
raw=img(image=anchor_raw,prompt_embeds=pe.cuda(),pooled_prompt_embeds=ppe.cuda(),strength=strength,num_inference_steps=6,guidance_scale=0,output_type='pil',generator=gen).images[0]
frame,cov=finish_frame(raw);frames.append(frame);ok=True;print(f"KAGGLE_CHR_FRAME={i['id']} frame={fi} attempt={attempt+1} mode={mode} cov={cov:.2f}",flush=True);break
⋮----
last_reason=str(e);retry_reasons.append(last_reason);print(f"KAGGLE_CHR_RETRY={i['id']} frame={fi} attempt={attempt+1} mode={mode} reason={e}",flush=True)
if not ok:fail=f'frame-{fi}-failed';break
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
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'docs/art/FINAL_AAA_SPRITE_MANIFEST.md'
INCOMING=ROOT/'art/incoming/final-sprites'
OUT=ROOT/'art/production'
QUEUE=OUT/'controlled-character-regen-queue.json'
⋮----
ROLES={
ACTIONS={
POSES={
⋮----
def pending()
⋮----
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
def mark_queue(aid,status,seed=None)
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
def cutout(raw)
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
def sheetqa(frames)
⋮----
vals=[iou(frames[n-1],frames[n]) for n in range(1,len(frames))]
⋮----
bottoms=[]; centers=[]
⋮----
bb=frame.getchannel('A').getbbox()
⋮----
def sheet_prompt(item)
⋮----
action=item['action']; fc=ACTIONS[action][1]
poses=', '.join(POSES[action][:fc])
⋮----
def extract_frames(raw,frame_count)
⋮----
raw=raw.resize((1024,1024),Image.Resampling.LANCZOS)
frames=[]
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
⋮----
raw=fetch(sheet_prompt(it),seed)
frames=extract_frames(raw,fc)
⋮----
sheet=Image.new('RGBA',(1024,1024),(0,0,0,0))
⋮----
p=INCOMING/f"{it['stem']}.png"
⋮----
done=True
⋮----
last=str(e)
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
