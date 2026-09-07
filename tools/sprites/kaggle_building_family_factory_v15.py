#!/usr/bin/env python3
"""Building factory v15.2: multi-anchor search with live semantic/technical QA."""
from __future__ import annotations
import argparse,gc,importlib.util,json
from pathlib import Path
import numpy as np
import torch

HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('v14',HERE/'kaggle_building_family_factory_v14.py')
v14=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(v14)
print('KAGGLE_STARTUP=building-family-flux-v15.2-live-semantic-validation',flush=True)

ANCHORS=4
BRANCHES=2
CONTEXT_RETRIES=3

def prompts(i):
    dna=v14.DNA[i['family']]; tier=v14.TIER[i['tier']]
    short=(f"AAA mobile isometric FINISHED INDUSTRIAL FACTORY. {dna}. {tier}. One connected completed production building only. Flat gray studio background.")
    detail=(f"Finished operating factory upgraded in place. {dna}. {tier}. 34-degree orthographic view. Preserve facade, production core and roof direction; all additions attached. "
            "NO construction site, crane, tower crane, jib, boom arm, hoist, gantry crane, scaffolding, temporary frame, flag, worker, person, vehicle, road, pavement, floor slab, platform, site card, loose prop, sign or text. "
            "NO church, temple, palace, civic tower, monument, castle or campus. Compact finished industrial machinery integrated into the building; gray background reaches every edge.")
    return short,detail
v14.prompts=prompts

def boom_score(final):
    """Detect crane-like thin long horizontal structures high above the main mass."""
    a=np.array(final.getchannel('A'))>24
    ys,xs=np.where(a)
    if len(xs)<20:return 0.0
    x0,x1=xs.min(),xs.max(); y0,y1=ys.min(),ys.max(); w=max(1,x1-x0+1); h=max(1,y1-y0+1)
    top_end=y0+max(1,int(h*.42)); rows=[]
    for y in range(y0,top_end+1):
        xx=np.where(a[y,x0:x1+1])[0]
        if len(xx)<3: rows.append(False); continue
        span=xx[-1]-xx[0]+1
        rows.append(span>=w*.55)
    best=cur=0
    for hit in rows:
        cur=cur+1 if hit else 0; best=max(best,cur)
    # A crane boom tends to be long but only a few pixels thick; substantial roof masses are thicker.
    thin_limit=max(4,int(h*.065))
    if 1<=best<=thin_limit:return min(1.0,(best/thin_limit)+.35)
    return 0.0

def anchor_score(final,cov):
    slab=v14.slab_score(final.getchannel('A')); boom=boom_score(final); target_penalty=abs(cov-.105)
    return 1.0 - slab*3.2 - boom*1.8 - target_penalty*3.0

def live_gate(recs,new_final,new_cov,tier):
    reasons=[]
    slab=v14.slab_score(new_final.getchannel('A'))
    boom=boom_score(new_final)
    if slab>.16: reasons.append(f'slab={slab:.2f}')
    if boom>.45: reasons.append(f'crane-boom={boom:.2f}')
    box=v14.bbox(new_final)
    if recs:
        prev=recs[-1][1]; prev_cov=recs[-1][2]
        ident=v14.iou(prev,new_final)
        if ident<.25: reasons.append(f'adj-iou={ident:.2f}')
        if new_cov < prev_cov*.78: reasons.append(f'coverage-collapse={prev_cov:.3f}->{new_cov:.3f}')
        start_cx=v14.bbox(recs[0][1])[2]
        if abs(box[2]-start_cx)>6.0: reasons.append(f'center-drift={abs(box[2]-start_cx):.1f}')
        if tier>=2 and new_cov < recs[0][2]*1.03: reasons.append(f'no-growth-from-anchor={recs[0][2]:.3f}->{new_cov:.3f}')
    if recs and tier>=4:
        start=recs[0][2]; minimum={4:1.28,5:1.45,6:1.70}[tier]
        if new_cov < start*minimum: reasons.append(f'growth-track={new_cov/max(start,1e-6):.2f}x<{minimum:.2f}x')
    return (not reasons),reasons

def branch_score(recs):
    ok,why=v14.family_qa(recs)
    if not ok:return -999.0,why
    cov=[r[2] for r in recs]; adj=[v14.iou(recs[n-1][1],recs[n][1]) for n in range(1,len(recs))]
    boxes=[v14.bbox(r[1]) for r in recs]; cx=boxes[0][2]; drift=max(abs(b[2]-cx) for b in boxes)
    slabs=max(v14.slab_score(r[1].getchannel('A')) for r in recs)
    booms=max(boom_score(r[1]) for r in recs)
    growth=cov[-1]/max(cov[0],1e-6)
    score=min(adj)*2.0 + min(growth,3.0) - drift*.05 - slabs*3.2 - booms*1.8
    return score,why+f' max-boom={booms:.2f}'

