#!/usr/bin/env python3
"""Turn real Android emulator dumpsys evidence into a machine-readable performance snapshot.

This is diagnostic instrumentation, not an FPS or memory regression gate: the
GitHub-hosted software-rendered emulator is not representative of a phone GPU.
"""
import argparse
import csv
import io
import json
import math
import re
from pathlib import Path


def total_pss_kib(raw: str) -> int:
    """Android App Summary (new) or TOTAL table (older) PSS, in KiB."""
    match = re.search(r"(?m)^\s*TOTAL PSS:\s*([\d,]+)", raw)
    if not match:
        match = re.search(r"(?m)^\s*TOTAL\s+([\d,]+)\s+[\d,]+", raw)
    if not match:
        raise ValueError("missing TOTAL PSS in meminfo dump")
    return int(match.group(1).replace(",", ""))


def percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("no frame samples")
    position = (len(ordered) - 1) * fraction
    left = math.floor(position)
    right = math.ceil(position)
    return ordered[left] + (ordered[right] - ordered[left]) * (position - left)


def frame_durations_ms(raw: str) -> tuple[list[float], int]:
    """Read the named CSV columns rather than depending on Android API column offsets."""
    durations: list[float] = []
    rows_seen = 0
    for section in raw.split("---PROFILEDATA---")[1::2]:
        lines = [line for line in section.splitlines() if line.strip()]
        if not lines:
            continue
        reader = csv.DictReader(io.StringIO("\n".join(lines)))
        if not reader.fieldnames:
            continue
        names = {field.strip().lower(): field for field in reader.fieldnames}
        if not {"flags", "intendedvsync", "framecompleted"}.issubset(names):
            continue
        for row in reader:
            rows_seen += 1
            try:
                if int(row[names["flags"]]) != 0:
                    continue
                started = int(row[names["intendedvsync"]])
                finished = int(row[names["framecompleted"]])
                elapsed_ms = (finished - started) / 1_000_000
                if 0 < elapsed_ms < 10_000:
                    durations.append(elapsed_ms)
            except (ValueError, TypeError, KeyError):
                continue
    return durations, rows_seen


def generate(mem_start: str, mem_end: str, gfxinfo: str) -> dict:
    start = total_pss_kib(mem_start)
    end = total_pss_kib(mem_end)
    frames, total_rows = frame_durations_ms(gfxinfo)
    frame_stats = {
        "measurement": "dumpsys gfxinfo framestats; IntendedVsync to FrameCompleted",
        "recorded_rows": total_rows,
        "valid_frames": len(frames),
        "discarded_rows": total_rows - len(frames),
        "p50_ms": round(percentile(frames, 0.50), 2) if frames else None,
        "p95_ms": round(percentile(frames, 0.95), 2) if frames else None,
        "p99_ms": round(percentile(frames, 0.99), 2) if frames else None,
        "over_16_67ms_pct": round(100 * sum(t > 16.67 for t in frames) / len(frames), 2) if frames else None,
        "status": "measured" if frames else "no_valid_frames",
    }
    return {
        "schema_version": 1,
        "device": "GitHub Actions Android API 35 default x86_64 pixel_6 emulator",
        "kind": "functional_smoke_diagnostic_not_a_device_benchmark",
        "memory": {
            "unit": "KiB",
            "pss_after_onboarding": start,
            "pss_after_functional_soak": end,
            "delta_pss": end - start,
            "note": "Snapshots at different gameplay states; growth is not proof of a leak.",
        },
        "frame_timing": frame_stats,
        "limitations": [
            "Software emulation, animations disabled by CI, and variable runner load",
            "A short functional smoke sample, not sustained gameplay or measured device FPS",
            "No FPS or memory pass/fail thresholds inferred from emulator figures",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--meminfo-start", type=Path, required=True)
    parser.add_argument("--meminfo-end", type=Path, required=True)
    parser.add_argument("--gfxinfo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()
    data = generate(
        args.meminfo_start.read_text(encoding="utf-8"),
        args.meminfo_end.read_text(encoding="utf-8"),
        args.gfxinfo.read_text(encoding="utf-8"),
    )
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    memory, frame = data["memory"], data["frame_timing"]
    p95 = f'{frame["p95_ms"]:.2f} ms' if frame["p95_ms"] is not None else "N/A"
    md = (
        "### Android emulator performance snapshot (diagnostic)\n\n"
        "| Signal | Value |\n|---|---:|\n"
        f'| PSS after onboarding | {memory["pss_after_onboarding"]:,} KiB |\n'
        f'| PSS after functional soak | {memory["pss_after_functional_soak"]:,} KiB |\n'
        f'| PSS change (different game states) | {memory["delta_pss"]:+,} KiB |\n'
        f'| Valid rendered frames | {frame["valid_frames"]} |\n'
        f'| P95 frame completion time | {p95} |\n\n'
        "The emulator uses software rendering and disabled animations; these data "
        "are **not** phone FPS, a memory-leak diagnosis or a performance release gate.\n"
    )
    args.markdown.write_text(md, encoding="utf-8")
    print("PERFORMANCE_SNAPSHOT=" + str(args.output))
    print(f'PERFORMANCE_PSS_FINAL_KIB={memory["pss_after_functional_soak"]}')
    print(f'PERFORMANCE_VALID_FRAMES={frame["valid_frames"]}')


if __name__ == "__main__":
    main()
