"""Offline Android animation comparison for *already verified* polish proposals.

Called only after the candidate bank, same-run reference atlas and all-frame
alternative have passed source/audit SHA-256 checks. This viewer never
updates game resources, certifies art or transmits the review notes.
"""
from __future__ import annotations

import base64
import json
from pathlib import Path


HTML = r'''<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="dark">
<title>Zero to Empire · Comparaison animée des visages</title>
<style>
:root{color-scheme:dark;font:15px system-ui,-apple-system,sans-serif;background:#0b1422;color:#eff8ff}
*{box-sizing:border-box}body{max-width:840px;margin:0 auto;padding:14px}
h1{font-size:1.43rem;margin:9px 0}h2{font-size:1.05rem;margin:6px 0 12px}
p{line-height:1.5;color:#bbccde}.muted{color:#bbccde;font-size:.88rem}
.card{background:#152338;border:1px solid #33465d;padding:13px;border-radius:11px;margin:12px 0}
nav,.controls{display:flex;align-items:center;flex-wrap:wrap;gap:9px;margin:10px 0}
button,select,textarea{font:inherit;color:white;background:#26425f;border:1px solid #557693;border-radius:8px}
button,select{min-height:44px;padding:8px 12px}button{cursor:pointer}
button[aria-pressed="true"]{border:2px solid #83e9ec;background:#155665}
button:focus-visible,select:focus-visible,textarea:focus-visible,input:focus-visible{outline:3px solid #80deea}
.compare{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.panel{background:#24384e;border:1px solid #46627c;border-radius:10px;padding:10px;min-width:0}
.panel h3{font-size:.98rem;margin:1px 0 10px}
.panel>canvas{display:block;width:min(100%,300px);height:auto;aspect-ratio:1;background:#c2cfd9;
border-radius:6px;margin:auto}
.stage{display:flex;justify-content:space-between;align-items:center;gap:8px;margin:10px 0}
.tiny{display:flex;gap:8px;align-items:center}.tiny canvas{width:42px;height:42px}
.tiny .day{background:#bfd0da}.tiny .night{background:#101b29}
.tag{font-size:.8rem;color:#d1e8f2;overflow-wrap:anywhere}
.range{flex:1;min-width:110px;accent-color:#6ae2e4}
textarea{display:block;padding:9px;width:100%;min-height:76px;margin-top:6px}
label{display:block;margin:9px 0 4px}strong.counter{font-variant-numeric:tabular-nums}
@media(max-width:530px){.compare{grid-template-columns:1fr}.panel>canvas{max-width:270px}}
</style></head><body>
<h1>Zero to Empire · Harmonisation des visages</h1>
<p>Comparaison synchronisée de variantes <strong>en attente de revue</strong>.
Le transfert automatique améliore la ressemblance du visage mais peut créer des
raccords visibles près du cou et du costume. <strong>Aucun sprite n'est approuvé ni publié dans le jeu.</strong></p>
<div class="card"><h2>Choisir une animation</h2><nav id="choices"></nav>
<p class="muted" id="progress"></p><p class="tag" id="difference"></p></div>
<div class="compare">
<section class="panel"><h3>Source originale</h3><canvas id="original" width="256" height="256"></canvas>
<p class="tag" id="sourceHash"></p></section>
<section class="panel"><h3>Variante à examiner</h3><canvas id="polished" width="256" height="256"></canvas>
<p class="tag" id="polishedHash"></p></section>
</div>
<div class="card">
<h2>Animation à la taille du jeu (42 px)</h2>
<div class="stage">
<div class="tiny"><span class="tag">Avant</span><canvas class="night" id="beforeNight" width="42" height="42"></canvas><canvas class="day" id="beforeDay" width="42" height="42"></canvas></div>
<div class="tiny"><span class="tag">Après</span><canvas class="night" id="afterNight" width="42" height="42"></canvas><canvas class="day" id="afterDay" width="42" height="42"></canvas></div>
</div>
<nav class="controls"><button id="play">Pause</button><button id="previous">← Image</button>
<button id="next">Image →</button><label for="fps">Vitesse</label>
<select id="fps"><option value="4">4 FPS</option><option value="6" selected>6 FPS</option>
<option value="8">8 FPS</option><option value="12">12 FPS</option></select></nav>
<div class="controls"><input aria-label="Position de l'animation" id="scrub" class="range"
type="range" min="0" max="9" step="1" value="0"><strong class="counter" id="counter">1 / 10</strong></div>
</div>
<div class="card"><h2>Revue artistique personnelle</h2>
<p class="muted">Vérifier la continuité visage/casque, les éventuelles coutures au cou,
la couleur du costume et des gants, les outils et les mouvements aux différentes vitesses.
Une erreur de visage sur une seule image suffit à refuser l'alternative.</p>
<label for="rating">Évaluation de la variante (non transmise au jeu)</label>
<select id="rating"><option value="unreviewed">Non examinée</option>
<option value="better-needs-polish">Meilleure, mais à retravailler</option>
<option value="reject">Refuser la variante</option>
<option value="provisional">Provisoire, nécessite une validation complète</option></select>
<label for="notes">Notes</label><textarea id="notes" maxlength="2400"
placeholder="Exemple : visage cohérent mais raccord au col visible..."></textarea>
<nav><button id="export">Exporter les observations (JSON)</button></nav>
<p class="muted">Cette page fonctionne hors connexion. Les notes restent en mémoire pendant
la session et l'export est manuel. Aucun envoi à GitHub ni validation automatique.</p></div>
<p class="muted" id="summary"></p>
<script id="polish-data" type="application/json">__DATA__</script>
<script>
(()=>{'use strict';
const data=JSON.parse(document.getElementById('polish-data').textContent);
const byId=Object.fromEntries(data.alternatives.map(x=>[x.id,x]));
const $=id=>document.getElementById(id);
const review={};let current=null,frame=0,paused=false,fps=6,last=0,before=null,after=null;
function store(){if(!current)return;review[current]={status:$('rating').value,notes:$('notes').value.slice(0,2400)}}
function button(label,callback,selected){const b=document.createElement('button');b.textContent=label;
b.setAttribute('aria-pressed',String(selected));b.onclick=callback;return b}
function select(id){if(!byId[id])return;store();current=id;frame=0;last=0;
const row=byId[id];before=new Image();after=new Image();before.onload=render;after.onload=render;
before.src=row.originalAtlas;after.src=row.polishedAtlas;
$('progress').textContent=row.id+' · '+row.frames+' images · référence : '+row.referenceId;
$('difference').textContent='Écart visuel de la tête : '+row.before.toFixed(2)+' → '+row.after.toFixed(2)+
' (mesure technique, pas une validation artistique)';
$('sourceHash').textContent='SHA-256 source : '+row.sourceSha;
$('polishedHash').textContent='SHA-256 proposition : '+row.alternativeSha;
$('scrub').max=String(row.frames-1);
$('rating').value=(review[id]||{}).status||'unreviewed';
$('notes').value=(review[id]||{}).notes||'';
$('choices').replaceChildren(...data.alternatives.map(x=>button(x.id,()=>select(x.id),x.id===id)));
render()}
function paint(id,img,side){const canvas=$(id),ctx=canvas.getContext('2d');
ctx.clearRect(0,0,canvas.width,canvas.height);
if(!img||!img.complete||!img.naturalWidth)return;
const x=(frame%4)*256,y=Math.floor(frame/4)*256;
ctx.drawImage(img,x,y,256,256,0,0,side,side)}
function render(){const row=byId[current];if(!row)return;
frame=(frame+row.frames)%row.frames;
$('scrub').value=String(frame);$('counter').textContent=(frame+1)+' / '+row.frames;
paint('original',before,256);paint('polished',after,256);
paint('beforeNight',before,42);paint('beforeDay',before,42);
paint('afterNight',after,42);paint('afterDay',after,42)}
function tick(now){if(!paused&&document.visibilityState==='visible'&&now-last>1000/fps){last=now;frame++;render()}
requestAnimationFrame(tick)}
function pause(){paused=true;$('play').textContent='Lecture'}
$('play').onclick=()=>{paused=!paused;$('play').textContent=paused?'Lecture':'Pause'};
$('previous').onclick=()=>{pause();frame--;render()};
$('next').onclick=()=>{pause();frame++;render()};
$('fps').onchange=event=>{fps=Number(event.target.value)};
$('scrub').oninput=event=>{pause();frame=Number(event.target.value);render()};
$('rating').onchange=store;$('notes').oninput=store;
$('export').onclick=()=>{store();const payload={review_only:true,
source:'zte-identity-polish-review',generated_at:new Date().toISOString(),
strict_done_unchanged:data.strictDone,
reviews:data.alternatives.map(row=>({id:row.id,
original_sha256:row.sourceSha,alternative_sha256:row.alternativeSha,
status:(review[row.id]||{}).status||'unreviewed',
notes:(review[row.id]||{}).notes||''}))};
const blob=new Blob([JSON.stringify(payload,null,2)],{type:'application/json'});
const href=URL.createObjectURL(blob),a=document.createElement('a');
a.href=href;a.download='zte-identity-polish-review.json';a.click();
setTimeout(()=>URL.revokeObjectURL(href),1000)};
$('summary').textContent=data.alternatives.length+' alternatives vérifiées SHA-256 · '+
data.strictDone+' assets strictement validés dans la file officielle, sans modification.';
if(data.alternatives.length)select(data.alternatives[0].id);
else $('progress').textContent='Aucune alternative sûre disponible. Ne pas remplacer les originaux.';
requestAnimationFrame(tick);
})();</script></body></html>'''


