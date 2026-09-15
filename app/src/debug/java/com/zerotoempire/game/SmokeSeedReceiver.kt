package com.zerotoempire.game

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.runBlocking

/** Debug-only state seeder used by the emulator functional smoke. */
class SmokeSeedReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action != ACTION_SEED) return
        val requestedCash = intent.getLongExtra(EXTRA_CASH, DEFAULT_CASH).toDouble()
            .coerceIn(0.0, EconomyMath.MAX_VALUE)

        runBlocking(Dispatchers.IO) {
            val repository = GameRepository(context.applicationContext)
            val save = repository.load()
            val seededCash = maxOf(save.state.cash, requestedCash)
            repository.save(
                s = save.state.copy(
                    cash = seededCash,
                    lifetimeCash = maxOf(save.state.lifetimeCash, seededCash)
                ),
                m = save.meta.copy(onboardingCompleted = true),
                creditedPurchaseTokens = save.creditedPurchaseTokens
            )
        }
    }

    companion object {
        const val ACTION_SEED = "com.zerotoempire.game.DEBUG_SMOKE_SEED"
        const val EXTRA_CASH = "cash"
        const val DEFAULT_CASH = 3_000L
    }
}
