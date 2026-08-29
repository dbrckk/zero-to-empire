package com.zerotoempire.game

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.animateColorAsState
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.spring
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.scaleIn
import androidx.compose.animation.scaleOut
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

private enum class PremiumTab(val label: String, val glyph: String) {
    EMPIRE("EMPIRE", "◉"), MANAGERS("MANAGERS", "◇"), UPGRADES("UPGRADES", "⬡"), GOALS("GOALS", "★")
}

@Composable
fun PremiumZeroToEmpireApp(vm: GameViewModel) {
    val state by vm.state.collectAsStateWithLifecycle()
    val meta by vm.meta.collectAsStateWithLifecycle()
    val buyMode by vm.buyMode.collectAsStateWithLifecycle()
    var tab by remember { mutableStateOf(PremiumTab.EMPIRE) }
    val era = EmpireEras.current(state.lifetimeCash)
    MaterialTheme(colorScheme = EmpireColorScheme) {
        Scaffold(containerColor = EmpireColors.Void, bottomBar = { PremiumNav(tab) { tab = it } }) { padding ->
            Box(Modifier.fillMaxSize().padding(padding)) {
                EmpireAmbientBackdrop(era.index, Modifier.fillMaxSize())
                when (tab) {
                    PremiumTab.EMPIRE -> PremiumEmpireTab(vm, state, buyMode)
                    PremiumTab.MANAGERS -> PremiumManagersTab(vm, state)
                    PremiumTab.UPGRADES -> PremiumUpgradesTab(vm, state)
                    PremiumTab.GOALS -> PremiumGoalsTab(vm, state, meta)
                }
            }
        }
    }
}

@Composable
private fun PremiumEmpireTab(vm: GameViewModel, state: GameState, buyMode: BuyMode) {
    val visible = remember(state.businesses, state.lifetimeCash) { ContentUnlocks.visibleBusinesses(state) }
    var previousEra by remember { mutableIntStateOf(state.empireLevel) }
    var eraReveal by remember { mutableStateOf(false) }
    LaunchedEffect(state.empireLevel) {
        if (state.empireLevel > previousEra) {
            previousEra = state.empireLevel
            eraReveal = true
            delay(1800)
            eraReveal = false
        } else previousEra = state.empireLevel
    }
    Box(Modifier.fillMaxSize()) {
        LazyColumn(Modifier.fillMaxSize(), contentPadding = PaddingValues(16.dp,14.dp,16.dp,30.dp), verticalArrangement = Arrangement.spacedBy(13.dp)) {
            item { PremiumTopStatus(state) }
            item { PremiumEmpireSignal(state) }
            item { CinematicEraHero(state) }
            item { PremiumCampaignPulse(state) }
            item { PremiumPowerCore(state, vm::tap) }
            item { PurchaseModeRail(vm, buyMode) }
            item { PremiumSectionTitle("ASSET NETWORK", "${state.businesses.sumOf { it.level }} levels online") }
            items(visible, key = { it.id }) { PremiumBusinessCard(vm, it, state, buyMode) }
            ContentUnlocks.nextHiddenBusiness(state)?.let { item { PremiumLockedAsset(state, it) } }
            item { PremiumAscensionCard(vm, state) }
        }
        AnimatedVisibility(eraReveal, enter=fadeIn()+scaleIn(initialScale=.86f), exit=fadeOut()+scaleOut(targetScale=1.08f), modifier=Modifier.align(Alignment.Center)) {
            val era=EmpireEras.current(state.lifetimeCash)
            Surface(color=EmpireColors.DeepSpace.copy(alpha=.96f),shape=RoundedCornerShape(28.dp),modifier=Modifier.padding(28.dp).border(1.dp,EmpireColors.Gold.copy(alpha=.55f),RoundedCornerShape(28.dp))){
                Column(Modifier.padding(horizontal=28.dp,vertical=24.dp),horizontalAlignment=Alignment.CenterHorizontally){Text("NEW ERA",color=EmpireColors.Gold,fontSize=11.sp,fontWeight=FontWeight.Black,letterSpacing=2.4.sp);Text(era.name.uppercase(),color=EmpireColors.TextPrimary,fontSize=25.sp,fontWeight=FontWeight.Black);Text("Empire evolution unlocked",color=EmpireColors.Cyan,fontSize=11.sp,fontWeight=FontWeight.Bold)}
            }
        }
    }
}

