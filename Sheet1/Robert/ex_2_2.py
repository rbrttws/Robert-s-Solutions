
import numpy as np
import matplotlib.pyplot as plt


mass = 2.
grav = 9.81
vv_0 = np.array([0,0])

def force(mass, grav, vv, gamma, vv_w):

    vv_0 = np.array([vv_w,0])

    return np.array([0, -mass*grav]) - gamma*(vv - vv_0)

#print(force(mass, grav))

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

traject1 = main_loop(0,0)
traject2 = main_loop(0.1,0)
traject3 = main_loop(0.1,-50)

plt.plot(traject1[:,0], traject1[:,1], '-', label = "no friction and no wind")
plt.plot(traject2[:,0], traject2[:,1], '-', label = "friction and no wind")
plt.plot(traject3[:,0], traject3[:,1], '-', label = "friction and wind")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
