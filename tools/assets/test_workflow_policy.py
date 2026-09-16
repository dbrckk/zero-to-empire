import unittest
from pathlib import Path


WORKFLOW = Path(".github/workflows/unified-asset-pipeline.yml")


class WorkflowPolicyTest(unittest.TestCase):
    def text(self) -> str:
        return WORKFLOW.read_text(encoding="utf-8")

    def test_workflow_is_read_only(self):
        text = self.text()
        self.assertIn("contents: read", text)
        self.assertNotIn("contents: write", text)
        self.assertNotIn("git push", text)
        self.assertNotIn("pull_request_target", text)

    def test_manual_generation_requires_explicit_asset_id(self):
        text = self.text()
        self.assertIn("workflow_dispatch:", text)
        self.assertIn("asset_id:", text)
        self.assertIn("required: true", text)

    def test_pull_requests_run_deterministic_pipeline_tests(self):
        text = self.text()
        self.assertIn("pull_request:", text)
        self.assertIn("python -m unittest discover -s tools/assets", text)


if __name__ == "__main__":
    unittest.main()
