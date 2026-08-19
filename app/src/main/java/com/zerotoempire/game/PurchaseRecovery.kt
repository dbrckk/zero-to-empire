package com.zerotoempire.game

/** Pure purchase-recovery rules kept separate so Billing edge cases remain unit-testable. */
object PurchaseRecovery {
    fun extraConsumableGems(products: List<StoreProduct>): Int {
        val extraSmall = (products.count { it == StoreProduct.GEM_PACK_SMALL } - 1).coerceAtLeast(0)
        val extraMedium = (products.count { it == StoreProduct.GEM_PACK_MEDIUM } - 1).coerceAtLeast(0)
        return extraSmall * 120 + extraMedium * 650
    }

    /** Consumables are transactional: only one restore waiter may receive them after consumption. */
    fun deliveryForWaiter(products: List<StoreProduct>, waiterIndex: Int): List<StoreProduct> =
        if (waiterIndex == 0) products else products.filterNot { it.consumable }
}

/**
 * List overload used by Billing restore. The existing Set member restores permanent entitlements,
 * Starter Pack, and one occurrence of each recovered consumable. We then credit only duplicate
 * consumable transactions that a Set cannot represent.
 */
fun GameViewModel.applyEntitlements(products: List<StoreProduct>) {
    applyEntitlements(products.toSet())
    val extraGems = PurchaseRecovery.extraConsumableGems(products)
    if (extraGems > 0) grantGems(extraGems)
}
