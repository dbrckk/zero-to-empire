"""Regression tests for six TECH runtime review atlases.

Run AFTER the six-clip generator in CI. Never silently skip missing input.
"""
from __future__ import annotations
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image
from package_tech_actions_runtime import ACTIONS, package, verify, game_scale_metrics

FIXTURE=Path('build/tech-actions-v3').resolve()


class RuntimePackTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(FIXTURE.is_dir(),f'Six-action build missing: {FIXTURE}')

    def test_six_atlases_keep_the_review_gate(self):
        with tempfile.TemporaryDirectory() as temp:
            out=Path(temp)/'runtime'
            manifest=package(FIXTURE,out)
            self.assertEqual(tuple(manifest['animations']),ACTIONS)
            self.assertEqual(sum(v['frames'] for v in manifest['animations'].values()),144)
            self.assertFalse(manifest['visual_review_pass'])
            self.assertFalse(manifest['semantic_review_pass'])
            self.assertFalse(manifest['integrated_into_game'])
            self.assertFalse(manifest['approved_for_release'])
            self.assertEqual(manifest['strict_status'],'NEEDS_REVIEW')
            self.assertTrue((out/'REVIEW_REQUIRED.txt').exists())
            self.assertEqual(len(list((out/'atlases').glob('*.png'))),24)
            for action,item in manifest['animations'].items():
                self.assertEqual(item['strict_status'],'NEEDS_REVIEW')
                self.assertEqual(item['reference_pivot_px'],[252,449])
                self.assertFalse(item['optional_shadow_layer']['default_enabled'])
                self.assertEqual(item['collision_boxes_status'],
                                 'NOT_DEFINED_REQUIRES_GAMEPLAY_REVIEW')
                self.assertEqual(len(item['per_frame_visual_bounds_px']),24)
                self.assertTrue(item['game_scale_96px_technical_pass'])
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
            self.assertIn('requestAnimationFrame',(out/'review-player.html').read_text())

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
