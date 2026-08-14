package com.zerotoempire.game

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import java.util.Locale
import kotlin.math.abs

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { ZeroToEmpireApp() }
    }
}

@Composable
fun ZeroToEmpireApp(vm: GameViewModel = viewModel()) {
    val state by vm.state.collectAsStateWithLifecycle()
    MaterialTheme(colorScheme = EmpireColorScheme) {
        Scaffold(containerColor = EmpireColors.Void) { inset ->
            LazyColumn(
                modifier = Modifier
                    .padding(inset)
                    .fillMaxSize()
                    .background(Brush.verticalGradient(listOf(EmpireColors.Void, EmpireColors.DeepSpace)))
                    .padding(horizontal = 16.dp),
                verticalArrangement = Arrangement.spacedBy(10.dp),
                contentPadding = PaddingValues(bottom = 30.dp)
            ) {
                item { Header(state) }
                item { WealthHero(state) }
                item { PowerTap(state, vm::tap) }
                item { EmpireSectionHeader(state) }
                items(state.businesses) { b -> BusinessCard(b, state.cash >= b.nextCost) { vm.buy(b.id) } }
                item { PrestigeCard(state, vm::prestige) }
            }
        }
    }
}

@Composable
private fun Header(state: GameState) {
    Row(Modifier.fillMaxWidth().padding(top = 18.dp, bottom = 4.dp), verticalAlignment = Alignment.CenterVertically) {
        Column(Modifier.weight(1f)) {
            Text("ZERO → EMPIRE", color = EmpireColors.Gold, fontWeight = FontWeight.Black, fontSize = 23.sp)
            Text("FROM NOTHING. BEYOND EVERYTHING.", color = EmpireColors.TextSecondary, fontSize = 10.sp, letterSpacing = 1.sp)
        }
        Surface(shape = RoundedCornerShape(50), color = EmpireColors.SurfaceHigh) {
            Text("◆ ${state.prestigePoints}", modifier = Modifier.padding(horizontal = 12.dp, vertical = 7.dp), color = EmpireColors.Violet, fontWeight = FontWeight.Bold)
        }
    }
}

@Composable
private fun WealthHero(state: GameState) {
    Surface(shape = RoundedCornerShape(24.dp), color = Color.Transparent, modifier = Modifier.fillMaxWidth()) {
        Box(Modifier.background(Brush.horizontalGradient(listOf(EmpireColors.SurfaceHigh, EmpireColors.Surface))).padding(20.dp)) {
            Column {
                Text("NET WORTH", color = EmpireColors.TextSecondary, fontSize = 11.sp, fontWeight = FontWeight.Bold)
                Text(formatMoney(state.cash), color = EmpireColors.TextPrimary, fontSize = 40.sp, fontWeight = FontWeight.Black)
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Text("▲ ${formatMoney(state.incomePerSecond)} / SEC", color = EmpireColors.Success, fontWeight = FontWeight.ExtraBold, fontSize = 13.sp)
                    Spacer(Modifier.width(10.dp))
                    Text("×${String.format(Locale.US, "%.1f", state.prestigeMultiplier)} LEGACY", color = EmpireColors.Gold, fontSize = 11.sp)
                }
            }
        }
    }
}

@Composable
private fun PowerTap(state: GameState, onTap: () -> Unit) {
    var pressed by remember { mutableStateOf(false) }
    val scale by animateFloatAsState(if (pressed) .94f else 1f, label = "tapScale")
    val interaction = remember { MutableInteractionSource() }
    Box(Modifier.fillMaxWidth().padding(vertical = 6.dp), contentAlignment = Alignment.Center) {
        Surface(
            modifier = Modifier.size(190.dp).scale(scale).clickable(interactionSource = interaction, indication = null) {
                pressed = true
                onTap()
                pressed = false
            },
            shape = CircleShape,
            shadowElevation = 18.dp,
            color = EmpireColors.Gold
        ) {
            Box(Modifier.background(Brush.radialGradient(listOf(EmpireColors.GoldBright, EmpireColors.Gold))), contentAlignment = Alignment.Center) {
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text("$", color = EmpireColors.Void, fontWeight = FontWeight.Black, fontSize = 56.sp)
                    Text("POWER TAP", color = EmpireColors.Void, fontWeight = FontWeight.Black, fontSize = 15.sp)
                    Text("+${formatMoney((1.0 + state.incomePerSecond * .05) * state.prestigeMultiplier)}", color = EmpireColors.Void.copy(alpha = .68f), fontWeight = FontWeight.Bold)
                }
            }
        }
    }
}

