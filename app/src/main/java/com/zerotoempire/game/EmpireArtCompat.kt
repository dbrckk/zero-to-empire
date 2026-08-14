package com.zerotoempire.game

import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.Dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun BusinessArtIcon(id: Int, iconSize: Dp, modifier: Modifier = Modifier) {
    val vm: GameViewModel = viewModel()
    val state by vm.state.collectAsStateWithLifecycle()
    val level = state.businesses.firstOrNull { it.id == id }?.level ?: 0
    BusinessArtIcon(id = id, level = level, iconSize = iconSize, modifier = modifier)
}
