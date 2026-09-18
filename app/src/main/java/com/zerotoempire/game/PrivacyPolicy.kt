package com.zerotoempire.game

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

internal const val PRIVACY_POLICY_VERSION = "2026-09-18"

internal val PRIVACY_POLICY_SECTIONS: List<Pair<String, String>> = listOf(
    "Overview" to
        "ZERO → EMPIRE stores game progress and preferences on your device. The game does not require a developer account and does not send gameplay telemetry to a developer analytics server.",
    "Advertising and consent" to
        "The game uses Google User Messaging Platform to request and manage advertising consent where required. Google Mobile Ads may process device, advertising, diagnostic and interaction data according to Google's terms and your consent choices. Ad requests are disabled until the consent system reports that ads may be requested. Rewarded ads are optional. Interstitial ads, when enabled, are limited to natural progression breaks and can be disabled by the lifetime remove-ads purchase.",
    "Purchases" to
        "In-app purchases are processed by Google Play Billing. ZERO → EMPIRE receives purchase product identifiers and transaction tokens needed to deliver and restore entitlements. The game does not receive your full payment card details.",
    "Local game data" to
        "Progress, settings, purchase-delivery markers and limited local growth milestones are stored on-device. Android backup or device-transfer services may copy eligible local save data according to your Android and Google account settings.",
    "Diagnostics" to
        "The current build uses local Android logging and local preferences for development and gameplay diagnostics. It does not include a third-party developer analytics SDK.",
    "Your choices" to
        "You can use the in-game privacy options when Google requires an advertising privacy choice. You can also clear the app's local data through Android settings. Removing the app may remove local data, although platform backups can persist according to your Android backup settings.",
    "Third-party services" to
        "Google Play Billing, Google Mobile Ads and Google User Messaging Platform are Google services and may process data under Google's own privacy terms. Their behavior can vary by region, consent state and service configuration.",
    "Contact and updates" to
        "This policy applies to the current ZERO → EMPIRE Android release candidate. Material changes to data handling should be reflected here before a new production release. Privacy questions can be raised through the public ZERO → EMPIRE GitHub repository issue tracker."
)

@Composable
internal fun PrivacyPolicyDialog(onDismiss: () -> Unit) {
    AlertDialog(
        onDismissRequest = onDismiss,
        title = { Text("PRIVACY POLICY") },
        text = {
            Column(
                modifier = Modifier
                    .heightIn(max = 520.dp)
                    .verticalScroll(rememberScrollState())
            ) {
                Text("Version: $PRIVACY_POLICY_VERSION")
                PRIVACY_POLICY_SECTIONS.forEach { (heading, body) ->
                    Text("\n$heading\n$body")
                }
            }
        },
        confirmButton = {
            TextButton(onClick = onDismiss) { Text("CLOSE") }
        }
    )
}
