
import numpy as np
from numpy.linalg import linalg
import matplotlib.pyplot as plt


data = np . load ( "solar_system.npz")
names = data [ "names"]
x_init = data [ "x_init"]
v_init = data [ "v_init"]
m = data [ "m"]
g = data [ "g"]


#print(names[0])
#print(x_init[:,0])
#print()
#print(v_init)
#print(g)

xx = x_init
vv = v_init


def force(x12, m1, m2, g):

    fac = np.linalg.norm(x12)
    fac = 1/(fac**3)

    f12 = - g * m1 * m2 * fac * x12

    return f12

print(force(xx[:,0]-xx[:,1], m[0], m[1], g))

def step_euler(xx, vv, dtt, mass, grav, gamma, vv_w):
  for ii in range(2):
    xx[ii] += vv[ii]*dtt
    vv[ii] += (force(mass, grav, vv, gamma, vv_w)[ii] * dtt)/mass
  return xx, vv

#print(step_euler(xx, vv, 5, mass, grav))

def main_loop(gamma, vv_w):

    xx = np.array([0.0, 0.0])
    vv = np.array([50.0, 50.0])

    traject = []
    traject.append(xx.copy())

    while True:
    	xx, vv = step_euler(xx, vv, 0.1, mass, grav, gamma, vv_w)
    

    	#print(xx)
    	if xx[1] <= 0:
        	break

    	traject.append(xx.copy())

    traject = np.array(traject)
    return traject
