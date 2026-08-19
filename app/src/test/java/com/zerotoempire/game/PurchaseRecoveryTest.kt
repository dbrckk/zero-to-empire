package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Test

class PurchaseRecoveryTest {
    @Test
    fun noDuplicateConsumablesNeedNoExtraCredit() {
        val products = listOf(
            StoreProduct.REMOVE_ADS,
            StoreProduct.STARTER_PACK,
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_MEDIUM
        )

        assertEquals(0, PurchaseRecovery.extraConsumableGems(products))
    }

    @Test
    fun duplicateSmallPacksPreserveEveryRecoveredTransaction() {
        val products = listOf(
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_SMALL
        )

        // Existing Set-based entitlement path credits the first 120; this covers the other two.
        assertEquals(240, PurchaseRecovery.extraConsumableGems(products))
    }

    @Test
    fun mixedDuplicatePacksPreserveExactGemValue() {
        val products = listOf(
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_MEDIUM,
            StoreProduct.GEM_PACK_MEDIUM,
            StoreProduct.GEM_PACK_MEDIUM
        )

        assertEquals(120 + 650 + 650, PurchaseRecovery.extraConsumableGems(products))
    }
}
