"""Synthetic visual failure tests, no external models and no automatic approval."""
import unittest
from PIL import Image,ImageDraw
from character_semantic_gate import clip_risk,frame_geometry,palette_distance,color_signature,idle_visual_activity,lower_ground_band_ratio,celebration_arm_reach_counts,head_structure_drift


def person(i=0,color=(80,144,187,255)):
    frame=Image.new('RGBA',(256,256))
    d=ImageDraw.Draw(frame)
    d.ellipse((113+i,20,144+i,52),fill=color)
    d.polygon([(108+i,57),(148+i,57),(155+i,140),(99+i,140)],fill=color)
    d.line((101+i,74,80+i,131),fill=color,width=10)
    d.line((145+i,74,174+i,131),fill=color,width=10)
    d.line((114+i,135,104+i,221),fill=color,width=15)
    d.line((138+i,135,150+i,221),fill=color,width=15)
    d.line((99+i,222,111+i,222),fill=color,width=11)
    d.line((142+i,222,157+i,222),fill=color,width=11)
    return frame


def portrait(i=0):
    frame=Image.new('RGBA',(256,256))
    d=ImageDraw.Draw(frame)
    d.ellipse((33+i,10,224+i,198),fill=(85,151,189,255))
    d.polygon([(70+i,173),(175+i,173),(205+i,239),(47+i,239)],
              fill=(85,151,189,255))
    return frame


