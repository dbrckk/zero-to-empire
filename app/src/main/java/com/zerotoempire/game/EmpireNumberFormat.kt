package com.zerotoempire.game

import java.util.Locale
import kotlin.math.abs

object EmpireNumberFormat {
    private data class UnitDef(val value: Double, val suffix: String)

    private val units = listOf(
        UnitDef(1e33, "Dc"),
        UnitDef(1e30, "No"),
        UnitDef(1e27, "Oc"),
        UnitDef(1e24, "Sp"),
        UnitDef(1e21, "Sx"),
        UnitDef(1e18, "Qi"),
        UnitDef(1e15, "Qa"),
        UnitDef(1e12, "T"),
        UnitDef(1e9, "B"),
        UnitDef(1e6, "M"),
        UnitDef(1e3, "K")
    )

    fun compact(value: Double, currency: Boolean = false): String {
        if (value.isNaN()) return if (currency) "$0" else "0"
        if (value == Double.POSITIVE_INFINITY) return if (currency) "$∞" else "∞"
        if (value == Double.NEGATIVE_INFINITY) return if (currency) "-$∞" else "-∞"

        val magnitude = abs(value)
        val unit = units.firstOrNull { magnitude >= it.value }
        val body = if (unit == null) {
            when {
                magnitude >= 100.0 -> String.format(Locale.US, "%.0f", value)
                magnitude >= 10.0 -> String.format(Locale.US, "%.1f", value)
                else -> String.format(Locale.US, "%.2f", value)
            }
        } else {
            val scaled = value / unit.value
            val decimals = when {
                abs(scaled) >= 100 -> 0
                abs(scaled) >= 10 -> 1
                else -> 2
            }
            String.format(Locale.US, "%.${decimals}f%s", scaled, unit.suffix)
        }
        return if (currency) "$${body}" else body
    }

    fun money(value: Double): String = compact(value, currency = true)
}
