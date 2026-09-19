package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
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
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import androidx.compose.ui.unit.dp

private data class CharacterPlacement(
    val role: ReviewedCharacterRole,
    val action: ReviewedCharacterAction,
    val x: Dp,
    val y: Dp,
    val size: Dp,
    val phaseFrames: Int,
)

/**
 * Authored ambient population for the Ascendant city.
 *
 * The source assets are 4x4 atlases. This renderer crops one 256x256 cell per
 * actor and advances all actors from one shared 10 fps clock, keeping visual
 * density high without starting one independent infinite animation per sprite.
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
            CharacterPlacement(ReviewedCharacterRole.OPERATOR, ReviewedCharacterAction.WORK, 34.dp, 306.dp, 45.dp, 0),
            CharacterPlacement(ReviewedCharacterRole.TECHNICIAN, ReviewedCharacterAction.WALK, 112.dp, 374.dp, 42.dp, 3),
            CharacterPlacement(ReviewedCharacterRole.LOGISTICS, ReviewedCharacterAction.WALK, 203.dp, 455.dp, 43.dp, 5),
            CharacterPlacement(ReviewedCharacterRole.ENGINEER, ReviewedCharacterAction.WORK, 286.dp, 332.dp, 46.dp, 7),
            CharacterPlacement(ReviewedCharacterRole.LOGISTICS, ReviewedCharacterAction.IDLE, 72.dp, 498.dp, 36.dp, 2),
            CharacterPlacement(ReviewedCharacterRole.OPERATOR, ReviewedCharacterAction.WALK, 245.dp, 520.dp, 37.dp, 6),
            CharacterPlacement(ReviewedCharacterRole.TECHNICIAN, ReviewedCharacterAction.WORK, 318.dp, 432.dp, 39.dp, 4),
            CharacterPlacement(ReviewedCharacterRole.ENGINEER, ReviewedCharacterAction.IDLE, 156.dp, 535.dp, 35.dp, 1),
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

    Box(modifier.fillMaxSize()) {
        placements.forEach { placement ->
            val frameCount = reviewedCharacterFrameCount(placement.action)
            val frame = if (reducedMotion) {
                placement.phaseFrames % frameCount
            } else {
                (worldFrame + placement.phaseFrames) % frameCount
            }
            val atlas = atlases.getValue(placement.role to placement.action)

            CharacterAtlasFrame(
                atlas = atlas,
                frame = frame,
                modifier = Modifier
                    .offset(placement.x, placement.y)
                    .size(placement.size * lateEraScale),
            )
        }
    }
}

@Composable
private fun CharacterAtlasFrame(
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
