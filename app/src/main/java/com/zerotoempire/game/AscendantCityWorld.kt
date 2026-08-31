package com.zerotoempire.game

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

/** First playable world-scene implementation from AAA_WORLD_SPRITE_BIBLE.md.
 * Keeps economy/save behavior intact while moving Empire from dashboard-first to world-first.
 */
@Composable
internal fun AscendantCityEmpireWorld(vm: GameViewModel, state: GameState, buyMode: BuyMode) {
    val visible = remember(state.businesses, state.lifetimeCash) { ContentUnlocks.visibleBusinesses(state) }
    val era = EmpireEras.current(state.lifetimeCash)
    LazyColumn(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.spacedBy(10.dp)
    ) {
        item { AscendantCompactHud(state) }
        item {
            Box(Modifier.fillMaxWidth().height(560.dp)) {
                AscendantCityStage(era.index, Modifier.fillMaxSize())
                Column(
                    Modifier.fillMaxSize().padding(horizontal = 12.dp, vertical = 14.dp),
                    verticalArrangement = Arrangement.SpaceBetween
                ) {
                    Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
                        EraChip(era.index + 1, era.name)
                        Surface(color = EmpireColors.DeepSpace.copy(alpha = .86f), shape = RoundedCornerShape(14.dp)) {
                            Text("${visible.size}/14 DISTRICTS", Modifier.padding(horizontal = 10.dp, vertical = 7.dp), color = EmpireColors.Cyan, fontSize = 9.sp, fontWeight = FontWeight.Black)
                        }
                    }
                    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                        visible.take(4).reversed().forEachIndexed { row, business ->
                            AscendantWorldLot(vm, business, state, buyMode, row)
                        }
                        AscendantCorePlaza(state, vm::tap)
                    }
                }
            }
        }
        item { PurchaseModeRailWorld(vm, buyMode) }
        item {
            Text("DISTRICT NETWORK", Modifier.padding(horizontal = 16.dp, vertical = 4.dp), color = EmpireColors.TextSecondary, fontSize = 10.sp, fontWeight = FontWeight.Black, letterSpacing = 1.5.sp)
        }
        visible.drop(4).forEach { business -> item(key = business.id) { AscendantWorldLot(vm, business, state, buyMode, business.id) } }
        item { Spacer(Modifier.height(22.dp)) }
    }
}

@Composable
private fun AscendantCompactHud(state: GameState) {
    Surface(color = EmpireColors.Surface.copy(alpha = .94f), shape = RoundedCornerShape(0.dp)) {
        Row(Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 10.dp), verticalAlignment = Alignment.CenterVertically) {
            Column(Modifier.weight(1f)) {
                Text("CAPITAL", color = EmpireColors.TextSecondary, fontSize = 8.sp, fontWeight = FontWeight.Bold, letterSpacing = 1.2.sp)
                Text(moneyV2(state.cash), color = EmpireColors.TextPrimary, fontSize = 24.sp, fontWeight = FontWeight.Black)
            }
            HudChip("+${moneyV2(state.incomePerSecond)}/s", EmpireColors.Success)
            Spacer(Modifier.width(6.dp))
            HudChip("◆ ${state.gems}", EmpireColors.Violet)
            Spacer(Modifier.width(6.dp))
            HudChip("×${String.format("%.1f", state.boostMultiplier)}", EmpireColors.Gold)
        }
    }
}

@Composable private fun HudChip(text: String, accent: Color) {
    Surface(color = accent.copy(alpha = .11f), shape = RoundedCornerShape(12.dp), modifier = Modifier.border(1.dp, accent.copy(alpha = .25f), RoundedCornerShape(12.dp))) {
        Text(text, Modifier.padding(horizontal = 8.dp, vertical = 7.dp), color = accent, fontSize = 10.sp, fontWeight = FontWeight.Black)
    }
}

