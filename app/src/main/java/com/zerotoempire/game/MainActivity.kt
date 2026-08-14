package com.zerotoempire.game

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
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

private val Navy = Color(0xFF08111F)
private val Panel = Color(0xFF111E31)
private val Gold = Color(0xFFFFC857)
private val Cyan = Color(0xFF45E0E8)

@Composable
fun ZeroToEmpireApp(vm: GameViewModel = viewModel()) {
    val state by vm.state.collectAsStateWithLifecycle()
    MaterialTheme(colorScheme = darkColorScheme(primary = Gold, secondary = Cyan, background = Navy, surface = Panel)) {
        Scaffold(containerColor = Navy) { padding ->
            Column(
                modifier = Modifier
                    .padding(padding)
                    .fillMaxSize()
                    .background(Brush.verticalGradient(listOf(Color(0xFF08111F), Color(0xFF102A43))))
                    .padding(horizontal = 16.dp)
            ) {
                Spacer(Modifier.height(14.dp))
                Text("ZERO → EMPIRE", color = Gold, fontWeight = FontWeight.Black, fontSize = 24.sp)
                Text("BUILD. AUTOMATE. DOMINATE.", color = Color.White.copy(alpha = .55f), fontSize = 11.sp)
                Spacer(Modifier.height(18.dp))
                Text(formatMoney(state.cash), color = Color.White, fontWeight = FontWeight.Black, fontSize = 38.sp)
                Text("+${formatMoney(state.incomePerSecond)} / sec", color = Cyan, fontWeight = FontWeight.Bold)
                Spacer(Modifier.height(16.dp))

                Surface(
                    modifier = Modifier.fillMaxWidth().clickable { vm.tap() },
                    color = Gold,
                    shape = RoundedCornerShape(22.dp),
                    shadowElevation = 10.dp
                ) {
                    Column(Modifier.padding(22.dp), horizontalAlignment = Alignment.CenterHorizontally) {
                        Text("💰", fontSize = 42.sp)
                        Text("TAP TO HUSTLE", color = Navy, fontWeight = FontWeight.Black, fontSize = 18.sp)
                        Text("Every tap grows your empire", color = Navy.copy(alpha = .7f), fontSize = 12.sp)
                    }
                }

                Spacer(Modifier.height(20.dp))
                Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
                    Text("YOUR EMPIRE", color = Color.White, fontWeight = FontWeight.ExtraBold)
                    Text("PRESTIGE ×${String.format(Locale.US, "%.1f", state.prestigeMultiplier)}", color = Gold, fontSize = 12.sp)
                }
                Spacer(Modifier.height(8.dp))
                LazyColumn(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                    items(state.businesses) { business ->
                        BusinessCard(business, state.cash >= business.nextCost) { vm.buy(business.id) }
                    }
                    item {
                        Spacer(Modifier.height(8.dp))
                        Button(onClick = vm::prestige, modifier = Modifier.fillMaxWidth(), shape = RoundedCornerShape(16.dp)) {
                            Text("ASCEND — RESET FOR PERMANENT POWER", textAlign = TextAlign.Center, fontWeight = FontWeight.Bold)
                        }
                        Spacer(Modifier.height(24.dp))
                    }
                }
            }
        }
    }
}

@Composable
private fun BusinessCard(b: Business, affordable: Boolean, onBuy: () -> Unit) {
    Surface(color = Panel, shape = RoundedCornerShape(16.dp), modifier = Modifier.fillMaxWidth().clickable(enabled = affordable, onClick = onBuy)) {
        Row(Modifier.padding(14.dp), verticalAlignment = Alignment.CenterVertically) {
            Text(b.emoji, fontSize = 32.sp)
            Spacer(Modifier.width(12.dp))
            Column(Modifier.weight(1f)) {
                Text(b.name, color = Color.White, fontWeight = FontWeight.Bold)
                Text("Lv. ${b.level}  •  ${formatMoney(b.incomePerSecond)}/s", color = Cyan, fontSize = 12.sp)
            }
            Column(horizontalAlignment = Alignment.End) {
                Text(formatMoney(b.nextCost), color = if (affordable) Gold else Color.Gray, fontWeight = FontWeight.Bold)
                Text("BUY", color = if (affordable) Color.White else Color.Gray, fontSize = 11.sp)
            }
        }
    }
}

private fun formatMoney(value: Double): String {
    val v = abs(value)
    val units = listOf(1e15 to "Q", 1e12 to "T", 1e9 to "B", 1e6 to "M", 1e3 to "K")
    val unit = units.firstOrNull { v >= it.first }
    return if (unit != null) "$${String.format(Locale.US, "%.2f", value / unit.first)}${unit.second}"
    else "$${String.format(Locale.US, "%.0f", value)}"
}
