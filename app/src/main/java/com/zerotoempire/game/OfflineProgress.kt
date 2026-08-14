package com.zerotoempire.game

import kotlin.math.min

data class OfflineReward(val elapsedSeconds:Long,val paidSeconds:Long,val cash:Double) { val eligible:Boolean get()=cash>0.0 && paidSeconds>=30 }

object OfflineProgress {
    fun calculate(state:GameState,lastSeenMillis:Long,nowMillis:Long=System.currentTimeMillis()):OfflineReward {
        if(lastSeenMillis<=0 || nowMillis<=lastSeenMillis) return OfflineReward(0,0,0.0)
        val elapsed=((nowMillis-lastSeenMillis)/1000L).coerceAtLeast(0)
        val extraHours=(state.upgradeRanks["offline"]?:0).coerceIn(0,8)
        val capSeconds=(8L+extraHours)*3600L
        val paid=min(elapsed,capSeconds)
        // Offline runs at 75% to preserve value of active play.
        return OfflineReward(elapsed,paid,state.incomePerSecond*paid*.75)
    }
}
