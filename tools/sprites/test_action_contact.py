"""Regression tests for contact-driven WORK/REPAIR effects and safety gate."""
from __future__ import annotations
import math
import unittest
from action_contact import (work_hands, work_contact, work_pulse, work_event_indices, screen_bounds,
                            repair_tip, repair_contact, repair_spark_intensity)


class ContactTests(unittest.TestCase):
    def test_work_hands_remain_inside_one_visible_screen(self):
        for i in range(512):
            t=i/512
            root=(252,270+1.8*math.sin(2*math.pi*t))
            left,right=work_hands(t,root)
            touch=work_contact({'root':root,'handL':left,'handR':right})
            self.assertTrue(touch['handL_on_screen'],(t,touch))
            self.assertTrue(touch['handR_on_screen'],(t,touch))
            self.assertTrue(.30<=work_pulse(t)<=1.0)
        self.assertEqual(work_hands(0,(252,270)),work_hands(1,(252,270)))

    def test_work_events_are_at_visual_peak_after_reindex(self):
        for count in (8, 16, 24, 32):
            origin=round(count*5/24)
            picks=work_event_indices(count,origin)
            self.assertEqual(len(picks),4,(count,picks))
            for frame in picks:
                p=work_pulse(((frame+origin)%count)/count)
                prev=work_pulse(((frame-1+origin)%count)/count)
                nxt=work_pulse(((frame+1+origin)%count)/count)
                self.assertGreaterEqual(p,.90)
                self.assertGreater(p,prev)
                self.assertGreaterEqual(p,nxt)
        self.assertEqual(work_event_indices(24,5),(4,10,16,22))
        with self.assertRaises(ValueError):work_event_indices(7,1)
        with self.assertRaises(ValueError):work_event_indices(24,-1)

    def test_repair_tool_physically_connects_to_wrist(self):
        for i in range(512):
            t=i/512
            phase=2*math.pi*t
            root=(252,270+1.8*math.sin(phase))
            hand=(root[0]+58+12*math.sin(phase),root[1]-54+11*math.cos(phase))
            contact=repair_contact({'root':root,'handR':hand})
            self.assertTrue(contact['torch_reachable'],(t,contact))
            self.assertEqual(repair_tip(root),(root[0]+94,root[1]-72))

    def test_contact_rejects_disconnected_hands(self):
        base={'root':(252,270),'handL':(0,0),'handR':(0,0)}
        self.assertFalse(work_contact(base)['handL_on_screen'])
        self.assertFalse(work_contact(base)['handR_on_screen'])
        self.assertFalse(repair_contact(base)['torch_reachable'])
        self.assertFalse(repair_contact({'root':base['root'],'handR':(252,270)})['torch_reachable'])

    def test_weld_sparks_are_periodic_and_phase_gated(self):
        for i in range(256):
            t=i/256
            self.assertAlmostEqual(repair_spark_intensity(t),
                                   repair_spark_intensity(t+1),places=8)
            self.assertTrue(0<=repair_spark_intensity(t)<=1)
        for x in (.5,.6,.75,.875,.99):
            self.assertEqual(repair_spark_intensity(x),0)
        for bad in (float('nan'),float('inf')):
            with self.assertRaises(ValueError):
                work_hands(bad,(252,270))
            with self.assertRaises(ValueError):
                repair_spark_intensity(bad)


if __name__=='__main__':
    unittest.main()
