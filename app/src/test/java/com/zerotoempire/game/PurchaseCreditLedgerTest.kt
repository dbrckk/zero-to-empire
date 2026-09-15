package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class PurchaseCreditLedgerTest {
    @Test fun blankTransactionIsRejected() {
        val ledger = PurchaseCreditLedger()
        assertFalse(ledger.claim(""))
        assertFalse(ledger.claim("   "))
        assertTrue(ledger.snapshot().isEmpty())
    }

    @Test fun sameTransactionCanOnlyBeClaimedOnce() {
        val ledger = PurchaseCreditLedger()
        assertTrue(ledger.claim("token-a"))
        assertFalse(ledger.claim("token-a"))
        assertEquals(setOf("token-a"), ledger.snapshot())
    }

    @Test fun differentTransactionsForSameSkuRemainIndependent() {
        val ledger = PurchaseCreditLedger()
        assertTrue(ledger.claim("token-a"))
        assertTrue(ledger.claim("token-b"))
        assertEquals(setOf("token-a", "token-b"), ledger.snapshot())
    }

    @Test fun restoredLedgerRejectsPreviouslyCreditedTransaction() {
        val restored = PurchaseCreditLedger(setOf("token-old"))
        assertFalse(restored.claim("token-old"))
        assertTrue(restored.claim("token-new"))
        assertEquals(setOf("token-old", "token-new"), restored.snapshot())
    }
}
