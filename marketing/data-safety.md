# ZERO → EMPIRE — Google Play Data Safety Working Sheet

**Status:** release-candidate working document.  
**Do not copy this into Play Console without re-checking the exact production AAB and current Google SDK provider disclosures.**

Google Play requires developers to account for data behavior from the app **and from third-party SDKs**. This sheet records what the repository can establish and what still requires a production-console/provider check.

## First-party app behavior established by the repository

| Area | Repository behavior | Data Safety implication |
| --- | --- | --- |
| Gameplay save | Stored locally with DataStore/preferences | On-device-only data is not automatically "collected" unless transmitted off device |
| Local growth telemetry | SharedPreferences + Android Log only | No developer-operated analytics transmission in current RC |
| Billing | Google Play Billing; app receives product IDs and transaction tokens | Payment-card details are not accessed by the app |
| Rewarded ads | Google Mobile Ads after UMP permits ad requests | Third-party SDK/provider disclosure must be included |
| Interstitial ads | Google Mobile Ads after UMP permits ad requests; frequency-limited | Third-party SDK/provider disclosure must be included |
| Consent | Google UMP | Third-party SDK/provider disclosure must be included |
| Backup/device transfer | Eligible local save can participate in Android backup rules | Verify whether any Play Console declaration is affected by final backup configuration |

## Production SDK inventory

Verify these exact dependencies from the production commit before submission:

- `com.android.billingclient:billing:9.1.0`
- `com.google.android.gms:play-services-ads:25.4.0`
- `com.google.android.ump:user-messaging-platform:3.2.0`

The final Data Safety form must use the current provider disclosures for those exact versions (or whatever versions are in the final AAB).

## Play Billing note

The app does not read full card/payment credentials. Google Play processes the payment flow. The app receives purchase state, product identifiers and purchase tokens needed for entitlement delivery and recovery.

## Advertising note

Do **not** declare "no data collected" simply because ZERO → EMPIRE has no developer analytics backend. Google Mobile Ads and UMP are third-party SDKs and their provider-documented collection/sharing behavior must be included.

Review, at minimum, provider guidance for categories that may include:

- device or other identifiers;
- app interactions;
- diagnostics;
- advertising data;
- approximate location or other signals if documented by the provider for the final configuration.

The exact Play Console answers must come from the provider disclosures and the final runtime configuration, not from guesses in this repository.

## Security / transport

The Android manifest disables cleartext traffic and the app uses networked Google SDKs over their supported transports. Re-check the merged production manifest before submission.

## Console declarations still requiring human confirmation

Before production review:

- privacy-policy public URL is live and matches `marketing/privacy-policy.md`;
- Data Safety answers match the final AAB and current Google SDK disclosures;
- "Contains ads" is declared;
- in-app purchases are declared;
- target audience is selected;
- content rating is completed;
- production billing products match the four repository product IDs;
- developer contact details are complete;
- signed AAB has been installed through an internal/closed Play testing track.

## Drift rule

Any change to these areas requires a Data Safety/privacy review before release:

- dependencies containing billing, ads, consent, analytics, crash reporting, attribution or social SDKs;
- Android permissions;
- network/backend integrations;
- account creation/login;
- cloud save;
- location, contacts, media, health, financial or other sensitive-data access.
