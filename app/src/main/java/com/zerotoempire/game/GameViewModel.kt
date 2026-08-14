package com.zerotoempire.game

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import java.time.LocalDate

class GameViewModel(application: Application) : AndroidViewModel(application) {
    private val repository = GameRepository(application.applicationContext)

    private val _state = MutableStateFlow(GameState())
    val state: StateFlow<GameState> = _state.asStateFlow()

    private val _meta = MutableStateFlow(PlayerMeta())
    val meta: StateFlow<PlayerMeta> = _meta.asStateFlow()

    private val _offlineReward = MutableStateFlow<OfflineReward?>(null)
    val offlineReward: StateFlow<OfflineReward?> = _offlineReward.asStateFlow()

    private var loaded = false
    private var saveJob: Job? = null

    init {
        viewModelScope.launch {
            val save = repository.load()
            var restored = save.state
            val reward = OfflineProgress.calculate(restored, save.lastSeenMillis)
            if (reward.eligible) {
                restored = restored.copy(cash = restored.cash + reward.cash, lifetimeCash = restored.lifetimeCash + reward.cash)
                _offlineReward.value = reward
            }
            _state.value = restored
            _meta.value = save.meta.copy(gems = restored.gems, boostEndsAtMillis = restored.boostEndsAtMillis)
            loaded = true

            launch {
                while (true) {
                    delay(100L)
                    val s = _state.value
                    val gain = s.incomePerSecond / 10.0
                    if (gain > 0) _state.value = s.copy(cash = s.cash + gain, lifetimeCash = s.lifetimeCash + gain)
                }
            }

            launch {
                while (true) {
                    delay(5_000L)
                    persistNow()
                }
            }
        }
    }

    fun dismissOfflineReward() { _offlineReward.value = null }

    fun canClaimDaily(): Boolean = _meta.value.lastDailyClaimEpochDay != LocalDate.now().toEpochDay()

    fun claimDaily(): RewardDay? {
        val today = LocalDate.now().toEpochDay()
        val meta = _meta.value
        if (meta.lastDailyClaimEpochDay == today) return null
        val nextStreak = if (meta.lastDailyClaimEpochDay == today - 1) meta.streakDays + 1 else 1
        val reward = LoginCalendar.rewardFor(nextStreak)
        val s = _state.value
        val boostBase = maxOf(System.currentTimeMillis(), s.boostEndsAtMillis)
        val boostEnd = if (reward.multiplierMinutes > 0) boostBase + reward.multiplierMinutes * 60_000L else s.boostEndsAtMillis
        _state.value = s.copy(gems = s.gems + reward.gems, boostEndsAtMillis = boostEnd)
        _meta.value = meta.copy(gems = _state.value.gems, streakDays = nextStreak, lastDailyClaimEpochDay = today, boostEndsAtMillis = boostEnd)
        scheduleSave()
        return reward
    }

    fun missions(): List<Mission> = Progression.missions(_state.value, _meta.value)
    fun achievements(): List<Achievement> = Progression.achievements(_state.value, _meta.value)

    fun claimMission(id: String): Boolean {
        val mission = missions().firstOrNull { it.id == id } ?: return false
        if (!mission.completed || mission.claimed) return false
        _state.value = _state.value.copy(gems = _state.value.gems + mission.rewardGems)
        _meta.value = _meta.value.copy(gems = _state.value.gems, claimedMissionIds = _meta.value.claimedMissionIds + id)
        scheduleSave()
        return true
    }

    fun claimAchievement(id: String): Boolean {
        val achievement = achievements().firstOrNull { it.id == id } ?: return false
        if (!achievement.unlocked || achievement.claimed) return false
        _state.value = _state.value.copy(gems = _state.value.gems + achievement.rewardGems)
        _meta.value = _meta.value.copy(gems = _state.value.gems, claimedAchievementIds = _meta.value.claimedAchievementIds + id)
        scheduleSave()
        return true
    }

    fun tap() {
        val s = _state.value
        _state.value = s.copy(cash = s.cash + s.tapValue, lifetimeCash = s.lifetimeCash + s.tapValue)
        _meta.value = _meta.value.copy(totalTaps = _meta.value.totalTaps + 1)
        scheduleSave()
    }

    fun buy(id: Int) {
        val s = _state.value
        val b = s.businesses.firstOrNull { it.id == id } ?: return
        if (s.cash < b.nextCost) return
        _state.value = s.copy(cash = s.cash - b.nextCost, businesses = s.businesses.map { if (it.id == id) it.copy(level = it.level + 1) else it })
        _meta.value = _meta.value.copy(totalPurchases = _meta.value.totalPurchases + 1)
        scheduleSave()
    }

    fun hireManager(businessId: Int): Boolean {
        val s = _state.value
        val manager = Managers.catalog.firstOrNull { it.businessId == businessId } ?: return false
        if (businessId in s.hiredManagerIds || s.cash < manager.cost) return false
        _state.value = s.copy(cash = s.cash - manager.cost, hiredManagerIds = s.hiredManagerIds + businessId)
        scheduleSave()
        return true
    }

    fun buyUpgrade(id: String): Boolean {
        val s = _state.value
        val u = Upgrades.catalog.firstOrNull { it.id == id } ?: return false
        val rank = s.upgradeRanks[id] ?: 0
        if (rank >= u.maxRank || s.gems < u.gemCost) return false
        _state.value = s.copy(gems = s.gems - u.gemCost, upgradeRanks = s.upgradeRanks + (id to rank + 1))
        syncMetaCurrency(); scheduleSave(); return true
    }

    fun grantGems(amount: Int) { if (amount > 0) { _state.value = _state.value.copy(gems = _state.value.gems + amount); syncMetaCurrency(); scheduleSave() } }

    fun activateProfitBoost(minutes: Int = 10) {
        val s = _state.value
        val base = maxOf(System.currentTimeMillis(), s.boostEndsAtMillis)
        _state.value = s.copy(boostEndsAtMillis = base + minutes * 60_000L)
        _meta.value = _meta.value.copy(boostEndsAtMillis = _state.value.boostEndsAtMillis)
        scheduleSave()
    }

    fun prestige() {
        val s = _state.value
        val totalReward = Progression.prestigeReward(s.lifetimeCash)
        if (totalReward - s.prestigePoints <= 0) return
        _state.value = GameState(prestigePoints = totalReward, gems = s.gems, upgradeRanks = s.upgradeRanks)
        _meta.value = _meta.value.copy(prestigeCount = _meta.value.prestigeCount + 1)
        scheduleSave()
    }

    private fun syncMetaCurrency() { _meta.value = _meta.value.copy(gems = _state.value.gems) }
    private fun scheduleSave() { if (loaded) { saveJob?.cancel(); saveJob = viewModelScope.launch { delay(350L); persistNow() } } }
    private suspend fun persistNow() { if (loaded) repository.save(_state.value, _meta.value) }

    override fun onCleared() {
        if (loaded) { val s = _state.value; val m = _meta.value; viewModelScope.launch { repository.save(s, m) } }
        super.onCleared()
    }
}