@Composable private fun EraChip(number: Int, name: String) {
    Surface(color = EmpireColors.DeepSpace.copy(alpha = .88f), shape = RoundedCornerShape(15.dp), modifier = Modifier.border(1.dp, EmpireColors.Gold.copy(alpha = .25f), RoundedCornerShape(15.dp))) {
        Column(Modifier.padding(horizontal = 11.dp, vertical = 7.dp)) {
            Text("ERA $number", color = EmpireColors.Gold, fontSize = 8.sp, fontWeight = FontWeight.Black, letterSpacing = 1.2.sp)
            Text(name.uppercase(), color = EmpireColors.TextPrimary, fontSize = 11.sp, fontWeight = FontWeight.Black)
        }
    }
}

@Composable
private fun AscendantCityStage(eraIndex: Int, modifier: Modifier = Modifier) {
    Box(modifier.background(Brush.verticalGradient(listOf(Color(0xFF07101C), Color(0xFF101B24), Color(0xFF080D13))))) {
        EraVistaAAA(eraIndex, Modifier.fillMaxSize())
        Canvas(Modifier.fillMaxSize()) {
            val w = size.width; val h = size.height
            // Ground plane: original diagonal industrial district geometry.
            val ground = Path().apply { moveTo(0f, h * .31f); lineTo(w, h * .18f); lineTo(w, h); lineTo(0f, h); close() }
            drawPath(ground, Color(0xD9141B20))
            // Main cargo avenue.
            val road = Path().apply { moveTo(w * .36f, h * .31f); lineTo(w * .57f, h * .27f); lineTo(w * .88f, h); lineTo(w * .18f, h); close() }
            drawPath(road, Color(0xFF1B2227))
            drawLine(EmpireColors.Gold.copy(alpha=.35f), Offset(w*.47f,h*.32f), Offset(w*.53f,h*.96f), 3f)
            // Energy conduits connect the city to the core plaza.
            repeat(4) { i ->
                val y = h * (.48f + i * .105f)
                drawLine(EmpireColors.Cyan.copy(alpha=.18f), Offset(w*.12f,y), Offset(w*.50f,h*.91f), 2f)
                drawLine(EmpireColors.Cyan.copy(alpha=.13f), Offset(w*.88f,y-.035f*h), Offset(w*.50f,h*.91f), 2f)
            }
            // Lot pads create depth without turning back into UI cards.
            repeat(4) { i ->
                val y = h * (.44f + i*.105f)
                val left = i % 2 == 0
                val x = if(left) w*.055f else w*.63f
                drawRoundRect(Color(0xCC20282C), Offset(x,y), Size(w*.31f,h*.075f), cornerRadius=androidx.compose.ui.geometry.CornerRadius(14f,14f))
                drawRoundRect(EmpireColors.Cyan.copy(alpha=.13f), Offset(x,y), Size(w*.31f,h*.075f), cornerRadius=androidx.compose.ui.geometry.CornerRadius(14f,14f), style=Stroke(2f))
            }
        }
        Box(Modifier.fillMaxSize().background(Brush.verticalGradient(listOf(Color.Transparent, Color.Transparent, EmpireColors.Void.copy(alpha=.28f)))))
    }
}

