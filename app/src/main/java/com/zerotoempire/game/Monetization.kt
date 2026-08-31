package com.zerotoempire.game

import android.app.Activity

/** Provider-neutral contracts: gameplay code never talks directly to billing or ad SDKs. */
interface RewardedAdGateway {
    /**
     * Lets privacy-aware hosts disable ad work immediately. The default keeps test/fake
     * implementations source-compatible while production gateways can actively invalidate loads.
     */
    fun setEnabled(enabled: Boolean) {}
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
    /**
     * Returns every recovered transaction. This is intentionally a List rather than a Set:
     * multiple interrupted purchases of the same consumable must each be credited exactly once.
     */
    fun restore(onResult: (RestoreResult) -> Unit)
}

enum class StoreProduct(val productId: String, val consumable: Boolean) {
    REMOVE_ADS("remove_ads_lifetime", false),
    STARTER_PACK("starter_pack", false),
    GEM_PACK_SMALL("gems_small", true),
    GEM_PACK_MEDIUM("gems_medium", true)
}

/** A one-time Google Play transaction is accepted only when it identifies one exact catalog SKU. */
object StoreProductResolver {
    fun resolve(productIds: List<String>): StoreProduct? {
        val productId = productIds.distinct().singleOrNull() ?: return null
        return StoreProduct.entries.singleOrNull { it.productId == productId }
    }
}

sealed interface PurchaseResult {
    data class Success(val product: StoreProduct) : PurchaseResult
    data object Cancelled : PurchaseResult
    data object Pending : PurchaseResult
    data class Failed(val reason: String) : PurchaseResult
}

sealed interface RestoreResult {
    val products: List<StoreProduct>
    val pendingProducts: Set<StoreProduct>

    data class Success(
        override val products: List<StoreProduct>,
        override val pendingProducts: Set<StoreProduct> = emptySet()
    ) : RestoreResult
    data class Failed(
        val reason: String,
        override val products: List<StoreProduct> = emptyList(),
        override val pendingProducts: Set<StoreProduct> = emptySet()
    ) : RestoreResult
}

data class MonetizationState(
    val adsRemoved: Boolean = false,
    val starterPackOwned: Boolean = false,
    val billingReady: Boolean = false,
    val rewardedReady: Boolean = false
)
