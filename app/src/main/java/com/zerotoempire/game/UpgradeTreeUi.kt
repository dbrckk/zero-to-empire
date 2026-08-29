package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun PremiumUpgradeTree(
    vm: GameViewModel,
    state: GameState,
    modifier: Modifier = Modifier
) {
    val nodes = UpgradeProgression.nodes(state)
    val overall = UpgradeProgression.overallProgress(state)
    val mastered = UpgradeProgression.masteredCount(state)
    val unlockedTier = UpgradeProgression.unlockedTier(state)

    Column(modifier, verticalArrangement = Arrangement.spacedBy(0.dp)) {
        Surface(
            color = EmpireColors.Violet.copy(alpha = .12f),
            shape = RoundedCornerShape(24.dp),
            modifier = Modifier.fillMaxWidth().border(
                1.dp,
                EmpireColors.Violet.copy(alpha = .32f),
                RoundedCornerShape(24.dp)
            )
        ) {
            Column(Modifier.padding(16.dp)) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Column(Modifier.weight(1f)) {
                        Text(
                            "PERMANENT LAB",
                            color = EmpireColors.Violet,
                            fontSize = 10.sp,
                            fontWeight = FontWeight.Black,
                            letterSpacing = 1.7.sp
                        )
                        Text(
                            "EMPIRE TECHNOLOGY TREE",
                            color = EmpireColors.TextPrimary,
                            fontSize = 18.sp,
                            fontWeight = FontWeight.Black
                        )
                    }
                    Text(
                        "${state.gems} GEMS",
                        color = EmpireColors.GoldBright,
                        fontSize = 13.sp,
                        fontWeight = FontWeight.Black
                    )
                }
                Spacer(Modifier.height(11.dp))
                LinearProgressIndicator(
                    progress = { overall },
                    modifier = Modifier.fillMaxWidth().height(6.dp),
                    color = EmpireColors.Violet,
                    trackColor = EmpireColors.SurfaceHigh
                )
                Spacer(Modifier.height(7.dp))
                Row(Modifier.fillMaxWidth()) {
                    Text(
                        "TIER $unlockedTier/${UpgradeProgression.TIER_COUNT}",
                        color = EmpireColors.Cyan,
                        fontSize = 9.sp,
                        fontWeight = FontWeight.Black
                    )
                    Spacer(Modifier.weight(1f))
                    Text(
                        "$mastered/${nodes.size} MASTERED  •  ${(overall * 100).toInt()}%",
                        color = EmpireColors.TextSecondary,
                        fontSize = 9.sp,
                        fontWeight = FontWeight.Bold
                    )
                }
            }
        }

        nodes.forEachIndexed { index, node ->
            if (index > 0) UpgradeConnector(active = node.state != UpgradeNodeState.LOCKED)
            val upgrade = Upgrades.catalog.first { it.id == node.id }
            UpgradeTreeNode(
                upgradeName = upgrade.name,
                description = upgrade.description,
                gemCost = upgrade.gemCost,
                node = node,
                gems = state.gems,
                onUpgrade = { vm.buyUpgrade(node.id) }
            )
        }
    }
}

@Composable
private fun UpgradeConnector(active: Boolean) {
    Box(Modifier.fillMaxWidth().height(28.dp), contentAlignment = Alignment.Center) {
        Canvas(Modifier.size(18.dp, 28.dp)) {
            val color = if (active) EmpireColors.Violet else EmpireColors.TextSecondary.copy(alpha = .20f)
            drawLine(
                color = color.copy(alpha = if (active) .65f else .22f),
                start = Offset(size.width / 2f, 0f),
                end = Offset(size.width / 2f, size.height),
                strokeWidth = if (active) 4f else 2f
            )
            drawCircle(
                color = color,
                radius = if (active) 5f else 3f,
                center = Offset(size.width / 2f, size.height / 2f)
            )
        }
    }
}

