"""
This file contains code that runs the scripts for both discrete and ODE simulations
(Uncomment the simulations/visualizations you want and run the script to see the results)
"""

# import sir
from sir import *
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


########################################################################################################################
# Running simulations for discrete case
########################################################################################################################

#### Simulation 1:
# b = 1
# k = 0.1
# p = 0.1
# main_discrete2D(p, b, k, N = 1000, T = 100, z = 1)

#### Simulation 2:
# b = 5
# k = 0.01
# main_discrete(b, k, N = 1000, T = 100, z = 1)

#### Simulation 3:
# b = 1
# k = 0.5
# main_discrete(b, k, N = 1000, T = 100, z = 1)

#### Simulation 5:
b = 5
k = 0.1
p = 0.05
main_discrete2(b, k, p, N = 1000, T = 100, z = 1)

#### Phase diagram:

# bs = np.linspace(1,10,10, dtype = int)
# ks = np.linspace(0.01, 0.3, 10)
#
# cts = np.zeros((len(bs), len(ks)))
# for i, b in tqdm(enumerate(bs)):
#     for j in range(len(ks)):
#         inf,sus,rem = discrete_simulation(b, ks[j], T = 20)
#         cts[i,j] = inf[-1]
#
# # Creating plot
# fig, ax = plt.subplots(figsize=(10,10))
#
# # Setting the axis
# ks = [round(num, 4) for num in ks]
# ax.set_yticklabels(ks)
# #ax.set_xticklabels(bs)
#
# im = ax.imshow(cts)
#
# # Setting up color bar
# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="5%", pad=0.05)
# fig.colorbar(im, cax = cax)
#
# plt.xlabel('b')
# plt.ylabel('k')
#
# plt.show()


########################################################################################################################
# Running simulations for ODE case
########################################################################################################################


#### Simulation 1:
# b=1
# k=0.1
#
# s=0.92
# i=0.003
# r=1-s-i
# day=100
#
# a=ode(b,k,s,i,r,day)
#
# plt.plot(a.t,a.y[0])
# plt.plot(a.t,a.y[1])
# plt.plot(a.t,a.y[2])
# plt.legend(["Susceptible","Infected", "Removed"])
# plt.title("ODE simulation1")
# plt.xlabel("day")
# plt.ylabel("fraction of population")


#### Simulation 2:

# b=0.5
# k=0.2
#
# s=0.92
# i=0.003
# r=1-s-i
# day=100
#
# a=ode(b,k,s,i,r,day)
#
# plt.plot(a.t,a.y[0])
# plt.plot(a.t,a.y[1])
# plt.plot(a.t,a.y[2])
# plt.legend(["Susceptible","Infected", "Removed"])
# plt.title("ODE simulation2")
# plt.xlabel("day")
# plt.ylabel("fraction of population")


#### Simulation 3

# b=0.2
# k=0.08
#
# s=0.92
# i=0.003
# r=1-s-i
# day=100
#
# a=ode(b,k,s,i,r,day)
#
# plt.plot(a.t,a.y[0])
# plt.plot(a.t,a.y[1])
# plt.plot(a.t,a.y[2])
# plt.legend(["Susceptible","Infected", "Removed"])
# plt.title("ODE simulation3")
# plt.xlabel("day")
# plt.ylabel("fraction of population")


#### Simulation 4

# b=0.2
# k=0.5
#
# s=0.35
# i=0.53
# r=1-s-i
# day=100
#
# a=ode(b,k,s,i,r,day)
#
# plt.plot(a.t,a.y[0])
# plt.plot(a.t,a.y[1])
# plt.plot(a.t,a.y[2])
# plt.legend(["Susceptible","Infected", "Removed"],loc ="right")
# plt.title("ODE simulation4")
# plt.xlabel("day")
# plt.ylabel("fraction of population")


