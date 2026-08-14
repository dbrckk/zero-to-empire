package com.zerotoempire.game

import android.app.Activity
import android.content.Context
import android.content.ContextWrapper
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun CommerceRoot(vm: GameViewModel = viewModel()) {
    val context = LocalContext.current
    val activity = remember(context) { context.findActivity() }
    val billing = remember(context) { PlayBillingGateway(context.applicationContext) }
    val rewarded = remember(context) { AdMobRewardedGateway(context.applicationContext) }

    var showStore by remember { mutableStateOf(false) }
    var owned by remember { mutableStateOf<Set<StoreProduct>>(emptySet()) }
    var status by remember { mutableStateOf<String?>(null) }

    DisposableEffect(billing) {
        billing.connect()
        rewarded.preload()
        billing.restore { restored -> owned = restored }
        onDispose { billing.disconnect() }
    }

    Box(Modifier.fillMaxSize()) {
        EmpireRoot(vm)

        if (activity != null) {
            Column(
                modifier = Modifier.align(Alignment.TopEnd).padding(top = 52.dp, end = 12.dp),
                horizontalAlignment = Alignment.End
            ) {
                SmallFloatingActionButton(
                    onClick = { showStore = true },
                    containerColor = EmpireColors.SurfaceHigh,
                    contentColor = EmpireColors.Gold
                ) { Text("$", fontWeight = FontWeight.Black) }

                Spacer(Modifier.height(8.dp))

                FilledTonalButton(
                    onClick = {
                        if (!rewarded.isReady()) {
                            rewarded.preload()
                            status = "Reward video is loading. Try again shortly."
                        } else {
                            rewarded.show(
                                activity = activity,
                                placement = RewardPlacement.PROFIT_BOOST,
                                onReward = {
                                    vm.activateProfitBoost(10)
                                    status = "Profit Overdrive activated for 10 minutes."
                                }
                            )
                        }
                    },
                    shape = RoundedCornerShape(50),
                    contentPadding = PaddingValues(horizontal = 12.dp, vertical = 6.dp)
                ) {
                    Text("▶ ×2 BOOST", fontSize = 10.sp, fontWeight = FontWeight.Black)
                }
            }
        }
    }

    status?.let { message ->
        AlertDialog(
            onDismissRequest = { status = null },
            confirmButton = { TextButton(onClick = { status = null }) { Text("OK") } },
            text = { Text(message) }
        )
    }

    if (showStore && activity != null) {
        StoreDialog(
            owned = owned,
            onDismiss = { showStore = false },
            onRestore = {
                billing.restore {
                    owned = it
                    status = if (it.isEmpty()) "No permanent purchases found." else "Purchases restored."
                }
            },
            onPurchase = { product ->
                billing.purchase(activity, product) { result ->
                    when (result) {
                        is PurchaseResult.Success -> {
                            when (result.product) {
                                StoreProduct.REMOVE_ADS -> owned = owned + StoreProduct.REMOVE_ADS
                                StoreProduct.STARTER_PACK -> {
                                    owned = owned + StoreProduct.STARTER_PACK
                                    vm.grantGems(150)
                                    vm.activateProfitBoost(30)
                                }
                                StoreProduct.GEM_PACK_SMALL -> vm.grantGems(100)
                                StoreProduct.GEM_PACK_MEDIUM -> vm.grantGems(600)
                            }
                            status = "Purchase completed."
                        }
                        PurchaseResult.Cancelled -> Unit
                        PurchaseResult.Pending -> status = "Purchase pending. Reward will unlock after Google Play confirms payment."
                        is PurchaseResult.Failed -> status = result.reason
                    }
                }
            }
        )
    }
}

@Composable
private fun StoreDialog(
    owned: Set<StoreProduct>,
    onDismiss: () -> Unit,
    onRestore: () -> Unit,
    onPurchase: (StoreProduct) -> Unit
) {
    AlertDialog(
        onDismissRequest = onDismiss,
        containerColor = EmpireColors.SurfaceHigh,
        title = { Text("EMPIRE STORE", color = EmpireColors.Gold, fontWeight = FontWeight.Black) },
        text = {
            Column(verticalArrangement = Arrangement.spacedBy(10.dp)) {
                Text(
                    "Purchases are handled by Google Play. Prices are shown by the Play purchase sheet.",
                    color = EmpireColors.TextSecondary,
                    fontSize = 11.sp
                )
                StoreRow(
                    "REMOVE ADS",
                    "Lifetime removal of non-rewarded advertising.",
                    StoreProduct.REMOVE_ADS in owned,
                    { onPurchase(StoreProduct.REMOVE_ADS) }
                )
                StoreRow(
                    "STARTER PACK",
                    "150 gems + 30 min ×2 income. One-time purchase.",
                    StoreProduct.STARTER_PACK in owned,
                    { onPurchase(StoreProduct.STARTER_PACK) }
                )
                StoreRow("100 GEMS", "Consumable gem pack.", false) { onPurchase(StoreProduct.GEM_PACK_SMALL) }
                StoreRow("600 GEMS", "Consumable gem pack.", false) { onPurchase(StoreProduct.GEM_PACK_MEDIUM) }
                OutlinedButton(onClick = onRestore, modifier = Modifier.fillMaxWidth()) {
                    Text("RESTORE PURCHASES")
                }
            }
        },
        confirmButton = { TextButton(onClick = onDismiss) { Text("CLOSE") } }
    )
}

@Composable
private fun StoreRow(title: String, subtitle: String, owned: Boolean, purchase: () -> Unit) {
    Surface(color = EmpireColors.Surface, shape = RoundedCornerShape(14.dp)) {
        Row(Modifier.fillMaxWidth().padding(12.dp), verticalAlignment = Alignment.CenterVertically) {
            Column(Modifier.weight(1f)) {
                Text(title, color = EmpireColors.TextPrimary, fontWeight = FontWeight.Black)
                Text(subtitle, color = EmpireColors.TextSecondary, fontSize = 10.sp)
            }
            Button(onClick = purchase, enabled = !owned) {
                Text(if (owned) "OWNED" else "BUY", fontSize = 10.sp)
            }
        }
    }
}

private tailrec fun Context.findActivity(): Activity? = when (this) {
    is Activity -> this
    is ContextWrapper -> baseContext.findActivity()
    else -> null
}
