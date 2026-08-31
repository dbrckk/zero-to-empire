package com.zerotoempire.game

import android.app.Activity
import android.content.Context
import android.content.ContextWrapper
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
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
    var purchaseInFlight by remember { mutableStateOf<StoreProduct?>(null) }
    var pendingPurchases by remember { mutableStateOf<Set<StoreProduct>>(emptySet()) }
    var status by remember { mutableStateOf<String?>(null) }
    var adsAllowed by remember { mutableStateOf(false) }
    var privacyOptionsRequired by remember { mutableStateOf(false) }

    DisposableEffect(billing, activity) {
        billing.connect()
        if (activity != null && consent != null) consent.gather { canRequestAds, error -> adsAllowed = canRequestAds; rewarded.setEnabled(canRequestAds); privacyOptionsRequired = consent.isPrivacyOptionsRequired(); if (canRequestAds) rewarded.preload(); if (error != null && !canRequestAds) status = "Privacy setup is incomplete: $error" }
        billing.restore { result -> val restored = result.products; owned = restored.filterNot { it.consumable }.toSet(); if (purchaseInFlight == null) pendingPurchases = result.pendingProducts; vm.applyEntitlements(restored, authoritativePermanentEntitlements = result is RestoreResult.Success) }
        onDispose { rewarded.setEnabled(false); billing.disconnect() }
    }
    DisposableEffect(lifecycleOwner, billing) {
        var leftForeground = false
        val observer = LifecycleEventObserver { _, event ->
            when (event) {
                Lifecycle.Event.ON_STOP -> leftForeground = true
                Lifecycle.Event.ON_RESUME -> if (leftForeground) {
                    leftForeground = false
                    billing.restore { result ->
                        val restored = result.products
                        owned = restored.filterNot { it.consumable }.toSet()
                        if (purchaseInFlight == null) pendingPurchases = result.pendingProducts
                        vm.applyEntitlements(restored, authoritativePermanentEntitlements = result is RestoreResult.Success)
                    }
                }
                else -> Unit
            }
        }
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
                FilledTonalButton(onClick = { showStore = true }, modifier = Modifier.weight(1f).heightIn(min = 48.dp), shape = RoundedCornerShape(16.dp), contentPadding = PaddingValues(vertical = 9.dp)) { MetaSprite(MetaSpriteKind.STORE, 23.dp); Spacer(Modifier.width(5.dp)); Text("STORE", fontSize = 9.sp, fontWeight = FontWeight.Black) }
                FilledTonalButton(onClick = vm::requestProfitBoostAd, enabled = adsAllowed, modifier = Modifier.weight(1f).heightIn(min = 48.dp), shape = RoundedCornerShape(16.dp), contentPadding = PaddingValues(vertical = 9.dp)) { MetaSprite(MetaSpriteKind.BOOST, 23.dp, active = adsAllowed); Spacer(Modifier.width(5.dp)); Text("×2 BOOST", fontSize = 9.sp, fontWeight = FontWeight.Black) }
                if (privacyOptionsRequired && consent != null) TextButton(onClick = { consent.showPrivacyOptions { error -> adsAllowed = consent.canRequestAds(); rewarded.setEnabled(adsAllowed); privacyOptionsRequired = consent.isPrivacyOptionsRequired(); if (adsAllowed) rewarded.preload(); if (error != null) status = error } }, modifier = Modifier.weight(.8f).heightIn(min = 48.dp)) { Text("PRIVACY", fontSize = 8.sp) }
            }
        }
    }
    status?.let { message -> AlertDialog(onDismissRequest = { status = null }, confirmButton = { TextButton(onClick = { status = null }, modifier = Modifier.heightIn(min = 48.dp)) { Text("OK") } }, text = { Text(message) }) }
    if (showStore && activity != null) StoreDialog(
        owned = owned + buildSet { if (meta.adsRemoved) add(StoreProduct.REMOVE_ADS); if (meta.starterPackOwned) add(StoreProduct.STARTER_PACK) },
        purchaseInFlight = purchaseInFlight,
        pendingPurchases = pendingPurchases,
        onDismiss = { showStore = false },
        onDiagnostics = if (BuildConfig.DEBUG) {
            { status = LocalBillingDiagnostics.snapshot().toSupportText() }
        } else null,
        onRestore = { billing.restore { result ->
            val restored = result.products
            owned = restored.filterNot { it.consumable }.toSet()
            if (purchaseInFlight == null) pendingPurchases = result.pendingProducts
            vm.applyEntitlements(restored, authoritativePermanentEntitlements = result is RestoreResult.Success)
            status = when (result) {
                is RestoreResult.Success -> when {
                    restored.isNotEmpty() -> "Purchases restored."
                    result.pendingProducts.isNotEmpty() -> "Payment is still pending Google Play confirmation."
                    else -> "No purchases found."
                }
                is RestoreResult.Failed -> if (restored.isEmpty()) result.reason else "${result.reason} Some purchases were restored."
            }
        } },
        onPurchase = { product ->
            if (purchaseInFlight != null) return@StoreDialog
            purchaseInFlight = product
            pendingPurchases = pendingPurchases - product
            billing.purchase(activity, product) { result ->
                when (result) {
                    is PurchaseResult.Success -> {
                        purchaseInFlight = null
                        pendingPurchases = pendingPurchases - result.product
                        if (!result.product.consumable) owned = owned + result.product
                        vm.applyPurchase(result.product)
                        status = "Purchase completed."
                    }
                    PurchaseResult.Cancelled -> {
                        purchaseInFlight = null
                        pendingPurchases = pendingPurchases - product
                    }
                    PurchaseResult.Pending -> {
                        purchaseInFlight = null
                        pendingPurchases = pendingPurchases + product
                        status = "Purchase pending. You can close the Store; the reward will unlock after Google Play confirms payment."
                    }
                    is PurchaseResult.Failed -> {
                        purchaseInFlight = null
                        pendingPurchases = pendingPurchases - product
                        status = result.reason
                    }
                }
            }
        }
    )
}