@Composable
private fun PremiumTopStatus(state: GameState) {
    Surface(color=EmpireColors.Surface.copy(alpha=.82f),shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth().border(1.dp,Color.White.copy(alpha=.06f),RoundedCornerShape(22.dp))) {
        Row(Modifier.padding(horizontal=16.dp,vertical=13.dp),verticalAlignment=Alignment.CenterVertically) {
            Column(Modifier.weight(1f)) { Text("NET WORTH",color=EmpireColors.TextSecondary,fontSize=10.sp,fontWeight=FontWeight.Bold,letterSpacing=1.4.sp);Text(moneyV2(state.cash),color=EmpireColors.TextPrimary,fontSize=30.sp,fontWeight=FontWeight.Black) }
            Column(horizontalAlignment=Alignment.End) { Text("+${moneyV2(state.incomePerSecond)}/S",color=EmpireColors.Success,fontSize=14.sp,fontWeight=FontWeight.Black);Text("LEGACY ×${String.format("%.2f",state.prestigeMultiplier)}",color=EmpireColors.Gold,fontSize=10.sp,fontWeight=FontWeight.Bold) }
        }
    }
}

@Composable
private fun CinematicEraHero(state: GameState) {
    val era=EmpireEras.current(state.lifetimeCash)
    Surface(color=Color.Transparent,shape=RoundedCornerShape(28.dp),modifier=Modifier.fillMaxWidth().height(218.dp).border(1.dp,EmpireColors.Cyan.copy(alpha=.16f),RoundedCornerShape(28.dp))) {
        Box(Modifier.background(Brush.verticalGradient(listOf(EmpireColors.SurfaceHigh.copy(alpha=.72f),EmpireColors.DeepSpace.copy(alpha=.94f),EmpireColors.Void.copy(alpha=.98f))))) {
            EraVistaAAA(era.index,Modifier.fillMaxSize());Box(Modifier.fillMaxSize().background(Brush.verticalGradient(listOf(Color.Transparent,EmpireColors.Void.copy(alpha=.88f)))))
            Column(Modifier.align(Alignment.BottomStart).padding(18.dp)) { Text("ERA ${era.index+1}",color=EmpireColors.Cyan,fontSize=10.sp,fontWeight=FontWeight.Black,letterSpacing=1.8.sp);Text(era.name.uppercase(),color=EmpireColors.TextPrimary,fontSize=25.sp,fontWeight=FontWeight.Black);Text("Lifetime capital ${moneyV2(state.lifetimeCash)}",color=EmpireColors.TextSecondary,fontSize=11.sp) }
        }
    }
}

