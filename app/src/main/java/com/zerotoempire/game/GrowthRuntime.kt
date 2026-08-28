package com.zerotoempire.game

import android.app.Activity
import android.content.Context
import android.content.ContextWrapper
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import androidx.lifecycle.compose.LocalLifecycleOwner
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel

/** Runtime shell. Visual atmosphere must stay behind gameplay so it can never
 * obscure or intercept phone UI. Persistent controls live inside the Scaffold. */
@Composable
fun GrowthRuntimeRoot(vm: GameViewModel = viewModel()) {
    val context = LocalContext.current
    val activity = remember(context) { context.findGrowthActivity() }
    val lifecycleOwner = LocalLifecycleOwner.current
    val telemetry = remember(context) { LocalGrowthTelemetry(context.applicationContext) }
    val state = vm.state.collectAsStateWithLifecycle().value
    val meta = vm.meta.collectAsStateWithLifecycle().value
    val celebration = vm.celebration.collectAsStateWithLifecycle().value
    val adsAllowed = PrivacyConsentManager.adsAllowed.collectAsStateWithLifecycle().value
    val eraIndex = EmpireEras.current(state.lifetimeCash).index

    DisposableEffect(lifecycleOwner, vm) {
        val observer = LifecycleEventObserver { _, event ->
            when (event) {
                Lifecycle.Event.ON_START -> vm.onAppForegrounded()
                Lifecycle.Event.ON_STOP -> vm.onAppBackgrounded()
                else -> Unit
            }
        }
        lifecycleOwner.lifecycle.addObserver(observer)
        if (lifecycleOwner.lifecycle.currentState.isAtLeast(Lifecycle.State.STARTED)) vm.onAppForegrounded()
        onDispose { lifecycleOwner.lifecycle.removeObserver(observer) }
    }

    LaunchedEffect(Unit) { telemetry.track(GrowthEvent.SessionStarted) }
    LaunchedEffect(eraIndex) { GameMusicBus.setEmpireLevel(eraIndex) }
    LaunchedEffect(meta.onboardingCompleted) {
        if (meta.onboardingCompleted) telemetry.track(GrowthEvent.OnboardingCompleted)
    }
    LaunchedEffect(state.businesses.sumOf { it.level }) {
        if (state.businesses.any { it.level > 0 }) telemetry.track(GrowthEvent.FirstAssetPurchased)
    }
    LaunchedEffect(state.hiredManagerIds.size) {
        if (state.hiredManagerIds.isNotEmpty()) telemetry.track(GrowthEvent.FirstManagerHired)
    }
    LaunchedEffect(meta.prestigeCount) {
        if (meta.prestigeCount > 0) telemetry.track(GrowthEvent.FirstPrestige)
    }
    LaunchedEffect(celebration?.accent) {
        if (celebration?.accent == "REWARDED") telemetry.track(GrowthEvent.FirstRewardedCompleted)
    }

    SfxRuntime(vm)

    Box(Modifier.fillMaxSize()) {
        // Draw ambience first. CommerceRoot contains every interactive surface.
        EndgameAtmosphere(eraIndex = eraIndex, modifier = Modifier.fillMaxSize())
        CommerceRoot(vm)
    }

    if (activity != null) {
        InterstitialController(
            activity = activity,
            adsAllowed = adsAllowed,
            vm = vm,
            telemetry = telemetry
        )
    }
}

private tailrec fun Context.findGrowthActivity(): Activity? = when (this) {
    is Activity -> this
    is ContextWrapper -> baseContext.findGrowthActivity()
    else -> null
}
