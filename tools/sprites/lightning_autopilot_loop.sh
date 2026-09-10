#!/usr/bin/env bash
set -u

REPO="$HOME/zero-to-empire"
LOG="$HOME/zte-lightning-autopilot.log"
LOCK="$HOME/.zte-lightning-autopilot.lock"
INTERVAL="${LIGHTNING_SPRITE_INTERVAL_SECONDS:-300}"

mkdir -p "$REPO"
exec 9>"$LOCK"
if ! flock -n 9; then
  echo "$(date -Is) AUTOPILOT_ALREADY_RUNNING" >> "$LOG"
  exit 0
fi

echo "$(date -Is) AUTOPILOT_STARTED interval=${INTERVAL}s" >> "$LOG"

while true; do
  {
    echo "$(date -Is) WAVE_START"
    cd "$REPO"
    git fetch origin main
    git reset --hard origin/main
    export SPRITE_COUNT="${SPRITE_COUNT:-56}"
    export SPRITE_SEED="$(date +%s)"
    python -u tools/sprites/lightning_studio_factory.py
    rc=$?
    echo "$(date -Is) WAVE_END rc=$rc"
  } >> "$LOG" 2>&1
  sleep "$INTERVAL"
done
