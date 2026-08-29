package com.zerotoempire.game

/**
 * Presentation/progression metadata for the permanent upgrade lab.
 * This layer derives entirely from existing upgrade ranks, so old saves remain compatible.
 */
data class UpgradeProgressNode(
    val id: String,
    val tier: Int,
    val rank: Int,
    val maxRank: Int,
    val progress: Float,
    val state: UpgradeNodeState
)

enum class UpgradeNodeState {
    LOCKED,
    AVAILABLE,
    IN_PROGRESS,
    MASTERED
}

object UpgradeProgression {
    const val TIER_COUNT = 4

    /**
     * Upgrade tiers are deliberately derived from catalog order. No new save fields are required.
     * Each tier becomes available after the previous tier has at least one invested rank.
     */
    fun nodes(state: GameState): List<UpgradeProgressNode> {
        val catalog = Upgrades.catalog
        return catalog.mapIndexed { index, upgrade ->
            val rank = (state.upgradeRanks[upgrade.id] ?: 0).coerceIn(0, upgrade.maxRank)
            val previousUnlocked = index == 0 || run {
                val previous = catalog[index - 1]
                (state.upgradeRanks[previous.id] ?: 0) > 0
            }
            val nodeState = when {
                rank >= upgrade.maxRank -> UpgradeNodeState.MASTERED
                rank > 0 -> UpgradeNodeState.IN_PROGRESS
                previousUnlocked -> UpgradeNodeState.AVAILABLE
                else -> UpgradeNodeState.LOCKED
            }
            UpgradeProgressNode(
                id = upgrade.id,
                tier = index + 1,
                rank = rank,
                maxRank = upgrade.maxRank,
                progress = if (upgrade.maxRank <= 0) 1f else rank.toFloat() / upgrade.maxRank.toFloat(),
                state = nodeState
            )
        }
    }

    fun overallProgress(state: GameState): Float {
        val nodes = nodes(state)
        val totalRanks = nodes.sumOf { it.maxRank }
        if (totalRanks <= 0) return 1f
        return (nodes.sumOf { it.rank }.toFloat() / totalRanks.toFloat()).coerceIn(0f, 1f)
    }

    fun masteredCount(state: GameState): Int = nodes(state).count { it.state == UpgradeNodeState.MASTERED }

    fun unlockedTier(state: GameState): Int = nodes(state)
        .filter { it.state != UpgradeNodeState.LOCKED }
        .maxOfOrNull { it.tier }
        ?: 1
}
