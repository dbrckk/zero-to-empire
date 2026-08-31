# ZERO → EMPIRE — Google Play listing

This file is the release-candidate source of truth for the Play Store text and asset checklist. Keep copy factual: no download-count, ranking, earnings, or performance claims that are not independently verified.

## App name

ZERO → EMPIRE

## Short description

Build, automate and evolve an idle empire from zero to cosmic scale.

## Full description

Start with nothing. Build your first income source, automate production with managers, expand into increasingly ambitious industries, and push your empire through new eras.

ZERO → EMPIRE is an idle progression game focused on clear growth, satisfying upgrades and large-scale visual evolution.

Build your empire
- Buy and upgrade businesses to increase income.
- Hire managers to automate production.
- Unlock new assets as your economy expands.
- Use bulk-buy controls to accelerate late-game progression.

Evolve through eras
- Watch businesses gain richer visual forms as they level up.
- Reach major milestones and unlock new eras.
- Use Ascension to reset short-term progress in exchange for permanent progression.
- Develop permanent upgrades and strengthen future runs.

Idle progression
- Automated businesses continue to create value while you play.
- Eligible offline time can generate an offline reward when you return.
- The game caps paid offline progression to keep the economy controlled.

Optional monetization
- Optional rewarded ads can provide clearly presented in-game benefits.
- Optional purchases include lifetime ad removal, a starter pack and gem packs.
- Core progression remains playable without purchasing these options.

Designed for phones
- Small-screen layouts and touch targets are treated as first-class UI constraints.
- Reduced-motion and battery-saver policies reduce decorative animation where appropriate.
- Game progress is stored locally and the canonical save is included in Android backup/device-transfer rules.

Build. Automate. Ascend. Push from ZERO → EMPIRE.

## Store classification notes

- Category candidate: Game / Simulation or Game / Casual. Final category must be selected in Play Console after reviewing the live catalog positioning.
- Contains ads: Yes, when consent and runtime policy allow ads.
- In-app purchases: Yes.
- Gambling: No gambling mechanic should be represented in store copy.
- Multiplayer: Do not claim multiplayer unless a real multiplayer feature is added.
- Offline: Do not market the app as fully offline; advertising, consent, billing and other service integrations can require network access.

## Graphic assets

- App icon: Android launcher/adaptive icon is defined in the app resources; export the Play Console 512×512 icon from the final production artwork rather than using an arbitrary screenshot.
- Feature graphic: `marketing/play-store-feature-graphic.svg`, authored at 1024×500.
- Social card: `marketing/social-share-card.svg`; not a substitute for required Play screenshots.
- Phone screenshots: still required from the final RC build. Capture real gameplay rather than mock screens.
- Recommended screenshot coverage: empire/business screen, manager automation, Power Core/permanent progression, era evolution, goals/challenges, store/optional monetization disclosure.

## RC screenshot matrix

Capture the final RC on at least:

| Profile | Target coverage |
| --- | --- |
| Compact phone | ~360dp width or smaller; verify no clipped primary actions |
| Typical phone | ~390–430dp width; primary Play Store screenshot set |
| Tall phone | Verify long content, dialogs and bottom navigation/insets |
| Rotated/recreated Activity | Verify state survives normal configuration recreation |
| Reduced motion / battery saver | Verify decorative motion is reduced without hiding required UI |

Do not claim physical-device validation in release notes unless the build was actually exercised on that device/profile.

## Play Console items that cannot be completed from repository code alone

Before production submission, complete and verify in Play Console:

- production app signing / upload key configuration;
- production `VERSION_CODE` and `VERSION_NAME`;
- production AdMob App ID and rewarded/interstitial unit IDs;
- Play Billing products matching the app catalog;
- privacy policy URL and Data safety form based on the final SDK/runtime behavior;
- ads declaration, content rating and target audience questionnaires;
- final screenshots from the release candidate;
- contact email and store listing locale(s);
- internal/closed testing install of the signed AAB before production rollout.

## Release-copy guardrails

Do not add claims such as “AAA”, “best”, “#1”, guaranteed earnings, exact battery savings, exact FPS, or user-count/review statistics to the Play listing unless they are objectively supportable and compliant with current Play policies. The visual target can be premium, but marketing copy should describe observable features rather than unverifiable quality claims.
