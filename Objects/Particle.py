# ------------------------------------------------------------------------
# Particle.py
# ------------------------------------------------------------------------
#
#  Antares Chen written on March 15, 2015
# 
#  Waffle Revengeance
#
# ------------------------------------------------------------------------


import random
import math
import util


class Particle(object):

    """
    The particle object is used as a random pinpoint to perform a hypothesis
    test. We begin with the hypothesis that the robot is at the particles's 
    locations and generate the distribution of probabilities.
    """


    def __init__(self, x, y, theta=None, weight=1):
        """
        Basic constructor for the Particle object. It takes in the cartesian
        coordinates x,y along with the heading theta, and weight.
        """

        if theta == None:
            theta = random.uniform(0, 360)

        self.x = x
        self.y = y
        self.theta = theta
        self.weight = weight

    def __repr__(self):
        return "(x = %f, y = %f, theta = %f, weight = %f)" % (x, y, theta, weight)

# ------------------------------------------------------------------------

    @x.property
    def x(self):
        return self.x

    @y.property
    def y(self):
        return self.y

    @theta.property
    def theta(self):
        return self.theta

    @weight.property
    def weight(self):
        return self.weight

# ------------------------------------------------------------------------

    @classmethod
    def generate_random_set(cls, count, world):
        """
        Creates a set of particles evenly distributed across the world
        """

        return [cls(*world.random_open_position()) for _ in range(0, count)]

    @classmethod
    def generate_initial_set(cls, count, world, position):
        """
        Creates the initial set of particles at position tuple (x,y)
        """

        return [cls(*position) for _ in range(0, count)]

# ------------------------------------------------------------------------

    def translate(self, x, y):
        """
        Translates the position of the particles
        """

        self.x += x
        self.y += y

    def iterate(self, velocity, checker = None):
        """
        Calculates the position of the particle during the next iteration. 
        Returns if the particles are moved
        """

        theta = self.theta

        # Calculate the deltas to translate the particles by
        theta_r = math.radians(theta)
        dx = math.sin(theta_r) * velocity
        dy = math.sin(theta_r) * velocity

        if checker is None or checker(self, dx, dy):
            self.translate(dx, dy)
            return True

        return False

# ------------------------------------------------------------------------

