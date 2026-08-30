package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Test

class PurchaseRecoveryTest {
    @Test
    fun duplicatePurchaseTokensAreRecoveredExactlyOnce() {
        data class Transaction(val token: String, val product: StoreProduct)
        val transactions = listOf(
            Transaction("token-a", StoreProduct.GEM_PACK_SMALL),
            Transaction("token-a", StoreProduct.GEM_PACK_SMALL),
            Transaction("token-b", StoreProduct.GEM_PACK_SMALL)
        )

        assertEquals(
            listOf(transactions[0], transactions[2]),
            PurchaseRecovery.distinctTransactions(transactions, Transaction::token)
        )
    }

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

    @Test
    fun pathologicalRecoveryValueSaturatesInsteadOfOverflowing() {
        assertEquals(
            Int.MAX_VALUE,
            PurchaseRecovery.recoveredConsumableGemValue(Int.MAX_VALUE, Int.MAX_VALUE)
        )
    }

    @Test
    fun recoveryValueRejectsNegativeCounts() {
        assertEquals(0, PurchaseRecovery.recoveredConsumableGemValue(-1, -1))
    }

    @Test
    fun concurrentRestoreWaitersCannotDoubleCreditConsumables() {
        val products = listOf(
            StoreProduct.REMOVE_ADS,
            StoreProduct.STARTER_PACK,
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_SMALL,
            StoreProduct.GEM_PACK_MEDIUM
        )

        assertEquals(products, PurchaseRecovery.deliveryForWaiter(products, 0))
        assertEquals(
            listOf(StoreProduct.REMOVE_ADS, StoreProduct.STARTER_PACK),
            PurchaseRecovery.deliveryForWaiter(products, 1)
        )
        assertEquals(
            listOf(StoreProduct.REMOVE_ADS, StoreProduct.STARTER_PACK),
            PurchaseRecovery.deliveryForWaiter(products, 2)
        )
    }
}
