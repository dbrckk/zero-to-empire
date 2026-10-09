#!/usr/bin/env bash

ui_dump_with_retry() {
  local output="${1:?output path required}"
  local remote="${UI_DUMP_REMOTE_PATH:-/sdcard/window.xml}"
  local attempts="${UI_DUMP_ATTEMPTS:-5}"
  local delay_seconds="${UI_DUMP_RETRY_DELAY_SECONDS:-1}"
  local attempt=1
  local log="${output}.uiautomator.log"
  local command_timeout="${UI_DUMP_COMMAND_TIMEOUT_SECONDS:-35}"

  rm -f "$output" "$log"
  while (( attempt <= attempts )); do
    rm -f "$output"
    adb shell rm -f "$remote" >/dev/null 2>&1 || true

    if timeout "${command_timeout}s" adb shell uiautomator dump "$remote" >"$log" 2>&1; then
      # adb pull intermittently fails on slow API-35 CI emulators even after
      # uiautomator has successfully written the remote hierarchy.
      timeout "${command_timeout}s" adb exec-out cat "$remote" > "$output" 2>/dev/null || true
      if ! grep -q '</hierarchy>' "$output" 2>/dev/null; then
        timeout "${command_timeout}s" adb pull "$remote" "$output" >/dev/null 2>&1 || true
      fi
      if grep -q '</hierarchy>' "$output" 2>/dev/null; then
        rm -f "$log"
        return 0
      fi
    fi

    rm -f "$output"
    if (( attempt < attempts )); then
      sleep "$delay_seconds"
    fi
    attempt=$((attempt + 1))
  done

  echo "UI_DUMP_FAILED attempts=$attempts timeout_seconds=$command_timeout output=$output" >&2
  if [[ -s "$log" ]]; then
    cat "$log" >&2
  fi
  return 1
}
