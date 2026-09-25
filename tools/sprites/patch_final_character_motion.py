#!/usr/bin/env python3
from pathlib import Path

p=Path('tools/sprites/kaggle_character_sheet_factory_v1.py')
s=p.read_text(encoding='utf-8')
if 'v1.8-final-motion-guard' in s:
    print('already patched')
    raise SystemExit(0)

old_repair="'REPAIR':['half-kneel and reach tool toward low repair point','tool pressed to low repair point, free hand bracing','tool moves horizontally across repair point, no sparks','lean closer and inspect repair point','tool contacts mid-height repair point','free hand adjusts component while tool stays ready','pull back and inspect with torso upright','second tool contact at mid height','rise from half-kneel while lowering tool','neutral repair-ready stance']"
new_repair="'REPAIR':['deep half-kneel, torso leaned far forward, right arm fully extended with tool toward low repair point','tool pressed low, free hand bracing wide, shoulders rotated toward repair','tool sweeps clearly left across low repair point, torso follows, no sparks','pull tool back to chest and lean close to inspect, elbow strongly bent','rise to wide crouch, tool reaches diagonally to mid-height repair point','free hand reaches high to adjust component while tool hand stays low','pull both arms back, torso upright and weight shifted onto rear leg','second strong tool contact at mid height with opposite shoulder forward','rise from crouch while lowering tool beside thigh, free arm extended for balance','standing repair-ready stance, both arms lowered and feet apart']"
old_celeb="'CELEB':['neutral stance both arms down','right arm begins lifting, elbow bent','right fist reaches shoulder height, torso opens','right fist fully overhead, weight shifts to left leg','small overhead fist pump with opposite arm bent','arm lowers to shoulder height, weight recenters','arm lowers beside body','return to neutral stance']"
new_celeb="'CELEB':['neutral stance both arms down, feet apart','right arm lifts outward to forty-five degrees, elbow bent, left arm stays down','right fist at shoulder height, left arm swings outward, torso rotates right','right fist fully overhead, left arm bent across chest, weight shifts strongly to left leg','both arms clearly raised, right fist high and left fist at shoulder, torso leaning left','right arm drops to shoulder height while left arm extends outward, weight shifts right','right arm lowers diagonally while left arm returns down, torso recenters','return to neutral stance with both arms fully down and feet apart']"
old_strength="""elif i['action']=='REPAIR':
        strength=min(.58,.38+fi*.018+attempt*.03)
       else:
        strength=min(.48,.29+fi*.015+attempt*.025)"""
new_strength="""elif i['action']=='REPAIR':
        strength=min(.68,.48+fi*.018+attempt*.035)
       elif i['action']=='CELEB':
        strength=min(.62,.43+fi*.016+attempt*.035)
       else:
        strength=min(.48,.29+fi*.015+attempt*.025)"""
for label,old in [('startup','character-sheet-flux-v1.7-action-motion-retry'),('repair',old_repair),('celeb',old_celeb),('strength',old_strength)]:
    if old not in s:
        raise SystemExit(f'expected {label} source block not found')
s=s.replace('character-sheet-flux-v1.7-action-motion-retry','character-sheet-flux-v1.8-final-motion-guard')
s=s.replace(old_repair,new_repair).replace(old_celeb,new_celeb).replace(old_strength,new_strength)
p.write_text(s,encoding='utf-8')
print('patched final TECH repair/celeb motion')
