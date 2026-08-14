package com.zerotoempire.game

import android.content.Context
import androidx.datastore.preferences.core.doublePreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.intPreferencesKey
import androidx.datastore.preferences.core.longPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.first

private val Context.gameDataStore by preferencesDataStore("zero_empire_save_v1")

class GameRepository(private val context: Context) {
    private object Keys {
        val cash = doublePreferencesKey("cash")
        val lifetime = doublePreferencesKey("lifetime")
        val prestige = intPreferencesKey("prestige")
        val gems = intPreferencesKey("gems")
        val taps = longPreferencesKey("taps")
        val purchases = longPreferencesKey("purchases")
        val prestigeCount = intPreferencesKey("prestige_count")
        val lastSeen = longPreferencesKey("last_seen")
        fun level(id: Int) = intPreferencesKey("business_${id}_level")
    }

    data class Save(val state: GameState, val meta: PlayerMeta, val lastSeenMillis: Long)

    suspend fun load(): Save {
        val p = context.gameDataStore.data.first()
        val businesses = defaultBusinesses().map { it.copy(level = p[Keys.level(it.id)] ?: 0) }
        return Save(
            GameState(
                cash = p[Keys.cash] ?: 10.0,
                lifetimeCash = p[Keys.lifetime] ?: 10.0,
                prestigePoints = p[Keys.prestige] ?: 0,
                businesses = businesses
            ),
            PlayerMeta(
                gems = p[Keys.gems] ?: 0,
                totalTaps = p[Keys.taps] ?: 0L,
                totalPurchases = p[Keys.purchases] ?: 0L,
                prestigeCount = p[Keys.prestigeCount] ?: 0
            ),
            p[Keys.lastSeen] ?: 0L
        )
    }

    suspend fun save(state: GameState, meta: PlayerMeta, now: Long = System.currentTimeMillis()) {
        context.gameDataStore.edit { p ->
            p[Keys.cash] = state.cash
            p[Keys.lifetime] = state.lifetimeCash
            p[Keys.prestige] = state.prestigePoints
            p[Keys.gems] = meta.gems
            p[Keys.taps] = meta.totalTaps
            p[Keys.purchases] = meta.totalPurchases
            p[Keys.prestigeCount] = meta.prestigeCount
            p[Keys.lastSeen] = now
            state.businesses.forEach { p[Keys.level(it.id)] = it.level }
        }
    }
}
