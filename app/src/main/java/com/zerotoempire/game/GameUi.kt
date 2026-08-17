package com.zerotoempire.game

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.scaleIn
import androidx.compose.animation.scaleOut
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.Spring
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
    var tab by remember { mutableStateOf(GameTab.EMPIRE) }
    val eraIndex = EmpireEras.current(state.lifetimeCash).index
    val visibleBusinesses = remember(state.businesses, state.lifetimeCash) { ContentUnlocks.visibleBusinesses(state) }
    val visibleManagers = remember(state.hiredManagerIds, state.lifetimeCash) { ContentUnlocks.visibleManagers(state) }

    MaterialTheme(colorScheme = EmpireColorScheme) {
        offlineReward?.let { OfflineRewardDialog(it, vm::dismissOfflineReward, vm::requestDoubleOfflineAd) }
        Scaffold(containerColor = EmpireColors.Void, bottomBar = { GameNav(tab) { tab = it } }) { inset ->
            Box(Modifier.padding(inset).fillMaxSize()) {
                EmpireAmbientBackdrop(eraIndex = eraIndex, modifier = Modifier.matchParentSize())
                LazyColumn(
                    Modifier.fillMaxSize().padding(horizontal = 16.dp),
                    verticalArrangement = Arrangement.spacedBy(10.dp),
                    contentPadding = PaddingValues(bottom = 24.dp)
                ) {
                    item { Header(state) }
                    LiveOps.currentEvent(LocalDate.now())?.let { event -> item { EventBanner(event) } }
                    when (tab) {
                        GameTab.EMPIRE -> {
                            item { WealthHero(state) }
                            item { EraVistaCard(state) }
                            item { JuicyPowerTap(state, vm::tap) }
                            item { Section("YOUR EMPIRE", "${state.businesses.sumOf { it.level }} total assets") }
                            items(visibleBusinesses, key = { it.id }) { b -> JuicyBusinessCard(b, state) { vm.buy(b.id) } }
                            ContentUnlocks.nextHiddenBusiness(state)?.let { next -> item { NextAssetUnlockCard(state, next) } }
                            item { PrestigeCard(state, vm::prestige) }
                        }
                        GameTab.MANAGERS -> {
                            item { Section("MANAGERS", "Recruit, automate and master every revealed asset") }
                            items(visibleManagers, key = { it.businessId }) { m -> ManagerCard(m, state) { vm.hireManager(m.businessId) } }
                            ContentUnlocks.nextHiddenBusiness(state)?.let { next -> item { NextManagerUnlockCard(state, next) } }
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
}

@Composable
private fun JuicyPowerTap(s: GameState, tap: () -> Unit) {
    val haptics = LocalHapticFeedback.current
    val scope = rememberCoroutineScope()
    val scale = remember { Animatable(1f) }
    var burst by remember { mutableStateOf(false) }
    var displayedGain by remember { mutableStateOf(0.0) }
    Box(Modifier.fillMaxWidth().height(226.dp), contentAlignment = Alignment.Center) {
        Surface(modifier = Modifier.size(184.dp).scale(scale.value).pointerInput(s.tapValue) { detectTapGestures(onPress = {
            scale.animateTo(.92f, spring(stiffness = Spring.StiffnessHigh))
            if (tryAwaitRelease()) { displayedGain = s.tapValue; tap(); haptics.performHapticFeedback(HapticFeedbackType.TextHandleMove); burst = true
                scope.launch { scale.animateTo(1.06f, spring(dampingRatio = .42f, stiffness = Spring.StiffnessMedium)); scale.animateTo(1f, spring(dampingRatio = .55f)) }
                scope.launch { delay(520); burst = false }
            } else scale.snapTo(1f)
        }) }, shape = CircleShape, color = EmpireColors.SurfaceHigh, shadowElevation = 24.dp) {
            Box(Modifier.background(Brush.radialGradient(listOf(EmpireColors.Gold.copy(alpha = .35f), EmpireColors.SurfaceHigh, EmpireColors.Void))), contentAlignment = Alignment.Center) {
                EmpireCoreGlyph(Modifier.size(142.dp))
                Column(modifier = Modifier.align(Alignment.BottomCenter).padding(bottom = 18.dp), horizontalAlignment = Alignment.CenterHorizontally) {
                    Text("POWER CORE", color = EmpireColors.GoldBright, fontWeight = FontWeight.Black, fontSize = 11.sp)
                    Text("+${money(s.tapValue)}", color = EmpireColors.TextPrimary, fontWeight = FontWeight.Black, fontSize = 12.sp)
                }
            }
        }
        AnimatedVisibility(visible = burst, enter = fadeIn() + scaleIn(initialScale = .65f), exit = fadeOut() + scaleOut(targetScale = 1.25f), modifier = Modifier.align(Alignment.TopCenter).padding(top = 4.dp)) {
            Text("+${money(displayedGain)}", color = EmpireColors.GoldBright, fontWeight = FontWeight.Black, fontSize = 20.sp)
        }
    }
}

@Composable
private fun JuicyBusinessCard(b: Business, s: GameState, buy: () -> Unit) {
    val haptics = LocalHapticFeedback.current
    val affordable = s.cash >= b.nextCost
    var lastLevel by remember(b.id) { mutableIntStateOf(b.level) }
    var milestoneFlash by remember(b.id) { mutableStateOf(false) }
    val milestone = b.nextMilestone ?: ((b.level / 1000) + 1) * 1000
    val progress = (b.level.toFloat() / milestone).coerceIn(0f, 1f)
    LaunchedEffect(b.level) { if (b.level > lastLevel) { if (b.level in listOf(10,25,50,100,250,500,1000)) { milestoneFlash=true; haptics.performHapticFeedback(HapticFeedbackType.LongPress); delay(900); milestoneFlash=false }; lastLevel=b.level } }
    Surface(color = if (milestoneFlash) EmpireColors.Gold.copy(alpha=.20f) else EmpireColors.Surface.copy(alpha=.94f), shape=RoundedCornerShape(18.dp), modifier=Modifier.fillMaxWidth().clickable(enabled=affordable){buy();haptics.performHapticFeedback(HapticFeedbackType.TextHandleMove)}) {
        Column(Modifier.padding(14.dp)) { Row(verticalAlignment=Alignment.CenterVertically){ BusinessArtIcon(b.id,50.dp);Spacer(Modifier.width(11.dp));Column(Modifier.weight(1f)){Text(b.name,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Bold);Text("LV ${b.level} • ${money(s.businessIncome(b))}/s",color=EmpireColors.Cyan,fontSize=11.sp)};Text(money(b.nextCost),color=if(affordable)EmpireColors.Gold else EmpireColors.TextSecondary,fontWeight=FontWeight.Bold)};Spacer(Modifier.height(8.dp));LinearProgressIndicator(progress={progress},modifier=Modifier.fillMaxWidth().height(4.dp),color=EmpireColors.Gold,trackColor=EmpireColors.SurfaceHigh);Text(if(milestoneFlash)"POWER SPIKE UNLOCKED ×${GameEconomy.milestoneMultiplier(b.level)}" else "NEXT POWER SPIKE • LV $milestone",color=if(milestoneFlash)EmpireColors.GoldBright else EmpireColors.TextSecondary,fontSize=9.sp,fontWeight=if(milestoneFlash)FontWeight.Black else FontWeight.Normal)}
    }
}

@Composable private fun NextAssetUnlockCard(state:GameState,next:Business){val threshold=ContentUnlocks.thresholdForBusiness(next.id);val progress=ContentUnlocks.progressToNextUnlock(state);Surface(color=EmpireColors.Surface.copy(alpha=.72f),shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(14.dp)){Row(verticalAlignment=Alignment.CenterVertically){Surface(shape=RoundedCornerShape(14.dp),color=EmpireColors.Void,modifier=Modifier.size(50.dp)){Box(contentAlignment=Alignment.Center){Text("?",color=EmpireColors.Violet,fontSize=25.sp,fontWeight=FontWeight.Black)}};Spacer(Modifier.width(11.dp));Column(Modifier.weight(1f)){Text("CLASSIFIED ASSET",color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Text("Next economic class reveals at ${money(threshold)} lifetime capital",color=EmpireColors.TextSecondary,fontSize=10.sp)}};Spacer(Modifier.height(9.dp));LinearProgressIndicator(progress={progress},modifier=Modifier.fillMaxWidth().height(4.dp),color=EmpireColors.Violet,trackColor=EmpireColors.SurfaceHigh)}}}
@Composable private fun NextManagerUnlockCard(state:GameState,next:Business){val threshold=ContentUnlocks.thresholdForBusiness(next.id);Surface(color=EmpireColors.Violet.copy(alpha=.08f),shape=RoundedCornerShape(16.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(14.dp),verticalAlignment=Alignment.CenterVertically){Text("◇",color=EmpireColors.Violet,fontSize=26.sp);Spacer(Modifier.width(10.dp));Column{Text("NEXT EXECUTIVE CLASSIFIED",color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black,fontSize=12.sp);Text("Reveals with the next asset at ${money(threshold)} lifetime capital",color=EmpireColors.TextSecondary,fontSize=10.sp)}}}}
@Composable private fun DailyRewardCard(meta:PlayerMeta,claimable:Boolean,claim:()->RewardDay?){val h=LocalHapticFeedback.current;val next=LoginCalendar.rewardFor(meta.streakDays+1);Surface(color=EmpireColors.Gold.copy(alpha=.13f),shape=RoundedCornerShape(20.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(18.dp)){Text("DAILY CAPITAL DROP",color=EmpireColors.Gold,fontWeight=FontWeight.Black,fontSize=18.sp);Text("STREAK ${meta.streakDays} DAYS",color=EmpireColors.TextSecondary,fontSize=11.sp);Spacer(Modifier.height(8.dp));Text("Next reward: ◆ ${next.gems}${if(next.multiplierMinutes>0)" + ×2 for ${next.multiplierMinutes}m" else ""}",color=EmpireColors.TextPrimary,fontWeight=FontWeight.Bold);Spacer(Modifier.height(10.dp));Button(onClick={if(claim()!=null)h.performHapticFeedback(HapticFeedbackType.LongPress)},enabled=claimable,modifier=Modifier.fillMaxWidth()){Text(if(claimable)"CLAIM DAILY REWARD" else "CLAIMED TODAY",fontWeight=FontWeight.Black)}}}}
@Composable private fun MissionCard(m:Mission,claim:()->Unit){val h=LocalHapticFeedback.current;Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(16.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(14.dp)){Row(verticalAlignment=Alignment.CenterVertically){Column(Modifier.weight(1f)){Text(m.title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Bold);Text("◆ ${m.rewardGems} reward",color=EmpireColors.Violet,fontSize=11.sp)};Button(onClick={claim();h.performHapticFeedback(HapticFeedbackType.LongPress)},enabled=m.completed&&!m.claimed){Text(if(m.claimed)"DONE" else if(m.completed)"CLAIM" else "${(m.fraction*100).toInt()}%",fontSize=10.sp)}};Spacer(Modifier.height(7.dp));LinearProgressIndicator(progress={m.fraction},modifier=Modifier.fillMaxWidth().height(4.dp),color=EmpireColors.Cyan,trackColor=EmpireColors.SurfaceHigh)}}}
@Composable private fun AchievementCard(a:Achievement,claim:()->Unit){val h=LocalHapticFeedback.current;Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(16.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(14.dp),verticalAlignment=Alignment.CenterVertically){Text(if(a.unlocked)"★" else "☆",color=if(a.unlocked)EmpireColors.Gold else EmpireColors.TextSecondary,fontSize=28.sp);Spacer(Modifier.width(10.dp));Column(Modifier.weight(1f)){Text(a.title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Text(a.description,color=EmpireColors.TextSecondary,fontSize=11.sp)};Button(onClick={claim();h.performHapticFeedback(HapticFeedbackType.LongPress)},enabled=a.unlocked&&!a.claimed){Text(if(a.claimed)"DONE" else "◆ ${a.rewardGems}",fontSize=10.sp)}}}}

@Composable private fun OfflineRewardDialog(reward:OfflineReward,dismiss:()->Unit,doubleReward:()->Unit){val h=LocalHapticFeedback.current;val hours=reward.paidSeconds/3600;val minutes=(reward.paidSeconds%3600)/60;AlertDialog(onDismissRequest=dismiss,containerColor=EmpireColors.SurfaceHigh,title={Text("EMPIRE NEVER SLEEPS",color=EmpireColors.Gold,fontWeight=FontWeight.Black)},text={Column(horizontalAlignment=Alignment.CenterHorizontally,modifier=Modifier.fillMaxWidth()){Text("Your managers kept the machine running while you were away.",color=EmpireColors.TextSecondary,textAlign=TextAlign.Center);Spacer(Modifier.height(18.dp));Text("+${money(reward.cash)}",color=EmpireColors.Success,fontSize=34.sp,fontWeight=FontWeight.Black);Text("$hours h ${minutes} min of offline production",color=EmpireColors.TextSecondary,fontSize=12.sp);Spacer(Modifier.height(10.dp));Text("75% OFFLINE EFFICIENCY",color=EmpireColors.Cyan,fontSize=10.sp,fontWeight=FontWeight.Bold)}},confirmButton={Column(Modifier.fillMaxWidth(),verticalArrangement=Arrangement.spacedBy(8.dp)){Button(onClick={doubleReward();h.performHapticFeedback(HapticFeedbackType.LongPress)},modifier=Modifier.fillMaxWidth()){Text("▶ WATCH AD • DOUBLE TO ${money(reward.cash*2)}",fontWeight=FontWeight.Black,fontSize=11.sp)};TextButton(onClick={dismiss();h.performHapticFeedback(HapticFeedbackType.LongPress)},modifier=Modifier.fillMaxWidth()){Text("COLLECT ${money(reward.cash)}")}}})}

@Composable private fun GameNav(selected:GameTab,onSelect:(GameTab)->Unit){NavigationBar(containerColor=EmpireColors.Surface){GameTab.entries.forEach{tab->NavigationBarItem(selected=tab==selected,onClick={onSelect(tab)},icon={Text(when(tab){GameTab.EMPIRE->"◈";GameTab.MANAGERS->"♟";GameTab.UPGRADES->"◆";GameTab.GOALS->"★"})},label={Text(tab.name)})}}}
@Composable private fun Header(s:GameState){Row(Modifier.fillMaxWidth().padding(top=16.dp),verticalAlignment=Alignment.CenterVertically){Column(Modifier.weight(1f)){Text("ZERO → EMPIRE",color=EmpireColors.Gold,fontWeight=FontWeight.Black,fontSize=23.sp);Text("FROM NOTHING. BEYOND EVERYTHING.",color=EmpireColors.TextSecondary,fontSize=9.sp)};Text("◆ ${s.gems}   ◇ ${s.prestigePoints}",color=EmpireColors.Violet,fontWeight=FontWeight.Bold)}}
@Composable private fun EventBanner(e:LiveEvent){Surface(color=EmpireColors.Violet.copy(alpha=.16f),shape=RoundedCornerShape(15.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(13.dp),verticalAlignment=Alignment.CenterVertically){Text(e.icon,fontSize=25.sp);Spacer(Modifier.width(10.dp));Column{Text(e.name.uppercase(),color=EmpireColors.Violet,fontWeight=FontWeight.Black);Text("${e.description}  ×${e.incomeMultiplier}",color=EmpireColors.TextSecondary,fontSize=11.sp)}}}}
@Composable private fun WealthHero(s:GameState){Surface(shape=RoundedCornerShape(24.dp),color=EmpireColors.SurfaceHigh.copy(alpha=.92f),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(20.dp)){Text("NET WORTH",color=EmpireColors.TextSecondary,fontSize=10.sp);Text(money(s.cash),color=EmpireColors.TextPrimary,fontSize=39.sp,fontWeight=FontWeight.Black);Text("▲ ${money(s.incomePerSecond)} / SEC   ×${String.format(Locale.US,"%.1f",s.prestigeMultiplier)} LEGACY",color=EmpireColors.Success,fontWeight=FontWeight.Bold,fontSize=12.sp)}}}
@Composable private fun EraVistaCard(s:GameState){val era=EmpireEras.current(s.lifetimeCash);Surface(shape=RoundedCornerShape(20.dp),color=EmpireColors.Surface.copy(alpha=.88f),modifier=Modifier.fillMaxWidth().height(132.dp)){Box(Modifier.fillMaxSize()){EraVista(era.index,Modifier.fillMaxSize());Column(Modifier.fillMaxSize().background(Brush.verticalGradient(listOf(EmpireColors.Void.copy(alpha=.06f),EmpireColors.Void.copy(alpha=.86f)))).padding(15.dp),verticalArrangement=Arrangement.Bottom){Text("ERA ${era.index+1}",color=EmpireColors.Cyan,fontSize=9.sp,fontWeight=FontWeight.Black,letterSpacing=1.5.sp);Text(era.name,color=EmpireColors.TextPrimary,fontSize=19.sp,fontWeight=FontWeight.Black);Text(era.subtitle,color=EmpireColors.TextSecondary,fontSize=11.sp)}}}}
@Composable private fun Section(title:String,subtitle:String){Column(Modifier.padding(top=8.dp)){Text(title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black,fontSize=19.sp);Text(subtitle,color=EmpireColors.TextSecondary,fontSize=11.sp)}}

private enum class ManagerVisualState { LOCKED, RECRUIT, HIRED, MASTERED }
private fun managerVisualState(m:Manager,s:GameState):ManagerVisualState { val hired=m.businessId in s.hiredManagerIds; val level=s.businesses.firstOrNull{it.id==m.businessId}?.level?:0; return when { hired&&level>=100->ManagerVisualState.MASTERED; hired->ManagerVisualState.HIRED; s.cash>=m.cost->ManagerVisualState.RECRUIT; else->ManagerVisualState.LOCKED } }
@Composable private fun ManagerCard(m:Manager,s:GameState,hire:()->Unit){
    val h=LocalHapticFeedback.current;val state=managerVisualState(m,s);val canHire=state==ManagerVisualState.RECRUIT
    val accent=when(state){ManagerVisualState.LOCKED->EmpireColors.TextSecondary;ManagerVisualState.RECRUIT->EmpireColors.Gold;ManagerVisualState.HIRED->EmpireColors.Cyan;ManagerVisualState.MASTERED->EmpireColors.GoldBright}
    val badge=when(state){ManagerVisualState.LOCKED->"LOCKED";ManagerVisualState.RECRUIT->"RECRUIT";ManagerVisualState.HIRED->"HIRED";ManagerVisualState.MASTERED->"MASTERED"}
    val detail=when(state){ManagerVisualState.LOCKED->"Need ${money(m.cost-s.cash)} more capital";ManagerVisualState.RECRUIT->"Executive ready • ${money(m.cost)}";ManagerVisualState.HIRED->"Automation online";ManagerVisualState.MASTERED->"Elite automation • asset LV 100+"}
    Surface(color=if(state==ManagerVisualState.MASTERED)EmpireColors.Gold.copy(alpha=.11f) else EmpireColors.Surface.copy(alpha=.95f),shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth().border(1.dp,accent.copy(alpha=.38f),RoundedCornerShape(18.dp))){
        Row(Modifier.padding(15.dp),verticalAlignment=Alignment.CenterVertically){
            Box(contentAlignment=Alignment.Center){ManagerPortrait(m.businessId,56.dp);if(state==ManagerVisualState.LOCKED)Box(Modifier.size(56.dp).alpha(.68f).background(EmpireColors.Void,RoundedCornerShape(18.dp)),contentAlignment=Alignment.Center){Text("⌾",color=EmpireColors.TextSecondary,fontSize=23.sp,fontWeight=FontWeight.Black)};if(state==ManagerVisualState.MASTERED)Text("★",color=EmpireColors.GoldBright,fontSize=15.sp,modifier=Modifier.align(Alignment.TopEnd))}
            Spacer(Modifier.width(12.dp));Column(Modifier.weight(1f)){Row(verticalAlignment=Alignment.CenterVertically){Text(m.name,color=if(state==ManagerVisualState.LOCKED)EmpireColors.TextSecondary else EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Spacer(Modifier.width(7.dp));Surface(color=accent.copy(alpha=.14f),shape=RoundedCornerShape(50)){Text(badge,color=accent,fontSize=8.sp,fontWeight=FontWeight.Black,modifier=Modifier.padding(horizontal=7.dp,vertical=3.dp))}};Text(m.title,color=EmpireColors.TextSecondary,fontSize=11.sp);Text("×${m.incomeMultiplier} production",color=if(state==ManagerVisualState.LOCKED)EmpireColors.TextSecondary else EmpireColors.Success,fontSize=11.sp,fontWeight=FontWeight.Bold);Text(detail,color=accent,fontSize=9.sp)}
            Button(onClick={hire();h.performHapticFeedback(HapticFeedbackType.LongPress)},enabled=canHire){Text(when(state){ManagerVisualState.LOCKED->"LOCKED";ManagerVisualState.RECRUIT->"HIRE";ManagerVisualState.HIRED->"ACTIVE";ManagerVisualState.MASTERED->"MAX"},fontSize=9.sp,fontWeight=FontWeight.Black)}
        }
    }
}
@Composable private fun UpgradeCard(u:Upgrade,s:GameState,buy:()->Unit){val h=LocalHapticFeedback.current;val rank=s.upgradeRanks[u.id]?:0;val maxed=rank>=u.maxRank;Surface(color=EmpireColors.Surface,shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(15.dp),verticalAlignment=Alignment.CenterVertically){Column(Modifier.weight(1f)){Text(u.name,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black);Text(u.description,color=EmpireColors.TextSecondary,fontSize=11.sp);Text("RANK $rank / ${u.maxRank}",color=EmpireColors.Cyan,fontSize=10.sp)};Button(onClick={buy();h.performHapticFeedback(HapticFeedbackType.LongPress)},enabled=!maxed&&s.gems>=u.gemCost){Text(if(maxed)"MAX" else "◆ ${u.gemCost}")}}}}
@Composable private fun BoostCard(s:GameState,boost:()->Unit){val h=LocalHapticFeedback.current;val active=System.currentTimeMillis()<s.boostEndsAtMillis;Surface(color=EmpireColors.Gold.copy(alpha=.12f),shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(16.dp)){Text("PROFIT OVERDRIVE",color=EmpireColors.Gold,fontWeight=FontWeight.Black);Text("Double all income for 10 minutes.",color=EmpireColors.TextSecondary,fontSize=11.sp);Spacer(Modifier.height(8.dp));Button(onClick={boost();h.performHapticFeedback(HapticFeedbackType.LongPress)},enabled=!active){Text(if(active)"BOOST ACTIVE ×2" else "ACTIVATE ×2 BOOST")}}}}
@Composable private fun PrestigeCard(s:GameState,prestige:()->Unit){val h=LocalHapticFeedback.current;val reward=(Progression.prestigeReward(s.lifetimeCash)-s.prestigePoints).coerceAtLeast(0);Surface(color=EmpireColors.SurfaceHigh,shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(19.dp),horizontalAlignment=Alignment.CenterHorizontally){Text("ASCENSION",color=EmpireColors.Violet,fontWeight=FontWeight.Black,fontSize=20.sp);Text("Reset this empire for permanent legacy power.",color=EmpireColors.TextSecondary,textAlign=TextAlign.Center,fontSize=11.sp);Text("+$reward LEGACY",color=EmpireColors.Gold,fontWeight=FontWeight.Black,fontSize=17.sp);Button(onClick={prestige();h.performHapticFeedback(HapticFeedbackType.LongPress)},enabled=reward>0,modifier=Modifier.fillMaxWidth()){Text("TRANSCEND")}}}}
private fun money(value:Double):String=EmpireNumberFormat.money(value)
