package com.zerotoempire.game

import org.junit.Assert.*
import org.junit.Test

class BulkPurchaseTest {
    @Test fun bulkCostMatchesSequentialPurchases() {
        val b = defaultBusinesses().first().copy(level = 12)
        var sequential = 0.0
        repeat(25) { i -> sequential += b.baseCost * Math.pow(1.15, (b.level + i).toDouble()) }
        assertEquals(sequential, BulkPurchase.cost(b, 25), sequential * 1e-10)
    }

    @Test fun maxNeverOverspends() {
        val b = defaultBusinesses()[2].copy(level = 31)
        val cash = BulkPurchase.cost(b, 40) * 0.73
        val quote = BulkPurchase.quote(b, cash, BuyMode.MAX)
        assertTrue(quote.totalCost <= cash)
        assertTrue(BulkPurchase.cost(b, quote.count + 1) > cash)
    }

    @Test fun fixedQuoteKeepsRequestedCount() {
        val b = defaultBusinesses().first()
        val cash = BulkPurchase.cost(b, 25)
        val q = BulkPurchase.quote(b, cash, BuyMode.X25)
        assertEquals(25, q.count)
    }

    @Test fun milestonesCrossedAreDetectedInBulk() {
        assertEquals(listOf(10,25,50), BulkPurchase.crossedMilestones(8, 52))
    }
}
