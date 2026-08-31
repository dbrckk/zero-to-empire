package com.zerotoempire.game

import android.app.Activity
import android.content.Context
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.FullScreenContentCallback
import com.google.android.gms.ads.LoadAdError
import com.google.android.gms.ads.MobileAds
import com.google.android.gms.ads.rewarded.RewardedAd
import com.google.android.gms.ads.rewarded.RewardedAdLoadCallback

class AdMobRewardedGateway(private val context: Context) : RewardedAdGateway {
    @Volatile private var rewardedAd: RewardedAd? = null
    @Volatile private var loading = false
    @Volatile private var mobileAdsReady = false
    @Volatile private var initializing = false
    @Volatile private var enabled = false
    @Volatile private var requestGeneration = 0L

    @Synchronized
    override fun setEnabled(enabled: Boolean) {
        if (this.enabled == enabled) return
        this.enabled = enabled
        if (!enabled) {
            requestGeneration += 1L
            rewardedAd = null
            loading = false
        }
    }

    /**
     * Preload is intentionally the first point that may initialize the ads SDK.
     * CommerceRoot only enables this gateway after the privacy gate allows ad requests.
     */
    @Synchronized
    override fun preload() {
        if (!enabled || loading || rewardedAd != null || BuildConfig.REWARDED_AD_UNIT_ID.isBlank()) return
        if (!mobileAdsReady) {
            if (initializing) return
            initializing = true
            val generation = requestGeneration
            MobileAds.initialize(context) {
                synchronized(this) {
                    initializing = false
                    mobileAdsReady = true
                }
                if (enabled && generation == requestGeneration) preload()
            }
            return
        }

        loading = true
        val generation = requestGeneration
        RewardedAd.load(
            context,
            BuildConfig.REWARDED_AD_UNIT_ID,
            AdRequest.Builder().build(),
            object : RewardedAdLoadCallback() {
                override fun onAdLoaded(ad: RewardedAd) {
                    if (!enabled || generation != requestGeneration) return
                    loading = false
                    rewardedAd = ad
                }

                override fun onAdFailedToLoad(error: LoadAdError) {
                    if (generation != requestGeneration) return
                    loading = false
                    rewardedAd = null
                }
            }
        )
    }

    override fun isReady(): Boolean = enabled && rewardedAd != null

    override fun show(
        activity: Activity,
        placement: RewardPlacement,
        onReward: () -> Unit,
        onClosed: () -> Unit
    ) {
        if (!enabled) {
            onClosed()
            return
        }
        val ad = rewardedAd ?: run {
            preload()
            onClosed()
            return
        }
        rewardedAd = null
        var rewarded = false
        ad.fullScreenContentCallback = object : FullScreenContentCallback() {
            override fun onAdDismissedFullScreenContent() {
                preload()
                onClosed()
            }

            override fun onAdFailedToShowFullScreenContent(adError: com.google.android.gms.ads.AdError) {
                preload()
                onClosed()
            }
        }
        ad.show(activity) {
            if (!rewarded) {
                rewarded = true
                onReward()
            }
        }
    }
}
