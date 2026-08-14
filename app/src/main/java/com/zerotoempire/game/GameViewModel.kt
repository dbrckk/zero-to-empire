package com.zerotoempire.game

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import kotlin.math.floor
import kotlin.math.sqrt

class GameViewModel : ViewModel() {
    private val _state = MutableStateFlow(GameState())
    val state: StateFlow<GameState> = _state.asStateFlow()

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
        val gain = (1.0 + s.incomePerSecond * 0.05) * s.prestigeMultiplier
        _state.value = s.copy(cash = s.cash + gain, lifetimeCash = s.lifetimeCash + gain)
    }

    fun buy(id: Int) {
        val s = _state.value
        val business = s.businesses.first { it.id == id }
        if (s.cash < business.nextCost) return
        _state.value = s.copy(
            cash = s.cash - business.nextCost,
            businesses = s.businesses.map { if (it.id == id) it.copy(level = it.level + 1) else it }
        )
    }

    fun prestige() {
        val s = _state.value
        val earned = floor(sqrt(s.lifetimeCash / 1_000_000.0)).toInt()
        if (earned <= s.prestigePoints) return
        _state.value = GameState(prestigePoints = earned)
    }
}
