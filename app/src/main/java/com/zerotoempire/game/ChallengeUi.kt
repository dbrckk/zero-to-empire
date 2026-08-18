package com.zerotoempire.game

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import java.time.LocalDate

/** Compact entry point that makes the rotating challenge system reachable during normal play. */
@Composable
fun ChallengeDock(vm: GameViewModel, modifier: Modifier = Modifier) {
    val state by vm.state.collectAsStateWithLifecycle()
    val meta by vm.meta.collectAsStateWithLifecycle()
    val currentWeek = ChallengeRotation.weeklyKey()
    LaunchedEffect(currentWeek, meta.challengeWeekKey) {
        if (meta.challengeWeekKey != currentWeek) vm.ensureChallengeWeek()
    }
    val challenges = remember(state, meta, currentWeek) { ChallengeRotation.current(state, meta) }
    val completed = challenges.count { it.completed }
    val unclaimed = challenges.count { it.completed && !it.claimed }
    var open by remember { mutableStateOf(false) }

    FilledTonalButton(
        onClick = { open = true },
        modifier = modifier,
        shape = RoundedCornerShape(50),
        contentPadding = PaddingValues(horizontal = 12.dp, vertical = 7.dp)
    ) {
        MetaSprite(MetaSpriteKind.ACHIEVEMENT, 23.dp, active = unclaimed > 0)
        Spacer(Modifier.width(6.dp))
        Text(
            if (unclaimed > 0) "WEEKLY • $unclaimed CLAIM" else "WEEKLY • $completed/${challenges.size}",
            fontSize = 10.sp,
            fontWeight = FontWeight.Black
        )
    }

    if (open) {
        ChallengeDialog(
            challenges = challenges,
            onClaim = { vm.claimChallenge(it) },
            onDismiss = { open = false }
        )
    }
}

@Composable
private fun ChallengeDialog(
    challenges: List<TimedChallenge>,
    onClaim: (String) -> Boolean,
    onDismiss: () -> Unit
) {
    val haptics = LocalHapticFeedback.current
    AlertDialog(
        onDismissRequest = onDismiss,
        containerColor = EmpireColors.SurfaceHigh,
        title = {
            Column {
                Text("WEEKLY COMMAND", color = EmpireColors.Gold, fontWeight = FontWeight.Black)
                Text(ChallengeRotation.weeklyKey(LocalDate.now()), color = EmpireColors.TextSecondary, fontSize = 10.sp)
            }
        },
        text = {
            Column(verticalArrangement = Arrangement.spacedBy(9.dp)) {
                challenges.forEach { challenge ->
                    Surface(color = EmpireColors.Surface, shape = RoundedCornerShape(14.dp)) {
                        Column(Modifier.fillMaxWidth().padding(12.dp)) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Column(Modifier.weight(1f)) {
                                    Text(challenge.title, color = EmpireColors.TextPrimary, fontWeight = FontWeight.Black)
                                    Text(challenge.description, color = EmpireColors.TextSecondary, fontSize = 10.sp)
                                }
                                Spacer(Modifier.width(8.dp))
                                Row(verticalAlignment = Alignment.CenterVertically) {
                                    MetaSprite(MetaSpriteKind.GEM, 20.dp)
                                    Text("${challenge.rewardGems}", color = EmpireColors.Violet, fontWeight = FontWeight.Black, fontSize = 11.sp)
                                }
                            }
                            Spacer(Modifier.height(8.dp))
                            LinearProgressIndicator(
                                progress = { challenge.fraction },
                                modifier = Modifier.fillMaxWidth().height(4.dp),
                                color = if (challenge.completed) EmpireColors.Success else EmpireColors.Cyan,
                                trackColor = EmpireColors.SurfaceHigh
                            )
                            Spacer(Modifier.height(6.dp))
                            val progressText = when (challenge.metric) {
                                ChallengeMetric.LIFETIME_CASH -> "${EmpireNumberFormat.money(challenge.progress)} / ${EmpireNumberFormat.money(challenge.target)}"
                                else -> "${challenge.progress.toLong()} / ${challenge.target.toLong()}"
                            }
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Text(progressText, color = EmpireColors.TextSecondary, fontSize = 9.sp, modifier = Modifier.weight(1f))
                                Button(
                                    onClick = { if (onClaim(challenge.id)) haptics.performHapticFeedback(HapticFeedbackType.LongPress) },
                                    enabled = challenge.completed && !challenge.claimed,
                                    contentPadding = PaddingValues(horizontal = 10.dp, vertical = 2.dp),
                                    modifier = Modifier.height(30.dp)
                                ) {
                                    Text(
                                        when {
                                            challenge.claimed -> "CLAIMED"
                                            challenge.completed -> "CLAIM"
                                            else -> "ACTIVE"
                                        },
                                        fontSize = 9.sp,
                                        fontWeight = FontWeight.Black
                                    )
                                }
                            }
                        }
                    }
                }
            }
        },
        confirmButton = { TextButton(onClick = onDismiss) { Text("CLOSE") } }
    )
}
