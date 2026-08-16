package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class EndgameProgressionTest {
    @Test fun multiplier_is_one_before_endgame() {
        assertEquals(1.0, EndgameProgression.transcendenceMultiplier(1e15), 0.000001)
    }

    @Test fun transcendence_multiplier_is_monotonic_and_bounded() {
        val values = listOf(1e18, 1e21, 1e24, 1e27, 1e30).map(EndgameProgression::transcendenceMultiplier)
        values.zipWithNext().forEach { (a, b) -> assertTrue(b > a) }
        assertTrue(values.last().isFinite())
        assertTrue(values.last() < 5.0)
    }

    @Test fun eras_extend_beyond_galactic() {
        assertEquals("GALACTIC", EmpireEras.current(1e18).name)
        assertEquals("INTERGALACTIC", EmpireEras.current(1e21).name)
        assertEquals("COSMIC", EmpireEras.current(1e24).name)
        assertEquals("REALITY ENGINE", EmpireEras.current(1e27).name)
        assertEquals("TRANSCENDENT", EmpireEras.current(1e30).name)
    }

    @Test fun empire_level_tracks_era_catalog() {
        assertEquals(10, GameState(lifetimeCash = 1e30).empireLevel)
    }
}
