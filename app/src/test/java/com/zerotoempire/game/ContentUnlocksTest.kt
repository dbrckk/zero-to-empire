package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class ContentUnlocksTest {
    @Test fun firstBusinessIsAlwaysVisible() {
        assertTrue(ContentUnlocks.isBusinessVisible(0, 0.0))
        assertFalse(ContentUnlocks.isBusinessVisible(1, 0.0))
    }

    @Test fun revealThresholdsAreStrictlyIncreasing() {
        val thresholds = defaultBusinesses().map { ContentUnlocks.thresholdForBusiness(it.id) }
        thresholds.zipWithNext().forEach { (a, b) -> assertTrue(b > a) }
    }

    @Test fun everyAssetRevealsBeforeItsBasePurchaseCost() {
        defaultBusinesses().forEach { business ->
            assertTrue(
                "${business.name} reveals too late",
                ContentUnlocks.thresholdForBusiness(business.id) <= business.baseCost
            )
        }
    }

    @Test fun endgameContentStaysHiddenUntilEarned() {
        assertFalse(ContentUnlocks.isBusinessVisible(10, 1e15))
        assertTrue(ContentUnlocks.isBusinessVisible(10, 5e17))
        assertFalse(ContentUnlocks.isBusinessVisible(13, 1e27))
        assertTrue(ContentUnlocks.isBusinessVisible(13, 3e28))
    }

    @Test fun managersFollowTheirBusinessReveal() {
        val early = GameState(lifetimeCash = 10.0)
        assertEquals(listOf(0), ContentUnlocks.visibleManagers(early).map { it.businessId })
    }

    @Test fun affordableUnhiredManagersArePrioritizedForPhoneUsability() {
        val state = GameState(
            cash = 600_000.0,
            lifetimeCash = 600_000.0,
            hiredManagerIds = setOf(0)
        )

        assertEquals(
            listOf(1, 2, 3, 4, 0),
            ContentUnlocks.visibleManagers(state).map { it.businessId }
        )
    }

    @Test fun managerPrioritizationNeverRevealsLockedContent() {
        val state = GameState(cash = Double.MAX_VALUE, lifetimeCash = 10.0)
        assertEquals(listOf(0), ContentUnlocks.visibleManagers(state).map { it.businessId })
    }

    @Test fun fullyProgressedEmpireHasNoHiddenBusiness() {
        val state = GameState(lifetimeCash = 1e31)
        assertNull(ContentUnlocks.nextHiddenBusiness(state))
        assertEquals(1f, ContentUnlocks.progressToNextUnlock(state))
    }
}
