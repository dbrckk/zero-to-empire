package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.imageResource
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import androidx.compose.ui.unit.dp

/**
 * Internal visual-review surface for the complete authored character catalog.
 *
 * This is deliberately not wired into the production navigation. It renders
 * every role/action through the same atlas crop contract used by the game so
 * reviewers can inspect all 24 sheets without changing gameplay composition.
 */
@Composable
internal fun CharacterReviewGallery(
    frame: Int,
    modifier: Modifier = Modifier,
) {
    val context = LocalContext.current
    Column(modifier = modifier, verticalArrangement = Arrangement.spacedBy(6.dp)) {
        ReviewedCharacterRole.entries.forEach { role ->
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceEvenly,
            ) {
                ReviewedCharacterAction.entries.forEach { action ->
                    val atlas = ImageBitmap.imageResource(
                        context.resources,
                        reviewedCharacterRasterRes(role, action),
                    )
                    CharacterReviewFrame(
                        atlas = atlas,
                        frame = frame % reviewedCharacterFrameCount(action),
                    )
                }
            }
        }
    }
}

@Composable
private fun CharacterReviewFrame(
    atlas: ImageBitmap,
    frame: Int,
) {
    Canvas(Modifier.size(52.dp)) {
        val sourceFrame = frame.coerceIn(0, REVIEWED_CHARACTER_COLUMNS * REVIEWED_CHARACTER_ROWS - 1)
        val srcX = (sourceFrame % REVIEWED_CHARACTER_COLUMNS) * REVIEWED_CHARACTER_CELL_SIDE
        val srcY = (sourceFrame / REVIEWED_CHARACTER_COLUMNS) * REVIEWED_CHARACTER_CELL_SIDE
        val side = minOf(size.width, size.height).toInt().coerceAtLeast(1)
        drawOval(
            color = Color.Black.copy(alpha = .22f),
            topLeft = Offset(size.width * .23f, size.height * .78f),
            size = Size(size.width * .54f, size.height * .11f),
        )
        drawImage(
            image = atlas,
            srcOffset = IntOffset(srcX, srcY),
            srcSize = IntSize(REVIEWED_CHARACTER_CELL_SIDE, REVIEWED_CHARACTER_CELL_SIDE),
            dstSize = IntSize(side, side),
        )
    }
}