@Composable
private fun EmpireSectionHeader(state: GameState) {
    Row(Modifier.fillMaxWidth().padding(top = 8.dp), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.Bottom) {
        Column {
            Text("YOUR EMPIRE", color = EmpireColors.TextPrimary, fontWeight = FontWeight.Black, fontSize = 19.sp)
            Text("${state.businesses.sumOf { it.level }} total assets", color = EmpireColors.TextSecondary, fontSize = 11.sp)
        }
        Text("BUY & SCALE", color = EmpireColors.Cyan, fontSize = 11.sp, fontWeight = FontWeight.Bold)
    }
}

@Composable
private fun BusinessCard(b: Business, affordable: Boolean, onBuy: () -> Unit) {
    val milestone = when {
        b.level < 10 -> 10
        b.level < 25 -> 25
        b.level < 50 -> 50
        b.level < 100 -> 100
        else -> ((b.level / 100) + 1) * 100
    }
    val progress = (b.level.toFloat() / milestone).coerceIn(0f, 1f)
    Surface(
        color = EmpireColors.Surface,
        shape = RoundedCornerShape(19.dp),
        modifier = Modifier.fillMaxWidth().clickable(enabled = affordable, onClick = onBuy),
        tonalElevation = if (affordable) 3.dp else 0.dp
    ) {
        Column(Modifier.padding(14.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Surface(shape = RoundedCornerShape(14.dp), color = EmpireColors.SurfaceHigh) {
                    Text(b.emoji, modifier = Modifier.padding(11.dp), fontSize = 28.sp)
                }
                Spacer(Modifier.width(12.dp))
                Column(Modifier.weight(1f)) {
                    Text(b.name, color = EmpireColors.TextPrimary, fontWeight = FontWeight.ExtraBold, fontSize = 16.sp)
                    Text("LEVEL ${b.level}  •  ${formatMoney(b.incomePerSecond)}/s", color = EmpireColors.Cyan, fontSize = 11.sp, fontWeight = FontWeight.Bold)
                }
                Surface(shape = RoundedCornerShape(12.dp), color = if (affordable) EmpireColors.Gold else EmpireColors.SurfaceHigh) {
                    Column(Modifier.padding(horizontal = 12.dp, vertical = 8.dp), horizontalAlignment = Alignment.CenterHorizontally) {
                        Text("BUY", color = if (affordable) EmpireColors.Void else EmpireColors.TextSecondary, fontWeight = FontWeight.Black, fontSize = 10.sp)
                        Text(formatMoney(b.nextCost), color = if (affordable) EmpireColors.Void else EmpireColors.TextSecondary, fontWeight = FontWeight.Bold, fontSize = 11.sp)
                    }
                }
            }
            Spacer(Modifier.height(10.dp))
            LinearProgressIndicator(progress = { progress }, modifier = Modifier.fillMaxWidth().height(4.dp), color = EmpireColors.Gold, trackColor = EmpireColors.SurfaceHigh)
            Spacer(Modifier.height(5.dp))
            Text("NEXT MILESTONE • LV $milestone", color = EmpireColors.TextSecondary, fontSize = 9.sp)
        }
    }
}

@Composable
private fun PrestigeCard(state: GameState, onPrestige: () -> Unit) {
    Surface(shape = RoundedCornerShape(22.dp), color = EmpireColors.SurfaceHigh, modifier = Modifier.fillMaxWidth().padding(top = 8.dp)) {
        Column(Modifier.padding(20.dp), horizontalAlignment = Alignment.CenterHorizontally) {
            Text("ASCENSION", color = EmpireColors.Violet, fontWeight = FontWeight.Black, fontSize = 20.sp)
            Text("Reset your current empire. Keep permanent power and rebuild exponentially faster.", color = EmpireColors.TextSecondary, textAlign = TextAlign.Center, fontSize = 12.sp)
            Spacer(Modifier.height(12.dp))
            Button(onClick = onPrestige, modifier = Modifier.fillMaxWidth(), shape = RoundedCornerShape(14.dp)) {
                Text("TRANSCEND THE EMPIRE", fontWeight = FontWeight.Black)
            }
        }
    }
}

private fun formatMoney(value: Double): String {
    val v = abs(value)
    val units = listOf(1e18 to "Qi", 1e15 to "Q", 1e12 to "T", 1e9 to "B", 1e6 to "M", 1e3 to "K")
    val unit = units.firstOrNull { v >= it.first }
    return if (unit != null) "$${String.format(Locale.US, "%.2f", value / unit.first)}${unit.second}" else "$${String.format(Locale.US, "%.0f", value)}"
}
