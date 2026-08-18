package com.zerotoempire.game

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import kotlinx.coroutines.delay

/**
 * Identity/gameplay presentation root.
 *
 * Monetization deliberately lives in CommerceRoot only. Keeping ads, privacy consent and billing
 * outside this layer prevents duplicate BillingClient/AdMob instances and guarantees that every
 * rewarded-ad request passes through the consent-aware commerce flow.
 */
@Composable
fun EmpireRoot(vm: GameViewModel = viewModel()) {
    val state by vm.state.collectAsStateWithLifecycle()
    val meta by vm.meta.collectAsStateWithLifecycle()
    val celebration by vm.celebration.collectAsStateWithLifecycle()
    val buyMode by vm.buyMode.collectAsStateWithLifecycle()
    val eraIndex = EmpireEras.current(state.lifetimeCash).index
    var previousEra by remember { mutableIntStateOf(eraIndex) }
    var eraTransitionVisible by remember { mutableStateOf(false) }

    LaunchedEffect(eraIndex) {
        if (eraIndex > previousEra && meta.onboardingCompleted) {
            eraTransitionVisible = true
            GameSfxBus.play(PremiumSfxCue.PRESTIGE)
            delay(1550)
            eraTransitionVisible = false
        }
        previousEra = eraIndex
    }

    Box(Modifier.fillMaxSize()) {
        ZeroToEmpireApp(vm)

        if (!meta.onboardingCompleted) {
            OnboardingOverlay(
                onTapSound = { GameSfxBus.play(PremiumSfxCue.UI, .85f) },
                onComplete = {
                    GameSfxBus.play(PremiumSfxCue.REWARD)
                    vm.completeOnboarding()
                }
            )
        } else {
            Column(
                modifier = Modifier.fillMaxWidth(),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                EraHud(state)
                Spacer(Modifier.height(5.dp))
                ViralShareChip(state)
                Spacer(Modifier.height(5.dp))
                BulkBuySelector(selected = buyMode, onSelect = vm::setBuyMode)
            }
        }

        celebration?.let { item ->
            CelebrationOverlay(
                item = item,
                onShown = {
                    GameSfxBus.play(
                        if (item.accent == "PRESTIGE") PremiumSfxCue.PRESTIGE else PremiumSfxCue.MILESTONE
                    )
                },
                onDismiss = vm::dismissCelebration
            )
        }

        EraTransitionOverlay(
            eraIndex = eraIndex,
            visible = eraTransitionVisible,
            modifier = Modifier.fillMaxSize()
        )
    }
}