@Composable
private fun UpgradeTreeNode(
    upgradeName: String,
    description: String,
    gemCost: Int,
    node: UpgradeProgressNode,
    gems: Int,
    onUpgrade: () -> Unit
) {
    val mastered = node.state == UpgradeNodeState.MASTERED
    val locked = node.state == UpgradeNodeState.LOCKED
    val canBuy = !mastered && !locked && gems >= gemCost
    val accent = when (node.state) {
        UpgradeNodeState.MASTERED -> EmpireColors.Cyan
        UpgradeNodeState.IN_PROGRESS -> EmpireColors.Violet
        UpgradeNodeState.AVAILABLE -> EmpireColors.Gold
        UpgradeNodeState.LOCKED -> EmpireColors.TextSecondary
    }
    val status = when (node.state) {
        UpgradeNodeState.MASTERED -> "MASTERED"
        UpgradeNodeState.IN_PROGRESS -> "IN DEVELOPMENT"
        UpgradeNodeState.AVAILABLE -> "AVAILABLE"
        UpgradeNodeState.LOCKED -> "LOCKED"
    }

    Surface(
        color = when (node.state) {
            UpgradeNodeState.MASTERED -> EmpireColors.Cyan.copy(alpha = .09f)
            UpgradeNodeState.IN_PROGRESS -> EmpireColors.Violet.copy(alpha = .10f)
            UpgradeNodeState.AVAILABLE -> EmpireColors.Gold.copy(alpha = .08f)
            UpgradeNodeState.LOCKED -> EmpireColors.Surface.copy(alpha = .58f)
        },
        shape = RoundedCornerShape(22.dp),
        modifier = Modifier.fillMaxWidth().border(
            1.dp,
            accent.copy(alpha = if (locked) .12f else .34f),
            RoundedCornerShape(22.dp)
        )
    ) {
        Column(Modifier.padding(15.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Box(
                    Modifier.size(42.dp)
                        .background(accent.copy(alpha = .14f), CircleShape)
                        .border(1.dp, accent.copy(alpha = .45f), CircleShape),
                    contentAlignment = Alignment.Center
                ) {
                    Text(
                        if (mastered) "✓" else "${node.tier}",
                        color = accent,
                        fontSize = 15.sp,
                        fontWeight = FontWeight.Black
                    )
                }
                Spacer(Modifier.size(11.dp))
                Column(Modifier.weight(1f)) {
                    Text(
                        "TIER ${node.tier}  •  $status",
                        color = accent,
                        fontSize = 9.sp,
                        fontWeight = FontWeight.Black,
                        letterSpacing = .8.sp
                    )
                    Text(
                        upgradeName,
                        color = if (locked) EmpireColors.TextSecondary else EmpireColors.TextPrimary,
                        fontSize = 16.sp,
                        fontWeight = FontWeight.Black,
                        maxLines = 1,
                        overflow = TextOverflow.Ellipsis
                    )
                    Text(
                        description,
                        color = EmpireColors.TextSecondary,
                        fontSize = 10.sp,
                        maxLines = 2,
                        overflow = TextOverflow.Ellipsis
                    )
                }
            }

            Spacer(Modifier.height(12.dp))
            LinearProgressIndicator(
                progress = { node.progress.coerceIn(0f, 1f) },
                modifier = Modifier.fillMaxWidth().height(5.dp),
                color = accent,
                trackColor = EmpireColors.SurfaceHigh
            )
            Spacer(Modifier.height(6.dp))
            Row(Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                Text(
                    "RANK ${node.rank}/${node.maxRank}",
                    color = EmpireColors.TextSecondary,
                    fontSize = 9.sp,
                    fontWeight = FontWeight.Bold
                )
                Spacer(Modifier.weight(1f))
                Text(
                    when {
                        mastered -> "COMPLETE"
                        locked -> "INVEST IN PREVIOUS TIER"
                        gems < gemCost -> "NEED ${gemCost - gems} GEMS"
                        else -> "$gemCost GEMS"
                    },
                    color = if (canBuy) EmpireColors.GoldBright else EmpireColors.TextSecondary,
                    fontSize = 9.sp,
                    fontWeight = FontWeight.Black
                )
            }
            Spacer(Modifier.height(9.dp))
            Button(
                onClick = onUpgrade,
                enabled = canBuy,
                modifier = Modifier.fillMaxWidth().height(46.dp),
                shape = RoundedCornerShape(14.dp),
                colors = ButtonDefaults.buttonColors(
                    containerColor = accent,
                    contentColor = EmpireColors.Void
                )
            ) {
                Text(
                    when {
                        mastered -> "MASTERED"
                        locked -> "LOCKED"
                        else -> "INVEST  •  $gemCost GEMS"
                    },
                    fontWeight = FontWeight.Black,
                    fontSize = 10.sp
                )
            }
        }
    }
}
