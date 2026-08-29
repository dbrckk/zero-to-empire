package com.zerotoempire.game

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp

@Composable
fun PremiumUpgradeTreeScreen(vm: GameViewModel, state: GameState) {
    LazyColumn(
        modifier = Modifier.fillMaxSize(),
        contentPadding = PaddingValues(16.dp, 18.dp, 16.dp, 30.dp),
        verticalArrangement = Arrangement.spacedBy(14.dp)
    ) {
        item { PremiumUpgradeTree(vm, state, Modifier.fillMaxWidth()) }
        item {
            Button(
                onClick = vm::activateProfitBoost,
                modifier = Modifier.fillMaxWidth().height(50.dp)
            ) {
                Text("⚡ WATCH REWARD  •  ×2 PROFITS", fontWeight = FontWeight.Black)
            }
        }
    }
}
