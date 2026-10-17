# Android emulator performance evidence

The existing Android Emulator Smoke pipeline checks startup, real tap/purchase,
manager automation, offline income, autosave durability, and a long emulator
session. It also records a **diagnostic** rendering and memory snapshot.

## Artifact

Open a run of **Android Emulator Smoke** and download
`android-emulator-smoke-evidence`. Relevant files:

- `meminfo-start.txt`: process PSS after completing onboarding.
- `meminfo.txt`: process PSS after the functional/persistence smoke.
- `gfxinfo-reset.txt`: raw result of the frame-history reset.
- `gfxinfo-framestats.txt`: raw `dumpsys gfxinfo <package> framestats`.
- `performance-snapshot.json`: structured metrics, units, sample count, notes.
- `performance-summary.md`: abbreviated human-readable result, also sent to
  the GitHub Actions job summary.

The JSON captures the PSS **in KiB** at two different game states, and frame
completion latency from **IntendedVsync** to **FrameCompleted** on eligible
records with `Flags == 0`. Frame timings report p50, p95, p99, and the
fraction exceeding a **fixed 16.67ms reference budget**. The reference
threshold is not the dynamically measured panel refresh deadline. If Android
produces no eligible frames, frame statistics are `null` and the report
explicitly says `no_valid_frames`, rather than pretending a zero-millisecond
render time.

## How to interpret

The CI emulator is an x86_64 Android API 35 software-rendered environment and
the workflow disables system animations. GitHub runner CPU/GPU contention varies
between jobs. Do **not** interpret these numbers as actual phone FPS, production
GPU performance, or a formal memory regression threshold. Differences in PSS
between onboarding and a later game state are not proof of a memory leak.

For useful comparisons, collect several runs **with the same workflow image and
APK configuration**. Keep the raw dumps, sample counts, and run identifiers.
Investigate repeatable large changes before setting any performance budget.
Confirm meaningful regressions on a physical low-end Android device using
Android Studio profiler / Macrobenchmark with realistic interaction workloads.

Snapshot collection failures or invalid PSS cause smoke to fail; an empty
frame sample is reported as unavailable but does not invent a timing value.
This instrumentation adds no new unit tests and does not alter production code.