@Composable
private fun PremiumPowerCore(state: GameState,tap:()->Unit) {
    val haptic=LocalHapticFeedback.current;val scope=rememberCoroutineScope();val scale=remember{Animatable(1f)};var pop by remember{mutableStateOf(false)};var lastGain by remember{mutableDoubleStateOf(0.0)};var combo by remember{mutableIntStateOf(0)};var comboToken by remember{mutableIntStateOf(0)};var impactSerial by remember{mutableIntStateOf(0)};val eraIndex=EmpireEras.current(state.lifetimeCash).index
    Surface(color=EmpireColors.Surface.copy(alpha=.70f),shape=RoundedCornerShape(30.dp),modifier=Modifier.fillMaxWidth().border(1.dp,EmpireColors.Gold.copy(alpha=.15f),RoundedCornerShape(30.dp))) {
        Column(Modifier.padding(vertical=18.dp),horizontalAlignment=Alignment.CenterHorizontally) {
            Text("POWER CORE",color=EmpireColors.Gold,fontSize=11.sp,fontWeight=FontWeight.Black,letterSpacing=2.sp);Text("Tap to inject capital",color=EmpireColors.TextSecondary,fontSize=10.sp);Spacer(Modifier.height(8.dp))
            Box(Modifier.height(206.dp).fillMaxWidth(),contentAlignment=Alignment.Center) {
                PremiumCoreAura(eraIndex, Modifier.size(190.dp))
                PowerCoreTapImpact(impactSerial,eraIndex,Modifier.size(202.dp))
                Box(Modifier.size(188.dp).scale(scale.value).background(Brush.radialGradient(listOf(EmpireColors.Gold.copy(alpha=.16f),EmpireColors.Cyan.copy(alpha=.06f),Color.Transparent)),CircleShape).pointerInput(state.tapValue) { detectTapGestures(onPress={scale.animateTo(.93f,spring(stiffness=Spring.StiffnessHigh));if(tryAwaitRelease()){lastGain=state.tapValue;tap();impactSerial++;combo=(combo+1).coerceAtMost(99);comboToken++;haptic.performHapticFeedback(HapticFeedbackType.TextHandleMove);pop=true;scope.launch{scale.animateTo(1.08f,spring(dampingRatio=.38f,stiffness=Spring.StiffnessMedium));scale.animateTo(1f,spring(dampingRatio=.55f))};scope.launch{delay(430);pop=false};val token=comboToken;scope.launch{delay(900);if(token==comboToken)combo=0}}else scale.snapTo(1f)}) },contentAlignment=Alignment.Center) { EmpireCoreGlyph(Modifier.size(166.dp),eraIndex=eraIndex) }
                if(pop) Text("+${moneyV2(lastGain)}",color=EmpireColors.GoldBright,fontSize=22.sp,fontWeight=FontWeight.Black,modifier=Modifier.align(Alignment.TopCenter));if(combo>=3) Text("CHAIN ×$combo",color=EmpireColors.Cyan,fontSize=10.sp,fontWeight=FontWeight.Black,letterSpacing=1.2.sp,modifier=Modifier.align(Alignment.BottomCenter))
            }
            Text("+${moneyV2(state.tapValue)} PER TAP",color=EmpireColors.TextPrimary,fontSize=13.sp,fontWeight=FontWeight.Black)
        }
    }
}

@Composable
private fun PurchaseModeRail(vm:GameViewModel,selected:BuyMode){val modes=listOf(BuyMode.X1 to "×1",BuyMode.X10 to "×10",BuyMode.X25 to "×25",BuyMode.MILESTONE to "NEXT",BuyMode.MAX to "MAX");Surface(color=EmpireColors.Surface.copy(alpha=.86f),shape=RoundedCornerShape(18.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(6.dp),horizontalArrangement=Arrangement.spacedBy(4.dp)){modes.forEach{(mode,label)->val active=mode==selected;Surface(color=if(active)EmpireColors.Violet.copy(alpha=.90f)else Color.Transparent,shape=RoundedCornerShape(13.dp),modifier=Modifier.weight(1f).height(42.dp).clickable{vm.setBuyMode(mode)}){Box(contentAlignment=Alignment.Center){Text(label,color=if(active)Color.White else EmpireColors.TextSecondary,fontSize=10.sp,fontWeight=FontWeight.Black)}}}}}}

