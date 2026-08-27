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
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import androidx.lifecycle.compose.LocalLifecycleOwner
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun CommerceRoot(vm: GameViewModel = viewModel()) {
    val context = LocalContext.current
    val activity = remember(context) { context.findActivity() }
    val lifecycleOwner = LocalLifecycleOwner.current
    val meta by vm.meta.collectAsStateWithLifecycle()
    val billing = remember(context) { PlayBillingGateway(context.applicationContext) }
    val rewarded = remember(context) { AdMobRewardedGateway(context.applicationContext) }
    val consent = remember(activity) { activity?.let(::PrivacyConsentManager) }
    var showStore by remember { mutableStateOf(false) }
    var owned by remember { mutableStateOf<Set<StoreProduct>>(emptySet()) }
    var status by remember { mutableStateOf<String?>(null) }
    var adsAllowed by remember { mutableStateOf(false) }
    var privacyOptionsRequired by remember { mutableStateOf(false) }

    DisposableEffect(billing, activity) {
        billing.connect()
        if (activity != null && consent != null) consent.gather { canRequestAds, error -> adsAllowed = canRequestAds; privacyOptionsRequired = consent.isPrivacyOptionsRequired(); if (canRequestAds) rewarded.preload(); if (error != null && !canRequestAds) status = "Privacy setup is incomplete: $error" }
        billing.restore { restored -> owned = restored.filterNot { it.consumable }.toSet(); vm.applyEntitlements(restored) }
        onDispose { billing.disconnect() }
    }
    DisposableEffect(lifecycleOwner, billing) {
        val observer = LifecycleEventObserver { _, event -> if (event == Lifecycle.Event.ON_RESUME) billing.restore { restored -> owned = restored.filterNot { it.consumable }.toSet(); vm.applyEntitlements(restored) } }
        lifecycleOwner.lifecycle.addObserver(observer); onDispose { lifecycleOwner.lifecycle.removeObserver(observer) }
    }
    LaunchedEffect(activity, adsAllowed) {
        if (activity == null) return@LaunchedEffect
        vm.rewardedRequests.collect { placement ->
            if (!adsAllowed) { status = "Ads are unavailable until privacy choices are resolved."; return@collect }
            if (!rewarded.isReady()) { rewarded.preload(); status = "Reward video is loading. Try again shortly."; return@collect }
            rewarded.show(activity = activity, placement = placement, onReward = { when (placement) { RewardPlacement.DOUBLE_OFFLINE_EARNINGS -> vm.rewardDoubleOffline(); RewardPlacement.PROFIT_BOOST -> vm.rewardProfitBoost(); RewardPlacement.DAILY_BONUS -> vm.grantGems(10); RewardPlacement.EVENT_BONUS -> vm.activateProfitBoost(5) } })
        }
    }

    Box(Modifier.fillMaxSize()) {
        EmpireRoot(vm)
        if (activity != null) {
            Row(modifier = Modifier.align(Alignment.BottomCenter).padding(start = 16.dp, end = 16.dp, bottom = 86.dp).fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp), verticalAlignment = Alignment.CenterVertically) {
                FilledTonalButton(onClick = { showStore = true }, modifier = Modifier.weight(1f), shape = RoundedCornerShape(16.dp), contentPadding = PaddingValues(vertical = 9.dp)) { MetaSprite(MetaSpriteKind.STORE, 23.dp); Spacer(Modifier.width(5.dp)); Text("STORE", fontSize = 9.sp, fontWeight = FontWeight.Black) }
                FilledTonalButton(onClick = vm::requestProfitBoostAd, enabled = adsAllowed, modifier = Modifier.weight(1f), shape = RoundedCornerShape(16.dp), contentPadding = PaddingValues(vertical = 9.dp)) { MetaSprite(MetaSpriteKind.BOOST, 23.dp, active = adsAllowed); Spacer(Modifier.width(5.dp)); Text("×2 BOOST", fontSize = 9.sp, fontWeight = FontWeight.Black) }
                if (privacyOptionsRequired && consent != null) TextButton(onClick = { consent.showPrivacyOptions { error -> adsAllowed = consent.canRequestAds(); privacyOptionsRequired = consent.isPrivacyOptionsRequired(); if (adsAllowed) rewarded.preload(); if (error != null) status = error } }, modifier = Modifier.weight(.8f)) { Text("PRIVACY", fontSize = 8.sp) }
            }
        }
    }
    status?.let { message -> AlertDialog(onDismissRequest = { status = null }, confirmButton = { TextButton(onClick = { status = null }) { Text("OK") } }, text = { Text(message) }) }
    if (showStore && activity != null) StoreDialog(owned = owned + buildSet { if (meta.adsRemoved) add(StoreProduct.REMOVE_ADS); if (meta.starterPackOwned) add(StoreProduct.STARTER_PACK) }, onDismiss = { showStore = false }, onRestore = { billing.restore { restored -> owned = restored.filterNot { it.consumable }.toSet(); vm.applyEntitlements(restored); status = if (restored.isEmpty()) "No purchases found." else "Purchases restored." } }, onPurchase = { product -> billing.purchase(activity, product) { result -> when (result) { is PurchaseResult.Success -> { if (!result.product.consumable) owned = owned + result.product; vm.applyPurchase(result.product); status = "Purchase completed." }; PurchaseResult.Cancelled -> Unit; PurchaseResult.Pending -> status = "Purchase pending. Reward will unlock after Google Play confirms payment."; is PurchaseResult.Failed -> status = result.reason } } })
}

