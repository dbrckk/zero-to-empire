package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

@Composable
fun ManagerPortrait(businessId: Int, size: Dp = 58.dp) {
    val accent = when (businessId.coerceAtLeast(0)) {
        0 -> Color(0xFF69E08A)
        1 -> Color(0xFF56BFFF)
        2 -> Color(0xFFFFA54D)
        3 -> Color(0xFFC28BFF)
        4 -> Color(0xFF43E6FF)
        5 -> Color(0xFF4FA8FF)
        6 -> Color(0xFFEAF6FF)
        7 -> Color(0xFFFF654F)
        8 -> Color(0xFFFFD45A)
        9 -> Color(0xFF5BE6FF)
        10 -> Color(0xFF9F7CFF)
        11 -> Color(0xFFFF65D7)
        12 -> Color(0xFFFF68D8)
        else -> Color(0xFFFFE36E)
    }
    val tier = when {
        businessId >= 12 -> 4
        businessId >= 8 -> 3
        businessId >= 4 -> 2
        else -> 1
    }

    Box(modifier = Modifier.size(size), contentAlignment = Alignment.Center) {
        when {
            businessId in 0..3 -> ManagerGroup01Portrait(businessId = businessId, portraitSize = size)
            businessId in 4..7 -> ManagerGroup02Portrait(businessId = businessId, portraitSize = size)
            businessId in 8..9 -> ManagerGroup03Portrait(businessId = businessId, portraitSize = size)
            else -> EndgameManagerPortrait(businessId = businessId, portraitSize = size)
        }

        Canvas(Modifier.size(size)) {
            val s = this.size.minDimension
            val c = Offset(this.size.width * .5f, this.size.height * .5f)

            // Shared premium glass/frame treatment. Kept static so manager lists remain cheap.
            drawCircle(
                color = Color.Black.copy(alpha = .24f),
                radius = s * .486f,
                center = c,
                style = Stroke(width = s * .024f)
            )
            drawCircle(
                color = accent.copy(alpha = .72f),
                radius = s * .472f,
                center = c,
                style = Stroke(width = s * .010f)
            )
            drawArc(
                color = Color.White.copy(alpha = .42f),
                startAngle = 208f,
                sweepAngle = 76f,
                useCenter = false,
                topLeft = Offset(s * .052f, s * .052f),
                size = Size(s * .896f, s * .896f),
                style = Stroke(width = s * .009f)
            )
            drawArc(
                color = accent.copy(alpha = .36f),
                startAngle = 18f,
                sweepAngle = 112f,
                useCenter = false,
                topLeft = Offset(s * .074f, s * .074f),
                size = Size(s * .852f, s * .852f),
                style = Stroke(width = s * .006f)
            )

            val markerCount = tier + 1
            repeat(markerCount) { index ->
                val x = s * (.38f + index * .06f)
                drawCircle(
                    color = if (index == markerCount - 1) Color.White.copy(alpha = .92f) else accent.copy(alpha = .78f),
                    radius = s * .010f,
                    center = Offset(x, s * .925f)
                )
            }
        }
    }
}

@Composable
fun EraVista(eraIndex: Int, modifier: Modifier = Modifier) {
    Box(modifier = modifier) {
        EraVistaAAA(eraIndex = eraIndex, modifier = Modifier.fillMaxSize())
        EraVistaCinematicOverlay(eraIndex = eraIndex, modifier = Modifier.fillMaxSize())
    }
}
