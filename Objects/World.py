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

LANDMARK_INDEX = 0
GRASS_INDEX = 1
SIDEWALK_INDEX = 2
LANE_EDGE_INDEX = 3
ROAD_INDEX = 4
SLOW_EDGE_INDEX = 5
PARKING_EDGE_INDEX = 6
STOP_EDGE_INDEX = 7
ERROR = -1

class World(object):

    """
    This code implements the world that the robot travels on. Need to determine 
    a way to convert the image to a world object. 
    """

    LANDMARK = 0
    GRASS = 1
    SIDEWALK = 2
    LANE_EDGE = 3
    ROAD = 4
    SLOW_EDGE = 5
    PARKING_EDGE = 6
    STOP_EDGE = 7
    ERROR = -1

    def __init__(self, city_map, robot_size):

        """
        Basic constructor for the world object
        """

        self.map = city_map
        self.width = len(city_map[0])
        self.height = len(city_map)

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

    def is_index(self, particle, index):
        """
        Determines if the particle is placed on a block that is a road
        """

        if not self.is_contained(self, particle):
            return False

        y_0 = self.height- int(particle.y) - 1
        x_0 = int(particle.x)

        return self.map[x_0][y_0] == index

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
            if self.is_index(x, y, ROAD):
                return (x, y)


