"""Ensure privileged release archival never elevates unreviewed assets to DONE."""
import unittest
from pathlib import Path


class CandidateArchiveWorkflowTests(unittest.TestCase):
    def test_trigger_is_trusted_collector_completion_or_manual_bootstrap(self):
        text = Path(".github/workflows/archive-character-candidates.yml").read_text()
        self.assertIn("workflow_run:", text)
        self.assertIn("workflows: [Kaggle Async Character Collector]", text)
        self.assertIn("github.event.workflow_run.conclusion == 'success'", text)
        self.assertIn("github.event.workflow_run.head_branch == 'main'", text)
        self.assertIn("github.event.workflow_run.head_repository.full_name == github.repository", text)
        self.assertIn("Refusing non-successful/non-main/non-repository collector run", text)

    def test_release_uses_only_qa_passed_candidates_and_never_promotes(self):
        flow = Path(".github/workflows/archive-character-candidates.yml").read_text()
        script = Path("tools/sprites/archive_character_candidates.py").read_text()
        self.assertIn("--name kaggle-async-character-batch", flow)
        self.assertIn("--source-run-id", flow)
        self.assertIn("gh release upload", flow)
        self.assertIn("candidate-index.json", script)
        self.assertIn('row.get("pass") is not True', script)
        self.assertIn("hashlib.sha256", script)
        self.assertIn('"strict_approved": False', script)
        self.assertIn('"automatic_runtime_promotion": False', script)
        self.assertNotIn("git push", flow)
        self.assertNotIn("app/src/main/res/", flow)
        self.assertNotIn("strict_status", flow)


if __name__ == "__main__":
    unittest.main()
