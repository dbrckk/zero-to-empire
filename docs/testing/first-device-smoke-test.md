# ZERO → EMPIRE — First Real Device Smoke Test

Use a physical Android phone on the **debug** build first. Debug uses Google's official sample ad unit IDs; Google Play Billing may report products unavailable when the APK is sideloaded, which is expected.

## Preconditions

- Android 8.0+ (minSdk 26).
- Internet enabled for consent/ad checks, then repeat part of the test with airplane mode.
- Fresh install for section A.
- Do not inject production AdMob IDs into a debug test.

## A — Fresh install / onboarding

1. Install and launch the debug APK.
2. PASS: application reaches onboarding without crash or blank screen.
3. PASS: onboarding art/text fits the display with no clipped primary action.
4. Complete all onboarding steps.
5. PASS: gameplay opens with $10 and Street Stand visible.
6. PASS: first Street Stand level can be purchased immediately.
7. PASS: cash begins increasing after the purchase.
8. Tap the Power Core repeatedly.
9. PASS: cash/tap feedback, animation, haptic and audio respond without frame stalls.

## B — Navigation / core systems

Visit every tab: Empire, Managers, Upgrades, Goals.

PASS criteria:
- No crash or stuck dialog.
- Bottom navigation remains reachable.
- No text overlaps major buttons.
- Store button opens and closes.
- Challenges are visible and have progress states.
- Daily reward can be claimed once only.

## C — Persistence

1. Buy at least one business level.
2. Note cash, business level and gems.
3. Put the app in background for 10 seconds, return.
4. PASS: no giant 100%-active-income catch-up occurs.
5. Force-close the app.
6. Relaunch.
7. PASS: purchased levels, gems and permanent state are restored.

## D — Manager/offline automation

This requires reaching/hiring Maya normally, or using a progressed test save later.

1. Hire Maya.
2. Background the app for at least 60 seconds.
3. Return.
4. PASS: offline reward appears and only manager-operated assets contribute.
5. Collect normal offline reward.
6. Repeat and choose DOUBLE OFFLINE if rewarded ad is ready.
7. PASS: reward is doubled exactly once.

## E — Rewarded ads / privacy

1. Complete privacy flow if shown.
2. Request ×2 boost.
3. PASS: if ad is ready, Google's test rewarded ad appears.
4. PASS: reward is granted only after reward callback.
5. PASS: if no network/ad is unavailable, gameplay remains usable and an informative status appears.
6. Switch to airplane mode and repeat navigation/gameplay.
7. PASS: game remains playable offline.

## F — Billing fail-safe on sideload

Open Store and tap a product.

Expected for a sideloaded debug APK: Google Play may say Billing/Product unavailable.

PASS: no crash, no free purchase reward, and the store remains dismissible.

Actual purchase validation must later be performed through a Play Console internal-testing build with configured products.

## G — Audio lifecycle

1. Start game with music audible.
2. Background app.
3. PASS: game music stops.
4. Return.
5. PASS: music resumes.
6. Start another audio app / media session and return to game.
7. PASS: audio focus behaves without two streams fighting continuously.

## H — Performance visual scan

During 5+ minutes of play:

PASS:
- scrolling business list is smooth;
- no obvious memory-induced slowdown;
- Power Core remains responsive;
- no repeated full-screen flashes;
- device does not heat abnormally during ordinary idle gameplay;
- reduced-motion mode visibly freezes ambient motion when enabled at system level.

## I — Rotation / background resilience

If device allows rotation, rotate at least twice during gameplay and with Store open.

PASS: no crash and persistent game state is retained. Cosmetic transient dialogs may close/recreate.

## J — First prestige test

For the first device smoke test, this can be deferred until enough progression exists. Before public beta it is mandatory.

PASS after Ascension:
- run cash resets to $10;
- business levels reset;
- managers reset;
- gems remain;
- permanent upgrades remain;
- legacy points increase;
- any active timed ×2 boost keeps its remaining duration.

## Immediate FAIL / release blocker

Treat any of these as a blocker:

- crash / ANR;
- blank gameplay screen;
- first business cannot be purchased;
- negative/NaN/Infinity currency displayed;
- state lost after normal relaunch;
- active production continues at full rate while backgrounded;
- rewarded reward granted without completing an ad;
- purchase reward granted after a failed/cancelled transaction;
- UI control required for progression is unreachable;
- repeated reward claim exploit.

## Evidence to capture

For every failure record:

- exact step;
- screenshot or short screen recording;
- phone model + Android version;
- whether Wi‑Fi/mobile data was active;
- Logcat stack trace for crashes.

The first device pass is successful when sections A–C, E–I have no blockers. Sections D and J become mandatory in the progressed-save pass.
