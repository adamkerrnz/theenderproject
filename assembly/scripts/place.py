import os
HERE=os.path.dirname(os.path.abspath(__file__))
REPO=os.path.abspath(os.path.join(HERE,'..','..'))
WORK=os.environ.get('WORK',os.path.join(HERE,'work'))
os.makedirs(WORK,exist_ok=True)
import trimesh, numpy as np, sys
sys.path.insert(0,HERE)
from reg import load_ref
S=os.path.join(REPO,'stl')+'/'
def Tm(rows, t):
    M=np.eye(4); M[:3,:3]=np.array(rows,float); M[:3,3]=t; return M
T={}
T['shroud']=Tm([[1,0,0],[0,0,1],[0,-1,0]],[-560,0,0])   # from ICP against the designer's shroud
T['core']=Tm([[1,0,0],[0,0,-1],[0,1,0]],[840,-130,0])
T['door']=Tm([[1,0,0],[0,0,-1],[0,1,0]],[-0.088,0.666,66.824])   # from ICP against the designer's cable door
# x-frame left: x_b = z_s + 93.4 ; y_b = y_s + 9.9 ; z_b = -x_s + 171.6
T['xL']=Tm([[0,0,1],[0,1,0],[-1,0,0]],[93.4,9.9,171.6])
Mxs=np.diag([-1,1,1,1.]); Mxs[0,3]=2*119.9
Mxb=np.diag([-1,1,1,1.])
T['xR']=Mxb@T['xL']@Mxs
# Eddy bracket: x_b = -z_s - 79.67 ; y_b = y_s ; z_b = x_s + 646.35
for n in ['eddy','eddy1','eddy15']: pass
T['eddy']=Tm([[0,0,-1],[0,1,0],[1,0,0]],[-79.67,0,646.35])
ZC=89.6
# motor bridge: x_b = x_s-8.25 ; y_b = -z_s - 10.2 ; z_b = y_s - 32.35 + ZC
T['bridge']=Tm([[1,0,0],[0,0,-1],[0,1,0]],[-8.25,-10.2,ZC-32.35])
# pcb mount: x_b = x_s-8.25 ; y_b = z_s + 82.8 ; z_b = -(y_s-32.35)+ZC
T['mount']=Tm([[1,0,0],[0,0,1],[0,-1,0]],[-8.25,82.8,ZC+32.35])
files={'shroud':'[a]_MiniStealth_Shroud_SherpaMicro_ProbeRight_2510.stl','core':'MiniStealth_Core_SherpaMicro_Bambu.stl','door':'SherpaMicro_Cable_Door.stl',
'xL':'Ender3_MGN9H_Front_x-frame_Left.stl','xR':'Ender3_MGN9H_Front_x-frame_Right.stl','eddy':'Side_Mount_V0_BTT_Eddy_bracket.stl',
'bridge':'SherpaMicro_Motor_Bridge_UmbilicalPCB_Mount.stl','mount':'SherpaMicro_UmbilicalPCB_Mount.stl'}
def part(k):
    m=trimesh.load(S+files[k],force='mesh'); 
    if np.linalg.det(T[k][:3,:3])<0: print('WARNING mirror',k)
    m.apply_transform(T[k]); return m
if __name__=='__main__':
    P={k:part(k) for k in files}
    for k,m in P.items(): print(k, m.bounds.round(1).tolist())
    # interference check between pairs
    keys=list(P)
    for i in range(len(keys)):
        for j in range(i+1,len(keys)):
            a,b=P[keys[i]],P[keys[j]]
            if (a.bounds[0]<b.bounds[1]).all() and (b.bounds[0]<a.bounds[1]).all():
                f=b.contains(a.sample(3000)).mean()
                if f>0.003: print(f'overlap {keys[i]} in {keys[j]}: {f:.3f}')
