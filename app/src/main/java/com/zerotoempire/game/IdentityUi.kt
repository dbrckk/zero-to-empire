package com.zerotoempire.game

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
    val audio = remember { GameAudioEngine() }

    DisposableEffect(Unit) { onDispose { audio.release() } }

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
            EraHud(state)
        }

        celebration?.let { item ->
            CelebrationOverlay(
                item = item,
                onShown = {
                    if (item.accent == "PRESTIGE") audio.prestige() else audio.milestone()
                },
                onDismiss = vm::dismissCelebration
            )
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
        Modifier.fillMaxSize().background(Brush.verticalGradient(listOf(EmpireColors.Void, EmpireColors.DeepSpace))),
        contentAlignment = Alignment.Center
    ) {
        Column(
            Modifier.fillMaxWidth().padding(28.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
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
            LinearProgressIndicator(
                progress = { (step + 1) / steps.size.toFloat() },
                modifier = Modifier.fillMaxWidth().height(5.dp),
                color = EmpireColors.Gold,
                trackColor = EmpireColors.SurfaceHigh
            )
            Spacer(Modifier.height(18.dp))
            Button(
                onClick = {
                    onTapSound()
                    if (step == steps.lastIndex) onComplete() else step++
                },
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(16.dp)
            ) {
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

    Column(
        Modifier.fillMaxWidth().padding(top = 6.dp, start = 72.dp, end = 72.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Surface(shape = RoundedCornerShape(50), color = EmpireColors.Void.copy(alpha = .88f)) {
            Row(Modifier.padding(horizontal = 12.dp, vertical = 6.dp), verticalAlignment = Alignment.CenterVertically) {
                Text(current.icon, color = EmpireColors.Gold, fontSize = 12.sp)
                Spacer(Modifier.width(6.dp))
                Text(current.name, color = EmpireColors.TextPrimary, fontSize = 9.sp, fontWeight = FontWeight.Black)
            }
        }
        Spacer(Modifier.height(3.dp))
        LinearProgressIndicator(progress = { fraction }, modifier = Modifier.fillMaxWidth().height(2.dp), color = EmpireColors.Gold, trackColor = EmpireColors.SurfaceHigh.copy(alpha = .6f))
    }
}

@Composable
private fun CelebrationOverlay(item: MajorCelebration, onShown: () -> Unit, onDismiss: () -> Unit) {
    var visible by remember(item) { mutableStateOf(false) }

    LaunchedEffect(item) {
        visible = true
        onShown()
        delay(1800)
        visible = false
        delay(260)
        onDismiss()
    }

    AnimatedVisibility(
        visible = visible,
        enter = fadeIn() + scaleIn(initialScale = .82f),
        exit = fadeOut() + scaleOut(targetScale = 1.08f),
        modifier = Modifier.fillMaxSize()
    ) {
        Box(
            Modifier.fillMaxSize().background(EmpireColors.Void.copy(alpha = .88f)),
            contentAlignment = Alignment.Center
        ) {
            Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.padding(32.dp)) {
                Text(item.accent, color = EmpireColors.Cyan, fontWeight = FontWeight.Black, fontSize = 12.sp, letterSpacing = 2.sp)
                Spacer(Modifier.height(16.dp))
                Text(item.icon, fontSize = 72.sp)
                Spacer(Modifier.height(18.dp))
                Text(item.title, color = EmpireColors.GoldBright, fontWeight = FontWeight.Black, fontSize = 30.sp, textAlign = TextAlign.Center)
                Spacer(Modifier.height(8.dp))
                Text(item.subtitle, color = EmpireColors.TextSecondary, fontSize = 15.sp, textAlign = TextAlign.Center)
            }
        }
    }
}
