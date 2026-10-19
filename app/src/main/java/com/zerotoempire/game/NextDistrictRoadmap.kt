package com.zerotoempire.game
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

/** Live progression goal; all thresholds come from the existing unlock rules. */
@Composable
internal fun NextDistrictRoadmap(state: GameState) {
    val next = ContentUnlocks.nextHiddenBusiness(state)
    Surface(
        color = EmpireColors.Surface.copy(alpha = .96f),
        shape = RoundedCornerShape(16.dp),
        modifier = Modifier.fillMaxWidth().padding(horizontal = 14.dp, vertical = 4.dp),
    ) {
        Column(Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(7.dp)) {
            Text(
                if (next == null) "DISTRICT NETWORK COMPLETE" else "NEXT DISTRICT",
                color = EmpireColors.Cyan, fontSize = 10.sp,
                fontWeight = FontWeight.Black, letterSpacing = 1.sp,
            )
            if (next == null) {
                Text("All districts discovered", color = EmpireColors.TextPrimary, fontSize = 14.sp)
            } else {
                val target = ContentUnlocks.thresholdForBusiness(next.id)
                Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
                    Text(next.name, color = EmpireColors.TextPrimary, fontSize = 15.sp,
                        fontWeight = FontWeight.Bold, maxLines = 1,
                        overflow = TextOverflow.Ellipsis, modifier = Modifier.weight(1f))
                    Text(" " + moneyV2(target), color = EmpireColors.GoldBright,
                        fontSize = 12.sp, fontWeight = FontWeight.Bold)
                }
                LinearProgressIndicator(
                    progress = { ContentUnlocks.progressToNextUnlock(state) },
                    modifier = Modifier.fillMaxWidth().height(7.dp),
                    color = EmpireColors.Cyan,
                    trackColor = Color.White.copy(alpha = .10f),
                )
                Text(
                    "Earn " + moneyV2((target - state.lifetimeCash).coerceAtLeast(0.0)) +
                        " more lifetime capital to discover",
                    color = EmpireColors.TextSecondary, fontSize = 11.sp,
                )
            }
        }
    }
}
