"""Synthetic regressions for WORK/REPAIR translation-only atlas rejection."""
import tempfile
import unittest
from pathlib import Path
from PIL import Image, ImageDraw

from character_semantic_gate import action_translation_metrics
from verify_character_action_candidates import annotate_report, check_action_atlas


def figure(offset: int = 0, raised_hand: int = 0) -> Image.Image:
    frame = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    d = ImageDraw.Draw(frame)
    dx = offset
    d.ellipse((113+dx, 25, 148+dx, 55), fill=(183, 116, 70, 255))
    d.rectangle((107+dx, 55, 154+dx, 158), fill=(55, 98, 137, 255))
    d.line((121+dx, 158, 112+dx, 215), width=14, fill=(48, 63, 93, 255))
    d.line((142+dx, 158, 153+dx, 215), width=14, fill=(48, 63, 93, 255))
    d.line((109+dx, 76, 80+dx, 150), width=13, fill=(70, 70, 70, 255))
    d.line((154+dx, 76, 175+dx-raised_hand, 150-raised_hand*2),
           width=13, fill=(70, 70, 70, 255))
    return frame


def atlas(frames: list[Image.Image]) -> Image.Image:
    output = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
    for i, frame in enumerate(frames):
        output.alpha_composite(frame, ((i % 4) * 256, (i // 4) * 256))
    return output


class CharacterActionCollectorTests(unittest.TestCase):
    def test_rejects_ten_frames_of_standing_character_sliding_sideways(self):
        offsets = (0, 4, 8, 12, 16, 20, 16, 12, 8, 4)
        frames = [figure(offset) for offset in offsets]
        metrics = action_translation_metrics(frames)
        self.assertTrue(metrics["translation_dominated"], metrics)
        self.assertGreaterEqual(metrics["head_horizontal_excursion_px"], 12)
        self.assertLess(metrics["retained_pose_motion_ratio"], .43)
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "zte_chr_op_work_final.png"
            atlas(frames).save(target)
            qa = {"assets": [{"file": target.name, "pass": True, "issues": []}]}
            result = annotate_report(Path(temp), qa)
            self.assertFalse(result["assets"][0]["pass"])
            self.assertIn("action-visual-risk:ACTION_TRANSLATION_DOMINATES_POSE_RISK",
                          result["assets"][0]["issues"])
            self.assertFalse(
                result["assets"][0]["action_visual_risk"]["image_only_semantic_approval"]
            )
            self.assertEqual(result["automatic_pass"], 0)

    def test_true_arm_pose_variation_is_not_mistaken_for_actor_translation(self):
        frames = [figure(0, raised_hand=i * 4) for i in range(10)]
        metrics = action_translation_metrics(frames)
        self.assertFalse(metrics["translation_dominated"])
        self.assertEqual(metrics["head_horizontal_excursion_px"], 0)

    def test_eight_frames_without_overhead_arms_cannot_pass_celebration(self):
        # Regression for the real collector 38296422676 OP-CELEB: visual
        # variations from torso/helmet redrawing do not equal raised fists.
        frames = [figure() for _ in range(8)]
        with tempfile.TemporaryDirectory() as temp:
            name = "zte_chr_op_celeb_final.png"
            atlas(frames).save(Path(temp) / name)
            qa = {"assets": [{"file": name, "pass": True, "issues": []}]}
            result = annotate_report(Path(temp), qa)
            row = result["assets"][0]
            self.assertFalse(row["pass"])
            self.assertIn("action-visual-risk:CELEBRATION_NO_OVERHEAD_ARM_GESTURE_RISK",
                          row["issues"])
            self.assertEqual(row["action_visual_risk"]["raised_arm_frames"], 0)
            self.assertEqual(result["automatic_pass"], 0)

    def test_several_overhead_arm_frames_do_not_trigger_false_celebration_block(self):
        frames = []
        for index in range(8):
            frame = figure()
            if index in (2,3,4,5):
                ImageDraw.Draw(frame).line((110,75,63,29),
                    fill=(70,70,70,255), width=14)
            frames.append(frame)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "zte_chr_log_celeb_final.png"
            atlas(frames).save(path)
            evidence = check_action_atlas(path, "celeb")
            self.assertGreaterEqual(evidence["raised_arm_frames"], 3)
            self.assertNotIn("CELEBRATION_NO_OVERHEAD_ARM_GESTURE_RISK",
                             evidence["flags"])

    def test_bad_work_atlas_is_rejected_without_aborting_sibling_candidates(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "zte_chr_eng_repair_final.png"
            Image.new("RGBA", (256, 256)).save(target)
            qa = {"assets": [
                {"file": target.name, "pass": True, "issues": []},
                {"file": "zte_chr_eng_idle_final.png", "pass": True, "issues": []},
            ]}
            result = annotate_report(Path(temp), qa)
            self.assertFalse(result["assets"][0]["pass"])
            self.assertTrue(result["assets"][1]["pass"])
            self.assertIn("ACTION_VISUAL_QA_ERROR",
                          result["assets"][0]["action_visual_risk"]["flags"])


if __name__ == "__main__":
    unittest.main()
