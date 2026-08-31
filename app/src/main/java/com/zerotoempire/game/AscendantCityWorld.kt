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

/** World-first Empire surface defined by AAA_WORLD_SPRITE_BIBLE.md.
 * Economy and save behavior remain delegated to the existing GameViewModel.
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
            Box(Modifier.fillMaxWidth().height(620.dp)) {
                AscendantCityStage(era.index, Modifier.fillMaxSize())

                Row(
                    Modifier.fillMaxWidth().padding(horizontal = 12.dp, vertical = 14.dp),
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {
                    EraChip(era.index + 1, era.name)
                    Surface(color = EmpireColors.DeepSpace.copy(alpha = .82f), shape = RoundedCornerShape(14.dp)) {
                        Text(
                            "${visible.size}/14 DISTRICTS",
                            Modifier.padding(horizontal = 10.dp, vertical = 7.dp),
                            color = EmpireColors.Cyan,
                            fontSize = 9.sp,
                            fontWeight = FontWeight.Black
                        )
                    }
                }

                visible.take(4).getOrNull(0)?.let {
                    AscendantHeroLot(vm, it, state, buyMode, Modifier.align(Alignment.TopStart).padding(start = 14.dp, top = 142.dp), false)
                }
                visible.take(4).getOrNull(1)?.let {
                    AscendantHeroLot(vm, it, state, buyMode, Modifier.align(Alignment.TopEnd).padding(end = 14.dp, top = 238.dp), true)
                }
                visible.take(4).getOrNull(2)?.let {
                    AscendantHeroLot(vm, it, state, buyMode, Modifier.align(Alignment.TopStart).padding(start = 14.dp, top = 334.dp), false)
                }
                visible.take(4).getOrNull(3)?.let {
                    AscendantHeroLot(vm, it, state, buyMode, Modifier.align(Alignment.TopEnd).padding(end = 14.dp, top = 430.dp), true)
                }

                AscendantCorePlaza(
                    state = state,
                    tap = vm::tap,
                    modifier = Modifier.align(Alignment.BottomCenter).padding(bottom = 12.dp)
                )
            }
        }
        item { PurchaseModeRailWorld(vm, buyMode) }
        item {
            Text(
                "DISTRICT NETWORK",
                Modifier.padding(horizontal = 16.dp, vertical = 4.dp),
                color = EmpireColors.TextSecondary,
                fontSize = 10.sp,
                fontWeight = FontWeight.Black,
                letterSpacing = 1.5.sp
            )
        }
        visible.drop(4).forEach { business ->
            item(key = business.id) { AscendantWorldLot(vm, business, state, buyMode, business.id) }
        }
        item { Spacer(Modifier.height(22.dp)) }
    }
}

@Composable
private fun AscendantCompactHud(state: GameState) {
    Surface(color = EmpireColors.Surface.copy(alpha = .94f), shape = RoundedCornerShape(0.dp)) {
        Row(
            Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 10.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
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

@Composable
private fun HudChip(text: String, accent: Color) {
    Surface(
        color = accent.copy(alpha = .11f),
        shape = RoundedCornerShape(12.dp),
        modifier = Modifier.border(1.dp, accent.copy(alpha = .25f), RoundedCornerShape(12.dp))
    ) {
        Text(text, Modifier.padding(horizontal = 8.dp, vertical = 7.dp), color = accent, fontSize = 10.sp, fontWeight = FontWeight.Black)
    }
}

@Composable
private fun EraChip(number: Int, name: String) {
    Surface(
        color = EmpireColors.DeepSpace.copy(alpha = .88f),
        shape = RoundedCornerShape(15.dp),
        modifier = Modifier.border(1.dp, EmpireColors.Gold.copy(alpha = .25f), RoundedCornerShape(15.dp))
    ) {
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
            val w = size.width
            val h = size.height

            // Distant industrial silhouette: several depth bands, deliberately static.
            repeat(7) { i ->
                val bw = w * (.065f + (i % 3) * .018f)
                val bh = h * (.07f + (i % 4) * .024f)
                val x = w * (.03f + i * .145f)
                val y = h * .31f - bh
                drawRect(Color(0xB510171D), Offset(x, y), Size(bw, bh))
                drawRect(EmpireColors.Gold.copy(alpha = .12f), Offset(x + bw * .18f, y + bh * .28f), Size(bw * .12f, 3f))
                drawRect(EmpireColors.Cyan.copy(alpha = .10f), Offset(x + bw * .54f, y + bh * .48f), Size(bw * .16f, 3f))
            }

            // Ground plane and retaining wall establish the 2.5D city slab.
            val ground = Path().apply {
                moveTo(0f, h * .30f)
                lineTo(w, h * .17f)
                lineTo(w, h)
                lineTo(0f, h)
                close()
            }
            drawPath(ground, Color(0xE5141B20))
            drawLine(Color.White.copy(alpha = .06f), Offset(0f, h * .30f), Offset(w, h * .17f), 2f)

            // Main cargo avenue, shoulder strips and centre power spine.
            val road = Path().apply {
                moveTo(w * .36f, h * .30f)
                lineTo(w * .57f, h * .26f)
                lineTo(w * .88f, h)
                lineTo(w * .18f, h)
                close()
            }
            drawPath(road, Color(0xFF1B2227))
            drawLine(Color.White.copy(alpha = .05f), Offset(w * .37f, h * .31f), Offset(w * .20f, h), 2f)
            drawLine(Color.White.copy(alpha = .05f), Offset(w * .56f, h * .28f), Offset(w * .86f, h), 2f)
            drawLine(EmpireColors.Gold.copy(alpha = .34f), Offset(w * .47f, h * .31f), Offset(w * .53f, h * .95f), 3f)

            // Energy conduits and industrial pipework visually connect production lots.
            repeat(4) { i ->
                val y = h * (.42f + i * .145f)
                drawLine(EmpireColors.Cyan.copy(alpha = .20f), Offset(w * .10f, y), Offset(w * .50f, h * .91f), 2f)
                drawLine(EmpireColors.Cyan.copy(alpha = .15f), Offset(w * .90f, y - h * .025f), Offset(w * .50f, h * .91f), 2f)
            }
            repeat(3) { i ->
                val y = h * (.39f + i * .19f)
                drawLine(Color(0xFF6F5B3C).copy(alpha = .24f), Offset(0f, y), Offset(w * .22f, y - h * .025f), 5f)
                drawCircle(EmpireColors.Gold.copy(alpha = .18f), 6f, Offset(w * .22f, y - h * .025f))
            }

            // Four physical lot foundations. These are scenery, not UI cards.
            repeat(4) { i ->
                val y = h * (.34f + i * .155f)
                val left = i % 2 == 0
                val x = if (left) w * .035f else w * .595f
                val pad = Path().apply {
                    moveTo(x, y + h * .035f)
                    lineTo(x + w * .25f, y)
                    lineTo(x + w * .39f, y + h * .045f)
                    lineTo(x + w * .13f, y + h * .083f)
                    close()
                }
                drawPath(pad, Color(0xE5263034))
                drawPath(pad, EmpireColors.Cyan.copy(alpha = .12f), style = Stroke(2f))
                drawLine(EmpireColors.Gold.copy(alpha = .18f), Offset(x + w * .06f, y + h * .056f), Offset(x + w * .31f, y + h * .02f), 3f)
            }

            // Foreground occluders add depth and make the city read as a place.
            drawRect(Color(0xFF0E151A), Offset(0f, h * .90f), Size(w * .16f, h * .10f))
            drawRect(Color(0xFF0E151A), Offset(w * .86f, h * .88f), Size(w * .14f, h * .12f))
        }
        Box(
            Modifier.fillMaxSize().background(
                Brush.verticalGradient(listOf(Color.Transparent, Color.Transparent, EmpireColors.Void.copy(alpha = .24f)))
            )
        )
    }
}

@Composable
private fun AscendantHeroLot(
    vm: GameViewModel,
    business: Business,
    state: GameState,
    mode: BuyMode,
    modifier: Modifier,
    alignRight: Boolean
) {
    val quote = vm.bulkQuote(business.id, mode)
    val affordable = quote.count > 0 && state.cash >= quote.cost
    val income = state.businessIncome(business) * state.permanentIncomeMultiplier * state.boostMultiplier * state.eventMultiplier
    val accent = if (affordable) EmpireColors.Gold else EmpireColors.Cyan

    Column(
        modifier.width(178.dp).clickable(enabled = affordable, role = Role.Button) { vm.buyBulk(business.id, mode) },
        horizontalAlignment = if (alignRight) Alignment.End else Alignment.Start
    ) {
        Box(Modifier.fillMaxWidth().height(92.dp), contentAlignment = if (alignRight) Alignment.CenterEnd else Alignment.CenterStart) {
            Canvas(Modifier.fillMaxSize()) {
                val baseY = size.height * .76f
                val left = if (alignRight) size.width * .18f else 0f
                drawOval(Color.Black.copy(alpha = .34f), Offset(left, baseY), Size(size.width * .76f, size.height * .18f))
                drawLine(accent.copy(alpha = .22f), Offset(left + 8f, baseY + 8f), Offset(left + size.width * .65f, baseY + 2f), 3f)
            }
            BusinessArtIcon(business.id, business.level, 88.dp)
        }
        Surface(
            color = EmpireColors.DeepSpace.copy(alpha = .84f),
            shape = RoundedCornerShape(12.dp),
            modifier = Modifier.border(1.dp, accent.copy(alpha = .28f), RoundedCornerShape(12.dp))
        ) {
            Row(Modifier.padding(horizontal = 8.dp, vertical = 6.dp), verticalAlignment = Alignment.CenterVertically) {
                Column(Modifier.weight(1f)) {
                    Text(business.name, color = EmpireColors.TextPrimary, fontSize = 10.sp, fontWeight = FontWeight.Black, maxLines = 1, overflow = TextOverflow.Ellipsis)
                    Text("LV ${business.level} • ${moneyV2(income)}/s", color = EmpireColors.Cyan, fontSize = 8.sp, fontWeight = FontWeight.Bold)
                }
                Spacer(Modifier.width(5.dp))
                Column(horizontalAlignment = Alignment.End) {
                    Text(if (quote.count > 0) "+${quote.count}" else "—", color = if (affordable) EmpireColors.GoldBright else EmpireColors.TextSecondary, fontSize = 9.sp, fontWeight = FontWeight.Black)
                    Text(if (quote.count > 0) moneyV2(quote.cost) else "LOCKED", color = EmpireColors.TextSecondary, fontSize = 7.sp, fontWeight = FontWeight.Bold)
                }
            }
        }
    }
}

@Composable
private fun AscendantWorldLot(vm: GameViewModel, business: Business, state: GameState, mode: BuyMode, row: Int) {
    val quote = vm.bulkQuote(business.id, mode)
    val affordable = quote.count > 0 && state.cash >= quote.cost
    val income = state.businessIncome(business) * state.permanentIncomeMultiplier * state.boostMultiplier * state.eventMultiplier
    val alignRight = row % 2 != 0
    Row(
        Modifier.fillMaxWidth().padding(horizontal = 14.dp),
        horizontalArrangement = if (alignRight) Arrangement.End else Arrangement.Start,
        verticalAlignment = Alignment.CenterVertically
    ) {
        Surface(
            color = EmpireColors.Surface.copy(alpha = .94f),
            shape = RoundedCornerShape(18.dp),
            modifier = Modifier.fillMaxWidth(.96f)
                .border(1.dp, if (affordable) EmpireColors.Gold.copy(alpha = .38f) else Color.White.copy(alpha = .07f), RoundedCornerShape(18.dp))
                .clickable(enabled = affordable, role = Role.Button) { vm.buyBulk(business.id, mode) }
        ) {
            Row(Modifier.padding(horizontal = 10.dp, vertical = 9.dp), verticalAlignment = Alignment.CenterVertically) {
                Box(Modifier.size(68.dp), contentAlignment = Alignment.Center) { BusinessArtIcon(business.id, business.level, 66.dp) }
                Spacer(Modifier.width(9.dp))
                Column(Modifier.weight(1f)) {
                    Text(business.name, color = EmpireColors.TextPrimary, fontSize = 15.sp, fontWeight = FontWeight.Black, maxLines = 1, overflow = TextOverflow.Ellipsis)
                    Text("LV ${business.level} • ${moneyV2(income)}/s", color = EmpireColors.Cyan, fontSize = 9.sp, fontWeight = FontWeight.Bold)
                }
                Column(horizontalAlignment = Alignment.End) {
                    Text(if (quote.count > 0) "+${quote.count}" else "—", color = if (affordable) EmpireColors.GoldBright else EmpireColors.TextSecondary, fontSize = 11.sp, fontWeight = FontWeight.Black)
                    Text(if (quote.count > 0) moneyV2(quote.cost) else "LOCKED", color = EmpireColors.TextSecondary, fontSize = 8.sp, fontWeight = FontWeight.Bold)
                }
            }
        }
    }
}

@Composable
private fun AscendantCorePlaza(state: GameState, tap: () -> Unit, modifier: Modifier = Modifier) {
    Box(modifier.fillMaxWidth().height(118.dp), contentAlignment = Alignment.Center) {
        Box(
            Modifier.size(118.dp).background(
                Brush.radialGradient(listOf(EmpireColors.Gold.copy(alpha = .22f), EmpireColors.Cyan.copy(alpha = .08f), Color.Transparent)),
                CircleShape
            )
        )
        Surface(
            color = EmpireColors.DeepSpace.copy(alpha = .86f),
            shape = CircleShape,
            modifier = Modifier.size(98.dp)
                .border(2.dp, EmpireColors.Gold.copy(alpha = .48f), CircleShape)
                .clickable(role = Role.Button) { tap() }
        ) {
            Box(contentAlignment = Alignment.Center) {
                EmpireCoreGlyph(Modifier.size(86.dp), EmpireEras.current(state.lifetimeCash).index)
            }
        }
        Surface(
            color = EmpireColors.DeepSpace.copy(alpha = .90f),
            shape = RoundedCornerShape(10.dp),
            modifier = Modifier.align(Alignment.BottomCenter)
        ) {
            Text(
                "POWER CORE  +${moneyV2(state.tapValue)}",
                Modifier.padding(horizontal = 9.dp, vertical = 5.dp),
                color = EmpireColors.GoldBright,
                fontSize = 9.sp,
                fontWeight = FontWeight.Black
            )
        }
    }
}

@Composable
private fun PurchaseModeRailWorld(vm: GameViewModel, selected: BuyMode) {
    val modes = listOf(BuyMode.X1 to "×1", BuyMode.X10 to "×10", BuyMode.X25 to "×25", BuyMode.MILESTONE to "NEXT", BuyMode.MAX to "MAX")
    Row(Modifier.fillMaxWidth().padding(horizontal = 14.dp), horizontalArrangement = Arrangement.spacedBy(5.dp)) {
        modes.forEach { (mode, label) ->
            val active = mode == selected
            Surface(
                color = if (active) EmpireColors.Violet else EmpireColors.Surface,
                shape = RoundedCornerShape(12.dp),
                modifier = Modifier.weight(1f).height(42.dp).clickable { vm.setBuyMode(mode) }
            ) {
                Box(contentAlignment = Alignment.Center) {
                    Text(label, color = if (active) Color.White else EmpireColors.TextSecondary, fontSize = 9.sp, fontWeight = FontWeight.Black)
                }
            }
        }
    }
}
