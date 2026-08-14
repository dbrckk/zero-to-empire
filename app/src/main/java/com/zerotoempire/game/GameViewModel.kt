package com.zerotoempire.game

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class GameViewModel : ViewModel() {
    private val _state = MutableStateFlow(GameState())
    val state: StateFlow<GameState> = _state.asStateFlow()

    private val _meta = MutableStateFlow(PlayerMeta())
    val meta: StateFlow<PlayerMeta> = _meta.asStateFlow()

    init {
        viewModelScope.launch {
            while (true) {
                delay(100L)
                val s = _state.value
                val gain = s.incomePerSecond / 10.0
                if (gain > 0) _state.value = s.copy(cash = s.cash + gain, lifetimeCash = s.lifetimeCash + gain)
            }
        }
    }

    fun tap() {
        val s = _state.value
        _state.value = s.copy(cash = s.cash + s.tapValue, lifetimeCash = s.lifetimeCash + s.tapValue)
        _meta.value = _meta.value.copy(totalTaps = _meta.value.totalTaps + 1)
    }

    fun buy(id: Int) {
        val s = _state.value
        val b = s.businesses.firstOrNull { it.id == id } ?: return
        if (s.cash < b.nextCost) return
        _state.value = s.copy(cash = s.cash - b.nextCost, businesses = s.businesses.map { if (it.id == id) it.copy(level = it.level + 1) else it })
        _meta.value = _meta.value.copy(totalPurchases = _meta.value.totalPurchases + 1)
    }

    fun hireManager(businessId: Int): Boolean {
        val s = _state.value
        val manager = Managers.catalog.firstOrNull { it.businessId == businessId } ?: return false
        if (businessId in s.hiredManagerIds || s.cash < manager.cost) return false
        _state.value = s.copy(cash = s.cash - manager.cost, hiredManagerIds = s.hiredManagerIds + businessId)
        return true
    }

    fun buyUpgrade(id: String): Boolean {
        val s = _state.value
        val u = Upgrades.catalog.firstOrNull { it.id == id } ?: return false
        val rank = s.upgradeRanks[id] ?: 0
        if (rank >= u.maxRank || s.gems < u.gemCost) return false
        _state.value = s.copy(gems = s.gems - u.gemCost, upgradeRanks = s.upgradeRanks + (id to rank + 1))
        return true
    }

    fun grantGems(amount: Int) {
        if (amount <= 0) return
        val s = _state.value
        _state.value = s.copy(gems = s.gems + amount)
    }

    fun activateProfitBoost(minutes: Int = 10) {
        val s = _state.value
        val base = maxOf(System.currentTimeMillis(), s.boostEndsAtMillis)
        _state.value = s.copy(boostEndsAtMillis = base + minutes * 60_000L)
    }

    fun prestige() {
        val s = _state.value
        val totalReward = Progression.prestigeReward(s.lifetimeCash)
        val earned = totalReward - s.prestigePoints
        if (earned <= 0) return
        val persistentGems = s.gems
        val persistentUpgrades = s.upgradeRanks
        _state.value = GameState(prestigePoints = totalReward, gems = persistentGems, upgradeRanks = persistentUpgrades)
        _meta.value = _meta.value.copy(prestigeCount = _meta.value.prestigeCount + 1)
    }
}
