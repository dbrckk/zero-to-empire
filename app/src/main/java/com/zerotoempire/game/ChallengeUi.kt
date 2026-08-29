package com.zerotoempire.game

import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import java.time.LocalDate

/** Goals command module: permanent Dynasty campaign rank + rotating weekly challenges. */
@Composable
fun ChallengeDock(vm: GameViewModel, modifier: Modifier = Modifier) {
    val state by vm.state.collectAsStateWithLifecycle()
    val meta by vm.meta.collectAsStateWithLifecycle()
    val currentWeek = ChallengeRotation.weeklyKey()
    LaunchedEffect(currentWeek, meta.challengeWeekKey) {
        if (meta.challengeWeekKey != currentWeek) vm.ensureChallengeWeek()
    }
    val challenges = remember(state, meta, currentWeek) { ChallengeRotation.current(state, meta) }
    val dynasty = remember(state.prestigePoints, meta) { DynastyProgression.status(state, meta) }
    val completed = challenges.count { it.completed }
    val unclaimed = challenges.count { it.completed && !it.claimed }
    var open by remember { mutableStateOf(false) }

    Column(modifier, verticalArrangement = Arrangement.spacedBy(9.dp)) {
        Surface(
            color = EmpireColors.Violet.copy(alpha = .10f),
            shape = RoundedCornerShape(22.dp),
            modifier = Modifier
                .fillMaxWidth()
                .border(1.dp, EmpireColors.Violet.copy(alpha = .22f), RoundedCornerShape(22.dp))
        ) {
            Column(Modifier.padding(15.dp)) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    MetaSprite(MetaSpriteKind.ACHIEVEMENT, 42.dp, active = true, progress = dynasty.progress)
                    Spacer(Modifier.width(11.dp))
                    Column(Modifier.weight(1f)) {
                        Text("DYNASTY RANK ${dynasty.rank.level}", color = EmpireColors.Violet, fontSize = 10.sp, fontWeight = FontWeight.Black, letterSpacing = 1.3.sp)
                        Text(dynasty.rank.title.uppercase(), color = EmpireColors.TextPrimary, fontSize = 17.sp, fontWeight = FontWeight.Black)
                        Text(
                            if (dynasty.next == null) "APEX DYNASTY • MAXIMUM RANK" else "Next: Rank ${dynasty.next.level} • ${dynasty.next.title}",
                            color = EmpireColors.TextSecondary,
                            fontSize = 9.sp
                        )
                    }
                    Text("${dynasty.rank.level}/${DynastyProgression.MAX_RANK}", color = EmpireColors.Gold, fontSize = 11.sp, fontWeight = FontWeight.Black)
                }
                Spacer(Modifier.height(10.dp))
                LinearProgressIndicator(
                    progress = { dynasty.progress },
                    modifier = Modifier.fillMaxWidth().height(5.dp),
                    color = EmpireColors.Violet,
                    trackColor = EmpireColors.SurfaceHigh
                )
                Spacer(Modifier.height(6.dp))
                Text(
                    "Permanent renown grows through ascensions, eras, purchases, taps and streaks.",
                    color = Color.White.copy(alpha = .48f),
                    fontSize = 9.sp
                )
            }
        }

        FilledTonalButton(
            onClick = { open = true },
            modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp),
            shape = RoundedCornerShape(16.dp),
            contentPadding = PaddingValues(horizontal = 14.dp, vertical = 11.dp)
        ) {
            MetaSprite(MetaSpriteKind.MISSION, 25.dp, active = unclaimed > 0)
            Spacer(Modifier.width(8.dp))
            Column(Modifier.weight(1f)) {
                Text("WEEKLY COMMAND", fontSize = 10.sp, fontWeight = FontWeight.Black)
                Text("$completed/${challenges.size} objectives complete", color = EmpireColors.TextSecondary, fontSize = 9.sp)
            }
            Text(if (unclaimed > 0) "$unclaimed CLAIM" else "OPEN", color = if (unclaimed > 0) EmpireColors.Gold else EmpireColors.Cyan, fontSize = 10.sp, fontWeight = FontWeight.Black)
        }
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
    val orderedChallenges = remember(challenges) {
        challenges.sortedBy { challenge ->
            when {
                challenge.completed && !challenge.claimed -> 0
                !challenge.completed -> 1
                else -> 2
            }
        }
    }

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
            LazyColumn(
                modifier = Modifier.heightIn(max = 440.dp),
                verticalArrangement = Arrangement.spacedBy(9.dp)
            ) {
                items(orderedChallenges, key = { it.id }) { challenge ->
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
                                Spacer(Modifier.width(8.dp))
                                Button(
                                    onClick = { if (onClaim(challenge.id)) haptics.performHapticFeedback(HapticFeedbackType.LongPress) },
                                    enabled = challenge.completed && !challenge.claimed,
                                    contentPadding = PaddingValues(horizontal = 12.dp, vertical = 6.dp),
                                    modifier = Modifier.heightIn(min = 48.dp)
                                ) {
                                    Text(
                                        when {
                                            challenge.claimed -> "DONE"
                                            challenge.completed -> "CLAIM"
                                            else -> "IN PROGRESS"
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
        confirmButton = {
            TextButton(
                onClick = onDismiss,
                modifier = Modifier.heightIn(min = 48.dp)
            ) { Text("CLOSE") }
        }
    )
}
