package com.zerotoempire.game

import android.animation.ValueAnimator
import android.content.Context
import android.os.PowerManager

/** Central policy for animation density and accessibility-aware visual load. */
object MotionQuality {
    fun animationsEnabled(context: Context): Boolean = ValueAnimator.areAnimatorsEnabled()

    fun lowPowerMode(context: Context): Boolean {
        val power = context.getSystemService(Context.POWER_SERVICE) as? PowerManager
        return power?.isPowerSaveMode == true
    }

    /**
     * Decorative motion is disabled when Android animations are disabled or Battery Saver is active.
     * This keeps low-power mode genuinely static instead of running the same infinite transitions slower.
     */
    fun reducedMotion(context: Context): Boolean = !animationsEnabled(context) || lowPowerMode(context)

    fun particleBudget(context: Context, requested: Int): Int = when {
        reducedMotion(context) -> 0
        else -> requested
    }

    fun animationDuration(context: Context, millis: Int): Int = when {
        reducedMotion(context) -> 1
        else -> millis
    }
}
