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
import kotlin.math.abs

/**
 * One shared motion phase for lightweight authored worker, vehicle and machine activity
 * in the Foundry district. Decorative motion stops completely when Android animations
 * are disabled or battery saver is active.
 */
@Composable
internal fun FoundryWorkerTraffic(
    businessId: Int,
    modifier: Modifier = Modifier
) {
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

        // Four transparent raster frames replace the earlier two-pose vector worker cycle.
        // They still use the single district clock and freeze deterministically in reduced motion.
        val workerFrames = intArrayOf(
            R.drawable.zte_foundry_worker_raster_f0,
            R.drawable.zte_foundry_worker_raster_f1,
            R.drawable.zte_foundry_worker_raster_f2,
            R.drawable.zte_foundry_worker_raster_f3
        )
        val workerFrameIndex = if (reducedMotion) 0 else ((p * 16f).toInt() and 3)
        val secondWorkerFrameIndex = if (reducedMotion) 0 else (((p + .5f) * 16f).toInt() and 3)

        Image(
            painter = painterResource(workerFrames[workerFrameIndex]),
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
            painter = painterResource(workerFrames[secondWorkerFrameIndex]),
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

        if (businessId == 1 || businessId == 3) {
            Image(
                painter = painterResource(R.drawable.zte_foundry_delivery_v1_runtime),
                contentDescription = null,
                modifier = Modifier
                    .size(46.dp)
                    .graphicsLayer {
                        val r = (p + .24f) % 1f
                        translationX = widthPx * (.08f + r * .58f)
                        translationY = heightPx * (.70f - r * .15f)
                        alpha = if (reducedMotion) .74f else .94f
                        scaleX = .78f
                        scaleY = .78f
                    }
            )
        }

        if (businessId == 2 || businessId == 3) {
            val route = if (reducedMotion) .38f else (p + .63f) % 1f
            val forkliftFrame = if (reducedMotion || route < .32f || route > .70f) {
                R.drawable.zte_foundry_forklift_v1_runtime
            } else {
                R.drawable.zte_foundry_forklift_load_v1_runtime
            }

            Image(
                painter = painterResource(forkliftFrame),
                contentDescription = null,
                modifier = Modifier
                    .size(44.dp)
                    .graphicsLayer {
                        translationX = widthPx * (.34f + route * .24f)
                        translationY = heightPx * (.66f - route * .07f)
                        alpha = if (reducedMotion) .76f else .96f
                        scaleX = if (route < .5f) .74f else -.74f
                        scaleY = .74f
                    }
            )

            // Authored spark/smoke activity gives industrial lots a visible production beat
            // without introducing another animation clock. The overlay freezes to a subtle,
            // readable state in reduced-motion / battery-saver mode.
            Image(
                painter = painterResource(R.drawable.zte_foundry_machine_activity_t0_runtime),
                contentDescription = null,
                modifier = Modifier
                    .size(if (businessId == 2) 45.dp else 39.dp)
                    .graphicsLayer {
                        val cycle = if (reducedMotion) .35f else (p * 3f) % 1f
                        val pulse = 1f - abs(cycle * 2f - 1f)
                        translationX = widthPx * if (businessId == 2) .51f else .57f
                        translationY = heightPx * if (businessId == 2) .34f else .40f
                        alpha = if (reducedMotion) .34f else (.28f + pulse * .64f)
                        val activityScale = if (reducedMotion) .70f else (.66f + pulse * .18f)
                        scaleX = activityScale
                        scaleY = activityScale
                        rotationZ = if (reducedMotion) 0f else (cycle - .5f) * 5f
                    }
            )
        }
    }
}
