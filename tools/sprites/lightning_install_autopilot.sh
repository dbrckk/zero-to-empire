#!/usr/bin/env bash
set -euo pipefail

REPO="$HOME/zero-to-empire"
START_DIR="$HOME/.lightning_studio"
START_FILE="$START_DIR/on_start.sh"
LOG="$HOME/zte-lightning-autopilot.log"

if [ -d "$REPO/.git" ]; then
  git -C "$REPO" fetch origin main
  git -C "$REPO" reset --hard origin/main
else
  rm -rf "$REPO"
  git clone --depth 1 https://github.com/dbrckk/zero-to-empire.git "$REPO"
fi

mkdir -p "$START_DIR"
cat > "$START_FILE" <<'EOF'
#!/usr/bin/env bash
set -u
REPO="$HOME/zero-to-empire"
if [ -d "$REPO/.git" ]; then
  git -C "$REPO" fetch origin main >/dev/null 2>&1 || true
  git -C "$REPO" reset --hard origin/main >/dev/null 2>&1 || true
else
  git clone --depth 1 https://github.com/dbrckk/zero-to-empire.git "$REPO" >/dev/null 2>&1 || true
fi
if [ -f "$REPO/tools/sprites/lightning_autopilot_loop.sh" ]; then
  nohup bash "$REPO/tools/sprites/lightning_autopilot_loop.sh" >/dev/null 2>&1 &
fi
EOF
chmod +x "$START_FILE"

python - <<'PY'
from lightning_sdk import Studio
s = Studio()
s.auto_sleep = False
try:
    urls = s.add_ports(8765)
    if urls:
        try:
            print('LIGHTNING_OUTPUT_URL=' + urls[0].urls[0])
        except Exception:
            print('LIGHTNING_PORT_8765_EXPOSED=1')
except Exception as exc:
    print('LIGHTNING_PORT_WARNING=' + str(exc))
PY

pkill -f 'http.server 8765' >/dev/null 2>&1 || true
mkdir -p "$REPO/.lightning-output"
nohup python -m http.server 8765 --directory "$REPO/.lightning-output" >> "$LOG" 2>&1 &

nohup bash "$REPO/tools/sprites/lightning_autopilot_loop.sh" >/dev/null 2>&1 &

echo "AUTOPILOT_INSTALLED=1"
echo "AUTOPILOT_LOG=$LOG"

python - <<'PY'
from lightning_sdk import Machine, Studio
s = Studio()
print('CURRENT_MACHINE=' + str(s.machine))
if 'CPU' in str(s.machine).upper():
    candidates = []
    for name in ('T4','L4','L40S'):
        m = getattr(Machine, name, None)
        if m is not None:
            candidates.append((name, m))
    last = None
    for name, machine in candidates:
        try:
            print('TRY_SWITCH_MACHINE=' + name, flush=True)
            s.switch_machine(machine)
            print('SWITCHED_MACHINE=' + name, flush=True)
            break
        except Exception as exc:
            last = exc
            print('SWITCH_FAILED_' + name + '=' + str(exc), flush=True)
    else:
        if last is not None:
            print('GPU_SWITCH_REQUIRED_MANUALLY=1')
PY
