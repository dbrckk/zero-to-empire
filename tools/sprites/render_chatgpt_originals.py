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
from local_character_material_finish import finish_frame
from local_character_action_fx import action_fx,tool_angle,TOOL_TIP_OFFSETS
from local_character_contact_gait import foot_pose,torso_weight_shift

FRAME=256
ACTIONS={'IDLE':6,'WALK':8,'WORK':10,'CARRY':8,'REPAIR':10,'CELEB':8}
ROLES={
 'OP':{'helmet':'#ec832f','helmet_hi':'#ffbf69','jacket':'#344453','jacket_hi':'#586b78','seam':'#f3a452','pant':'#344354','hair':'#382e2a','skin':'#daaa80','eye':'#263446','accessory':'#e9a052'},
 'LOG':{'helmet':'#ebedf0','helmet_hi':'#ffffff','jacket':'#9c5d32','jacket_hi':'#e49e4f','seam':'#ffe1a1','pant':'#3b4959','hair':'#422a2d','skin':'#dca888','eye':'#283449','accessory':'#f1c66b'},
 'ENG':{'helmet':'#eef2f2','helmet_hi':'#ffffff','jacket':'#294859','jacket_hi':'#4b6b79','seam':'#56c0c9','pant':'#354a58','hair':'#443327','skin':'#d3a178','eye':'#273342','accessory':'#64cbda'},
}

# A physical repair socket is fixed in world/frame space, rather than glued to
# the wrist. Invert the same rigid endpoint transform used by action_fx so the
# engineered tool contacts the actual bolt throughout its ratcheting cycle.
ENG_REPAIR_TARGET=(218.0,129.0)

def engineer_repair_wrist(phase:float)->tuple[float,float]:
 dx,dy=TOOL_TIP_OFFSETS['REPAIR']['ENG']
 theta=math.radians(tool_angle('REPAIR',phase,role='ENG'))
 rotated_x=dx*math.cos(theta)-dy*math.sin(theta)
 rotated_y=dx*math.sin(theta)+dy*math.cos(theta)
 return (ENG_REPAIR_TARGET[0]-rotated_x,
         ENG_REPAIR_TARGET[1]-rotated_y)


def engineer_work_wrist(phase:float,bounce:float)->tuple[float,float]:
 # Separate wide diagnostic scan sweep. The held tablet, right hand and
 # illuminated sensor share exactly one trajectory, not three approximations.
 return (176+23.0*math.sin(phase),123+15.0*math.cos(phase)+bounce)


