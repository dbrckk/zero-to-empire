package com.zerotoempire.game

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class RewardRequestGateTest {
    @Test fun requestIsOneShotUntilReleased() {
        val gate = RewardRequestGate()
        assertTrue(gate.request())
        assertFalse(gate.request())
        gate.release()
        assertTrue(gate.request())
    }

    @Test fun consumeRequiresPendingRequestAndIsOneShot() {
        val gate = RewardRequestGate()
        assertFalse(gate.consume())
        assertTrue(gate.request())
        assertTrue(gate.consume())
        assertFalse(gate.consume())
        assertFalse(gate.isPending())
    }

    @Test fun releaseIsIdempotent() {
        val gate = RewardRequestGate()
        gate.release()
        gate.release()
        assertFalse(gate.isPending())
        assertTrue(gate.request())
        gate.release()
        gate.release()
        assertFalse(gate.isPending())
    }
}
