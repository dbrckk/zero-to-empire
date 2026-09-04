#!/usr/bin/env python3
"""Idempotently wire FX-07 construction dust/debris into purchase impact feedback."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "app/src/main/java/com/zerotoempire/game/PurchaseImpactVfx.kt"


def main() -> None:
    text = PATH.read_text()
    if "R.drawable.zte_fx_07_final" in text:
        print("FX-07 runtime integration already present")
        return

    text = text.replace(
        "private const val WarmPulsePeakFrame = 4\n",
        "private const val WarmPulsePeakFrame = 4\nprivate const val ConstructionDustPeakFrame = 3\n",
        1,
    )
    text = text.replace(
        "    val sheet = remember(context) {\n        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_06_final).asImageBitmap()\n    }\n",
        "    val sheet = remember(context) {\n        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_06_final).asImageBitmap()\n    }\n    val dustSheet = remember(context) {\n        BitmapFactory.decodeResource(context.resources, R.drawable.zte_fx_07_final).asImageBitmap()\n    }\n",
        1,
    )
    anchor = '''        drawImage(
            image = sheet,
            srcOffset = IntOffset(
                x = (frame % WarmPulseColumns) * WarmPulseFrameSize,
                y = (frame / WarmPulseColumns) * WarmPulseFrameSize
            ),
            srcSize = IntSize(WarmPulseFrameSize, WarmPulseFrameSize),
            dstOffset = pulseOffset,
            dstSize = IntSize(pulseSize, pulseSize),
            alpha = if (reduced) intensity * .72f else intensity
        )
'''
    replacement = anchor + '''
        val dustFrame = when {
            reduced -> ConstructionDustPeakFrame
            lowPower -> ((p * 4f).toInt().coerceIn(0, 3) * 2).coerceAtMost(WarmPulseFrameCount - 1)
            else -> (p * WarmPulseFrameCount).toInt().coerceIn(0, WarmPulseFrameCount - 1)
        }
        val dustSize = (min * (.42f + intensity * .14f)).toInt().coerceAtLeast(1)
        drawImage(
            image = dustSheet,
            srcOffset = IntOffset(
                x = (dustFrame % WarmPulseColumns) * WarmPulseFrameSize,
                y = (dustFrame / WarmPulseColumns) * WarmPulseFrameSize
            ),
            srcSize = IntSize(WarmPulseFrameSize, WarmPulseFrameSize),
            dstOffset = IntOffset(
                x = (center.x - dustSize / 2f).toInt(),
                y = (center.y - dustSize * .36f).toInt()
            ),
            dstSize = IntSize(dustSize, dustSize),
            alpha = if (reduced) intensity * .48f else intensity * .76f
        )
'''
    if anchor not in text:
        raise SystemExit("PurchaseImpactVfx source changed; refusing unsafe FX-07 patch")
    text = text.replace(anchor, replacement, 1)
    PATH.write_text(text)
    print("Integrated FX-07 into AssetPurchaseImpact")


if __name__ == "__main__":
    main()
