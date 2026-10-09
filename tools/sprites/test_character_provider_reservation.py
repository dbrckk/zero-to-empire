"""Prevent Kaggle/Autofactory from stealing a live provider-specific repair."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from datetime import datetime,timezone,timedelta
import asset_wave_orchestrator as worker


class ReservationTests(unittest.TestCase):
    def test_external_repair_excludes_concurrent_kaggle_character_dispatch(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'queue.json'
            p.write_text(json.dumps({
                'mode':'pollinations-controlled-repair',
                'reservation_expires_utc':(datetime.now(timezone.utc)+timedelta(hours=18)).isoformat(),
                'targets':[{'id':'CHR-LOG-CARRY','status':'PENDING_POLLINATIONS'}]
            }))
            with patch.object(worker,'CHARACTER_QUEUE',p):
                self.assertEqual(worker.active_pollinations_repair(),['CHR-LOG-CARRY'])
                with patch.object(worker,'stats',return_value={'strict_done':216}), \
                     patch.object(worker,'pending_ids_from_controlled',return_value=[]), \
                     patch.object(worker,'next_group',return_value=None):
                    answer=worker.make_decision({
                        'stop_when_strict_done':235,'assets':[]})
                    self.assertEqual(answer['action'],'WAIT_EXTERNAL_CHARACTER_REPAIR')
                    self.assertEqual(answer['ids'],['CHR-LOG-CARRY'])

    def test_expired_or_other_provider_has_no_lock(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'queue.json'
            for mode,expiry,expected in [
                ('pollinations-controlled-repair','2000-01-01T00:00:00Z',[]),
                ('kaggle-character-burst-v1.12','2099-01-01T00:00:00Z',[]),
                ('pollinations-controlled-repair','2099-01-01T00:00:00Z',['CHR-OP-WORK'])]:
                p.write_text(json.dumps({'mode':mode,
                    'reservation_expires_utc':expiry,
                    'targets':[{'id':'CHR-OP-WORK','status':'BLOCKED'}]}))
                with patch.object(worker,'CHARACTER_QUEUE',p):
                    self.assertEqual(worker.active_pollinations_repair(),expected)

    def test_injected_invalid_or_missing_reservation_does_not_block(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'queue.json'
            for expiry in (None,'invalid','2099-01-01T00:00:00'):
                p.write_text(json.dumps({'mode':'pollinations-controlled-repair',
                    'reservation_expires_utc':expiry,
                    'targets':[{'id':'CHR-LOG-CARRY','status':'PENDING_POLLINATIONS'}]}))
                with patch.object(worker,'CHARACTER_QUEUE',p):
                    self.assertEqual(worker.active_pollinations_repair(),[])


if __name__=='__main__':
    unittest.main()
