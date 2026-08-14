package com.zerotoempire.game

import android.app.Activity

/** Provider-neutral contracts: gameplay code never talks directly to billing or ad SDKs. */
interface RewardedAdGateway {
    fun preload()
    fun isReady(): Boolean
    fun show(activity: Activity, placement: RewardPlacement, onReward: () -> Unit, onClosed: () -> Unit = {})
}

enum class RewardPlacement {
    DOUBLE_OFFLINE_EARNINGS,
    PROFIT_BOOST,
    DAILY_BONUS,
    EVENT_BONUS
}

interface PurchaseGateway {
    fun connect()
    fun disconnect()
    fun purchase(activity: Activity, product: StoreProduct, onResult: (PurchaseResult) -> Unit)
    fun restore(onResult: (Set<StoreProduct>) -> Unit)
}

enum class StoreProduct(val productId: String, val consumable: Boolean) {
    REMOVE_ADS("remove_ads_lifetime", false),
    STARTER_PACK("starter_pack", false),
    GEM_PACK_SMALL("gems_small", true),
    GEM_PACK_MEDIUM("gems_medium", true)
}

sealed interface PurchaseResult {
    data class Success(val product: StoreProduct) : PurchaseResult
    data object Cancelled : PurchaseResult
    data object Pending : PurchaseResult
    data class Failed(val reason: String) : PurchaseResult
}

data class MonetizationState(
    val adsRemoved: Boolean = false,
    val starterPackOwned: Boolean = false,
    val billingReady: Boolean = false,
    val rewardedReady: Boolean = false
)
