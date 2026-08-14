package com.zerotoempire.game

import org.junit.Assert.*
import org.junit.Test

class EconomyTest {
    @Test fun costsAlwaysIncrease(){ defaultBusinesses().forEach{b->assertTrue(b.copy(level=100).nextCost>b.copy(level=10).nextCost)} }
    @Test fun milestonesNeverReduceIncome(){ val b=defaultBusinesses().first(); assertTrue(b.copy(level=25).rawIncomePerSecond>=b.copy(level=24).rawIncomePerSecond) }
    @Test fun prestigeRewardIsMonotonic(){ var previous=0; listOf(1e6,1e7,1e8,1e9,1e12,1e15).forEach{cash->val reward=Progression.prestigeReward(cash);assertTrue(reward>=previous);previous=reward} }
    @Test fun managerRaisesBusinessIncome(){ val base=GameState(businesses=defaultBusinesses().map{if(it.id==0)it.copy(level=10) else it}); val managed=base.copy(hiredManagerIds=setOf(0)); assertTrue(managed.businessIncome(managed.businesses[0])>base.businessIncome(base.businesses[0])) }
    @Test fun upgradeRaisesGlobalIncome(){ val b=defaultBusinesses().map{if(it.id==0)it.copy(level=10)else it}; val base=GameState(businesses=b); val upgraded=base.copy(upgradeRanks=mapOf("income" to 1)); assertTrue(upgraded.incomePerSecond>base.incomePerSecond) }
    @Test fun offlineRewardIsCapped(){ val s=GameState(businesses=defaultBusinesses().map{if(it.id==0)it.copy(level=10)else it}); val now=1_000_000_000L; val r=OfflineProgress.calculate(s,now-100L*3600*1000,now); assertEquals(8L*3600,r.paidSeconds) }
    @Test fun offlineUpgradeExtendsCap(){ val s=GameState(businesses=defaultBusinesses().map{if(it.id==0)it.copy(level=10)else it},upgradeRanks=mapOf("offline" to 3)); val now=1_000_000_000L; val r=OfflineProgress.calculate(s,now-100L*3600*1000,now); assertEquals(11L*3600,r.paidSeconds) }
}
