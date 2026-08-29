package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.Dp
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin

@Composable
fun BusinessGroup04Evolution(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val stage = when {
        level >= 1000 -> 7
        level >= 500 -> 6
        level >= 250 -> 5
        level >= 100 -> 4
        level >= 50 -> 3
        level >= 25 -> 2
        level >= 10 -> 1
        else -> 0
    }
    if (stage == 0) return

    val accent = if (id == 12) Color(0xFFFF68D8) else Color(0xFFFFE36E)
    val secondary = if (id == 12) Color(0xFF6EEBFF) else Color(0xFFC68BFF)

    Canvas(modifier.size(iconSize).fillMaxSize()) {
        val s = size.minDimension
        val c = Offset(s * .5f, s * .51f)

        if (stage >= 1) {
            drawCircle(accent.copy(alpha = .30f), s * .35f, c, style = Stroke(s * .008f))
            drawCircle(secondary.copy(alpha = .68f), s * .008f, Offset(s * .23f, s * .71f))
            drawCircle(secondary.copy(alpha = .68f), s * .008f, Offset(s * .77f, s * .71f))
        }
        if (stage >= 2) {
            drawArc(
                secondary.copy(alpha = .50f),
                205f,
                130f,
                false,
                Offset(s * .15f, s * .14f),
                Size(s * .70f, s * .72f),
                style = Stroke(s * .009f)
            )
        }
        if (stage >= 3) {
            repeat(4) { i ->
                val x = s * (.30f + i * .13f)
                drawLine(accent.copy(alpha = .48f), Offset(x, s * .69f), Offset(x, s * .31f), s * .005f)
            }
        }
        if (stage >= 4) {
            drawCircle(
                brush = Brush.radialGradient(
                    colors = listOf(
                        Color.White.copy(alpha = .05f),
                        accent.copy(alpha = .10f),
                        secondary.copy(alpha = .04f),
                        Color.Transparent
                    ),
                    center = c,
                    radius = s * .47f
                ),
                radius = s * .47f,
                center = c
            )
            drawCircle(secondary.copy(alpha = .40f), s * .43f, c, style = Stroke(s * .008f))
            drawCircle(accent.copy(alpha = .18f), s * .395f, c, style = Stroke(s * .005f))
        }
        if (stage >= 5) {
            repeat(6) { i ->
                val a = -PI.toFloat() * .82f + i * PI.toFloat() * .164f
                val radius = s * .405f
                val p = Offset(c.x + cos(a) * radius, c.y + sin(a) * radius)
                drawCircle(Color.White.copy(alpha = .82f), s * .007f, p)
                drawCircle(secondary.copy(alpha = .32f), s * .014f, p, style = Stroke(s * .004f))
            }
        }
        if (stage >= 6) {
            drawArc(
                accent.copy(alpha = .72f),
                -30f,
                255f,
                false,
                Offset(s * .065f, s * .065f),
                Size(s * .87f, s * .87f),
                style = Stroke(s * .012f)
            )
            drawArc(
                secondary.copy(alpha = .48f),
                160f,
                175f,
                false,
                Offset(s * .105f, s * .105f),
                Size(s * .79f, s * .79f),
                style = Stroke(s * .007f)
            )
            repeat(8) { i ->
                val a = i * 2f * PI.toFloat() / 8f + .18f
                val r = if (i % 2 == 0) s * .445f else s * .418f
                val p = Offset(c.x + cos(a) * r, c.y + sin(a) * r)
                drawCircle(
                    color = if (i % 2 == 0) accent else secondary,
                    radius = if (i % 2 == 0) s * .008f else s * .006f,
                    center = p,
                    alpha = .86f
                )
            }
        }
        if (stage >= 7) {
            drawCircle(Color.White.copy(alpha = .08f), s * .49f, c)
            drawCircle(Color.White.copy(alpha = .86f), s * .475f, c, style = Stroke(s * .010f))
            drawCircle(accent.copy(alpha = .34f), s * .458f, c, style = Stroke(s * .0045f))

            repeat(12) { i ->
                val a = -PI.toFloat() / 2f + i * 2f * PI.toFloat() / 12f
                val inner = s * .462f
                val outer = s * if (i % 3 == 0) .515f else .495f
                val start = Offset(c.x + cos(a) * inner, c.y + sin(a) * inner)
                val end = Offset(c.x + cos(a) * outer, c.y + sin(a) * outer)
                drawLine(
                    color = if (i % 2 == 0) accent else secondary,
                    start = start,
                    end = end,
                    strokeWidth = if (i % 3 == 0) s * .009f else s * .005f,
                    alpha = if (i % 3 == 0) .88f else .62f
                )
                drawCircle(
                    color = if (i % 2 == 0) Color.White else secondary,
                    radius = if (i % 3 == 0) s * .007f else s * .005f,
                    center = end,
                    alpha = .90f
                )
            }
        }
    }
}
