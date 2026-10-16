"""Regressions for editable first-party sprite effects: no semantic approval."""
import math
import unittest
from pathlib import Path
import xml.etree.ElementTree as ET

from local_character_action_fx import action_fx, ROLE_LIGHT, tool_angle, tool_tip

ROOT=Path(__file__).resolve().parents[2]


class LocalActionFxTests(unittest.TestCase):
    def test_every_role_has_distinct_integrated_action_effects(self):
        for role in ROLE_LIGHT:
            for action in ('WORK','REPAIR','CARRY','CELEB'):
                with self.subTest(role=role,action=action):
                    fx=action_fx(role,action,.9,tool_x=182,tool_y=132,bounce=2)
                    root=ET.fromstring('<svg xmlns="http://www.w3.org/2000/svg">'+fx+'</svg>')
                    namespaces={'svg':'http://www.w3.org/2000/svg'}
                    nodes=root.findall('.//svg:g',namespaces)
                    self.assertEqual(len(nodes),1)
                    self.assertEqual(nodes[0].attrib['data-action-fx'],action)
                    self.assertNotIn('<text',fx)
                    self.assertNotIn('confetti',fx)
                    self.assertTrue(any(word in fx for word in ('circle','path')))

    def test_action_highlights_close_the_loop(self):
        for role in ROLE_LIGHT:
            for action in ('WORK','REPAIR','CARRY','CELEB'):
                with self.subTest(role=role,action=action):
                    a=action_fx(role,action,0,tool_x=180,tool_y=123)
                    b=action_fx(role,action,2*math.pi,tool_x=180,tool_y=123)
                    self.assertEqual(a,b)

    def test_raster_effects_do_not_escape_frame_or_create_fake_labels(self):
        for role in ROLE_LIGHT:
            for action in ('WORK','REPAIR','CARRY','CELEB'):
                markup=action_fx(role,action,1.9,tool_x=191,tool_y=125)
                self.assertNotIn('<text',markup)
                self.assertNotIn('foreignObject',markup)
                ET.fromstring('<svg xmlns="http://www.w3.org/2000/svg">'+markup+'</svg>')
                if action in ('WORK','REPAIR'):
                    # Explicit clamp prevents highlights crossing right side.
                    self.assertNotIn('cx="235.',markup)
                    self.assertNotIn('cx="240.',markup)

    def test_repair_is_a_distinct_compact_hand_tool_cycle(self):
        # WORK and REPAIR used to have identical 15px x 12px hand strokes,
        # which made the two actions indistinguishable at gameplay size.
        source=(ROOT/'tools/sprites/render_chatgpt_originals.py').read_text(encoding='utf8')
        self.assertIn("reach_px=15 if pose=='WORK' else 8",source)
        self.assertIn("pump_px=12 if pose=='WORK' else 7",source)
        wrist="176+(15 if action=='WORK' else 8)*math.sin(phase)"
        vertical="123+(12 if action=='WORK' else 7)*math.cos(phase)+bounce"
        self.assertEqual(source.count(wrist),2)
        self.assertEqual(source.count(vertical),2)
        self.assertIn("handpos=((80+2*reach",source)
        self.assertIn("else (176+reach_px*reach,123+pump_px*pump+bounce)",source)
        self.assertIn("add(action_fx(role,action,phase",source)

    def test_engineer_repair_wrench_rotates_about_fixed_real_socket(self):
        from render_chatgpt_originals import engineer_repair_wrist, ENG_REPAIR_TARGET, svg_frame
        swings = []
        stations = []
        ns = "{http://www.w3.org/2000/svg}"
        for index in range(10):
            phase = 2 * math.pi * index / 10
            wrist = engineer_repair_wrist(phase)
            tip = tool_tip("ENG", "REPAIR", phase,
                           tool_x=wrist[0], tool_y=wrist[1])
            self.assertLess(math.dist(tip, ENG_REPAIR_TARGET), 1e-8)
            angle = tool_angle("REPAIR", phase, role="ENG")
            swings.append(angle)
            svg = ET.fromstring(svg_frame("ENG", "REPAIR", index, 10))
            station = [e for e in svg.iter()
                       if e.get("data-fixed-socket") == "true"]
            wrench = [e for e in svg.iter()
                      if e.get("data-repair-tool") == "ENG"]
            self.assertEqual((len(station), len(wrench)), (1, 1))
            stations.append(ET.tostring(station[0]))
            self.assertIn(f"rotate({angle:.1f})", wrench[0].get("transform"))
            self.assertGreaterEqual(len(list(wrench[0])), 6)
        self.assertEqual(len(set(stations)), 1)
        self.assertGreater(max(swings) - min(swings), 48)
        self.assertLess(max(tool_angle("REPAIR", p) for p in
                            (math.pi/2, 3*math.pi/2)) -
                        min(tool_angle("REPAIR", p) for p in
                            (math.pi/2, 3*math.pi/2)), 40)

    def test_engineer_repair_torso_loads_but_both_feet_stay_planted(self):
        from render_chatgpt_originals import svg_frame
        stations = []
        motions = []
        for index in range(10):
            svg = ET.fromstring(svg_frame("ENG", "REPAIR", index, 10))
            feet = [e for e in svg.iter()
                    if e.get("data-eng-repair-foot") is not None]
            self.assertEqual(
                {e.get("data-eng-repair-foot") for e in feet}, {"L", "R"})
            self.assertTrue(all(float(e.get("data-ankle-y")) == 226.0
                                for e in feet))
            motion = [e for e in svg.iter()
                      if e.get("data-eng-repair-body-bounce") is not None]
            self.assertEqual(len(motion), 1)
            motions.append(float(motion[0].get("data-eng-repair-body-bounce")))
            fixed = [e for e in svg.iter()
                     if e.get("data-fixed-socket") == "true"]
            self.assertEqual(len(fixed), 1)
            stations.append(ET.tostring(fixed[0]))
        self.assertEqual(len(set(stations)), 1)
        self.assertGreater(max(motions) - min(motions), 9.0)
        for role in ("OP", "LOG"):
            svg = svg_frame(role, "REPAIR", 3, 10)
            self.assertNotIn("data-eng-repair-foot", svg)
            self.assertNotIn("data-eng-repair-body-bounce", svg)

    def test_idle_and_walk_have_no_unattached_decorations(self):
        for role in ROLE_LIGHT:
            self.assertEqual(action_fx(role,'IDLE',0),'')
            self.assertEqual(action_fx(role,'WALK',0),'')

    def test_bad_role_action_rejected(self):
        with self.assertRaises(ValueError):
            action_fx('UNKNOWN','WORK',0)
        with self.assertRaises(ValueError):
            action_fx('ENG','DANCE',0)

    def test_renderer_invokes_attached_effects_after_hand(self):
        text=(ROOT/'tools/sprites/render_chatgpt_originals.py').read_text(encoding='utf8')
        self.assertIn('from local_character_action_fx import action_fx',text)
        # The renderer's VFX metadata is versioned independently of its
        # physically attached tool/wrist geometry. Keep metadata validation,
        # without pinning the obsolete v1 implementation label.
        self.assertRegex(text, r"'action_vfx'\s*:\s*'local-[a-z0-9-]+'")
        self.assertLess(text.index("add(joint_arm('R',action))"),
                        text.index('add(action_fx(role,action,phase'))


if __name__=='__main__':
    unittest.main()
