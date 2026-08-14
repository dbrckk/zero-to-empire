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

    init {
        MobileAds.initialize(context) { preload() }
    }

    override fun preload() {
        if (loading || rewardedAd != null || BuildConfig.REWARDED_AD_UNIT_ID.isBlank()) return
        loading = true
        RewardedAd.load(
            context,
            BuildConfig.REWARDED_AD_UNIT_ID,
            AdRequest.Builder().build(),
            object : RewardedAdLoadCallback() {
                override fun onAdLoaded(ad: RewardedAd) {
                    loading = false
                    rewardedAd = ad
                }

                override fun onAdFailedToLoad(error: LoadAdError) {
                    loading = false
                    rewardedAd = null
                }
            }
        )
    }

    override fun isReady(): Boolean = rewardedAd != null

    override fun show(
        activity: Activity,
        placement: RewardPlacement,
        onReward: () -> Unit,
        onClosed: () -> Unit
    ) {
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
