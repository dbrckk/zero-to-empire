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

    def test_backfill_uses_only_canonical_pending_review_provenance(self):
        flow = Path(".github/workflows/backfill-character-candidate-archives.yml").read_text()
        self.assertIn("review_artifact_run_id", flow)
        self.assertIn("pipeline_status')=='AWAITING_REVIEW'", flow)
        self.assertIn("strict_status')!='DONE'", flow)
        self.assertIn("zt e".replace(" ", "") + "-characters-", flow)
        self.assertIn("gh workflow run 'Archive Character Candidates'", flow)
        self.assertIn("ALREADY_ARCHIVED=", flow)
        self.assertNotIn("git push", flow)
        self.assertNotIn("app/src/main/res/", flow)

    def test_candidate_bank_is_assembled_only_from_trusted_release_and_queue(self):
        flow = Path(".github/workflows/character-candidate-bank.yml").read_text()
        source = Path("tools/sprites/build_character_candidate_bank.py").read_text()
        self.assertIn("workflows: [Archive Character Candidates]", flow)
        self.assertIn("github.event.workflow_run.conclusion == 'success'", flow)
        self.assertIn("github.event.workflow_run.head_branch == 'main'", flow)
        self.assertIn("github.event.workflow_run.head_repository.full_name == github.repository", flow)
        # Either the archive or the canonical queue can become ready first.
        # Trigger on both to prevent a stale incomplete bank indefinitely.
        self.assertIn("  push:", flow)
        self.assertIn("'art/production/master-asset-queue.json'", flow)
        self.assertIn("gh release download", flow)
        self.assertIn("gh release upload", flow)
        self.assertIn("candidate-bank-index.json", source)
        self.assertIn("review_artifact_run_id", source)
        self.assertIn("sha256", source)
        self.assertIn("candidate_production_complete", source)
        self.assertIn("--local-original art/incoming/chatgpt-original", flow)
        self.assertIn("'art/incoming/chatgpt-original/candidates/**'", flow)
        self.assertIn("'art/incoming/chatgpt-original/src_svg/**'", flow)
        self.assertIn("validated_local_candidate", source)
        self.assertIn("canonical_queue_production_processed", source)
        self.assertIn("repo-local-original", source)
        self.assertIn('"automatic_runtime_promotion": False', source)
        self.assertIn('"strict_approved": False', source)
        self.assertNotIn("app/src/main/res/", flow)
        self.assertNotIn("git push", flow)

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