@Composable
private fun BulkBuySelector(selected: BuyMode, onSelect: (BuyMode) -> Unit) {
    val modes = listOf(
        BuyMode.X1 to "×1",
        BuyMode.X10 to "×10",
        BuyMode.X25 to "×25",
        BuyMode.MILESTONE to "NEXT",
        BuyMode.MAX to "MAX"
    )

    Surface(
        color = EmpireColors.Void.copy(alpha = .91f),
        shape = RoundedCornerShape(18.dp),
        shadowElevation = 8.dp
    ) {
        Row(
            modifier = Modifier.padding(horizontal = 7.dp, vertical = 6.dp),
            horizontalArrangement = Arrangement.spacedBy(5.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            MetaSprite(MetaSpriteKind.CASH, 24.dp)
            modes.forEach { (mode, label) ->
                if (mode == selected) {
                    Button(
                        onClick = { onSelect(mode) },
                        contentPadding = PaddingValues(horizontal = 10.dp, vertical = 2.dp),
                        modifier = Modifier.height(30.dp),
                        shape = RoundedCornerShape(10.dp)
                    ) {
                        Text(label, fontSize = 9.sp, fontWeight = FontWeight.Black)
                    }
                } else {
                    TextButton(
                        onClick = { onSelect(mode) },
                        contentPadding = PaddingValues(horizontal = 9.dp, vertical = 2.dp),
                        modifier = Modifier.height(30.dp),
                        shape = RoundedCornerShape(10.dp)
                    ) {
                        Text(
                            label,
                            fontSize = 9.sp,
                            fontWeight = FontWeight.Bold,
                            color = EmpireColors.TextSecondary
                        )
                    }
                }
            }
        }
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

    Box(
        Modifier
            .fillMaxSize()
            .background(Brush.verticalGradient(listOf(EmpireColors.Void, EmpireColors.DeepSpace))),
        contentAlignment = Alignment.Center
    ) {
        Column(
            Modifier.fillMaxWidth().padding(28.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text("ZERO → EMPIRE", color = EmpireColors.Gold, fontSize = 28.sp, fontWeight = FontWeight.Black)
            Spacer(Modifier.height(12.dp))
            OnboardingStepArt(step)
            Spacer(Modifier.height(8.dp))
            Text(current.first, color = EmpireColors.TextPrimary, fontSize = 36.sp, fontWeight = FontWeight.Black)
            Spacer(Modifier.height(10.dp))
            Text(
                current.second,
                color = EmpireColors.TextSecondary,
                fontSize = 16.sp,
                textAlign = TextAlign.Center,
                lineHeight = 23.sp
            )
            Spacer(Modifier.height(14.dp))
            Surface(shape = RoundedCornerShape(50), color = EmpireColors.SurfaceHigh) {
                Text(
                    current.third,
                    modifier = Modifier.padding(horizontal = 18.dp, vertical = 9.dp),
                    color = EmpireColors.Cyan,
                    fontWeight = FontWeight.Bold,
                    fontSize = 12.sp
                )
            }
            Spacer(Modifier.height(22.dp))
            LinearProgressIndicator(
                progress = { (step + 1) / steps.size.toFloat() },
                modifier = Modifier.fillMaxWidth().height(5.dp),
                color = EmpireColors.Gold,
                trackColor = EmpireColors.SurfaceHigh
            )
            Spacer(Modifier.height(16.dp))
            Button(
                onClick = {
                    onTapSound()
                    if (step == steps.lastIndex) onComplete() else step++
                },
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(16.dp)
            ) {
                Text(
                    if (step == steps.lastIndex) "BUILD MY EMPIRE" else "CONTINUE",
                    fontWeight = FontWeight.Black
                )
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
        modifier = Modifier
            .fillMaxWidth()
            .padding(top = 6.dp, start = 62.dp, end = 62.dp)
            .height(74.dp),
        shape = RoundedCornerShape(18.dp),
        color = EmpireColors.Void.copy(alpha = .90f),
        shadowElevation = 10.dp
    ) {
        Box(Modifier.fillMaxSize()) {
            EraVista(current.index, Modifier.fillMaxSize())
            Column(
                Modifier
                    .fillMaxSize()
                    .background(
                        Brush.verticalGradient(
                            listOf(EmpireColors.Void.copy(alpha = .18f), EmpireColors.Void.copy(alpha = .78f))
                        )
                    )
                    .padding(horizontal = 12.dp, vertical = 8.dp),
                verticalArrangement = Arrangement.Bottom
            ) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    MetaSprite(MetaSpriteKind.LEGACY, 22.dp)
                    Spacer(Modifier.width(6.dp))
                    Text(current.name, color = EmpireColors.TextPrimary, fontSize = 10.sp, fontWeight = FontWeight.Black)
                    Spacer(Modifier.weight(1f))
                    next?.let {
                        Text(
                            "NEXT: ${it.name}",
                            color = EmpireColors.TextSecondary,
                            fontSize = 8.sp,
                            fontWeight = FontWeight.Bold
                        )
                    }
                }
                Spacer(Modifier.height(5.dp))
                LinearProgressIndicator(
                    progress = { fraction },
                    modifier = Modifier.fillMaxWidth().height(3.dp),
                    color = EmpireColors.Gold,
                    trackColor = EmpireColors.SurfaceHigh.copy(alpha = .75f)
                )
            }
        }
    }
}

@Composable
private fun CelebrationOverlay(item: MajorCelebration, onShown: () -> Unit, onDismiss: () -> Unit) {
    var visible by remember(item) { mutableStateOf(true) }
    LaunchedEffect(item) {
        onShown()
        delay(2100)
        visible = false
        delay(280)
        onDismiss()
    }
    if (!visible) return

    Box(
        Modifier.fillMaxSize().background(EmpireColors.Void.copy(alpha = .92f)),
        contentAlignment = Alignment.Center
    ) {
        CelebrationVfx(item.accent, Modifier.fillMaxSize())
        Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.padding(32.dp)) {
            Surface(shape = RoundedCornerShape(50), color = EmpireColors.SurfaceHigh.copy(alpha = .86f)) {
                Text(
                    item.accent,
                    modifier = Modifier.padding(horizontal = 14.dp, vertical = 7.dp),
                    color = EmpireColors.Cyan,
                    fontWeight = FontWeight.Black,
                    fontSize = 11.sp,
                    letterSpacing = 2.sp
                )
            }
            Spacer(Modifier.height(18.dp))
            val businessId = item.businessId
            if (businessId != null) {
                Box(Modifier.size(124.dp), contentAlignment = Alignment.Center) {
                    CelebrationBusinessSprite(businessId, item.businessLevel ?: 0, 116.dp)
                }
            } else {
                val kind = if (item.accent == "PRESTIGE") MetaSpriteKind.LEGACY else MetaSpriteKind.ACHIEVEMENT
                MetaSprite(kind, 96.dp)
            }
            Spacer(Modifier.height(18.dp))
            Text(
                item.title,
                color = EmpireColors.GoldBright,
                fontWeight = FontWeight.Black,
                fontSize = 30.sp,
                textAlign = TextAlign.Center
            )
            Spacer(Modifier.height(8.dp))
            Text(
                item.subtitle,
                color = EmpireColors.TextSecondary,
                fontSize = 15.sp,
                textAlign = TextAlign.Center
            )
        }
    }
}
