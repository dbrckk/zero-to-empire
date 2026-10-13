#!/usr/bin/env python3
"""Original role-consistent 2.5D character sprite atlases, authored in ChatGPT.

All art is generated locally, with one fixed vector rig and no network model calls.
The output is review-only and NEVER grants strict DONE. Frames: 256x256,
4-column RGBA atlas: 1024x1024, no ground shadow. Role IDLE can accompany
unresolved sibling actions as a continuity anchor without replacing strict DONE.
"""
from __future__ import annotations
import argparse, io, json, math, pathlib
from PIL import Image
import cairosvg

FRAME=256
ACTIONS={'IDLE':6,'WALK':8,'WORK':10,'CARRY':8,'REPAIR':10,'CELEB':8}
ROLES={
 'OP':{'helmet':'#ec832f','helmet_hi':'#ffbf69','jacket':'#344453','jacket_hi':'#586b78','seam':'#f3a452','pant':'#344354','hair':'#382e2a','skin':'#daaa80','eye':'#263446','accessory':'#e9a052'},
 'LOG':{'helmet':'#ebedf0','helmet_hi':'#ffffff','jacket':'#9c5d32','jacket_hi':'#e49e4f','seam':'#ffe1a1','pant':'#3b4959','hair':'#422a2d','skin':'#dca888','eye':'#283449','accessory':'#f1c66b'},
 'ENG':{'helmet':'#eef2f2','helmet_hi':'#ffffff','jacket':'#294859','jacket_hi':'#4b6b79','seam':'#56c0c9','pant':'#354a58','hair':'#443327','skin':'#d3a178','eye':'#273342','accessory':'#64cbda'},
}