def render_contextual(i,prev,recs,pe,ppe,base,img,seed,report):
    last=[]
    for attempt in range(CONTEXT_RETRIES):
        report['context_attempts']+=1
        try:
            raw,final,cov=v14.render(i,prev,pe,ppe,base,img,seed+attempt*23003)
            ok,reasons=live_gate(recs,final,cov,i['tier'])
            if ok:
                print(f'KAGGLE_LIVE_PASS={i["id"]} context_attempt={attempt+1} coverage={cov:.1%} boom={boom_score(final):.2f}',flush=True)
                return raw,final,cov
            msg=','.join(reasons);last.append(msg);report['live_rejections']+=1
            print(f'KAGGLE_LIVE_REJECT={i["id"]} context_attempt={attempt+1} reason={msg}',flush=True)
        except Exception as e:
            last.append(str(e));print(f'KAGGLE_LIVE_RENDER_REJECT={i["id"]} context_attempt={attempt+1} reason={e}',flush=True)
        finally:gc.collect();torch.cuda.empty_cache()
    raise RuntimeError('context QA exhausted: '+'; '.join(last[-3:]))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=56);ap.add_argument('--seed',type=int,default=73117);args=ap.parse_args()
    items=v14.select(list(v14.rows()),max(1,args.count));print('KAGGLE_BUILDING_PLAN='+','.join(i['id'] for i in items),flush=True)
    if not items:return
    v14.INCOMING.mkdir(parents=True,exist_ok=True);emb={};t,enc=v14.load_encode()
    for i in items:
        s,d=prompts(i)
        with torch.no_grad():pe,ppe,_=enc.encode_prompt(prompt=s,prompt_2=d,max_sequence_length=192)
        emb[i['id']]=(pe.cpu(),ppe.cpu())
    del t,enc;gc.collect();torch.cuda.empty_cache();tr,base,img=v14.load_render();by={}
    for i in items:by.setdefault(i['family'],[]).append(i)
    report={'engine':'v15.2-live-semantic-validation','anchor_attempts':0,'branch_attempts':0,'context_attempts':0,'live_rejections':0,'early_aborts':0,'families':[]}
    accepted=[];rejected=0
    for fam,group in sorted(by.items()):
        group.sort(key=lambda x:x['tier']);t0=group[0];pe0,ppe0=emb[t0['id']];anchors=[]
        for a in range(ANCHORS):
            report['anchor_attempts']+=1
            try:
                raw,final,cov=v14.render(t0,None,pe0,ppe0,base,img,args.seed+fam*10000+a*15401)
                sc=anchor_score(final,cov);slab=v14.slab_score(final.getchannel('A'));boom=boom_score(final)
                if sc<.55 or slab>.12 or boom>.45 or not (.055<=cov<=.16):
                    report['live_rejections']+=1;print(f'KAGGLE_ANCHOR_LIVE_REJECT={t0["id"]} variant={a+1} score={sc:.3f} slab={slab:.2f} boom={boom:.2f} coverage={cov:.1%}',flush=True);continue
                anchors.append((sc,a,raw,final,cov));print(f'KAGGLE_ANCHOR_PASS={t0["id"]} variant={a+1} score={sc:.3f} boom={boom:.2f} coverage={cov:.1%}',flush=True)
            except Exception as e:print(f'KAGGLE_ANCHOR_REJECTED={t0["id"]} variant={a+1} reason={e}',flush=True)
            finally:gc.collect();torch.cuda.empty_cache()
        anchors.sort(key=lambda x:x[0],reverse=True);branches=[]
        for sc,a,raw0,final0,cov0 in anchors[:BRANCHES]:
            report['branch_attempts']+=1;recs=[(t0,final0,cov0)];prev=raw0;failed=False
            for i in group[1:]:
                pe,ppe=emb[i['id']]
                try:
                    prev,final,cov=render_contextual(i,prev,recs,pe,ppe,base,img,args.seed+fam*10000+a*15401+i['tier']*977,report)
                    recs.append((i,final,cov))
                except Exception as e:
                    report['early_aborts']+=1;print(f'KAGGLE_BRANCH_EARLY_ABORT=BLD-{fam:02d} branch={a+1} tier={i["tier"]} reason={e}',flush=True);failed=True;break
            if failed or len(recs)!=len(group):continue
            bscore,why=branch_score(recs);branches.append((bscore,a,recs,why));print(f'KAGGLE_BRANCH_SCORE=BLD-{fam:02d} branch={a+1} score={bscore:.3f} {why}',flush=True)
        branches.sort(key=lambda x:x[0],reverse=True);famrec={'family':fam,'anchors_generated':len(anchors),'branches_completed':len(branches)}
        if not branches or branches[0][0] < -100:
            rejected+=len(group);famrec['accepted']=False;report['families'].append(famrec);continue
        bscore,a,recs,why=branches[0];famrec.update({'accepted':True,'selected_branch':a+1,'score':bscore,'qa':why});report['families'].append(famrec)
        for i,final,cov in recs:
            p=v14.INCOMING/f"{i['stem']}.png";final.save(p,'PNG',optimize=True);accepted.append(i['id']);print(f'KAGGLE_VALIDATED={p.relative_to(v14.ROOT)} coverage={cov:.1%} selected_branch={a+1} score={bscore:.3f}',flush=True)
    (v14.INCOMING/'branch-search-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(f'KAGGLE_LIVE_QA context_attempts={report["context_attempts"]} live_rejections={report["live_rejections"]} early_aborts={report["early_aborts"]}',flush=True)
    print(f'KAGGLE_BRANCH_SEARCH anchors={report["anchor_attempts"]} branches={report["branch_attempts"]}',flush=True)
    print(f'KAGGLE_BUILDING_SUCCESS={len(accepted)} KAGGLE_BUILDING_REJECTED={rejected} KAGGLE_BUILDING_ATTEMPTED={len(items)}',flush=True)

if __name__=='__main__':main()
