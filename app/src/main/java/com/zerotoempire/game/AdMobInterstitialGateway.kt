package com.zerotoempire.game

import android.app.Activity
import android.content.Context
import com.google.android.gms.ads.AdError
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.FullScreenContentCallback
import com.google.android.gms.ads.LoadAdError
import com.google.android.gms.ads.interstitial.InterstitialAd
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback

class AdMobInterstitialGateway(private val context: Context) {
    @Volatile private var ad: InterstitialAd? = null
    @Volatile private var loading = false
    @Volatile private var enabled = false
    @Volatile private var requestGeneration = 0L

    fun setEnabled(value: Boolean) {
        if (enabled == value) return
        enabled = value
        if (!value) {
            requestGeneration += 1L
            ad = null
            loading = false
        }
    }

    fun preload() {
        if (!enabled || loading || ad != null || BuildConfig.INTERSTITIAL_AD_UNIT_ID.isBlank()) return
        loading = true
        val generation = requestGeneration
        InterstitialAd.load(
            context,
            BuildConfig.INTERSTITIAL_AD_UNIT_ID,
            AdRequest.Builder().build(),
            object : InterstitialAdLoadCallback() {
                override fun onAdLoaded(interstitialAd: InterstitialAd) {
                    if (!enabled || generation != requestGeneration) return
                    loading = false
                    ad = interstitialAd
                }

                override fun onAdFailedToLoad(error: LoadAdError) {
                    if (generation != requestGeneration) return
                    loading = false
                    ad = null
                }
            }
        )
    }

    fun isReady(): Boolean = enabled && ad != null

    fun show(
        activity: Activity,
        onShown: () -> Unit = {},
        onClosed: () -> Unit = {}
    ) {
        if (!enabled || !activity.canHostFullScreenAd()) {
            onClosed()
            return
        }
        val current = ad ?: run {
            preload()
            onClosed()
            return
        }
        ad = null
        current.fullScreenContentCallback = object : FullScreenContentCallback() {
            override fun onAdShowedFullScreenContent() {
                onShown()
            }

            override fun onAdDismissedFullScreenContent() {
                preload()
                onClosed()
            }

            override fun onAdFailedToShowFullScreenContent(adError: AdError) {
                preload()
                onClosed()
            }
        }
        runCatching { current.show(activity) }
            .onFailure {
                preload()
                onClosed()
            }
    }
}
