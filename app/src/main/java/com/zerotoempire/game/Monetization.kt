package com.zerotoempire.game

/**
 * Provider-neutral monetization contract. Gameplay never depends directly on an ad SDK.
 * This keeps rewards testable and lets providers be replaced without touching the economy.
 */
interface RewardedAdGateway {
    fun isReady(): Boolean
    fun show(placement: RewardPlacement, onReward: () -> Unit, onClosed: () -> Unit = {})
}

enum class RewardPlacement {
    DOUBLE_OFFLINE_EARNINGS,
    PROFIT_BOOST,
    DAILY_BONUS,
    EVENT_BONUS
}

interface PurchaseGateway {
    suspend fun purchase(product: StoreProduct): PurchaseResult
    suspend fun restore(): Set<StoreProduct>
}

enum class StoreProduct(val productId: String) {
    REMOVE_ADS("remove_ads_lifetime"),
    STARTER_PACK("starter_pack"),
    GEM_PACK_SMALL("gems_small"),
    GEM_PACK_MEDIUM("gems_medium")
}

sealed interface PurchaseResult {
    data object Success : PurchaseResult
    data object Cancelled : PurchaseResult
    data class Failed(val reason: String) : PurchaseResult
}

data class MonetizationState(
    val adsRemoved: Boolean = false,
    val starterPackOwned: Boolean = false
)
