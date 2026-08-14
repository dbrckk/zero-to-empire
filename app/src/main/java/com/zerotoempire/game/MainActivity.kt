package com.zerotoempire.game

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import java.time.LocalDate
import java.util.Locale
import kotlin.math.abs

enum class GameTab { EMPIRE, MANAGERS, UPGRADES, GOALS }

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) { super.onCreate(savedInstanceState); setContent { ZeroToEmpireApp() } }
}

@Composable
fun ZeroToEmpireApp(vm: GameViewModel = viewModel()) {
    val state by vm.state.collectAsStateWithLifecycle()
    val meta by vm.meta.collectAsStateWithLifecycle()
    val offlineReward by vm.offlineReward.collectAsStateWithLifecycle()
    var tab by remember { mutableStateOf(GameTab.EMPIRE) }

    MaterialTheme(colorScheme = EmpireColorScheme) {
        offlineReward?.let { reward -> OfflineRewardDialog(reward, vm::dismissOfflineReward) }
        Scaffold(containerColor = EmpireColors.Void, bottomBar = { GameNav(tab) { tab = it } }) { inset ->
            LazyColumn(Modifier.padding(inset).fillMaxSize().background(Brush.verticalGradient(listOf(EmpireColors.Void, EmpireColors.DeepSpace))).padding(horizontal = 16.dp), verticalArrangement = Arrangement.spacedBy(10.dp), contentPadding = PaddingValues(bottom = 24.dp)) {
                item { Header(state) }
                LiveOps.currentEvent(LocalDate.now())?.let { event -> item { EventBanner(event) } }
                when (tab) {
                    GameTab.EMPIRE -> {
                        item { WealthHero(state) }
                        item { PowerTap(state, vm::tap) }
                        item { Section("YOUR EMPIRE", "${state.businesses.sumOf { it.level }} total assets") }
                        items(state.businesses) { b -> BusinessCard(b, state, state.cash >= b.nextCost) { vm.buy(b.id) } }
                        item { PrestigeCard(state, vm::prestige) }
                    }
                    GameTab.MANAGERS -> {
                        item { Section("MANAGERS", "Automate and multiply every asset") }
                        items(Managers.catalog) { m -> ManagerCard(m, state) { vm.hireManager(m.businessId) } }
                    }
                    GameTab.UPGRADES -> {
                        item { Section("PERMANENT LAB", "Spend gems on permanent power") }
                        item { Text("◆ ${state.gems} GEMS", color = EmpireColors.Violet, fontSize = 24.sp, fontWeight = FontWeight.Black) }
                        items(Upgrades.catalog) { u -> UpgradeCard(u, state) { vm.buyUpgrade(u.id) } }
                        item { BoostCard(state, vm::activateProfitBoost) }
                    }
                    GameTab.GOALS -> {
                        item { Section("COMMAND CENTER", "Daily momentum and permanent achievements") }
                        item { DailyRewardCard(meta, vm.canClaimDaily(), vm::claimDaily) }
                        item { Section("MISSIONS", "Complete objectives to earn gems") }
                        items(vm.missions()) { mission -> MissionCard(mission) { vm.claimMission(mission.id) } }
                        item { Section("ACHIEVEMENTS", "Permanent milestones across your empire") }
                        items(vm.achievements()) { achievement -> AchievementCard(achievement) { vm.claimAchievement(achievement.id) } }
                    }
                }
            }
        }
    }
}

