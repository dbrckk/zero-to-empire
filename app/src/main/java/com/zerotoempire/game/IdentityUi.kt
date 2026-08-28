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

/** Identity/gameplay presentation root. Persistent HUD controls live inside the scroll layout. */
@Composable
fun EmpireRoot(vm: GameViewModel = viewModel()) {
    val state by vm.state.collectAsStateWithLifecycle()
    val meta by vm.meta.collectAsStateWithLifecycle()
    val celebration by vm.celebration.collectAsStateWithLifecycle()
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
        PremiumZeroToEmpireApp(vm)
        if (!meta.onboardingCompleted) {
            OnboardingOverlay(
                onTapSound = { GameSfxBus.play(PremiumSfxCue.UI, .85f) },
                onComplete = { GameSfxBus.play(PremiumSfxCue.REWARD); vm.completeOnboarding() }
            )
        }
        celebration?.let { item ->
            CelebrationOverlay(
                item = item,
                onShown = { GameSfxBus.play(if (item.accent == "PRESTIGE") PremiumSfxCue.PRESTIGE else PremiumSfxCue.MILESTONE) },
                onDismiss = vm::dismissCelebration
            )
        }
        EraTransitionOverlay(eraIndex = eraIndex, visible = eraTransitionVisible, modifier = Modifier.fillMaxSize())
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
            Text("ZERO → EMPIRE", color = EmpireColors.Gold, fontSize = 28.sp, fontWeight = FontWeight.Black)
            Spacer(Modifier.height(12.dp)); OnboardingStepArt(step); Spacer(Modifier.height(8.dp))
            Text(current.first, color = EmpireColors.TextPrimary, fontSize = 36.sp, fontWeight = FontWeight.Black)
            Spacer(Modifier.height(10.dp))
            Text(current.second, color = EmpireColors.TextSecondary, fontSize = 16.sp, textAlign = TextAlign.Center, lineHeight = 23.sp)
            Spacer(Modifier.height(14.dp))
            Surface(shape = RoundedCornerShape(50), color = EmpireColors.SurfaceHigh) { Text(current.third, modifier = Modifier.padding(horizontal = 18.dp, vertical = 9.dp), color = EmpireColors.Cyan, fontWeight = FontWeight.Bold, fontSize = 12.sp) }
            Spacer(Modifier.height(22.dp))
            LinearProgressIndicator(progress = { (step + 1) / steps.size.toFloat() }, modifier = Modifier.fillMaxWidth().height(5.dp), color = EmpireColors.Gold, trackColor = EmpireColors.SurfaceHigh)
            Spacer(Modifier.height(16.dp))
            Button(onClick = { onTapSound(); if (step == steps.lastIndex) onComplete() else step++ }, modifier = Modifier.fillMaxWidth(), shape = RoundedCornerShape(16.dp)) {
                Text(if (step == steps.lastIndex) "BUILD MY EMPIRE" else "CONTINUE", fontWeight = FontWeight.Black)
            }
        }
    }
}

@Composable
private fun CelebrationOverlay(item: MajorCelebration, onShown: () -> Unit, onDismiss: () -> Unit) {
    var visible by remember(item) { mutableStateOf(true) }
    LaunchedEffect(item) { onShown(); delay(2100); visible = false; delay(280); onDismiss() }
    if (!visible) return
    Box(Modifier.fillMaxSize().background(EmpireColors.Void.copy(alpha = .72f)), contentAlignment = Alignment.Center) {
        Surface(shape = RoundedCornerShape(28.dp), color = EmpireColors.SurfaceHigh, shadowElevation = 28.dp, modifier = Modifier.padding(24.dp)) {
            Column(Modifier.padding(28.dp), horizontalAlignment = Alignment.CenterHorizontally) {
                MetaSprite(MetaSpriteKind.ACHIEVEMENT, 76.dp)
                Spacer(Modifier.height(14.dp))
                Text(item.accent, color = EmpireColors.Gold, fontSize = 12.sp, fontWeight = FontWeight.Black, letterSpacing = 2.sp)
                Text(item.title, color = EmpireColors.TextPrimary, fontSize = 28.sp, fontWeight = FontWeight.Black, textAlign = TextAlign.Center)
                Spacer(Modifier.height(8.dp))
                Text(item.subtitle, color = EmpireColors.TextSecondary, fontSize = 13.sp, textAlign = TextAlign.Center)
            }
        }
    }
}