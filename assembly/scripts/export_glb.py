import os
import bpy, json, sys
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'render_bl.py')).read().split("# frame on toolhead")[0].replace("bpy.ops.wm.read_factory_settings(use_empty=True)","bpy.ops.wm.read_factory_settings(use_empty=True)"))
for o in bpy.data.objects:
    if o.type=='MESH':
        m=o.modifiers.new('dec','DECIMATE'); 
        n=len(o.data.polygons)
        m.ratio=min(1.0, 20000/n) if n>20000 else 1.0
bpy.ops.export_scene.gltf(filepath=os.path.join(os.environ.get('WORK','work'),'toolhead.glb'), export_format='GLB', export_apply=True, export_yup=True)
