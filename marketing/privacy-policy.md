# ZERO → EMPIRE — Privacy Policy

**Policy version:** 2026-09-18

This document is the repository source for the public privacy policy used by the ZERO → EMPIRE Android app. The production Play Store listing must link to an active public URL containing materially equivalent text, and the in-app policy must remain consistent with it.

## Overview

ZERO → EMPIRE stores game progress and preferences on the user's device. The current release candidate does not require a developer account and does not send gameplay telemetry to a developer-operated analytics server.

## Advertising and consent

ZERO → EMPIRE uses:

- Google User Messaging Platform (UMP) to request and manage advertising consent where required;
- Google Mobile Ads for rewarded and interstitial advertising.

The app does not request an ad until the consent layer reports that ads may be requested. Rewarded ads are optional. Interstitial ads are limited by the game's frequency policy to natural progression breaks and are disabled for players who own the lifetime remove-ads entitlement.

Google advertising services may process device, advertising, diagnostic and interaction data according to Google's service terms, the user's consent choices, region, and configuration.

## Purchases

In-app purchases are processed through Google Play Billing.

The app receives the product identifiers and transaction tokens required to deliver, acknowledge, consume and restore purchases. ZERO → EMPIRE does not receive the user's full payment-card details.

Current product identifiers:

- `remove_ads_lifetime`
- `starter_pack`
- `gems_small`
- `gems_medium`

## Local game data

The app stores data locally, including:

- game progress and economy state;
- settings and onboarding state;
- purchase-delivery and entitlement markers;
- limited local growth milestones used to avoid repeating first-time events;
- local ad-frequency state.

Eligible save data can participate in Android backup/device transfer according to the user's Android and Google account settings and the app's backup rules.

## Diagnostics and analytics

The current release candidate does not include a third-party developer analytics SDK. Development/gameplay diagnostics use local Android logging and local preferences.

This statement does not mean Google Play, Google Mobile Ads, UMP, or other platform services collect no service data; their SDK/service behavior must be accounted for separately in the Play Console Data safety declaration.

## User choices

Users can:

- use the in-game advertising privacy options when UMP reports that privacy options are required;
- decline optional rewarded ads;
- purchase lifetime removal of non-rewarded ads;
- clear local app data through Android settings;
- uninstall the app.

Platform backups may persist according to Android/Google backup settings even after local app data is removed.

## Third-party services

ZERO → EMPIRE integrates Google services for billing, advertising and consent. These services can process data under Google's own privacy terms and service configuration.

Before every production submission, the developer must re-check the Google Play SDK Index/provider disclosures for the exact SDK versions bundled in that release and update this policy and the Data safety declaration if behavior changes.

## Children and target audience

The target-audience selection is finalized in Google Play Console. This repository policy does not make a child-directed claim. If the production target audience includes children, the app, ad configuration, store declarations and this policy must be reviewed against the additional applicable requirements before release.

## Changes

Material changes to data handling should be reflected in this document and in the in-app policy before a new production release is distributed.

## Contact

Privacy questions and policy corrections can be raised through the public ZERO → EMPIRE GitHub repository issue tracker. The production Play Store listing must also provide the developer contact details required by Google Play.
