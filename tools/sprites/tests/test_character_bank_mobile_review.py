"""Offline visual review generator regressions, no Android/GPU/network needed."""
from __future__ import annotations

import hashlib
import io
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build_character_bank_mobile_review import build


class MobileCandidateReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.original = self.root / "original"
        self.local_cand = self.original / "candidates"
        self.svg_dir = self.original / "src_svg" / "ENG" / "WALK"
        self.local_cand.mkdir(parents=True)
        self.svg_dir.mkdir(parents=True)
        self.bank = self.root / "bank.zip"
        self.html = self.root / "offline-review.html"
        self.name = "zte_chr_eng_walk_final.png"
        self.asset_id = "CHR-ENG-WALK"
        rows = []
        qa = []
        counts = {"IDLE": 6, "WALK": 8, "WORK": 10,
                  "CARRY": 8, "REPAIR": 10, "CELEB": 8}
        for role in ("OP","LOG","ENG"):
            for action,n in counts.items():
                aid = f"CHR-{role}-{action}"
                rows.append({
                    "id": aid, "role": role, "action": action, "frames": n,
                    "file": f"zte_chr_{role.lower()}_{action.lower()}_final.png",
                    "context_only": False, "strict_approved": False,
                })
                qa.append({
                    "id":aid, "frames":n, "technical_geometry_pass":True,
                    "semantic_approved":False, "android_validated":False,
                    "strict_done_added":0,
                })
        (self.original / "creation-manifest.json").write_text(json.dumps({
            "review_only":True, "strict_done_added":0, "assets":rows}))
        (self.original / "candidate-qa.json").write_text(json.dumps({
            "review_only":True, "assets":qa}))
        frame = Image.new("RGBA",(1024,1024),(0,0,0,0))
        painter = ImageDraw.Draw(frame)
        for i in range(8):
            ox,oy=(i%4)*256,(i//4)*256
            painter.rectangle((ox+80,oy+40,ox+185,oy+220),
                              fill=(40,95,116,255))
            (self.svg_dir / f"{i:02d}.svg").write_text('<svg/>')
        output = io.BytesIO()
        frame.save(output,"PNG")
        self.sprite = output.getvalue()
        (self.local_cand / self.name).write_bytes(self.sprite)
        self.record = {
            "id": self.asset_id, "filename":self.name,
            "runtime_target_for_later_approval":
                "app/src/main/res/drawable-nodpi/zte_chr_eng_walk_final.webp",
            "sha256":hashlib.sha256(self.sprite).hexdigest(),
            "bytes":len(self.sprite), "source_type":"repo-local-original",
            "deferred_art_warnings":[],
            "strict_approved":False,"runtime_promoted":False,
        }
        self.save_bank()

    def save_bank(self):
        with zipfile.ZipFile(self.bank,"w") as z:
            z.writestr("candidate-bank-index.json",json.dumps({
                "candidate_count":1,"automatic_semantic_approval":False,
                "automatic_runtime_promotion":False, "target_total":235,
                "strict_done":234,"production_processed":235,
                "candidate_production_complete":True,
                "bank_entries":[self.record],
            }))
            z.writestr("candidates/"+self.name,self.sprite)

    def test_mobile_review_embeds_verified_selected_and_original(self):
        d=build(self.bank,self.original,self.html)
        self.assertEqual(d["assets"],1)
        self.assertTrue(d["review_only"])
        self.assertEqual(d["strict_done_added"],0)
        self.assertTrue(d["candidate_scope_complete"])
        html=self.html.read_text()
        self.assertIn("CHR-ENG-WALK",html)
        self.assertIn("selectedAtlas",html)
        self.assertIn("originalAtlas",html)
        self.assertIn("42 px",html)
        self.assertIn("Exporter mes notes",html)
        self.assertNotIn("__ART_DATA__",html)
        self.assertNotIn("https://",html)
        self.assertNotIn("http://",html)

    def test_mobile_review_includes_verified_motion_flags(self):
        audit = self.root / "motion-audit.json"
        audit.write_text(json.dumps({
            "review_only": True, "automatic_semantic_approval": False,
            "automatic_runtime_promotion": False, "candidate_count": 1,
            "assets": [{
                "id": self.asset_id, "sha256": self.record["sha256"],
                "new_motion_flags": ["LOW_MOBILE_FRAME_CHANGE_REVIEW"],
                "strict_approved": False, "runtime_promoted": False,
            }],
        }))
        build(self.bank, self.original, self.html, audit)
        html = self.html.read_text()
        self.assertIn("LOW_MOBILE_FRAME_CHANGE_REVIEW", html)
        self.assertIn("Animation trop peu visible", html)

    def test_stale_motion_audit_must_not_be_misattached_to_new_png(self):
        audit = self.root / "stale-audit.json"
        audit.write_text(json.dumps({
            "review_only": True, "automatic_semantic_approval": False,
            "automatic_runtime_promotion": False, "candidate_count": 1,
            "assets": [{
                "id": self.asset_id, "sha256": "0" * 64,
                "new_motion_flags": ["LOW_MOBILE_FRAME_CHANGE_REVIEW"],
                "strict_approved": False, "runtime_promoted": False,
            }],
        }))
        with self.assertRaisesRegex(ValueError, "Stale/untrusted motion audit"):
            build(self.bank, self.original, self.html, audit)

    def test_hash_tampering_fails_closed(self):
        self.record["sha256"]="0"*64
        self.save_bank()
        with self.assertRaisesRegex(ValueError,"SHA-256"):
            build(self.bank,self.original,self.html)
        self.assertFalse(self.html.exists())

    def test_invalid_local_frame_geometry_fails_closed(self):
        Image.new("RGBA",(1024,1024),(0,0,0,0)).save(
            self.local_cand/self.name)
        with self.assertRaisesRegex(ValueError,"independent frame/alpha QA"):
            build(self.bank,self.original,self.html)

    def test_script_closing_in_review_flags_is_html_escaped(self):
        self.record["deferred_art_warnings"]=["</script><script>alert(1)</script>"]
        self.save_bank()
        build(self.bank,self.original,self.html)
        html=self.html.read_text()
        self.assertNotIn("</script><script>alert(1)</script>",html)
        self.assertIn("\\u003c/script",html)

    def test_unapproved_bank_is_required(self):
        with zipfile.ZipFile(self.bank,"w") as z:
            z.writestr("candidate-bank-index.json",json.dumps({
                "candidate_count":1, "automatic_semantic_approval":True,
                "automatic_runtime_promotion":False,"bank_entries":[self.record],
            }))
            z.writestr("candidates/"+self.name,self.sprite)
        with self.assertRaisesRegex(ValueError,"Invalid review-only"):
            build(self.bank,self.original,self.html)


if __name__=="__main__":
    unittest.main()
