package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.Dp

@Composable
fun BusinessGroup03Evolution(id: Int, level: Int, iconSize: Dp, modifier: Modifier = Modifier) {
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

    val accent = when (id) {
        8 -> Color(0xFFFFD45A)
        9 -> Color(0xFF5BE6FF)
        10 -> Color(0xFF9F7CFF)
        else -> Color(0xFFFF65D7)
    }
    val secondary = when (id) {
        8 -> Color(0xFFFFF2B0)
        9 -> Color(0xFF8C88FF)
        10 -> Color(0xFF6EEBFF)
        else -> Color(0xFFFFC85A)
    }

    Canvas(modifier.size(iconSize).fillMaxSize()) {
        val s = size.minDimension
        val c = Offset(s * .5f, s * .52f)

        if (stage >= 1) {
            drawCircle(accent.copy(alpha = .32f), s * .36f, c, style = Stroke(s * .008f))
            drawCircle(secondary.copy(alpha = .58f), s * .010f, Offset(s * .22f, s * .72f))
            drawCircle(secondary.copy(alpha = .58f), s * .010f, Offset(s * .78f, s * .72f))
        }
        if (stage >= 2) {
            drawArc(secondary.copy(alpha = .48f), 195f, 150f, false, Offset(s * .13f, s * .15f), Size(s * .74f, s * .70f), style = Stroke(s * .009f))
        }
        if (stage >= 3) {
            repeat(4) { i ->
                val x = s * (.29f + i * .14f)
                drawLine(accent.copy(alpha = .45f), Offset(x, s * .68f), Offset(x, s * .34f), s * .005f)
            }
        }
        if (stage >= 4) {
            drawCircle(accent.copy(alpha = .12f), s * .42f, c)
            drawCircle(secondary.copy(alpha = .36f), s * .43f, c, style = Stroke(s * .008f))
        }
        if (stage >= 5) {
            repeat(6) { i ->
                drawCircle(secondary.copy(alpha = .72f), s * .007f, Offset(s * (.25f + i * .10f), s * .18f))
            }
        }
        if (stage >= 6) {
            drawArc(accent.copy(alpha = .68f), -35f, 250f, false, Offset(s * .07f, s * .07f), Size(s * .86f, s * .86f), style = Stroke(s * .012f))
            drawArc(secondary.copy(alpha = .42f), 165f, 170f, false, Offset(s * .11f, s * .11f), Size(s * .78f, s * .78f), style = Stroke(s * .007f))
        }
        if (stage >= 7) {
            drawCircle(Color.White.copy(alpha = .12f), s * .48f, c)
            drawCircle(Color(0xFFFFE79B).copy(alpha = .76f), s * .47f, c, style = Stroke(s * .010f))
            repeat(8) { i ->
                val x = s * (.22f + i * .08f)
                drawCircle(Color.White.copy(alpha = .88f), s * .006f, Offset(x, s * .12f + (i % 2) * s * .035f))
            }
        }
    }
}
