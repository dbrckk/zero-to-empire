package com.zerotoempire.game

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

private data class CharacterPlacement(
    val role: ReviewedCharacterRole,
    val x: Dp,
    val y: Dp,
    val size: Dp,
)

/** Authored ambient population for the Ascendant city industrial midground. */
@Composable
internal fun ReviewedCharacterLayer(eraIndex: Int, modifier: Modifier = Modifier) {
    val lateEraScale = if (eraIndex >= 4) 1.08f else 1f
    val placements = listOf(
        CharacterPlacement(ReviewedCharacterRole.OPERATOR, 38.dp, 318.dp, 42.dp),
        CharacterPlacement(ReviewedCharacterRole.TECHNICIAN, 126.dp, 397.dp, 44.dp),
        CharacterPlacement(ReviewedCharacterRole.LOGISTICS, 218.dp, 474.dp, 42.dp),
        CharacterPlacement(ReviewedCharacterRole.ENGINEER, 292.dp, 349.dp, 44.dp),
    )

    Box(modifier.fillMaxSize()) {
        placements.forEach { placement ->
            Image(
                painter = painterResource(reviewedCharacterIdleRasterRes(placement.role)),
                contentDescription = null,
                contentScale = ContentScale.Fit,
                modifier = Modifier
                    .offset(placement.x, placement.y)
                    .size(placement.size * lateEraScale),
            )
        }
    }
}
