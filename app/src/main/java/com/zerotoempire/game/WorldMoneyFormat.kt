package com.zerotoempire.game

internal fun worldMoney(value: Double): String {
    if (!value.isFinite()) return "∞"
    val v = value.coerceAtLeast(0.0)
    return when {
        v >= 1e30 -> String.format("%.2fN", v / 1e30)
        v >= 1e27 -> String.format("%.2fO", v / 1e27)
        v >= 1e24 -> String.format("%.2fSp", v / 1e24)
        v >= 1e21 -> String.format("%.2fSx", v / 1e21)
        v >= 1e18 -> String.format("%.2fQi", v / 1e18)
        v >= 1e15 -> String.format("%.2fQa", v / 1e15)
        v >= 1e12 -> String.format("%.2fT", v / 1e12)
        v >= 1e9 -> String.format("%.2fB", v / 1e9)
        v >= 1e6 -> String.format("%.2fM", v / 1e6)
        v >= 1e3 -> String.format("%.2fK", v / 1e3)
        else -> String.format("%.0f", v)
    }
}
