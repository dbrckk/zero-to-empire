package com.zerotoempire.game

import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.DrawScope

/**
 * Explicit premium-art overload for start/end/width/color ordering.
 * Keeps the procedural art sources concise while delegating to Compose's canonical API.
 */
fun DrawScope.drawLine(start: Offset, end: Offset, strokeWidth: Float, color: Color) {
    drawLine(color = color, start = start, end = end, strokeWidth = strokeWidth)
}
