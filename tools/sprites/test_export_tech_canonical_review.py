"""Offline tests for canonical TECH candidate staging: no network/auto-promotion."""
from __future__ import annotations
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image, ImageDraw

from export_tech_canonical_review import (
    ACTIONS, digest, selected_indices, stage_action, validate_index,
)


class TechCanonicalReviewTests(unittest.TestCase):
    def test_phase_indices_are_stable_distinct_and_bounded(self):
        self.assertEqual(selected_indices(8), [0, 3, 6, 9, 12, 15, 18, 21])
        self.assertEqual(selected_indices(10), [0, 2, 4, 7, 9, 12, 14, 16, 19, 21])
        for count in ACTIONS.values():
            self.assertEqual(len(set(selected_indices(count))), count)
        for count in (0, 3, 17, 25):
            with self.assertRaises(ValueError):
                selected_indices(count)

    def fixture(self, root: Path, action: str = "CARRY") -> tuple[Path, Path]:
        source = root / "source"
        skin = root / "skin.webp"
        skin.write_bytes(b"stable single identity texture")
        skin_hash = hashlib.sha256(skin.read_bytes()).hexdigest()
        actions = ("WALK", "CARRY", "IDLE", "WORK", "REPAIR", "CELEB")
        index = {
            "format": "zte-modular-actions-v3",
            "review_required": True,
            "strict_status": "NEEDS_REVIEW",
            "source_skin_sha256": skin_hash,
            "actions": [
                {"action": a, "asset_id": "CHR-TECH-" + a,
                 "strict_status": "NEEDS_REVIEW", "technical_pass": True,
                 "source_skin_sha256": skin_hash}
                for a in actions
            ],
        }
        source.mkdir()
        (source / "production-index.json").write_text(json.dumps(index))
        folder = source / action
        (folder / "frames").mkdir(parents=True)
        manifest = {
            "asset_id": "CHR-TECH-" + action,
            "strict_status": "NEEDS_REVIEW",
            "human_visual_review_required": True,
            "source_skin_sha256": skin_hash,
            "frames": 24, "fps": 12,
            "qa": {"technical_pass": True, "visual_review_pass": False,
                   "semantic_review_pass": False},
        }
        (folder / "qa-manifest.json").write_text(json.dumps(manifest))
        (folder / "REVIEW_REQUIRED.txt").write_text("Must visually approve")
        # 24 actual full-body 512px RGBA frames. The silhouette is game-size legible.
        for i in selected_indices(ACTIONS[action]):
            im = Image.new("RGBA", (512, 512))
            d = ImageDraw.Draw(im)
            d.ellipse((211, 63, 300, 155), fill=(75, 135, 150, 255))
            d.rectangle((188, 152, 320, 327), fill=(32, 101, 139, 255))
            d.rectangle((193, 327, 234, 466), fill=(40, 95, 130, 255))
            d.rectangle((268, 327, 309, 468), fill=(40, 95, 130, 255))
            d.rectangle((178 + i % 7, 180, 207 + i % 7, 316),
                        fill=(41, 130, 168, 255))
            d.rectangle((310 - i % 7, 177, 337 - i % 7, 310),
                        fill=(41, 130, 168, 255))
            im.save(folder / "frames" / f"CHR-TECH-{action}-{i:02d}.png")
        return source, skin

    def test_real_staged_pixels_preserve_review_and_padding(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, skin = self.fixture(root)
            output = root / "review"
            result = stage_action(source, output, "CARRY", digest(skin))
            self.assertEqual(result["strict_status"], "NEEDS_REVIEW")
            self.assertFalse(result["semantic_approved"])
            self.assertFalse(result["runtime_integrated"])
            self.assertFalse(result["release_eligible"])
            self.assertTrue(result["canonical_geometry_pass"])
            self.assertTrue((output / "zte_chr_tech_carry_final-preview.gif").is_file())
            with Image.open(output / result["staged_png"]) as image:
                self.assertEqual(image.size, (1024, 1024))
                self.assertEqual(image.mode, "RGBA")
                self.assertIsNone(image.crop((0, 512, 1024, 1024))
                                  .getchannel("A").getbbox())

    def test_refuse_unreviewable_metadata_and_missing_pixels(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, skin = self.fixture(root)
            validate_index(source, skin)
            bad = root / "bad-skin"
            bad.write_bytes(b"another texture")
            with self.assertRaisesRegex(ValueError, "provenance"):
                validate_index(source, bad)
            qa = source / "CARRY" / "qa-manifest.json"
            data = json.loads(qa.read_text())
            data["strict_status"] = "DONE"
            qa.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, "reviewable"):
                stage_action(source, root / "out", "CARRY", digest(skin))
            data["strict_status"] = "NEEDS_REVIEW"
            qa.write_text(json.dumps(data))
            (source / "CARRY" / "frames" / "CHR-TECH-CARRY-03.png").unlink()
            with self.assertRaisesRegex(ValueError, "Missing source frame"):
                stage_action(source, root / "out", "CARRY", digest(skin))

    def test_unsupported_action_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "Unknown action"):
                stage_action(Path(tmp), Path(tmp) / "out", "FLY", "x")


if __name__ == "__main__":
    unittest.main()
