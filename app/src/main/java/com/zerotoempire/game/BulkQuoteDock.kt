package com.zerotoempire.game

import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import java.util.Locale
import kotlin.math.abs

@Composable
fun BulkQuoteDock(vm: GameViewModel) {
    val state by vm.state.collectAsStateWithLifecycle()
    val mode by vm.buyMode.collectAsStateWithLifecycle()
    val candidates = state.businesses.mapNotNull { business ->
        val quote = vm.bulkQuote(business.id, mode)
        if (!quote.valid) null else Triple(business, quote, quote.totalCost <= state.cash)
    }
    if (candidates.isEmpty()) return

    Surface(
        color = EmpireColors.Void.copy(alpha = .93f),
        shape = RoundedCornerShape(18.dp),
        shadowElevation = 12.dp,
        modifier = Modifier.fillMaxWidth().padding(horizontal = 12.dp)
    ) {
        Column(Modifier.padding(10.dp)) {
            val label = when (mode) {
                BuyMode.X1 -> "×1"
                BuyMode.X10 -> "×10"
                BuyMode.X25 -> "×25"
                BuyMode.MAX -> "MAX"
            }
            Text("BULK PURCHASE • $label", color = EmpireColors.Gold, fontWeight = FontWeight.Black, fontSize = 10.sp)
            Spacer(Modifier.height(7.dp))
            Row(
                Modifier.horizontalScroll(rememberScrollState()),
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                candidates.forEach { (business, quote, affordable) ->
                    Button(
                        onClick = { vm.buyBulk(business.id, mode) },
                        enabled = affordable,
                        shape = RoundedCornerShape(14.dp)
                    ) {
                        Column {
                            Text(business.name, fontWeight = FontWeight.Black, fontSize = 10.sp)
                            Text("+${quote.count} LV • ${compactMoney(quote.totalCost)}", fontSize = 9.sp)
                        }
                    }
                }
            }
        }
    }
}

private fun compactMoney(value: Double): String {
    val v = abs(value)
    val units = listOf(1e18 to "Qi", 1e15 to "Q", 1e12 to "T", 1e9 to "B", 1e6 to "M", 1e3 to "K")
    val u = units.firstOrNull { v >= it.first }
    return if (u != null) "$${String.format(Locale.US, "%.2f", value / u.first)}${u.second}"
    else "$${String.format(Locale.US, "%.0f", value)}"
}
