package com.zerotoempire.game

import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.alpha
import androidx.compose.ui.draw.scale
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlin.math.ceil
import kotlin.math.cos
import kotlin.math.sin

private val campaignMilestones = listOf(10.0, 120.0, 1_500.0, 25_000.0, 500_000.0, 12_000_000.0, 350_000_000.0, 18_000_000_000.0, 2.5e12, 4e15, 2e18, 8e21, 3e25, 1.2e29, 1e30)

@Composable
fun PremiumCampaignPulse(state: GameState) {
    val current = state.lifetimeCash.coerceAtLeast(0.0)
    val next = campaignMilestones.firstOrNull { it > current } ?: campaignMilestones.last()
    val previous = campaignMilestones.lastOrNull { it <= current } ?: 0.0
    val denominator = (next - previous).coerceAtLeast(1.0)
    val progress = ((current - previous) / denominator).toFloat().coerceIn(0f, 1f)
    val remaining = (next - current).coerceAtLeast(0.0)
    Surface(
        color = EmpireColors.Surface.copy(alpha = .78f),
        shape = RoundedCornerShape(20.dp),
        modifier = Modifier.fillMaxWidth().border(1.dp, EmpireColors.Cyan.copy(alpha = .12f), RoundedCornerShape(20.dp))
    ) {
        Column(Modifier.padding(14.dp)) {
            Row(Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                Column(Modifier.weight(1f)) {
                    Text("NEXT BREAKTHROUGH", color = EmpireColors.Cyan, fontSize = 9.sp, fontWeight = FontWeight.Black, letterSpacing = 1.4.sp)
                    Text(if (remaining > 0.0) "$${EmpireNumberFormat.compact(remaining)} TO NEXT TIER" else "TRANSCENDENCE RANGE", color = EmpireColors.TextPrimary, fontSize = 13.sp, fontWeight = FontWeight.Black)
                }
                Text("${(progress * 100).toInt()}%", color = EmpireColors.Gold, fontSize = 12.sp, fontWeight = FontWeight.Black)
            }
            Spacer(Modifier.height(9.dp))
            LinearProgressIndicator(progress = { progress }, modifier = Modifier.fillMaxWidth().height(5.dp), color = EmpireColors.Cyan, trackColor = EmpireColors.SurfaceHigh)
        }
    }
}

/**
 * Lightweight hero VFX for the Power Core. The effect stays Canvas-based so
 * the composable count is fixed, and automatically scales down in low-power
 * and reduced-motion modes. Reduced-motion is truly static: no infinite
 * animation clock is created at all.
 */
@Composable
fun PremiumCoreAura(eraIndex: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)
    val accent = when (eraIndex) {
        in 0..2 -> EmpireColors.Gold
        in 3..5 -> EmpireColors.Cyan
        in 6..8 -> EmpireColors.Violet
        else -> EmpireColors.GoldBright
    }

    var pulse = 1f
    var auraAlpha = .26f
    var phase = 32f
    if (!reducedMotion) {
        val transition = rememberInfiniteTransition(label = "coreAura")
        val masterDurationMs = if (lowPower) 399_000 else 70_200
        val masterAnimated by transition.animateFloat(
            initialValue = 0f,
            targetValue = masterDurationMs.toFloat(),
            animationSpec = infiniteRepeatable(
                tween(masterDurationMs, easing = LinearEasing),
                RepeatMode.Restart
            ),
            label = "coreAuraMaster"
        )
        val pulseHalfCycleMs = if (lowPower) 1_900f else 1_300f
        val pulseCycle = (masterAnimated % (pulseHalfCycleMs * 2f)) / pulseHalfCycleMs
        val pulseFraction = if (pulseCycle <= 1f) pulseCycle else 2f - pulseCycle
        val easedPulse = FastOutSlowInEasing.transform(pulseFraction)
        val pulseMin = if (lowPower) .97f else .94f
        val pulseMax = if (lowPower) 1.025f else 1.045f
        val alphaMin = if (lowPower) .16f else .20f
        val alphaMax = if (lowPower) .30f else .46f
        val phaseCycleMs = if (lowPower) 10_500f else 5_400f
        pulse = pulseMin + (pulseMax - pulseMin) * easedPulse
        auraAlpha = alphaMin + (alphaMax - alphaMin) * easedPulse
        phase = (masterAnimated % phaseCycleMs) / phaseCycleMs * 360f
    }

    Box(modifier, contentAlignment = Alignment.Center) {
        Box(
            Modifier.fillMaxSize().scale(pulse).alpha(auraAlpha).background(
                Brush.radialGradient(
                    listOf(
                        accent.copy(alpha = if (lowPower) .62f else .80f),
                        accent.copy(alpha = if (lowPower) .09f else .14f),
                        Color.Transparent
                    )
                ),
                CircleShape
            )
        )

        Canvas(Modifier.fillMaxSize()) {
            val center = Offset(size.width / 2f, size.height / 2f)
            val min = size.minDimension
            val orbitCount = if (lowPower) 4 else 12
            val phaseRad = Math.toRadians(phase.toDouble())

            drawCircle(
                color = accent.copy(alpha = if (lowPower) .34f else .48f),
                radius = min * .43f,
                center = center,
                style = Stroke(width = min * .006f)
            )
            if (!lowPower) {
                drawCircle(
                    color = Color.White.copy(alpha = .14f),
                    radius = min * .34f,
                    center = center,
                    style = Stroke(width = min * .004f)
                )
            }

            repeat(orbitCount) { index ->
                val angle = phaseRad + index * (Math.PI * 2.0 / orbitCount)
                val radius = min * if (index % 3 == 0) .46f else .405f
                val dot = Offset(
                    x = center.x + cos(angle).toFloat() * radius,
                    y = center.y + sin(angle).toFloat() * radius
                )
                drawCircle(
                    color = if (index % 2 == 0) accent.copy(alpha = .80f) else Color.White.copy(alpha = .52f),
                    radius = min * if (index % 3 == 0) .014f else .009f,
                    center = dot
                )
            }

            if (!lowPower) {
                repeat(4) { index ->
                    val angle = -phaseRad * .72 + index * (Math.PI / 2.0)
                    val inner = min * .25f
                    val outer = min * .38f
                    drawLine(
                        color = accent.copy(alpha = .24f),
                        start = Offset(center.x + cos(angle).toFloat() * inner, center.y + sin(angle).toFloat() * inner),
                        end = Offset(center.x + cos(angle).toFloat() * outer, center.y + sin(angle).toFloat() * outer),
                        strokeWidth = min * .005f
                    )
                }
            }
        }

        Box(Modifier.fillMaxSize().scale(.88f).border(1.dp, accent.copy(alpha = auraAlpha), CircleShape))
        if (!lowPower) {
            Box(Modifier.fillMaxSize().scale(.68f).border(1.dp, Color.White.copy(alpha = auraAlpha * .50f), CircleShape))
        }
    }
}

