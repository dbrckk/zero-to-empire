package com.zerotoempire.game

import android.app.Application
import android.os.SystemClock
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharedFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asSharedFlow
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
    private val _celebration = MutableStateFlow<MajorCelebration?>(null)
    val celebration: StateFlow<MajorCelebration?> = _celebration.asStateFlow()
    private val _buyMode = MutableStateFlow(BuyMode.X1)
    val buyMode: StateFlow<BuyMode> = _buyMode.asStateFlow()
    private val _rewardedRequests = MutableSharedFlow<RewardPlacement>(extraBufferCapacity = 1)
    val rewardedRequests: SharedFlow<RewardPlacement> = _rewardedRequests.asSharedFlow()

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
            val eraIndex = EmpireEras.current(restored.lifetimeCash).index
            _meta.value = save.meta.copy(gems = restored.gems, boostEndsAtMillis = restored.boostEndsAtMillis, highestEraSeen = maxOf(save.meta.highestEraSeen, eraIndex))
            loaded = true
            persistNow()

            launch {
                var previousTickNanos = SystemClock.elapsedRealtimeNanos()
                while (true) {
                    delay(250L)
                    val nowNanos = SystemClock.elapsedRealtimeNanos()
                    val elapsedSeconds = (nowNanos - previousTickNanos).coerceAtLeast(0L) / 1_000_000_000.0
                    previousTickNanos = nowNanos
                    val s = _state.value
                    val gain = s.incomePerSecond * elapsedSeconds
                    if (gain > 0.0 && gain.isFinite()) {
                        val updated = s.copy(cash = s.cash + gain, lifetimeCash = s.lifetimeCash + gain)
                        _state.value = updated
                        checkEraUnlock(updated)
                    }
                }
            }
            launch {
                while (true) {
                    delay(30_000L)
                    ensureChallengeWeek()
                    persistNow()
                }
            }
        }
    }

    fun setBuyMode(mode: BuyMode) { _buyMode.value = mode }
    fun completeOnboarding() { if (!_meta.value.onboardingCompleted) { _meta.value = _meta.value.copy(onboardingCompleted = true); scheduleSave() } }
    fun dismissCelebration() { _celebration.value = null }
    fun dismissOfflineReward() { _offlineReward.value = null }
    fun requestDoubleOfflineAd() { if (_offlineReward.value?.eligible == true) _rewardedRequests.tryEmit(RewardPlacement.DOUBLE_OFFLINE_EARNINGS) }
    fun requestProfitBoostAd() { _rewardedRequests.tryEmit(RewardPlacement.PROFIT_BOOST) }
    fun canClaimDaily(): Boolean = _meta.value.lastDailyClaimEpochDay != LocalDate.now().toEpochDay()

    fun ensureChallengeWeek() {
        val key = ChallengeRotation.weeklyKey()
        val m = _meta.value
        if (m.challengeWeekKey == key) return
        _meta.value = m.copy(
            challengeWeekKey = key,
            challengeWeekTapBase = m.totalTaps,
            challengeWeekPurchaseBase = m.totalPurchases,
            challengeWeekPrestigeBase = m.prestigeCount
        )
        scheduleSave()
    }

    fun claimDaily(): RewardDay? {
        val today = LocalDate.now().toEpochDay(); val meta = _meta.value
        if (meta.lastDailyClaimEpochDay == today) return null
        val nextStreak = if (meta.lastDailyClaimEpochDay == today - 1) meta.streakDays + 1 else 1
        val reward = LoginCalendar.rewardFor(nextStreak); val s = _state.value
        val boostBase = maxOf(System.currentTimeMillis(), s.boostEndsAtMillis)
        val boostEnd = if (reward.multiplierMinutes > 0) boostBase + reward.multiplierMinutes * 60_000L else s.boostEndsAtMillis
        _state.value = s.copy(gems = s.gems + reward.gems, boostEndsAtMillis = boostEnd)
        _meta.value = meta.copy(gems = _state.value.gems, streakDays = nextStreak, lastDailyClaimEpochDay = today, boostEndsAtMillis = boostEnd)
        scheduleSave(); return reward
    }

    fun missions(): List<Mission> = Progression.missions(_state.value, _meta.value)
    fun achievements(): List<Achievement> = Progression.achievements(_state.value, _meta.value)
    fun challenges(): List<TimedChallenge> { ensureChallengeWeek(); return ChallengeRotation.current(_state.value, _meta.value) }

    fun claimMission(id: String): Boolean { val m=missions().firstOrNull{it.id==id}?:return false; if(!m.completed||m.claimed)return false; _state.value=_state.value.copy(gems=_state.value.gems+m.rewardGems); _meta.value=_meta.value.copy(gems=_state.value.gems,claimedMissionIds=_meta.value.claimedMissionIds+id); scheduleSave(); return true }
    fun claimAchievement(id: String): Boolean { val a=achievements().firstOrNull{it.id==id}?:return false; if(!a.unlocked||a.claimed)return false; _state.value=_state.value.copy(gems=_state.value.gems+a.rewardGems); _meta.value=_meta.value.copy(gems=_state.value.gems,claimedAchievementIds=_meta.value.claimedAchievementIds+id); scheduleSave(); return true }
    fun claimChallenge(id: String): Boolean { val c=challenges().firstOrNull{it.id==id}?:return false; if(!c.completed||c.claimed)return false; _state.value=_state.value.copy(gems=_state.value.gems+c.rewardGems); _meta.value=_meta.value.copy(gems=_state.value.gems,claimedChallengeIds=_meta.value.claimedChallengeIds+id); _celebration.value=MajorCelebration("CHALLENGE COMPLETE","+${c.rewardGems} gems earned","★","WEEKLY"); scheduleSave(); return true }

    fun applyEntitlements(products: Set<StoreProduct>) {
        val hadStarter = _meta.value.starterPackOwned
        val restoredStarter = StoreProduct.STARTER_PACK in products && !hadStarter
        val hasRemoveAds = StoreProduct.REMOVE_ADS in products || _meta.value.adsRemoved
        val hasStarter = StoreProduct.STARTER_PACK in products || hadStarter
        val recoveredConsumableGems = (if (StoreProduct.GEM_PACK_SMALL in products) 120 else 0) + (if (StoreProduct.GEM_PACK_MEDIUM in products) 650 else 0)
        val restoredStarterGems = if (restoredStarter) 250 else 0
        val totalRecoveredGems = recoveredConsumableGems + restoredStarterGems
        if (totalRecoveredGems > 0) _state.value = _state.value.copy(gems = _state.value.gems + totalRecoveredGems)
        _meta.value = _meta.value.copy(gems = _state.value.gems, adsRemoved = hasRemoveAds, starterPackOwned = hasStarter)
        if (restoredStarter) activateProfitBoost(30)
        if (totalRecoveredGems > 0) {
            val detail = if (restoredStarter) "Starter Pack and purchase rewards restored." else "+$totalRecoveredGems gems restored."
            _celebration.value = MajorCelebration("PURCHASE RECOVERED", detail, "◆", "STORE")
        }
        scheduleSave()
    }

    fun applyPurchase(product: StoreProduct) {
        when (product) {
            StoreProduct.REMOVE_ADS -> _meta.value = _meta.value.copy(adsRemoved = true)
            StoreProduct.STARTER_PACK -> if (!_meta.value.starterPackOwned) { _state.value = _state.value.copy(gems = _state.value.gems + 250); _meta.value = _meta.value.copy(gems = _state.value.gems, starterPackOwned = true); activateProfitBoost(30) }
            StoreProduct.GEM_PACK_SMALL -> grantGems(120)
            StoreProduct.GEM_PACK_MEDIUM -> grantGems(650)
        }
        _celebration.value = MajorCelebration("PURCHASE COMPLETE", "Your empire has been upgraded.", "◆", "STORE")
        scheduleSave()
    }

    fun rewardDoubleOffline() { val reward = _offlineReward.value ?: return; if (!reward.eligible) return; _state.value = _state.value.copy(cash = _state.value.cash + reward.cash, lifetimeCash = _state.value.lifetimeCash + reward.cash); _offlineReward.value = null; _celebration.value = MajorCelebration("OFFLINE PROFITS ×2", "+${reward.cash.toLong()} bonus cash", "⚡", "REWARDED"); scheduleSave() }
    fun rewardProfitBoost() { activateProfitBoost(10); _celebration.value = MajorCelebration("OVERDRIVE ACTIVE", "All profits doubled for 10 minutes.", "⚡", "REWARDED") }

    fun tap() {
        ensureChallengeWeek()
        val s=_state.value; val u=s.copy(cash=s.cash+s.tapValue,lifetimeCash=s.lifetimeCash+s.tapValue)
        _state.value=u; _meta.value=_meta.value.copy(totalTaps=_meta.value.totalTaps+1); checkEraUnlock(u); scheduleSave()
    }

    fun buy(id: Int) { buyBulk(id, _buyMode.value) }
    fun bulkQuote(id: Int, mode: BuyMode = _buyMode.value): BulkQuote { val s = _state.value; val b = s.businesses.firstOrNull { it.id == id } ?: return BulkQuote(0, 0.0); return BulkPurchase.quote(b, s.cash, mode) }

    fun buyBulk(id: Int, mode: BuyMode): BulkQuote {
        ensureChallengeWeek()
        val s = _state.value; val b = s.businesses.firstOrNull { it.id == id } ?: return BulkQuote(0, 0.0)
        val quote = BulkPurchase.quote(b, s.cash, mode); if (!quote.valid || quote.totalCost > s.cash) return BulkQuote(0, 0.0)
        val newLevel = b.level + quote.count; val updatedBusiness = b.copy(level = newLevel)
        _state.value = s.copy(cash = (s.cash - quote.totalCost).coerceAtLeast(0.0), businesses = s.businesses.map { if (it.id == id) updatedBusiness else it })
        _meta.value = _meta.value.copy(totalPurchases = _meta.value.totalPurchases + quote.count)
        val crossed = BulkPurchase.crossedMilestones(b.level, newLevel)
        if (crossed.isNotEmpty()) _celebration.value = Celebrations.milestone(updatedBusiness.copy(level = crossed.last()))
        else if (quote.count >= 10) _celebration.value = MajorCelebration("MASS EXPANSION", "+${quote.count} ${b.name} levels", "▲", "EXPANSION")
        scheduleSave(); return quote
    }

    fun hireManager(businessId:Int):Boolean{val s=_state.value;val m=Managers.catalog.firstOrNull{it.businessId==businessId}?:return false;if(businessId in s.hiredManagerIds||s.cash<m.cost)return false;_state.value=s.copy(cash=s.cash-m.cost,hiredManagerIds=s.hiredManagerIds+businessId);scheduleSave();return true}
    fun buyUpgrade(id:String):Boolean{val s=_state.value;val u=Upgrades.catalog.firstOrNull{it.id==id}?:return false;val r=s.upgradeRanks[id]?:0;if(r>=u.maxRank||s.gems<u.gemCost)return false;_state.value=s.copy(gems=s.gems-u.gemCost,upgradeRanks=s.upgradeRanks+(id to r+1));syncMetaCurrency();scheduleSave();return true}
    fun grantGems(amount:Int){if(amount>0){_state.value=_state.value.copy(gems=_state.value.gems+amount);syncMetaCurrency();scheduleSave()}}
    fun activateProfitBoost(){requestProfitBoostAd()}
    fun activateProfitBoost(minutes:Int){val s=_state.value;val base=maxOf(System.currentTimeMillis(),s.boostEndsAtMillis);_state.value=s.copy(boostEndsAtMillis=base+minutes*60_000L);_meta.value=_meta.value.copy(boostEndsAtMillis=_state.value.boostEndsAtMillis);scheduleSave()}
    fun prestige(){ensureChallengeWeek();val s=_state.value;val total=Progression.prestigeReward(s.lifetimeCash);if(total-s.prestigePoints<=0)return;_state.value=GameState(prestigePoints=total,gems=s.gems,upgradeRanks=s.upgradeRanks);_meta.value=_meta.value.copy(prestigeCount=_meta.value.prestigeCount+1);_celebration.value=MajorCelebration("ASCENSION COMPLETE","Legacy power permanently increased.","◇","PRESTIGE");scheduleSave()}

    private fun checkEraUnlock(s:GameState){val era=EmpireEras.current(s.lifetimeCash);if(era.index>_meta.value.highestEraSeen){_meta.value=_meta.value.copy(highestEraSeen=era.index);_celebration.value=Celebrations.era(era);scheduleSave()}}
    private fun syncMetaCurrency(){_meta.value=_meta.value.copy(gems=_state.value.gems)}
    private fun scheduleSave(){if(loaded){saveJob?.cancel();saveJob=viewModelScope.launch{delay(350L);persistNow()}}}
    private suspend fun persistNow(){if(loaded)repository.save(_state.value,_meta.value)}
    override fun onCleared(){if(loaded){val s=_state.value;val m=_meta.value;viewModelScope.launch{repository.save(s,m)}};super.onCleared()}
}
