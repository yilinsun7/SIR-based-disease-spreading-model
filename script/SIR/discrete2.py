"""
This file contains functions necessary for discrete simulations.
Note: code in this file is for variation 1 in the discrete case, functions that run simulations are adjusted to take
into consideration the parameter p (probability to interact with others)
"""
import numpy as np
from numpy.random import randint, rand
import matplotlib.pyplot as plt
from .Person import Person
from .Person2 import Person2

########################################################################################################################
# Helper functions to be called in the run_simulation function
########################################################################################################################

def count_infected(pop):
    """
    This function counts number of infected people in the population

    Input: population (type: list of Person)
    Output: number of infected people (type: int)
    """
    return sum(p.is_infected() for p in pop)

def count_susceptible(pop):
    """
    This function counts number of susceptible people in the population

    Input: population (type: list of Person)
    Output: number of susceptible people (type: int)
    """
    return sum(p.is_susceptible() for p in pop)

def count_removed(pop):
    """
    This function counts number of removed people (cured, died, etc.) in the population

    Input: population (type: list of Person)
    Output: number of removed people (type: int)
    """
    return sum(p.is_removed() for p in pop)

def one_day2(pop, N, b, k):
    """
    This function captures what happens in one day of the simulation
    :param pop: the population
    :param N: size of population
    :param b: number of people one infected patient can infect in one day
    :param k: fraction of people that could recover every day
    :return: population after one day of interactions
    """

    # Infect Part
    for i in range(N):
        if pop[i].is_infected():
            # If this person is infected, they could infect all b number of contacts
            contacts = randint(N, size=b)

            for j in contacts:
                if (pop[i].is_interactable and pop[j].is_interactable):
                    pop[j].infect()

    # Recover Part
    recover = randint(N, size = round(k * N))
    for h in recover:
        pop[h].remove()

    return pop

########################################################################################################################
# Function that runs simulation
########################################################################################################################

def discrete_simulation2(b, k, p, N = 1000, T = 100, z = 1):
    """
    This function runs agent-based simulation on the disease-spread model

    Inputs:
    :param b: Number of people one infected patient can infect in one day (int)
    :param k: Fraction of people that could recover everyday (between 0 and 1)
    :param p: probability that a person will still interact and infect others after being infected
    :param N: population size, default to 1000
    :param T: number of days we want to run the simulation, default to 100
    :param z: number of infected people at the start of the simulation, default to 1

    Outputs:
    :counts_inf: number of infected people by the end of the simulation
    :counts_sus: number of susceptible people by the end of the simulation
    :counts_cur: number of removed(cured, died, etc.) people by the end of the simulation
    """
    # Creates population
    pop = [Person2(p) for i in range(N)]

    # Initialize the population by setting z people to be already infected:
    for i in range(z):
        pop[i].infect()

    # Initialize the three count vectors to be returned
    counts_inf = [count_infected(pop)]
    counts_sus = [count_susceptible(pop)]
    counts_rem = [count_removed(pop)]

    # Running simulation
    for t in range(T):
        # Update the population
        pop = one_day2(pop, N, b, k)

        # Update all three counts
        counts_inf.append(count_infected(pop))
        counts_sus.append(count_susceptible(pop))
        counts_rem.append(count_removed(pop))

    return counts_inf, counts_sus, counts_rem

########################################################################################################################
# Function that runs simulation and visualize results
########################################################################################################################

def main_discrete2(b, k, p, N = 1000, T = 100, z = 1):

    """
    This function runs agent-based simulation on the disease-spread model and visualize results in a plot

    Inputs:
    :param b: Number of people one infected patient can infect in one day (int)
    :param k: Fraction of people that could recover everyday (between 0 and 1)
    :param p: probability that a person will still interact and infect others after being infected
    :param N: population size, default to 1000
    :param T: number of days we want to run the simulation, default to 100
    :param z: number of infected people at the start of the simulation, default to 1

    Outputs:
    A plot that captures the number of infected, susceptible, and removed people in the population through time
    """

    # Runs simulation
    c_inf, c_sus, c_rem = discrete_simulation2(b, k, p, N, T, z)

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