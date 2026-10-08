#!/usr/bin/env python3
"""Deterministic, unattended walk-sprite generator for Zero to Empire.

Uses one identity-locked vector renderer from pose_studio.html and a cyclic,
world-space planted-foot trajectory. No Kaggle, prompts or UI operations.
Outputs are review candidates, NEVER strict DONE.
"""
from __future__ import annotations

import argparse
import base64
import io
import hashlib
import json
import math
import shutil
import statistics
import zipfile
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

from PIL import Image

CANVAS = 512
GROUND = 446
ROOT_X = 252
HIP_Y = 270
KINEMATIC_REACH = 94 + 99 - 1


@dataclass(frozen=True)
class WalkSettings:
    asset_id: str = 'CHR-TECH-WALK'
    frames: int = 24
    fps: int = 12
    stride: float = 92.0
    clearance: float = 36.0
    stance_fraction: float = 0.62
    pelvis_bob: float = 3.5
    arm_swing: float = 30.0
    palette: str = 'cyan'

    def validate(self) -> None:
        if self.frames < 8 or self.frames > 64 or self.frames % 2:
            raise ValueError('frames must be even between 8 and 64')
        if not 3 <= self.fps <= 24:
            raise ValueError('fps must be 3-24')
        if not 30 <= self.stride <= 110:
            raise ValueError('stride must be 30-110')
        if not 10 <= self.clearance <= 70:
            raise ValueError('clearance must be 10-70')
        if not .53 <= self.stance_fraction <= .72:
            raise ValueError('stance_fraction must be .53-.72')
        if self.palette not in {'cyan', 'amber', 'lime'}:
            raise ValueError('palette must be cyan, amber or lime')


def ease_hermite(start: float, end: float, u: float, slope_u: float) -> float:
    """Cubic position and velocity matching at lift-off/touch-down."""
    h00 = 2 * u**3 - 3 * u**2 + 1
    h10 = u**3 - 2 * u**2 + u
    h01 = -2 * u**3 + 3 * u**2
    h11 = u**3 - u**2
    return h00*start + h10*slope_u + h01*end + h11*slope_u


def foot_local(phase: float, settings: WalkSettings) -> tuple[float, float, bool]:
    """Foot trajectory relative to torso. During stance the planted foot does
    not move in world coordinates as the body advances at constant speed.
    """
    phase %= 1.0
    d = settings.stance_fraction
    s = settings.stride
    if phase < d:
        return s/2 - (s/d)*phase, GROUND, True
    u = (phase-d)/(1-d)
    slope_u = -(s/d)*(1-d)
    x = ease_hermite(-s/2, s/2, u, slope_u)
    y = GROUND - settings.clearance*(math.sin(math.pi*u)**1.3)
    return x, y, False


def foot_roll(phase: float, settings: WalkSettings) -> float:
    """Toe tilt in radians, continuous across toe-off and heel-strike.
    Negative = toe lifted before landing; positive = toe pointed down on push.
    Exact ankle/ground positions remain governed by foot_local().
    """
    phase %= 1.0
    d = settings.stance_fraction
    if phase < d:
        u = phase / d
        if u < .17:
            return -.18 * (1 - u / .17)
        if u > .8:
            return .22 * ((u - .8) / .2)
        return 0.0
    u = (phase - d) / (1 - d)
    return .22 * (1-u) - .18 * u


def pose(t: float, settings: WalkSettings) -> dict[str, Any]:
    t %= 1.0
    rx, ry = ROOT_X, HIP_Y + settings.pelvis_bob*math.cos(4*math.pi*t)
    lx, ly, lock_l = foot_local(t+.5, settings)
    fx, fy, lock_r = foot_local(t, settings)
    # Arms counter-swing to legs, with sub-pixel smooth motion.
    opposite = settings.arm_swing*math.cos(2*math.pi*t)
    return {
        'root': {'x': rx, 'y': ry},
        'left': {'x': rx+lx, 'y': ly},
        'right': {'x': rx+fx, 'y': fy},
        'handL': {'x': rx-19+opposite, 'y': ry-18-5*math.sin(2*math.pi*t)},
        'handR': {'x': rx+43-opposite, 'y': ry-21+5*math.sin(2*math.pi*t)},
        'lockL': lock_l, 'lockR': lock_r,
        'rollL': foot_roll(t+.5, settings), 'rollR': foot_roll(t, settings),
    }


