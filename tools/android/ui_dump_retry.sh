#!/usr/bin/env bash

ui_dump_with_retry() {
  local output="${1:?output path required}"
  local remote="${UI_DUMP_REMOTE_PATH:-/sdcard/window.xml}"
  local attempts="${UI_DUMP_ATTEMPTS:-5}"
  local delay_seconds="${UI_DUMP_RETRY_DELAY_SECONDS:-1}"
  local attempt=1
  local log="${output}.uiautomator.log"

  rm -f "$output" "$log"
  while (( attempt <= attempts )); do
    rm -f "$output"
    adb shell rm -f "$remote" >/dev/null 2>&1 || true

    if adb shell uiautomator dump "$remote" >"$log" 2>&1 && \
       adb pull "$remote" "$output" >/dev/null 2>&1 && \
       [[ -s "$output" ]]; then
      rm -f "$log"
      return 0
    fi

    rm -f "$output"
    if (( attempt < attempts )); then
      sleep "$delay_seconds"
    fi
    attempt=$((attempt + 1))
  done

  echo "UI_DUMP_FAILED attempts=$attempts output=$output" >&2
  if [[ -s "$log" ]]; then
    cat "$log" >&2
  fi
  return 1
}
