package com.zerotoempire.game

import android.animation.ValueAnimator
import android.content.Context
import android.os.PowerManager

/** Central policy for animation density and accessibility-aware visual load. */
object MotionQuality {
    fun animationsEnabled(context: Context): Boolean = ValueAnimator.areAnimatorsEnabled()

    fun reducedMotion(context: Context): Boolean = !animationsEnabled(context)

    fun lowPowerMode(context: Context): Boolean {
        val power = context.getSystemService(Context.POWER_SERVICE) as? PowerManager
        return power?.isPowerSaveMode == true
    }

    fun particleBudget(context: Context, requested: Int): Int = when {
        reducedMotion(context) -> 0
        lowPowerMode(context) -> (requested / 2).coerceAtLeast(1)
        else -> requested
    }

    fun animationDuration(context: Context, millis: Int): Int = when {
        reducedMotion(context) -> 1
        lowPowerMode(context) -> (millis * 1.25f).toInt()
        else -> millis
    }
}
