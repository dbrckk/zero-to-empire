package com.zerotoempire.game

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class UpgradeProgressionTest {
    @Test
    fun firstTierIsAvailableOnFreshSave() {
        val nodes = UpgradeProgression.nodes(GameState())
        assertTrue(nodes.isNotEmpty())
        assertEquals(UpgradeNodeState.AVAILABLE, nodes.first().state)
        if (nodes.size > 1) assertEquals(UpgradeNodeState.LOCKED, nodes[1].state)
    }

    @Test
    fun investingUnlocksNextTierWithoutNewSaveFields() {
        val first = Upgrades.catalog.first()
        val state = GameState(upgradeRanks = mapOf(first.id to 1))
        val nodes = UpgradeProgression.nodes(state)
        assertEquals(UpgradeNodeState.IN_PROGRESS, nodes[0].state)
        if (nodes.size > 1) assertEquals(UpgradeNodeState.AVAILABLE, nodes[1].state)
    }

    @Test
    fun masteredUpgradeReportsFullProgress() {
        val first = Upgrades.catalog.first()
        val state = GameState(upgradeRanks = mapOf(first.id to first.maxRank))
        val node = UpgradeProgression.nodes(state).first()
        assertEquals(UpgradeNodeState.MASTERED, node.state)
        assertEquals(1f, node.progress)
    }

    @Test
    fun overallProgressIsBounded() {
        val progress = UpgradeProgression.overallProgress(GameState())
        assertTrue(progress in 0f..1f)
    }
}
