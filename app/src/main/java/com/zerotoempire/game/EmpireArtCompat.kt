package com.zerotoempire.game

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.Dp

@Composable
fun BusinessArtIcon(id: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    BusinessArtIcon(id = id, level = 0, iconSize = iconSize, modifier = modifier)
}
