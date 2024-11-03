"""
Implement tests for ODE based simulation
"""
import unittest
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import solve_ivp
import sys
import os
import os.path as osp
dir = osp.join(osp.dirname(osp.abspath(__file__)), "../doc/Midterm Checkpoint/")
sys.path.append(dir)
from sir import *

def ode(b,k,s0,i0,r0,day):
    """
    This is the function we create to run the ode based simulation
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



class Testode(unittest.TestCase):
    """
    A test for ode based simulation
    """
    

    def setUp(self):
        pass
    
    
    def test_ode_simulation(self):
        """
        test the ode based simulation
        test1: numerical test to check the validity of the ODE function
        test2: numerical test to check s(t)+i(t)+r(t)=1
        """
        b = 0.3
        k = 0.11
        s0 = 0.92
        i0 = 0.003
        r0 = 1-s0- i0
        day = 100
        
        
        a=ode(b,k,s0,i0,r0,day)

        h = 0.000001
       
        test_r = []
        test_i = []
        test_s = []

        for num in range(99):

            test_r.append (abs((a.y[2][num+1]-a.y[2][num])/h -k*a.y[1][num]) <= 0.01)

        for num in range(99):

            test_i.append (abs((a.y[0][num+1]-a.y[0][num])/h -b*a.y[0][num]*a.y[1][num] + k*a.y[1][num]) <= 0.01)

        for num in range(99):

            test_s.append (abs((a.y[1][num+1]-a.y[1][num])/h + b*a.y[0][num]*a.y[1][num]) <= 0.01)


        real = []
        

        for m in range(99):
            real.append(True)
            
        self.assertTrue((abs(test_r[-1] + test_s[-1] + test_i[-1] -1)<= 1e-2) & (test_r == real) & (test_s == real) & (test_i == real) )


class TestPerson(unittest.TestCase):

    def test_is_susceptible(self):
        p = Person()
        self.assertEqual(p.is_susceptible(), True, "Should be susceptible")

    def test_infect_is_infected(self):
        p = Person()
        self.assertEqual(p.is_infected(), False, "Should not be infected")
        p.infect()
        self.assertEqual(p.is_infected(), True, "Should be infected")

    def test_remove_is_removed(self):
        p = Person()
        self.assertEqual(p.is_removed(), False, "Should not be removed")

        p.remove()
        self.assertEqual(p.is_removed(), False, "Should not be removed")

        p.infect()
        p.remove()
        self.assertEqual(p.is_removed(), True, "Should be removed")

if __name__ == '__main__':
    unittest.main()
