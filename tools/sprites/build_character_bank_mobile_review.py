#!/usr/bin/env python3
"""Generate a complete offline mobile comparison of the 16 review-only sprites.

Data sources: the published SHA-256 checked candidate-bank ZIP and the
reproducible in-repository 18 original SVG/PNG atlases. Never promotes assets.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path

from PIL import Image

from build_character_candidate_bank import load_local_originals, validated_local_candidate

PNG_NAME = re.compile(r"^zte_chr_(op|log|eng|tech)_(idle|walk|work|carry|repair|celeb)_final\.png$")
COUNTS = {"idle": 6, "walk": 8, "work": 10, "carry": 8, "repair": 10, "celeb": 8}

HTML = r'''<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="dark">
<title>Zero to Empire · Revue des 16 personnages</title>
<style>
:root{color-scheme:dark;font:15px system-ui,-apple-system,sans-serif;background:#0c1421;color:#ecf3ff}
*{box-sizing:border-box}body{max-width:1050px;margin:0 auto;padding:14px}
h1{font-size:1.55rem;margin:7px 0}h2{font-size:1.05rem;margin:0 0 12px}
p{line-height:1.45;color:#b5c7de}.muted{color:#b5c7de;font-size:.9rem}
.card{background:#162335;border:1px solid #33465d;padding:14px;border-radius:12px;margin:12px 0}
button,select,textarea,input{font:inherit}button,select{background:#243a53;border:1px solid #50708c;
border-radius:8px;color:white;min-height:43px;padding:8px 11px}
button{cursor:pointer}button[aria-pressed="true"]{border:2px solid #75deea;background:#18546a}
button:focus-visible,select:focus-visible,input:focus-visible{outline:3px solid #80deea}
nav{display:flex;flex-wrap:wrap;gap:7px;margin:8px 0}
.framegrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.panel{background:#223446;border:1px solid #41596c;padding:10px;border-radius:10px;min-width:0}
.panel>canvas{display:block;width:min(100%,300px);height:auto;aspect-ratio:1;margin:auto;
border-radius:5px;background:#c1cbd1;image-rendering:auto}
.panel h3{font-size:.97rem;margin:4px 0}.tag{font-size:.78rem;color:#d7e8fa}
.controls{display:flex;flex-wrap:wrap;align-items:center;gap:9px}
.controls>input[type=range]{flex:1;min-width:140px;accent-color:#6cd7e4}
.stages{display:flex;flex-wrap:wrap;gap:24px;align-items:center}
.ministage{display:flex;align-items:center;gap:8px}
.ministage canvas{width:42px;height:42px;image-rendering:auto}
.ministage .day{background:#bdcbd3}.ministage .night{background:#101b29}
.warning{color:#ffcf88}.good{color:#8be6cb}
textarea{background:#0c1a2b;color:#e8f3ff;min-height:72px;width:100%;border:1px solid #52647b;
border-radius:8px;padding:10px;margin-top:7px}
label{display:block;margin:7px 0 3px}.warnlist{overflow-wrap:anywhere}
.footer{font-size:.88rem;color:#bacbe0}.counter{font-variant-numeric:tabular-nums}
@media(max-width:610px){.framegrid{grid-template-columns:1fr}.panel>canvas{max-width:280px}}
</style></head><body>
<h1>Zero to Empire · Revue des personnages</h1>
<p>16 animations candidates · premières créations et générations récupérées ·
<strong>hors ligne sur Android</strong>. Cette page n’approuve et ne publie aucun asset.</p>
<div class="card">
<h2>Choisir le personnage et l’action</h2><nav id="roles"></nav><nav id="actions"></nav>
<p id="progress" class="muted"></p>
</div>
<div class="framegrid">
<section class="panel"><h3>Candidat retenu dans le paquet</h3><canvas id="chosen" width="256" height="256"></canvas>
<p id="chosenSource" class="tag"></p></section>
<section class="panel"><h3>Original local · référence</h3><canvas id="local" width="256" height="256"></canvas>
<p class="tag">Même rôle/action · SVG modifiables et reproductibles</p></section>
</div>
<div class="card"><h2>Lecture synchronisée</h2>
<div class="controls">
<button id="toggle">Pause</button><button id="prev">← Image</button>
<button id="next">Image →</button><label for="fps">Vitesse</label>
<select id="fps"><option value="4">4 FPS</option><option value="6" selected>6 FPS</option>
<option value="8">8 FPS</option><option value="10">10 FPS</option><option value="12">12 FPS</option></select>
</div>
<div class="controls"><input id="scrub" type="range" min="0" max="7" step="1" value="0">
<strong class="counter" id="framecount">1 / 8</strong></div>
<h2>À l’échelle du jeu (42 px)</h2><div class="stages">
<div class="ministage"><span class="tag">Candidat</span>
<canvas class="night" id="chosenNight" width="42" height="42"></canvas>
<canvas class="day" id="chosenDay" width="42" height="42"></canvas></div>
<div class="ministage"><span class="tag">Original</span>
<canvas class="night" id="localNight" width="42" height="42"></canvas>
<canvas class="day" id="localDay" width="42" height="42"></canvas></div>
</div></div>
<div class="card"><h2>Points de contrôle visuel</h2>
<p id="warnings" class="warnlist"></p>
<p class="muted">Examiner les poses, le contact pied-sol, les mains, outils, visage, continuité
du costume et la lisibilité sur un téléphone. Un défaut non détecté automatiquement peut rester visible.</p>
<label for="reviewStatus">Appréciation personnelle (non transmise au jeu)</label>
<select id="reviewStatus"><option value="unreviewed">Non examiné</option>
<option value="polish">À améliorer graphiquement</option>
<option value="reject">Animation ou identité à refaire</option>
<option value="provisional">Acceptable pour une première passe seulement</option></select>
<label for="reviewNotes">Notes sur cette animation</label><textarea id="reviewNotes" maxlength="2500"
placeholder="Ex. jambes trop statiques, mains qui glissent, équipement incohérent…"></textarea>
<nav><button id="export">Exporter mes notes (JSON)</button></nav>
<p class="muted">Les appréciations restent dans cette page pendant la session. L’export est manuel ;
il ne modifie ni GitHub, ni les 219 assets strictement validés.</p>
</div><p class="footer" id="bankinfo"></p>
<script id="art-data" type="application/json">__ART_DATA__</script>
<script>
(()=>{'use strict';
const bank=JSON.parse(document.getElementById('art-data').textContent);
const byId=Object.fromEntries(bank.assets.map(x=>[x.id,x]));
const roleLabels={OP:'Opérateur',LOG:'Logistique',ENG:'Ingénieur'};
const actionLabels={IDLE:'Repos',WALK:'Marche',WORK:'Travail',CARRY:'Transport',REPAIR:'Réparer',CELEB:'Célébrer'};
const explain={
CROSS_ACTION_HEAD_IDENTITY_REVIEW:'Visage ou casque potentiellement différent de la référence du même métier : comparer côte à côte',
CROSS_ACTION_VISUAL_STYLE_REVIEW:'Écart visuel très marqué avec le rôle de référence : style et identité à revoir',
LOW_MOBILE_FRAME_CHANGE_REVIEW:'Animation trop peu visible à la taille du jeu (42 px) : examiner les poses',
WALK_LOWER_BODY_MOTION_REVIEW:'Mouvement du bas du corps peu perceptible : contrôler la marche',
NEAR_STATIC_TRANSITIONS_REVIEW:'Plusieurs transitions d’images presque immobiles à 42 px',
VISIBLE_LOOP_SEAM_REVIEW:'Possible saut visuel entre la fin et le début de l’animation',
CELEBRATION_NO_OVERHEAD_ARM_GESTURE_RISK:'Célébration peu lisible : bras insuffisamment levés',
ACTION_TRANSLATION_DOMINATES_POSE_RISK:'Glissement latéral dominant plutôt que variation des poses',
FACE_HEADGEAR_STRUCTURE_DRIFT_RISK:'Visage ou casque irrégulier entre les images',
PALETTE_IDENTITY_DISCONTINUITY_RISK:'Palette / costume pouvant changer en cours d’animation',
FRAME_SCALE_COLLAPSE_RISK:'Échelle du personnage pouvant varier',
BAKED_GROUND_SHADOW_RISK:'Ombre du sol intégrée au sprite'};
let current=bank.assets[0].id,frame=0,paused=false,fps=6,last=0,chosen=null,original=null;
const notes={};const $=id=>document.getElementById(id);
const roles=['OP','LOG','ENG'];
function button(label,on,selected){const b=document.createElement('button');b.textContent=label;
b.setAttribute('aria-pressed',String(selected));b.onclick=on;return b}
function select(id){if(!byId[id])return;store();current=id;frame=0;last=0;
const row=byId[id];chosen=new Image();original=new Image();
chosen.onload=render;original.onload=render;chosen.src=row.selectedAtlas;original.src=row.originalAtlas;
$('progress').textContent=row.id+' · '+row.frames+' images · '+(bank.assets.indexOf(row)+1)+' / '+bank.assets.length;
$('chosenSource').textContent=row.sourceType==='repo-local-original'?'Source : SVG/PNG original local':'Source : collecte GPU '+row.sourceRun;
const warnings=row.warnings.map(w=>explain[w]||w);
if(row.identityReference&&row.identityReference!==row.id){warnings.push('Référence du rôle : '+row.identityReference)}
$('warnings').textContent=warnings.length?warnings.join(' · '):'Aucun avertissement automatique enregistré. Vérification visuelle toujours nécessaire.';
$('warnings').className='warnlist '+(warnings.length?'warning':'good');
$('scrub').max=String(row.frames-1);
$('reviewStatus').value=(notes[id]||{}).status||'unreviewed';
$('reviewNotes').value=(notes[id]||{}).text||'';
const role=id.split('-')[1];
$('roles').replaceChildren(...roles.filter(r=>bank.assets.some(x=>x.id.startsWith('CHR-'+r+'-')))
.map(r=>button(roleLabels[r],()=>select(bank.assets.find(x=>x.id.startsWith('CHR-'+r+'-')).id),r===role)));
const actions=bank.assets.filter(x=>x.id.startsWith('CHR-'+role+'-'));
$('actions').replaceChildren(...actions.map(x=>button(actionLabels[x.id.split('-')[2]],()=>select(x.id),x.id===id)));
render()}
function store(){if(!current)return;notes[current]={status:$('reviewStatus').value,text:$('reviewNotes').value.slice(0,2500)}}
function draw(canvas,image,target){if(!image||!image.complete||!image.naturalWidth)return;
const ctx=canvas.getContext('2d');ctx.clearRect(0,0,canvas.width,canvas.height);
const x=(frame%4)*256,y=Math.floor(frame/4)*256;
ctx.drawImage(image,x,y,256,256,0,0,target,target)}
function render(){const row=byId[current];if(!row)return;
frame=(frame+row.frames)%row.frames;
$('scrub').value=String(frame);$('framecount').textContent=(frame+1)+' / '+row.frames;
draw($('chosen'),chosen,256);draw($('local'),original,256);
draw($('chosenNight'),chosen,42);draw($('chosenDay'),chosen,42);
draw($('localNight'),original,42);draw($('localDay'),original,42)}
function tick(ts){if(!paused&&document.visibilityState==='visible'&&ts-last>1000/fps){last=ts;frame++;render()}
requestAnimationFrame(tick)}
$('toggle').onclick=()=>{paused=!paused;$('toggle').textContent=paused?'Lecture':'Pause'};
$('prev').onclick=()=>{paused=true;$('toggle').textContent='Lecture';frame--;render()};
$('next').onclick=()=>{paused=true;$('toggle').textContent='Lecture';frame++;render()};
$('scrub').oninput=e=>{paused=true;$('toggle').textContent='Lecture';frame=Number(e.target.value);render()};
$('fps').onchange=e=>fps=Number(e.target.value);
$('reviewStatus').onchange=store;$('reviewNotes').oninput=store;
$('export').onclick=()=>{store();
const result={review_only:true,source:'zte-mobile-candidate-bank',date:new Date().toISOString(),
bank_production_processed:bank.productionProcessed,strict_done_unchanged:bank.strictDone,
ratings:bank.assets.map(x=>({id:x.id,status:(notes[x.id]||{}).status||'unreviewed',
notes:(notes[x.id]||{}).text||'',sha256:x.sha256}))};
const blob=new Blob([JSON.stringify(result,null,2)],{type:'application/json'});
const url=URL.createObjectURL(blob),link=document.createElement('a');
link.href=url;link.download='zte-character-art-review.json';link.click();
setTimeout(()=>URL.revokeObjectURL(url),1000)};
$('bankinfo').textContent='Sources vérifiées SHA-256 · '+bank.productionProcessed+'/'+bank.targetTotal+
' candidats disponibles · '+bank.strictDone+' strictement DONE · révision locale uniquement.';
select(bank.assets[0].id);requestAnimationFrame(tick);
})();</script></body></html>'''


def build(bank_path: Path, local_path: Path, destination: Path,
          audit_path: Path | None = None) -> dict:
    originals = load_local_originals(local_path)
    audit_by_id = None
    if audit_path is not None:
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        records = audit.get("assets")
        if (audit.get("review_only") is not True
                or audit.get("automatic_semantic_approval") is not False
                or audit.get("automatic_runtime_promotion") is not False
                or not isinstance(records, list)
                or len(records) != audit.get("candidate_count")):
            raise ValueError("Untrusted motion audit")
        audit_by_id = {str(row.get("id")): row for row in records}
        if len(audit_by_id) != len(records):
            raise ValueError("Duplicate motion audit IDs")
    with zipfile.ZipFile(bank_path) as bank:
        if bank.namelist().count("candidate-bank-index.json") != 1:
            raise ValueError("Missing or duplicate source candidate bank index")
        meta = json.loads(bank.read("candidate-bank-index.json"))
        rows = meta.get("bank_entries")
        if (not isinstance(rows, list) or not rows or
            meta.get("candidate_count") != len(rows) or
            meta.get("automatic_semantic_approval") is not False or
            meta.get("automatic_runtime_promotion") is not False):
            raise ValueError("Invalid review-only candidate bank")
        bank_names = bank.namelist()
        seen = set()
        embedded = []
        for row in rows:
            aid = str(row.get("id") or "")
            filename = str(row.get("filename") or "")
            match = PNG_NAME.fullmatch(filename)
            if (not match or aid != "CHR-"+match.group(1).upper()+"-"+match.group(2).upper()
                    or aid in seen or bank_names.count("candidates/"+filename) != 1):
                raise ValueError("Duplicate/unrecognized/missing candidate " + aid)
            seen.add(aid)
            source = bank.read("candidates/"+filename)
            if (hashlib.sha256(source).hexdigest() != row.get("sha256") or
                    len(source) != row.get("bytes")):
                raise ValueError("Incorrect selected candidate SHA-256: " + aid)
            with Image.open(io.BytesIO(source)) as atlas:
                atlas.load()
                if atlas.size != (1024,1024) or atlas.mode != "RGBA":
                    raise ValueError("Invalid selected atlas: " + aid)
            motion_flags = []
            identity_flags = []
            identity_reference = None
            if audit_by_id is not None:
                audit_record = audit_by_id.get(aid)
                if (not audit_record or audit_record.get("sha256") != row.get("sha256")
                        or audit_record.get("strict_approved") is not False
                        or audit_record.get("runtime_promoted") is not False):
                    raise ValueError("Stale/untrusted motion audit for " + aid)
                motion_flags = [str(flag) for flag in (audit_record.get("new_motion_flags") or [])]
                identity_flags = [str(flag) for flag in (audit_record.get("new_identity_flags") or [])]
                identity_reference = (audit_record.get("head_identity_metrics") or {}).get("reference_id")
            if aid not in originals:
                raise ValueError("Missing original reference: " + aid)
            original, _ = validated_local_candidate(
                {"id": aid, "runtime": row["runtime_target_for_later_approval"]},
                originals[aid])
            embedded.append({
                "id": aid, "frames": COUNTS[match.group(2)],
                "selectedAtlas": "data:image/png;base64," + base64.b64encode(source).decode("ascii"),
                "originalAtlas": "data:image/png;base64," + base64.b64encode(original).decode("ascii"),
                "sourceType": row.get("source_type"),
                "sourceRun": row.get("source_collector_run_id"),
                "warnings": sorted(set(
                    [str(x) for x in row.get("deferred_art_warnings") or []] + motion_flags + identity_flags
                )),
                "sha256": row["sha256"],
                "identityReference": identity_reference,
            })
    if audit_by_id is not None and set(audit_by_id) != seen:
        raise ValueError("Motion audit coverage does not match bank")
    payload = {
        "schemaVersion": 1, "reviewOnly": True,
        "targetTotal": meta["target_total"],
        "productionProcessed": meta["production_processed"],
        "strictDone": meta["strict_done"],
        "assets": embedded,
    }
    serialized = json.dumps(payload, ensure_ascii=False, separators=(",",":"))
    # Avoid closing <script> from tainted machine-written warning text.
    serialized = serialized.replace("<","\\u003c").replace(">","\\u003e").replace("&","\\u0026")
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(HTML.replace("__ART_DATA__", serialized), encoding="utf-8")
    return {"review_only":True,"assets":len(embedded),"strict_done_added":0,
            "bytes":destination.stat().st_size,
            "candidate_scope_complete":meta.get("candidate_production_complete") is True}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--local-original", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--motion-audit", type=Path)
    args = parser.parse_args()
    print(json.dumps(build(args.bank,args.local_original,args.output,args.motion_audit),sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
