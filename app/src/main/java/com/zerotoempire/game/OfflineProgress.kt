package com.zerotoempire.game

import java.time.Instant
import java.time.ZoneId
import kotlin.math.min

data class OfflineReward(val elapsedSeconds:Long,val paidSeconds:Long,val cash:Double) {
    val eligible:Boolean get()=cash>0.0 && paidSeconds>=30
}

object OfflineProgress {
    fun calculate(
        state: GameState,
        lastSeenMillis: Long,
        nowMillis: Long = System.currentTimeMillis(),
        zoneId: ZoneId = ZoneId.systemDefault()
    ): OfflineReward {
        if (lastSeenMillis <= 0 || nowMillis <= lastSeenMillis) return OfflineReward(0,0,0.0)
        val elapsed = ((nowMillis-lastSeenMillis)/1000L).coerceAtLeast(0)
        val extraHours = (state.upgradeRanks["offline"] ?: 0).coerceIn(0,8)
        val capSeconds = (8L+extraHours)*3600L
        val paid = min(elapsed,capSeconds)
        if (paid <= 0 || state.automatedBaseIncomePerSecond <= 0.0) return OfflineReward(elapsed,paid,0.0)

        val paidEndMillis = lastSeenMillis + paid * 1000L
        var cursor = lastSeenMillis
        var cash = 0.0

        // Integrate only across boundaries that can change the multiplier: local midnight and boost expiry.
        while (cursor < paidEndMillis) {
            val zoned = Instant.ofEpochMilli(cursor).atZone(zoneId)
            val date = zoned.toLocalDate()
            val nextMidnight = date.plusDays(1).atStartOfDay(zoneId).toInstant().toEpochMilli()
            var segmentEnd = min(paidEndMillis, nextMidnight)
            if (state.boostEndsAtMillis > cursor && state.boostEndsAtMillis < segmentEnd) {
                segmentEnd = state.boostEndsAtMillis
            }
            if (segmentEnd <= cursor) segmentEnd = min(paidEndMillis, cursor + 1000L)

            val seconds = (segmentEnd - cursor) / 1000.0
            val boost = if (cursor < state.boostEndsAtMillis) 2.0 else 1.0
            val event = LiveOps.currentEvent(date)?.incomeMultiplier ?: 1.0
            val segmentCash = EconomyMath.finite(state.automatedBaseIncomePerSecond * boost * event * seconds * .75)
            cash = EconomyMath.safeAdd(cash, segmentCash)
            cursor = segmentEnd
        }

        return OfflineReward(elapsed,paid,EconomyMath.finite(cash))
    }
}
