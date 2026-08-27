package com.zerotoempire.game

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.spring
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.alpha
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import java.time.LocalDate
import java.util.Locale

enum class GameTab { EMPIRE, MANAGERS, UPGRADES, GOALS }

@Composable
fun ZeroToEmpireApp(vm: GameViewModel = viewModel()) {
    val state by vm.state.collectAsStateWithLifecycle()
    val meta by vm.meta.collectAsStateWithLifecycle()
    val offlineReward by vm.offlineReward.collectAsStateWithLifecycle()
    val buyMode by vm.buyMode.collectAsStateWithLifecycle()
    var tab by remember { mutableStateOf(GameTab.EMPIRE) }
    val eraIndex = EmpireEras.current(state.lifetimeCash).index
    val visibleBusinesses = remember(state.businesses, state.lifetimeCash) { ContentUnlocks.visibleBusinesses(state) }
    val visibleManagers = remember(state.hiredManagerIds, state.lifetimeCash) { ContentUnlocks.visibleManagers(state) }

    MaterialTheme(colorScheme = EmpireColorScheme) {
        offlineReward?.let { OfflineRewardDialog(it, vm::dismissOfflineReward, vm::requestDoubleOfflineAd) }
        Scaffold(containerColor = EmpireColors.Void, bottomBar = { GameNav(tab) { tab = it } }) { inset ->
            Box(Modifier.padding(inset).fillMaxSize()) {
                EmpireAmbientBackdrop(eraIndex, Modifier.fillMaxSize())
                LazyColumn(
                    modifier = Modifier.fillMaxSize().padding(horizontal = 16.dp),
                    verticalArrangement = Arrangement.spacedBy(12.dp),
                    contentPadding = PaddingValues(top = 10.dp, bottom = 32.dp)
                ) {
                    item { Header(state) }
                    LiveOps.currentEvent(LocalDate.now())?.let { event -> item { EventBanner(event) } }
                    when (tab) {
                        GameTab.EMPIRE -> {
                            item { WealthHero(state) }
                            item { EraVistaCard(state) }
                            item { EmpireControlDeck(vm, buyMode) }
                            item { JuicyPowerTap(state, vm::tap) }
                            item { Section("YOUR EMPIRE", "${state.businesses.sumOf { it.level }} total assets") }
                            items(visibleBusinesses, key = { it.id }) { business -> JuicyBusinessCard(business, state) { vm.buy(business.id) } }
                            ContentUnlocks.nextHiddenBusiness(state)?.let { next -> item { NextAssetUnlockCard(state, next) } }
                            item { PrestigeCard(state, vm::prestige) }
                        }
                        GameTab.MANAGERS -> {
                            item { Section("MANAGERS", "Recruit, automate and master every revealed asset") }
                            items(visibleManagers, key = { it.businessId }) { manager -> ManagerCard(manager, state) { vm.hireManager(manager.businessId) } }
                            ContentUnlocks.nextHiddenBusiness(state)?.let { next -> item { NextManagerUnlockCard(state, next) } }
                        }
                        GameTab.UPGRADES -> {
                            item { Section("PERMANENT LAB", "Spend gems on permanent power") }
                            item { Row(verticalAlignment = Alignment.CenterVertically) { MetaSprite(MetaSpriteKind.GEM, 38.dp); Spacer(Modifier.width(8.dp)); Text("${state.gems} GEMS", color = EmpireColors.Violet, fontSize = 24.sp, fontWeight = FontWeight.Black) } }
                            items(Upgrades.catalog) { upgrade -> UpgradeCard(upgrade, state) { vm.buyUpgrade(upgrade.id) } }
                            item { BoostCard(state, vm::activateProfitBoost) }
                        }
                        GameTab.GOALS -> {
                            item { Section("COMMAND CENTER", "Daily, weekly and permanent objectives") }
                            item { ChallengeDock(vm, Modifier.fillMaxWidth()) }
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
}

@Composable
private fun EmpireControlDeck(vm: GameViewModel, selected: BuyMode) {
    Surface(shape = RoundedCornerShape(20.dp), color = EmpireColors.Surface.copy(alpha = .92f), modifier = Modifier.fillMaxWidth()) {
        Column(Modifier.padding(12.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text("PURCHASE MODE", color = EmpireColors.TextSecondary, fontSize = 9.sp, fontWeight = FontWeight.Black, modifier = Modifier.weight(1f))
                ChallengeDock(vm)
            }
            Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(5.dp)) {
                listOf(BuyMode.X1 to "×1", BuyMode.X10 to "×10", BuyMode.X25 to "×25", BuyMode.MILESTONE to "NEXT", BuyMode.MAX to "MAX").forEach { (mode, label) ->
                    if (mode == selected) Button(onClick = { vm.setBuyMode(mode) }, modifier = Modifier.weight(1f).height(38.dp), contentPadding = PaddingValues(0.dp), shape = RoundedCornerShape(11.dp)) { Text(label, fontSize = 9.sp, fontWeight = FontWeight.Black) }
                    else TextButton(onClick = { vm.setBuyMode(mode) }, modifier = Modifier.weight(1f).height(38.dp), contentPadding = PaddingValues(0.dp), shape = RoundedCornerShape(11.dp)) { Text(label, fontSize = 9.sp, fontWeight = FontWeight.Bold, color = EmpireColors.TextSecondary) }
                }
            }
        }
    }
}

@Composable
private fun JuicyPowerTap(state: GameState, tap: () -> Unit) {
    val haptics = LocalHapticFeedback.current
    val scope = rememberCoroutineScope()
    val scale = remember { Animatable(1f) }
    var burst by remember { mutableStateOf(false) }
    var displayedGain by remember { mutableDoubleStateOf(0.0) }
    Box(Modifier.fillMaxWidth().height(226.dp), contentAlignment = Alignment.Center) {
        Surface(modifier = Modifier.size(184.dp).scale(scale.value).pointerInput(state.tapValue) { detectTapGestures(onPress = { scale.animateTo(.92f, spring(stiffness = Spring.StiffnessHigh)); if (tryAwaitRelease()) { displayedGain = state.tapValue; tap(); haptics.performHapticFeedback(HapticFeedbackType.TextHandleMove); burst = true; scope.launch { scale.animateTo(1.06f, spring(dampingRatio = .42f, stiffness = Spring.StiffnessMedium)); scale.animateTo(1f, spring(dampingRatio = .55f)) }; scope.launch { delay(520); burst = false } } else scale.snapTo(1f) }) }, shape = CircleShape, color = EmpireColors.SurfaceHigh, shadowElevation = 24.dp) {
            Box(Modifier.background(Brush.radialGradient(listOf(EmpireColors.Gold.copy(alpha = .35f), EmpireColors.SurfaceHigh, EmpireColors.Void))), contentAlignment = Alignment.Center) {
                EmpireCoreGlyph(Modifier.size(142.dp))
                Column(Modifier.align(Alignment.BottomCenter).padding(bottom = 18.dp), horizontalAlignment = Alignment.CenterHorizontally) { Text("POWER CORE", color = EmpireColors.GoldBright, fontWeight = FontWeight.Black, fontSize = 11.sp); Text("+${money(state.tapValue)}", color = EmpireColors.TextPrimary, fontWeight = FontWeight.Black, fontSize = 12.sp) }
            }
        }
        if (burst) Text("+${money(displayedGain)}", color = EmpireColors.GoldBright, fontWeight = FontWeight.Black, fontSize = 20.sp, modifier = Modifier.align(Alignment.TopCenter).padding(top = 4.dp))
    }
}

@Composable
private fun JuicyBusinessCard(business: Business, state: GameState, buy: () -> Unit) {
    val haptics = LocalHapticFeedback.current; val affordable = state.cash >= business.nextCost
    var lastLevel by remember(business.id) { mutableIntStateOf(business.level) }; var milestoneFlash by remember(business.id) { mutableStateOf(false) }
    val milestone = business.nextMilestone ?: ((business.level / 1000) + 1) * 1000; val progress = (business.level.toFloat() / milestone).coerceIn(0f, 1f)
    LaunchedEffect(business.level) { if (business.level > lastLevel) { if (business.level in listOf(10,25,50,100,250,500,1000)) { milestoneFlash = true; haptics.performHapticFeedback(HapticFeedbackType.LongPress); delay(900); milestoneFlash = false }; lastLevel = business.level } }
    Surface(color = if (milestoneFlash) EmpireColors.Gold.copy(alpha=.20f) else EmpireColors.Surface.copy(alpha=.94f), shape=RoundedCornerShape(18.dp), modifier=Modifier.fillMaxWidth().clickable(enabled=affordable){buy();haptics.performHapticFeedback(HapticFeedbackType.TextHandleMove)}) {
        Column(Modifier.padding(14.dp)) { Row(verticalAlignment=Alignment.CenterVertically){ BusinessArtIcon(business.id,50.dp); Spacer(Modifier.width(11.dp)); Column(Modifier.weight(1f)){Text(business.name,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Bold);Text("LV ${business.level} • ${money(state.businessIncome(business))}/s",color=EmpireColors.Cyan,fontSize=11.sp)}; Text(money(business.nextCost),color=if(affordable)EmpireColors.Gold else EmpireColors.TextSecondary,fontWeight=FontWeight.Bold)}; Spacer(Modifier.height(8.dp)); LinearProgressIndicator(progress={progress},modifier=Modifier.fillMaxWidth().height(4.dp),color=EmpireColors.Gold,trackColor=EmpireColors.SurfaceHigh); Text(if(milestoneFlash)"POWER SPIKE UNLOCKED ×${GameEconomy.milestoneMultiplier(business.level)}" else "NEXT POWER SPIKE • LV $milestone",color=if(milestoneFlash)EmpireColors.GoldBright else EmpireColors.TextSecondary,fontSize=9.sp,fontWeight=if(milestoneFlash)FontWeight.Black else FontWeight.Normal) }
    }
}

@Composable private fun NextAssetUnlockCard(state:GameState,next:Business){val threshold=ContentUnlocks.thresholdForBusiness(next.id);val progress=ContentUnlocks.progressToNextUnlock(state);Surface(color=EmpireColors.Surface.copy(alpha=.72f),shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(14.dp)){Row(verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.LOCK,50.dp,active=false);Spacer(Modifier.width(11.dp));Column(Modifier.weight(1f)){Text("CLASSIFIED ASSET",color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Text("Next economic class reveals at ${money(threshold)} lifetime capital",color=EmpireColors.TextSecondary,fontSize=10.sp)}};Spacer(Modifier.height(9.dp));LinearProgressIndicator(progress={progress},modifier=Modifier.fillMaxWidth().height(4.dp),color=EmpireColors.Violet,trackColor=EmpireColors.SurfaceHigh)}}}
@Composable private fun NextManagerUnlockCard(state:GameState,next:Business){val threshold=ContentUnlocks.thresholdForBusiness(next.id);Surface(color=EmpireColors.Violet.copy(alpha=.08f),shape=RoundedCornerShape(16.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(14.dp),verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.LOCK,42.dp,active=false);Spacer(Modifier.width(10.dp));Column{Text("NEXT EXECUTIVE CLASSIFIED",color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black,fontSize=12.sp);Text("Reveals with the next asset at ${money(threshold)} lifetime capital",color=EmpireColors.TextSecondary,fontSize=10.sp)}}}}

private enum class ManagerVisualState { LOCKED, RECRUIT, HIRED, MASTERED }
private fun managerVisualState(manager:Manager,state:GameState):ManagerVisualState{val hired=manager.businessId in state.hiredManagerIds;val level=state.businesses.firstOrNull{it.id==manager.businessId}?.level?:0;return when{hired&&level>=100->ManagerVisualState.MASTERED;hired->ManagerVisualState.HIRED;state.cash>=manager.cost->ManagerVisualState.RECRUIT;else->ManagerVisualState.LOCKED}}
@Composable private fun ManagerCard(manager:Manager,gameState:GameState,hire:()->Unit){val h=LocalHapticFeedback.current;val vs=managerVisualState(manager,gameState);val accent=when(vs){ManagerVisualState.LOCKED->EmpireColors.TextSecondary;ManagerVisualState.RECRUIT->EmpireColors.Gold;ManagerVisualState.HIRED->EmpireColors.Cyan;ManagerVisualState.MASTERED->EmpireColors.GoldBright};Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth().border(1.dp,accent.copy(alpha=.35f),RoundedCornerShape(18.dp))){Row(Modifier.padding(15.dp),verticalAlignment=Alignment.CenterVertically){ManagerPortrait(manager.businessId,56.dp);Spacer(Modifier.width(12.dp));Column(Modifier.weight(1f)){Text(manager.name,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Text(manager.title,color=EmpireColors.TextSecondary,fontSize=11.sp);Text("×${manager.incomeMultiplier} production",color=accent,fontSize=11.sp,fontWeight=FontWeight.Bold)};Button(onClick={hire();h.performHapticFeedback(HapticFeedbackType.LongPress)},enabled=vs==ManagerVisualState.RECRUIT){Text(if(vs==ManagerVisualState.RECRUIT)"HIRE" else vs.name,fontSize=9.sp)}}}}
@Composable private fun DailyRewardCard(meta:PlayerMeta,claimable:Boolean,claim:()->RewardDay?){val next=LoginCalendar.rewardFor(meta.streakDays+1);Surface(color=EmpireColors.Gold.copy(alpha=.13f),shape=RoundedCornerShape(20.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(18.dp)){Row(verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.DAILY,46.dp,active=claimable);Spacer(Modifier.width(10.dp));Column{Text("DAILY CAPITAL DROP",color=EmpireColors.Gold,fontWeight=FontWeight.Black,fontSize=18.sp);Text("STREAK ${meta.streakDays} DAYS",color=EmpireColors.TextSecondary,fontSize=11.sp)}};Spacer(Modifier.height(8.dp));Text("Next reward: ${next.gems} gems${if(next.multiplierMinutes>0)" + ×2 for ${next.multiplierMinutes}m" else ""}",color=EmpireColors.TextPrimary,fontWeight=FontWeight.Bold);Spacer(Modifier.height(10.dp));Button(onClick={claim()},enabled=claimable,modifier=Modifier.fillMaxWidth()){Text(if(claimable)"CLAIM DAILY REWARD" else "CLAIMED TODAY",fontWeight=FontWeight.Black)}}}}
@Composable private fun MissionCard(mission:Mission,claim:()->Unit){Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(16.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(14.dp)){Row(verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.MISSION,40.dp,active=!mission.claimed,progress=mission.fraction);Spacer(Modifier.width(10.dp));Column(Modifier.weight(1f)){Text(mission.title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Bold);Text("${mission.rewardGems} gems",color=EmpireColors.Violet,fontSize=11.sp)};Button(onClick=claim,enabled=mission.completed&&!mission.claimed){Text(if(mission.claimed)"DONE" else if(mission.completed)"CLAIM" else "${(mission.fraction*100).toInt()}%",fontSize=10.sp)}};Spacer(Modifier.height(7.dp));LinearProgressIndicator(progress={mission.fraction},modifier=Modifier.fillMaxWidth().height(4.dp),color=EmpireColors.Cyan,trackColor=EmpireColors.SurfaceHigh)}}}
@Composable private fun AchievementCard(achievement:Achievement,claim:()->Unit){Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(16.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(14.dp),verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.ACHIEVEMENT,46.dp,active=achievement.unlocked);Spacer(Modifier.width(10.dp));Column(Modifier.weight(1f)){Text(achievement.title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Text(achievement.description,color=EmpireColors.TextSecondary,fontSize=11.sp)};Button(onClick=claim,enabled=achievement.unlocked&&!achievement.claimed){Text(if(achievement.claimed)"DONE" else "${achievement.rewardGems}",fontSize=10.sp)}}}}
@Composable private fun OfflineRewardDialog(reward:OfflineReward,dismiss:()->Unit,doubleReward:()->Unit){AlertDialog(onDismissRequest=dismiss,containerColor=EmpireColors.SurfaceHigh,title={Text("EMPIRE NEVER SLEEPS",color=EmpireColors.Gold,fontWeight=FontWeight.Black)},text={Column(horizontalAlignment=Alignment.CenterHorizontally,modifier=Modifier.fillMaxWidth()){MetaSprite(MetaSpriteKind.CASH,64.dp);Text("+${money(reward.cash)}",color=EmpireColors.Success,fontSize=34.sp,fontWeight=FontWeight.Black);Text("Offline production secured",color=EmpireColors.TextSecondary)}},confirmButton={Column(Modifier.fillMaxWidth()){Button(onClick=doubleReward,modifier=Modifier.fillMaxWidth()){Text("DOUBLE REWARD",fontWeight=FontWeight.Black)};TextButton(onClick=dismiss,modifier=Modifier.fillMaxWidth()){Text("COLLECT")}}})}
@Composable private fun GameNav(selected:GameTab,onSelect:(GameTab)->Unit){NavigationBar(containerColor=EmpireColors.Surface){GameTab.entries.forEach{tab->NavigationBarItem(selected=tab==selected,onClick={onSelect(tab)},icon={NavSprite(tab,selected=tab==selected,size=28.dp)},label={Text(tab.name)})}}}
@Composable private fun Header(state:GameState){Row(Modifier.fillMaxWidth(),verticalAlignment=Alignment.CenterVertically){Column(Modifier.weight(1f)){Text("ZERO → EMPIRE",color=EmpireColors.Gold,fontWeight=FontWeight.Black,fontSize=23.sp);Text("FROM NOTHING. BEYOND EVERYTHING.",color=EmpireColors.TextSecondary,fontSize=9.sp)};Row(verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.GEM,25.dp);Text("${state.gems}",color=EmpireColors.Violet,fontWeight=FontWeight.Bold);Spacer(Modifier.width(6.dp));MetaSprite(MetaSpriteKind.LEGACY,25.dp);Text("${state.prestigePoints}",color=EmpireColors.Gold,fontWeight=FontWeight.Bold)}}}
@Composable private fun EventBanner(event:LiveEvent){Surface(color=EmpireColors.Violet.copy(alpha=.16f),shape=RoundedCornerShape(15.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(13.dp),verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.EVENT,42.dp);Spacer(Modifier.width(10.dp));Column{Text(event.name.uppercase(),color=EmpireColors.Violet,fontWeight=FontWeight.Black);Text("${event.description}  ×${event.incomeMultiplier}",color=EmpireColors.TextSecondary,fontSize=11.sp)}}}}
@Composable private fun WealthHero(state:GameState){Surface(shape=RoundedCornerShape(24.dp),color=EmpireColors.SurfaceHigh.copy(alpha=.92f),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(20.dp),verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.CASH,52.dp);Spacer(Modifier.width(12.dp));Column{Text("NET WORTH",color=EmpireColors.TextSecondary,fontSize=10.sp);Text(money(state.cash),color=EmpireColors.TextPrimary,fontSize=36.sp,fontWeight=FontWeight.Black);Text("${money(state.incomePerSecond)} / SEC   ×${String.format(Locale.US,"%.1f",state.prestigeMultiplier)} LEGACY",color=EmpireColors.Success,fontWeight=FontWeight.Bold,fontSize=12.sp)}}}}
@Composable private fun EraVistaCard(state:GameState){val era=EmpireEras.current(state.lifetimeCash);Surface(shape=RoundedCornerShape(20.dp),color=EmpireColors.Surface.copy(alpha=.88f),modifier=Modifier.fillMaxWidth().height(150.dp)){Box(Modifier.fillMaxSize()){EraVista(era.index,Modifier.fillMaxSize());Column(Modifier.fillMaxSize().background(Brush.verticalGradient(listOf(EmpireColors.Void.copy(alpha=.02f),EmpireColors.Void.copy(alpha=.90f)))).padding(15.dp),verticalArrangement=Arrangement.Bottom){Text("ERA ${era.index+1}",color=EmpireColors.Cyan,fontSize=9.sp,fontWeight=FontWeight.Black,letterSpacing=1.5.sp);Text(era.name,color=EmpireColors.TextPrimary,fontSize=21.sp,fontWeight=FontWeight.Black);Text(era.subtitle,color=EmpireColors.TextSecondary,fontSize=11.sp)}}}}
@Composable private fun Section(title:String,subtitle:String){Column(Modifier.padding(top=8.dp)){Text(title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black,fontSize=19.sp);Text(subtitle,color=EmpireColors.TextSecondary,fontSize=11.sp)}}
@Composable private fun UpgradeCard(upgrade:Upgrade,state:GameState,buy:()->Unit){val rank=state.upgradeRanks[upgrade.id]?:0;val maxed=rank>=upgrade.maxRank;Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(15.dp),verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.UPGRADE,46.dp,active=!maxed);Spacer(Modifier.width(10.dp));Column(Modifier.weight(1f)){Text(upgrade.name,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Text(upgrade.description,color=EmpireColors.TextSecondary,fontSize=10.sp);Text("RANK $rank/${upgrade.maxRank}",color=EmpireColors.Cyan,fontSize=9.sp)};Button(onClick=buy,enabled=!maxed&&state.gems>=upgrade.cost(rank)){Text(if(maxed)"MAX" else "${upgrade.cost(rank)}",fontSize=10.sp)}}}}
@Composable private fun BoostCard(state:GameState,activate:()->Unit){Surface(color=EmpireColors.Violet.copy(alpha=.12f),shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(16.dp),verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.BOOST,48.dp);Spacer(Modifier.width(10.dp));Column(Modifier.weight(1f)){Text("PROFIT SURGE",color=EmpireColors.Violet,fontWeight=FontWeight.Black);Text("Temporary ×2 production",color=EmpireColors.TextSecondary,fontSize=11.sp)};Button(onClick=activate){Text("ACTIVATE",fontSize=9.sp)}}}}
@Composable private fun PrestigeCard(state:GameState,prestige:()->Unit){val gain=state.prestigeGain;Surface(color=EmpireColors.Gold.copy(alpha=.10f),shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(18.dp)){Row(verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.LEGACY,52.dp);Spacer(Modifier.width(10.dp));Column{Text("ASCENSION",color=EmpireColors.Gold,fontWeight=FontWeight.Black,fontSize=19.sp);Text("Reset the run. Keep permanent Legacy power.",color=EmpireColors.TextSecondary,fontSize=10.sp)}};Spacer(Modifier.height(10.dp));Button(onClick=prestige,enabled=gain>0,modifier=Modifier.fillMaxWidth()){Text(if(gain>0)"ASCEND +$gain LEGACY" else "BUILD MORE CAPITAL",fontWeight=FontWeight.Black)}}}}
private fun money(value:Double)=EmpireNumberFormat.money(value)
