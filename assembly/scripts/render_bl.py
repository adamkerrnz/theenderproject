import os
import bpy, json, math, sys, os
from mathutils import Vector
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene
man=json.load(open(os.path.join(os.environ.get('WORK','work'),'parts','manifest.json')))
cols={'print':(0.035,0.035,0.04,1),'accent':(0.80,0.12,0.02,1),'extruder':(0.18,0.18,0.2,1),'motor':(0.12,0.12,0.13,1),
'fan':(0.05,0.05,0.05,1),'pcb':(0.05,0.18,0.08,1),'alu':(0.75,0.76,0.78,1),'sock':(0.85,0.85,0.83,1),'brass':(0.85,0.62,0.25,1),
'eddy':(0.08,0.2,0.55,1),'steel':(0.6,0.62,0.65,1),'alu_dark':(0.3,0.31,0.33,1)}
metal={'alu':0.9,'brass':1,'steel':0.9,'alu_dark':0.8,'motor':0.4}
rough={'print':0.55,'accent':0.45,'fan':0.6,'pcb':0.4,'sock':0.7}
M={}
for k,c in cols.items():
    m=bpy.data.materials.new(k); m.use_nodes=True; b=m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value=c; b.inputs['Metallic'].default_value=metal.get(k,0); b.inputs['Roughness'].default_value=rough.get(k,0.35); M[k]=m
objs=[]
hide=set(sys.argv[sys.argv.index('--hide')+1].split(',')) if '--hide' in sys.argv else set()
for p in man:
    if p['name'] in hide: continue
    bpy.ops.wm.ply_import(filepath=os.path.join(os.environ.get('WORK','work'),'parts',p['name']+'.ply'))
    o=bpy.context.selected_objects[0]; o.name=p['name']; o.data.materials.clear(); o.data.materials.append(M[p['mat']])
    for poly in o.data.polygons: poly.use_smooth=False
    objs.append(o)
# frame on toolhead (ignore long rail/extrusion)
pts=[o.matrix_world@Vector(c) for o in objs if o.name not in('mgn_rail','extrusion') for c in o.bound_box]
mn=Vector([min(p[i] for p in pts) for i in range(3)]); mx=Vector([max(p[i] for p in pts) for i in range(3)])
ctr=(mn+mx)/2; size=(mx-mn).length
tgt=bpy.data.objects.new('tgt',None); sc.collection.objects.link(tgt); tgt.location=ctr
w=bpy.data.worlds.new('w'); sc.world=w; w.use_nodes=True; w.node_tree.nodes['Background'].inputs[0].default_value=(1,1,1,1); w.node_tree.nodes['Background'].inputs[1].default_value=1.0
def light(name,loc,energy,size=200):
    L=bpy.data.lights.new(name,'AREA'); L.energy=energy; L.size=size; o=bpy.data.objects.new(name,L); sc.collection.objects.link(o); o.location=loc
    c=o.constraints.new('TRACK_TO'); c.target=tgt; c.track_axis='TRACK_NEGATIVE_Z'; c.up_axis='UP_Y'
light('key',ctr+Vector((-250,-300,300)),2.2e6); light('fill',ctr+Vector((300,-200,100)),0.9e6); light('rim',ctr+Vector((100,350,250)),1.4e6)
cam=bpy.data.cameras.new('cam'); cam.lens=85; cam.clip_end=10000; co=bpy.data.objects.new('cam',cam); sc.collection.objects.link(co); sc.camera=co
c=co.constraints.new('TRACK_TO'); c.target=tgt; c.track_axis='TRACK_NEGATIVE_Z'; c.up_axis='UP_Y'
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=int(os.environ.get('SAMPLES','48')); sc.cycles.use_denoising=True
sc.render.resolution_x=1400; sc.render.resolution_y=1100; sc.render.film_transparent=False
sc.view_settings.view_transform='AgX'
views=json.loads(sys.argv[sys.argv.index('--views')+1])
for name,(az,el,dist) in views.items():
    a=math.radians(az); e=math.radians(el); d=size*dist
    co.location=ctr+Vector((d*math.cos(e)*math.sin(a), -d*math.cos(e)*math.cos(a), d*math.sin(e)))
    sc.render.filepath=os.path.join(os.environ.get('WORK','work'),f'out_{name}.png'); bpy.ops.render.render(write_still=True); print('rendered',name)
