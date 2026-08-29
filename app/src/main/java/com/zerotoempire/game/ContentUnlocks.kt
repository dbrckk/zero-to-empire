package com.zerotoempire.game

/**
 * Presentation unlocks are deliberately separate from GameState persistence/economy.
 * Existing saves retain every business; the UI simply reveals higher tiers as the empire grows.
 */
object ContentUnlocks {
    private val businessThresholds = mapOf(
        0 to 0.0,
        1 to 40.0,
        2 to 500.0,
        3 to 6_000.0,
        4 to 120_000.0,
        5 to 3_000_000.0,
        6 to 180_000_000.0,
        7 to 18_000_000_000.0,
        8 to 2_500_000_000_000.0,
        9 to 650_000_000_000_000.0,
        10 to 500_000_000_000_000_000.0,
        11 to 2.0e21,
        12 to 8.0e24,
        13 to 3.0e28
    )

    fun thresholdForBusiness(id: Int): Double = businessThresholds[id] ?: Double.POSITIVE_INFINITY

    fun isBusinessVisible(id: Int, lifetimeCash: Double): Boolean =
        lifetimeCash >= thresholdForBusiness(id)

    fun visibleBusinesses(state: GameState): List<Business> =
        state.businesses.filter { isBusinessVisible(it.id, state.lifetimeCash) }

    /**
     * Keeps the manager screen useful on phones by putting the next actionable hires first.
     * This is presentation-only: costs, manager effects, unlock thresholds and saved state are untouched.
     */
    fun visibleManagers(state: GameState): List<Manager> =
        Managers.catalog
            .asSequence()
            .filter { isBusinessVisible(it.businessId, state.lifetimeCash) }
            .sortedWith(
                compareBy<Manager> {
                    when {
                        it.businessId in state.hiredManagerIds -> 2
                        state.cash >= it.cost -> 0
                        else -> 1
                    }
                }.thenBy { it.businessId }
            )
            .toList()

    fun nextHiddenBusiness(state: GameState): Business? =
        state.businesses.firstOrNull { !isBusinessVisible(it.id, state.lifetimeCash) }

    fun progressToNextUnlock(state: GameState): Float {
        val next = nextHiddenBusiness(state) ?: return 1f
        val threshold = thresholdForBusiness(next.id)
        if (!threshold.isFinite() || threshold <= 0.0) return 0f
        val previousThreshold = thresholdForBusiness((next.id - 1).coerceAtLeast(0))
        val span = (threshold - previousThreshold).coerceAtLeast(1.0)
        return ((state.lifetimeCash - previousThreshold) / span).toFloat().coerceIn(0f, 1f)
    }
}
