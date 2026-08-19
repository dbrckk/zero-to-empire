package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Test
import java.time.ZoneId
import java.time.ZonedDateTime

class OfflineTemporalTest {
    private val zone = ZoneId.of("Europe/Paris")

    private fun managedState(boostEndsAtMillis: Long = 0L): GameState {
        val first = defaultBusinesses().first().copy(level = 100)
        return GameState(
            businesses = defaultBusinesses().map { if (it.id == first.id) first else it },
            hiredManagerIds = setOf(first.id),
            boostEndsAtMillis = boostEndsAtMillis
        )
    }

    @Test
    fun boostOnlyAppliesUntilItsActualExpiry() {
        val start = ZonedDateTime.of(2026, 8, 17, 10, 0, 0, 0, zone).toInstant().toEpochMilli() // Monday
        val end = start + 3_600_000L
        val boostEnd = start + 1_800_000L
        val state = managedState(boostEnd)

        val reward = OfflineProgress.calculate(state, start, end, zone)
        val expected = state.automatedBaseIncomePerSecond * ((1_800.0 * 2.0) + 1_800.0) * .75

        assertEquals(expected, reward.cash, expected * 1e-9)
    }

    @Test
    fun liveEventMultiplierChangesAtLocalMidnight() {
        val start = ZonedDateTime.of(2026, 8, 21, 23, 30, 0, 0, zone).toInstant().toEpochMilli() // Friday
        val end = start + 3_600_000L // Saturday 00:30
        val state = managedState()

        val reward = OfflineProgress.calculate(state, start, end, zone)
        val expected = state.automatedBaseIncomePerSecond * ((1_800.0 * 2.0) + (1_800.0 * 1.5)) * .75

        assertEquals(expected, reward.cash, expected * 1e-9)
    }
}
