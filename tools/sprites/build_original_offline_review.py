#!/usr/bin/env python3
"""Offline Android-first sprite inspection; never changes strict DONE."""
from __future__ import annotations
import argparse,base64,json
from pathlib import Path
from PIL import Image

ROLES=("OP","LOG","ENG")
FRAMES={"IDLE":6,"WALK":8,"WORK":10,"CARRY":8,"REPAIR":10,"CELEB":8}

HTML=r'''<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="dark"><title>Zero to Empire · Revue originale</title>
<style>
*{box-sizing:border-box}body{margin:0 auto;padding:16px;max-width:940px;background:#0d1420;color:#e6eef9;font:15px system-ui,sans-serif}
h1{font-size:1.8rem;margin:6px 0}h2{font-size:1.15rem;margin:6px 0 12px}
p,.muted{color:#b6c4d8;line-height:1.5}.warn{border-left:3px solid #efbb78;padding:9px;background:#292a30}
.card{background:#172132;border:1px solid #31425b;border-radius:14px;padding:14px;margin:12px 0}
nav{display:flex;flex-wrap:wrap;gap:8px;margin:11px 0}button{cursor:pointer;border:1px solid #476078;background:#243348;color:#f4f8ff;border-radius:9px;padding:10px 12px;min-height:44px}
button[aria-pressed=true]{border:2px solid #69d7e6;background:#1b4a63}button:focus-visible{outline:3px solid #fff}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:13px}.stage{display:grid;place-items:center;min-height:250px;border-radius:10px;background:#455566}
.stage img,.stage canvas{width:min(100%,310px);aspect-ratio:1;object-fit:contain}
#frame{display:none}input[type=range]{width:100%;accent-color:#65d8e6}
.game{display:flex;gap:10px}.cell{flex:1;display:grid;place-items:center;min-height:120px;background:#101b24}.cell.day{background:#bdcdd7;color:#243a45}
.cell img,.cell canvas{width:42px;height:42px}.cell.day img,.cell.day canvas{width:39px;height:39px}
.cell canvas{display:none}
pre{white-space:pre-wrap;overflow-wrap:anywhere;color:#a9bacc;font-size:.81rem}
@media(max-width:650px){.cols{grid-template-columns:1fr}body{padding:10px}.stage{min-height:245px}}
</style></head><body>
<h1>Zero to Empire · Personnages</h1><p>18 atlas · 150 poses SVG · créés dans le projet · lecture hors ligne</p>
<p class="warn">REVUE UNIQUEMENT · 16 actions à valider · 2 IDLE de référence. Aucun changement automatique du compteur strict.</p>
<section class="card"><h2>Métier</h2><nav id="roles"></nav><h2>Animation</h2><nav id="actions"></nav></section>
<div class="cols"><section class="card"><h2 id="title">Opérateur</h2><div class="stage"><img id="animation" alt="Animation originale"><canvas id="frame" width="256" height="256"></canvas></div>
<p id="source" class="muted"></p></section>
<section class="card"><h2>Contrôler les frames</h2><nav><button id="mode">Voir les frames</button><button id="previous">← Précédente</button><button id="following">Suivante →</button></nav>
<label for="scrub">Frame <span id="index">1 / 8</span></label><input id="scrub" type="range" min="0" max="7" step="1" value="0">
<p class="muted">Comparer le visage, les pieds, la caisse, les outils et la continuité de la boucle. En mode frame, les aperçus nuit et jour sont figés sur la même pose.</p>
<h2>À l'échelle du jeu</h2><div class="game"><div class="cell"><span>Nuit · 42px</span><img id="night" alt="Aperçu nuit"><canvas id="night-frame" width="256" height="256" aria-label="Pose figée de nuit"></canvas></div>
<div class="cell day"><span>Jour · 39px</span><img id="day" alt="Aperçu jour"><canvas id="day-frame" width="256" height="256" aria-label="Pose figée de jour"></canvas></div></div></section></div>
<section class="card"><h2>Vérifications visuelles</h2><p>Une vraie action lisible · même personnage sur les six actions · mains reliées aux objets ·
pieds correctement plantés · boucle sans saut · identifiable à 39 pixels.</p><p class="muted">Le passage technique ne vaut pas approbation AAA ou Android production.</p></section>
<script type="application/json" id="embedded">__MEDIA__</script><script>
(()=>{'use strict';
const data=JSON.parse(document.getElementById('embedded').textContent);
const actions=['IDLE','WALK','WORK','CARRY','REPAIR','CELEB'];const roles=['OP','LOG','ENG'];
const labels={IDLE:'Repos',WALK:'Marche',WORK:'Travail',CARRY:'Transport',REPAIR:'Réparer',CELEB:'Célébrer',OP:'Opérateur',LOG:'Logistique',ENG:'Ingénieur'};
let role='OP',action='WALK',frame=0,still=false,atlas=new Image();
const E=id=>document.getElementById(id),current=()=>data[role+'-'+action];
function controls(id,values,change,selected){const host=E(id);host.replaceChildren();
for(const item of values){const b=document.createElement('button');b.textContent=labels[item];b.setAttribute('aria-pressed',String(item===selected));
b.onclick=()=>change(item);host.append(b)}}
function paint(){const item=current();frame=(frame+item.count)%item.count;E('scrub').max=item.count-1;E('scrub').value=frame;
E('index').textContent=(frame+1)+' / '+item.count;
if(still&&atlas.complete&&atlas.naturalWidth){
// Use exactly the same atlas cell for all three canvases. Animated GIFs
// cannot be scrubbed reliably and must be hidden during frame inspection.
for(const id of ['frame','night-frame','day-frame']){
const ctx=E(id).getContext('2d');ctx.clearRect(0,0,256,256);
ctx.drawImage(atlas,(frame%4)*256,Math.floor(frame/4)*256,256,256,0,0,256,256)}}}
function mode(){for(const [gif,canvas] of [['animation','frame'],['night','night-frame'],['day','day-frame']]){
E(gif).style.display=still?'none':'block';E(canvas).style.display=still?'block':'none'}
E('scrub').disabled=!still;E('previous').disabled=!still;E('following').disabled=!still;
E('mode').textContent=still?'Revenir à l’animation':'Voir les frames';paint()}
function render(){const item=current();frame=0;still=false;atlas=new Image();atlas.onload=paint;atlas.src=item.atlas;
E('animation').src=item.animation;E('night').src=item.animation;E('day').src=item.animation;
E('title').textContent=labels[role]+' · '+labels[action];E('source').textContent='CHR-'+role+'-'+action+
' · '+item.count+' frames · 1024 × 1024 · '+(action==='IDLE'&&role!=='ENG'?'IDLE contexte':'Non approuvé');
controls('roles',roles,r=>{role=r;render()},role);controls('actions',actions,a=>{action=a;render()},action);mode()}
E('mode').onclick=()=>{still=!still;mode()};E('previous').onclick=()=>{frame--;paint()};
E('following').onclick=()=>{frame++;paint()};E('scrub').oninput=e=>{still=true;frame=Number(e.target.value);mode()};
render()})();</script></body></html>'''

