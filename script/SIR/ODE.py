import numpy as np
from numpy.random import randint, rand
import matplotlib.pyplot as plt
from tqdm import tqdm
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.integrate import solve_ivp



def ode(b,k,s0,i0,r0,day):
    """
    This is the function we create to run the ode based simulation
    b: the number of interactions each day that could spread the disease (per individual)
    k: the fraction of the infectious population which recovers each day
    s0 - the fraction of the individual who has not yet caught the disease
    i0- the fraction of the susceptible individuals
    r0 - the fraction of the individuals were previously infectious, and either have recovered and are now immune, or have died. 
    day - the number of days the simulation goes

    """
    v0=np.array([s0,i0,r0])
    t_span=(0,day)
    t_eval=np.linspace(0,day,100000*day)

    f = lambda t,v: np.array([
        -b*v[0]*v[1],                #ds/dt=-b*s(t)*i(t)
        b*v[0]*v[1]-k*v[1],          #di/dt=b*s(t)*i(t)-k*i(t)
        k*v[1]                       #dr/dt=k*i(t)
    ])

    sol=solve_ivp(f,t_span,v0,t_eval=t_eval)
    return sol