@Composable private fun StoreDialog(owned:Set<StoreProduct>,onDismiss:()->Unit,onRestore:()->Unit,onPurchase:(StoreProduct)->Unit){AlertDialog(onDismissRequest=onDismiss,containerColor=EmpireColors.SurfaceHigh,title={Row(verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.STORE,34.dp);Spacer(Modifier.width(8.dp));Text("EMPIRE STORE",color=EmpireColors.Gold,fontWeight=FontWeight.Black)}},text={Column(verticalArrangement=Arrangement.spacedBy(10.dp)){Text("Purchases are handled by Google Play. Prices and final confirmation are shown by Google Play.",color=EmpireColors.TextSecondary,fontSize=11.sp);StoreRow("REMOVE ADS","Lifetime removal of non-rewarded advertising. Reward videos remain optional.",StoreProduct.REMOVE_ADS in owned,MetaSpriteKind.LEGACY){onPurchase(StoreProduct.REMOVE_ADS)};StoreRow("STARTER PACK","250 gems + 30 min ×2 income. One-time purchase.",StoreProduct.STARTER_PACK in owned,MetaSpriteKind.BOOST){onPurchase(StoreProduct.STARTER_PACK)};StoreRow("120 GEMS","Consumable gem pack.",false,MetaSpriteKind.GEM){onPurchase(StoreProduct.GEM_PACK_SMALL)};StoreRow("650 GEMS","Consumable gem pack.",false,MetaSpriteKind.GEM){onPurchase(StoreProduct.GEM_PACK_MEDIUM)};OutlinedButton(onClick=onRestore,modifier=Modifier.fillMaxWidth()){Text("RESTORE PURCHASES")}}},confirmButton={TextButton(onClick=onDismiss){Text("CLOSE")}})}
@Composable private fun StoreRow(title:String,subtitle:String,owned:Boolean,kind:MetaSpriteKind,purchase:()->Unit){Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(14.dp)){Row(Modifier.fillMaxWidth().padding(12.dp),verticalAlignment=Alignment.CenterVertically){MetaSprite(kind,38.dp,active=!owned);Spacer(Modifier.width(10.dp));Column(Modifier.weight(1f)){Text(title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Text(subtitle,color=EmpireColors.TextSecondary,fontSize=10.sp)};Button(onClick=purchase,enabled=!owned){Text(if(owned)"OWNED" else "BUY",fontSize=10.sp)}}}}
private tailrec fun Context.findActivity():Activity?=when(this){is Activity->this;is ContextWrapper->baseContext.findActivity();else->null}
