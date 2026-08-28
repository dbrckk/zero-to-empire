package com.zerotoempire.game

import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
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
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlin.math.ceil

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

@Composable
fun PremiumCoreAura(eraIndex: Int, modifier: Modifier = Modifier) {
    val transition = rememberInfiniteTransition(label = "coreAura")
    val pulse by transition.animateFloat(
        initialValue = .82f,
        targetValue = 1.08f,
        animationSpec = infiniteRepeatable(tween(1450, easing = FastOutSlowInEasing), RepeatMode.Reverse),
        label = "coreAuraPulse"
    )
    val alpha by transition.animateFloat(
        initialValue = .18f,
        targetValue = .42f,
        animationSpec = infiniteRepeatable(tween(1450, easing = FastOutSlowInEasing), RepeatMode.Reverse),
        label = "coreAuraAlpha"
    )
    val accent = when (eraIndex) {
        in 0..2 -> EmpireColors.Gold
        in 3..5 -> EmpireColors.Cyan
        in 6..8 -> EmpireColors.Violet
        else -> EmpireColors.GoldBright
    }
    Box(modifier, contentAlignment = Alignment.Center) {
        Box(Modifier.fillMaxSize().scale(pulse).alpha(alpha).background(Brush.radialGradient(listOf(accent.copy(alpha = .75f), accent.copy(alpha = .12f), Color.Transparent)), CircleShape))
        Box(Modifier.fillMaxSize().scale(.88f).border(1.dp, accent.copy(alpha = alpha), CircleShape))
        Box(Modifier.fillMaxSize().scale(.68f).border(1.dp, Color.White.copy(alpha = alpha * .45f), CircleShape))
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
