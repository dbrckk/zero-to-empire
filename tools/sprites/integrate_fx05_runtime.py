#!/usr/bin/env python3
"""Idempotently wire validated FX-05 cyan energy pulse into the power-core plaza."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "app/src/main/java/com/zerotoempire/game/AscendantCityWorld.kt"


def main() -> None:
    text = PATH.read_text()
    if "R.drawable.zte_fx_05_final" in text:
        print("FX-05 runtime integration already present")
        return

    old_sheet = "    val pulseSheet = remember { ImageBitmap.imageResource(context.resources, R.drawable.zte_fx_06_final) }\n"
    new_sheet = (
        "    val cyanPulseSheet = remember { ImageBitmap.imageResource(context.resources, R.drawable.zte_fx_05_final) }\n"
        "    val pulseSheet = remember { ImageBitmap.imageResource(context.resources, R.drawable.zte_fx_06_final) }\n"
    )
    if old_sheet not in text:
        raise SystemExit("FX-06 pulse sheet anchor missing; refusing unsafe FX-05 patch")
    text = text.replace(old_sheet, new_sheet, 1)

    old_state = "    var pulseToken by remember { mutableIntStateOf(0) }\n    var pulseFrame by remember { mutableIntStateOf(-1) }\n\n"
    new_state = (
        "    var cyanFrame by remember { mutableIntStateOf(0) }\n"
        "    var pulseToken by remember { mutableIntStateOf(0) }\n"
        "    var pulseFrame by remember { mutableIntStateOf(-1) }\n\n"
        "    LaunchedEffect(motionEnabled) {\n"
        "        if (!motionEnabled) {\n"
        "            cyanFrame = 3\n"
        "        } else {\n"
        "            while (true) {\n"
        "                for (frame in 0 until 8) {\n"
        "                    cyanFrame = frame\n"
        "                    delay(110)\n"
        "                }\n"
        "                delay(440)\n"
        "            }\n"
        "        }\n"
        "    }\n\n"
    )
    if old_state not in text:
        raise SystemExit("FX-06 pulse state anchor missing; refusing unsafe FX-05 patch")
    text = text.replace(old_state, new_state, 1)

    old_surface = """        Surface(
            color = EmpireColors.DeepSpace.copy(alpha = .86f),
"""
    new_surface = """        Canvas(Modifier.size(110.dp)) {
            val frame = cyanFrame.coerceIn(0, 7)
            val side = minOf(size.width, size.height).toInt()
            drawImage(
                image = cyanPulseSheet,
                srcOffset = IntOffset((frame % 4) * 128, (frame / 4) * 128),
                srcSize = IntSize(128, 128),
                dstOffset = IntOffset(((size.width - side) / 2f).toInt(), ((size.height - side) / 2f).toInt()),
                dstSize = IntSize(side, side)
            )
        }
        Surface(
            color = EmpireColors.DeepSpace.copy(alpha = .86f),
"""
    if old_surface not in text:
        raise SystemExit("AscendantCorePlaza surface anchor missing; refusing unsafe FX-05 patch")
    text = text.replace(old_surface, new_surface, 1)

    PATH.write_text(text)
    print("Integrated FX-05 cyan pulse into AscendantCorePlaza")


if __name__ == "__main__":
    main()