@Composable private fun DailyRewardCard(meta:PlayerMeta, claimable:Boolean, claim:()->RewardDay?) { val next=LoginCalendar.rewardFor(meta.streakDays+1); Surface(color=EmpireColors.Gold.copy(alpha=.13f),shape=RoundedCornerShape(20.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(18.dp)){Text("DAILY CAPITAL DROP",color=EmpireColors.Gold,fontWeight=FontWeight.Black,fontSize=18.sp);Text("STREAK ${meta.streakDays} DAYS",color=EmpireColors.TextSecondary,fontSize=11.sp);Spacer(Modifier.height(8.dp));Text("Next reward: ◆ ${next.gems}${if(next.multiplierMinutes>0) " + ×2 for ${next.multiplierMinutes}m" else ""}",color=EmpireColors.TextPrimary,fontWeight=FontWeight.Bold);Spacer(Modifier.height(10.dp));Button(onClick={claim()},enabled=claimable,modifier=Modifier.fillMaxWidth()){Text(if(claimable)"CLAIM DAILY REWARD" else "CLAIMED TODAY",fontWeight=FontWeight.Black)}}} }
@Composable private fun MissionCard(m:Mission,claim:()->Unit){Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(16.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(14.dp)){Row(verticalAlignment=Alignment.CenterVertically){Column(Modifier.weight(1f)){Text(m.title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Bold);Text("◆ ${m.rewardGems} reward",color=EmpireColors.Violet,fontSize=11.sp)};Button(onClick=claim,enabled=m.completed&&!m.claimed){Text(if(m.claimed)"DONE" else if(m.completed)"CLAIM" else "${(m.fraction*100).toInt()}%",fontSize=10.sp)}};Spacer(Modifier.height(7.dp));LinearProgressIndicator(progress={m.fraction},modifier=Modifier.fillMaxWidth().height(4.dp),color=EmpireColors.Cyan,trackColor=EmpireColors.SurfaceHigh)}}}
@Composable private fun AchievementCard(a:Achievement,claim:()->Unit){Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(16.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(14.dp),verticalAlignment=Alignment.CenterVertically){Text(if(a.unlocked)"★" else "☆",color=if(a.unlocked)EmpireColors.Gold else EmpireColors.TextSecondary,fontSize=28.sp);Spacer(Modifier.width(10.dp));Column(Modifier.weight(1f)){Text(a.title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Text(a.description,color=EmpireColors.TextSecondary,fontSize=11.sp)};Button(onClick=claim,enabled=a.unlocked&&!a.claimed){Text(if(a.claimed)"DONE" else "◆ ${a.rewardGems}",fontSize=10.sp)}}}}

@Composable
private fun OfflineRewardDialog(reward: OfflineReward, dismiss: () -> Unit) {
    val hours = reward.paidSeconds / 3600; val minutes = (reward.paidSeconds % 3600) / 60
    AlertDialog(onDismissRequest = dismiss, containerColor = EmpireColors.SurfaceHigh, title = { Text("EMPIRE NEVER SLEEPS", color = EmpireColors.Gold, fontWeight = FontWeight.Black) }, text = { Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.fillMaxWidth()) { Text("Your managers kept the machine running while you were away.", color = EmpireColors.TextSecondary, textAlign = TextAlign.Center); Spacer(Modifier.height(18.dp)); Text("+${money(reward.cash)}", color = EmpireColors.Success, fontSize = 34.sp, fontWeight = FontWeight.Black); Text("$hours h ${minutes} min of offline production", color = EmpireColors.TextSecondary, fontSize = 12.sp); Spacer(Modifier.height(10.dp)); Text("75% OFFLINE EFFICIENCY", color = EmpireColors.Cyan, fontSize = 10.sp, fontWeight = FontWeight.Bold) } }, confirmButton = { Button(onClick = dismiss, modifier = Modifier.fillMaxWidth()) { Text("COLLECT", fontWeight = FontWeight.Black) } })
}

