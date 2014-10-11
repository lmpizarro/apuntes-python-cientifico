import numpy as np              # Numerical library

def scale (A,B,C,D):
 t1 = np.concatenate ((A,B),1)
 t2 = np.concatenate ((C,D),1)
 c = np.concatenate ((t1,t2))
 d = np.linalg.inv(c)

 z = np.zeros(((A.shape[0]),1))
 i = np.eye ((C.shape[0]),1)
 y = np.concatenate ((z,i))
 s = d*y
 Nx =  s[0:A.shape[0],0:1]
 Nu = s[A.shape[0]-1: B.shape[0],0:1]

 return Nx, Nu


