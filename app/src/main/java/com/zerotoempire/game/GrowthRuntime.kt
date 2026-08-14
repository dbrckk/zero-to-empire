package com.zerotoempire.game

import android.app.Activity
import android.content.Context
import android.content.ContextWrapper
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun GrowthRuntimeRoot(vm: GameViewModel = viewModel()) {
    val context = LocalContext.current
    val activity = remember(context) { context.findGrowthActivity() }
    val telemetry = remember(context) { LocalGrowthTelemetry(context.applicationContext) }
    val state = vm.state.collectAsStateWithLifecycle().value
    val meta = vm.meta.collectAsStateWithLifecycle().value
    val celebration = vm.celebration.collectAsStateWithLifecycle().value
    val adsAllowed = PrivacyConsentManager.adsAllowed.collectAsStateWithLifecycle().value

    LaunchedEffect(Unit) { telemetry.track(GrowthEvent.SessionStarted) }
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

    Box {
        CommerceRoot(vm)
        if (meta.onboardingCompleted) {
            BulkQuoteDock(
                vm = vm,
                modifier = Modifier
                    .align(Alignment.BottomCenter)
                    .padding(start = 10.dp, end = 10.dp, bottom = 148.dp)
            )
        }
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
