#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET

path = sys.argv[1] if len(sys.argv) > 1 else "app/src/main/AndroidManifest.xml"
root = ET.parse(path).getroot()
A = "{http://schemas.android.com/apk/res/android}"
permissions = {n.get(A+"name") for n in root.findall("uses-permission")}
allowed = {"android.permission.INTERNET", "android.permission.ACCESS_NETWORK_STATE"}
unexpected = sorted(p for p in permissions if p and p not in allowed)
missing = sorted(allowed - permissions)
if unexpected:
    raise SystemExit("Unexpected Android permissions: " + ", ".join(unexpected))
if missing:
    raise SystemExit("Required Android permissions missing: " + ", ".join(missing))
app = root.find("application")
if app is None:
    raise SystemExit("application element missing")
if app.get(A+"usesCleartextTraffic") != "false":
    raise SystemExit("usesCleartextTraffic must remain false")
activities = app.findall("activity")
launchers = []
for activity in activities:
    for intent in activity.findall("intent-filter"):
        actions={x.get(A+"name") for x in intent.findall("action")}
        cats={x.get(A+"name") for x in intent.findall("category")}
        if "android.intent.action.MAIN" in actions and "android.intent.category.LAUNCHER" in cats:
            launchers.append(activity)
if len(launchers) != 1:
    raise SystemExit(f"Expected exactly one launcher activity, got {len(launchers)}")
if launchers[0].get(A+"exported") != "true":
    raise SystemExit("Launcher activity must be explicitly exported=true")
for activity in activities:
    if activity is not launchers[0] and activity.get(A+"exported") == "true":
        raise SystemExit("Unexpected exported activity: " + str(activity.get(A+"name")))
print("ANDROID_MANIFEST_POLICY_PASS=1")
