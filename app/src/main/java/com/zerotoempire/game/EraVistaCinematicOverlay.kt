package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext

/**
 * Lightweight foreground treatment for EraVista. It deliberately owns no animation state:
 * the vista beneath it already supplies motion, while this layer adds depth and lens framing
 * without another frame clock or persistent allocation stream.
 */
@Composable
fun EraVistaCinematicOverlay(eraIndex: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val lowPower = MotionQuality.lowPowerMode(context)
    val era = eraIndex.coerceIn(0, 10)
    val accent = when (era) {
        0 -> EmpireArtPalette.Gold
        1 -> Color(0xFFFF9B55)
        2, 4 -> EmpireArtPalette.Cyan
        3 -> EmpireArtPalette.Violet
        5 -> EmpireArtPalette.Red
        6 -> EmpireArtPalette.GoldHot
        7 -> EmpireArtPalette.Violet
        8 -> EmpireArtPalette.Cyan
        9 -> Color(0xFFFF68D8)
        else -> Color(0xFFFFE36E)
    }

    Canvas(modifier.fillMaxSize()) {
        val w = size.width
        val h = size.height
        val center = Offset(w * .5f, h * .45f)

        // Optical vignette: preserves the focal center while giving the vista a camera-like frame.
        drawRect(
            brush = Brush.radialGradient(
                colors = listOf(
                    Color.Transparent,
                    Color.Transparent,
                    Color.Black.copy(alpha = if (lowPower) .24f else .32f)
                ),
                center = center,
                radius = size.maxDimension * .72f
            )
        )

        // Foreground atmospheric falloff separates UI/silhouettes from the distant scene.
        drawRect(
            brush = Brush.verticalGradient(
                colors = listOf(Color.Transparent, Color.Black.copy(alpha = if (lowPower) .12f else .20f)),
                startY = h * .54f,
                endY = h
            ),
            topLeft = Offset(0f, h * .52f),
            size = Size(w, h * .48f)
        )

        // Era-colored horizon bloom. Cheap, static, and visually binds every vista to its era palette.
        drawRect(
            brush = Brush.verticalGradient(
                colors = listOf(
                    Color.Transparent,
                    accent.copy(alpha = if (lowPower) .025f else .055f),
                    Color.Transparent
                ),
                startY = h * .64f,
                endY = h * .91f
            ),
            topLeft = Offset(0f, h * .60f),
            size = Size(w, h * .34f)
        )

        if (!lowPower) {
            // Thin anamorphic edge glints add a premium lens treatment without bloom shaders.
            drawLine(accent.copy(alpha = .15f), Offset(w * .06f, h * .09f), Offset(w * .30f, h * .09f), 1.2f)
            drawLine(accent.copy(alpha = .11f), Offset(w * .70f, h * .91f), Offset(w * .94f, h * .91f), 1.2f)
            if (era >= 6) {
                drawArc(
                    color = accent.copy(alpha = .09f),
                    startAngle = 198f,
                    sweepAngle = 144f,
                    useCenter = false,
                    topLeft = Offset(w * .08f, h * .10f),
                    size = Size(w * .84f, h * .70f),
                    style = Stroke(1.2f)
                )
            }
        }
    }
}
