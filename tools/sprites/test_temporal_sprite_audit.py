"""Synthetic regression tests for 96px frame-to-frame TECH audit."""
from __future__ import annotations
import json
import math
import tempfile
import unittest
from pathlib import Path
from PIL import Image, ImageDraw
from temporal_sprite_audit import ACTIONS, audit, inspect_clip


class TemporalAuditTests(unittest.TestCase):
    def setUp(self):
        self.work=tempfile.TemporaryDirectory()
        self.root=Path(self.work.name)/'source'
        self.root.mkdir()
        self.frames=24
        for a in ACTIONS:
            directory=self.root/a
            (directory/'frames').mkdir(parents=True)
            record={'asset_id':'CHR-TECH-'+a,'frames':self.frames,
                    'source_skin_sha256':'test-identical-skin',
                    'strict_status':'NEEDS_REVIEW','human_visual_review_required':True,
                    'qa':{'visual_review_pass':False,'semantic_review_pass':False}}
            (directory/'qa-manifest.json').write_text(json.dumps(record))
            for i in range(self.frames):
                self.save_frame(a,i)
        index={'strict_status':'NEEDS_REVIEW','review_required':True,
               'source_skin_sha256':'test-identical-skin',
               'actions':[{'action':a,'frames':24} for a in ACTIONS]}
        (self.root/'production-index.json').write_text(json.dumps(index))

    def tearDown(self):
        self.work.cleanup()

    def save_frame(self,a,i,blank=False,jump=False):
        image=Image.new('RGBA',(512,512))
        if not blank:
            d=ImageDraw.Draw(image)
            displacement=round(13*math.sin(2*math.pi*i/self.frames))
            if jump:displacement+=120
            x=252+displacement
            d.ellipse((x-37,135,x+36,426),fill=(54,70,94,255))
            d.ellipse((x-18,114,x+19,178),fill=(172,146,131,255))
            d.rectangle((x-29,405,x+34,449),fill=(47,58,70,255))
            # Track deterministic frame identity without changing the binary alpha.
            d.point((x,250),fill=(i*8%256,155,170,255))
        image.save(self.root/a/'frames'/f'CHR-TECH-{a}-{i:02d}.png')

    def test_six_valid_clips_export_review_only_evidence(self):
        report=audit(self.root,Path(self.work.name)/'report')
        self.assertEqual(set(report['actions']),set(ACTIONS))
        self.assertFalse(report['visual_review_pass'])
        self.assertFalse(report['semantic_review_pass'])
        self.assertEqual(report['strict_status'],'NEEDS_REVIEW')
        self.assertTrue((Path(self.work.name)/'report/motion-timeline.png').exists())
        self.assertTrue((Path(self.work.name)/'report/frame-transition-metrics.csv').exists())
        self.assertTrue((Path(self.work.name)/'report/REVIEW_REQUIRED.txt').exists())

    def test_empty_and_clipped_frames_are_rejected(self):
        self.save_frame('WORK',6,blank=True)
        with self.assertRaisesRegex(ValueError,'Empty silhouette'):
            inspect_clip(self.root,'WORK',24)
        self.save_frame('WORK',6)
        image=Image.open(self.root/'WORK/frames/CHR-TECH-WORK-06.png')
        d=ImageDraw.Draw(image)
        d.rectangle((0,0,40,40),fill=(255,255,255,255))
        image.save(self.root/'WORK/frames/CHR-TECH-WORK-06.png')
        with self.assertRaisesRegex(ValueError,'Clipped frame'):
            inspect_clip(self.root,'WORK',24)

    def test_duplicate_content_is_rejected(self):
        original=(self.root/'IDLE/frames/CHR-TECH-IDLE-00.png').read_bytes()
        for i in range(3,24):
            (self.root/'IDLE/frames'/f'CHR-TECH-IDLE-{i:02d}.png').write_bytes(original)
        with self.assertRaisesRegex(ValueError,'Excessive duplicate frames'):
            inspect_clip(self.root,'IDLE',24)

    def test_temporal_spike_and_bad_seam_are_rejected(self):
        self.save_frame('WALK',13,jump=True)
        with self.assertRaisesRegex(ValueError,'Temporal QA failed'):
            inspect_clip(self.root,'WALK',24)

    def test_single_frame_color_flash_is_detected_even_with_same_alpha(self):
        path=self.root/'WORK/frames/CHR-TECH-WORK-09.png'
        with Image.open(path) as image:
            rgba=image.convert('RGBA')
            r,g,b,a=rgba.split()
            # Deliberately invert garment and skin RGB without moving even
            # one silhouette/alpha pixel; geometry-only QA must not pass it.
            corrupted=Image.merge('RGBA',tuple(
                x.point(lambda v:255-v) for x in (r,g,b))+(a,))
            corrupted.save(path)
        with self.assertRaisesRegex(ValueError,'global-rgb-flash-or-texture-drift'):
            inspect_clip(self.root,'WORK',24)

    def test_optional_real_skin_digest_matches_output_provenance(self):
        import hashlib
        source=Path(self.work.name)/'skin.webp'
        source.write_bytes(b'synthetic-source-skin-for-integrity-test')
        digest=hashlib.sha256(source.read_bytes()).hexdigest()
        index_path=self.root/'production-index.json'
        index=json.loads(index_path.read_text())
        index['source_skin_sha256']=digest
        index_path.write_text(json.dumps(index))
        for action in ACTIONS:
            path=self.root/action/'qa-manifest.json'
            data=json.loads(path.read_text())
            data['source_skin_sha256']=digest
            path.write_text(json.dumps(data))
        accepted=audit(self.root,Path(self.work.name)/'good',skin=source)
        self.assertTrue(accepted['technical_pass'])
        source.write_bytes(b'synthetic-tampered-content')
        with self.assertRaisesRegex(ValueError,'Actual skin atlas SHA-256 mismatch'):
            audit(self.root,Path(self.work.name)/'tampered',skin=source)

    def test_review_and_identity_guards_are_enforced(self):
        file=self.root/'REPAIR/qa-manifest.json'
        record=json.loads(file.read_text())
        record['qa']['semantic_review_pass']=True
        file.write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError,'Premature visual'):
            inspect_clip(self.root,'REPAIR',24)
        record['qa']['semantic_review_pass']=False
        record['source_skin_sha256']='different-character'
        file.write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError,'identity source hash mismatch'):
            audit(self.root,Path(self.work.name)/'bad-report')


if __name__=='__main__':unittest.main()
