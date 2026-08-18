package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PlayableFlowTest {

    @Test
    fun freshPlayerCanBuyFirstAssetAndStartPassiveIncome() {
        val initial = GameState()
        val first = initial.businesses.first()
        val quote = BulkPurchase.quote(first, initial.cash, BuyMode.X1)

        assertEquals(1, quote.count)
        assertTrue(quote.totalCost <= initial.cash)

        val purchased = first.copy(level = first.level + quote.count)
        val next = initial.copy(
            cash = initial.cash - quote.totalCost,
            businesses = initial.businesses.map { if (it.id == purchased.id) purchased else it }
        )

        assertEquals(1, next.businesses.first().level)
        assertTrue(next.incomePerSecond > 0.0)
        assertTrue(next.tapValue > 0.0)
    }

    @Test
    fun managerHireActuallyImprovesAssociatedProduction() {
        val business = defaultBusinesses().first().copy(level = 100)
        val withoutManager = GameState(
            cash = 10_000.0,
            lifetimeCash = 10_000.0,
            businesses = defaultBusinesses().map { if (it.id == business.id) business else it }
        )
        val withManager = withoutManager.copy(hiredManagerIds = setOf(business.id))

        assertTrue(withManager.businessIncome(business) > withoutManager.businessIncome(business))
        assertTrue(withManager.incomePerSecond > withoutManager.incomePerSecond)
    }

    @Test
    fun offlineProgressPaysPositiveCappedIncomeForAutomatedEmpire() {
        val business = defaultBusinesses().first().copy(level = 100)
        val state = GameState(
            businesses = defaultBusinesses().map { if (it.id == business.id) business else it },
            hiredManagerIds = setOf(business.id)
        )
        val lastSeen = 1_000_000L
        val nineHoursLater = lastSeen + 9L * 60L * 60L * 1000L
        val reward = OfflineProgress.calculate(state, lastSeen, nineHoursLater)

        assertTrue(reward.eligible)
        assertEquals(8L * 60L * 60L, reward.paidSeconds)
        assertTrue(reward.cash > 0.0)
    }

    @Test
    fun prestigeBecomesAvailableAndCreatesPermanentPower() {
        val lifetime = 1.0e12
        val reward = Progression.prestigeReward(lifetime)
        assertTrue(reward > 0)

        val before = GameState(lifetimeCash = lifetime)
        val after = GameState(prestigePoints = reward)

        assertTrue(after.prestigeMultiplier > before.prestigeMultiplier)
    }

    @Test
    fun bulkMilestonePurchaseTargetsNextPowerSpike() {
        val business = defaultBusinesses().first().copy(level = 24)
        val required = BulkPurchase.cost(business, 1)
        val quote = BulkPurchase.quote(business, required, BuyMode.MILESTONE)

        assertEquals(1, quote.count)
        assertEquals(25, business.level + quote.count)
        assertTrue(25 in BulkPurchase.crossedMilestones(business.level, business.level + quote.count))
    }

    @Test
    fun endgameContentRemainsEconomicallyFiniteAtUnlockScale() {
        val businesses = defaultBusinesses().mapIndexed { index, business ->
            business.copy(level = if (index <= 13) 25 else 0)
        }
        val state = GameState(
            cash = 1.0e32,
            lifetimeCash = 1.0e32,
            businesses = businesses,
            hiredManagerIds = Managers.catalog.map { it.businessId }.toSet(),
            prestigePoints = 250
        )

        assertEquals(14, state.businesses.size)
        assertTrue(state.incomePerSecond.isFinite())
        assertTrue(state.incomePerSecond > 0.0)
        assertTrue(state.transcendenceMultiplier >= 1.0)
    }
}