@Composable private fun GameNav(selected: GameTab, onSelect: (GameTab) -> Unit) { NavigationBar(containerColor = EmpireColors.Surface) { GameTab.entries.forEach { tab -> NavigationBarItem(selected = tab == selected, onClick = { onSelect(tab) }, icon = { Text(when(tab){ GameTab.EMPIRE -> "◈"; GameTab.MANAGERS -> "♟"; GameTab.UPGRADES -> "◆"; GameTab.GOALS -> "★" }) }, label = { Text(tab.name) }) } } }
@Composable private fun Header(s: GameState) { Row(Modifier.fillMaxWidth().padding(top=16.dp), verticalAlignment=Alignment.CenterVertically) { Column(Modifier.weight(1f)) { Text("ZERO → EMPIRE", color=EmpireColors.Gold, fontWeight=FontWeight.Black, fontSize=23.sp); Text("FROM NOTHING. BEYOND EVERYTHING.", color=EmpireColors.TextSecondary, fontSize=9.sp) }; Text("◆ ${s.gems}   ◇ ${s.prestigePoints}", color=EmpireColors.Violet, fontWeight=FontWeight.Bold) } }
@Composable private fun EventBanner(e: LiveEvent) { Surface(color=EmpireColors.Violet.copy(alpha=.16f), shape=RoundedCornerShape(15.dp), modifier=Modifier.fillMaxWidth()) { Row(Modifier.padding(13.dp), verticalAlignment=Alignment.CenterVertically) { Text(e.icon, fontSize=25.sp); Spacer(Modifier.width(10.dp)); Column { Text(e.name.uppercase(), color=EmpireColors.Violet, fontWeight=FontWeight.Black); Text("${e.description}  ×${e.incomeMultiplier}", color=EmpireColors.TextSecondary, fontSize=11.sp) } } } }
@Composable private fun WealthHero(s: GameState) { Surface(shape=RoundedCornerShape(24.dp), color=EmpireColors.SurfaceHigh, modifier=Modifier.fillMaxWidth()) { Column(Modifier.padding(20.dp)) { Text("NET WORTH", color=EmpireColors.TextSecondary, fontSize=10.sp); Text(money(s.cash), color=EmpireColors.TextPrimary, fontSize=39.sp, fontWeight=FontWeight.Black); Text("▲ ${money(s.incomePerSecond)} / SEC   ×${String.format(Locale.US,"%.1f",s.prestigeMultiplier)} LEGACY", color=EmpireColors.Success, fontWeight=FontWeight.Bold, fontSize=12.sp) } } }
@Composable private fun PowerTap(s: GameState, tap:()->Unit) { Box(Modifier.fillMaxWidth().padding(8.dp), contentAlignment=Alignment.Center) { Surface(Modifier.size(180.dp).clickable(onClick=tap), shape=CircleShape, color=EmpireColors.Gold, shadowElevation=18.dp) { Box(Modifier.background(Brush.radialGradient(listOf(EmpireColors.GoldBright,EmpireColors.Gold))), contentAlignment=Alignment.Center) { Column(horizontalAlignment=Alignment.CenterHorizontally) { Text("$", color=EmpireColors.Void, fontSize=52.sp, fontWeight=FontWeight.Black); Text("POWER TAP", color=EmpireColors.Void, fontWeight=FontWeight.Black); Text("+${money(s.tapValue)}", color=EmpireColors.Void.copy(alpha=.7f), fontWeight=FontWeight.Bold) } } } } }
@Composable private fun Section(title:String, subtitle:String) { Column(Modifier.padding(top=8.dp)) { Text(title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black,fontSize=19.sp); Text(subtitle,color=EmpireColors.TextSecondary,fontSize=11.sp) } }
@Composable private fun BusinessCard(b:Business,s:GameState,affordable:Boolean,buy:()->Unit) { val milestone=b.nextMilestone ?: ((b.level/1000)+1)*1000; val progress=(b.level.toFloat()/milestone).coerceIn(0f,1f); Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth().clickable(enabled=affordable,onClick=buy)) { Column(Modifier.padding(14.dp)) { Row(verticalAlignment=Alignment.CenterVertically) { Text(b.emoji,fontSize=30.sp); Spacer(Modifier.width(11.dp)); Column(Modifier.weight(1f)){Text(b.name,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Bold);Text("LV ${b.level} • ${money(s.businessIncome(b))}/s",color=EmpireColors.Cyan,fontSize=11.sp)}; Text(money(b.nextCost),color=if(affordable) EmpireColors.Gold else EmpireColors.TextSecondary,fontWeight=FontWeight.Bold) }; Spacer(Modifier.height(8.dp)); LinearProgressIndicator(progress={progress},modifier=Modifier.fillMaxWidth().height(4.dp),color=EmpireColors.Gold,trackColor=EmpireColors.SurfaceHigh); Text("NEXT POWER SPIKE • LV $milestone",color=EmpireColors.TextSecondary,fontSize=9.sp) } } }
@Composable private fun ManagerCard(m:Manager,s:GameState,hire:()->Unit) { val hired=m.businessId in s.hiredManagerIds; val affordable=s.cash>=m.cost; Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth()) { Row(Modifier.padding(15.dp),verticalAlignment=Alignment.CenterVertically){ Surface(shape=CircleShape,color=EmpireColors.SurfaceHigh){Text(m.name.take(1),modifier=Modifier.padding(15.dp),color=EmpireColors.Gold,fontWeight=FontWeight.Black)};Spacer(Modifier.width(12.dp));Column(Modifier.weight(1f)){Text(m.name,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Text(m.title,color=EmpireColors.TextSecondary,fontSize=11.sp);Text("×${m.incomeMultiplier} production",color=EmpireColors.Success,fontSize=11.sp)};Button(onClick=hire,enabled=!hired&&affordable){Text(if(hired)"HIRED" else money(m.cost),fontSize=10.sp)} } } }
@Composable private fun UpgradeCard(u:Upgrade,s:GameState,buy:()->Unit) { val rank=s.upgradeRanks[u.id]?:0; val maxed=rank>=u.maxRank; Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth()) { Row(Modifier.padding(15.dp),verticalAlignment=Alignment.CenterVertically){Column(Modifier.weight(1f)){Text(u.name,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Text(u.description,color=EmpireColors.TextSecondary,fontSize=11.sp);Text("RANK $rank / ${u.maxRank}",color=EmpireColors.Cyan,fontSize=10.sp)};Button(onClick=buy,enabled=!maxed&&s.gems>=u.gemCost){Text(if(maxed)"MAX" else "◆ ${u.gemCost}")} } } }
@Composable private fun BoostCard(s:GameState,boost:()->Unit) { val active=System.currentTimeMillis()<s.boostEndsAtMillis; Surface(color=EmpireColors.Gold.copy(alpha=.12f),shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth()) { Column(Modifier.padding(16.dp)){Text("PROFIT OVERDRIVE",color=EmpireColors.Gold,fontWeight=FontWeight.Black);Text("Double all income for 10 minutes.",color=EmpireColors.TextSecondary,fontSize=11.sp);Spacer(Modifier.height(8.dp));Button(onClick=boost,enabled=!active){Text(if(active)"BOOST ACTIVE ×2" else "ACTIVATE ×2 BOOST")}} } }
@Composable private fun PrestigeCard(s:GameState,prestige:()->Unit) { val reward=(Progression.prestigeReward(s.lifetimeCash)-s.prestigePoints).coerceAtLeast(0); Surface(color=EmpireColors.SurfaceHigh,shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth()) { Column(Modifier.padding(19.dp),horizontalAlignment=Alignment.CenterHorizontally){Text("ASCENSION",color=EmpireColors.Violet,fontWeight=FontWeight.Black,fontSize=20.sp);Text("Reset this empire for permanent legacy power.",color=EmpireColors.TextSecondary,textAlign=TextAlign.Center,fontSize=11.sp);Text("+$reward LEGACY",color=EmpireColors.Gold,fontWeight=FontWeight.Black,fontSize=17.sp);Button(onClick=prestige,enabled=reward>0,modifier=Modifier.fillMaxWidth()){Text("TRANSCEND")}} } }
private fun money(value:Double):String { val v=abs(value); val units=listOf(1e18 to "Qi",1e15 to "Q",1e12 to "T",1e9 to "B",1e6 to "M",1e3 to "K"); val u=units.firstOrNull{v>=it.first}; return if(u!=null) "$${String.format(Locale.US,"%.2f",value/u.first)}${u.second}" else "$${String.format(Locale.US,"%.0f",value)}" }