# SVG drawn in painter's order: back arm and legs -> torso -> head -> front hands.
def svg_frame(role:str, action:str, index:int, count:int)->str:
 p=ROLES[role]; phase=2*math.pi*index/count; motion=math.sin(phase); bounce=0.0
 if action in ('WALK','CARRY'):
  bounce=2.8*(1-math.cos(phase*2))/2
 elif action=='IDLE':bounce=1.8*math.sin(phase)
 elif role=='ENG' and action=='WORK':
  bounce=3.6*math.sin(phase)
 elif role=='ENG' and action=='REPAIR':
  # Torque transfers through the knees and shoulders while BOTH boots stay
  # planted. The socket/tool remain locked to world space, not to this bob.
  bounce=5.1*math.sin(phase)
 else:bounce=1.6*math.sin(phase)
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
   # One slow, physically connected tool cycle. Earlier 22px reach/24px
   # vertical pumping made the tool look like it floated and clipped the face.
   reach=math.sin(phase); pump=math.cos(phase)
   # WORK: broad horizontal fabrication stroke. REPAIR: compact diagonal
   # inspection/twist. Both use exactly the same wrist coordinates as the
   # physical tool and attached light below; no disconnected props.
   reach_px=15 if pose=='WORK' else 8
   pump_px=12 if pose=='WORK' else 7
   handpos=((80+2*reach,146-3*pump+bounce) if side=='L'
            else (176+reach_px*reach,123+pump_px*pump+bounce))
   elbow=((82,132+bounce) if side=='L'
          else (168+reach_px*.47*reach,115+pump_px*.58*pump+bounce))
   if role=='ENG' and pose=='WORK' and side=='R':
    handpos=engineer_work_wrist(phase,bounce)
    elbow=(165+11*math.sin(phase-.18),115+7*math.cos(phase-.18)+.30*bounce)
   if role=='ENG' and pose=='REPAIR' and side=='R':
    handpos=engineer_repair_wrist(phase)
    # Braced elbow drives the ratchet against a world-fixed socket instead
    # of letting the entire character remain static during the torque cycle.
    elbow=(167+9.5*math.sin(phase-.35),
           115+8.5*math.cos(phase-.35)+.30*bounce)
  elif pose=='WALK':
   swing=motion*(-1 if side=='L' else 1)
   if role=='ENG':
    # A visibly reciprocal arm drive balances the stronger planted-foot
    # engineer gait; it remains distinct from tool/carry arm poses.
    opposite=math.cos(phase+.45)
    handpos=((84-12*opposite,147+14*opposite+bounce) if side=='L'
             else (170+12*opposite,148-14*opposite+bounce))
    elbow=((83-6*opposite,124+7*opposite+bounce) if side=='L'
           else (171+6*opposite,127-7*opposite+bounce))
   elif role=='OP':
    # Reciprocal opposing arm motion: front arm rises as opposite boot leads.
    # Earlier both wrists bobbed in the same vertical direction.
    opposite=math.cos(phase)
    handpos=((84-10*opposite,147+11*opposite+bounce) if side=='L'
             else (170+10*opposite,148-11*opposite+bounce))
    elbow=((83-5*opposite,124+5*opposite+bounce) if side=='L'
           else (171+5*opposite,127-5*opposite+bounce))
   else:
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

 # Locally authored planted-foot gait: 60% support, 40% lifted
 # recovery, damped 3/4-view two-bone knees, and reciprocal L/R steps.
 # Grounded ankles keep exactly the same Y even as pelvis bob changes.
 leg_poses=[]
 for side in ('L','R'):
  if action in ('WALK','CARRY'):
   leg=foot_pose(phase,side,action,bounce,profile=('op-walk' if role=='OP' and action=='WALK' else
                                'eng-walk' if role=='ENG' and action=='WALK' else 'standard'))
   hipx,yhip=leg.hip_x,leg.hip_y
   knee_x,knee_y=leg.knee_x,leg.knee_y
   ankle_x,ankle_y=leg.ankle_x,leg.ankle_y
   boot_angle=leg.boot_angle
  else:
   hipx=106 if side=='L' else 146
   yhip=155+bounce
   knee_x=hipx+(2 if side=='L' else -2)
   knee_y=190+(.48*bounce if role=='ENG' and action in ('WORK','REPAIR') else bounce)
   ankle_x=hipx
   ankle_y=(226 if role=='ENG' and action in ('WORK','REPAIR') else 226+bounce)
   boot_angle=0.0
  leg_poses.append((side,hipx,yhip,knee_x,knee_y,ankle_x,ankle_y,boot_angle))
 add('<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">')
 add(f'''<defs>
 <linearGradient id="jacket" x1=".1" x2=".9" y1="0" y2="1"><stop offset="0" stop-color="{p['jacket_hi']}"/><stop offset=".43" stop-color="{p['jacket']}"/><stop offset="1" stop-color="#1b2c3a"/></linearGradient>
 <linearGradient id="helmet" x1="0" x2="1" y1="0" y2=".5"><stop offset="0" stop-color="{p['helmet_hi']}"/><stop offset=".5" stop-color="{p['helmet']}"/><stop offset="1" stop-color="#96633c"/></linearGradient>
 <linearGradient id="skin" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#ffe4bb"/><stop offset=".65" stop-color="{p['skin']}"/><stop offset="1" stop-color="#af745b"/></linearGradient>
 <linearGradient id="pant" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="{p['jacket_hi']}"/><stop offset=".5" stop-color="{p['pant']}"/><stop offset="1" stop-color="#1f3040"/></linearGradient>
 <linearGradient id="reinforced" x1="0" x2=".95" y1="0" y2="1">
  <stop offset="0" stop-color="#81949e"/><stop offset=".20" stop-color="#475b6b"/>
  <stop offset=".68" stop-color="#263b49"/><stop offset="1" stop-color="#172834"/>
 </linearGradient>
 <linearGradient id="metalEdge" x1="0" x2="1" y1="0" y2="0">
  <stop offset="0" stop-color="#263946"/><stop offset=".33" stop-color="#a9bac0"/>
  <stop offset=".51" stop-color="#566b78"/><stop offset=".90" stop-color="#1f3542"/>
 </linearGradient>
 <pattern id="workwearWeave" width="6" height="6" patternUnits="userSpaceOnUse">
  <path d="M 0 6 L 6 0 M -1 2 L 2 -1" fill="none" stroke="#d4e1e2" stroke-opacity=".105" stroke-width=".6"/>
 </pattern>
 </defs>''')
 # no floor shadow; transparency is exact outside figure
 # back ponytail / hair only LOG
 if role=='LOG':
  add(f'<path d="M 151 {62+bounce:.1f} Q 184 {64+bounce:.1f} 172 {106+bounce:.1f} Q 161 {119+bounce:.1f} 152 {94+bounce:.1f}Z" fill="{p["hair"]}" stroke="#1b2330" stroke-width="3"/>')
 # Engineer-only free-standing diagnostics column. It has a fixed ground
 # support, a real repairable fastener, and stays independent of torso bounce.
 # The wrist/tool/VFX endpoint locks to the highlighted fastener below.
 if role=='ENG' and action=='REPAIR':
  tx,ty=ENG_REPAIR_TARGET
  add('<g data-repair-station="ENG" data-fixed-socket="true">')
  add('<path d="M 220 149 L 238 146 L 240 226 L 219 226Z" fill="#253e4b" stroke="#152a38" stroke-width="3"/>')
  add('<path d="M 223 163 L 234 163 L 235 220 L 221 220Z" fill="#395969" stroke="#6e929e" stroke-width="1.4"/>')
  add('<path d="M 216 224 L 241 224 L 241 233 L 212 233Z" fill="#334957" stroke="#142936" stroke-width="2.5"/>')
  add('<path d="M 208 111 L 232 109 L 240 118 L 239 154 L 213 158 L 205 148Z" fill="#304c5b" stroke="#122b39" stroke-width="3"/>')
  add('<path d="M 212 116 L 230 115 L 234 122 L 232 149 L 214 151 L 210 143Z" fill="#456777" stroke="#91b5be" stroke-width="1.3"/>')
  add('<path d="M 214 144 H 232" stroke="#173745" stroke-width="3"/>')
  # Readable bolted service hatch and warning strip at phone scale.
  add('<path d="M 222 168 h 11 v 33 h -11 Z" fill="#2b4958" stroke="#7394a0" stroke-width="1.8"/>')
  add('<path d="M 223 177 l 9 -7 M 223 187 l 9 -7 M 223 197 l 9 -7" stroke="#e4b66d" stroke-width="2.8"/>')
  for xx,yy in ((216,115),(234,148)):
   add(f'<circle cx="{xx}" cy="{yy}" r="2.5" fill="#a5bec5" stroke="#142b38" stroke-width="1.3"/>')
  add('<rect x="214" y="118" width="6" height="3" rx="1" fill="#75dce2"/>')
  add('<rect x="222" y="118" width="7" height="3" rx="1" fill="#ecb76e"/>')
  add(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="6.7" fill="#142d3b" stroke="#d6b879" stroke-width="2.5"/>')
  add(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="3.5" fill="#648b99" stroke="#253d49" stroke-width="1.5"/>')
  add(f'<path d="M {tx-2:.1f} {ty:.1f} h 4 M {tx:.1f} {ty-2:.1f} v 4" stroke="#d1e8e8" stroke-width="1.2"/>')
  add('</g>')
 # boots and 2 articulated segments per leg
 for side,hipx,yhip,kx,ky,ax,ay,boot_angle in leg_poses:
  if role in ('OP','ENG') and action=='WALK':
   # Real editable ankle/boot contact telemetry; no automatic art approval.
   gait_profile='op-walk' if role=='OP' else 'eng-walk'
   gait_attr='data-op-walk-foot' if role=='OP' else 'data-eng-walk-foot'
   foot=foot_pose(phase,side,action,bounce,profile=gait_profile)
   add(f'<g {gait_attr}="{side}" data-planted="{str(foot.planted).lower()}" data-ankle-x="{ax:.2f}" data-ankle-y="{ay:.2f}">')
  if role=='ENG' and action=='REPAIR':
   add(f'<g data-eng-repair-foot="{side}" data-ankle-y="{ay:.2f}">')
  if role=='ENG' and action=='WORK':
   add(f'<g data-eng-work-foot="{side}" data-ankle-y="{ay:.2f}">')
  add(line(hipx,yhip,kx,ky,'url(#pant)',23,3));add(line(kx,ky,ax,ay,'url(#pant)',20,3))
  # knee armor pad and seam
  add(f'<ellipse cx="{kx:.1f}" cy="{ky:.1f}" rx="11" ry="8" fill="#647687" stroke="#253645" stroke-width="2" opacity=".85"/>')
  add(f'<path d="M {kx-7:.1f} {ky-2:.1f} l 12 0" stroke="{p["seam"]}" stroke-width="1.5" opacity=".65"/>')
  add(f'<path d="M {kx-9:.1f} {ky+3:.1f} l 17 0" stroke="#b7cbd0" stroke-width="1.7" opacity=".7"/>')
  add(f'<circle cx="{kx-7:.1f}" cy="{ky-3:.1f}" r="1.6" fill="{p["accessory"]}"/><circle cx="{kx+7:.1f}" cy="{ky-3:.1f}" r="1.6" fill="{p["accessory"]}"/>')
  if side=='L': toe=ax-9
  else:toe=ax+9
  # Heel-strike and toe-off flex the same boot art around its ankle.
  add(f'<g transform="rotate({boot_angle:.2f} {ax:.2f} {ay:.2f})">')
  add(f'<path d="M {ax-10:.1f} {ay-8:.1f} Q {ax+11:.1f} {ay-11:.1f} {ax+13:.1f} {ay+2:.1f} L {toe+9:.1f} {ay+9:.1f} L {toe-12:.1f} {ay+7:.1f}Z" fill="#37434f" stroke="#1b2633" stroke-width="3"/>')
  add(f'<path d="M {toe-9:.1f} {ay+4:.1f} l 24 0" stroke="{p["seam"]}" stroke-width="2" opacity=".7"/>')
  add(f'<path d="M {toe-11:.1f} {ay+7:.1f} q 12 3 26 0" stroke="#16232d" stroke-width="3.8" fill="none"/>')
  add(f'<path d="M {toe-5:.1f} {ay-1:.1f} l 12 -2" stroke="#9cb2bd" stroke-width="1.9" opacity=".7"/>')
  add('</g>')
  if role in ('OP','ENG') and action=='WALK':
   add('</g>')  # close the per-leg pose-evidence group
  if role=='ENG' and action=='REPAIR':
   add('</g>')  # close world-planted repair boot evidence group
  if role=='ENG' and action=='WORK':
   add('</g>')  # close world-planted diagnostic work boots
 # Weight shifts toward stance foot; cargo carry sway remains restrained.
 # The hands, equipment, torso, helmet and face all receive the exact same
 # transform, avoiding drift in object contact or character identity.
 repair_body_evidence=(f' data-eng-repair-body-bounce="{bounce:.2f}"'
                       if role=='ENG' and action=='REPAIR' else '')
 add(f'<g{repair_body_evidence} transform="translate({torso_weight_shift(phase,action):.2f},0)">')
 # BACK arm
 add(joint_arm('L',action))
 # main torso, premium tapered silhouette, safety accents
 add(f'<path d="M 104 {93+bounce:.1f} Q 124 {85+bounce:.1f} 149 {93+bounce:.1f} L 164 {124+bounce:.1f} L 154 {157+bounce:.1f} Q 125 {170+bounce:.1f} 99 {158+bounce:.1f} L 88 {123+bounce:.1f}Z" fill="url(#jacket)" stroke="#172632" stroke-width="3.6"/>')
 # Original workwear material pass: cropped shoulder armor, woven fabric,
 # laminated vest segments and two retention fasteners. All follow the same
 # torso/bounce transform and remain invariant across the six actions.
 add(f'<path d="M 104 {93+bounce:.1f} Q 124 {85+bounce:.1f} 149 {93+bounce:.1f} L 164 {124+bounce:.1f} L 154 {157+bounce:.1f} Q 125 {170+bounce:.1f} 99 {158+bounce:.1f} L 88 {123+bounce:.1f}Z" fill="url(#workwearWeave)" opacity=".74"/>')
 for side in ('L','R'):
  dx=0 if side=='L' else 59
  add(f'<path d="M {89+dx} {106+bounce:.1f} L {99+dx} {96+bounce:.1f} Q {107+dx} {95+bounce:.1f} {116+dx} {105+bounce:.1f} L {112+dx} {118+bounce:.1f} Q {100+dx} {119+bounce:.1f} {89+dx} {115+bounce:.1f}Z" fill="url(#reinforced)" stroke="#1b303c" stroke-width="2.7"/>')
  add(f'<path d="M {94+dx} {105+bounce:.1f} q 7 -5 14 0" stroke="#b8ccd2" stroke-width="2.2" stroke-opacity=".72" fill="none"/>')
  add(f'<circle cx="{102+dx}" cy="{113+bounce:.1f}" r="2.3" fill="{p["accessory"]}" stroke="#213645" stroke-width="1.1"/>')
 # A subtle chest-harness fits inside the jacket; it is neither a text logo
 # nor a detached floating decoration and stays attached while the arms move.
 add(f'<path d="M 111 {103+bounce:.1f} L 119 {119+bounce:.1f} L 117 {150+bounce:.1f} M 144 {103+bounce:.1f} L 135 {119+bounce:.1f} L 136 {150+bounce:.1f}" stroke="#162c3a" stroke-width="7" opacity=".78" fill="none"/>')
 add(f'<path d="M 111 {103+bounce:.1f} L 119 {119+bounce:.1f} L 117 {148+bounce:.1f} M 144 {103+bounce:.1f} L 135 {119+bounce:.1f} L 136 {148+bounce:.1f}" stroke="{p["seam"]}" stroke-width="2.2" opacity=".9" fill="none"/>')
 add(f'<rect x="120" y="{125+bounce:.1f}" width="15" height="13" rx="2.5" fill="#233847" stroke="url(#metalEdge)" stroke-width="2"/>')
 add(f'<path d="M 124 {128+bounce:.1f} h 6 m -3 -3 v 7" stroke="{p["accessory"]}" stroke-width="1.5" opacity=".9"/>')
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
  # OP goggles conceal the eyelids, so an IDLE blink is expressed by a
  # brief lens reflection shift, never by a floating eye outside the visor.
  # Lens geometry remains identical across all other action families.
  lens_shift=(1.5 if action=='IDLE' and index in (2,3) else 0.0)
  add(f'<path d="M {112+lens_shift:.1f} {70+bounce:.1f} l 5 0 M {133+lens_shift:.1f} {70+bounce:.1f} l 5 0" stroke="#c7eff1" stroke-width="1.5" opacity=".76"/>')
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
 add(f'<path d="M 110 {37+bounce:.1f} Q 114 {28+bounce:.1f} 120 {27+bounce:.1f}" stroke="#fff4d6" stroke-width="2.2" opacity=".63" fill="none"/>')
 add(f'<path d="M 145 {31+bounce:.1f} q 8 8 7 19" stroke="#1a3040" stroke-width="2.3" opacity=".45" fill="none"/>')
 for xx in (106,155):
  add(f'<circle cx="{xx}" cy="{55+bounce:.1f}" r="2.4" fill="#304353" stroke="{p["accessory"]}" stroke-width="1.2"/>')
 add(f'<path d="M 100 {52+bounce:.1f} Q 132 {46+bounce:.1f} 165 {53+bounce:.1f} L 164 {60+bounce:.1f} Q 128 {57+bounce:.1f} 95 {62+bounce:.1f}Z" fill="{p["helmet"]}" stroke="#223340" stroke-width="2.8"/>')
 if role=='ENG':
  add(f'<path d="M 147 {33+bounce:.1f} l 5 17" stroke="#3bd3dc" stroke-width="5"/>')
 elif role=='LOG':
  add(f'<path d="M 139 {30+bounce:.1f} l 8 14" stroke="#d29b4e" stroke-width="3"/>')
 else:add(f'<path d="M 147 {32+bounce:.1f} l 6 16" stroke="#fdd18b" stroke-width="4"/>')
 # ACTION EQUIPMENT. All objects are authored here as editable SVG
 # geometry, with invariant shape within each animation and hand contact.
 if action=='CARRY':
  by=121+bounce
  if role=='OP':
   # A bolted cast-metal ore bin (not a generic cardboard package).
   add(f'<path d="M 90 {by:.1f} L 166 {by:.1f} L 163 {by+47:.1f} L 94 {by+47:.1f}Z" fill="#50616b" stroke="#182b38" stroke-width="3.5"/>')
   add(f'<path d="M 96 {by+5:.1f} L 159 {by+5:.1f} L 157 {by+42:.1f} L 98 {by+42:.1f}Z" fill="#748995" stroke="#243743" stroke-width="2"/>')
   add(f'<path d="M 98 {by+10:.1f} L 154 {by+37:.1f} M 153 {by+10:.1f} L 99 {by+37:.1f}" stroke="#304956" stroke-width="5"/>')
   for xx in (100,154):
    for yy in (by+9,by+38):
     add(f'<circle cx="{xx}" cy="{yy:.1f}" r="2.6" fill="#e6b365" stroke="#263a46" stroke-width="1"/>')
   add(f'<rect x="111" y="{by+2:.1f}" width="34" height="5" rx="2" fill="#e5b46f"/>')
  elif role=='LOG':
   # Warehouse parcel with tape and readable strapped corners.
   add(f'<path d="M 91 {by:.1f} L 164 {by:.1f} L 164 {by+47:.1f} L 91 {by+47:.1f}Z" fill="#a87542" stroke="#332e33" stroke-width="3.5"/>')
   add(f'<rect x="96" y="{by+4:.1f}" width="63" height="38" rx="2" fill="#ce985f" stroke="#754827" stroke-width="1.8"/>')
   add(f'<path d="M 96 {by+7:.1f} L 156 {by+40:.1f} M 157 {by+7:.1f} L 96 {by+40:.1f}" stroke="#80502e" stroke-width="3.5"/>')
   add(f'<rect x="120" y="{by+4:.1f}" width="12" height="38" fill="#ebca8c" opacity=".85"/>')
   add(f'<path d="M 104 {by+13:.1f} h 13 M 104 {by+17:.1f} h 12 M 104 {by+21:.1f} h 10" stroke="#725137" stroke-width="1.6"/>')
  else:
   # Engineer's sealed field-instrument case, cyan latch lights.
   add(f'<rect x="91" y="{by:.1f}" width="74" height="47" rx="7" fill="#314d5d" stroke="#172d3b" stroke-width="4"/>')
   add(f'<rect x="97" y="{by+5:.1f}" width="62" height="37" rx="4" fill="#466a7a" stroke="#668e9d" stroke-width="2"/>')
   add(f'<path d="M 106 {by+8:.1f} v 29 M 150 {by+8:.1f} v 29" stroke="#254555" stroke-width="5"/>')
   add(f'<rect x="119" y="{by+5:.1f}" width="18" height="10" rx="3" fill="#72cdd3" stroke="#163e4b" stroke-width="1.5"/>')
   add(f'<circle cx="124" cy="{by+32:.1f}" r="3" fill="#9deff0"/><circle cx="136" cy="{by+32:.1f}" r="3" fill="#80bec9"/>')
  # Two hand grips overlap the left/right handle in every phase.
  for hx in (90,164):
   add(f'<rect x="{hx-7}" y="{by+8:.1f}" width="14" height="13" rx="5" fill="{p["skin"]}" stroke="#23313e" stroke-width="2.2"/>')
   add(f'<path d="M {hx-4} {by+10:.1f} v 6" stroke="#f9d5b4" stroke-width="1.5"/>')
 elif action in ('WORK','REPAIR'):
  # The exact same right-hand joint drives the held equipment. One cycle
  # and stable local geometry prevent fake floating tools and prop morphing.
  tool_x=176+(15 if action=='WORK' else 8)*math.sin(phase)
  tool_y=123+(12 if action=='WORK' else 7)*math.cos(phase)+bounce
  if role=='ENG' and action=='REPAIR':
   tool_x,tool_y=engineer_repair_wrist(phase)
  elif role=='ENG' and action=='WORK':
   tool_x,tool_y=engineer_work_wrist(phase,bounce)
  repair_marker=' data-repair-tool="ENG"' if role=='ENG' and action=='REPAIR' else ''
  work_marker=' data-work-tool="ENG"' if role=='ENG' and action=='WORK' else ''
  add(f'<g{repair_marker}{work_marker} transform="translate({tool_x:.1f},{tool_y:.1f}) rotate({tool_angle(action,phase,role=role):.1f})">')
  if action=='WORK':
   if role=='OP':
    add('<rect x="-12" y="-9" width="37" height="19" rx="5" fill="#435964" stroke="#182c3b" stroke-width="3"/>')
    add('<path d="M 16 -6 L 35 -5 L 35 4 L 16 5Z" fill="#7babb5" stroke="#263d4b" stroke-width="2"/>')
    add('<path d="M -2 10 V 20 M 3 10 V 19" stroke="#344654" stroke-width="4" stroke-linecap="round"/>')
    add('<circle cx="-2" cy="-1" r="4" fill="#f0b35d"/><path d="M 25 -3 h 10" stroke="#b9dce1" stroke-width="1.6"/>')
   elif role=='LOG':
    add('<path d="M -11 -9 h 31 l 5 7 l -5 11 h -31 Z" fill="#3c505d" stroke="#1a303d" stroke-width="3"/>')
    add('<rect x="13" y="-5" width="13" height="11" rx="2" fill="#ae2636" stroke="#f8aa9d" stroke-width="1.5"/>')
    add('<rect x="-3" y="7" width="8" height="14" rx="2" fill="#314353"/>')
    add('<path d="M 25 0 h 12" stroke="#f2aa7d" stroke-width="2.5" opacity=".8"/>')
   else:
    add('<rect x="-12" y="-12" width="45" height="30" rx="4" fill="#1d3545" stroke="#71d1d7" stroke-width="2.6"/>')
    add('<rect x="-7" y="-7" width="35" height="19" rx="2" fill="#294e61" stroke="#8ce1e2" stroke-width="1"/>')
    add('<path d="M -1 4 l 6 -8 l 7 5 l 5 -7" fill="none" stroke="#7de7e8" stroke-width="2"/>')
    add('<circle cx="26" cy="14" r="2" fill="#f9bc6b"/>')
  else:
   if role=='OP':
    add('<path d="M -10 8 L 12 -14 L 19 -13 L 16 -6 L 10 -7 L -2 13Z" fill="#8aa0a9" stroke="#253b48" stroke-width="2.8"/>')
    add('<circle cx="-7" cy="11" r="3.5" fill="#e4a45b"/><path d="M 16 -13 L 25 -19" stroke="#e0be82" stroke-width="3"/>')
   elif role=='LOG':
    add('<rect x="-11" y="-7" width="30" height="14" rx="5" fill="#4c6071" stroke="#253949" stroke-width="2.5"/>')
    add('<path d="M 17 -3 l 21 -14 l 3 5 l -20 17" fill="#a7b6bd" stroke="#26394a" stroke-width="2"/>')
    add('<circle cx="-4" cy="0" r="3.5" fill="#f0bb69"/>')
   else:
    # Physical articulated torque wrench, not an electronic scanner.
    # Tip geometry is centred on the *exact* fixed socket offset (43,-13).
    add('<path d="M -12 -9 L 10 -10 L 27 -12 L 39 -16 L 44 -16 L 44 -10 L 28 -4 L 11 9 L -12 9 Z" fill="url(#metalEdge)" stroke="#172b38" stroke-width="3"/>')
    add('<path d="M -12 -7 L 10 -8 L 12 7 L -12 7 Z" fill="#294b5b" stroke="#7cd4dc" stroke-width="2"/>')
    add('<path d="M -9 -4 h 3 M -2 -4 h 3 M 5 -4 h 3 M -9 3 h 3 M -2 3 h 3 M 5 3 h 3" stroke="#9fe6e7" stroke-width="1.6"/>')
    add('<path d="M 11 -3 L 31 -7" stroke="#d3e0df" stroke-width="2.8" stroke-linecap="round"/>')
    add('<path d="M 36 -17 L 42 -20 L 48 -16 L 43 -13 L 46 -9 L 39 -6" fill="none" stroke="#e3d09d" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>')
    add('<circle cx="19" cy="-4" r="2" fill="#eac479"/>')
  add('</g>')
 # foreground right arm and hand over equipment, never floating
 add(joint_arm('R',action))
 # Physically attached local vector action lighting. Equipment highlights are
 # driven by the very same right-wrist tool transform as the authored prop.
 # No detached generated particles or external model are introduced.
 # The rigid light must use the same wrist coordinates as the actual tool.
 fx_tool_x=176+(15 if action=='WORK' else 8)*math.sin(phase)
 fx_tool_y=123+(12 if action=='WORK' else 7)*math.cos(phase)+bounce
 if role=='ENG' and action=='REPAIR':
  fx_tool_x,fx_tool_y=engineer_repair_wrist(phase)
 elif role=='ENG' and action=='WORK':
  fx_tool_x,fx_tool_y=engineer_work_wrist(phase,bounce)
 add(action_fx(role,action,phase,
               tool_x=fx_tool_x,tool_y=fx_tool_y,
               bounce=bounce))
 if action=='CELEB':
  # Both arms raised over ~half a cycle; no detached particle VFX.
  add(f'<path d="M 108 {95+bounce:.1f} Q 126 {93+bounce:.1f} 143 {97+bounce:.1f}" stroke="{p["seam"]}" stroke-width="3" opacity=".7"/>')
 # reflective micro-detail texture, unique per role but invariant per frame
 add(f'<path d="M 111 {111+bounce:.1f} l 7 4 M 139 {112+bounce:.1f} l 8 -4" stroke="#b8d7db" stroke-width="1.7" opacity=".7"/>')
 add('</g>')  # balanced upper-body weight-transfer group
 add('</svg>')
 return '\n'.join(s)


def render_atlas(role,action,outdir,save_svgs=False):
 # Pure SVG pose/unit tests need no Cairo dependency; only pixel rendering does.
 import cairosvg
 count=ACTIONS[action]; atlas=Image.new('RGBA',(1024,1024),(0,0,0,0))
 for i in range(count):
  svg=svg_frame(role,action,i,count)
  png=cairosvg.svg2png(bytestring=svg.encode('utf8'),output_width=768,output_height=768)
  rgba=Image.open(io.BytesIO(png)).convert('RGBA').resize((FRAME,FRAME),Image.Resampling.LANCZOS)
  # Final material illumination is deterministic and preserves exact alpha;
  # editable SVG geometry remains the authoritative rig/source for all frames.
  rgba=finish_frame(rgba)
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
 report={'version':'chatgpt-original-character-rig-v13-engineer-diagnostic-sweep','strict_done_added':0,'review_only':True,
         'material_finish':'local-alpha-safe-directional-light-v1',
         'action_vfx':'local-rigid-tool-tip-lights-and-engineer-torque-v4',
         'asset_count':len(results),'unresolved_target_count':16,'assets':results}
 (outdir/'creation-manifest.json').write_text(json.dumps(report,indent=2)+'\n')
 print(f'CHATGPT_CHARACTER_ATLASES_CREATED={len(results)} ASSETS_UNRESOLVED=16 STRICT_DONE_ADDED=0')

if __name__=='__main__':main()
