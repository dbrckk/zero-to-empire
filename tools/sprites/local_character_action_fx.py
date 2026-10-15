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
        reach={'OP':(30,24),'LOG':(31,37),'ENG':(28,39)}[role][0 if action=='WORK' else 1]
        x=min(234.0,tool_x+reach)
        y=tool_y-4 if action=='WORK' else tool_y-11
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