/**
 * Compact phone-safe status deck. It deliberately uses two rows instead of one
 * crowded rail so values remain readable on narrow devices and never overlap.
 */
@Composable
fun PremiumEmpireSignal(state: GameState) {
    val owned = state.businesses.count { it.level > 0 }
    val automated = state.hiredManagerIds.size
    val era = EmpireEras.current(state.lifetimeCash)
    val now = System.currentTimeMillis()
    val boostLeftMs = (state.boostEndsAtMillis - now).coerceAtLeast(0L)
    val boostLabel = if (boostLeftMs > 0L) {
        val minutes = ceil(boostLeftMs / 60_000.0).toInt().coerceAtLeast(1)
        "×2 ${minutes}M"
    } else "OFF"

    Surface(
        color = EmpireColors.DeepSpace.copy(alpha = .78f),
        shape = RoundedCornerShape(20.dp),
        modifier = Modifier.fillMaxWidth().border(1.dp, Color.White.copy(alpha = .05f), RoundedCornerShape(20.dp))
    ) {
        Column(Modifier.padding(7.dp), verticalArrangement = Arrangement.spacedBy(6.dp)) {
            Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                SignalChip("ERA", "${era.index + 1}/11", Modifier.weight(1f), EmpireColors.Cyan)
                SignalChip("GEMS", state.gems.toString(), Modifier.weight(1f), EmpireColors.Violet)
                SignalChip("BOOST", boostLabel, Modifier.weight(1f), if (boostLeftMs > 0L) EmpireColors.GoldBright else EmpireColors.TextSecondary)
            }
            Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                SignalChip("ASSETS", "$owned/${state.businesses.size}", Modifier.weight(1f), EmpireColors.Gold)
                SignalChip("AUTO", "$automated/${state.businesses.size}", Modifier.weight(1f), EmpireColors.Success)
            }
        }
    }
}

@Composable
private fun SignalChip(label: String, value: String, modifier: Modifier = Modifier, accent: Color = EmpireColors.TextPrimary) {
    Surface(color = EmpireColors.Surface.copy(alpha = .72f), shape = RoundedCornerShape(13.dp), modifier = modifier) {
        Column(Modifier.padding(horizontal = 5.dp, vertical = 8.dp), horizontalAlignment = Alignment.CenterHorizontally) {
            Text(label, color = EmpireColors.TextSecondary, fontSize = 7.sp, fontWeight = FontWeight.Bold, letterSpacing = .8.sp, maxLines = 1)
            Text(value, color = accent, fontSize = 12.sp, fontWeight = FontWeight.Black, maxLines = 1)
        }
    }
}
