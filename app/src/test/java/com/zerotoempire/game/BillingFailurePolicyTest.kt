package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class BillingFailurePolicyTest {
    @Test
    fun transientFailuresRequestReconnectionWithActionableMessages() {
        val disconnected = BillingFailurePolicy.resolve(BillingFailureKind.SERVICE_DISCONNECTED, "internal", "fallback")
        val unavailable = BillingFailurePolicy.resolve(BillingFailureKind.SERVICE_UNAVAILABLE, "internal", "fallback")
        val network = BillingFailurePolicy.resolve(BillingFailureKind.NETWORK_ERROR, "internal", "fallback")

        assertTrue(disconnected.shouldReconnect)
        assertTrue(unavailable.shouldReconnect)
        assertTrue(network.shouldReconnect)
        assertEquals("Google Play disconnected. Reopen the store and try again.", disconnected.message)
        assertEquals("Google Play is temporarily unavailable. Try again shortly.", unavailable.message)
        assertEquals("Network error while contacting Google Play. Check your connection and try again.", network.message)
    }

    @Test
    fun permanentFailureKeepsUsefulDetailWithoutRequestingRetry() {
        val detailed = BillingFailurePolicy.resolve(BillingFailureKind.OTHER, "Product is unavailable", "fallback")
        val fallback = BillingFailurePolicy.resolve(BillingFailureKind.OTHER, "", "Purchase failed")

        assertFalse(detailed.shouldReconnect)
        assertEquals("Product is unavailable", detailed.message)
        assertEquals("Purchase failed", fallback.message)
    }
}
