package com.zerotoempire.game

import android.app.Activity
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import java.time.LocalDate

@Composable
fun InterstitialController(
    activity: Activity,
    adsAllowed: Boolean,
    vm: GameViewModel,
    telemetry: GrowthTelemetry
) {
    val meta = vm.meta.collectAsStateWithLifecycle().value
    val celebration = vm.celebration.collectAsStateWithLifecycle().value
    val gateway = remember(activity) { AdMobInterstitialGateway(activity.applicationContext) }
    val frequency = remember(activity) { InterstitialFrequencyStore(activity.applicationContext) }

    LaunchedEffect(adsAllowed, meta.adsRemoved) {
        if (adsAllowed && !meta.adsRemoved) gateway.preload()
    }

    LaunchedEffect(celebration, adsAllowed, meta.adsRemoved, meta.onboardingCompleted) {
        if (!adsAllowed || celebration == null || meta.adsRemoved) return@LaunchedEffect
        val breakPoint = when (celebration.accent) {
            "PRESTIGE" -> NaturalBreakPoint.PRESTIGE
            "NEW ERA", "ERA" -> NaturalBreakPoint.ERA_UNLOCK
            else -> return@LaunchedEffect
        }
        val now = System.currentTimeMillis()
        val today = LocalDate.now().toEpochDay()
        if (!InterstitialPolicy.canShow(
                state = frequency.snapshot(),
                nowMillis = now,
                currentEpochDay = today,
                breakPoint = breakPoint,
                onboardingCompleted = meta.onboardingCompleted,
                adsRemoved = meta.adsRemoved
            )) return@LaunchedEffect
        if (!gateway.isReady()) {
            gateway.preload()
            return@LaunchedEffect
        }
        gateway.show(
            activity = activity,
            onShown = {
                frequency.recordShow(System.currentTimeMillis())
                telemetry.track(GrowthEvent.InterstitialShown(breakPoint))
            }
        )
    }
}