def length(a: dict, b: dict) -> float:
    return math.hypot(a['x']-b['x'], a['y']-b['y'])


def pose_distance(a: dict, b: dict) -> float:
    return math.sqrt(sum(length(a[k], b[k])**2 for k in ('root','left','right','handL','handR')))


def verify_motion(settings: WalkSettings) -> dict[str, Any]:
    """Numerical QA is independent of the renderer and cannot approve art."""
    samples = max(192, settings.frames*8)
    points = [pose(i/samples,settings) for i in range(samples)]
    bad_reach, penetration, stance_error, swing_samples = [], [], [], []
    velocity = settings.stride / settings.stance_fraction
    step = 1.0 / samples
    for i, p in enumerate(points):
        for side, hip_shift in [('left',-13),('right',13)]:
            foot = p[side]
            hip = {'x':p['root']['x']+hip_shift, 'y':p['root']['y']}
            reach = length(hip,foot)
            if reach > KINEMATIC_REACH:
                bad_reach.append({'frame':i,'side':side,'length':reach})
            if foot['y'] > GROUND + 1e-7:
                penetration.append({'frame':i,'side':side,'excess':foot['y']-GROUND})
            if p[f'lock{side[0].upper()}'] and points[(i+1)%samples][f'lock{side[0].upper()}']:
                # Stay inside one contiguous stance; avoid wrapping phase-snap.
                nxt=points[(i+1)%samples][side]
                # Absolute positions are relative to a torso moving at velocity 'velocity'.
                dx=nxt['x']-foot['x'] + velocity*step
                dy=nxt['y']-foot['y']
                if i < samples-1: stance_error.append(math.hypot(dx,dy))
            if not p[f'lock{side[0].upper()}']:
                swing_samples.append(GROUND-foot['y'])
    poses=[pose(i/settings.frames, settings) for i in range(settings.frames)]
    edges=[pose_distance(poses[i],poses[(i+1)%settings.frames]) for i in range(settings.frames)]
    median=statistics.median(edges)
    seam_ratio=edges[-1]/median if median else math.inf
    q={
        'kinematic_reach_violations':len(bad_reach),
        'penetrations':len(penetration),
        'max_planted_world_slip_px_per_sample':max(stance_error,default=0),
        'max_swing_clearance_px':max(swing_samples,default=0),
        'mean_swing_clearance_px':statistics.mean(swing_samples) if swing_samples else 0,
        'seam_joint_distance_px':edges[-1],
        'median_adjacent_joint_distance_px':median,
        'seam_to_median_ratio':seam_ratio,
        'transition_joint_distances_px':edges,
        'frame_contact_labels':[('both' if p['lockL'] and p['lockR'] else 'left' if p['lockL'] else 'right' if p['lockR'] else 'air') for p in poses],
        'technical_motion_pass':not (bad_reach or penetration) and max(stance_error,default=0)<.02 and .65 <= seam_ratio <=1.65,
        'visual_review_pass':False,
        'semantic_review_pass':False,
    }
    return q


def render(poses: list[dict[str,Any]], source_html: Path, palette: str) -> list[Image.Image]:
    from playwright.sync_api import sync_playwright
    if not source_html.exists():
        raise FileNotFoundError(f'Pose Studio renderer missing: {source_html}')
    frames=[]
    with sync_playwright() as playwright:
        browser=playwright.chromium.launch(headless=True,executable_path=shutil.which('chromium') or shutil.which('google-chrome'),args=['--no-sandbox'])
        try:
            page=browser.new_page(viewport={'width':600,'height':600})
            failures=[]
            page.on('pageerror',lambda x: failures.append(str(x)))
            page.set_content(source_html.read_text(encoding='utf-8'),wait_until='load')
            page.evaluate('(palette) => {state.playing=false;state.skin=palette}',palette)
            for p in poses:
                png_url=page.evaluate('''p => {const c=document.createElement('canvas');c.width=512;c.height=512;
                 scene(c.getContext('2d'),p,{background:false,handles:false});return c.toDataURL('image/png')}''',p)
                frames.append(Image.open(io.BytesIO(base64.b64decode(png_url.split(',',1)[1]))).convert('RGBA'))
            if failures:
                raise RuntimeError(f'Browser rendering errors: {failures}')
        finally:
            browser.close()
    return frames


