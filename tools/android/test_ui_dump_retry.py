import os
import pathlib
import subprocess
import tempfile
import textwrap
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
HELPER = ROOT / "tools" / "android" / "ui_dump_retry.sh"


class UiDumpRetryTest(unittest.TestCase):
    def make_fake_adb(self, directory: pathlib.Path, *, failures_before_success: int) -> tuple[pathlib.Path, pathlib.Path]:
        state = directory / "attempts.txt"
        state.write_text("0")
        fake_bin = directory / "bin"
        fake_bin.mkdir()
        adb = fake_bin / "adb"
        adb.write_text(textwrap.dedent(f"""\
            #!/usr/bin/env bash
            set -euo pipefail
            state={str(state)!r}
            failures_before_success={failures_before_success}
            if [[ "$1" == "shell" && "$2" == "rm" ]]; then
              exit 0
            fi
            if [[ "$1" == "shell" && "$2" == "uiautomator" && "$3" == "dump" ]]; then
              attempts=$(cat "$state")
              attempts=$((attempts + 1))
              printf '%s' "$attempts" > "$state"
              if (( attempts <= failures_before_success )); then
                echo 'ERROR: null root node returned by UiTestAutomationBridge.' >&2
                exit 1
              fi
              exit 0
            fi
            if [[ "$1" == "pull" ]]; then
              attempts=$(cat "$state")
              if (( attempts <= failures_before_success )); then
                exit 1
              fi
              printf '<hierarchy><node text="EMPIRE"/></hierarchy>\\n' > "$3"
              exit 0
            fi
            echo "unexpected adb invocation: $*" >&2
            exit 99
        """))
        adb.chmod(0o755)
        return fake_bin, state

    def run_helper(self, fake_bin: pathlib.Path, output: pathlib.Path, attempts: int) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PATH"] = f"{fake_bin}:{env['PATH']}"
        env["UI_DUMP_ATTEMPTS"] = str(attempts)
        env["UI_DUMP_RETRY_DELAY_SECONDS"] = "0"
        command = f"source {HELPER!s}; ui_dump_with_retry {output!s}"
        return subprocess.run(["bash", "-c", command], env=env, text=True, capture_output=True)

    def test_retries_transient_null_root_and_writes_fresh_xml(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = pathlib.Path(tmp)
            fake_bin, state = self.make_fake_adb(directory, failures_before_success=1)
            output = directory / "window.xml"

            result = self.run_helper(fake_bin, output, attempts=3)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(state.read_text(), "2")
            self.assertIn("EMPIRE", output.read_text())

    def test_fails_after_bounded_retries_without_stale_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = pathlib.Path(tmp)
            fake_bin, state = self.make_fake_adb(directory, failures_before_success=99)
            output = directory / "window.xml"
            output.write_text("stale")

            result = self.run_helper(fake_bin, output, attempts=3)

            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(state.read_text(), "3")
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
