package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalConfiguration
import androidx.compose.ui.platform.LocalContext
import kotlin.math.min

/**
 * Lightweight full-screen punctuation for major era changes.
 * It owns no gameplay state, consumes no input, and is completely disabled
 * when reduced-motion / battery-saver policy is active.
 */
@Composable
fun CinematicRuntimeTransitionOverlay(
    eraIndex: Int,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val configuration = LocalConfiguration.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val compactScreen = configuration.screenWidthDp < 360
    val phase = remember { Animatable(1f) }
    var previousEra by remember { mutableIntStateOf(eraIndex) }

    LaunchedEffect(eraIndex, reducedMotion, compactScreen) {
        val advanced = eraIndex > previousEra
        previousEra = eraIndex
        if (!advanced || reducedMotion) {
            phase.snapTo(1f)
            return@LaunchedEffect
        }
        phase.snapTo(0f)
        // The final 1.5% is visually negligible; ending there also removes
        // the otherwise invisible animation tail from the composition clock.
        phase.animateTo(
            .985f,
            animationSpec = tween(durationMillis = if (compactScreen) 472 else 552)
        )
    }

    if (!reducedMotion && phase.value < .985f) {
        val progress = phase.value.coerceIn(0f, 1f)
        val impact = (1f - progress).coerceIn(0f, 1f)
        val cyan = Color(0xFF63E7FF)
        val gold = Color(0xFFFFD166)

        Canvas(modifier.fillMaxSize()) {
            val shortest = min(size.width, size.height)
            val center = Offset(size.width * .5f, size.height * .46f)
            val ringRadius = shortest * (.10f + .72f * progress)
            val edgeWidth = shortest * .012f

            drawRect(Color.White.copy(alpha = .16f * impact))
            drawRect(cyan.copy(alpha = .09f * impact))

            drawCircle(
                color = gold.copy(alpha = .70f * impact),
                radius = ringRadius,
                center = center,
                style = Stroke(width = edgeWidth * (1.15f - .55f * progress))
            )
            if (!compactScreen) {
                drawCircle(
                    color = cyan.copy(alpha = .48f * impact),
                    radius = ringRadius * 1.18f,
                    center = center,
                    style = Stroke(width = edgeWidth * .48f)
                )
            }

            val sweepY = size.height * (-.08f + 1.16f * progress)
            drawLine(
                color = Color.White.copy(alpha = .28f * impact),
                start = Offset(0f, sweepY),
                end = Offset(size.width, sweepY),
                strokeWidth = edgeWidth * .65f
            )
            if (!compactScreen) {
                drawLine(
                    color = cyan.copy(alpha = .34f * impact),
                    start = Offset(0f, sweepY + edgeWidth * 1.8f),
                    end = Offset(size.width, sweepY + edgeWidth * 1.8f),
                    strokeWidth = edgeWidth * .28f
                )

                val cornerLength = shortest * (.10f + .05f * impact)
                val inset = shortest * .035f
                val cornerAlpha = .55f * impact
                drawLine(gold.copy(alpha = cornerAlpha), Offset(inset, inset), Offset(inset + cornerLength, inset), edgeWidth * .32f)
                drawLine(gold.copy(alpha = cornerAlpha), Offset(inset, inset), Offset(inset, inset + cornerLength), edgeWidth * .32f)
                drawLine(cyan.copy(alpha = cornerAlpha), Offset(size.width - inset, size.height - inset), Offset(size.width - inset - cornerLength, size.height - inset), edgeWidth * .32f)
                drawLine(cyan.copy(alpha = cornerAlpha), Offset(size.width - inset, size.height - inset), Offset(size.width - inset, size.height - inset - cornerLength), edgeWidth * .32f)
            }
        }
    }
}
