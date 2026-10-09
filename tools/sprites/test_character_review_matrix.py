import unittest
from character_review_matrix import build,markdown


def fake_queue():
    actions=['WALK','WORK','CARRY','REPAIR','CELEB']
    ids=['CHR-OP-'+a for a in actions]
    ids+=['CHR-TECH-'+a for a in ('WALK','WORK','CARRY')]
    ids+=['CHR-LOG-'+a for a in actions]
    ids+=['CHR-ENG-'+a for a in ('IDLE','WALK','WORK','CARRY','REPAIR','CELEB')]
    assets=[{'id':'DONE-'+str(i),'strict_status':'DONE'} for i in range(216)]
    assets += [{'id':a,'strict_status':'NEEDS_REVIEW',
                'pipeline_status':'REJECTED_SEMANTIC' if a=='CHR-TECH-WALK' else 'AWAITING_REVIEW',
                'review_reason':'walk-orientation/silhouette-jump=0.30' if a=='CHR-TECH-WALK' else 'Needs review',
                'last_generator':'kaggle-character-sheet','last_run_id':1234}
               for a in ids]
    return {'target_total':235,'assets':assets}


class MatrixTests(unittest.TestCase):
    def test_exact_pending_roles_and_no_auto_promotion(self):
        report=build(fake_queue())
        self.assertEqual(report['strict_done'],216)
        self.assertEqual(report['pending_count'],19)
        self.assertEqual(report['by_role'],{'OP':5,'TECH':3,'LOG':5,'ENG':6})
        self.assertFalse(report['auto_promotion_permitted'])
        self.assertTrue(report['human_approval_required'])
        self.assertTrue(all(not x['semantic_review_pass'] for x in report['items']))

    def test_semantic_rejection_before_technical_success(self):
        report=build(fake_queue())
        self.assertEqual(report['items'][0]['asset_id'],'CHR-TECH-WALK')
        self.assertEqual(report['items'][0]['canonical_pipeline_status'],'REJECTED_SEMANTIC')
        self.assertTrue(report['items'][0]['alternate_tech_renderer_available'])
        self.assertTrue(report['items'][0]['alternate_is_not_canonical_approval'])
        self.assertIn('semantic rejection',markdown(report))

    def test_cannot_inflate_canonical_queue(self):
        q=fake_queue()
        q['assets'].append(q['assets'][-1])
        with self.assertRaises(ValueError):build(q)
        q=fake_queue()
        q['assets'][-1]['id']='CHR-ALIEN-WALK'
        with self.assertRaises(ValueError):build(q)
        q=fake_queue()
        q['assets'][-1]['id']='TER-OTHER'
        with self.assertRaises(ValueError):build(q)

    def test_deterministic_order_and_source_immutability(self):
        q=fake_queue()
        first=build(q)
        second=build(q)
        self.assertEqual(first,second)
        self.assertEqual(q['assets'][-1]['strict_status'],'NEEDS_REVIEW')
        self.assertEqual(len(set(x['asset_id'] for x in first['items'])),19)
        self.assertIn('CHR-ENG-IDLE',markdown(first))


if __name__=='__main__':unittest.main()
