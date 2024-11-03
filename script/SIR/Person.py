"""
This file defines a class Person that will be used in the discrete case simulations for the disease-spread model.
Note: this version doesn't have any variations
"""
class Person():
    """
    Class Person has three parameters:
    susceptible(default to True):            if a person could be infected
    infectious(default to False):            a person is infected and can infect others
    removed(default to False):               a person was once infected, but infection is now removed

    Class Person has two methods:
    infect:
    If a person is susceptible, infect this person by setting their parameter "infectious" to true.

    remove:
    If a person is infectious, remove their infection by setting the parameter "infectious" to false,
    parameter "susceptible" to false, and parameter "removed" to true.
    """

    def __init__(self):
        # At the start: everyone is not infected, can be infected, and is not cured
        self.susceptible = True     # If this person can be infected
        self.infectious = False     # If this person is infected
        self.removed = False        # If this person is cured

    def is_infected(self):
        # Return true if this person is infected
        return self.infectious

    def is_susceptible(self):
        # Return true if this person is susceptible
        return self.susceptible

    def is_removed(self):
        # Return true if this person is cured
        return self.removed

    def infect(self):
        """
        If this person can be infected, change the parameter to be true
        """
        if self.susceptible:
            self.infectious = True
            self.susceptible = False # Once this person is infected, they can't be infected anymore

    def remove(self):
        """
        Once this person is cured, they are no longer infected, and can't be infected anymore
        """
        if self.infectious:
            self.infectious = False
            self.susceptible = False
            self.removed = True