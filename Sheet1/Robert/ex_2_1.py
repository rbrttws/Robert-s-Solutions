import numpy as np
import matplotlib.pyplot as plt


xx = np.array([0.0, 0.0])
vv = np.array([50.0, 50.0])

mass = 2.
grav = 9.81
vv_0 = np.array([0,0])

def force(mass, grav, vv, gamma, vv_0):

    return np.array([0, -mass*grav]) - gamma*(vv - vv_0)

#print(force(mass, grav))

def step_euler(xx, vv, dtt, mass, grav, gamma, vv_0):
  for ii in range(2):
    xx[ii] += vv[ii]*dtt
    vv[ii] += (force(mass, grav, vv, gamma, vv_0)[ii] * dtt)/mass
  return xx, vv

#print(step_euler(xx, vv, 5, mass, grav))


traject = []
traject.append(xx.copy())

while True:
    xx, vv = step_euler(xx, vv, 0.1, mass, grav, 0, vv_0)
    

    #print(xx)
    if xx[1] <= 0:
        break

    traject.append(xx.copy())

traject = np.array(traject)



plt.plot(traject[:,0], traject[:,1], '-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