class SemanticGateTests(unittest.TestCase):
    def test_consistent_full_body_is_not_blocked(self):
        result=clip_risk([person(i%3) for i in range(8)])
        self.assertNotEqual(result['risk_level'],'BLOCKING')
        self.assertFalse(result['image_only_semantic_approval'])

    def test_portraits_and_fragments_block(self):
        result=clip_risk([portrait(i%2) for i in range(8)])
        self.assertEqual(result['risk_level'],'BLOCKING')
        self.assertIn('MULTIPLE_NON_FULL_BODY_FRAMES',result['flags'])

    def test_unrelated_costume_palettes_are_detected(self):
        frames=[person(0,(210,30,45,255)) if i%2 else
                person(0,(12,185,210,255)) for i in range(8)]
        result=clip_risk(frames)
        self.assertIn('PALETTE_IDENTITY_DISCONTINUITY_RISK',result['flags'])

    def test_two_people_in_one_cell_cause_visible_mass_jump(self):
        pair=Image.new('RGBA',(256,256))
        pair.alpha_composite(person(-60))
        pair.alpha_composite(person(60))
        frames=[person() for _ in range(7)]+[pair]
        result=clip_risk(frames)
        self.assertEqual(result['risk_level'],'BLOCKING')
        self.assertIn('SILHOUETTE_MASS_DISCONTINUITY_RISK',result['flags'])
        self.assertGreater(result['max_silhouette_mass_ratio'],1.80)

    def test_empty_frame_fails_hard(self):
        self.assertFalse(frame_geometry(Image.new('RGBA',(256,256)))['valid'])
        frames=[person() for _ in range(7)]+[Image.new('RGBA',(256,256))]
        self.assertEqual(clip_risk(frames)['risk_level'],'BLOCKING')

    def test_persistent_flat_floor_shadow_blocks_candidate(self):
        clean=[person(i%2) for i in range(8)]
        self.assertTrue(all(lower_ground_band_ratio(frame)<1.27 for frame in clean))
        self.assertNotIn('BAKED_GROUND_SHADOW_RISK',clip_risk(clean,'IDLE')['flags'])
        shadowed=[]
        for frame in clean:
            with_shadow=frame.copy()
            ImageDraw.Draw(with_shadow).ellipse((70,221,187,239),
                                               fill=(80,83,87,230))
            shadowed.append(with_shadow)
        report=clip_risk(shadowed,'IDLE')
        self.assertEqual(report['risk_level'],'BLOCKING')
        self.assertIn('BAKED_GROUND_SHADOW_RISK',report['flags'])
        self.assertGreaterEqual(report['baked_ground_band_suspected_frames'],4)

    def test_one_long_ground_contact_is_not_a_persistent_shadow(self):
        frames=[person(i%2) for i in range(8)]
        ImageDraw.Draw(frames[3]).ellipse((70,221,187,239),
                                         fill=(80,83,87,230))
        report=clip_risk(frames,'WORK')
        self.assertNotIn('BAKED_GROUND_SHADOW_RISK',report['flags'])

    def test_one_collapsed_work_frame_blocks_even_if_nine_others_are_full_body(self):
        normal=person()
        tiny=normal.crop((0,16,256,229)).resize((256,164))
        short=Image.new('RGBA',(256,256))
        short.alpha_composite(tiny,(0,65))
        frames=[normal.copy() for _ in range(10)]
        frames[4]=short
        result=clip_risk(frames,'WORK')
        self.assertEqual(result['risk_level'],'BLOCKING')
        self.assertIn('FRAME_SCALE_COLLAPSE_RISK',result['flags'])
        self.assertLess(result['min_relative_frame_height'],.82)

    def test_alternating_helmet_or_face_color_blocks_identity(self):
        frames=[]
        for index in range(8):
            frame=person()
            color=(245,65,35,255) if index%2 else (30,235,224,255)
            ImageDraw.Draw(frame).ellipse((102,10,155,70),fill=color)
            frames.append(frame)
        result=clip_risk(frames,'IDLE')
        self.assertEqual(result['risk_level'],'BLOCKING')
        self.assertIn('HEAD_FACE_HEADGEAR_COLOR_DISCONTINUITY_RISK',result['flags'])
        self.assertGreater(result['max_headgear_adjacent_color_distance'],.24)

    def test_morphing_crate_palette_blocks_carrying(self):
        frames=[]
        for index in range(8):
            frame=person()
            color=(230,50,32,255) if index%2 else (15,225,226,255)
            ImageDraw.Draw(frame).rectangle((78,106,175,169),fill=color)
            frames.append(frame)
        result=clip_risk(frames,'CARRY')
        self.assertEqual(result['risk_level'],'BLOCKING')
        self.assertIn('TOOL_CRATE_TORSO_COLOR_DISCONTINUITY_RISK',result['flags'])
        self.assertGreater(result['max_mid_body_prop_adjacent_color_distance'],.30)
        # The same synthetic color change is not proof that a different
        # non-prop action should be blocked on mid-body content alone.
        self.assertNotIn('TOOL_CRATE_TORSO_COLOR_DISCONTINUITY_RISK',
                         clip_risk(frames,'IDLE')['flags'])

    def test_face_helmet_morph_blocks_work_even_when_color_palette_matches(self):
        reference=person()
        altered=person()
        draw=ImageDraw.Draw(altered)
        draw.rectangle((100,8,164,70),fill=(0,0,0,0))
        draw.ellipse((92,18,165,68),fill=(80,144,187,255))
        frames=[reference.copy() for _ in range(10)]
        frames[4]=altered
        result=clip_risk(frames,'WORK')
        self.assertEqual(result['risk_level'],'BLOCKING')
        self.assertIn('FACE_HEADGEAR_STRUCTURE_DRIFT_RISK',result['flags'])
        self.assertGreater(result['max_face_headgear_structural_drift'],.19)
        self.assertGreater(head_structure_drift(frames),.19)

    def test_celebration_counts_actual_raised_arm_frames_not_final_sparkle(self):
        def simple(raised=False):
            frame=Image.new('RGBA',(256,256))
            d=ImageDraw.Draw(frame)
            d.ellipse((113,20,144,52),fill=(160,120,120,255))
            d.rounded_rectangle((104,58,150,157),radius=14,fill=(60,80,100,255))
            d.line((110,80,91,150),fill=(60,80,100,255),width=11)
            d.line((147,80,165,150),fill=(60,80,100,255),width=11)
            d.line((116,150,110,230),fill=(60,80,100,255),width=14)
            d.line((138,150,150,230),fill=(60,80,100,255),width=14)
            if raised:
                d.line((110,75,78,48),fill=(60,80,100,255),width=14)
            return frame
        neutral=simple()
        cheering=simple(True)
        # The historical LOG-CELEB produced mostly neutral poses, then a
        # final-frame effect. It must not pass as progressive arm animation.
        false_loop=[neutral.copy() for _ in range(7)]+[cheering]
        counts=celebration_arm_reach_counts(false_loop)
        self.assertLess(sum(n>=28 for n in counts),3)
        progressive=[neutral.copy() for _ in range(3)]+[cheering.copy() for _ in range(5)]
        scores=celebration_arm_reach_counts(progressive)
        self.assertGreaterEqual(sum(n>=28 for n in scores),3)

    def test_idles_with_subtle_eye_blinks_have_visible_activity(self):
        base=person()
        frames=[]
        for index in range(6):
            frame=base.copy()
            if index%2:
                ImageDraw.Draw(frame).rectangle((118,34,140,39),
                                                fill=(12,18,24,255))
            frames.append(frame)
        self.assertEqual(idle_visual_activity([base]*6),0)
        self.assertGreater(idle_visual_activity(frames),.00035)
        self.assertLess(idle_visual_activity(frames),.03)

    def test_idle_visual_activity_requires_multiple_nonempty_frames(self):
        self.assertEqual(idle_visual_activity([person()]),0.0)
        self.assertEqual(idle_visual_activity([]),0.0)

    def test_same_palette_is_identical(self):
        signature=color_signature(person())
        self.assertAlmostEqual(palette_distance(signature,signature),0)
        with self.assertRaises(ValueError):
            clip_risk([person()])


if __name__=='__main__':
    unittest.main()
