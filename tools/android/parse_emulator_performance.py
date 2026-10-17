#!/usr/bin/env python3
"""Summarize observational Android gfxinfo framestats + meminfo CI evidence.

Does not enforce FPS thresholds: emulator timing is not production-device FPS.
Missing/malformed samples are explicitly marked unavailable, never reported as zero.
"""

import argparse
import json
import re
from pathlib import Path


def percentile(sorted_values, fraction):
    if not sorted_values:
        return None
    index = (len(sorted_values) - 1) * fraction
    lower = int(index)
    upper = min(lower + 1, len(sorted_values) - 1)
    return round(sorted_values[lower] + (sorted_values[upper] - sorted_values[lower]) * (index - lower), 2)


def read_frames(raw):
    in_profile = False
    fields = None
    durations_ms = []
    discarded_rows = 0
    profile_sections = 0
    for line_text in raw.splitlines():
        line = line_text.strip()
        if line == '---PROFILEDATA---':
            in_profile = not in_profile
            fields = None
            if in_profile:
                profile_sections += 1
            continue
        if not in_profile:
            continue
        if line.startswith('Flags,'):
            fields = {field.strip(): n for n, field in enumerate(line.split(','))}
            continue
        if not line or fields is None:
            continue
        if not {'Flags', 'IntendedVsync', 'FrameCompleted'} <= fields.keys():
            discarded_rows += 1
            continue
        columns = line.split(',')
        try:
            flags = int(columns[fields['Flags']])
            start = int(columns[fields['IntendedVsync']])
            end = int(columns[fields['FrameCompleted']])
        except (ValueError, IndexError):
            discarded_rows += 1
            continue
        # Android uses flags 0 and 1 for ordinary and first-window frames.
        # Only completed, positive timestamps describe a real rendered frame.
        if flags not in (0, 1):
            continue
        duration_ns = end - start
        if start <= 0 or duration_ns <= 0 or duration_ns >= 100_000_000_000:
            discarded_rows += 1
            continue
        durations_ms.append(duration_ns / 1_000_000)
    durations_ms.sort()
    count = len(durations_ms)
    return {
        'status': 'ok' if count else 'no_eligible_frames' if profile_sections else 'no_profiledata',
        'profile_sections': profile_sections,
        'frames': count,
        'discarded_rows': discarded_rows,
        'p50_ms': percentile(durations_ms, .50),
        'p90_ms': percentile(durations_ms, .90),
        'p95_ms': percentile(durations_ms, .95),
        'max_ms': round(durations_ms[-1], 2) if count else None,
        # A diagnostic 60 Hz threshold, NOT a device-calibrated jank metric.
        'over_16_67ms': sum(ms > 16.67 for ms in durations_ms) if count else None,
        'over_16_67ms_pct': round(100 * sum(ms > 16.67 for ms in durations_ms) / count, 2) if count else None,
    }


def read_total_pss_kb(raw):
    # Android changes meminfo layout across API levels. App Summary has
    # `TOTAL: ...`; the detailed table has `TOTAL ...`; either is in KiB.
    for pattern in (r'^\s*TOTAL:\s*([\d,]+)(?:\s|$)',
                    r'^\s*TOTAL\s+([\d,]+)(?:\s|$)',
                    r'^\s*TOTAL PSS:\s*([\d,]+)(?:\s|$)'):
        match = re.search(pattern, raw, re.MULTILINE)
        if match:
            return int(match.group(1).replace(',', ''))
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gfxinfo', type=Path, required=True)
    parser.add_argument('--meminfo', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    gfx = args.gfxinfo.read_text(errors='replace') if args.gfxinfo.is_file() else ''
    mem = args.meminfo.read_text(errors='replace') if args.meminfo.is_file() else ''
    summary = {
        'schema': 1,
        'source': 'android-emulator-api35-debug-observational',
        'frame_duration_definition': 'FrameCompleted - IntendedVsync, ms',
        'frame_timings': read_frames(gfx),
        'memory': {'total_pss_kb': read_total_pss_kb(mem)},
        'limitations': 'Emulator timing is not device FPS; different hardware/builds cannot be compared directly.',
    }
    args.output.write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
    print('PERF_EVIDENCE=' + json.dumps({
        'frames': summary['frame_timings']['frames'],
        'p95_ms': summary['frame_timings']['p95_ms'],
        'status': summary['frame_timings']['status'],
        'total_pss_kb': summary['memory']['total_pss_kb'],
    }, sort_keys=True))


if __name__ == '__main__':
    main()
