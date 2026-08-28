package com.zerotoempire.game

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlinx.coroutines.delay
import kotlin.math.cos
import kotlin.math.sin

private val premiumMilestones = intArrayOf(10, 25, 50, 100, 250, 500, 1000)

@Composable
fun PremiumProgressionStrip(state: GameState) {
    val next = ContentUnlocks.nextHiddenBusiness(state)
    val era = EmpireEras.current(state.lifetimeCash)
    val unlockProgress = if (next == null) 1f else ContentUnlocks.progressToNextUnlock(state)
    Surface(
        color = EmpireColors.Surface.copy(alpha = .72f),
        shape = RoundedCornerShape(20.dp),
        modifier = Modifier.fillMaxWidth().border(1.dp, EmpireColors.Cyan.copy(alpha = .10f), RoundedCornerShape(20.dp))
    ) {
        Column(Modifier.padding(horizontal = 15.dp, vertical = 12.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Column(Modifier.weight(1f)) {
                    Text("EMPIRE MOMENTUM", color = EmpireColors.Cyan, fontSize = 9.sp, fontWeight = FontWeight.Black, letterSpacing = 1.5.sp)
                    Text(if (next == null) "All asset classes revealed" else "Next: ${next.name}", color = EmpireColors.TextPrimary, fontSize = 13.sp, fontWeight = FontWeight.Black)
                }
                Text("ERA ${era.index + 1}/11", color = EmpireColors.Gold, fontSize = 10.sp, fontWeight = FontWeight.Black)
            }
            Spacer(Modifier.height(8.dp))
            LinearProgressIndicator(progress = { unlockProgress.coerceIn(0f, 1f) }, modifier = Modifier.fillMaxWidth().height(4.dp), color = EmpireColors.Cyan, trackColor = EmpireColors.SurfaceHigh)
        }
    }
}

@Composable
fun PremiumMilestoneCelebration(state: GameState, modifier: Modifier = Modifier) {
    var knownLevels by remember { mutableStateOf(state.businesses.associate { it.id to it.level }) }
    var serial by remember { mutableIntStateOf(0) }
    var title by remember { mutableStateOf("") }
    var subtitle by remember { mutableStateOf("") }
    var visible by remember { mutableStateOf(false) }

    LaunchedEffect(state.businesses) {
        val previous = knownLevels
        val hit = state.businesses.firstOrNull { business ->
            val old = previous[business.id] ?: business.level
            business.level > old && premiumMilestones.any { it in (old + 1)..business.level }
        }
        knownLevels = state.businesses.associate { it.id to it.level }
        if (hit != null) {
            val old = previous[hit.id] ?: 0
            val reached = premiumMilestones.lastOrNull { it in (old + 1)..hit.level } ?: hit.level
            title = "POWER SPIKE  •  LV $reached"
            subtitle = hit.name.uppercase()
            serial++
            val token = serial
            visible = true
            delay(1350)
            if (token == serial) visible = false
        }
    }

    AnimatedVisibility(visible, enter = fadeIn(tween(160)), exit = fadeOut(tween(300)), modifier = modifier) {
        Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
            PremiumBurst(serial)
            Surface(
                color = EmpireColors.DeepSpace.copy(alpha = .95f),
                shape = RoundedCornerShape(24.dp),
                modifier = Modifier.padding(34.dp).border(1.dp, EmpireColors.GoldBright.copy(alpha = .65f), RoundedCornerShape(24.dp))
            ) {
                Column(Modifier.padding(horizontal = 26.dp, vertical = 20.dp), horizontalAlignment = Alignment.CenterHorizontally) {
                    Text(title, color = EmpireColors.GoldBright, fontSize = 12.sp, fontWeight = FontWeight.Black, letterSpacing = 1.2.sp)
                    Text(subtitle, color = EmpireColors.TextPrimary, fontSize = 20.sp, fontWeight = FontWeight.Black)
                    Text("Production evolved", color = EmpireColors.Cyan, fontSize = 10.sp, fontWeight = FontWeight.Bold)
                }
            }
        }
    }
}

@Composable
private fun PremiumBurst(seed: Int) {
    val context = LocalContext.current
    val reduced = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val progress: Float
    if (reduced) progress = .72f else {
        val transition = rememberInfiniteTransition(label = "premiumBurst$seed")
        val p by transition.animateFloat(
            initialValue = 0f,
            targetValue = 1f,
            animationSpec = infiniteRepeatable(
                animation = tween(durationMillis = 900, easing = FastOutSlowInEasing),
                repeatMode = RepeatMode.Restart
            ),
            label = "burst"
        )
        progress = p
    }
    Canvas(Modifier.fillMaxSize()) {
        val center = Offset(size.width / 2f, size.height / 2f)
        val count = if (lowPower) 10 else 20
        val radius = size.minDimension * (.16f + .34f * progress)
        drawCircle(EmpireColors.Gold.copy(alpha = (.18f * (1f - progress)).coerceAtLeast(.03f)), radius * .72f, center, style = Stroke(size.minDimension * .008f))
        repeat(count) { i ->
            val angle = i * (Math.PI * 2.0 / count) + seed * .17
            val start = radius * .45f
            val end = radius * (if (i % 3 == 0) 1f else .78f)
            val a = (.62f * (1f - progress)).coerceAtLeast(.06f)
            val color = if (i % 2 == 0) EmpireColors.GoldBright else EmpireColors.Cyan
            drawLine(color.copy(alpha = a), Offset(center.x + cos(angle).toFloat() * start, center.y + sin(angle).toFloat() * start), Offset(center.x + cos(angle).toFloat() * end, center.y + sin(angle).toFloat() * end), size.minDimension * .006f)
        }
    }
}
