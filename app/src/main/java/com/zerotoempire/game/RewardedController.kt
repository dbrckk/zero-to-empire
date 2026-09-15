package com.zerotoempire.game

import android.app.Activity
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import kotlinx.coroutines.flow.collectLatest

/**
 * Owns rewarded-ad lifecycle at the runtime boundary.
 *
 * Gameplay emits provider-neutral placements; this controller is the only layer
 * that talks to AdMob and it keeps consent/ad-removal policy out of GameViewModel.
 */
@Composable
fun RewardedController(
    activity: Activity,
    adsAllowed: Boolean,
    vm: GameViewModel
) {
    val meta = vm.meta.collectAsStateWithLifecycle().value
    val gateway = remember(activity) { AdMobRewardedGateway(activity.applicationContext) }

    LaunchedEffect(adsAllowed, meta.adsRemoved) {
        val enabled = adsAllowed && !meta.adsRemoved
        gateway.setEnabled(enabled)
        if (enabled) gateway.preload()
    }

    LaunchedEffect(activity, gateway, vm) {
        vm.rewardedRequests.collectLatest { placement ->
            if (!adsAllowed || meta.adsRemoved) return@collectLatest
            if (!gateway.isReady()) {
                gateway.preload()
                return@collectLatest
            }
            gateway.show(
                activity = activity,
                placement = placement,
                onReward = { vm.onRewardedCompleted(placement) }
            )
        }
    }
}
