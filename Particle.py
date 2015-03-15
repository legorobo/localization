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

    @x.setter
    def x(self, value):
        self.x = value

    @y.property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self.y = value

    @theta.property
    def theta(self):
        return self.theta

    @theta.setter
    def theta(self, value):
        self.theta = value

    @weight.property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value):
        self.weight = value

# ------------------------------------------------------------------------

    @classmethod
    def generate_random_set(cls, count, world):
        """
        Creates a set of particles evenly distributed across the world
        """

        return [cls(*world.random_open_position()) for _ in range(0, count)]

# ------------------------------------------------------------------------

    def landmark_direction(self, landmark):
        """
        Calculates the angle of the landmark relative to the robot's current
        directional vector

        NOTE THIS ASSUMES THAT THE ROBOT ROTATES WITH RESPECT TO THE POSITIVE
        X-AXIS

        POSITIVE IS A CCW ROTATION AND NEGATIVE IS A CW ROTATION
        """
        dx = landmark[0] - self.x
        dy = landmark[1] - self.y
        phi = math.atan2(dy / dx)

        return phi - theta
        

    def translate(self, x, y):
        """
        Translates the position of the particles
        """

        self.x += x
        self.y += y

    def iterate(self, velocity, checker):
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

