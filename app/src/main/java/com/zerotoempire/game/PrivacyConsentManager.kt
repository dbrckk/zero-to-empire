package com.zerotoempire.game

import android.app.Activity
import com.google.android.ump.ConsentInformation
import com.google.android.ump.ConsentRequestParameters
import com.google.android.ump.UserMessagingPlatform

/**
 * Central privacy gate for ad requests.
 * Consent information is refreshed at every launch before ads are preloaded.
 */
class PrivacyConsentManager(private val activity: Activity) {
    private val consentInformation: ConsentInformation =
        UserMessagingPlatform.getConsentInformation(activity)

    fun gather(onComplete: (canRequestAds: Boolean, error: String?) -> Unit) {
        val params = ConsentRequestParameters.Builder().build()
        consentInformation.requestConsentInfoUpdate(
            activity,
            params,
            {
                UserMessagingPlatform.loadAndShowConsentFormIfRequired(activity) { formError ->
                    onComplete(
                        consentInformation.canRequestAds(),
                        formError?.message
                    )
                }
            },
            { requestError ->
                // canRequestAds() can still be true when a previous valid decision exists.
                onComplete(consentInformation.canRequestAds(), requestError.message)
            }
        )
    }

    fun canRequestAds(): Boolean = consentInformation.canRequestAds()

    fun isPrivacyOptionsRequired(): Boolean =
        consentInformation.privacyOptionsRequirementStatus ==
            ConsentInformation.PrivacyOptionsRequirementStatus.REQUIRED

    fun showPrivacyOptions(onClosed: (String?) -> Unit = {}) {
        UserMessagingPlatform.showPrivacyOptionsForm(activity) { error ->
            onClosed(error?.message)
        }
    }
}
