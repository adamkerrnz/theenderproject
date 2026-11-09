import os
import bpy, sys, os
bpy.ops.wm.open_mainfile(filepath=sys.argv[-1])
dg=bpy.context.evaluated_depsgraph_get()
import numpy as np
os.makedirs(os.path.join(os.environ.get('WORK','work'),'ref'),exist_ok=True)
for o in bpy.data.objects:
    if o.type!='MESH': continue
    e=o.evaluated_get(dg); me=e.to_mesh()
    me.transform(o.matrix_world)
    me.calc_loop_triangles()
    v=np.array([x.co[:] for x in me.vertices],dtype=np.float32)
    f=np.array([t.vertices[:] for t in me.loop_triangles],dtype=np.int32)
    np.savez_compressed(os.path.join(os.environ.get('WORK','work'),'ref',o.name.replace('/','_')+'.npz'),v=v,f=f)
    e.to_mesh_clear()
print('done')
