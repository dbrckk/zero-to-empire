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


class AutofactoryWorkflowPolicyTest(unittest.TestCase):
    def workflow_text(self) -> str:
        path = Path(".github/workflows/asset-autofactory.yml")
        self.assertTrue(path.is_file(), f"missing workflow: {path}")
        return path.read_text(encoding="utf-8")

    def test_character_dispatch_uses_computed_count(self):
        text = self.workflow_text()
        self.assertIn("producer_dispatch_token:", text)
        self.assertIn("-f count=\\"$count\\"", text)
        self.assertNotIn("DISPATCH_KAGGLE_CHARACTER)\\n              gh workflow run 'Kaggle Mass Sprite Factory' --ref main -f count=2", text)

    def test_dispatch_token_is_declared_and_forwarded(self):
        text = self.workflow_text()
        self.assertIn("AUTOF_TRIGGER_DISPATCH_TOKEN: ${{ inputs.producer_dispatch_token || '' }}", text)
        self.assertIn("-f dispatch_token='${{ github.run_id }}'", text)


if __name__ == "__main__":
    unittest.main()
