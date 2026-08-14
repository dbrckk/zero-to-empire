package com.zerotoempire.game

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.material3.Text
import androidx.compose.ui.unit.sp
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun PowerCoreTrailField(modifier: Modifier = Modifier) {
    val transition = rememberInfiniteTransition(label = "coreTrails")
    val phase by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(2600, easing = LinearEasing)), label = "trailPhase")
    Canvas(modifier) {
        val c = Offset(size.width / 2f, size.height / 2f)
        val r = size.minDimension * .34f
        repeat(18) { i ->
            val p = (phase + i / 18f) % 1f
            val a = p * (Math.PI * 2.0).toFloat() + i * .31f
            val rr = r * (.55f + .45f * p)
            val pos = Offset(c.x + cos(a) * rr, c.y + sin(a) * rr)
            val alpha = (1f - p) * .8f
            drawCircle(
                color = if (i % 3 == 0) EmpireArtPalette.Cyan.copy(alpha = alpha) else EmpireArtPalette.Gold.copy(alpha = alpha),
                radius = 1.5f + (1f - p) * 4f,
                center = pos
            )
        }
        repeat(3) { ring ->
            drawCircle(
                color = EmpireArtPalette.Gold.copy(alpha = .18f - ring * .035f),
                radius = r * (.72f + ring * .18f),
                center = c,
                style = Stroke(2f + ring)
            )
        }
    }
}

@Composable
fun EraTransitionOverlay(eraIndex: Int, visible: Boolean, modifier: Modifier = Modifier) {
    AnimatedVisibility(visible = visible, enter = fadeIn(tween(180)), exit = fadeOut(tween(520)), modifier = modifier) {
        val transition = rememberInfiniteTransition(label = "eraTransition")
        val phase by transition.animateFloat(0f, 1f, infiniteRepeatable(tween(1200, easing = LinearEasing)), label = "eraPhase")
        val accent = when (eraIndex) {
            0 -> EmpireArtPalette.Gold
            1, 2 -> EmpireArtPalette.Cyan
            3 -> EmpireArtPalette.Violet
            4 -> EmpireArtPalette.Red
            5 -> EmpireArtPalette.GoldHot
            else -> EmpireArtPalette.Magenta
        }
        Box(
            Modifier.fillMaxSize().background(
                Brush.radialGradient(listOf(accent.copy(alpha = .55f), EmpireColors.Void.copy(alpha = .94f)), radius = 1400f)
            ),
            contentAlignment = Alignment.Center
        ) {
            Canvas(Modifier.fillMaxSize()) {
                val c = Offset(size.width / 2f, size.height / 2f)
                repeat(4) { i ->
                    drawCircle(accent.copy(alpha = .45f - i * .08f), size.minDimension * (.12f + phase * .55f + i * .08f), c, style = Stroke(3f + i))
                }
                repeat(36) { i ->
                    val a = i * (Math.PI * 2.0 / 36.0).toFloat()
                    val d = size.minDimension * (.12f + phase * .62f)
                    drawCircle(accent.copy(alpha = (1f - phase) * .85f), 2f + (i % 4), Offset(c.x + cos(a) * d, c.y + sin(a) * d))
                }
            }
            Text("ERA ASCENDED", color = Color.White, fontSize = 28.sp, fontWeight = FontWeight.Black)
        }
    }
}