#### Simulation 5
# b=0.2
# k=0.0002
#
# s=0.89
# i=0.09
# r=1-s-i
# day=100
#
# a=ode(b,k,s,i,r,day)
#
# plt.plot(a.t,a.y[0])
# plt.plot(a.t,a.y[1])
# plt.plot(a.t,a.y[2])
# plt.legend(["Susceptible","Infected", "Removed"],loc ="right")
# plt.title("ODE simulation5")
# plt.xlabel("day")
# plt.ylabel("fraction of population")


#### phase diagram

# bs = np.linspace(0.2,0.4,10)   #variation in b
# ks = np.linspace(0.05,0.3,10)  #variation in k
#
# s=0.92
# i=0.03
# r=1-s-i
# day=100
# cts = np.zeros((len(bs), len(ks)))
# for i in range(len(bs)):
#     for j in range(len(ks)):
#         sol=ode(bs[i],ks[j],s,i,r,day)
#         cts[i,j]=sol.y[1][50]  #the fraction of infected peaple on the 50th day
#
# fig, ax = plt.subplots(figsize=(10,10))
# ks = [round(num, 4) for num in ks]
# ax.set_yticklabels(ks)
# bs = [round(num, 2) for num in bs]
# ax.set_xticklabels(bs)
# im = ax.imshow(cts)
#
# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="5%", pad=0.05)
# fig.colorbar(im, cax = cax)
#
# plt.xlabel('b')
# plt.ylabel('k')



#### Simulation of variation 1

# def ode(b,k,mu,s0,i0,r0,u0,day):
#     v0=np.array([s0,i0,r0,u0])
#     t_span=(0,day)
#     t_eval=np.linspace(0,day,day+1)

#     f = lambda t,v: np.array([
#         -b*v[0]*v[1],                #ds/dt=-b*s(t)*i(t)
#         b*v[0]*v[1]-k*v[1]-mu*v[1],          #di/dt=b*s(t)*i(t)-k*i(t)
#         k*v[1],                       #dr/dt=k*i(t)
#         v[1]*mu     #du/dt=mu*i(t)
#     ])

#     sol=solve_ivp(f,t_span,v0,t_eval=t_eval)
#     return sol



# b=0.2
# k=0.08
# mu = 0.005


# s=0.92
# i=0.003
# r=1-s-i
# u=0
# day=200

# a=ode(b,k,mu,s,i,r,u,day)

# plt.plot(a.t,a.y[0])
# plt.plot(a.t,a.y[1])
# plt.plot(a.t,a.y[2])
# plt.plot(a.t,a.y[3])
# plt.legend(["S","I", "R","U"])
# plt.title("ODE simulation of variation 1")
# plt.xlabel("day")
# plt.ylabel("fraction of population")
# fig = plt.gcf()
# fig.set_size_inches(18.5, 10.5)
# fig.savefig('ode_simulation_modified_variation 1.png', dpi=100)




#### Simulation of variation 2
# b=0.2
# k=0.08
# a = 0.05
# s=0.92
# i=0.003
# v=0.05
# r=1-s-i-v

# day=200

# def ode(b,k,a,s0,i0,r0,v0,day):
#     g0=np.array([s0,i0,r0,v0])
#     t_span=(0,day)
#     t_eval=np.linspace(0,day,day+1)

#     f = lambda t,g: np.array([        
#         -b*g[0]*g[1]-a*g[0]*g[3],           
#         b*g[0]*g[1]-k*g[1],   
#         k*g[1],                   
#         a*g[0]*g[3]])

#     sol=solve_ivp(f,t_span,g0,t_eval=t_eval)
#     return sol

# s=ode(b,k,a,s,i,r,v,day)

# plt.plot(s.t,s.y[0])
# plt.plot(s.t,s.y[1])
# plt.plot(s.t,s.y[2])
# plt.plot(s.t,s.y[3])
# plt.legend(["Susceptible","Infected", "Removed","Vaccinated"])
# plt.title("ODE_simulation_variation2")
# plt.xlabel("day")
# plt.ylabel("fraction of population")
# fig = plt.gcf()
# fig.set_size_inches(12, 6)
# fig.savefig('ODE_simulation_modified_variation2.png', dpi=100)
