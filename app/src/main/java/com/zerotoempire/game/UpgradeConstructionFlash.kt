package com.zerotoempire.game

import android.graphics.BitmapFactory
import androidx.compose.foundation.Canvas
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import kotlinx.coroutines.delay

private const val UpgradeFlashFrameSize = 128
private const val UpgradeFlashColumns = 4
private const val UpgradeFlashFrameCount = 8

internal enum class UpgradeVisualImpact {
    NONE,
    LEVEL,
    TIER,
    MASTERY,
}

internal fun upgradeVisualImpact(fromLevel: Int, toLevel: Int): UpgradeVisualImpact = when {
    toLevel <= fromLevel -> UpgradeVisualImpact.NONE
    fromLevel < 1000 && toLevel >= 1000 -> UpgradeVisualImpact.MASTERY
    canonicalBusinessTier(toLevel) > canonicalBusinessTier(fromLevel) -> UpgradeVisualImpact.TIER
    else -> UpgradeVisualImpact.LEVEL
}

/**
 * Progression-aware one-shot feedback.
 *
 * The first composition is intentionally silent: opening an existing save must
 * never look like the player just bought every visible business.
 */
@Composable
internal fun UpgradeConstructionFlash(level: Int, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val reducedMotion = remember(context) { MotionQuality.reducedMotion(context) }
    val constructionSheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_08_final).asImageBitmap()
    }
    val milestoneSheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_06_final).asImageBitmap()
    }

    var previousLevel by remember { mutableIntStateOf(level) }
    var frame by remember { mutableIntStateOf(UpgradeFlashFrameCount) }
    var impact by remember { mutableStateOf(UpgradeVisualImpact.NONE) }

    LaunchedEffect(level, reducedMotion) {
        val nextImpact = upgradeVisualImpact(previousLevel, level)
        previousLevel = level
        impact = nextImpact

        if (nextImpact == UpgradeVisualImpact.NONE) {
            frame = UpgradeFlashFrameCount
            return@LaunchedEffect
        }

        if (reducedMotion) {
            frame = when (nextImpact) {
                UpgradeVisualImpact.LEVEL -> 2
                UpgradeVisualImpact.TIER -> 3
                UpgradeVisualImpact.MASTERY -> 4
                UpgradeVisualImpact.NONE -> UpgradeFlashFrameCount
            }
            delay(
                when (nextImpact) {
                    UpgradeVisualImpact.LEVEL -> 90L
                    UpgradeVisualImpact.TIER -> 150L
                    UpgradeVisualImpact.MASTERY -> 190L
                    UpgradeVisualImpact.NONE -> 0L
                }
            )
            frame = UpgradeFlashFrameCount
            return@LaunchedEffect
        }

        repeat(UpgradeFlashFrameCount) { index ->
            frame = index
            delay(
                when (nextImpact) {
                    UpgradeVisualImpact.LEVEL -> 72L
                    UpgradeVisualImpact.TIER -> 95L
                    UpgradeVisualImpact.MASTERY -> 110L
                    UpgradeVisualImpact.NONE -> 72L
                }
            )
        }
        frame = UpgradeFlashFrameCount
    }

    if (frame >= UpgradeFlashFrameCount || impact == UpgradeVisualImpact.NONE) return

    Canvas(modifier) {
        val scale = when (impact) {
            UpgradeVisualImpact.LEVEL -> .44f
            UpgradeVisualImpact.TIER -> .78f
            UpgradeVisualImpact.MASTERY -> .96f
            UpgradeVisualImpact.NONE -> 0f
        }
        val alpha = when (impact) {
            UpgradeVisualImpact.LEVEL -> .58f
            UpgradeVisualImpact.TIER -> .90f
            UpgradeVisualImpact.MASTERY -> 1f
            UpgradeVisualImpact.NONE -> 0f
        }
        val effectSize = size.minDimension * scale
        val destination = Offset(
            (size.width - effectSize) * .5f,
            size.height * when (impact) {
                UpgradeVisualImpact.LEVEL -> .30f
                UpgradeVisualImpact.TIER -> .12f
                UpgradeVisualImpact.MASTERY -> .02f
                UpgradeVisualImpact.NONE -> .30f
            }
        )

        drawImage(
            image = constructionSheet,
            srcOffset = IntOffset(
                (frame % UpgradeFlashColumns) * UpgradeFlashFrameSize,
                (frame / UpgradeFlashColumns) * UpgradeFlashFrameSize,
            ),
            srcSize = IntSize(UpgradeFlashFrameSize, UpgradeFlashFrameSize),
            dstOffset = IntOffset(destination.x.toInt(), destination.y.toInt()),
            dstSize = IntSize(effectSize.toInt(), effectSize.toInt()),
            alpha = alpha,
        )

        if (impact == UpgradeVisualImpact.TIER || impact == UpgradeVisualImpact.MASTERY) {
            val pulseSize = (effectSize * if (impact == UpgradeVisualImpact.MASTERY) 1.05f else .86f)
                .toInt().coerceAtLeast(1)
            val pulseOffset = IntOffset(
                (size.width / 2f - pulseSize / 2f).toInt(),
                (size.height * .40f - pulseSize / 2f).toInt(),
            )
            drawImage(
                image = milestoneSheet,
                srcOffset = IntOffset(
                    (frame % UpgradeFlashColumns) * UpgradeFlashFrameSize,
                    (frame / UpgradeFlashColumns) * UpgradeFlashFrameSize,
                ),
                srcSize = IntSize(UpgradeFlashFrameSize, UpgradeFlashFrameSize),
                dstOffset = pulseOffset,
                dstSize = IntSize(pulseSize, pulseSize),
                alpha = if (impact == UpgradeVisualImpact.MASTERY) .88f else .62f,
            )
        }

        if (!reducedMotion && impact == UpgradeVisualImpact.MASTERY) {
            val t = frame.toFloat() / (UpgradeFlashFrameCount - 1).coerceAtLeast(1)
            drawCircle(
                color = EmpireArtPalette.GoldHot.copy(alpha = (1f - t) * .78f),
                radius = size.minDimension * (.18f + t * .32f),
                center = Offset(size.width * .5f, size.height * .48f),
                style = Stroke(width = 3f),
            )
            drawCircle(
                color = Color.White.copy(alpha = (1f - t) * .34f),
                radius = size.minDimension * (.10f + t * .24f),
                center = Offset(size.width * .5f, size.height * .48f),
                style = Stroke(width = 1.5f),
            )
        }
    }
}
