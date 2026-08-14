package com.zerotoempire.game

/** Small analytics boundary: no vendor SDK leaks into gameplay code. */
interface GameAnalytics {
    fun track(event: GameEvent)
}

sealed interface GameEvent {
    data class SessionStarted(val returningPlayer: Boolean) : GameEvent
    data class BusinessPurchased(val businessId: Int, val newLevel: Int) : GameEvent
    data class ManagerHired(val businessId: Int) : GameEvent
    data class PrestigeUsed(val pointsEarned: Int, val runSeconds: Long) : GameEvent
    data class RewardedAdCompleted(val placement: RewardPlacement) : GameEvent
    data class MissionClaimed(val missionId: String) : GameEvent
    data class TutorialStep(val step: Int) : GameEvent
}

object NoOpAnalytics : GameAnalytics {
    override fun track(event: GameEvent) = Unit
}
