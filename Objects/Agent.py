# ------------------------------------------------------------------------
# Robot.py
# ------------------------------------------------------------------------
#
#  Antares Chen written on March 16, 2015
# 
#  Waffle Revengeance
#
# ------------------------------------------------------------------------

from .. import 
import Particle
import random
import math


"""
Imports to uncomment when they are implemented

from Sensors import Color
from Sensors import Gyro
from Sensors import UltraSonic
import Motor
"""

print("HI")
class Agent(Particle): 

    """
    Represents the behavior of the robot as it traverses through the filter

    TODO:   implement how the color sensor will determine the direction of 
            the robot
    """

    def __init__(self, world, start_position, bearing):
        super(Agent, self).__init__(*start_position, theta=bearing)
        self.world = world
        # self.velocity = Motor.speed()
        self.step_count = 0

# ------------------------------------------------------------------------

    def update_theta(self):
        """
        Updates the robot's direction angle from the Gyroscope

        TODO: Implementation depending on Sensors/Motors package
        """

        # self.theta = Gyro.read()

    def update_v(self):
        """
        Updates the robot's velocity from the Motor
        
        TODO: Implementation depending on Sensors/Motors package
        """

        # self.velocity Motor.speed()

    def update_omega(self):
        """
        Updates the robot's omega from the Motor
        """

        pass

    def read_landmark_distance(self):
        """
        Points the ultrasonic sensor and reads the distance to the nearest
        landmark

        TODO: Implementation depending on Sensors/Motors package
        """

        sensor_angle = self.landmark_direction(world.nearest_landmark((self.x, self.y)))

        # UltraSonic.change_direction(sensot_angle)
        # return UltraSonic.read()

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

    def iterate(self):
        while True:
            self.step_count += 1
            checker_function = lambda r, dx, dy: maze.is_road(r.x + dx, r.y + dy)
            
            if self.iterate(self.velocity, checker = checker_function):
                break
            
            self.update_theta()
            self.update_velocity()

# ------------------------------------------------------------------------







