"""Regression tests for six TECH runtime review atlases.

Run AFTER the six-clip generator in CI; independently audit its real pixels.
"""
from __future__ import annotations
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image
from package_tech_actions_runtime import (ACTIONS, package, verify, game_scale_metrics,
                                         verify_temporal_evidence)
from temporal_sprite_audit import audit

FIXTURE=Path('build/tech-actions-v3').resolve()


class RuntimePackTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(FIXTURE.is_dir(),f'Six-action build missing: {FIXTURE}')

    def test_six_atlases_keep_the_review_gate(self):
        with tempfile.TemporaryDirectory() as temp:
            out=Path(temp)/'runtime'
            temporal_dir=Path(temp)/'temporal'
            audit(FIXTURE,temporal_dir)
            report_file=temporal_dir/'temporal-qa.json'
            manifest=package(FIXTURE,out,temporal_report=report_file)
            self.assertTrue(manifest['temporal_evidence_verified'])
            self.assertEqual(manifest['temporal_evidence_format'],'zte-temporal-qa-v1')
            bad=json.loads(report_file.read_text())
            bad['actions']['WORK']['ordered_frame_digest_sha256']='0'*64
            bad_file=Path(temp)/'stale-temporal.json'
            bad_file.write_text(json.dumps(bad))
            index,records=verify(FIXTURE)
            with self.assertRaisesRegex(ValueError,'Stale or mismatched temporal evidence'):
                verify_temporal_evidence(index,records,bad_file)
            self.assertEqual(tuple(manifest['animations']),ACTIONS)
            self.assertEqual(sum(v['frames'] for v in manifest['animations'].values()),144)
            self.assertFalse(manifest['visual_review_pass'])
            self.assertFalse(manifest['semantic_review_pass'])
            self.assertFalse(manifest['integrated_into_game'])
            self.assertFalse(manifest['approved_for_release'])
            self.assertEqual(manifest['strict_status'],'NEEDS_REVIEW')
            focus=manifest['focused_camera']
            self.assertTrue(focus['optional_review_variant_only'])
            self.assertEqual(focus['world_pivot_px'],[252,449])
            self.assertGreaterEqual(focus['zoom_factor'],1.0)
            self.assertLessEqual(focus['zoom_factor'],1.30)
            self.assertEqual(len(focus['shared_crop_bounds_px']),4)
            self.assertEqual(
                len(list((out/'focused-atlases').glob('*.png'))),24)
            self.assertTrue((out/'REVIEW_REQUIRED.txt').exists())
            self.assertEqual(len(list((out/'atlases').glob('*.png'))),24)
            with Image.open(out/'review-focused-all-actions-96.png') as focused:
                self.assertEqual(focused.size,(888,688))
                self.assertEqual(focused.mode,'RGB')
            with Image.open(out/'review-all-actions-96.png') as contact:
                self.assertEqual(contact.size,(888,688))
                self.assertEqual(contact.mode,'RGB')
            for action,item in manifest['animations'].items():
                self.assertEqual(item['strict_status'],'NEEDS_REVIEW')
                self.assertEqual(item['reference_pivot_px'],[252,449])
                for size in (96,128):
                    variant=item['focused_variants'][str(size)]
                    shadow=item['optional_shadow_layer']['focused_variants'][str(size)]
                    self.assertEqual(variant['shared_crop_bounds_px'],
                                     focus['shared_crop_bounds_px'])
                    crop=variant['shared_crop_bounds_px']
                    expected_pivot=[round((252-crop[0])*size/(crop[2]-crop[0]),3),
                                    round((449-crop[1])*size/(crop[2]-crop[0]),3)]
                    self.assertEqual(variant['pivot_px'],expected_pivot)
                    with Image.open(out/variant['path']) as atlas:
                        self.assertEqual(atlas.mode,'RGBA')
                        self.assertEqual(atlas.size,(size*6,size*4))
                    with Image.open(out/shadow['path']) as layer:
                        self.assertEqual(layer.mode,'RGBA')
                        self.assertEqual(layer.size,(size*6,size*4))
                self.assertFalse(item['optional_shadow_layer']['default_enabled'])
                self.assertEqual(item['collision_boxes_status'],
                                 'NOT_DEFINED_REQUIRES_GAMEPLAY_REVIEW')
                self.assertEqual(len(item['per_frame_visual_bounds_px']),24)
                self.assertTrue(item['game_scale_96px_technical_pass'])
                self.assertTrue(item['review_required'])
                self.assertEqual(item['strict_status'],'NEEDS_REVIEW')
                self.assertEqual(len(item['game_scale_96px_metrics']),24)
                for m in item['game_scale_96px_metrics']:
                    self.assertTrue(m['pass'],m)
                    self.assertGreaterEqual(m['opaque_pixels'],500)
                    self.assertGreaterEqual(m['min_edge_margin'],3)
                self.assertEqual(len(json.loads((out/item['events_file']).read_text())),24)
                for size in (128,256):
                    var=item['variants'][str(size)]
                    self.assertEqual(var['pivot_px'],
                                     [round(252*size/512,3),round(449*size/512,3)])
                    with Image.open(out/var['path']) as image:
                        self.assertEqual(image.size,(size*6,size*4))
                        self.assertEqual(image.mode,'RGBA')
                        self.assertEqual(image.getpixel((0,0))[3],0)
                    shadow=item['optional_shadow_layer']['variants'][str(size)]
                    with Image.open(out/shadow['path']) as layer:
                        self.assertEqual(layer.size,(size*6,size*4))
                        self.assertEqual(layer.mode,'RGBA')
                        self.assertIsNotNone(layer.getchannel('A').getbbox())
            player=(out/'review-player.html').read_text()
            self.assertIn('requestAnimationFrame',player)
            self.assertIn('value="96"',player)
            self.assertIn('id="showShadows"',player)
            self.assertNotIn('id="showShadows" type="checkbox" checked',player)
            self.assertIn('id="pause"',player)
            self.assertIn('id="framing"',player)
            self.assertIn('focus_src',player)
            self.assertIn('focused',player)
            self.assertIn('focusShadow',player)
            self.assertIn('showShadows&&c.shadowReady',player)

    def test_game_scale_check_rejects_clipped_or_empty_frames(self):
        from PIL import ImageDraw
        empty=Image.new('RGBA',(512,512))
        self.assertFalse(game_scale_metrics(empty)['pass'])
        clipped=Image.new('RGBA',(512,512))
        ImageDraw.Draw(clipped).rectangle((0,0,290,500),fill=(255,255,255,255))
        self.assertFalse(game_scale_metrics(clipped)['pass'])
        with Image.open(FIXTURE/'WALK'/'frames'/'CHR-TECH-WALK-00.png') as image:
            self.assertTrue(game_scale_metrics(image.convert('RGBA'))['pass'])

    def test_source_contract_has_shared_skin_and_event_timeline(self):
        index,records=verify(FIXTURE)
        self.assertEqual(index['format'],'zte-modular-actions-v3')
        self.assertEqual(len({r['count'] for r in records.values()}),1)
        for action in ACTIONS:
            self.assertEqual(len(records[action]['events']),24)

    def test_reject_approved_or_corrupted_index(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            source=json.loads((FIXTURE/'production-index.json').read_text())
            source['strict_status']='DONE'
            (root/'production-index.json').write_text(json.dumps(source))
            with self.assertRaisesRegex(ValueError,'review gate'):
                verify(root)

    def test_reject_missing_review_marker(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/'production-index.json').write_bytes(
                (FIXTURE/'production-index.json').read_bytes())
            for action in ACTIONS:
                if action!='WALK':
                    (root/action).symlink_to(FIXTURE/action,target_is_directory=True)
            (root/'WALK').mkdir()
            for name in ('qa-manifest.json','frame-poses.json','footstep-events.json'):
                (root/'WALK'/name).symlink_to(FIXTURE/'WALK'/name)
            with self.assertRaisesRegex(ValueError,'Missing review marker'):
                verify(root)

    def test_refuse_desynchronized_visual_events(self):
        for action,event_kind,expected in (
            ('WORK','data-update','WORK pulse event/visual phase mismatch'),
            ('REPAIR','weld-sparks','REPAIR spark event/visual phase mismatch')):
            with self.subTest(action=action),tempfile.TemporaryDirectory() as temp:
                root=Path(temp)
                (root/'production-index.json').write_bytes(
                    (FIXTURE/'production-index.json').read_bytes())
                for other in ACTIONS:
                    if other != action:
                        (root/other).symlink_to(FIXTURE/other,target_is_directory=True)
                (root/action).mkdir()
                for name in ('qa-manifest.json','frame-poses.json','REVIEW_REQUIRED.txt'):
                    (root/action/name).symlink_to(FIXTURE/action/name)
                (root/action/'frames').symlink_to(FIXTURE/action/'frames',target_is_directory=True)
                events=json.loads((FIXTURE/action/'footstep-events.json').read_text())
                changed=next(i for i,e in enumerate(events) if e.get('vfx_event')==event_kind)
                events[changed]['vfx_event']=None
                (root/action/'footstep-events.json').write_text(json.dumps(events))
                with self.assertRaisesRegex(ValueError,expected):
                    verify(root)

    def test_reject_narrow_celebration_pose(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/'production-index.json').write_bytes(
                (FIXTURE/'production-index.json').read_bytes())
            for action in ACTIONS:
                if action!='CELEB':
                    (root/action).symlink_to(FIXTURE/action,target_is_directory=True)
            (root/'CELEB').mkdir()
            manifest=json.loads((FIXTURE/'CELEB'/'qa-manifest.json').read_text())
            manifest['qa']['celebration_min_wrist_span_px']=20
            (root/'CELEB'/'qa-manifest.json').write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError,'Celebration arms not separated from head'):
                verify(root)

    def test_reject_celebration_below_overhead_qa_threshold(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/'production-index.json').write_bytes(
                (FIXTURE/'production-index.json').read_bytes())
            for action in ACTIONS:
                if action!='CELEB':
                    (root/action).symlink_to(FIXTURE/action,target_is_directory=True)
            (root/'CELEB').mkdir()
            manifest=json.loads((FIXTURE/'CELEB'/'qa-manifest.json').read_text())
            manifest['qa']['celebration_min_arm_raise_px']=10
            (root/'CELEB'/'qa-manifest.json').write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError,'Celebration arms not visibly overhead'):
                verify(root)

    def test_reject_mismatched_work_and_repair_contacts(self):
        for action in ('WORK','REPAIR'):
            with self.subTest(action=action),tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp)
                (root/'production-index.json').write_bytes(
                    (FIXTURE/'production-index.json').read_bytes())
                for other in ACTIONS:
                    if other!=action:
                        (root/other).symlink_to(FIXTURE/other,target_is_directory=True)
                (root/action).mkdir()
                manifest=json.loads((FIXTURE/action/'qa-manifest.json').read_text())
                manifest['qa']['interaction_contact_pass']=False
                (root/action/'qa-manifest.json').write_text(json.dumps(manifest))
                with self.assertRaisesRegex(ValueError,'Interaction contact QA failed'):
                    verify(root)

    def test_reject_mismatched_phase_and_transfer_provenance(self):
        for action,field,expected in (
            ('WORK','phase_origin_frame','Unexpected loop phase origin'),
            ('WALK','weight_transfer','Missing weight-transfer provenance')):
            with self.subTest(action=action),tempfile.TemporaryDirectory() as temp:
                root=Path(temp)
                (root/'production-index.json').write_bytes(
                    (FIXTURE/'production-index.json').read_bytes())
                for other in ACTIONS:
                    if other!=action:
                        (root/other).symlink_to(FIXTURE/other,target_is_directory=True)
                (root/action).mkdir()
                manifest=json.loads((FIXTURE/action/'qa-manifest.json').read_text())
                manifest.pop(field,None)
                (root/action/'qa-manifest.json').write_text(json.dumps(manifest))
                with self.assertRaisesRegex(ValueError,expected):
                    verify(root)

    def test_reject_missing_fabric_renderer_provenance(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'production-index.json').write_bytes(
                (FIXTURE/'production-index.json').read_bytes())
            for action in ACTIONS:
                if action != 'WORK':
                    (root/action).symlink_to(FIXTURE/action,target_is_directory=True)
            (root/'WORK').mkdir()
            manifest=json.loads((FIXTURE/'WORK'/'qa-manifest.json').read_text())
            manifest.pop('renderer_features',None)
            (root/'WORK'/'qa-manifest.json').write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError,'Renderer feature provenance missing'):
                verify(root)

    def test_reject_soft_deformation_disabled_in_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'production-index.json').write_bytes(
                (FIXTURE/'production-index.json').read_bytes())
            for action in ACTIONS:
                if action != 'WALK':
                    (root/action).symlink_to(FIXTURE/action,target_is_directory=True)
            (root/'WALK').mkdir()
            manifest=json.loads((FIXTURE/'WALK'/'qa-manifest.json').read_text())
            manifest['renderer_features']['soft_deform']=False
            (root/'WALK'/'qa-manifest.json').write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError,'Renderer feature provenance missing'):
                verify(root)

    def test_reject_falsely_approved_visual_qa(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/'production-index.json').write_bytes(
                (FIXTURE/'production-index.json').read_bytes())
            for action in ACTIONS:
                if action!='WALK':
                    (root/action).symlink_to(FIXTURE/action,target_is_directory=True)
            (root/'WALK').mkdir()
            qa=json.loads((FIXTURE/'WALK'/'qa-manifest.json').read_text())
            qa['qa']['semantic_review_pass']=True
            (root/'WALK'/'qa-manifest.json').write_text(json.dumps(qa))
            with self.assertRaisesRegex(ValueError,'QA gate invalid'):
                verify(root)


if __name__=='__main__':unittest.main()
