package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class CinematicRuntimeTransitionPolicyTest {
    @Test fun compactScreensUseShorterImpact() {
        assertEquals(472, cinematicTransitionDurationMillis(compactScreen = true))
        assertEquals(552, cinematicTransitionDurationMillis(compactScreen = false))
    }

    @Test fun reducedMotionNeverRendersImpact() {
        assertFalse(shouldRenderCinematicTransition(reducedMotion = true, phase = 0f))
        assertFalse(shouldRenderCinematicTransition(reducedMotion = true, phase = .5f))
    }

    @Test fun completedImpactLeavesNoIdleCanvas() {
        assertTrue(shouldRenderCinematicTransition(reducedMotion = false, phase = .5f))
        assertFalse(shouldRenderCinematicTransition(reducedMotion = false, phase = .985f))
        assertFalse(shouldRenderCinematicTransition(reducedMotion = false, phase = 1f))
    }
}
