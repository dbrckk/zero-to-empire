"""Hand-authored action lighting and physically attached VFX for original sprites.

Pure SVG geometry: no text, logos, detached effects or external image models.
Every glow is attached to an invariant tool tip, wrist or cargo fastener.
Review-only visuals; never marks an asset strict DONE.
"""
from __future__ import annotations
import math

ROLE_LIGHT={
    'OP':('#f3a84c','#fff0ba'),
    'LOG':('#f0b260','#ffe9c6'),
    'ENG':('#4acdd8','#d7ffff'),
}


# Endpoints are defined in wrist-local sprite coordinates, matching the
# ACTUAL authored props in render_chatgpt_originals.py. Both SVG geometry
# and lighting use one rigid rotation; there are no free-floating effects.
TOOL_TIP_OFFSETS={
    'WORK':{'OP':(35.0,-5.0),'LOG':(37.0,0.0),'ENG':(33.0,0.0)},
    'REPAIR':{'OP':(25.0,-19.0),'LOG':(41.0,-12.0),'ENG':(43.0,-13.0)},
}


def tool_angle(action:str,phase:float,*,role:str|None=None)->float:
    if action not in TOOL_TIP_OFFSETS:
        raise ValueError("Tool angle applies only to WORK and REPAIR")
    if role is not None and role not in ROLE_LIGHT:
        raise ValueError("Unknown role for action tool")
    # Engineer's long mechanical ratchet needs an unmistakable torque arc
    # at the 42px Android gameplay scale; preserve other roles' timings.
    if action=='REPAIR' and role=='ENG':
        # A continuous forward/back ratchet cycle with ten meaningful
        # intermediate turns. A sine parked the wrist near two extrema and
        # produced consecutive near-identical frames on the 42px display.
        cycle=(phase/(2.0*math.pi)) % 1.0
        return -4.0+26.0*(1.0-4.0*abs(cycle-.5))
    sweep = 18.0 if action=='REPAIR' else 3.0
    return -4.0+sweep*math.sin(phase)


def tool_tip(role:str,action:str,phase:float,*,tool_x:float,tool_y:float)->tuple[float,float]:
    try:
        dx,dy=TOOL_TIP_OFFSETS[action][role]
    except KeyError as exc:
        raise ValueError("No tool endpoint for role/action") from exc
    angle=math.radians(tool_angle(action,phase,role=role))
    return (tool_x+dx*math.cos(angle)-dy*math.sin(angle),
            tool_y+dx*math.sin(angle)+dy*math.cos(angle))


def action_fx(role:str, action:str, phase:float, *,
              tool_x:float=176.0, tool_y:float=123.0,
              bounce:float=0.0)->str:
    """Return an SVG group for a 256px sprite; empty for unsupported actions.

    WORK/REPAIR emissions are integrated with the tool's existing shaft;
    CELEB lights are on suit cuffs, never confetti; CARRY lights are rivets.
    The sinusoidal envelope closes exactly at the loop boundary.
    """
    if role not in ROLE_LIGHT:
        raise ValueError('Unknown role')
    if action not in {'WORK','REPAIR','CELEB','CARRY','IDLE','WALK'}:
        raise ValueError('Unknown action')
    accent, highlight = ROLE_LIGHT[role]
    envelope=.5+.5*math.cos(phase)
    glow=f'<defs><radialGradient id="fx-{role.lower()}"><stop offset="0" stop-color="{highlight}" stop-opacity=".86"/><stop offset=".45" stop-color="{accent}" stop-opacity=".46"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs>'
    if action in {'WORK','REPAIR'}:
        x,y=tool_tip(role,action,phase,tool_x=tool_x,tool_y=tool_y)
        x=max(12.0,min(233.0,x))
        y=max(12.0,min(233.0,y))
        pulse=round(.61+.39*envelope,3)
        radius=round(8+2.2*envelope,2)
        core=(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{radius}" fill="url(#fx-{role.lower()})"/>'
              f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{2.8+envelope:.2f}" fill="{highlight}" opacity="{pulse}"/>'
              f'<path d="M {x-6:.2f} {y+3:.2f} l 12 -6" stroke="{accent}" stroke-width="2.5" stroke-linecap="round" opacity="{pulse}"/>')
        if action=='WORK':
            core+=f'<path d="M {x-7:.2f} {y+7:.2f} L {x+3:.2f} {y-7:.2f}" stroke="{highlight}" stroke-width="1.2" opacity="{.35+.45*envelope:.3f}"/>'
        else:
            core+=(f'<path d="M {x-3:.2f} {y-4:.2f} l -3 -3 M {x+4:.2f} {y+2:.2f} l 4 3"'
                   f' fill="none" stroke="{highlight}" stroke-width="1.6" stroke-linecap="round" opacity="{.25+.6*envelope:.3f}"/>')
        return glow+f'<g data-action-fx="{action}" opacity=".86">{core}</g>'
    if action=='CARRY':
        y=129+bounce
        return (f'<g data-action-fx="CARRY">'
                f'<circle cx="100" cy="{y:.2f}" r="3.3" fill="{accent}" opacity="{.45+.35*envelope:.3f}"/>'
                f'<circle cx="155" cy="{y:.2f}" r="3.3" fill="{accent}" opacity="{.45+.35*envelope:.3f}"/>'
                f'</g>')
    if action=='CELEB':
        lift=(1-math.cos(phase))/2
        y=140-109*lift+bounce
        lx=75-4*lift
        rx=174+5*lift
        return (f'<g data-action-fx="CELEB">'
                f'<circle cx="{lx:.2f}" cy="{y:.2f}" r="4" fill="{accent}" opacity="{.18+.67*lift:.3f}"/>'
                f'<circle cx="{rx:.2f}" cy="{y:.2f}" r="4" fill="{highlight}" opacity="{.18+.67*lift:.3f}"/>'
                f'</g>')
    return ''
