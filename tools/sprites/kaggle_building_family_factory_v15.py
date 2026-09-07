#!/usr/bin/env python3
"""Building factory v15: multi-anchor branch search over v14 primitives."""
from __future__ import annotations
import argparse,gc,importlib.util,json
from pathlib import Path
import torch

HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('v14',HERE/'kaggle_building_family_factory_v14.py')
v14=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(v14)
print('KAGGLE_STARTUP=building-family-flux-v15-multibranch-semantic-safe',flush=True)

ANCHORS=4
BRANCHES=2

def prompts(i):
    dna=v14.DNA[i['family']]
    tier=v14.TIER[i['tier']]
    short=(f"AAA mobile isometric INDUSTRIAL FACTORY. {dna}. {tier}. One connected production building only. "
           "Flat gray studio background.")
    detail=(f"Same industrial factory upgraded in place. {dna}. {tier}. 34-degree orthographic view. "
            "Preserve facade, production core and roof direction; all additions attached. "
            "NO people, workers, flags, cranes, hoists, vehicles, roads, pavement, floor platform, site card, signs or text. "
            "NO church, temple, palace, civic tower, monument, castle, campus or decorative landmark. "
            "Factory machinery and industrial architecture only; gray background reaches every edge.")
    return short,detail

# Replace v14 prompt source while retaining its tested rendering / alpha / QA machinery.
v14.prompts=prompts

def anchor_score(final,cov):
    slab=v14.slab_score(final.getchannel('A'))
    # Prefer compact early-game anchors around 8-13% coverage and virtually no broad base.
    target_penalty=abs(cov-.105)
    return 1.0 - slab*2.5 - target_penalty*3.0

def branch_score(recs):
    ok,why=v14.family_qa(recs)
    if not ok:return -999.0,why
    cov=[r[2] for r in recs]
    adj=[v14.iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
    boxes=[v14.bbox(r[1]) for r in recs];cx=boxes[0][2]
    drift=max(abs(b[2]-cx) for b in boxes)
    slabs=max(v14.slab_score(r[1].getchannel('A')) for r in recs)
    growth=cov[-1]/max(cov[0],1e-6)
    score=min(adj)*2.0 + min(growth,3.0) - drift*.05 - slabs*2.5
    return score,why

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=56);ap.add_argument('--seed',type=int,default=73117);args=ap.parse_args()
    items=v14.select(list(v14.rows()),max(1,args.count));print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
    if not items:return
    v14.INCOMING.mkdir(parents=True,exist_ok=True)
    emb={};t,enc=v14.load_encode()
    for i in items:
        s,d=prompts(i)
        with torch.no_grad():pe,ppe,_=enc.encode_prompt(prompt=s,prompt_2=d,max_sequence_length=192)
        emb[i['id']]=(pe.cpu(),ppe.cpu())
    del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=v14.load_render()
    by={}
    for i in items:by.setdefault(i['family'],[]).append(i)
    report={'engine':'v15-multibranch-semantic-safe','anchor_attempts':0,'branch_attempts':0,'families':[]}
    accepted=[];rejected=0
    for fam,group in sorted(by.items()):
        group.sort(key=lambda x:x['tier']);t0=group[0];pe0,ppe0=emb[t0['id']];anchors=[]
        for a in range(ANCHORS):
            report['anchor_attempts']+=1
            try:
                raw,final,cov=v14.render(t0,None,pe0,ppe0,base,img,args.seed+fam*10000+a*15401)
                sc=anchor_score(final,cov);anchors.append((sc,a,raw,final,cov))
                print(f'KAGGLE_ANCHOR={t0["id"]} variant={a+1} score={sc:.3f} coverage={cov:.1%}',flush=True)
            except Exception as e:print(f'KAGGLE_ANCHOR_REJECTED={t0["id"]} variant={a+1} reason={e}',flush=True)
            finally:gc.collect();torch.cuda.empty_cache()
        anchors.sort(key=lambda x:x[0],reverse=True)
        branches=[]
        for sc,a,raw0,final0,cov0 in anchors[:BRANCHES]:
            report['branch_attempts']+=1;recs=[(t0,final0,cov0)];prev=raw0;failed=False
            for i in group[1:]:
                pe,ppe=emb[i['id']]
                try:
                    prev,final,cov=v14.render(i,prev,pe,ppe,base,img,args.seed+fam*10000+a*15401+i['tier']*977)
                    recs.append((i,final,cov))
                except Exception as e:
                    print(f'KAGGLE_BRANCH_REJECTED=BLD-{fam:02d} branch={a+1} tier={i["tier"]} reason={e}',flush=True);failed=True;break
                finally:gc.collect();torch.cuda.empty_cache()
            if failed or len(recs)!=len(group):continue
            bscore,why=branch_score(recs);branches.append((bscore,a,recs,why));print(f'KAGGLE_BRANCH_SCORE=BLD-{fam:02d} branch={a+1} score={bscore:.3f} {why}',flush=True)
        branches.sort(key=lambda x:x[0],reverse=True)
        famrec={'family':fam,'anchors_generated':len(anchors),'branches_completed':len(branches)}
        if not branches or branches[0][0] < -100:
            rejected+=len(group);famrec['accepted']=False;report['families'].append(famrec);continue
        bscore,a,recs,why=branches[0]
        famrec.update({'accepted':True,'selected_branch':a+1,'score':bscore,'qa':why});report['families'].append(famrec)
        for i,final,cov in recs:
            p=v14.INCOMING/f"{i['stem']}.png";final.save(p,'PNG',optimize=True);accepted.append(i['id'])
            print(f'KAGGLE_VALIDATED={p.relative_to(v14.ROOT)} coverage={cov:.1%} selected_branch={a+1} score={bscore:.3f}',flush=True)
    (v14.INCOMING/'branch-search-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(f'KAGGLE_BRANCH_SEARCH anchors={report["anchor_attempts"]} branches={report["branch_attempts"]}',flush=True)
    print(f'KAGGLE_BUILDING_SUCCESS={len(accepted)} KAGGLE_BUILDING_REJECTED={rejected} KAGGLE_BUILDING_ATTEMPTED={len(items)}',flush=True)

if __name__=='__main__':main()