def check_alpha(frames: list[Image.Image]) -> dict[str,Any]:
    touched=[]; empty=[]; bounds=[]
    for i, im in enumerate(frames):
        box=im.getchannel('A').getbbox()
        if not box:empty.append(i);continue
        bounds.append(list(box))
        if box[0]<=4 or box[1]<=4 or box[2]>=im.width-4 or box[3]>=im.height-4:
            touched.append(i)
    return {'empty_frames':empty,'edge_touched_frames':touched,'alpha_bounds':bounds,
            'technical_alpha_pass':not empty and not touched}


def export(output:Path, settings:WalkSettings, html:Path, bundle: bool=True) -> dict:
    settings.validate()
    output.mkdir(parents=True, exist_ok=True)
    frames_list=[pose(i/settings.frames,settings) for i in range(settings.frames)]
    q=verify_motion(settings)
    frames=render(frames_list,html,settings.palette)
    qa_alpha=check_alpha(frames)
    q.update(qa_alpha)
    # Silhouette seam is measured on the actual alpha pixels, not just IK joints.
    import numpy as np
    def silhouette_diff(a:Image.Image,b:Image.Image)->float:
        x=np.asarray(a.getchannel('A'))>127
        y=np.asarray(b.getchannel('A'))>127
        union=np.count_nonzero(x|y)
        return float(np.count_nonzero(x^y)/union) if union else 1.0
    transitions=[silhouette_diff(frames[i],frames[(i+1)%len(frames)]) for i in range(len(frames))]
    median_visual=statistics.median(transitions)
    q['silhouette_transition_disagreement']=transitions
    q['silhouette_seam_disagreement']=transitions[-1]
    q['silhouette_seam_to_median_ratio']=transitions[-1]/median_visual if median_visual else math.inf
    q['technical_pass']=(q['technical_motion_pass'] and q['technical_alpha_pass']
        and .30 <= q['silhouette_seam_to_median_ratio'] <= 2.2)
    atlas=Image.new('RGBA',(CANVAS*4,CANVAS*math.ceil(settings.frames/4)))
    for i,im in enumerate(frames):
        out=output/'frames'/f'{settings.asset_id}-{i:02d}.png'
        out.parent.mkdir(exist_ok=True)
        im.save(out,optimize=True)
        atlas.alpha_composite(im,((i%4)*CANVAS,(i//4)*CANVAS))
    atlas.save(output/'atlas.png', optimize=True)
    thumbs=[]
    for im in frames:
        rgb=Image.new('RGB',(CANVAS,CANVAS),(28,36,47))
        rgb.paste(im,mask=im.getchannel('A'))
        thumbs.append(rgb.resize((256,256),Image.Resampling.LANCZOS))
    thumbs[0].save(output/'preview.gif',save_all=True,append_images=thumbs[1:],duration=int(round(1000/settings.fps)),loop=0,optimize=False)
    review=Image.new('RGB',(256*8,256*math.ceil(settings.frames/8)),(24,32,44))
    for i,im in enumerate(thumbs):
        review.paste(im,((i%8)*256,(i//8)*256))
    review.save(output/'contact-sheet.jpg',quality=88)
    editable={
        'format':'zte-pose-studio-v1','asset_id':settings.asset_id,'strict_status':'NEEDS_REVIEW',
        'review_required':True,'canvas':{'width':CANVAS,'height':CANVAS,'ground':GROUND},
        'fps':settings.fps,'frame_count':settings.frames,'palette':settings.palette,
        'controls':{'preset':'walk','stride':settings.stride,'lift':settings.clearance,'arms':settings.arm_swing,'bounce':settings.pelvis_bob},
        'poses':[pose(i/8,settings) for i in range(8)],
    }
    (output/'project.json').write_text(json.dumps(editable,indent=2,ensure_ascii=False),encoding='utf-8')
    events = []
    for i, p in enumerate(frames_list):
        contact = ('both' if p['lockL'] and p['lockR'] else
                   'left' if p['lockL'] else 'right' if p['lockR'] else 'air')
        events.append({'frame': i, 'time_seconds': i/settings.fps,
            'contact': contact, 'left_foot_roll_degrees': round(math.degrees(p['rollL']),3),
            'right_foot_roll_degrees': round(math.degrees(p['rollR']),3),
            'footstep_event': ('right' if i == 0 else 'left' if i == settings.frames//2 else None)})
    (output/'frame-events.json').write_text(json.dumps({
        'asset_id':settings.asset_id, 'format':'zte-footstep-events-v1',
        'strict_status':'NEEDS_REVIEW','frames':events},indent=2),encoding='utf-8')
    (output/'frame-poses.json').write_text(json.dumps({'format':'zte-pose-frames-v2',
        'asset_id':settings.asset_id,'poses':frames_list,'fps':settings.fps,
        'strict_status':'NEEDS_REVIEW'},indent=2),encoding='utf-8')
    manifest={
        'asset_id':settings.asset_id,'generation_method':'deterministic_world_space_foot_lock_ik',
        'build':'pose-studio-autonomous-v2','config':asdict(settings),
        'status':'TECHNICAL_CANDIDATE' if q['technical_pass'] else 'TECHNICAL_REJECTED',
        'strict_status':'NEEDS_REVIEW','human_visual_review_required':True,
        'render_source':'single identity-locked vector renderer',
        'renderer_sha256':hashlib.sha256(html.read_bytes()).hexdigest(),
        'frames':settings.frames,'frame_size':[CANVAS,CANVAS],
        'atlas_columns':4,'atlas_rows':math.ceil(settings.frames/4),
        'pivot':{'x':ROOT_X,'y':GROUND+13},'qa':q,
        'limitations':['Vector demo skin, not AAA photorealistic texture',
                       'Numerical motion QA does not certify anatomy or visual quality',
                       'Pelvis and foot contact must be reviewed in real game playback',
                       'Foot-roll angles are stylistic and not certified by physics simulation',
                       'project.json stores eight editable keys; frame-poses.json is the exact full animation'],
    }
    (output/'qa-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
    (output/'REVIEW_REQUIRED.txt').write_text('AUTOMATED CANDIDATE ONLY. Strict DONE prohibited until real visual and semantic review.\n',encoding='utf-8')
    if bundle:
        with zipfile.ZipFile(output.parent/f'{settings.asset_id}-autonomous-pose-v2.zip','w',zipfile.ZIP_DEFLATED) as z:
            for path in sorted(output.rglob('*')):
                if path.is_file():z.write(path,path.relative_to(output))
    return manifest


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('build/character-tech-walk'))
    parser.add_argument('--studio',type=Path,default=Path(__file__).resolve().parent/'pose_studio.html')
    parser.add_argument('--asset-id',type=str,default='CHR-TECH-WALK')
    parser.add_argument('--frames',type=int,default=24)
    parser.add_argument('--fps',type=int,default=12)
    parser.add_argument('--stride',type=float,default=92.)
    parser.add_argument('--clearance',type=float,default=36.)
    parser.add_argument('--stance',type=float,default=.62)
    parser.add_argument('--palette',choices=('cyan','amber','lime'),default='cyan')
    args=parser.parse_args()
    settings=WalkSettings(asset_id=args.asset_id,frames=args.frames,fps=args.fps,stride=args.stride,clearance=args.clearance,stance_fraction=args.stance,palette=args.palette)
    manifest=export(args.output, settings, args.studio)
    qa=manifest['qa']
    print(json.dumps({'path':str(args.output),'status':manifest['status'],'technical_pass':qa['technical_pass'],
                      'seam_ratio':round(qa['seam_to_median_ratio'],4),'max_slip':round(qa['max_planted_world_slip_px_per_sample'],5),
                      'alpha_pass':qa['technical_alpha_pass']},indent=2))
    if not qa['technical_pass']:
        raise SystemExit('Technical QA failed; candidate stays rejected')


if __name__=='__main__':main()
