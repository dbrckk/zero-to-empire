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

    def test_strict_completion_mode_is_not_pinned_to_one_generator_version(self):
        text = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        self.assertIn("mode.startswith('kaggle-character-burst-v1.')", text)
        self.assertIn("'strict-completion' in mode", text)
        self.assertNotIn("startswith('kaggle-character-burst-v1.16')", text)

    def test_character_promotion_accepts_async_collector_artifact_and_can_continue_factory(self):
        text = Path(".github/workflows/promote-approved-kaggle-characters.yml").read_text(encoding="utf-8")
        self.assertIn("actions: write", text)
        self.assertIn("kaggle-async-character-batch", text)

    def test_character_promotion_can_resolve_source_artifact_run_from_queue(self):
        text = Path(".github/workflows/promote-approved-kaggle-characters.yml").read_text(encoding="utf-8")
        self.assertIn("default: 'auto'", text)
        self.assertIn("review_artifact_run_id", text)
        self.assertIn("Automatic source run resolution requires one shared review_artifact_run_id", text)

    def test_character_promotion_allows_only_reviewed_same_run_idle_replacement(self):
        text = Path(".github/workflows/promote-approved-kaggle-characters.yml").read_text(encoding="utf-8")
        self.assertIn("include the same-run IDLE anchor", text)
        self.assertIn("not str(aid).endswith('-IDLE')", text)
        self.assertIn("unreviewed-context-anchor", text)
        self.assertIn("context.get('status')!='AWAITING_REVIEW'", text)
        self.assertIn("context.get('review_artifact_run_id')", text)
        self.assertIn("item.get('autofactory_context_only')", text)

    def test_character_promotion_requires_pending_review_and_coherent_anchor(self):
        text = Path(".github/workflows/promote-approved-kaggle-characters.yml").read_text(encoding="utf-8")
        self.assertIn("not-current-reviewed-candidate", text)
        self.assertIn("str(recorded or '')!=source", text)
        self.assertIn("missing-coherent-", text)
        self.assertIn("approved_anchor=(", text)
        self.assertIn("a['review_artifact_run_id']=int(os.environ['SOURCE_RUN_ID'])", text)
        self.assertIn("unknown-asset", text)

    def test_character_promotion_rejects_wrong_artifact_provenance(self):
        text = Path(".github/workflows/promote-approved-kaggle-characters.yml").read_text(encoding="utf-8")
        self.assertIn("Promotion source run does not match canonical review provenance", text)
        self.assertIn("PROMOTION_SOURCE_PROVENANCE_PASS=", text)

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
        self.assertIn("workflow_dispatch:", text)
        # Historical collector can be manually dispatched only. The user's
        # remaining sprites are now original, authored locally in ChatGPT.
        header=text.split("\npermissions:",1)[0]
        self.assertNotIn("\n  schedule:",header)
        self.assertNotIn("\n  push:",header)
        self.assertIn("cancel-in-progress: false", text)

    def test_action_translation_reviewer_precedes_candidate_promotion(self):
        collector = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        verifier = Path("tools/sprites/verify_character_action_candidates.py").read_text(encoding="utf-8")
        self.assertIn("verify_character_action_candidates.py", collector)
        self.assertLess(collector.index("verify_character_action_candidates.py"),
                        collector.index("Reconcile controlled character queue"))
        self.assertIn("ACTION_TRANSLATION_DOMINATES_POSE_RISK", Path(
            "tools/sprites/character_semantic_gate.py").read_text(encoding="utf-8"))
        self.assertIn("if details[\"risk_level\"] == \"BLOCKING\":", verifier)
        self.assertNotIn("strict_status", verifier)
        self.assertNotIn("app/src/main/res/", verifier)
        generator = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("action_translation_dominates_pose_risk", generator)
        self.assertIn("head-excursion-px=", collector)
        self.assertIn("retained-pose-motion-ratio=", collector)

    def test_async_collector_keeps_valid_candidates_when_other_qa_rows_fail(self):
        text = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("incomplete/duplicate technical QA coverage", text)
        self.assertIn("KAGGLE_ASYNC_QA_REJECT=", text)
        self.assertIn("produced.discard(aid)", text)
        self.assertIn("rejected[aid]='technical-qa:'", text)
        self.assertNotIn("if failed: raise SystemExit('technical QA rejected:", text)

    def test_async_collector_requires_full_expected_target_coverage(self):
        text = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("missing=expected-actual", text)
        self.assertIn("incomplete/stale Kaggle output", text)
        self.assertNotIn("if expected and not (expected & actual)", text)

    def test_async_collector_preserves_retry_details_for_future_generation(self):
        text = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("retry-details=", text)
        self.assertIn("row.get('retry_reasons',[])", text)
        self.assertIn("dict.fromkeys(retries[-4:])", text)

    def test_async_collector_does_not_cancel_in_progress_evidence_download(self):
        text = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("group: kaggle-async-character-collector", text)
        self.assertIn("cancel-in-progress: false", text)

    def test_async_collector_allows_large_role_bursts_to_finish(self):
        workflow = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("target_count=len(d.get('target_ids') or [])", workflow)
        self.assertIn("stale_limit_minutes=600 if target_count >= 10 else 420", workflow)
        self.assertIn("stale_limit_minutes*60", workflow)
        self.assertIn("queued_stale_limit_minutes=1440", workflow)
        self.assertIn("queued_stale=elapsed > queued_stale_limit_minutes*60", workflow)
        self.assertIn("steps.gate.outputs.queued_stale", workflow)
        self.assertIn("KAGGLE_ASYNC_QUEUE_TIMEOUT=1", workflow)
        self.assertNotIn("'RUNNING|QUEUED'", workflow)
        self.assertNotIn("total_seconds() > 150*60", workflow)

    def test_async_collector_releases_wave_when_completed_output_validation_fails(self):
        text = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        condition = "steps.kernel.outputs.failed == 'true' || (steps.kernel.outputs.ready == 'true' && failure())"
        self.assertGreaterEqual(text.count(condition), 3)
        self.assertIn("Callback autofactory failure", text)

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
    def test_async_kernel_slug_changes_when_character_generator_changes(self):
        text = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        self.assertIn("generator_tag=hashlib.sha256(generator.read_bytes()).hexdigest()[:8]", text)
        self.assertIn("{token}-{generator_tag}", text)
        self.assertIn("KAGGLE_KERNEL_GENERATOR_TAG=", text)
    def test_kaggle_kernel_title_resolves_to_requested_slug(self):
        text = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        self.assertIn("d['title']=os.environ['KAGGLE_KERNEL_SLUG'].replace('-',' ')", text)
    def test_async_collector_captures_failed_kernel_evidence(self):
        text = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("Download failed kernel evidence", text)
        self.assertIn("kaggle kernels output", text)
        self.assertIn("kaggle-async-failure-evidence-", text)
        self.assertLess(text.index("Download failed kernel evidence"), text.index("Callback autofactory failure"))
    def test_async_collector_persists_kernel_observation_even_before_completion(self):
        text = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("kaggle-async-kernel-observation-", text)
        self.assertIn("/tmp/kaggle-kernel-status.txt", text)
        self.assertIn("Upload kernel observation", text)

    def test_superseded_kaggle_wave_evidence_is_review_only(self):
        text = Path(".github/workflows/kaggle-superseded-character-evidence.yml").read_text(encoding="utf-8")
        self.assertIn("kaggle-async-orphan-waves.json", text)
        self.assertIn("kaggle-superseded-character-batch-", text)
        self.assertIn("build_character_review_panels.py", text)
        self.assertIn("'ARTIFACT_COLLECTED_REVIEW_ONLY'", text)
        self.assertIn("automatic_strict_promotion", text)
        self.assertNotIn("master-asset-queue.json", text)
        self.assertNotIn("strict_status", text)

    def test_local_first_art_has_no_automatic_external_generator_schedule(self):
        # The user requires the remaining original sprites to be authored in
        # ChatGPT, not regenerated remotely by periodic GitHub Actions.
        workflows = [
            ".github/workflows/pollinations-character-atlas.yml",
            ".github/workflows/pollinations-building-candidate.yml",
            ".github/workflows/manifest-static-gpu-batch.yml",
            ".github/workflows/kaggle-async-character-collector.yml",
            ".github/workflows/kaggle-superseded-character-evidence.yml",
            ".github/workflows/kaggle-mass-sprite-factory.yml",
            ".github/workflows/pollinations-character-smoke.yml",
        ]
        for path in workflows:
            with self.subTest(workflow=path):
                text = Path(path).read_text(encoding="utf-8")
                header = text.split("\npermissions:", 1)[0]
                self.assertIn("  workflow_dispatch:", header)
                self.assertNotIn("\n  schedule:", header)
                self.assertNotIn("\n  push:", header)

    def test_mass_gpu_preflight_blocks_duplicate_active_waves(self):
        text = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        self.assertIn("jobs:\n  preflight:", text)
        self.assertIn("KAGGLE_DUPLICATE_WAVE_PREVENTED=1", text)
        self.assertIn("needs: preflight", text)
        self.assertIn("if: needs.preflight.outputs.permitted == 'true'", text)
        self.assertNotIn("      - 'kaggle/github_mass_factory.py'", text)
        self.assertNotIn("      - 'kaggle/kernel-metadata.template.json'", text)

    def test_async_kaggle_uses_unique_kernel_slug_and_stale_timeout(self):
        mass = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        collector = Path(".github/workflows/kaggle-async-character-collector.yml").read_text(encoding="utf-8")
        self.assertIn("Resolve Kaggle kernel slug", mass)
        self.assertIn("KAGGLE_KERNEL_FULL", mass)
        self.assertIn("'kernel_slug':os.environ.get('KAGGLE_KERNEL_SLUG'", mass)
        self.assertIn("stale_limit_minutes*60", collector)
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
        self.assertNotIn("cron: '*/5 * * * *'", collector)
        self.assertIn("workflow_dispatch:", collector)
        self.assertNotIn("  schedule:", autof)
        self.assertNotIn("  workflow_run:", autof)
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

    def test_kaggle_character_generator_reapplies_scaffold_each_frame(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("source=semantic_scaffold(anchor_raw,i['action'],fi)", text)
        self.assertIn("character-sheet-flux-v1.20-stable-idle-breathing-rescue", text)
    def test_kaggle_character_generator_adds_semantic_scaffolds_for_hard_actions(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("def semantic_scaffold(source,action,frame_index=0):", text)
        self.assertIn("action not in {'CARRY','WORK','REPAIR'}", text)
        self.assertIn("source=semantic_scaffold(shared,i['action'],fi)", text)
        self.assertIn("ImageDraw", text)

    def test_character_qa_requires_carry_stride_and_progressive_celebration(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("carry-lacks-stride lower-motion=", text)
        self.assertIn("changes=upper_body_transition_changes(frames)", text)
        self.assertIn("expressive=sum(delta>=.15 for delta in changes)", text)
        self.assertIn("celeb-unreadable-gesture upper-transitions=", text)
        self.assertIn("celeb-upper-silhouette-jump=", text)
        self.assertIn("arms=celebration_arm_reach_counts(frames)", text)
        self.assertIn("celeb-no-progressive-arm-raise active-frames=", text)

    def test_carry_scaffold_adds_deterministic_lower_body_motion(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("phase=(0,1,2,1,0,-1,-2,-1)[frame_index%8]", text)
        self.assertIn("shear=phase*.060", text)
        self.assertIn("deterministic", text)
        self.assertIn("lower=out.crop((0,hip_y,w,h))", text)

    def test_character_role_anchor_is_validated_before_action_frames(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("for anchor_attempt in range(4):", text)
        self.assertIn("coverage=validated_single_role_anchor(candidate)", text)
        self.assertIn("coverage=validated_single_role_anchor(single)", text)
        self.assertIn("coverage=validated_single_role_anchor(fallback)", text)
        self.assertIn("idle_distinct_head_clusters(cell)>=2", text)
        self.assertIn("multiple-idle-heads-in-canonical-role-anchor", text)
        self.assertIn("KAGGLE_CHR_ROLE_ANCHOR_REJECTED=", text)
        self.assertIn("'reason':'role-anchor-validation-failed'", text)
        self.assertLess(text.index("coverage=validated_single_role_anchor(candidate)"),
                        text.index("for idx,i in enumerate(items):"))

    def test_headgear_lock_never_uses_an_unverified_non_idle_reference(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("and i['role'] in verified_idle_roles", text)
        self.assertIn("frame,locked,lock_note=lock_head_to_idle", text)
        self.assertIn("'same_run_idle_head_locked_frames':head_lock_frames", text)

    def test_idle_edge_retries_preserve_validated_anchor(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertEqual(text.count("if i['action']=='IDLE' and mode=='framing':"),2)
        self.assertIn("strength=min(strength,.23)",text)
        self.assertIn("strength=min(strength,.21)",text)
        self.assertIn("required-role-idle-candidate-rejected",text)

    def test_idle_animation_gate_accepts_blinks_without_fake_locomotion(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("from character_semantic_gate import clip_risk,idle_visual_activity", text)
        self.assertIn("activity=idle_visual_activity(frames)", text)
        self.assertIn("mean_change<.008 and activity<.00035", text)
        self.assertIn("idle-frozen alpha-motion=", text)
        self.assertNotIn("'IDLE':.025", text)

    def test_same_run_idle_identity_is_required_before_sibling_render(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("required_idle_roles={item['role'] for item in items if item['action']=='IDLE'}", text)
        self.assertIn("i['role'] not in verified_idle_roles", text)
        self.assertIn("required-role-idle-candidate-rejected", text)
        self.assertIn("verified_idle_roles.add(i['role'])", text)
        self.assertLess(text.index("required-role-idle-candidate-rejected"), text.index("frames=[];anchor_raw=None"))

    def test_malformed_character_visual_qa_does_not_abort_valid_gpu_siblings(self):
        code = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("except (ValueError, IndexError, OSError) as exc:", code)
        self.assertIn("candidate-visual-qa-error:", code)
        self.assertIn("'status':'REJECT','reason':reason", code)
        self.assertLess(code.index("except (ValueError, IndexError, OSError) as exc:"),
                        code.index("if visual_risk.get('risk_level')=='BLOCKING':"))

    def test_kaggle_character_generator_rejects_blocking_visual_risks(self):
        generator = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        workflow = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        self.assertIn("from character_semantic_gate import clip_risk", generator)
        self.assertIn("visual_risk=clip_risk(frames,i['action'])", generator)
        self.assertIn("risk_level')=='BLOCKING", generator)
        self.assertIn("character_semantic_gate.py", workflow)

    def test_rejected_idle_images_are_isolated_from_promotable_candidates(self):
        generator = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        gpu = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        fallback = Path("kaggle/github_mass_factory.py").read_text(encoding="utf-8")
        diagnostic = Path("tools/sprites/character_rejection_evidence.py").read_text(encoding="utf-8")
        self.assertIn("from character_rejection_evidence import save_rejected_idle_preview", generator)
        self.assertIn("character-rejection-previews", generator)
        self.assertIn("'rejection_preview_file':preview", generator)
        self.assertIn("character_rejection_evidence.py", gpu)
        self.assertIn("'character_rejection_evidence.py'", fallback)
        self.assertIn('"strict_promotion_permitted": False', diagnostic)
        self.assertNotIn("INCOMING", diagnostic)

    def test_kaggle_head_identity_lock_is_present_in_all_gpu_fallbacks(self):
        generator = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        workflow = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        fallback = Path("kaggle/github_mass_factory.py").read_text(encoding="utf-8")
        self.assertIn("from character_head_identity_lock import lock_head_to_idle", generator)
        self.assertIn("character_head_identity_lock.py", workflow)
        self.assertIn("'character_head_identity_lock.py'", fallback)
        self.assertIn("and i['role'] in verified_idle_roles", generator)
        self.assertIn("unsafe-head-silhouette-overlap", Path(
            "tools/sprites/character_head_identity_lock.py").read_text(encoding="utf-8"))

    def test_strict_done_idle_fallback_is_included_in_all_kaggle_code_paths(self):
        generator = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        workflow = Path(".github/workflows/kaggle-mass-sprite-factory.yml").read_text(encoding="utf-8")
        fallback = Path("kaggle/github_mass_factory.py").read_text(encoding="utf-8")
        self.assertIn("from character_approved_idle_fallback import load_approved_idle_anchor", generator)
        self.assertIn("fallback,source_note=load_approved_idle_anchor(role,MANIFEST,INCOMING)", generator)
        self.assertIn("character_approved_idle_fallback.py", workflow)
        self.assertIn("'character_approved_idle_fallback.py'", fallback)
        self.assertIn("source-idle-not-uniquely-strict-done", Path(
            "tools/sprites/character_approved_idle_fallback.py").read_text(encoding="utf-8"))

    def test_kaggle_character_generator_uses_neutral_role_anchor(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("def anchor_prompt_pair(role):", text)
        self.assertIn("KAGGLE_CHR_CANONICAL_ROLE_ANCHOR=", text)
        self.assertIn("shared=role_anchor[i['role']]", text)
        self.assertNotIn("KAGGLE_CHR_IDENTITY_ANCHOR=", text)

    def test_recent_semantic_defect_survives_rejection_prompt_budget(self):
        # Extract pure helper as AST; importing the full GPU generator would
        # unnecessarily load torch/diffusers into this CPU-only CI check.
        import ast
        code = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        nodes = ast.parse(code).body
        node = next(x for x in nodes if isinstance(x, ast.FunctionDef)
                    and x.name == "compact_rejection_hints")
        namespace = {}
        exec(compile(ast.Module(body=[node],type_ignores=[]),
                     "<character-rejection-budget>", "exec"), namespace)
        fn = namespace["compact_rejection_hints"]
        older = "Older broad palette risk instruction " * 20
        latest = "MOST_RECENT_CRATE_SHAPE must remain unchanged in every frame " * 6
        generic = "QUEUE_DIAGNOSIS preserve actual grip and same role identity " * 5
        result = fn([older,latest],generic)
        self.assertTrue(result.startswith("MOST_RECENT_CRATE_SHAPE"))
        self.assertIn("QUEUE_DIAGNOSIS",result)
        self.assertLessEqual(len(result.split()),72)
        self.assertEqual(fn([],""),"")
        with self.assertRaises(ValueError):
            fn([latest],generic,max_words=0)

    def test_kaggle_rejection_memory_prefers_exact_asset_over_role_fallback(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("exact=str(row.get('id','')).upper()", text)
        self.assertIn("if exact:", text)
        self.assertIn("matched=exact==i['id']", text)
        self.assertIn("elif prefix:", text)
        self.assertIn("(not action or action==i['action'])", text)

    def test_kaggle_character_retry_uses_controlled_queue_rejection_risks(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("def queue_rejection_hint(i):", text)
        self.assertIn("palette_identity_discontinuity", text)
        self.assertIn("silhouette_mass_discontinuity", text)
        self.assertIn("walk-too-static", text)
        self.assertIn("carry-too-static", text)
        self.assertIn("detached-artifact", text)
        self.assertIn("qhint=queue_rejection_hint(i)", text)

    def test_kaggle_character_retry_routes_detached_subject_to_single_mode(self):
        text = Path("tools/sprites/kaggle_character_sheet_factory_v1.py").read_text(encoding="utf-8")
        self.assertIn("or 'detached-artifact' in r:return 'single'", text)
        self.assertIn("or 'bad border' in r:return 'framing'", text)


if __name__ == "__main__":
    unittest.main()
