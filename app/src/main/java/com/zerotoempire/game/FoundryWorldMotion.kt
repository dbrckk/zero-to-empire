package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp

/**
 * One shared motion phase for lightweight authored worker traffic in the Foundry district.
 * Decorative motion stops completely when Android animations are disabled or battery saver is active.
 */
@Composable
internal fun FoundryWorkerTraffic(modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val phase = remember { Animatable(.18f) }

    LaunchedEffect(reducedMotion) {
        if (reducedMotion) {
            phase.snapTo(.32f)
        } else {
            phase.snapTo(0f)
            while (true) {
                phase.animateTo(1f, tween(durationMillis = 7200, easing = LinearEasing))
                phase.snapTo(0f)
            }
        }
    }

    BoxWithConstraints(modifier.fillMaxSize()) {
        val widthPx = constraints.maxWidth.toFloat()
        val heightPx = constraints.maxHeight.toFloat()
        val p = phase.value

        Image(
            painter = painterResource(R.drawable.zte_worker_foundry_t0_runtime),
            contentDescription = null,
            modifier = Modifier
                .size(34.dp)
                .graphicsLayer {
                    translationX = widthPx * (.19f + p * .24f)
                    translationY = heightPx * (.48f + p * .11f)
                    alpha = if (reducedMotion) .76f else .92f
                    scaleX = .92f
                    scaleY = .92f
                }
        )

        Image(
            painter = painterResource(R.drawable.zte_worker_foundry_t0_runtime),
            contentDescription = null,
            modifier = Modifier
                .size(29.dp)
                .graphicsLayer {
                    val q = (p + .52f) % 1f
                    translationX = widthPx * (.73f - q * .20f)
                    translationY = heightPx * (.57f + q * .08f)
                    alpha = if (reducedMotion) .62f else .82f
                    scaleX = -.82f
                    scaleY = .82f
                }
        )
    }
}
