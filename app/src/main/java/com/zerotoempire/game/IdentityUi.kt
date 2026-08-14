package com.zerotoempire.game

import android.app.Activity
import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.scaleIn
import androidx.compose.animation.scaleOut
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import kotlinx.coroutines.delay

@Composable
fun EmpireRoot(vm: GameViewModel = viewModel()) {
    val state by vm.state.collectAsStateWithLifecycle()
    val meta by vm.meta.collectAsStateWithLifecycle()
    val celebration by vm.celebration.collectAsStateWithLifecycle()
    val context = LocalContext.current
    val activity = context as? Activity
    val audio = remember { GameAudioEngine() }
    val rewarded = remember { AdMobRewardedGateway(context.applicationContext) }
    val billing = remember { PlayBillingGateway(context.applicationContext) }

    DisposableEffect(Unit) {
        billing.connect()
        onDispose {
            audio.release()
            billing.disconnect()
        }
    }

    LaunchedEffect(Unit) {
        delay(900)
        billing.restore(vm::applyEntitlements)
    }

    Box(Modifier.fillMaxSize()) {
        ZeroToEmpireApp(vm)

        if (!meta.onboardingCompleted) {
            OnboardingOverlay(
                onTapSound = audio::tap,
                onComplete = {
                    audio.reward()
                    vm.completeOnboarding()
                }
            )
        } else {
            Column(modifier = Modifier.fillMaxWidth(), horizontalAlignment = Alignment.CenterHorizontally) {
                EraHud(state)
                Spacer(Modifier.height(5.dp))
                ViralShareChip(state)
            }
            if (activity != null) {
                MonetizationDock(
                    modifier = Modifier.align(Alignment.BottomEnd).padding(end = 14.dp, bottom = 88.dp),
                    activity = activity,
                    meta = meta,
                    rewarded = rewarded,
                    billing = billing,
                    vm = vm
                )
            }
        }

        celebration?.let { item ->
            CelebrationOverlay(
                item = item,
                onShown = { if (item.accent == "PRESTIGE") audio.prestige() else audio.milestone() },
                onDismiss = vm::dismissCelebration
            )
        }
    }
}

@Composable
private fun MonetizationDock(
    modifier: Modifier,
    activity: Activity,
    meta: PlayerMeta,
    rewarded: RewardedAdGateway,
    billing: PurchaseGateway,
    vm: GameViewModel
) {
    var storeOpen by remember { mutableStateOf(false) }
    var status by remember { mutableStateOf<String?>(null) }

    Column(modifier, horizontalAlignment = Alignment.End, verticalArrangement = Arrangement.spacedBy(8.dp)) {
        FilledTonalButton(
            onClick = {
                rewarded.show(activity, RewardPlacement.PROFIT_BOOST, onReward = vm::rewardProfitBoost) {
                    if (!rewarded.isReady()) rewarded.preload()
                }
            },
            shape = RoundedCornerShape(50)
        ) { Text("▶ ×2 BOOST", fontWeight = FontWeight.Black, fontSize = 11.sp) }

        Button(onClick = { storeOpen = true }, shape = RoundedCornerShape(50)) {
            Text(if (meta.adsRemoved) "◆ STORE" else "◆ STORE + NO ADS", fontWeight = FontWeight.Black, fontSize = 11.sp)
        }
    }

    if (storeOpen) {
        AlertDialog(
            onDismissRequest = { storeOpen = false },
            containerColor = EmpireColors.SurfaceHigh,
            title = { Text("EMPIRE STORE", color = EmpireColors.Gold, fontWeight = FontWeight.Black) },
            text = {
                Column(verticalArrangement = Arrangement.spacedBy(9.dp)) {
                    Text("Permanent upgrades and optional currency. Core progression remains playable without purchases.", color = EmpireColors.TextSecondary, fontSize = 12.sp)
                    StoreButton(
                        title = if (meta.adsRemoved) "ADS REMOVED ✓" else "REMOVE ADS — LIFETIME",
                        enabled = !meta.adsRemoved,
                        onClick = { buy(activity, billing, StoreProduct.REMOVE_ADS, vm, { status = it }) }
                    )
                    StoreButton(
                        title = if (meta.starterPackOwned) "STARTER PACK OWNED ✓" else "STARTER PACK — 250 GEMS",
                        enabled = !meta.starterPackOwned,
                        onClick = { buy(activity, billing, StoreProduct.STARTER_PACK, vm, { status = it }) }
                    )
                    StoreButton("120 GEMS", true) { buy(activity, billing, StoreProduct.GEM_PACK_SMALL, vm, { status = it }) }
                    StoreButton("650 GEMS", true) { buy(activity, billing, StoreProduct.GEM_PACK_MEDIUM, vm, { status = it }) }
                    OutlinedButton(
                        onClick = {
                            billing.restore {
                                vm.applyEntitlements(it)
                                status = "Purchases restored"
                            }
                        },
                        modifier = Modifier.fillMaxWidth()
                    ) { Text("RESTORE PURCHASES") }
                    status?.let { Text(it, color = EmpireColors.Cyan, fontSize = 11.sp) }
                }
            },
            confirmButton = { TextButton(onClick = { storeOpen = false }) { Text("CLOSE") } }
        )
    }
}