@Composable
private fun StoreDialog(
    owned: Set<StoreProduct>,
    purchaseInFlight: StoreProduct?,
    pendingPurchases: Set<StoreProduct>,
    onDismiss: () -> Unit,
    onDiagnostics: (() -> Unit)?,
    onRestore: () -> Unit,
    onPurchase: (StoreProduct) -> Unit
) {
    AlertDialog(
        onDismissRequest = onDismiss,
        containerColor = EmpireColors.SurfaceHigh,
        title = {
            Row(verticalAlignment = Alignment.CenterVertically) {
                MetaSprite(MetaSpriteKind.STORE, 34.dp)
                Spacer(Modifier.width(8.dp))
                Text("EMPIRE STORE", color = EmpireColors.Gold, fontWeight = FontWeight.Black)
            }
        },
        text = {
            Column(
                modifier = Modifier.heightIn(max = 480.dp).verticalScroll(rememberScrollState()),
                verticalArrangement = Arrangement.spacedBy(10.dp)
            ) {
                Text("Purchases are handled by Google Play. Prices and final confirmation are shown by Google Play.", color = EmpireColors.TextSecondary, fontSize = 11.sp)
                if (pendingPurchases.isNotEmpty()) {
                    Text(
                        "PAYMENT PENDING — Google Play has not confirmed this transaction yet. You can safely close and reopen the Store.",
                        color = EmpireColors.Gold,
                        fontSize = 11.sp,
                        fontWeight = FontWeight.Bold
                    )
                }
                StoreRow("REMOVE ADS", "Lifetime removal of non-rewarded advertising. Reward videos remain optional.", StoreProduct.REMOVE_ADS in owned, purchaseInFlight, pendingPurchases, StoreProduct.REMOVE_ADS, MetaSpriteKind.LEGACY) { onPurchase(StoreProduct.REMOVE_ADS) }
                StoreRow("STARTER PACK", "250 gems + 30 min ×2 income. One-time purchase.", StoreProduct.STARTER_PACK in owned, purchaseInFlight, pendingPurchases, StoreProduct.STARTER_PACK, MetaSpriteKind.BOOST) { onPurchase(StoreProduct.STARTER_PACK) }
                StoreRow("120 GEMS", "Consumable gem pack.", false, purchaseInFlight, pendingPurchases, StoreProduct.GEM_PACK_SMALL, MetaSpriteKind.GEM) { onPurchase(StoreProduct.GEM_PACK_SMALL) }
                StoreRow("650 GEMS", "Consumable gem pack.", false, purchaseInFlight, pendingPurchases, StoreProduct.GEM_PACK_MEDIUM, MetaSpriteKind.GEM) { onPurchase(StoreProduct.GEM_PACK_MEDIUM) }
                OutlinedButton(onClick = onRestore, enabled = purchaseInFlight == null, modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)) { Text("RESTORE PURCHASES") }
                if (onDiagnostics != null) {
                    TextButton(onClick = onDiagnostics, modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)) { Text("BILLING DIAGNOSTICS") }
                }
            }
        },
        confirmButton = {
            TextButton(onClick = onDismiss, modifier = Modifier.heightIn(min = 48.dp)) { Text("CLOSE") }
        }
    )
}

@Composable
private fun StoreRow(
    title: String,
    subtitle: String,
    owned: Boolean,
    purchaseInFlight: StoreProduct?,
    pendingPurchases: Set<StoreProduct>,
    product: StoreProduct,
    kind: MetaSpriteKind,
    purchase: () -> Unit
) {
    val pending = product in pendingPurchases
    val processing = purchaseInFlight == product && !pending
    val enabled = !owned && purchaseInFlight == null && !pending
    Surface(color = EmpireColors.Surface, shape = RoundedCornerShape(14.dp)) {
        Row(Modifier.fillMaxWidth().padding(12.dp), verticalAlignment = Alignment.CenterVertically) {
            MetaSprite(kind, 38.dp, active = !owned)
            Spacer(Modifier.width(10.dp))
            Column(Modifier.weight(1f)) {
                Text(title, color = EmpireColors.TextPrimary, fontWeight = FontWeight.Black)
                Text(subtitle, color = EmpireColors.TextSecondary, fontSize = 10.sp)
            }
            Spacer(Modifier.width(8.dp))
            Button(
                onClick = purchase,
                enabled = enabled,
                modifier = Modifier
                    .heightIn(min = 48.dp)
                    .semantics { contentDescription = when { owned -> "$title owned"; pending -> "$title payment pending Google Play confirmation"; processing -> "$title purchase processing"; else -> "Buy $title" } }
            ) {
                Text(when { owned -> "OWNED"; pending -> "PENDING"; processing -> "PROCESSING…"; else -> "BUY" }, fontSize = 10.sp)
            }
        }
    }
}

private tailrec fun Context.findActivity(): Activity? = when (this) {
    is Activity -> this
    is ContextWrapper -> baseContext.findActivity()
    else -> null
}
