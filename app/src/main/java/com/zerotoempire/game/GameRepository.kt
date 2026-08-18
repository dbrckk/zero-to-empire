package com.zerotoempire.game

import android.content.Context
import androidx.datastore.preferences.core.*
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.first

private val Context.gameDataStore by preferencesDataStore("zero_empire_save_v2")

class GameRepository(private val context: Context) {
    private object Keys {
        val cash = doublePreferencesKey("cash")
        val lifetime = doublePreferencesKey("lifetime")
        val prestige = intPreferencesKey("prestige")
        val gems = intPreferencesKey("gems")
        val taps = longPreferencesKey("taps")
        val purchases = longPreferencesKey("purchases")
        val prestigeCount = intPreferencesKey("prestige_count")
        val streak = intPreferencesKey("streak")
        val lastDaily = longPreferencesKey("last_daily")
        val lastSeen = longPreferencesKey("last_seen")
        val boostEnd = longPreferencesKey("boost_end")
        val missions = stringSetPreferencesKey("claimed_missions")
        val achievements = stringSetPreferencesKey("claimed_achievements")
        val challenges = stringSetPreferencesKey("claimed_challenges")
        val challengeWeek = stringPreferencesKey("challenge_week")
        val challengeTapBase = longPreferencesKey("challenge_tap_base")
        val challengePurchaseBase = longPreferencesKey("challenge_purchase_base")
        val challengePrestigeBase = intPreferencesKey("challenge_prestige_base")
        val onboarding = booleanPreferencesKey("onboarding_completed")
        val highestEra = intPreferencesKey("highest_era_seen")
        val adsRemoved = booleanPreferencesKey("ads_removed")
        val starterPack = booleanPreferencesKey("starter_pack_owned")
        fun level(id: Int) = intPreferencesKey("business_${id}_level")
        fun manager(id: Int) = booleanPreferencesKey("manager_$id")
        fun upgrade(id: String) = intPreferencesKey("upgrade_$id")
    }

    data class Save(val state: GameState, val meta: PlayerMeta, val lastSeenMillis: Long)

    suspend fun load(): Save {
        val p = context.gameDataStore.data.first()
        val businesses = defaultBusinesses().map { it.copy(level = p[Keys.level(it.id)] ?: 0) }
        val managers = Managers.catalog.filter { p[Keys.manager(it.businessId)] == true }.map { it.businessId }.toSet()
        val upgrades = Upgrades.catalog.associate { it.id to (p[Keys.upgrade(it.id)] ?: 0) }
        val gems = p[Keys.gems] ?: 0
        val taps = p[Keys.taps] ?: 0L
        val purchases = p[Keys.purchases] ?: 0L
        val prestigeCount = p[Keys.prestigeCount] ?: 0
        val currentWeek = ChallengeRotation.weeklyKey()
        val storedWeek = p[Keys.challengeWeek] ?: ""
        val sameWeek = storedWeek == currentWeek

        val state = GameState(
            cash = p[Keys.cash] ?: 10.0,
            lifetimeCash = p[Keys.lifetime] ?: 10.0,
            prestigePoints = p[Keys.prestige] ?: 0,
            businesses = businesses,
            hiredManagerIds = managers,
            upgradeRanks = upgrades,
            gems = gems,
            boostEndsAtMillis = p[Keys.boostEnd] ?: 0L
        )
        val meta = PlayerMeta(
            gems = gems,
            totalTaps = taps,
            totalPurchases = purchases,
            prestigeCount = prestigeCount,
            streakDays = p[Keys.streak] ?: 0,
            lastDailyClaimEpochDay = p[Keys.lastDaily] ?: -1L,
            boostEndsAtMillis = p[Keys.boostEnd] ?: 0L,
            claimedMissionIds = p[Keys.missions] ?: emptySet(),
            claimedAchievementIds = p[Keys.achievements] ?: emptySet(),
            claimedChallengeIds = p[Keys.challenges] ?: emptySet(),
            challengeWeekKey = currentWeek,
            challengeWeekTapBase = if (sameWeek) p[Keys.challengeTapBase] ?: taps else taps,
            challengeWeekPurchaseBase = if (sameWeek) p[Keys.challengePurchaseBase] ?: purchases else purchases,
            challengeWeekPrestigeBase = if (sameWeek) p[Keys.challengePrestigeBase] ?: prestigeCount else prestigeCount,
            onboardingCompleted = p[Keys.onboarding] ?: false,
            highestEraSeen = p[Keys.highestEra] ?: 0,
            adsRemoved = p[Keys.adsRemoved] ?: false,
            starterPackOwned = p[Keys.starterPack] ?: false
        )
        return Save(state, meta, p[Keys.lastSeen] ?: 0L)
    }

    suspend fun save(s: GameState, m: PlayerMeta, now: Long = System.currentTimeMillis()) {
        context.gameDataStore.edit { p ->
            p[Keys.cash] = s.cash
            p[Keys.lifetime] = s.lifetimeCash
            p[Keys.prestige] = s.prestigePoints
            p[Keys.gems] = s.gems
            p[Keys.taps] = m.totalTaps
            p[Keys.purchases] = m.totalPurchases
            p[Keys.prestigeCount] = m.prestigeCount
            p[Keys.streak] = m.streakDays
            p[Keys.lastDaily] = m.lastDailyClaimEpochDay
            p[Keys.lastSeen] = now
            p[Keys.boostEnd] = s.boostEndsAtMillis
            p[Keys.missions] = m.claimedMissionIds
            p[Keys.achievements] = m.claimedAchievementIds
            p[Keys.challenges] = m.claimedChallengeIds
            p[Keys.challengeWeek] = m.challengeWeekKey
            p[Keys.challengeTapBase] = m.challengeWeekTapBase
            p[Keys.challengePurchaseBase] = m.challengeWeekPurchaseBase
            p[Keys.challengePrestigeBase] = m.challengeWeekPrestigeBase
            p[Keys.onboarding] = m.onboardingCompleted
            p[Keys.highestEra] = m.highestEraSeen
            p[Keys.adsRemoved] = m.adsRemoved
            p[Keys.starterPack] = m.starterPackOwned
            s.businesses.forEach { p[Keys.level(it.id)] = it.level }
            Managers.catalog.forEach { p[Keys.manager(it.businessId)] = it.businessId in s.hiredManagerIds }
            Upgrades.catalog.forEach { p[Keys.upgrade(it.id)] = s.upgradeRanks[it.id] ?: 0 }
        }
    }
}