private fun buy(
    activity: Activity,
    billing: PurchaseGateway,
    product: StoreProduct,
    vm: GameViewModel,
    status: (String) -> Unit
) {
    billing.purchase(activity, product) { result ->
        when (result) {
            is PurchaseResult.Success -> { vm.applyPurchase(result.product); status("Purchase complete") }
            PurchaseResult.Cancelled -> status("Purchase cancelled")
            PurchaseResult.Pending -> status("Purchase pending")
            is PurchaseResult.Failed -> status(result.reason)
        }
    }
}

@Composable
private fun StoreButton(title: String, enabled: Boolean, onClick: () -> Unit) {
    Button(onClick = onClick, enabled = enabled, modifier = Modifier.fillMaxWidth(), shape = RoundedCornerShape(14.dp)) {
        Text(title, fontWeight = FontWeight.Bold, fontSize = 11.sp)
    }
}

@Composable
private fun OnboardingOverlay(onTapSound: () -> Unit, onComplete: () -> Unit) {
    var step by remember { mutableIntStateOf(0) }
    val steps = listOf(
        Triple("ZERO", "You start with almost nothing. Tap to create your first capital.", "TAP → EARN"),
        Triple("BUILD", "Buy assets. Every level increases automatic income.", "EARN → INVEST"),
        Triple("SCALE", "Hit power-spike levels to multiply production dramatically.", "10 • 25 • 50 • 100"),
        Triple("AUTOMATE", "Hire managers, stack upgrades and keep earning while offline.", "SYSTEMS → MOMENTUM"),
        Triple("ASCEND", "When growth slows, reset the run for permanent Legacy power.", "RESET → RETURN STRONGER")
    )
    val current = steps[step]

    Box(Modifier.fillMaxSize().background(Brush.verticalGradient(listOf(EmpireColors.Void, EmpireColors.DeepSpace))), contentAlignment = Alignment.Center) {
        Column(Modifier.fillMaxWidth().padding(28.dp), horizontalAlignment = Alignment.CenterHorizontally) {
            Text("ZERO → EMPIRE", color = EmpireColors.Gold, fontSize = 30.sp, fontWeight = FontWeight.Black)
            Spacer(Modifier.height(48.dp))
            Text(current.first, color = EmpireColors.TextPrimary, fontSize = 42.sp, fontWeight = FontWeight.Black)
            Spacer(Modifier.height(14.dp))
            Text(current.second, color = EmpireColors.TextSecondary, fontSize = 17.sp, textAlign = TextAlign.Center, lineHeight = 25.sp)
            Spacer(Modifier.height(20.dp))
            Surface(shape = RoundedCornerShape(50), color = EmpireColors.SurfaceHigh) {
                Text(current.third, modifier = Modifier.padding(horizontal = 18.dp, vertical = 9.dp), color = EmpireColors.Cyan, fontWeight = FontWeight.Bold, fontSize = 12.sp)
            }
            Spacer(Modifier.height(50.dp))
            LinearProgressIndicator(progress = { (step + 1) / steps.size.toFloat() }, modifier = Modifier.fillMaxWidth().height(5.dp), color = EmpireColors.Gold, trackColor = EmpireColors.SurfaceHigh)
            Spacer(Modifier.height(18.dp))
            Button(onClick = { onTapSound(); if (step == steps.lastIndex) onComplete() else step++ }, modifier = Modifier.fillMaxWidth(), shape = RoundedCornerShape(16.dp)) {
                Text(if (step == steps.lastIndex) "BUILD MY EMPIRE" else "CONTINUE", fontWeight = FontWeight.Black)
            }
        }
    }
}

