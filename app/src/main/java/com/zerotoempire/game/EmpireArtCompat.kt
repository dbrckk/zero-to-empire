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
import androidx.compose.ui.graphics.Color
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
                    val group = when (id) {
                        in 0..3 -> 0
                        in 4..7 -> 1
                        in 8..11 -> 2
                        else -> 3
                    }
                    val primary = when (group) {
                        0 -> EmpireColors.GoldBright
                        1 -> EmpireColors.Cyan
                        2 -> Color(0xFFB48CFF)
                        else -> Color.White
                    }
                    val secondary = when (group) {
                        0 -> EmpireColors.Cyan
                        1 -> Color(0xFF9A7CFF)
                        2 -> Color(0xFFFFD86A)
                        else -> Color(0xFFFF68D8)
                    }
                    val baseRays = when (group) {
                        0 -> 8
                        1 -> 10
                        2 -> 6
                        else -> 12
                    }
                    val extraRays = if (lowPower) 0 else (intensity * when (group) {
                        0 -> 16
                        1 -> 10
                        2 -> 6
                        else -> 8
                    }).toInt()
                    val rays = baseRays + extraRays
                    val radius = size.minDimension * (.32f + .18f * travel)

                    // The same purchase event now speaks the visual language of each era:
                    // energetic early-game sparks, engineered expansion locks, heavy
                    // megastructure pressure spokes, then a cleaner endgame singularity flash.
                    drawCircle(
                        color = primary,
                        radius = size.minDimension * (.16f + .06f * intensity),
                        center = center,
                        alpha = .10f * intensity
                    )
                    drawCircle(
                        color = secondary,
                        radius = size.minDimension * (.21f + .25f * travel),
                        center = center,
                        alpha = .32f * intensity,
                        style = Stroke(width = 1.4f + 2.2f * intensity)
                    )
                    drawCircle(
                        color = primary,
                        radius = size.minDimension * (.27f + .24f * travel),
                        center = center,
                        alpha = .20f * intensity,
                        style = Stroke(width = .9f + 1.5f * intensity)
                    )

                    if (group == 1) {
                        repeat(4) { i ->
                            val a = i * PI.toFloat() / 2f
                            val inner = size.minDimension * (.22f + .08f * travel)
                            val outer = size.minDimension * (.34f + .11f * travel)
                            val side = size.minDimension * .045f
                            val joint = Offset(
                                center.x + cos(a).toFloat() * outer,
                                center.y + sin(a).toFloat() * outer
                            )
                            drawLine(
                                color = primary,
                                start = Offset(center.x + cos(a).toFloat() * inner, center.y + sin(a).toFloat() * inner),
                                end = joint,
                                strokeWidth = 1.4f + intensity * 2.4f,
                                alpha = .72f * intensity
                            )
                            drawLine(
                                color = secondary,
                                start = Offset(joint.x + cos(a + PI.toFloat() / 2f) * side, joint.y + sin(a + PI.toFloat() / 2f) * side),
                                end = Offset(joint.x - cos(a + PI.toFloat() / 2f) * side, joint.y - sin(a + PI.toFloat() / 2f) * side),
                                strokeWidth = 1.1f + intensity * 1.7f,
                                alpha = .60f * intensity
                            )
                        }
                    }

                    repeat(rays) { i ->
                        val a = 2.0 * PI * i / rays + id * .17
                        val startScale = when (group) {
                            2 -> .40f
                            3 -> .58f
                            else -> .48f
                        }
                        val start = Offset(center.x + cos(a).toFloat() * radius * startScale, center.y + sin(a).toFloat() * radius * startScale)
                        val end = Offset(center.x + cos(a).toFloat() * radius, center.y + sin(a).toFloat() * radius)
                        drawLine(
                            color = when {
                                group == 3 && i % 3 == 0 -> Color.White
                                i % 2 == 0 -> primary
                                else -> secondary
                            },
                            start = start,
                            end = end,
                            strokeWidth = when (group) {
                                2 -> 2.2f + intensity * if (i % 2 == 0) 4.0f else 2.0f
                                3 -> 1.1f + intensity * 2.0f
                                else -> 1.5f + intensity * 3f
                            },
                            alpha = intensity
                        )
                    }

                    val sparkCount = if (lowPower) {
                        when (group) {
                            2, 3 -> 4
                            else -> 6
                        }
                    } else {
                        when (group) {
                            0 -> 12
                            1 -> 10
                            2 -> 6
                            else -> 8
                        }
                    }
                    repeat(sparkCount) { i ->
                        val a = 2.0 * PI * i / sparkCount + id * .31
                        val stagger = .72f + (i % 4) * .08f
                        val sparkRadius = size.minDimension * (.20f + .34f * travel * stagger)
                        val p = Offset(
                            center.x + cos(a).toFloat() * sparkRadius,
                            center.y + sin(a).toFloat() * sparkRadius
                        )
                        drawCircle(
                            color = when {
                                group == 3 && i % 3 == 0 -> Color.White
                                i % 3 == 0 -> primary
                                else -> secondary
                            },
                            radius = when (group) {
                                2 -> 1.4f + intensity * if (i % 2 == 0) 2.5f else 1.3f
                                3 -> 1.0f + intensity * 1.4f
                                else -> 1.2f + intensity * if (i % 3 == 0) 2.2f else 1.5f
                            },
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

            // Early and mid-game assets now receive the same material finish as late-game
            // machinery without adding another animation clock. These marks are deliberately
            // sparse and level-gated so the base silhouettes remain readable at phone size.
            if (id in 0..7 && level >= 25) {
                Canvas(Modifier.size(iconSize)) {
                    val s = size.minDimension
                    val center = Offset(size.width / 2f, size.height / 2f)
                    val tier = when {
                        level >= 1000 -> 5
                        level >= 500 -> 4
                        level >= 250 -> 3
                        level >= 100 -> 2
                        else -> 1
                    }
                    val accent = when (id) {
                        0 -> Color(0xFF78F56A)
                        1 -> Color(0xFF58BFFF)
                        2 -> Color(0xFFFF9A43)
                        3 -> Color(0xFFB76CFF)
                        4 -> Color(0xFF67E8FF)
                        5 -> Color(0xFFFFD166)
                        6 -> Color(0xFFFF776D)
                        else -> Color(0xFFA98BFF)
                    }

                    drawCircle(
                        color = accent.copy(alpha = .20f + tier * .025f),
                        radius = s * .455f,
                        center = center,
                        style = Stroke(width = s * .0065f)
                    )
                    drawLine(
                        color = Color.White.copy(alpha = .18f + tier * .025f),
                        start = Offset(s * .25f, s * .20f),
                        end = Offset(s * .46f, s * .11f),
                        strokeWidth = s * .008f
                    )
                    drawLine(
                        color = accent.copy(alpha = .24f),
                        start = Offset(s * .54f, s * .89f),
                        end = Offset(s * .75f, s * .80f),
                        strokeWidth = s * .006f
                    )

                    if (tier >= 2) {
                        val nodeCount = if (lowPower) 2 else 4
                        repeat(nodeCount) { i ->
                            val a = (2.0 * PI * i / nodeCount) + id * .23
                            drawCircle(
                                color = if (i % 2 == 0) accent else Color.White,
                                radius = s * .009f,
                                center = Offset(
                                    center.x + cos(a).toFloat() * s * .445f,
                                    center.y + sin(a).toFloat() * s * .445f
                                ),
                                alpha = .58f
                            )
                        }
                    }
                    if (tier >= 4 && !lowPower) {
                        repeat(3) { i ->
                            drawCircle(
                                color = Color.White,
                                radius = s * .0055f,
                                center = Offset(s * (.39f + i * .11f), s * .105f),
                                alpha = .72f
                            )
                        }
                    }
                }
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
