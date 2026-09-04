#!/usr/bin/env python3
"""Idempotently wire the validated FX-06 warm pulse sheet into the power-core tap UI."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "app/src/main/java/com/zerotoempire/game/AscendantCityWorld.kt"

IMPORT_ANCHOR = "package com.zerotoempire.game\n\n"
RUNTIME_IMPORTS = """import android.provider.Settings\nimport androidx.compose.runtime.LaunchedEffect\nimport androidx.compose.runtime.getValue\nimport androidx.compose.runtime.mutableIntStateOf\nimport androidx.compose.runtime.setValue\nimport androidx.compose.ui.graphics.ImageBitmap\nimport androidx.compose.ui.platform.LocalContext\nimport androidx.compose.ui.res.imageResource\nimport androidx.compose.ui.unit.IntOffset\nimport androidx.compose.ui.unit.IntSize\nimport kotlinx.coroutines.delay\n"""

OLD = '''@Composable
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
'''

NEW = '''@Composable
private fun AscendantCorePlaza(state: GameState, tap: () -> Unit, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    val pulseSheet = remember { ImageBitmap.imageResource(context.resources, R.drawable.zte_fx_06_final) }
    val motionEnabled = remember(context) {
        Settings.Global.getFloat(context.contentResolver, Settings.Global.ANIMATOR_DURATION_SCALE, 1f) > 0f
    }
    var pulseToken by remember { mutableIntStateOf(0) }
    var pulseFrame by remember { mutableIntStateOf(-1) }

    LaunchedEffect(pulseToken) {
        if (pulseToken == 0) return@LaunchedEffect
        if (!motionEnabled) {
            pulseFrame = 3
            delay(80)
        } else {
            for (frame in 0 until 8) {
                pulseFrame = frame
                delay(42)
            }
        }
        pulseFrame = -1
    }

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
                .clickable(role = Role.Button) {
                    pulseToken += 1
                    tap()
                }
        ) {
            Box(contentAlignment = Alignment.Center) {
                EmpireCoreGlyph(Modifier.size(86.dp), EmpireEras.current(state.lifetimeCash).index)
            }
        }
        if (pulseFrame >= 0) {
            Canvas(Modifier.size(118.dp)) {
                val frame = pulseFrame.coerceIn(0, 7)
                val side = minOf(size.width, size.height).toInt()
                drawImage(
                    image = pulseSheet,
                    srcOffset = IntOffset((frame % 4) * 128, (frame / 4) * 128),
                    srcSize = IntSize(128, 128),
                    dstOffset = IntOffset(((size.width - side) / 2f).toInt(), ((size.height - side) / 2f).toInt()),
                    dstSize = IntSize(side, side)
                )
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
'''


def main() -> None:
    text = PATH.read_text()
    if "R.drawable.zte_fx_06_final" in text:
        print("FX-06 runtime integration already present")
        return
    if OLD not in text:
        raise SystemExit("AscendantCorePlaza source changed; refusing unsafe patch")
    if "import android.provider.Settings\n" not in text:
        text = text.replace(IMPORT_ANCHOR, IMPORT_ANCHOR + RUNTIME_IMPORTS, 1)
    text = text.replace(OLD, NEW, 1)
    PATH.write_text(text)
    print("Integrated FX-06 into AscendantCorePlaza")


if __name__ == "__main__":
    main()
