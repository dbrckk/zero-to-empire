package com.zerotoempire.game

import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.lifecycle.compose.collectAsStateWithLifecycle

@Composable
fun SfxRuntime(vm: GameViewModel) {
    val state = vm.state.collectAsStateWithLifecycle().value
    val meta = vm.meta.collectAsStateWithLifecycle().value
    val celebration = vm.celebration.collectAsStateWithLifecycle().value

    val tracker = remember { SfxTracker() }

    LaunchedEffect(meta.totalTaps) {
        if (tracker.initialized && meta.totalTaps > tracker.taps) GameSfxBus.play(PremiumSfxCue.TAP, .72f)
        tracker.taps = meta.totalTaps
    }
    LaunchedEffect(meta.totalPurchases) {
        if (tracker.initialized && meta.totalPurchases > tracker.purchases) GameSfxBus.play(PremiumSfxCue.PURCHASE, .82f)
        tracker.purchases = meta.totalPurchases
    }
    LaunchedEffect(state.hiredManagerIds.size) {
        if (tracker.initialized && state.hiredManagerIds.size > tracker.managers) GameSfxBus.play(PremiumSfxCue.PURCHASE, .92f)
        tracker.managers = state.hiredManagerIds.size
    }
    LaunchedEffect(meta.streakDays, meta.claimedMissionIds.size, meta.claimedAchievementIds.size, meta.claimedChallengeIds.size) {
        val rewardScore = meta.streakDays + meta.claimedMissionIds.size + meta.claimedAchievementIds.size + meta.claimedChallengeIds.size
        if (tracker.initialized && rewardScore > tracker.rewardScore) GameSfxBus.play(PremiumSfxCue.REWARD, .90f)
        tracker.rewardScore = rewardScore
    }
    LaunchedEffect(meta.prestigeCount) {
        if (tracker.initialized && meta.prestigeCount > tracker.prestiges) GameSfxBus.play(PremiumSfxCue.PRESTIGE, 1f)
        tracker.prestiges = meta.prestigeCount
    }
    LaunchedEffect(celebration?.title, celebration?.accent) {
        if (celebration != null && celebration.title != tracker.celebrationTitle) {
            when (celebration.accent) {
                "MILESTONE" -> GameSfxBus.play(PremiumSfxCue.MILESTONE, 1f)
                "NEW ERA", "ERA", "PRESTIGE" -> GameSfxBus.play(PremiumSfxCue.PRESTIGE, 1f)
                else -> GameSfxBus.play(PremiumSfxCue.REWARD, .88f)
            }
            tracker.celebrationTitle = celebration.title
        }
    }

    LaunchedEffect(Unit) { tracker.initialized = true }
}

private class SfxTracker {
    var initialized = false
    var taps = 0L
    var purchases = 0L
    var managers = 0
    var rewardScore = 0
    var prestiges = 0
    var celebrationTitle: String? = null
}
