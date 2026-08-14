package com.zerotoempire.game

import android.content.Context
import android.util.Log

sealed interface GrowthEvent {
    data object SessionStarted : GrowthEvent
    data object OnboardingCompleted : GrowthEvent
    data object FirstAssetPurchased : GrowthEvent
    data object FirstManagerHired : GrowthEvent
    data object FirstPrestige : GrowthEvent
    data object FirstRewardedCompleted : GrowthEvent
    data object StoreOpened : GrowthEvent
    data class PurchaseCompleted(val productId: String) : GrowthEvent
    data class InterstitialShown(val breakPoint: NaturalBreakPoint) : GrowthEvent
}

interface GrowthTelemetry {
    fun track(event: GrowthEvent)
}

class LocalGrowthTelemetry(context: Context) : GrowthTelemetry {
    private val prefs = context.getSharedPreferences("zero_empire_growth_telemetry", Context.MODE_PRIVATE)

    override fun track(event: GrowthEvent) {
        val key = when (event) {
            GrowthEvent.SessionStarted -> null
            GrowthEvent.OnboardingCompleted -> "onboarding_completed"
            GrowthEvent.FirstAssetPurchased -> "first_asset"
            GrowthEvent.FirstManagerHired -> "first_manager"
            GrowthEvent.FirstPrestige -> "first_prestige"
            GrowthEvent.FirstRewardedCompleted -> "first_rewarded"
            GrowthEvent.StoreOpened -> null
            is GrowthEvent.PurchaseCompleted -> null
            is GrowthEvent.InterstitialShown -> null
        }
        if (key != null && prefs.getBoolean(key, false)) return
        if (key != null) prefs.edit().putBoolean(key, true).apply()
        Log.i("ZeroEmpireGrowth", event.toString())
    }
}
