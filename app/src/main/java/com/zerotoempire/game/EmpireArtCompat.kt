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
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.material3.Text
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import java.util.Locale
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.min
import kotlin.math.sin

/**
 * Stateless business artwork. Game state is collected once by the parent screen and
 * only the values needed for rendering are passed here. This avoids one ViewModel
 * subscription pair per visible business card.
 */
@Composable
fun BusinessArtIcon(
    id: Int,
    level: Int,
    iconSize: Dp,
    modifier: Modifier = Modifier,
    buyMode: BuyMode = BuyMode.X1,
    quote: BulkQuote? = null,
    cash: Double = 0.0
) {
    val affordable = quote?.let { it.valid && it.totalCost <= cash } ?: false
    val burst = remember(id) { Animatable(0f) }
    val previousLevel = remember(id) { intArrayOf(level) }

    LaunchedEffect(level) {
        val delta = level - previousLevel[0]
        previousLevel[0] = level
        if (delta > 0) {
            burst.snapTo(min(1f, .28f + delta / 25f))
            burst.animateTo(0f, tween(650))
        }
    }

    Column(modifier = modifier, horizontalAlignment = Alignment.CenterHorizontally) {
        Box(contentAlignment = Alignment.Center) {
            if (burst.value > 0f) {
                Canvas(Modifier.size(iconSize + 26.dp)) {
                    val center = Offset(size.width / 2f, size.height / 2f)
                    val rays = 8 + (burst.value * 16).toInt()
                    val radius = size.minDimension * (.32f + .18f * (1f - burst.value))
                    repeat(rays) { i ->
                        val a = 2.0 * PI * i / rays
                        val start = Offset(center.x + cos(a).toFloat() * radius * .48f, center.y + sin(a).toFloat() * radius * .48f)
                        val end = Offset(center.x + cos(a).toFloat() * radius, center.y + sin(a).toFloat() * radius)
                        drawLine(
                            color = if (i % 2 == 0) EmpireColors.GoldBright else EmpireColors.Cyan,
                            start = start,
                            end = end,
                            strokeWidth = 1.5f + burst.value * 3f,
                            alpha = burst.value
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
                id in 8..11 -> BusinessGroup03Sprite(id, level, iconSize)
                id in 12..13 -> BusinessGroup04Sprite(id, level, iconSize)
                else -> PremiumBusinessSprite(id, level, iconSize)
            }

            if (buyMode != BuyMode.X1 && quote != null) {
                Text(
                    text = if (quote.count > 0) "×${quote.count}" else "—",
                    color = if (affordable) EmpireColors.GoldBright else EmpireColors.TextSecondary,
                    fontSize = 8.sp,
                    fontWeight = FontWeight.Black,
                    modifier = Modifier.align(Alignment.TopEnd).offset(x = 8.dp, y = (-4).dp)
                )
            }
        }

        if (buyMode != BuyMode.X1 && quote != null) {
            Text(
                text = if (quote.count > 0) compactMoney(quote.totalCost) else "LOCKED",
                color = if (affordable) EmpireColors.Success else EmpireColors.TextSecondary,
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
