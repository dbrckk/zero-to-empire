package com.zerotoempire.game

import android.animation.ValueAnimator
import android.content.Context
import android.os.PowerManager
import androidx.compose.runtime.mutableStateOf

/** Central policy for animation density and accessibility-aware visual load. */
object MotionQuality {
    /*
     * Snapshot-backed system state lets existing composables that call this policy recompose when
     * Android's power/animation settings change, without threading a new flag through the UI tree.
     */
    private val animationsEnabledState = mutableStateOf<Boolean?>(null)
    private val lowPowerModeState = mutableStateOf<Boolean?>(null)

    fun refresh(context: Context) {
        animationsEnabledState.value = ValueAnimator.areAnimatorsEnabled()
        lowPowerModeState.value = queryLowPowerMode(context)
    }

    fun animationsEnabled(context: Context): Boolean =
        animationsEnabledState.value ?: ValueAnimator.areAnimatorsEnabled()

    fun lowPowerMode(context: Context): Boolean =
        lowPowerModeState.value ?: queryLowPowerMode(context)

    private fun queryLowPowerMode(context: Context): Boolean {
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