def build(source:Path,destination:Path)->dict:
    manifest=json.loads((source/'creation-manifest.json').read_text(encoding='utf-8'))
    expected={f'CHR-{role}-{action}' for role in ROLES for action in FRAMES}
    if (manifest.get('review_only') is not True or manifest.get('strict_done_added')!=0
        or len(manifest.get('assets',[]))!=18
        or {row.get('id') for row in manifest['assets']}!=expected):
        raise ValueError('Untrusted original character candidate manifest')
    media={}
    for role in ROLES:
        for action,count in FRAMES.items():
            name=f'zte_chr_{role.lower()}_{action.lower()}_final.png'
            src=source/'candidates'/name
            gif=source/'previews'/f'{role.lower()}-{action.lower()}.gif'
            with Image.open(src) as im:
                if im.size!=(1024,1024) or im.mode!='RGBA':
                    raise ValueError('Incorrect original atlas '+name)
            with Image.open(gif) as im:
                if im.format!='GIF' or not (2<=im.n_frames<=count):
                    raise ValueError('Incorrect original preview '+gif.name)
            media[role+'-'+action]={
                'count':count,
                'atlas':'data:image/png;base64,'+base64.b64encode(src.read_bytes()).decode(),
                'animation':'data:image/gif;base64,'+base64.b64encode(gif.read_bytes()).decode()}
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(HTML.replace('__MEDIA__',json.dumps(media,separators=(',',':'))),encoding='utf-8')
    return {'review_only':True,'assets':len(media),'frames':150,
            'bytes':destination.stat().st_size,'strict_done_added':0}

if __name__=='__main__':
    a=argparse.ArgumentParser()
    a.add_argument('--source',type=Path,default=Path('art/incoming/chatgpt-original'))
    a.add_argument('--output',type=Path,required=True)
    p=a.parse_args()
    print(json.dumps(build(p.source,p.output),sort_keys=True))
