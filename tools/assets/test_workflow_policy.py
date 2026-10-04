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
        self.assertIn('-f count="$count"', text)
        self.assertNotIn("DISPATCH_KAGGLE_CHARACTER)\\n              gh workflow run 'Kaggle Mass Sprite Factory' --ref main -f count=2", text)

    def test_dispatch_token_is_declared_and_forwarded(self):
        text = self.workflow_text()
        self.assertIn("AUTOF_TRIGGER_DISPATCH_TOKEN: ${{ inputs.producer_dispatch_token || '' }}", text)
        self.assertIn("-f dispatch_token='${{ github.run_id }}'", text)

    def test_async_mode_falls_back_to_sync_when_kernel_is_already_active(self):
        text = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        self.assertIn("env.ASYNC_SUBMIT != 'true' || steps.kernel-state.outputs.reuse == 'true'", text)
        self.assertIn("env.ASYNC_SUBMIT == 'true' && steps.kernel-state.outputs.reuse != 'true'", text)

    def test_async_preflight_failure_returns_dispatch_to_autofactory(self):
        text = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        self.assertIn("Recover async preflight failure", text)
        self.assertIn("failure() && env.ASYNC_SUBMIT == 'true'", text)
        self.assertIn("producer_conclusion='failure'", text)
        self.assertIn('producer_dispatch_token="${DISPATCH_TOKEN:-}"', text)
    def test_push_triggered_kaggle_wave_is_async_and_preserves_dispatch_owner(self):
        text = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        self.assertIn("Resolve push-triggered async wave", text)
        self.assertIn("ASYNC_SUBMIT:", text)
        self.assertIn("DISPATCH_TOKEN:", text)
        self.assertIn("tokens={str(by[i].get('dispatch_token') or '')", text)
        self.assertIn("SPRITE_COUNT='+str(min(12,len(ids)))", text)

    def test_character_promotion_accepts_async_collector_artifact_and_can_continue_factory(self):
        text = Path(".github/workflows/promote-approved-kaggle-characters.yml").read_text(encoding="utf-8")
        self.assertIn("actions: write", text)
        self.assertIn("kaggle-async-character-batch", text)

    def test_character_promotion_requires_android_runtime_validation_before_done(self):
        text = Path(".github/workflows/promote-approved-kaggle-characters.yml").read_text(encoding="utf-8")
        self.assertIn("Validate promoted Android runtime", text)
        self.assertIn("gradle assembleDebug --stacktrace", text)
        self.assertIn("Mark approved characters strict DONE", text)
        self.assertLess(text.index("Validate promoted Android runtime"), text.index("Mark approved characters strict DONE"))
        self.assertIn("Continue autofactory after promotion", text)
    def test_async_collector_recovers_candidates_when_generated_targets_is_empty(self):
        text = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("character-sheet-report.json", text)
        self.assertIn("candidate_dir=Path('/tmp/kaggle-output/output/candidates')", text)
        self.assertIn("candidate_dir.glob('*_final.png')", text)
        self.assertIn("ops/kaggle-collector-trigger.txt", text)

    def test_kaggle_bundle_tree_fallback_finds_nested_repo_bundle(self):
        text = Path("kaggle/github_mass_factory.py").read_text(encoding="utf-8")
        self.assertIn("base.glob('**/repo_bundle')", text)
        self.assertIn("base.glob('**/docs/art/FINAL_AAA_SPRITE_MANIFEST.md')", text)
        self.assertIn("KAGGLE_BUNDLE_TREE_FALLBACK=", text)
    def test_async_character_wave_reuses_dataset_with_inline_queue_overlay(self):
        mass = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        factory = Path("kaggle/github_mass_factory.py").read_text(encoding="utf-8")
        self.assertIn("QUEUE_OVERLAY_B64=''", factory)
        self.assertIn("KAGGLE_KERNEL_QUEUE_OVERLAY=inline-payload", factory)
        self.assertIn("Failed to inject QUEUE_OVERLAY_B64", mass)
        self.assertIn("KAGGLE_DATASET_ASYNC_REUSE=1", mass)
    def test_kaggle_kernel_title_resolves_to_requested_slug(self):
        text = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        self.assertIn("d['title']=os.environ['KAGGLE_KERNEL_SLUG'].replace('-',' ')", text)
    def test_async_collector_captures_failed_kernel_evidence(self):
        text = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("Download failed kernel evidence", text)
        self.assertIn("kaggle kernels output", text)
        self.assertIn("kaggle-async-failure-evidence-", text)
        self.assertLess(text.index("Download failed kernel evidence"), text.index("Callback autofactory failure"))
    def test_async_kaggle_uses_unique_kernel_slug_and_stale_timeout(self):
        mass = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        collector = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("Resolve Kaggle kernel slug", mass)
        self.assertIn("KAGGLE_KERNEL_FULL", mass)
        self.assertIn("'kernel_slug':os.environ.get('KAGGLE_KERNEL_SLUG'", mass)
        self.assertIn("150*60", collector)
        self.assertIn("KAGGLE_ASYNC_STALE=1", collector)
        self.assertIn("FAILED_STALE", collector)
    def test_async_kaggle_character_mode_releases_runner_and_uses_collector(self):
        mass = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        autof = Path(".github/workflows/asset-autofactory.yml").read_text(encoding="utf-8")
        collector = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("async_submit:", mass)
        self.assertIn("env.ASYNC_SUBMIT != 'true'", mass)
        self.assertIn("kaggle-async-state.json", mass)
        self.assertIn("-f async_submit=true", autof)
        self.assertIn("kaggle-async-state.json", autof)
        self.assertIn("cron: '*/5 * * * *'", collector)
        self.assertIn("Callback autofactory success", collector)

    def test_kaggle_character_all_reject_batch_is_not_infrastructure_failure(self):
        text = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        self.assertIn("KAGGLE_CHARACTER_CLEAN_REJECT_BATCH", text)
        self.assertIn("complete character rejection report", text)

    def test_kaggle_character_reconciliation_handles_partial_rejects(self):
        path = Path(".github/workflows/kaggle-mass-sprite-factory.yml")
        text = path.read_text(encoding="utf-8")
        self.assertIn("character-sheet-report.json", text)
        self.assertIn("item['status']='REJECTED'", text)
        self.assertIn("CONTROLLED_CHARACTER_REJECTED=", text)

    def test_kaggle_character_generator_rejects_source_fragments_before_resize(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("def validate_source_full_body", text)
        self.assertIn("source subject too short", text)
        self.assertIn("source edge contact", text)
        self.assertIn("finish_frame(raw,i['action'])", text)

    def test_kaggle_character_generator_has_clean_main_tail(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertTrue(text.rstrip().endswith("if __name__=='__main__':main()"))
        self.assertNotIn("main(       if fi==0", text)

    def test_kaggle_character_generator_adds_semantic_scaffolds_for_hard_actions(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("def semantic_scaffold(source,action):", text)
        self.assertIn("action not in {'CARRY','WORK','REPAIR'}", text)
        self.assertIn("source=semantic_scaffold(shared,i['action'])", text)
        self.assertIn("ImageDraw", text)

    def test_kaggle_character_generator_uses_neutral_role_anchor(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("def anchor_prompt_pair(role):", text)
        self.assertIn("KAGGLE_CHR_CANONICAL_ROLE_ANCHOR=", text)
        self.assertIn("shared=role_anchor[i['role']]", text)
        self.assertNotIn("KAGGLE_CHR_IDENTITY_ANCHOR=", text)

    def test_kaggle_rejection_memory_prefers_exact_asset_over_role_fallback(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("exact=str(row.get('id','')).upper()", text)
        self.assertIn("if exact:", text)
        self.assertIn("matched=exact==i['id']", text)
        self.assertIn("elif prefix:", text)
        self.assertIn("(not action or action==i['action'])", text)


if __name__ == "__main__":
    unittest.main()
