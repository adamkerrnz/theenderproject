import os
HERE=os.path.dirname(os.path.abspath(__file__))
REPO=os.path.abspath(os.path.join(HERE,'..','..'))
WORK=os.environ.get('WORK',os.path.join(HERE,'work'))
os.makedirs(WORK,exist_ok=True)
import trimesh, numpy as np, itertools, sys
from trimesh.registration import icp
def load_ref(name, dx=0):
    d=np.load(os.path.join(WORK,'ref',f'{name}.npz')); m=trimesh.Trimesh(d['v'],d['f'],process=False)
    m.apply_translation([dx,0,0]); return m
def rotations():
    Rs=[]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1,-1],repeat=3):
            R=np.zeros((3,3))
            for i,(p,s) in enumerate(zip(perm,signs)): R[i,p]=s
            if np.linalg.det(R)>0: Rs.append(R)
    return Rs
def register(src, ref, n=3000, iters=60, rots=None):
    pts=src.sample(n); best=None
    for R in (rots or rotations()):
        T=np.eye(4); T[:3,:3]=R
        c=(T[:3,:3]@src.bounds.mean(0))
        T[:3,3]=ref.bounds.mean(0)-c
        M,_,cost=icp(pts, ref, initial=T, max_iterations=iters, reflection=False, scale=False, threshold=1e-6)
        if best is None or cost<best[1]: best=(M,cost)
    return best
