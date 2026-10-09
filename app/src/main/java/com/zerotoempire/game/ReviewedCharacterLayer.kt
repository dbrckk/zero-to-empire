package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import androidx.compose.ui.unit.dp

private data class CharacterPlacement(
    val role: ReviewedCharacterRole,
    val action: ReviewedCharacterAction,
    /** Relative top-left inside the city's stage, not the device screen. */
    val xFraction: Float,
    val yFraction: Float,
    val size: Dp,
    val phaseFrames: Int,
    /** Total horizontal journey in stage-width units. */
    val travelFraction: Float = 0f,
)

internal data class AmbientCharacterMotion(
    val xOffsetFraction: Float,
    val spriteFrame: Int,
    val facingLeft: Boolean,
)

/**
 * One shared clock for all characters, with a genuine pedestrian journey.
 *
 * 80 frames in one direction, a 4-frame turn, 80 on the way back and a
 * 4-frame turn: feet animate only when movement occurs. Source WALK frames
 * always face right, so the return journey must flip the sprite.
 * The function is pure: unit tests can prove no teleport/foot-slide caused
 * by animation while the actor is standing still.
 */
internal fun ambientCharacterMotion(
    action: ReviewedCharacterAction,
    worldFrame: Int,
    phaseFrames: Int,
    travelFraction: Float,
    reducedMotion: Boolean,
): AmbientCharacterMotion {
    val frames = reviewedCharacterFrameCount(action)
    if (reducedMotion) {
        return AmbientCharacterMotion(0f, Math.floorMod(phaseFrames, frames), false)
    }
    if (action != ReviewedCharacterAction.WALK || travelFraction <= 0f) {
        return AmbientCharacterMotion(
            0f, Math.floorMod(worldFrame + phaseFrames, frames), false,
        )
    }
    val movingFrames = 80
    val turnFrames = 4
    val halfCycle = movingFrames + turnFrames
    val phase = Math.floorMod(worldFrame + phaseFrames, 2 * halfCycle)
    val returning = phase >= halfCycle
    val local = if (returning) phase - halfCycle else phase
    val inTurn = local >= movingFrames
    val progress = if (inTurn) 1f else local.toFloat() / movingFrames
    val x = travelFraction * (
        if (returning) .5f - progress else progress - .5f
    )
    return AmbientCharacterMotion(
        xOffsetFraction = x,
        spriteFrame = if (inTurn) 0 else local % frames,
        facingLeft = returning,
    )
}

/**
 * Characters are anchored to the *stage*, not an assumed 360dp-wide phone.
 * Only reviewed atlas frames are rendered; all speculative candidates remain
 * outside canonical runtime until the art approval and Android build gates.
 */
@Composable
internal fun ReviewedCharacterLayer(
    eraIndex: Int,
    worldFrame: Int,
    reducedMotion: Boolean,
    modifier: Modifier = Modifier,
) {
    val context = LocalContext.current
    val lateEraScale = if (eraIndex >= 4) 1.08f else 1f

    val placements = remember {
        listOf(
            CharacterPlacement(ReviewedCharacterRole.OPERATOR, ReviewedCharacterAction.WORK, .094f, .494f, 45.dp, 0),
            CharacterPlacement(ReviewedCharacterRole.TECHNICIAN, ReviewedCharacterAction.WALK, .311f, .603f, 42.dp, 3, .18f),
            CharacterPlacement(ReviewedCharacterRole.LOGISTICS, ReviewedCharacterAction.WALK, .564f, .734f, 43.dp, 5, .16f),
            CharacterPlacement(ReviewedCharacterRole.ENGINEER, ReviewedCharacterAction.WORK, .794f, .535f, 46.dp, 7),
            CharacterPlacement(ReviewedCharacterRole.LOGISTICS, ReviewedCharacterAction.IDLE, .200f, .803f, 36.dp, 2),
            CharacterPlacement(ReviewedCharacterRole.OPERATOR, ReviewedCharacterAction.WALK, .681f, .839f, 37.dp, 6, .18f),
            CharacterPlacement(ReviewedCharacterRole.TECHNICIAN, ReviewedCharacterAction.WORK, .883f, .697f, 39.dp, 4),
            CharacterPlacement(ReviewedCharacterRole.ENGINEER, ReviewedCharacterAction.IDLE, .433f, .863f, 35.dp, 1),
        )
    }

    val atlases = remember {
        placements
            .map { it.role to it.action }
            .distinct()
            .associateWith { (role, action) ->
                ImageBitmap.imageResource(
                    context.resources,
                    reviewedCharacterRasterRes(role, action),
                )
            }
    }

    BoxWithConstraints(modifier.fillMaxSize()) {
        val scale = minOf(maxWidth.value / 360f, maxHeight.value / 620f)
            .coerceIn(.75f, 1.20f) * lateEraScale
        placements.forEach { placement ->
            val sample = ambientCharacterMotion(
                action = placement.action,
                worldFrame = worldFrame,
                phaseFrames = placement.phaseFrames,
                travelFraction = placement.travelFraction,
                reducedMotion = reducedMotion,
            )
            val dimension = placement.size * scale
            // Prevent clipped sprites at the right/bottom of narrow stages.
            val x = (maxWidth * (placement.xFraction + sample.xOffsetFraction))
                .coerceIn(0.dp, (maxWidth - dimension).coerceAtLeast(0.dp))
            val y = (maxHeight * placement.yFraction)
                .coerceIn(0.dp, (maxHeight - dimension).coerceAtLeast(0.dp))
            CharacterAtlasFrame(
                atlas = atlases.getValue(placement.role to placement.action),
                frame = sample.spriteFrame,
                modifier = Modifier
                    .offset(x = x, y = y)
                    .size(dimension)
                    .graphicsLayer { scaleX = if (sample.facingLeft) -1f else 1f },
            )
        }
    }
}

@Composable
internal fun CharacterAtlasFrame(
    atlas: ImageBitmap,
    frame: Int,
    modifier: Modifier,
) {
    Canvas(modifier) {
        val sourceFrame = frame.coerceIn(0, REVIEWED_CHARACTER_COLUMNS * REVIEWED_CHARACTER_ROWS - 1)
        val srcX = (sourceFrame % REVIEWED_CHARACTER_COLUMNS) * REVIEWED_CHARACTER_CELL_SIDE
        val srcY = (sourceFrame / REVIEWED_CHARACTER_COLUMNS) * REVIEWED_CHARACTER_CELL_SIDE
        val side = minOf(size.width, size.height).toInt().coerceAtLeast(1)
        val dstX = ((size.width - side) / 2f).toInt()
        val dstY = ((size.height - side) / 2f).toInt()

        drawOval(
            color = Color.Black.copy(alpha = .22f),
            topLeft = Offset(size.width * .23f, size.height * .78f),
            size = Size(size.width * .54f, size.height * .11f),
        )
        drawImage(
            image = atlas,
            srcOffset = IntOffset(srcX, srcY),
            srcSize = IntSize(REVIEWED_CHARACTER_CELL_SIDE, REVIEWED_CHARACTER_CELL_SIDE),
            dstOffset = IntOffset(dstX, dstY),
            dstSize = IntSize(side, side),
        )
    }
}