# SVG drawn in painter's order: back arm and legs -> torso -> head -> front hands.
def svg_frame(role:str, action:str, index:int, count:int)->str:
 p=ROLES[role]; phase=2*math.pi*index/count; motion=math.sin(phase); bounce=0.0
 if action in ('WALK','CARRY'):
  stride=24*motion; bounce=3.5*(1-math.cos(phase*2))/2
 elif action=='IDLE':stride=0; bounce=1.8*math.sin(phase)
 else:stride=0;bounce=1.6*math.sin(phase)
 # Always keep same facial shape, helmet model, costume palette and 3/4 view.
 s=[]
 def add(v):s.append(v)
 def line(x1,y1,x2,y2,color,width,outline=3):
  return (f'<path d="M {x1:.1f} {y1:.1f} L {x2:.1f} {y2:.1f}" fill="none" stroke="#172533" stroke-width="{width+outline*2}" stroke-linecap="round"/>'
          f'<path d="M {x1:.1f} {y1:.1f} L {x2:.1f} {y2:.1f}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>')
 def hand(x,y):
  return f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="7.3" ry="8.3" fill="url(#skin)" stroke="#26313b" stroke-width="2.5"/><path d="M {x-4:.1f} {y-2:.1f} q 4 3 8 0" fill="none" stroke="#edc5a6" stroke-width="1.5"/>'
 def joint_arm(side, pose):
  # x shoulder, elbow, hand; design ergonomic positions for each action.
  shoulder=(95 if side=='L' else 154,106+bounce)
  if pose=='CELEB':
   lift=(1-math.cos(phase))/2
   handpos=((75-4*lift,140-109*lift+bounce) if side=='L' else (174+5*lift,140-109*lift+bounce))
   elbow=((76,126-53*lift+bounce) if side=='L' else (171,126-53*lift+bounce))
  elif pose=='CARRY':
   handpos=((89,132+bounce) if side=='L' else (166,132+bounce))
   elbow=((78,125+bounce) if side=='L' else (172,122+bounce))
  elif pose in ('WORK','REPAIR'):
   reach=math.sin(phase*2); pump=math.cos(phase*2)
   handpos=((80+3*reach,150-4*pump+bounce) if side=='L'
            else (174+22*reach,120+24*pump+bounce))
   elbow=((82,132+bounce) if side=='L'
          else (169+12*reach,108+12*pump+bounce))
  elif pose=='WALK':
   swing=motion*(-1 if side=='L' else 1)
   handpos=((84+8*swing,147+10*swing+bounce) if side=='L' else (170+8*swing,148-10*swing+bounce))
   elbow=((83+4*swing,124+5*swing+bounce) if side=='L' else (171+4*swing,127-5*swing+bounce))
  else:
   elbow=((81,129+bounce) if side=='L' else (170,126+bounce))
   handpos=((79,149+bounce) if side=='L' else (176,144+bounce))
  shoulder_x,shoulder_y=shoulder;ex,ey=elbow;hx,hy=handpos
  sleeve=line(shoulder_x,shoulder_y,ex,ey,'url(#jacket)',17,3)
  sleeve+=line(ex,ey,hx,hy,'url(#jacket)',14,3)
  # highlighted overarm and stitched safety cuff
  sleeve+=line(ex+(1 if side=='R' else -1)*2,ey,hx,hy,p['jacket_hi'],4,1)
  sleeve+=f'<circle cx="{ex}" cy="{ey}" r="3.5" fill="{p["seam"]}" opacity=".75"/>'
  return sleeve+hand(hx,hy)

 # legs behind torso: anti-phase step, readable ankle separation
 leg_poses=[]
 for side in ('L','R'):
  signed=(1 if side=='L' else -1)
  # Wider hip spacing and a damped ankle arc avoid the crossed ankles
  # seen in the original WALK/CARRY frames. Articulation remains readable
  # without stepping through the opposite shin.
  hipx=106 if side=='L' else 146
  swing=signed*stride
  yhip=155+bounce
  knee_x=hipx+0.45*swing + (2 if side=='L' else -2)
  # A gait has both position and velocity. A sinusoidal X position
  # alone repeats the same pose twice per loop (phase 45° and 135°).
  # Use the signed cosine for stance-vs-swing foot lift: eight real poses,
  # one grounded support foot per half-cycle and smooth loop closure.
  swing_velocity=signed*math.cos(phase) if action in ('WALK','CARRY') else 0
  knee_y=190+bounce-3*max(0,swing_velocity)
  ankle_x=hipx + swing*0.66
  lift=max(0,swing_velocity)*10 if action in ('WALK','CARRY') else 0
  ankle_y=226+bounce-lift
  leg_poses.append((side,hipx,yhip,knee_x,knee_y,ankle_x,ankle_y))
 add('<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">')
 add(f'''<defs>
 <linearGradient id="jacket" x1=".1" x2=".9" y1="0" y2="1"><stop offset="0" stop-color="{p['jacket_hi']}"/><stop offset=".43" stop-color="{p['jacket']}"/><stop offset="1" stop-color="#1b2c3a"/></linearGradient>
 <linearGradient id="helmet" x1="0" x2="1" y1="0" y2=".5"><stop offset="0" stop-color="{p['helmet_hi']}"/><stop offset=".5" stop-color="{p['helmet']}"/><stop offset="1" stop-color="#96633c"/></linearGradient>
 <linearGradient id="skin" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#ffe4bb"/><stop offset=".65" stop-color="{p['skin']}"/><stop offset="1" stop-color="#af745b"/></linearGradient>
 <linearGradient id="pant" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="{p['jacket_hi']}"/><stop offset=".5" stop-color="{p['pant']}"/><stop offset="1" stop-color="#1f3040"/></linearGradient>
 </defs>''')
 # no floor shadow; transparency is exact outside figure
 # back ponytail / hair only LOG
 if role=='LOG':
  add(f'<path d="M 151 {62+bounce:.1f} Q 184 {64+bounce:.1f} 172 {106+bounce:.1f} Q 161 {119+bounce:.1f} 152 {94+bounce:.1f}Z" fill="{p["hair"]}" stroke="#1b2330" stroke-width="3"/>')
 # boots and 2 articulated segments per leg
 for side,hipx,yhip,kx,ky,ax,ay in leg_poses:
  add(line(hipx,yhip,kx,ky,'url(#pant)',23,3));add(line(kx,ky,ax,ay,'url(#pant)',20,3))
  # knee armor pad and seam
  add(f'<ellipse cx="{kx:.1f}" cy="{ky:.1f}" rx="11" ry="8" fill="#647687" stroke="#253645" stroke-width="2" opacity=".85"/>')
  add(f'<path d="M {kx-7:.1f} {ky-2:.1f} l 12 0" stroke="{p["seam"]}" stroke-width="1.5" opacity=".65"/>')
  if side=='L': toe=ax-9
  else:toe=ax+9
  add(f'<path d="M {ax-10:.1f} {ay-8:.1f} Q {ax+11:.1f} {ay-11:.1f} {ax+13:.1f} {ay+2:.1f} L {toe+9:.1f} {ay+9:.1f} L {toe-12:.1f} {ay+7:.1f}Z" fill="#37434f" stroke="#1b2633" stroke-width="3"/>')
  add(f'<path d="M {toe-9:.1f} {ay+4:.1f} l 24 0" stroke="{p["seam"]}" stroke-width="2" opacity=".7"/>')
 # BACK arm
 add(joint_arm('L',action))
 # main torso, premium tapered silhouette, safety accents
 add(f'<path d="M 104 {93+bounce:.1f} Q 124 {85+bounce:.1f} 149 {93+bounce:.1f} L 164 {124+bounce:.1f} L 154 {157+bounce:.1f} Q 125 {170+bounce:.1f} 99 {158+bounce:.1f} L 88 {123+bounce:.1f}Z" fill="url(#jacket)" stroke="#172632" stroke-width="3.6"/>')
 add(f'<path d="M 109 {95+bounce:.1f} Q 124 {101+bounce:.1f} 140 {95+bounce:.1f} L 126 {115+bounce:.1f}Z" fill="#223344" stroke="{p["seam"]}" stroke-width="1.6"/>')
 add(f'<path d="M 123 {111+bounce:.1f} L 125 {155+bounce:.1f}" stroke="{p["seam"]}" stroke-width="2.6" opacity=".9"/>')
 add(f'<path d="M 92 {115+bounce:.1f} L 106 {120+bounce:.1f} M 151 {118+bounce:.1f} L 162 {116+bounce:.1f}" stroke="{p["seam"]}" stroke-width="4" opacity=".9"/>')
 # belt buckles and pockets
 add(f'<rect x="99" y="{153+bounce:.1f}" width="56" height="8" rx="3" fill="#1c2d3b" stroke="#8296a2" stroke-width="1.5"/>')
 add(f'<rect x="122" y="{152+bounce:.1f}" width="11" height="10" rx="2" fill="{p["accessory"]}" stroke="#2b3a46" stroke-width="2"/>')
 add(f'<path d="M 99 {133+bounce:.1f} l 14 0 l 0 11 l -14 -2 Z M 137 {133+bounce:.1f} l 13 -1 l 0 10 l -13 2 Z" fill="#3b5363" stroke="{p["seam"]}" stroke-width="1.4" opacity=".9"/>')
 # neck + head, same exact proportions across all actions
 add(f'<path d="M 119 {89+bounce:.1f} L 139 {88+bounce:.1f} L 142 {100+bounce:.1f} Q 125 {107+bounce:.1f} 116 {98+bounce:.1f}Z" fill="url(#skin)" stroke="#704e46" stroke-width="2"/>')
 add(f'<path d="M 103 {54+bounce:.1f} Q 113 {35+bounce:.1f} 135 {42+bounce:.1f} Q 157 {48+bounce:.1f} 155 {68+bounce:.1f} Q 155 {87+bounce:.1f} 136 {98+bounce:.1f} L 115 {94+bounce:.1f} Q 102 {82+bounce:.1f} 103 {54+bounce:.1f}Z" fill="url(#skin)" stroke="#26313b" stroke-width="3.3"/>')
 # ear, cheek and neck shading
 add(f'<ellipse cx="151" cy="{74+bounce:.1f}" rx="5" ry="9" fill="{p["skin"]}" stroke="#925a4d" stroke-width="2"/>')
 add(f'<path d="M 135 {83+bounce:.1f} q -10 6 -21 0" fill="none" stroke="#9a6257" stroke-width="2" opacity=".6"/>')
 if role=='OP':
  add(f'<path d="M 109 {66+bounce:.1f} h 39" stroke="#1c2e40" stroke-width="5" stroke-linecap="round"/>')
  add(f'<rect x="109" y="{68+bounce:.1f}" width="17" height="9" rx="3" fill="#1a3445" stroke="#7cbbc8" stroke-width="2"/><rect x="130" y="{68+bounce:.1f}" width="17" height="9" rx="3" fill="#1a3445" stroke="#7cbbc8" stroke-width="2"/>')
 else:
  # A blink must replace the open eyes, not paint a horizontal stroke over
  # still-visible pupils. This is an actual facial expression transition.
  if action=='IDLE' and index in (2,3):
   add(f'<path d="M 114 {71+bounce:.1f} q 6 3 12 0 M 135 {71+bounce:.1f} q 6 3 12 0" fill="none" stroke="{p["eye"]}" stroke-width="2.8" stroke-linecap="round"/>')
  else:
   add(f'<ellipse cx="120" cy="{71+bounce:.1f}" rx="2.5" ry="3" fill="{p["eye"]}"/><ellipse cx="141" cy="{71+bounce:.1f}" rx="2.5" ry="3" fill="{p["eye"]}"/>')
 add(f'<path d="M 127 {84+bounce:.1f} q 5 4 11 0" fill="none" stroke="#8e4e49" stroke-width="1.7" stroke-linecap="round"/>')
 # unique helmet per role (seams, raised ridge and front peak)
 add(f'<path d="M 101 {55+bounce:.1f} Q 100 {25+bounce:.1f} 121 {22+bounce:.1f} Q 153 {19+bounce:.1f} 157 {54+bounce:.1f}Z" fill="url(#helmet)" stroke="#202f3e" stroke-width="3"/>')
 add(f'<path d="M 121 {25+bounce:.1f} L 123 {49+bounce:.1f}" stroke="{p["helmet_hi"]}" stroke-width="4" opacity=".83"/>')
 add(f'<path d="M 100 {52+bounce:.1f} Q 132 {46+bounce:.1f} 165 {53+bounce:.1f} L 164 {60+bounce:.1f} Q 128 {57+bounce:.1f} 95 {62+bounce:.1f}Z" fill="{p["helmet"]}" stroke="#223340" stroke-width="2.8"/>')
 if role=='ENG':
  add(f'<path d="M 147 {33+bounce:.1f} l 5 17" stroke="#3bd3dc" stroke-width="5"/>')
 elif role=='LOG':
  add(f'<path d="M 139 {30+bounce:.1f} l 8 14" stroke="#d29b4e" stroke-width="3"/>')
 else:add(f'<path d="M 147 {32+bounce:.1f} l 6 16" stroke="#fdd18b" stroke-width="4"/>')
 # ACTION EQUIPMENT, and foreground hands actually touching it.
 if action=='CARRY':
  # crate rigid body: no frame-specific changing geometry; subtle 1px bob only
  by=121+bounce
  add(f'<path d="M 91 {by:.1f} L 164 {by:.1f} L 164 {by+47:.1f} L 91 {by+47:.1f}Z" fill="#9b7142" stroke="#2c333c" stroke-width="4"/>')
  add(f'<rect x="96" y="{by+4:.1f}" width="63" height="38" fill="#b98b50" stroke="#6e4d2f" stroke-width="1.6"/>')
  add(f'<path d="M 96 {by+7:.1f} L 156 {by+40:.1f} M 157 {by+7:.1f}L96 {by+40:.1f}" stroke="#704c31" stroke-width="4" opacity=".9"/>')
  add(f'<path d="M 109 {by:.1f} L 109 {by+47:.1f} M 147 {by:.1f} L 147 {by+47:.1f}" stroke="#dcb879" stroke-width="3"/>')
  # hands over handles, always same positions
  add(f'<rect x="82" y="{by+9:.1f}" width="16" height="11" rx="4" fill="{p["skin"]}" stroke="#23313e" stroke-width="2.2"/>')
  add(f'<rect x="158" y="{by+9:.1f}" width="16" height="11" rx="4" fill="{p["skin"]}" stroke="#23313e" stroke-width="2.2"/>')
 elif action in ('WORK','REPAIR'):
  tool_x=174+22*math.sin(phase*2)
  tool_y=120+24*math.cos(phase*2)+bounce
  add(f'<g transform="translate({tool_x:.1f},{tool_y:.1f}) rotate({-6+4*math.sin(phase):.1f})">')
  if action=='WORK':
   add('<rect x="-12" y="-8" width="31" height="16" rx="5" fill="#40525d" stroke="#172633" stroke-width="2.6"/><rect x="11" y="-4" width="20" height="8" rx="2" fill="#7b9e9b" stroke="#273746" stroke-width="2"/><circle cx="-5" cy="0" r="4" fill="#64cbd0"/>')
  else:
   add('<path d="M -8 9 L 14 -11 L 20 -9 L 17 -2 L 11 -3 L -2 13Z" fill="#869ba7" stroke="#263442" stroke-width="2.6"/><circle cx="-8" cy="12" r="4" fill="#263847"/><path d="M 16 -13l12 -8" stroke="#d2aa69" stroke-width="4" stroke-linecap="round"/>')
  add('</g>')
 # foreground right arm and hand over equipment, never floating
 add(joint_arm('R',action))
 if action=='CELEB':
  # Both arms raised over ~half a cycle; no detached particle VFX.
  add(f'<path d="M 108 {95+bounce:.1f} Q 126 {93+bounce:.1f} 143 {97+bounce:.1f}" stroke="{p["seam"]}" stroke-width="3" opacity=".7"/>')
 # reflective micro-detail texture, unique per role but invariant per frame
 add(f'<path d="M 111 {111+bounce:.1f} l 7 4 M 139 {112+bounce:.1f} l 8 -4" stroke="#b8d7db" stroke-width="1.7" opacity=".7"/>')
 add('</svg>')
 return '\n'.join(s)


