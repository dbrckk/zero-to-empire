package com.zerotoempire.game

import android.app.Activity
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.lifecycle.compose.collectAsStateWithLifecycle

/** Bridges provider-neutral gameplay reward requests to the AdMob gateway. */
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

    LaunchedEffect(activity, gateway, vm, adsAllowed, meta.adsRemoved) {
        vm.rewardedRequests.collect { placement ->
            if (!adsAllowed || meta.adsRemoved) return@collect
            if (!gateway.isReady()) {
                gateway.preload()
                return@collect
            }
            gateway.show(
                activity = activity,
                placement = placement,
                onReward = {
                    when (placement) {
                        RewardPlacement.DOUBLE_OFFLINE_EARNINGS -> vm.rewardDoubleOffline()
                        RewardPlacement.PROFIT_BOOST -> vm.rewardProfitBoost()
                        RewardPlacement.DAILY_BONUS,
                        RewardPlacement.EVENT_BONUS -> Unit
                    }
                }
            )
        }
    }
}
