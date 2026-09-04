#!/usr/bin/env python3
"""Idempotently integrate FX-04 steam vent into purchase feedback."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "app/src/main/java/com/zerotoempire/game/PurchaseImpactVfx.kt"
text = PATH.read_text()

if "R.drawable.zte_fx_04_final" in text:
    print("FX-04 already integrated")
    raise SystemExit(0)

anchor = '''    val dustSheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_07_final).asImageBitmap()
    }
'''
replacement = anchor + '''    val steamSheet = remember(context) {
        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_04_final).asImageBitmap()
    }
'''
if anchor not in text:
    raise SystemExit("Unsafe patch refused: FX-07 sheet anchor missing")
text = text.replace(anchor, replacement, 1)

anchor2 = '''        if (!reduced) {
            drawCircle(
'''
steam = '''        val steamFrame = when {
            reduced -> 3
            lowPower -> ((p * 4f).toInt().coerceIn(0, 3) * 2).coerceAtMost(WarmPulseFrameCount - 1)
            else -> (p * WarmPulseFrameCount).toInt().coerceIn(0, WarmPulseFrameCount - 1)
        }
        val steamSize = (min * (.30f + intensity * .10f)).toInt().coerceAtLeast(1)
        drawImage(
            image = steamSheet,
            srcOffset = IntOffset(
                x = (steamFrame % WarmPulseColumns) * WarmPulseFrameSize,
                y = (steamFrame / WarmPulseColumns) * WarmPulseFrameSize
            ),
            srcSize = IntSize(WarmPulseFrameSize, WarmPulseFrameSize),
            dstOffset = IntOffset(
                x = (center.x + min * .08f - steamSize / 2f).toInt(),
                y = (center.y - steamSize * .72f).toInt()
            ),
            dstSize = IntSize(steamSize, steamSize),
            alpha = if (reduced) intensity * .28f else (1f - p) * intensity * .48f
        )

''' + anchor2
if anchor2 not in text:
    raise SystemExit("Unsafe patch refused: Canvas effect anchor missing")
text = text.replace(anchor2, steam, 1)
PATH.write_text(text)
print("Integrated FX-04 steam vent runtime feedback")
