package com.zerotoempire.game

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

@Composable
fun ManagerPortrait(businessId: Int, size: Dp = 58.dp) {
    when {
        businessId in 0..3 -> ManagerGroup01Portrait(businessId = businessId, portraitSize = size)
        businessId >= 10 -> EndgameManagerPortrait(businessId = businessId, portraitSize = size)
        else -> LegacyManagerPortrait(businessId = businessId, portraitSize = size)
    }
}

@Composable
private fun LegacyManagerPortrait(businessId: Int, portraitSize: Dp) {
    // Temporary compatibility path for groups 2–3 until their dedicated AAA passes land.
    ManagerGroup01Portrait(businessId = businessId.coerceIn(0,3), portraitSize = portraitSize)
}

@Composable
fun EraVista(eraIndex: Int, modifier: Modifier = Modifier) {
    val transition = rememberInfiniteTransition(label = "eraVista")
    val drift by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(20_000, easing = LinearEasing)), label = "drift")
    Canvas(modifier) {
        val w = size.width
        val h = size.height
        val accent = when (eraIndex) {
            0 -> EmpireArtPalette.Gold
            1 -> EmpireArtPalette.Cyan
            2 -> Color(0xFFFF9B55)
            3 -> EmpireArtPalette.Violet
            4 -> EmpireArtPalette.Red
            5 -> EmpireArtPalette.GoldHot
            else -> EmpireArtPalette.Magenta
        }
        drawRect(Brush.verticalGradient(listOf(EmpireColors.DeepSpace, EmpireColors.Void)))
        repeat(22) { i ->
            val x = w * (((i * 37) % 101) / 100f)
            val y = h * (((i * 61) % 83) / 100f) * .65f
            drawCircle(EmpireArtPalette.White.copy(alpha = .25f + (i % 4) * .12f), if (i % 6 == 0) 2f else 1f, Offset(x, y))
        }
        drawCircle(
            Brush.radialGradient(listOf(accent.copy(alpha = .22f), Color.Transparent), center = Offset(w * (.25f + .5f * drift), h * .4f), radius = w * .45f),
            radius = w * .45f,
            center = Offset(w * (.25f + .5f * drift), h * .4f)
        )
        val base = h * .78f
        when {
            eraIndex <= 1 -> repeat(8) { i ->
                val bw = w * .09f
                val bh = h * (.18f + ((i * 7) % 5) * .055f)
                drawRect(EmpireArtPalette.Steel.copy(alpha = .9f), Offset(w * (.05f + i * .12f), base - bh), androidx.compose.ui.geometry.Size(bw, bh))
                drawCircle(accent, 2.2f, Offset(w * (.09f + i * .12f), base - bh * .55f))
            }
            eraIndex <= 3 -> {
                drawCircle(accent.copy(alpha = .7f), h * .22f, Offset(w * .72f, h * .43f))
                drawCircle(EmpireColors.Void.copy(alpha = .32f), h * .05f, Offset(w * .66f, h * .38f))
                drawLine(accent.copy(alpha = .55f), Offset(0f, base), Offset(w, base), 3f)
            }
            else -> {
                drawCircle(accent.copy(alpha = .2f), h * .25f, Offset(w * .5f, h * .42f))
                drawCircle(accent, h * .17f, Offset(w * .5f, h * .42f), style = androidx.compose.ui.graphics.drawscope.Stroke(5f))
                repeat(7) { i ->
                    val a = i * 6.28318f / 7f + drift
                    drawCircle(EmpireArtPalette.White, 2.5f, Offset(w*.5f + kotlin.math.cos(a)*w*.27f, h*.42f + kotlin.math.sin(a)*h*.20f))
                }
            }
        }
    }
}
