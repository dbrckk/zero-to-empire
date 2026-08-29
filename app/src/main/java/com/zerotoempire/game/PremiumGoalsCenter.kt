package com.zerotoempire.game

import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun PremiumGoalsCenter(
    vm: GameViewModel,
    state: GameState,
    meta: PlayerMeta,
    modifier: Modifier = Modifier
) {
    val missions = vm.missions()
    val achievements = vm.achievements()
    val missionDone = missions.count { it.claimed }
    val missionReady = missions.count { it.completed && !it.claimed }
    val achievementDone = achievements.count { it.claimed }
    val achievementReady = achievements.count { it.unlocked && !it.claimed }
    val dynasty = DynastyProgression.status(state, meta)

    LazyColumn(
        modifier.fillMaxSize(),
        contentPadding = PaddingValues(16.dp, 18.dp, 16.dp, 30.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        item {
            Column {
                Text("COMMAND CENTER", color = EmpireColors.TextPrimary, fontSize = 27.sp, fontWeight = FontWeight.Black)
                Text("Daily, weekly and long-term objectives", color = EmpireColors.TextSecondary, fontSize = 11.sp)
            }
        }

        item {
            Surface(
                color = EmpireColors.Cyan.copy(alpha = .08f),
                shape = RoundedCornerShape(24.dp),
                modifier = Modifier.fillMaxWidth().border(1.dp, EmpireColors.Cyan.copy(alpha = .22f), RoundedCornerShape(24.dp))
            ) {
                Column(Modifier.padding(16.dp)) {
                    Text("CAMPAIGN STATUS", color = EmpireColors.Cyan, fontSize = 10.sp, fontWeight = FontWeight.Black, letterSpacing = 1.5.sp)
                    Spacer(Modifier.height(5.dp))
                    Text("Dynasty Rank ${dynasty.rank.level}", color = EmpireColors.TextPrimary, fontSize = 20.sp, fontWeight = FontWeight.Black)
                    Text(dynasty.rank.title, color = EmpireColors.GoldBright, fontSize = 11.sp, fontWeight = FontWeight.Bold)
                    Spacer(Modifier.height(12.dp))
                    LinearProgressIndicator(
                        progress = { dynasty.progress.coerceIn(0f, 1f) },
                        modifier = Modifier.fillMaxWidth().height(6.dp),
                        color = EmpireColors.Cyan,
                        trackColor = EmpireColors.SurfaceHigh
                    )
                    Spacer(Modifier.height(8.dp))
                    Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
                        GoalStat("MISSIONS", "$missionDone/${missions.size}", missionReady)
                        GoalStat("ACHIEVEMENTS", "$achievementDone/${achievements.size}", achievementReady)
                        GoalStat("STREAK", "${meta.streakDays}D", 0)
                    }
                }
            }
        }

        item {
            val claimable = vm.canClaimDaily()
            Surface(
                color = EmpireColors.Gold.copy(alpha = .10f),
                shape = RoundedCornerShape(22.dp),
                modifier = Modifier.fillMaxWidth().border(1.dp, EmpireColors.Gold.copy(alpha = .24f), RoundedCornerShape(22.dp))
            ) {
                Column(Modifier.padding(16.dp)) {
                    Text("DAILY DROP", color = EmpireColors.Gold, fontSize = 10.sp, fontWeight = FontWeight.Black, letterSpacing = 1.5.sp)
                    Text("${meta.streakDays} day streak", color = EmpireColors.TextPrimary, fontSize = 20.sp, fontWeight = FontWeight.Black)
                    Text(
                        if (claimable) "Reward ready. Keep the streak alive." else "Today's reward secured.",
                        color = EmpireColors.TextSecondary,
                        fontSize = 10.sp
                    )
                    Spacer(Modifier.height(11.dp))
                    Button(onClick = { vm.claimDaily() }, enabled = claimable, modifier = Modifier.fillMaxWidth().height(46.dp), shape = RoundedCornerShape(14.dp)) {
                        Text(if (claimable) "CLAIM DAILY REWARD" else "CLAIMED TODAY", fontWeight = FontWeight.Black, fontSize = 10.sp)
                    }
                }
            }
        }

        item {
            GoalSectionHeader("WEEKLY OPERATION", "Rotating objective with premium rewards")
        }
        item { ChallengeDock(vm, Modifier.fillMaxWidth()) }

        item {
            GoalSectionHeader("MISSIONS", if (missionReady > 0) "$missionReady reward${if (missionReady == 1) "" else "s"} ready" else "Short-term progression")
        }
        items(missions, key = { it.id }) { mission ->
            PremiumGoalCard(
                title = mission.title,
                subtitle = "+${mission.rewardGems} gems",
                progress = mission.fraction,
                stateLabel = when {
                    mission.claimed -> "DONE"
                    mission.completed -> "CLAIM"
                    else -> "${(mission.fraction * 100).toInt()}%"
                },
                enabled = mission.completed && !mission.claimed,
                accent = if (mission.completed && !mission.claimed) EmpireColors.Gold else EmpireColors.Cyan,
                onClick = { vm.claimMission(mission.id) }
            )
        }

        item {
            GoalSectionHeader(
                "ACHIEVEMENTS",
                if (achievementReady > 0) "$achievementReady unlocked reward${if (achievementReady == 1) "" else "s"}" else "Permanent campaign milestones"
            )
        }
        items(achievements, key = { it.id }) { achievement ->
            PremiumGoalCard(
                title = achievement.title,
                subtitle = achievement.description,
                progress = if (achievement.unlocked) 1f else 0f,
                stateLabel = when {
                    achievement.claimed -> "DONE"
                    achievement.unlocked -> "+${achievement.rewardGems} GEMS"
                    else -> "LOCKED"
                },
                enabled = achievement.unlocked && !achievement.claimed,
                accent = if (achievement.unlocked) EmpireColors.Violet else EmpireColors.TextSecondary,
                onClick = { vm.claimAchievement(achievement.id) }
            )
        }
    }
}

