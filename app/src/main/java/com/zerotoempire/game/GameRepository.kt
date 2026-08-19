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
        val businesses = defaultBusinesses().map { business ->
            business.copy(level = (p[Keys.level(business.id)] ?: 0).coerceAtLeast(0))
        }
        val managers = Managers.catalog.filter { p[Keys.manager(it.businessId)] == true }.map { it.businessId }.toSet()
        val upgrades = Upgrades.catalog.associate { upgrade ->
            upgrade.id to (p[Keys.upgrade(upgrade.id)] ?: 0).coerceIn(0, upgrade.maxRank)
        }
        val rawCash = p[Keys.cash] ?: 10.0
        val rawLifetime = p[Keys.lifetime] ?: 10.0
        val cash = if (rawCash.isFinite() && rawCash >= 0.0) rawCash.coerceAtMost(EconomyMath.MAX_VALUE) else 10.0
        val lifetime = if (rawLifetime.isFinite() && rawLifetime >= 0.0) rawLifetime.coerceIn(10.0, EconomyMath.MAX_VALUE) else maxOf(10.0, cash)
        val gems = (p[Keys.gems] ?: 0).coerceAtLeast(0)
        val taps = (p[Keys.taps] ?: 0L).coerceAtLeast(0L)
        val purchases = (p[Keys.purchases] ?: 0L).coerceAtLeast(0L)
        val prestigeCount = (p[Keys.prestigeCount] ?: 0).coerceAtLeast(0)
        val currentWeek = ChallengeRotation.weeklyKey()
        val storedWeek = p[Keys.challengeWeek] ?: ""
        val sameWeek = storedWeek == currentWeek

        val state = GameState(
            cash = cash,
            lifetimeCash = maxOf(lifetime, cash),
            prestigePoints = (p[Keys.prestige] ?: 0).coerceAtLeast(0),
            businesses = businesses,
            hiredManagerIds = managers,
            upgradeRanks = upgrades,
            gems = gems,
            boostEndsAtMillis = (p[Keys.boostEnd] ?: 0L).coerceAtLeast(0L)
        )
        val meta = PlayerMeta(
            gems = gems,
            totalTaps = taps,
            totalPurchases = purchases,
            prestigeCount = prestigeCount,
            streakDays = (p[Keys.streak] ?: 0).coerceAtLeast(0),
            lastDailyClaimEpochDay = p[Keys.lastDaily] ?: -1L,
            boostEndsAtMillis = state.boostEndsAtMillis,
            claimedMissionIds = p[Keys.missions] ?: emptySet(),
            claimedAchievementIds = p[Keys.achievements] ?: emptySet(),
            claimedChallengeIds = p[Keys.challenges] ?: emptySet(),
            challengeWeekKey = currentWeek,
            challengeWeekTapBase = if (sameWeek) (p[Keys.challengeTapBase] ?: taps).coerceIn(0L, taps) else taps,
            challengeWeekPurchaseBase = if (sameWeek) (p[Keys.challengePurchaseBase] ?: purchases).coerceIn(0L, purchases) else purchases,
            challengeWeekPrestigeBase = if (sameWeek) (p[Keys.challengePrestigeBase] ?: prestigeCount).coerceIn(0, prestigeCount) else prestigeCount,
            onboardingCompleted = p[Keys.onboarding] ?: false,
            highestEraSeen = (p[Keys.highestEra] ?: 0).coerceIn(0, EmpireEras.all.lastIndex),
            adsRemoved = p[Keys.adsRemoved] ?: false,
            starterPackOwned = p[Keys.starterPack] ?: false
        )
        return Save(state, meta, (p[Keys.lastSeen] ?: 0L).coerceAtLeast(0L))
    }

    suspend fun save(s: GameState, m: PlayerMeta, now: Long = System.currentTimeMillis()) {
        context.gameDataStore.edit { p ->
            p[Keys.cash] = EconomyMath.finite(s.cash)
            p[Keys.lifetime] = EconomyMath.finite(s.lifetimeCash)
            p[Keys.prestige] = s.prestigePoints.coerceAtLeast(0)
            p[Keys.gems] = s.gems.coerceAtLeast(0)
            p[Keys.taps] = m.totalTaps.coerceAtLeast(0L)
            p[Keys.purchases] = m.totalPurchases.coerceAtLeast(0L)
            p[Keys.prestigeCount] = m.prestigeCount.coerceAtLeast(0)
            p[Keys.streak] = m.streakDays.coerceAtLeast(0)
            p[Keys.lastDaily] = m.lastDailyClaimEpochDay
            p[Keys.lastSeen] = now.coerceAtLeast(0L)
            p[Keys.boostEnd] = s.boostEndsAtMillis.coerceAtLeast(0L)
            p[Keys.missions] = m.claimedMissionIds
            p[Keys.achievements] = m.claimedAchievementIds
            p[Keys.challenges] = m.claimedChallengeIds
            p[Keys.challengeWeek] = m.challengeWeekKey
            p[Keys.challengeTapBase] = m.challengeWeekTapBase.coerceAtLeast(0L)
            p[Keys.challengePurchaseBase] = m.challengeWeekPurchaseBase.coerceAtLeast(0L)
            p[Keys.challengePrestigeBase] = m.challengeWeekPrestigeBase.coerceAtLeast(0)
            p[Keys.onboarding] = m.onboardingCompleted
            p[Keys.highestEra] = m.highestEraSeen.coerceIn(0, EmpireEras.all.lastIndex)
            p[Keys.adsRemoved] = m.adsRemoved
            p[Keys.starterPack] = m.starterPackOwned
            s.businesses.forEach { p[Keys.level(it.id)] = it.level.coerceAtLeast(0) }
            Managers.catalog.forEach { p[Keys.manager(it.businessId)] = it.businessId in s.hiredManagerIds }
            Upgrades.catalog.forEach { upgrade -> p[Keys.upgrade(upgrade.id)] = (s.upgradeRanks[upgrade.id] ?: 0).coerceIn(0, upgrade.maxRank) }
        }
    }
}
