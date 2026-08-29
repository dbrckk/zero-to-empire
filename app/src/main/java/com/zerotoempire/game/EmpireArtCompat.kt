package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.material3.Text
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import kotlinx.coroutines.flow.distinctUntilChanged
import kotlinx.coroutines.flow.map
import java.util.Locale
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.min
import kotlin.math.sin

private data class BusinessArtUiState(
    val level: Int,
    val quoteCount: Int,
    val quoteCost: Double,
    val affordable: Boolean
)

private fun businessArtUiState(state: GameState, id: Int, buyMode: BuyMode): BusinessArtUiState {
    val business = state.businesses.firstOrNull { it.id == id }
    val level = business?.level ?: 0
    if (business == null || buyMode == BuyMode.X1) {
        return BusinessArtUiState(level, 0, 0.0, false)
    }
    val quote = BulkPurchase.quote(business, state.cash, buyMode)
    return BusinessArtUiState(
        level = level,
        quoteCount = quote.count,
        quoteCost = quote.totalCost,
        affordable = quote.valid && quote.totalCost <= state.cash
    )
}

@Composable
fun BusinessArtIcon(id: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val vm: GameViewModel = viewModel()
    val buyMode by vm.buyMode.collectAsStateWithLifecycle()
    val context = LocalContext.current
    val reducedMotion = MotionQuality.reducedMotion(context)
    val lowPower = MotionQuality.lowPowerMode(context)

    // Cash changes several times per second. In X1 mode none of that cash data is rendered
    // inside the sprite, so emit only when this business level changes. In bulk modes the
    // quote is part of the visible icon and therefore remains live.
    val uiFlow = remember(vm, id, buyMode) {
        vm.state.map { state -> businessArtUiState(state, id, buyMode) }.distinctUntilChanged()
    }
    val initialUi = remember(vm, id, buyMode) { businessArtUiState(vm.state.value, id, buyMode) }
    val ui by uiFlow.collectAsStateWithLifecycle(initialValue = initialUi)

    val level = ui.level
    val burst = remember(id) { Animatable(0f) }
    val previousLevel = remember(id) { intArrayOf(level) }

    LaunchedEffect(level, reducedMotion, lowPower) {
        val delta = level - previousLevel[0]
        previousLevel[0] = level
        if (delta > 0 && !reducedMotion) {
            burst.snapTo(min(1f, .28f + delta / 25f))
            burst.animateTo(0f, tween(if (lowPower) 420 else 650))
        } else if (reducedMotion && burst.value != 0f) {
            burst.snapTo(0f)
        }
    }

    Column(modifier = modifier, horizontalAlignment = Alignment.CenterHorizontally) {
        Box(contentAlignment = Alignment.Center) {
            if (burst.value > 0f) {
                Canvas(Modifier.size(iconSize + 26.dp)) {
                    val center = Offset(size.width / 2f, size.height / 2f)
                    val intensity = burst.value.coerceIn(0f, 1f)
                    val travel = 1f - intensity
                    val rays = if (lowPower) 8 else 8 + (intensity * 16).toInt()
                    val radius = size.minDimension * (.32f + .18f * travel)

                    // Layer 1: a compact energy flash that anchors the purchase at the sprite.
                    drawCircle(
                        color = EmpireColors.GoldBright,
                        radius = size.minDimension * (.16f + .06f * intensity),
                        center = center,
                        alpha = .10f * intensity
                    )
                    drawCircle(
                        color = EmpireColors.Cyan,
                        radius = size.minDimension * (.21f + .25f * travel),
                        center = center,
                        alpha = .32f * intensity,
                        style = Stroke(width = 1.4f + 2.2f * intensity)
                    )
                    drawCircle(
                        color = EmpireColors.GoldBright,
                        radius = size.minDimension * (.27f + .24f * travel),
                        center = center,
                        alpha = .20f * intensity,
                        style = Stroke(width = .9f + 1.5f * intensity)
                    )

                    // Layer 2: sharp radial energy rays, preserving the original purchase punch.
                    repeat(rays) { i ->
                        val a = 2.0 * PI * i / rays + id * .17
                        val start = Offset(center.x + cos(a).toFloat() * radius * .48f, center.y + sin(a).toFloat() * radius * .48f)
                        val end = Offset(center.x + cos(a).toFloat() * radius, center.y + sin(a).toFloat() * radius)
                        drawLine(
                            color = if (i % 2 == 0) EmpireColors.GoldBright else EmpireColors.Cyan,
                            start = start,
                            end = end,
                            strokeWidth = 1.5f + intensity * 3f,
                            alpha = intensity
                        )
                    }

                    // Layer 3: small debris sparks with staggered travel for a more physical hit.
                    val sparkCount = if (lowPower) 6 else 12
                    repeat(sparkCount) { i ->
                        val a = 2.0 * PI * i / sparkCount + id * .31
                        val stagger = .72f + (i % 4) * .08f
                        val sparkRadius = size.minDimension * (.20f + .34f * travel * stagger)
                        val p = Offset(
                            center.x + cos(a).toFloat() * sparkRadius,
                            center.y + sin(a).toFloat() * sparkRadius
                        )
                        drawCircle(
                            color = if (i % 3 == 0) EmpireColors.GoldBright else EmpireColors.Cyan,
                            radius = 1.2f + intensity * if (i % 3 == 0) 2.2f else 1.5f,
                            center = p,
                            alpha = (.35f + .65f * intensity).coerceAtMost(1f)
                        )
                    }
                }
            }

            when {
                id in 0..3 -> {
                    BusinessGroup01Sprite(id, level, iconSize)
                    BusinessGroup01Evolution(id, level, iconSize)
                }
                id in 4..7 -> {
                    BusinessGroup02Sprite(id, level, iconSize)
                    BusinessGroup02Evolution(id, level, iconSize)
                }
                id in 8..11 -> {
                    BusinessGroup03Sprite(id, level, iconSize)
                    BusinessGroup03Evolution(id, level, iconSize)
                }
                id in 12..13 -> {
                    BusinessGroup04Sprite(id, level, iconSize)
                    BusinessGroup04Evolution(id, level, iconSize)
                }
                else -> PremiumBusinessSprite(id, level, iconSize)
            }

            if (buyMode != BuyMode.X1) {
                Text(
                    text = if (ui.quoteCount > 0) "×${ui.quoteCount}" else "—",
                    color = if (ui.affordable) EmpireColors.GoldBright else EmpireColors.TextSecondary,
                    fontSize = 8.sp,
                    fontWeight = FontWeight.Black,
                    modifier = Modifier.align(Alignment.TopEnd).offset(x = 8.dp, y = (-4).dp)
                )
            }
        }

        if (buyMode != BuyMode.X1) {
            Text(
                text = if (ui.quoteCount > 0) compactMoney(ui.quoteCost) else "LOCKED",
                color = if (ui.affordable) EmpireColors.Success else EmpireColors.TextSecondary,
                fontSize = 7.sp,
                fontWeight = FontWeight.Bold,
                maxLines = 1
            )
        }
    }
}

private fun compactMoney(value: Double): String {
    if (!value.isFinite()) return "∞"
    val units = listOf(1e30 to "No", 1e27 to "Oc", 1e24 to "Sp", 1e21 to "Sx", 1e18 to "Qi", 1e15 to "Q", 1e12 to "T", 1e9 to "B", 1e6 to "M", 1e3 to "K")
    val unit = units.firstOrNull { value >= it.first }
    return if (unit == null) "$${String.format(Locale.US, "%.0f", value)}"
    else "$${String.format(Locale.US, "%.1f", value / unit.first)}${unit.second}"
}