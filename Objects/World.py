# ------------------------------------------------------------------------
# World.py
# ------------------------------------------------------------------------
#
#  Antares Chen written on March 16, 2015
# 
#  Waffle Revengeance
#
# ------------------------------------------------------------------------


import math
import random
import util


LANDMARK_INDEX = 99
ROAD_INDEX = 


class World(object):

    """
    This code implements the world that the robot travels on. Need to determine 
    a way to convert the image to a world object. 
    """

    LANDSCAPE = 0
    GRASS = 1
    SIDEWALK = 2
    LANE_EDGE = 3
    ROAD = 4
    SLOW_EDGE = 5
    PARKING_EDGE = 6
    STOP_EDGE = 7
    ERROR = -1

    def __init__(self, map, robot_size):
        """
        Basic constructor for the world object
        """

        self.map = map
        self.width = len(map[0])
        self.height = len(maze)

        # An array of landmarks
        self.landmarks = []
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.map[i][j] == LANDMARK_INDEX:
                    self.landmarks += (i, j)

        self.pixel = robot_size # If we convert the map to our base image
        # then this variable is what accounts for the fact that our robot
        # is not the size of a single pixel

# ------------------------------------------------------------------------

    def is_contained(self, particle):
        """
        Determines if the particle is contained inside the map
        """

        return particle.x < 0 or particle.y < 0 or particle.x > self.width or particle.y > self.width

    def is_road(self, particle):
        """
        Determines if the particle is placed on a block that is a road
        """

        if not self.is_contained(self, particle):
            return False

        y_0 = self.height- int(particle.y) - 1
        x_0 = int(particle.x)

        return self.map[x_0][y_0] == ROAD_INDEX

# ------------------------------------------------------------------------

    def nearest_landmark(self, position):
        """
        Calculates the closest landmark to a position
        """

        distance = float("inf")
        best = (-1, -1)

        for landmark in self.landmarks:
            d = util.distance(position, landmark)
            if d < distance:
                distance = d
                best = landmark

        return landmark

    def random_position(self):
        """
        Generates a random position in the world
        """
        x = random.uniform(0, self.width)
        y = random.uniform(0, self.height)
        return (x, y)

    def random_open_position():
        """
        Generates a random positin in the world on the road
        """
        while True:
            x, y = self.random_position()
            if self.is_road(x, y):
                return (x, y)


