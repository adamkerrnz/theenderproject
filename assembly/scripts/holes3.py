import sys, trimesh, numpy as np
def holes(m, axes=(0,1,2), nslices=15, rmin=0.6, rmax=3.5):
    seen=[]
    for ax in axes:
        lo,hi=m.bounds[:,ax]
        for f in np.linspace(0.03,0.97,nslices):
            n=np.zeros(3);n[ax]=1;o=np.zeros(3);o[ax]=lo+(hi-lo)*f
            s=m.section(plane_origin=o,plane_normal=n)
            if s is None: continue
            for c3 in s.discrete:
                ctr=c3.mean(0); r=np.linalg.norm(c3-ctr,axis=1)
                if len(c3)>8 and r.std()<0.2 and rmin<r.mean()<rmax:
                    key=(ax,round(2*r.mean(),1))+tuple(np.round(np.delete(ctr,ax),1))
                    if all(not(k[0]==key[0] and abs(k[1]-key[1])<0.3 and abs(k[2]-key[2])<0.5 and abs(k[3]-key[3])<0.5) for k in seen):
                        seen.append(key)
    return seen
if __name__=='__main__':
    m=trimesh.load(sys.argv[1],force='mesh')
    if len(sys.argv)>2: m.apply_transform(np.load(sys.argv[2]))
    for h in holes(m): print(h)