def render_atlas(role,action,outdir,save_svgs=False):
 count=ACTIONS[action]; atlas=Image.new('RGBA',(1024,1024),(0,0,0,0))
 for i in range(count):
  svg=svg_frame(role,action,i,count)
  png=cairosvg.svg2png(bytestring=svg.encode('utf8'),output_width=768,output_height=768)
  rgba=Image.open(io.BytesIO(png)).convert('RGBA').resize((FRAME,FRAME),Image.Resampling.LANCZOS)
  x=(i%4)*FRAME;y=(i//4)*FRAME;atlas.alpha_composite(rgba,(x,y))
  if save_svgs:
   src=outdir/'src_svg'/role/action;src.mkdir(parents=True,exist_ok=True)
   (src/f'{i:02d}.svg').write_text(svg,encoding='utf8')
 name=f'zte_chr_{role.lower()}_{action.lower()}_final.png'
 path=outdir/'candidates'/name;path.parent.mkdir(parents=True,exist_ok=True);atlas.save(path,optimize=True)
 return dict(id=f'CHR-{role}-{action}',file=name,frames=count,role=role,action=action,context_only=(action=='IDLE' and role in ('OP','LOG')),strict_approved=False)

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--output-dir',default='art/incoming/chatgpt-original')
 parser.add_argument('--save-svg',action='store_true')
 args=parser.parse_args();outdir=pathlib.Path(args.output_dir);outdir.mkdir(parents=True,exist_ok=True)
 results=[]
 for role in ROLES:
  for action in ACTIONS:
   results.append(render_atlas(role,action,outdir,args.save_svg))
 report={'version':'chatgpt-original-character-rig-v1','strict_done_added':0,'review_only':True,
         'asset_count':len(results),'unresolved_target_count':16,'assets':results}
 (outdir/'creation-manifest.json').write_text(json.dumps(report,indent=2)+'\n')
 print(f'CHATGPT_CHARACTER_ATLASES_CREATED={len(results)} ASSETS_UNRESOLVED=16 STRICT_DONE_ADDED=0')

if __name__=='__main__':main()
