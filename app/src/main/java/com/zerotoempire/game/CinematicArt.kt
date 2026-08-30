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
import androidx.compose.ui.graphics.Brush
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

            // Static layered lens/frame treatment: richer depth without adding animation work
            // to manager lists or changing portrait layout dimensions.
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(Color.Transparent, accent.copy(alpha = .055f), Color.Black.copy(alpha = .22f)),
                    center = c,
                    radius = s * .50f
                ),
                radius = s * .488f,
                center = c
            )
            drawCircle(
                color = Color.Black.copy(alpha = .30f),
                radius = s * .486f,
                center = c,
                style = Stroke(width = s * .026f)
            )
            drawCircle(
                color = accent.copy(alpha = .78f),
                radius = s * .470f,
                center = c,
                style = Stroke(width = s * .010f)
            )
            drawCircle(
                color = Color.White.copy(alpha = .10f),
                radius = s * .448f,
                center = c,
                style = Stroke(width = s * .004f)
            )
            drawArc(
                color = Color.White.copy(alpha = .50f),
                startAngle = 208f,
                sweepAngle = 76f,
                useCenter = false,
                topLeft = Offset(s * .052f, s * .052f),
                size = Size(s * .896f, s * .896f),
                style = Stroke(width = s * .009f)
            )
            drawArc(
                color = accent.copy(alpha = .42f),
                startAngle = 18f,
                sweepAngle = 112f,
                useCenter = false,
                topLeft = Offset(s * .074f, s * .074f),
                size = Size(s * .852f, s * .852f),
                style = Stroke(width = s * .006f)
            )
            drawArc(
                color = Color.White.copy(alpha = .16f),
                startAngle = 298f,
                sweepAngle = 34f,
                useCenter = false,
                topLeft = Offset(s * .105f, s * .105f),
                size = Size(s * .790f, s * .790f),
                style = Stroke(width = s * .004f)
            )

            // Small machined frame notches make each portrait read as an executive badge.
            val notch = s * .035f
            val inset = s * .095f
            listOf(
                Offset(inset, inset) to Offset(inset + notch, inset),
                Offset(s - inset, inset) to Offset(s - inset - notch, inset),
                Offset(inset, s - inset) to Offset(inset + notch, s - inset),
                Offset(s - inset, s - inset) to Offset(s - inset - notch, s - inset)
            ).forEach { (start, end) ->
                drawLine(accent.copy(alpha = .58f), start, end, s * .006f)
            }

            val markerCount = tier + 1
            val markerSpacing = s * .060f
            val markerStart = c.x - (markerCount - 1) * markerSpacing * .5f
            repeat(markerCount) { index ->
                val markerCenter = Offset(markerStart + index * markerSpacing, s * .925f)
                drawCircle(Color.Black.copy(alpha = .58f), s * .016f, markerCenter)
                drawCircle(
                    color = if (index == markerCount - 1) Color.White.copy(alpha = .96f) else accent.copy(alpha = .84f),
                    radius = s * .010f,
                    center = markerCenter
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
