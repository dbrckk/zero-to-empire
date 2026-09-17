from pathlib import Path
import unittest


WORKFLOW = Path(".github/workflows/unified-asset-pipeline.yml")


class UnifiedAssetWorkflowPolicyTest(unittest.TestCase):
    def workflow_text(self) -> str:
        self.assertTrue(WORKFLOW.is_file(), f"missing workflow: {WORKFLOW}")
        return WORKFLOW.read_text(encoding="utf-8")

    def test_workflow_is_manual_read_only_and_requires_explicit_asset_id(self):
        text = self.workflow_text()
        self.assertIn("workflow_dispatch:", text)
        self.assertIn("asset_id:", text)
        self.assertIn("required: true", text)
        self.assertIn("provider:", text)
        self.assertIn("hf-static", text)
        self.assertIn("permissions:\n  contents: read", text)

    def test_workflow_cannot_mutate_repository_or_use_privileged_pr_trigger(self):
        text = self.workflow_text().lower()
        self.assertNotIn("git push", text)
        self.assertNotIn("contents: write", text)
        self.assertNotIn("pull_request_target", text)

    def test_workflow_emits_review_bundle_without_runtime_promotion(self):
        text = self.workflow_text()
        self.assertIn("art/incoming/assets/${{ inputs.asset_id }}", text)
        self.assertIn("candidate.png", text)
        self.assertIn("metadata.json", text)
        self.assertIn("qa-report.json", text)
        self.assertIn("contact-sheet.png", text)
        self.assertIn("actions/upload-artifact", text)
        self.assertNotIn("app/src/main/res/drawable-nodpi", text)


if __name__ == "__main__":
    unittest.main()