@Composable
private fun PremiumBusinessCard(vm:GameViewModel,business:Business,state:GameState,mode:BuyMode){
    val quote=vm.bulkQuote(business.id,mode);val affordable=quote.count>0&&state.cash>=quote.cost;val target=business.nextMilestone?:((business.level/1000)+1)*1000;val previous=listOf(0,10,25,50,100,250,500,1000).lastOrNull{it<=business.level}?:0;val progress=((business.level-previous).toFloat()/(target-previous).coerceAtLeast(1)).coerceIn(0f,1f);val borderColor by animateColorAsState(if(affordable)EmpireColors.Gold.copy(alpha=.34f)else Color.White.copy(alpha=.06f),label="assetBorder");val haptic=LocalHapticFeedback.current;var pulse by remember{mutableStateOf(false)};var oldLevel by remember{mutableIntStateOf(business.level)}
    LaunchedEffect(business.level){val crossed=business.level>oldLevel&&listOf(10,25,50,100,250,500,1000).any{it in (oldLevel+1)..business.level};oldLevel=business.level;if(crossed){pulse=true;haptic.performHapticFeedback(HapticFeedbackType.LongPress);delay(900);pulse=false}}
    Surface(color=if(pulse)EmpireColors.Gold.copy(alpha=.13f)else EmpireColors.Surface.copy(alpha=.94f),shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth().border(if(pulse)2.dp else 1.dp,if(pulse)EmpireColors.GoldBright else borderColor,RoundedCornerShape(22.dp)).clickable(enabled=affordable){vm.buyBulk(business.id,mode);haptic.performHapticFeedback(HapticFeedbackType.TextHandleMove)}){
        Column(Modifier.padding(14.dp)){if(pulse){Text("POWER SPIKE UNLOCKED",color=EmpireColors.GoldBright,fontSize=9.sp,fontWeight=FontWeight.Black,letterSpacing=1.3.sp);Spacer(Modifier.height(6.dp))};Row(verticalAlignment=Alignment.CenterVertically){BusinessArtIcon(business.id,business.level,64.dp);Spacer(Modifier.width(12.dp));Column(Modifier.weight(1f)){Text(business.name,color=EmpireColors.TextPrimary,fontSize=17.sp,fontWeight=FontWeight.Black,maxLines=1,overflow=TextOverflow.Ellipsis);Text("LEVEL ${business.level}",color=EmpireColors.TextSecondary,fontSize=9.sp,fontWeight=FontWeight.Bold,letterSpacing=1.sp);Text("${moneyV2(state.businessIncome(business)*state.permanentIncomeMultiplier*state.boostMultiplier*state.eventMultiplier)}/S",color=EmpireColors.Cyan,fontSize=12.sp,fontWeight=FontWeight.Black)};Column(horizontalAlignment=Alignment.End){Text(if(quote.count>0)"+${quote.count}" else "—",color=if(affordable)EmpireColors.GoldBright else EmpireColors.TextSecondary,fontSize=14.sp,fontWeight=FontWeight.Black);Text(if(quote.count>0)moneyV2(quote.cost)else "NOT ENOUGH",color=if(affordable)EmpireColors.Gold else EmpireColors.TextSecondary,fontSize=10.sp,fontWeight=FontWeight.Bold)}};Spacer(Modifier.height(11.dp));LinearProgressIndicator(progress={progress},modifier=Modifier.fillMaxWidth().height(5.dp),color=if(pulse)EmpireColors.GoldBright else EmpireColors.Gold,trackColor=EmpireColors.SurfaceHigh);Spacer(Modifier.height(6.dp));Row(Modifier.fillMaxWidth()){Text("POWER SPIKE",color=EmpireColors.TextSecondary,fontSize=9.sp,fontWeight=FontWeight.Bold);Spacer(Modifier.weight(1f));Text("LV $target",color=EmpireColors.Gold,fontSize=9.sp,fontWeight=FontWeight.Black)}}
    }
}

