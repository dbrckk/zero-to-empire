package com.zerotoempire.game

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import java.util.Locale

@Composable
fun AscensionAdvisor(state: GameState, modifier: Modifier = Modifier) {
    val total = Progression.prestigeReward(state.lifetimeCash)
    val gain = (total - state.prestigePoints).coerceAtLeast(0)
    if (gain <= 0) return

    val after = state.copy(prestigePoints = total)
    val beforePower = state.prestigeMultiplier * state.legacyMasteryMultiplier
    val afterPower = after.prestigeMultiplier * after.legacyMasteryMultiplier
    val improvement = ((afterPower / beforePower) - 1.0).coerceAtLeast(0.0)
    val recommended = LateGame.recommendedPrestige(state.prestigePoints, state.lifetimeCash)

    Surface(
        modifier = modifier.fillMaxWidth(),
        color = EmpireColors.Violet.copy(alpha = if (recommended) .22f else .12f),
        shape = RoundedCornerShape(16.dp),
        shadowElevation = if (recommended) 10.dp else 3.dp
    ) {
        Row(
            Modifier.padding(horizontal = 12.dp, vertical = 9.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Column(Modifier.weight(1f)) {
                Text(
                    if (recommended) "ASCENSION READY" else "ASCENSION CHARGING",
                    color = if (recommended) EmpireColors.Gold else EmpireColors.TextSecondary,
                    fontWeight = FontWeight.Black,
                    fontSize = 10.sp
                )
                Text(
                    "+$gain LEGACY  •  +${String.format(Locale.US, "%.0f", improvement * 100)}% permanent power",
                    color = EmpireColors.TextPrimary,
                    fontWeight = FontWeight.Bold,
                    fontSize = 10.sp
                )
            }
            Spacer(Modifier.width(10.dp))
            Text(
                "×${String.format(Locale.US, "%.2f", beforePower)} → ×${String.format(Locale.US, "%.2f", afterPower)}",
                color = EmpireColors.Cyan,
                fontWeight = FontWeight.Black,
                fontSize = 10.sp
            )
        }
    }
}
