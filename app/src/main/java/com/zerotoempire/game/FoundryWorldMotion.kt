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
import androidx.compose.runtime.derivedStateOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import kotlin.math.abs

private val WORKER_FRAMES = intArrayOf(
    R.drawable.zte_foundry_worker_raster_f0,
    R.drawable.zte_foundry_worker_raster_f1,
    R.drawable.zte_foundry_worker_raster_f2,
    R.drawable.zte_foundry_worker_raster_f3
)

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
    // Battery Saver and system animator changes must update this active ticker.
    val reducedMotion = MotionQuality.reducedMotion(context)
    val phase = remember { Animatable(.18f) }
    // Image identity changes at 10 fps; sub-frame positioning belongs in graphicsLayer.
    // Reading phase.value in composition would recompose the whole district at ~60 fps.
    val workerStep by remember(phase, reducedMotion) {
        derivedStateOf { if (reducedMotion) 0 else (phase.value * 72f).toInt() }
    }
    val forkliftLoading by remember(phase, reducedMotion) {
        derivedStateOf {
            val route = (phase.value + .63f) % 1f
            !reducedMotion && route >= .32f && route <= .70f
        }
    }

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
        // Four transparent raster frames run at ~10 fps from the existing shared district
        // clock. The second worker is two frames out of phase so the crowd does not march
        // in lockstep. Reduced motion remains a deterministic frozen pose.
        val workerFrameIndex = workerStep and 3
        val secondWorkerFrameIndex = (workerStep + 2) and 3

        Image(
            painter = painterResource(WORKER_FRAMES[workerFrameIndex]),
            contentDescription = null,
            modifier = Modifier
                .size(34.dp)
                .graphicsLayer {
                    val p = phase.value
                    val edgeFade = (minOf(p, 1f - p) * 12f).coerceIn(0f, 1f)
                    translationX = widthPx * (.19f + p * .24f)
                    translationY = heightPx * (.48f + p * .11f)
                    alpha = if (reducedMotion) .76f else (.18f + edgeFade * .74f)
                    scaleX = .92f
                    scaleY = .92f
                }
        )

        Image(
            painter = painterResource(WORKER_FRAMES[secondWorkerFrameIndex]),
            contentDescription = null,
            modifier = Modifier
                .size(29.dp)
                .graphicsLayer {
                    val p = phase.value
                    val q = (p + .52f) % 1f
                    val edgeFade = (minOf(q, 1f - q) * 12f).coerceIn(0f, 1f)
                    translationX = widthPx * (.73f - q * .20f)
                    translationY = heightPx * (.57f + q * .08f)
                    alpha = if (reducedMotion) .62f else (.16f + edgeFade * .66f)
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
                        val p = phase.value
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
            val forkliftFrame = if (forkliftLoading) {
                R.drawable.zte_foundry_forklift_load_v1_runtime
            } else {
                R.drawable.zte_foundry_forklift_v1_runtime
            }

            Image(
                painter = painterResource(forkliftFrame),
                contentDescription = null,
                modifier = Modifier
                    .size(44.dp)
                    .graphicsLayer {
                        val route = if (reducedMotion) .38f else (phase.value + .63f) % 1f
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
                        val p = phase.value
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
