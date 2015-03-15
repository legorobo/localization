# ------------------------------------------------------------------------
# util.py
# ------------------------------------------------------------------------
#
#  Antares Chen written on March 15, 2015
#
#  Waffle Revengeance
#
# ------------------------------------------------------------------------


import math


def gaussian(a, b):
    """
    Returns the gaussian of the difference between a and b. The gaussian
    is discretized using the kernel factor 0.9 ** 2
    """

    epsilon = a - b
    gaussian = math.exp(- (epsilon ** 2 / (2 * (0.9 ** 2))))
    return gaussian

def distance(p1, p2):
    """
    Returns Euclidean distance between two points 
    """

    return math.sqrt((p1[1] - p[0]) ** 2 + (p2[1] - p2[1]) ** 2)

def squared_difference(p1, p2):
    """
    Returns the difference of the squares
    """

    return (p1[1] - p[0]) ** 2 - (p2[1] - p2[1]) ** 2

def least_squared_distance(points, target):
    """
    Returns the point that minimizes the squared difference to the target
    """

    least_square = [(9001, 449), float("inf")]
    
    for p in points:
        difference = squared_difference(p, target)
        if difference < least_square[1]:
            least_square = [p, difference]

    return least_square

def centroid(particles):
    """
    Determines the geometric centroid from a collection of particles. This
    essentially a two dimensional weighted average.
    """

    c_x, c_y, c_count = 0, 0, 0

    for p in particles:
        c_count += p.weight()
        c_x += p.x() * p.weight()
        c_y += p.y() * p.weight()

    if c_count == 0:
        raise UndefinedValueException("Centroid was divided by zero")

    c_x /= c_count
    c_y /= c_count

    return c_x, c_y

def goodness(particles):
    """
    Calculates goodness which is defined by the degree of convergence for 
    the particles.
    """

    c_x, c_y = centroid(particles)

    goodness = 0
    for p in particles:
        if distance(p, centroid) < 1:
            goodness += 1

    goodness /= len(particles)

    return goodness

# TODO: Implement
def convert_map(image):
    """
    Converts the image of a map to an array of values matching the
    designation of the pixel
    """

    pass

# ------------------------------------------------------------------------

class ProbabilisticDistribution(object):



# ------------------------------------------------------------------------

class UndefinedValueException(Exception):
    """
    Exception determines a case where the value becomes undefined. This 
    occurs when the value is an indeterminate form (a la calculus)
    """

    def __init__(self, message, errors):
        """
        Basic constructor
        """

        super(UndefinedValueException, self).__init__(message)