@Composable
private fun GoalStat(label: String, value: String, ready: Int) {
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Text(value, color = EmpireColors.TextPrimary, fontSize = 15.sp, fontWeight = FontWeight.Black)
        Text(label, color = EmpireColors.TextSecondary, fontSize = 8.sp, fontWeight = FontWeight.Bold)
        if (ready > 0) Text("$ready READY", color = EmpireColors.GoldBright, fontSize = 8.sp, fontWeight = FontWeight.Black)
    }
}

@Composable
private fun GoalSectionHeader(title: String, subtitle: String) {
    Column {
        Text(title, color = EmpireColors.TextPrimary, fontSize = 15.sp, fontWeight = FontWeight.Black, letterSpacing = 1.sp)
        Text(subtitle, color = EmpireColors.TextSecondary, fontSize = 10.sp)
    }
}

@Composable
private fun PremiumGoalCard(
    title: String,
    subtitle: String,
    progress: Float,
    stateLabel: String,
    enabled: Boolean,
    accent: Color,
    onClick: () -> Unit
) {
    Surface(
        color = if (enabled) accent.copy(alpha = .09f) else EmpireColors.Surface.copy(alpha = .91f),
        shape = RoundedCornerShape(20.dp),
        modifier = Modifier.fillMaxWidth().border(
            1.dp,
            if (enabled) accent.copy(alpha = .35f) else Color.White.copy(alpha = .05f),
            RoundedCornerShape(20.dp)
        )
    ) {
        Column(Modifier.padding(14.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Column(Modifier.weight(1f)) {
                    Text(title, color = EmpireColors.TextPrimary, fontWeight = FontWeight.Black, fontSize = 14.sp, maxLines = 1, overflow = TextOverflow.Ellipsis)
                    Text(subtitle, color = EmpireColors.TextSecondary, fontSize = 10.sp, maxLines = 2, overflow = TextOverflow.Ellipsis)
                }
                TextButton(onClick = onClick, enabled = enabled) {
                    Text(stateLabel, color = if (enabled) accent else EmpireColors.TextSecondary, fontWeight = FontWeight.Black, fontSize = 9.sp)
                }
            }
            Spacer(Modifier.height(6.dp))
            LinearProgressIndicator(
                progress = { progress.coerceIn(0f, 1f) },
                modifier = Modifier.fillMaxWidth().height(5.dp),
                color = accent,
                trackColor = EmpireColors.SurfaceHigh
            )
        }
    }
}