@Composable private fun PremiumLockedAsset(state:GameState,next:Business){val threshold=ContentUnlocks.thresholdForBusiness(next.id);val progress=ContentUnlocks.progressToNextUnlock(state);Surface(color=EmpireColors.Surface.copy(alpha=.58f),shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(16.dp)){Text("NEXT ASSET CLASSIFIED",color=EmpireColors.Violet,fontSize=10.sp,fontWeight=FontWeight.Black,letterSpacing=1.5.sp);Spacer(Modifier.height(4.dp));Text("Unlock at ${moneyV2(threshold)} lifetime capital",color=EmpireColors.TextPrimary,fontSize=13.sp,fontWeight=FontWeight.Bold);Spacer(Modifier.height(9.dp));LinearProgressIndicator(progress={progress},modifier=Modifier.fillMaxWidth().height(5.dp),color=EmpireColors.Violet,trackColor=EmpireColors.SurfaceHigh)}}}
@Composable private fun PremiumAscensionCard(vm:GameViewModel,state:GameState){val targetPoints=Progression.prestigeReward(state.lifetimeCash);val gain=(targetPoints-state.prestigePoints).coerceAtLeast(0);Surface(color=EmpireColors.Gold.copy(alpha=.09f),shape=RoundedCornerShape(26.dp),modifier=Modifier.fillMaxWidth().border(1.dp,EmpireColors.Gold.copy(alpha=.20f),RoundedCornerShape(26.dp))){Column(Modifier.padding(18.dp)){Text("ASCENSION",color=EmpireColors.Gold,fontSize=10.sp,fontWeight=FontWeight.Black,letterSpacing=2.sp);Text("Rebuild. Return stronger.",color=EmpireColors.TextPrimary,fontSize=21.sp,fontWeight=FontWeight.Black);Text("Current Legacy ×${String.format("%.2f",state.prestigeMultiplier)}  •  Next +$gain points",color=EmpireColors.TextSecondary,fontSize=11.sp);Spacer(Modifier.height(12.dp));Button(onClick=vm::prestige,enabled=gain>0,modifier=Modifier.fillMaxWidth().height(48.dp),shape=RoundedCornerShape(15.dp),colors=ButtonDefaults.buttonColors(containerColor=EmpireColors.Gold,contentColor=EmpireColors.Void)){Text(if(gain>0)"ASCEND  +$gain LEGACY" else "BUILD MORE CAPITAL",fontWeight=FontWeight.Black)}}}}
@Composable private fun PremiumManagersTab(vm:GameViewModel,state:GameState){val visible=remember(state.hiredManagerIds,state.lifetimeCash){ContentUnlocks.visibleManagers(state)};PremiumListShell("EXECUTIVE NETWORK","Managers automate offline production"){items(visible,key={it.businessId}){manager->val hired=manager.businessId in state.hiredManagerIds;val canHire=!hired&&state.cash>=manager.cost;Surface(color=EmpireColors.Surface.copy(alpha=.92f),shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(15.dp),verticalAlignment=Alignment.CenterVertically){ManagerPortrait(manager.businessId,62.dp);Spacer(Modifier.width(12.dp));Column(Modifier.weight(1f)){Text(manager.name,color=EmpireColors.TextPrimary,fontSize=17.sp,fontWeight=FontWeight.Black);Text(manager.title,color=EmpireColors.TextSecondary,fontSize=10.sp);Text("×${manager.incomeMultiplier} production",color=if(hired)EmpireColors.Cyan else EmpireColors.Gold,fontSize=11.sp,fontWeight=FontWeight.Bold)};Button(onClick={vm.hireManager(manager.businessId)},enabled=canHire,shape=RoundedCornerShape(13.dp),contentPadding=PaddingValues(horizontal=12.dp)){Text(if(hired)"HIRED" else moneyV2(manager.cost),fontSize=9.sp,fontWeight=FontWeight.Black)}}}}}}
@Composable private fun PremiumUpgradesTab(vm:GameViewModel,state:GameState){PremiumListShell("PERMANENT LAB","Permanent systems survive every ascension"){item{Surface(color=EmpireColors.Violet.copy(alpha=.12f),shape=RoundedCornerShape(20.dp),modifier=Modifier.fillMaxWidth()){Row(Modifier.padding(16.dp),verticalAlignment=Alignment.CenterVertically){MetaSprite(MetaSpriteKind.GEM,44.dp);Spacer(Modifier.width(10.dp));Text("${state.gems} GEMS",color=EmpireColors.Violet,fontSize=23.sp,fontWeight=FontWeight.Black)}}};items(Upgrades.catalog,key={it.id}){upgrade->val rank=state.upgradeRanks[upgrade.id]?:0;val maxed=rank>=upgrade.maxRank;val canBuy=!maxed&&state.gems>=upgrade.gemCost;Surface(color=EmpireColors.Surface.copy(alpha=.92f),shape=RoundedCornerShape(21.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(16.dp)){Row(verticalAlignment=Alignment.CenterVertically){Column(Modifier.weight(1f)){Text(upgrade.name,color=EmpireColors.TextPrimary,fontSize=16.sp,fontWeight=FontWeight.Black);Text(upgrade.description,color=EmpireColors.TextSecondary,fontSize=10.sp)};Text("$rank/${upgrade.maxRank}",color=EmpireColors.Cyan,fontSize=11.sp,fontWeight=FontWeight.Black)};Spacer(Modifier.height(10.dp));Button(onClick={vm.buyUpgrade(upgrade.id)},enabled=canBuy,modifier=Modifier.fillMaxWidth(),shape=RoundedCornerShape(13.dp)){Text(if(maxed)"MAXED" else "UPGRADE  •  ${upgrade.gemCost} GEMS",fontWeight=FontWeight.Black,fontSize=10.sp)}}}};item{Button(onClick=vm::activateProfitBoost,modifier=Modifier.fillMaxWidth().height(50.dp),shape=RoundedCornerShape(16.dp)){Text("⚡ WATCH REWARD  •  ×2 PROFITS",fontWeight=FontWeight.Black)}}}}
@Composable private fun PremiumGoalsTab(vm:GameViewModel,state:GameState,meta:PlayerMeta){PremiumListShell("COMMAND CENTER","Daily, weekly and permanent objectives"){item{val claimable=vm.canClaimDaily();Surface(color=EmpireColors.Gold.copy(alpha=.10f),shape=RoundedCornerShape(22.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(16.dp)){Text("DAILY DROP",color=EmpireColors.Gold,fontSize=10.sp,fontWeight=FontWeight.Black,letterSpacing=1.5.sp);Text("${meta.streakDays} day streak",color=EmpireColors.TextPrimary,fontSize=19.sp,fontWeight=FontWeight.Black);Spacer(Modifier.height(10.dp));Button(onClick={vm.claimDaily()},enabled=claimable,modifier=Modifier.fillMaxWidth(),shape=RoundedCornerShape(13.dp)){Text(if(claimable)"CLAIM DAILY REWARD" else "CLAIMED TODAY",fontWeight=FontWeight.Black)}}}};item{ChallengeDock(vm,Modifier.fillMaxWidth())};item{PremiumSectionTitle("MISSIONS","Short-term progression")};items(vm.missions(),key={it.id}){mission->ObjectiveCard(mission.title,"+${mission.rewardGems} gems",mission.fraction,if(mission.claimed)"DONE" else if(mission.completed)"CLAIM" else "${(mission.fraction*100).toInt()}%",mission.completed&&!mission.claimed){vm.claimMission(mission.id)}};item{PremiumSectionTitle("ACHIEVEMENTS","Permanent campaign milestones")};items(vm.achievements(),key={it.id}){a->ObjectiveCard(a.title,a.description,if(a.unlocked)1f else 0f,if(a.claimed)"DONE" else if(a.unlocked)"+${a.rewardGems}" else "LOCKED",a.unlocked&&!a.claimed){vm.claimAchievement(a.id)}}}}
@Composable private fun ObjectiveCard(title:String,subtitle:String,progress:Float,action:String,enabled:Boolean,onClick:()->Unit){Surface(color=EmpireColors.Surface.copy(alpha=.91f),shape=RoundedCornerShape(19.dp),modifier=Modifier.fillMaxWidth()){Column(Modifier.padding(14.dp)){Row(verticalAlignment=Alignment.CenterVertically){Column(Modifier.weight(1f)){Text(title,color=EmpireColors.TextPrimary,fontWeight=FontWeight.Black,fontSize=14.sp);Text(subtitle,color=EmpireColors.TextSecondary,fontSize=10.sp,maxLines=2,overflow=TextOverflow.Ellipsis)};TextButton(onClick=onClick,enabled=enabled){Text(action,fontWeight=FontWeight.Black,fontSize=10.sp)}};LinearProgressIndicator(progress={progress.coerceIn(0f,1f)},modifier=Modifier.fillMaxWidth().height(4.dp),color=EmpireColors.Cyan,trackColor=EmpireColors.SurfaceHigh)}}}
@Composable private fun PremiumListShell(title:String,subtitle:String,content:androidx.compose.foundation.lazy.LazyListScope.()->Unit){LazyColumn(Modifier.fillMaxSize(),contentPadding=PaddingValues(16.dp),verticalArrangement=Arrangement.spacedBy(12.dp)){item{PremiumSectionTitle(title,subtitle)};content()}}
@Composable private fun PremiumSectionTitle(title:String,subtitle:String){Column(Modifier.fillMaxWidth()){Text(title,color=EmpireColors.TextPrimary,fontSize=17.sp,fontWeight=FontWeight.Black,letterSpacing=.7.sp);Text(subtitle,color=EmpireColors.TextSecondary,fontSize=10.sp)}}
@Composable private fun PremiumNav(tab:PremiumTab,onSelect:(PremiumTab)->Unit){NavigationBar(containerColor=EmpireColors.DeepSpace.copy(alpha=.98f),tonalElevation=0.dp,modifier=Modifier.navigationBarsPadding()){PremiumTab.entries.forEach{item->NavigationBarItem(selected=tab==item,onClick={onSelect(item)},icon={Text(item.glyph,fontSize=19.sp,fontWeight=FontWeight.Black)},label={Text(item.label,fontSize=9.sp,fontWeight=FontWeight.Black)})}}}
private fun moneyV2(value:Double):String="$${EmpireNumberFormat.compact(value)}"