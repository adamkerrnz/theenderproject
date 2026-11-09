import os
HERE=os.path.dirname(os.path.abspath(__file__))
REPO=os.path.abspath(os.path.join(HERE,'..','..'))
WORK=os.environ.get('WORK',os.path.join(HERE,'work'))
os.makedirs(WORK,exist_ok=True)
import sys, json, numpy as np, trimesh
sys.path.insert(0,HERE)
from place import part, files
from reg import load_ref
import os
os.makedirs(os.path.join(WORK,'parts'),exist_ok=True)
out=[]
def save(name,mesh,mat,label):
    mesh.export(os.path.join(WORK,'parts',f'{name}.ply')); out.append(dict(name=name,mat=mat,label=label))
# printed parts (ours)
mats={'shroud':'accent'}
labels={'shroud':'Shroud (Sherpa Micro, ProbeRight, 2510)','core':'Core (Sherpa Micro, Bambu)','door':'Cable door','xL':'X-frame left (Ender3 MGN9H front)','xR':'X-frame right','eddy':'Eddy side bracket','bridge':'Motor bridge (umbilical PCB)','mount':'EBB36 PCB mount'}
for k in files: save(k,part(k),mats.get(k,'print'),labels[k])
# reference parts from designer's blend
def ref(names,dx=0,R=None,c=None):
    m=trimesh.util.concatenate([load_ref(n,dx) for n in names])
    return m
sherpa=['housing_core_x1_rev15','housing_rear_x1_rev15','[a]_housing_front_x1_rev5','[a]_idler_arm_long_x1_rev5','Thumbscrew.001','50t_SpurGear_5mm_shaft.001','sestava_bondtech_real.001','sestava_bondtech_real.002','sestava_bondtech_real.003','MR85_bearing.001','MR85_bearing.002']
save('sherpa',ref(sherpa),'extruder','Sherpa extruder (Sherpa Mini model as stand-in)')
save('motor',ref(['LDO-36STH20-1004AHG(XH).005']),'motor','LDO-36STH20 round stepper')
b1=ref(['4010_Blower_Fan_v2_left.011'],-80); b2=ref(['4010_Blower_Fan_v2_left.012'],-80)
save('blowers',trimesh.util.concatenate([b1,b2]),'fan','2x 4010 blowers')
f=ref(['3010_hotend_fan.003'],-80); c=f.bounds.mean(0); S=np.diag([25/30,1,25/30,1]); S[:3,3]=c-np.diag(S)[:3]*c; f.apply_transform(S); f.apply_translation([0,0.8,0])
save('hotendfan',f,'fan','2510 hotend fan (scaled 3010 model)')
ebb=ref(['EBB36 CAN V1.015'],60)
save('ebb36',ebb,'pcb','BTT EBB36 (v1 model; Gen2 has the same footprint)')
# proxies
P=[]
hs=[]
for i,z in enumerate(np.arange(18,44,2.2)):
    hs.append(trimesh.creation.box([22,22,1.1]).apply_translation([0,0,z]))
hs.append(trimesh.creation.box([10,10,28]).apply_translation([0,0,31]))
save('hotend_heatsink',trimesh.util.concatenate(hs),'alu','Bambu X1 hotend heatsink (proxy)')
save('hotend_heater',trimesh.util.concatenate([trimesh.creation.box([15,15,9]).apply_translation([0,0,8.5]),trimesh.creation.cylinder(2.2,6,sections=24).apply_translation([0,0,15])]),'sock','Bambu X1 heater + sock (proxy)')
save('nozzle',trimesh.creation.cone(3.2,4,sections=32).apply_transform(trimesh.transformations.rotation_matrix(np.pi,[1,0,0])).apply_translation([0,0,4]),'brass','Nozzle (proxy)')
save('eddy_coil',trimesh.creation.box([7,21,22]).apply_translation([33.6+3.5,-5.65,2.5+11]),'eddy','BTT Eddy Coil (proxy)')
blk=trimesh.creation.box([39.9,8,20]).apply_translation([0,24.6+4,48.55])
rail=trimesh.creation.box([300,6.5,9]).apply_translation([0,28.1+3.25,48.55])
ext=trimesh.creation.box([300,20,20]).apply_translation([0,39.1+10,48.55])
save('mgn_block',blk,'steel','MGN9H block')
save('mgn_rail',rail,'steel','MGN9H rail')
save('extrusion',ext,'alu_dark','2020 X extrusion')
json.dump(out,open(os.path.join(WORK,'parts','manifest.json'),'w'),indent=1)
print(len(out),'parts')
