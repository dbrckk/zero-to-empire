package com.zerotoempire.game

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

@Composable
fun ManagerPortrait(businessId: Int, size: Dp = 58.dp) {
    when {
        businessId in 0..3 -> ManagerGroup01Portrait(businessId = businessId, portraitSize = size)
        businessId in 4..7 -> ManagerGroup02Portrait(businessId = businessId, portraitSize = size)
        businessId in 8..9 -> ManagerGroup03Portrait(businessId = businessId, portraitSize = size)
        else -> EndgameManagerPortrait(businessId = businessId, portraitSize = size)
    }
}

@Composable
fun EraVista(eraIndex: Int, modifier: Modifier = Modifier) {
    EraVistaAAA(eraIndex = eraIndex, modifier = modifier)
}