def write_mobile_review(rows: list[dict], destination: Path,
                        strict_done: int) -> dict:
    """rows must be supplied by the verified character identity polish builder."""
    if not isinstance(strict_done, int) or not 0 <= strict_done <= 235:
        raise ValueError("Invalid strict DONE reference")
    seen: set[str] = set()
    embedded: list[dict] = []
    for row in rows:
        asset_id = row["id"]
        if (not isinstance(asset_id, str) or not asset_id.startswith("CHR-")
                or asset_id in seen):
            raise ValueError("Invalid or duplicate review proposal ID")
        seen.add(asset_id)
        if not 4 <= row["frames"] <= 16:
            raise ValueError("Invalid review animation frame count")
        embedded.append({
            "id": asset_id, "frames": row["frames"],
            "referenceId": row["reference_id"],
            "sourceSha": row["source_sha256"],
            "alternativeSha": row["alternative_sha256"],
            "before": row["head_rgb_before"],
            "after": row["head_rgb_after"],
            "originalAtlas": "data:image/png;base64," +
                            base64.b64encode(row["original_png"]).decode("ascii"),
            "polishedAtlas": "data:image/png;base64," +
                            base64.b64encode(row["alternative_png"]).decode("ascii"),
        })
    payload = {"schemaVersion": 1, "reviewOnly": True,
               "strictDone": strict_done, "alternatives": embedded}
    serialized = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    serialized = (serialized.replace("<", "\\u003c")
                  .replace(">", "\\u003e").replace("&", "\\u0026"))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(HTML.replace("__DATA__", serialized), encoding="utf-8")
    return {"review_only": True, "assets": len(rows),
            "strict_done_added": 0, "bytes": destination.stat().st_size}
