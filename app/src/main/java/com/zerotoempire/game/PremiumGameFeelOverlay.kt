package com.zerotoempire.game

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier

/**
 * Non-blocking V2 feedback layer. It deliberately owns no economy state and
 * simply reacts to the already-sanitized GameState supplied by the main UI.
 */
@Composable
fun PremiumGameFeelOverlay(state: GameState, modifier: Modifier = Modifier) {
    Box(modifier.fillMaxSize()) {
        PremiumMilestoneCelebration(state, Modifier.fillMaxSize())
    }
}
