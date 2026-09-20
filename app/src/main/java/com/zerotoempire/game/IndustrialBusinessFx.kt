package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val IndustrialFxFrameSize = 128
private const val IndustrialFxColumns = 4
private const val IndustrialFxFrameCount = 8

private enum class IndustrialFxKind {
    SMALL_FURNACE,
    LARGE_PLASMA,
    SMOKE,
}

@Composable
private fun IndustrialFxLoop(
    kind: IndustrialFxKind,
    modifier: Modifier = Modifier,
) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val lowPower = remember(context) { MotionQuality.lowPowerMode(context) }
    val resource = when (kind) {
        IndustrialFxKind.SMALL_FURNACE -> R.drawable.zte_fx_01_final
        IndustrialFxKind.LARGE_PLASMA -> R.drawable.zte_fx_02_final
        IndustrialFxKind.SMOKE -> R.drawable.zte_fx_03_final
    }
    val sheet: ImageBitmap = remember(resource) {
        BitmapFactory.decodeResource(context.resources, resource).asImageBitmap()
    }
    var frame by remember { mutableIntStateOf(0) }

    LaunchedEffect(kind, reducedMotion, lowPower) {
        frame = when (kind) {
            IndustrialFxKind.SMALL_FURNACE -> 3
            IndustrialFxKind.LARGE_PLASMA -> 4
            IndustrialFxKind.SMOKE -> 3
        }
        if (!reducedMotion) {
            while (true) {
                delay(if (lowPower) 250 else 125)
                frame = (frame + if (lowPower) 2 else 1) % IndustrialFxFrameCount
            }
        }
    }

    Canvas(modifier) {
        val side = when (kind) {
            IndustrialFxKind.SMALL_FURNACE -> size.minDimension * .24f
            IndustrialFxKind.LARGE_PLASMA -> size.minDimension * .34f
            IndustrialFxKind.SMOKE -> size.minDimension * .28f
        }
        val destination = when (kind) {
            IndustrialFxKind.SMALL_FURNACE -> Offset(size.width * .18f, size.height * .49f)
            IndustrialFxKind.LARGE_PLASMA -> Offset(size.width * .34f, size.height * .40f)
            IndustrialFxKind.SMOKE -> Offset(size.width * .56f, size.height * .06f)
        }
        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                (frame % IndustrialFxColumns) * IndustrialFxFrameSize,
                (frame / IndustrialFxColumns) * IndustrialFxFrameSize,
            ),
            srcSize = IntSize(IndustrialFxFrameSize, IndustrialFxFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(side.toInt().coerceAtLeast(1), side.toInt().coerceAtLeast(1)),
            alpha = when (kind) {
                IndustrialFxKind.SMALL_FURNACE -> .72f
                IndustrialFxKind.LARGE_PLASMA -> .68f
                IndustrialFxKind.SMOKE -> .46f
            },
        )
    }
}

/**
 * Brings the remaining historical industrial FX into visible gameplay without
 * replacing the authored building identity. Reduced-motion users receive a
 * stable representative frame; battery saver advances at half cadence.
 */
@Composable
internal fun IndustrialBusinessFx(
    businessId: Int,
    tier: Int,
    modifier: Modifier = Modifier,
) {
    when (businessId) {
        2 -> {
            if (tier >= 2) {
                IndustrialFxLoop(IndustrialFxKind.SMALL_FURNACE, modifier)
            }
        }
        3 -> {
            if (tier >= 2) {
                IndustrialFxLoop(IndustrialFxKind.SMOKE, modifier)
            }
            if (tier >= 4) {
                IndustrialFxLoop(IndustrialFxKind.LARGE_PLASMA, modifier)
            }
        }
    }
}