@Composable
private fun AscendantWorldLot(vm: GameViewModel, business: Business, state: GameState, mode: BuyMode, row: Int) {
    val quote = vm.bulkQuote(business.id, mode)
    val affordable = quote.count > 0 && state.cash >= quote.cost
    val income = state.businessIncome(business) * state.permanentIncomeMultiplier * state.boostMultiplier * state.eventMultiplier
    val alignRight = row % 2 != 0
    Row(
        Modifier.fillMaxWidth().padding(horizontal = if (row < 4) 2.dp else 14.dp),
        horizontalArrangement = if (alignRight) Arrangement.End else Arrangement.Start,
        verticalAlignment = Alignment.CenterVertically
    ) {
        Surface(
            color = EmpireColors.Surface.copy(alpha = if (row < 4) .88f else .96f),
            shape = RoundedCornerShape(18.dp),
            modifier = Modifier.fillMaxWidth(if (row < 4) .72f else .96f)
                .border(1.dp, if (affordable) EmpireColors.Gold.copy(alpha=.38f) else Color.White.copy(alpha=.07f), RoundedCornerShape(18.dp))
                .clickable(enabled = affordable, role = Role.Button) { vm.buyBulk(business.id, mode) }
        ) {
            Row(Modifier.padding(horizontal = 10.dp, vertical = 9.dp), verticalAlignment = Alignment.CenterVertically) {
                Box(Modifier.size(if (row < 4) 54.dp else 64.dp), contentAlignment = Alignment.Center) { BusinessArtIcon(business.id, business.level, if (row < 4) 52.dp else 62.dp) }
                Spacer(Modifier.width(9.dp))
                Column(Modifier.weight(1f)) {
                    Text(business.name, color = EmpireColors.TextPrimary, fontSize = if(row<4) 12.sp else 15.sp, fontWeight = FontWeight.Black, maxLines=1, overflow=TextOverflow.Ellipsis)
                    Text("LV ${business.level}  •  ${moneyV2(income)}/s", color = EmpireColors.Cyan, fontSize = 9.sp, fontWeight = FontWeight.Bold)
                }
                Column(horizontalAlignment = Alignment.End) {
                    Text(if (quote.count > 0) "+${quote.count}" else "—", color = if(affordable) EmpireColors.GoldBright else EmpireColors.TextSecondary, fontSize = 11.sp, fontWeight = FontWeight.Black)
                    Text(if (quote.count > 0) moneyV2(quote.cost) else "LOCKED", color = EmpireColors.TextSecondary, fontSize = 8.sp, fontWeight = FontWeight.Bold)
                }
            }
        }
    }
}

@Composable
private fun AscendantCorePlaza(state: GameState, tap: () -> Unit) {
    Box(Modifier.fillMaxWidth().height(122.dp), contentAlignment = Alignment.Center) {
        Box(Modifier.size(112.dp).background(Brush.radialGradient(listOf(EmpireColors.Gold.copy(alpha=.20f), EmpireColors.Cyan.copy(alpha=.08f), Color.Transparent)), CircleShape))
        Surface(
            color = EmpireColors.DeepSpace.copy(alpha=.88f),
            shape = CircleShape,
            modifier = Modifier.size(96.dp).border(2.dp, EmpireColors.Gold.copy(alpha=.48f), CircleShape).clickable(role=Role.Button) { tap() }
        ) { Box(contentAlignment = Alignment.Center) { EmpireCoreGlyph(Modifier.size(84.dp), EmpireEras.current(state.lifetimeCash).index) } }
        Surface(color=EmpireColors.DeepSpace.copy(alpha=.90f), shape=RoundedCornerShape(10.dp), modifier=Modifier.align(Alignment.BottomCenter)) {
            Text("POWER CORE  +${moneyV2(state.tapValue)}", Modifier.padding(horizontal=9.dp,vertical=5.dp), color=EmpireColors.GoldBright, fontSize=9.sp, fontWeight=FontWeight.Black)
        }
    }
}

@Composable
private fun PurchaseModeRailWorld(vm: GameViewModel, selected: BuyMode) {
    val modes = listOf(BuyMode.X1 to "×1", BuyMode.X10 to "×10", BuyMode.X25 to "×25", BuyMode.MILESTONE to "NEXT", BuyMode.MAX to "MAX")
    Row(Modifier.fillMaxWidth().padding(horizontal=14.dp), horizontalArrangement=Arrangement.spacedBy(5.dp)) {
        modes.forEach { (mode,label) ->
            val active = mode == selected
            Surface(color=if(active) EmpireColors.Violet else EmpireColors.Surface, shape=RoundedCornerShape(12.dp), modifier=Modifier.weight(1f).height(42.dp).clickable { vm.setBuyMode(mode) }) {
                Box(contentAlignment=Alignment.Center) { Text(label, color=if(active) Color.White else EmpireColors.TextSecondary, fontSize=9.sp, fontWeight=FontWeight.Black) }
            }
        }
    }
}