@Composable
private fun EraHud(state: GameState) {
    val current = EmpireEras.current(state.lifetimeCash)
    val next = EmpireEras.next(state.lifetimeCash)
    val fraction = if (next == null) 1f else {
        val span = (next.requiredLifetimeCash - current.requiredLifetimeCash).coerceAtLeast(1.0)
        ((state.lifetimeCash - current.requiredLifetimeCash) / span).toFloat().coerceIn(0f, 1f)
    }
    Surface(
        modifier = Modifier.fillMaxWidth().padding(top = 6.dp, start = 62.dp, end = 62.dp).height(74.dp),
        shape = RoundedCornerShape(18.dp),
        color = EmpireColors.Void.copy(alpha = .90f),
        shadowElevation = 10.dp
    ) {
        Box(Modifier.fillMaxSize()) {
            EraVista(current.index, Modifier.fillMaxSize())
            Column(
                Modifier.fillMaxSize().background(Brush.verticalGradient(listOf(EmpireColors.Void.copy(alpha = .18f), EmpireColors.Void.copy(alpha = .78f)))).padding(horizontal = 12.dp, vertical = 8.dp),
                verticalArrangement = Arrangement.Bottom
            ) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Text(current.icon, color = EmpireColors.Gold, fontSize = 13.sp)
                    Spacer(Modifier.width(6.dp))
                    Text(current.name, color = EmpireColors.TextPrimary, fontSize = 10.sp, fontWeight = FontWeight.Black)
                    Spacer(Modifier.weight(1f))
                    next?.let { Text("NEXT: ${it.name}", color = EmpireColors.TextSecondary, fontSize = 8.sp, fontWeight = FontWeight.Bold) }
                }
                Spacer(Modifier.height(5.dp))
                LinearProgressIndicator(progress = { fraction }, modifier = Modifier.fillMaxWidth().height(3.dp), color = EmpireColors.Gold, trackColor = EmpireColors.SurfaceHigh.copy(alpha = .75f))
            }
        }
    }
}

@Composable
private fun CelebrationOverlay(item: MajorCelebration, onShown: () -> Unit, onDismiss: () -> Unit) {
    var visible by remember(item) { mutableStateOf(false) }
    LaunchedEffect(item) { visible = true; onShown(); delay(2100); visible = false; delay(280); onDismiss() }
    AnimatedVisibility(visible = visible, enter = fadeIn() + scaleIn(initialScale = .82f), exit = fadeOut() + scaleOut(targetScale = 1.08f), modifier = Modifier.fillMaxSize()) {
        Box(Modifier.fillMaxSize().background(EmpireColors.Void.copy(alpha = .92f)), contentAlignment = Alignment.Center) {
            CelebrationVfx(item.accent, Modifier.fillMaxSize())
            Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.padding(32.dp)) {
                Surface(shape = RoundedCornerShape(50), color = EmpireColors.SurfaceHigh.copy(alpha = .86f)) {
                    Text(item.accent, modifier = Modifier.padding(horizontal = 14.dp, vertical = 7.dp), color = EmpireColors.Cyan, fontWeight = FontWeight.Black, fontSize = 11.sp, letterSpacing = 2.sp)
                }
                Spacer(Modifier.height(18.dp))
                Text(item.icon, fontSize = 72.sp)
                Spacer(Modifier.height(18.dp))
                Text(item.title, color = EmpireColors.GoldBright, fontWeight = FontWeight.Black, fontSize = 30.sp, textAlign = TextAlign.Center)
                Spacer(Modifier.height(8.dp))
                Text(item.subtitle, color = EmpireColors.TextSecondary, fontSize = 15.sp, textAlign = TextAlign.Center)
            }
        }
    }
}
