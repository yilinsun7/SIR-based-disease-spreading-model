"""
This file contains functions necessary for discrete simulations
"""
import numpy as np
from numpy.random import randint, rand
import matplotlib.pyplot as plt
from .Person2D import Population2D

def discrete_simulation2D(p, b, k, N = 1000, T = 100, z = 1):
    """
    This function runs agent-based simulation on the disease-spread model

    Inputs:
    :param b: Number of people one infected patient can infect in one day (int)
    :param k: Fraction of people that could recover everyday (between 0 and 1)
    :param N: population size, default to 1000
    :param T: number of days we want to run the simulation, default to 100
    :param z: number of infected people at the start of the simulation, default to 1

    Outputs:
    :counts_inf: number of infected people by the end of the simulation
    :counts_sus: number of susceptible people by the end of the simulation
    :counts_cur: number of removed(cured, died, etc.) people by the end of the simulation
    """
    # Creates population
    pop = Population2D(N, z)

    # Initialize the three count vectors to be returned
    counts_inf = [z]
    counts_sus = [N-z]
    counts_rem = [0]

    q = np.sqrt(b / N / np.pi)

    # Running simulation
    for t in range(T):
        # Update the population
        s, i, r = pop.iterate(p, q, k)

        # Update all three counts
        counts_inf.append(i)
        counts_sus.append(s)
        counts_rem.append(r)

    return counts_inf, counts_sus, counts_rem

########################################################################################################################
# Function that runs simulation and visualize results
########################################################################################################################

def main_discrete2D(p, b, k, N = 1000, T = 100, z = 1):

    """
    This function runs agent-based simulation on the disease-spread model and visualize results in a plot

    Inputs:
    :param b: Number of people one infected patient can infect in one day (int)
    :param k: Fraction of people that could recover everyday (between 0 and 1)
    :param N: population size, default to 1000
    :param T: number of days we want to run the simulation, default to 100
    :param z: number of infected people at the start of the simulation, default to 1

    Outputs:
    A plot that captures the number of infected, susceptible, and removed people in the population through time
    """

    # Runs simulation
    c_inf, c_sus, c_rem = discrete_simulation2D(p, b, k, N, T, z)

    # Visualizing the result
    x_axis = np.linspace(1, 100 + 1, 100 + 1)
    plt.plot(x_axis, c_inf, c='r', label="Infected")
    plt.plot(x_axis, c_sus, c='b', label="Susceptible")
    plt.plot(x_axis, c_rem, c='g', label="Removed")
    plt.legend()
    plt.xlabel('number of days')
    plt.ylabel('number of people')
    plt.title('Simulation results')
    plt.show()