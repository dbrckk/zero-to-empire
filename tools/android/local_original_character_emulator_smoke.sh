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
for n in 2 3 4 5; do
  adb shell input swipe 290 690 290 220 380
  sleep 1
  adb exec-out screencap -p > "$OUT/0$n-stage-scroll.png"
  adb shell pidof com.zerotoempire.game.originalreview >/dev/null
done
# UI XML improves diagnosis; screenshots and active process are hard gates.
if adb shell uiautomator dump /sdcard/local-original-qa.xml; then
  adb pull /sdcard/local-original-qa.xml "$OUT/ui-hierarchy.xml" || true
else
  echo 'Optional uiautomator XML unavailable' > "$OUT/ui-dump-warning.txt"
fi
python3 - <<'PY'
from pathlib import Path
from PIL import Image
root=Path('/tmp/zte-original-review-evidence')
shots=sorted(root.glob('0*-*.png'))
if len(shots)!=5:
    raise SystemExit('Expected five emulator screenshots')
for shot in shots:
    if shot.stat().st_size<10000:
        raise SystemExit(f'Empty/invalid emulator screenshot: {shot}')
    with Image.open(shot) as image:
        image.verify()
print('LOCAL_ORIGINAL_EMULATOR_SCREENSHOT_DECODING_PASS=5')
PY
printf '%s\n' 'LOCAL_ORIGINAL_ANDROID_GALLERY_LAUNCHED=1'   'STRICT_DONE_UNCHANGED_BY_EMULATOR=1'   'EMULATOR_REVIEW_IS_NOT_SEMANTIC_APPROVAL=1'   > "$OUT/ANDROID_REVIEW_ONLY.txt"
