package com.zerotoempire.game

import android.app.Activity
import com.google.android.ump.ConsentInformation
import com.google.android.ump.ConsentRequestParameters
import com.google.android.ump.UserMessagingPlatform
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

/** Central privacy gate for every ad format. */
class PrivacyConsentManager(private val activity: Activity) {
    private val consentInformation: ConsentInformation = UserMessagingPlatform.getConsentInformation(activity)

    fun gather(onComplete: (canRequestAds: Boolean, error: String?) -> Unit) {
        val params = ConsentRequestParameters.Builder().build()
        consentInformation.requestConsentInfoUpdate(
            activity,
            params,
            {
                UserMessagingPlatform.loadAndShowConsentFormIfRequired(activity) { formError ->
                    publish(consentInformation.canRequestAds())
                    onComplete(consentInformation.canRequestAds(), formError?.message)
                }
            },
            { requestError ->
                publish(consentInformation.canRequestAds())
                onComplete(consentInformation.canRequestAds(), requestError.message)
            }
        )
    }

    fun canRequestAds(): Boolean = consentInformation.canRequestAds()

    fun isPrivacyOptionsRequired(): Boolean =
        consentInformation.privacyOptionsRequirementStatus == ConsentInformation.PrivacyOptionsRequirementStatus.REQUIRED

    fun showPrivacyOptions(onClosed: (String?) -> Unit = {}) {
        UserMessagingPlatform.showPrivacyOptionsForm(activity) { error ->
            publish(consentInformation.canRequestAds())
            onClosed(error?.message)
        }
    }

    private fun publish(value: Boolean) { _adsAllowed.value = value }

    companion object {
        private val _adsAllowed = MutableStateFlow(false)
        val adsAllowed: StateFlow<Boolean> = _adsAllowed.asStateFlow()
    }
}
