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
            drawArc(secondary.copy(alpha = .50f), 205f, 130f, false, Offset(s * .15f, s * .14f), Size(s * .70f, s * .72f), style = Stroke(s * .009f))
        }
        if (stage >= 3) {
            repeat(4) { i ->
                val x = s * (.30f + i * .13f)
                drawLine(accent.copy(alpha = .48f), Offset(x, s * .69f), Offset(x, s * .31f), s * .005f)
            }
        }
        if (stage >= 4) {
            drawCircle(accent.copy(alpha = .12f), s * .42f, c)
            drawCircle(secondary.copy(alpha = .40f), s * .43f, c, style = Stroke(s * .008f))
        }
        if (stage >= 5) {
            repeat(6) { i ->
                drawCircle(Color.White.copy(alpha = .80f), s * .007f, Offset(s * (.25f + i * .10f), s * .17f))
            }
        }
        if (stage >= 6) {
            drawArc(accent.copy(alpha = .70f), -30f, 255f, false, Offset(s * .065f, s * .065f), Size(s * .87f, s * .87f), style = Stroke(s * .012f))
            drawArc(secondary.copy(alpha = .45f), 160f, 175f, false, Offset(s * .105f, s * .105f), Size(s * .79f, s * .79f), style = Stroke(s * .007f))
        }
        if (stage >= 7) {
            drawCircle(Color.White.copy(alpha = .13f), s * .49f, c)
            drawCircle(Color.White.copy(alpha = .82f), s * .475f, c, style = Stroke(s * .010f))
            repeat(10) { i ->
                val x = s * (.19f + i * .068f)
                drawCircle(if (i % 2 == 0) accent else secondary, s * .006f, Offset(x, s * .115f + (i % 3) * s * .024f))
            }
        }
    }
}
