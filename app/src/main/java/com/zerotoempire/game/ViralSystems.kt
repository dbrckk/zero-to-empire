package com.zerotoempire.game

data class ShareMilestone(
    val id: String,
    val headline: String,
    val body: String,
    val minimumLifetimeCash: Double,
    val rewardGems: Int
)

object ViralMilestones {
    val catalog = listOf(
        ShareMilestone("million", "I BUILT MY FIRST MILLION", "Started with $10. Now the empire begins.", 1e6, 3),
        ShareMilestone("billion", "BILLIONAIRE EMPIRE", "My idle empire just crossed $1B.", 1e9, 5),
        ShareMilestone("trillion", "THE TRILLION CLUB", "This economy is officially out of control.", 1e12, 8),
        ShareMilestone("planet", "PLANETARY TYCOON", "Earth was only the tutorial.", 1e15, 12),
        ShareMilestone("galaxy", "GALACTIC ECONOMY", "I turned nothing into a galactic empire.", 1e18, 20)
    )

    fun latestUnlocked(lifetimeCash: Double): ShareMilestone? =
        catalog.lastOrNull { lifetimeCash >= it.minimumLifetimeCash }
}

data class ReferralState(val invited: Int = 0, val qualified: Int = 0)

object ReferralRewards {
    fun gemsForQualifiedFriends(count: Int): Int = when {
        count >= 20 -> 500
        count >= 10 -> 200
        count >= 5 -> 75
        count >= 3 -> 30
        count >= 1 -> 10
        else -> 0
    }
}
