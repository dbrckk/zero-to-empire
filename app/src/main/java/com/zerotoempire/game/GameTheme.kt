package com.zerotoempire.game

import androidx.compose.material3.darkColorScheme
import androidx.compose.ui.graphics.Color

object EmpireColors {
    val Void = Color(0xFF050914)
    val DeepSpace = Color(0xFF09152A)
    val Surface = Color(0xFF101D33)
    val SurfaceHigh = Color(0xFF172943)
    val Gold = Color(0xFFFFC857)
    val GoldBright = Color(0xFFFFE08A)
    val Cyan = Color(0xFF48E5E9)
    val Violet = Color(0xFF9B7BFF)
    val Success = Color(0xFF69E7A5)
    val TextPrimary = Color(0xFFF7FAFF)
    val TextSecondary = Color(0xFF9EB0C9)
}

val EmpireColorScheme = darkColorScheme(
    primary = EmpireColors.Gold,
    secondary = EmpireColors.Cyan,
    tertiary = EmpireColors.Violet,
    background = EmpireColors.Void,
    surface = EmpireColors.Surface,
    onPrimary = EmpireColors.Void,
    onBackground = EmpireColors.TextPrimary,
    onSurface = EmpireColors.TextPrimary
)
