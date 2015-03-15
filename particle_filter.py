# ------------------------------------------------------------------------
# particle_filter.py
# ------------------------------------------------------------------------
#
#  Antares Chen written on March 16, 2015
# 
#  Waffle Revengeance
#
# ------------------------------------------------------------------------


from Objects import *
import util
import random
import math


PARTICLE_COUNT = 2000


# TODO: Implement world map converted
world = util.convert_map(None)
particles = Particle.generate_random_set(PARTICLE_COUNT, world)
agent = Agent(world)


def run():
    """
    Implements the particle filter algorithm. It runs on an infinite loop.
    """

    while True:
        # Determine the distance to the nearest landmark
        agent_distance = agent.read_landmark_distance()

        # Update the particle weights accordingly
        for p in particles:
            if world.is_road(p):
                # Instead of calculating the distance between nearest 
                # landmark relative to p, maybe do it to agent?
                p_distance = util.distance(p, world.nearest_landmark(p))
                p.weight = util.gaussian(agent_distance, p_distance)
            else:
                p.weight = 0

        # Find centroid and goodness
        c_x, c_y = util.centroid(particles)
        goodness = util.goodness(particles)

        # Resample particles
        particles_new = []

        # Normalize weights
        alpha = sum(p.weight for p in particles)
        if alpha: 
            for p in particles:
                p.weight /= alpha

        # Create the new distribution of particles
        distribution = util.ProbabilisticDistribution(particles)
        for _ in particles:
            p = distribution.value()
            
            try:
                # Generate the new particle
                p_new = Particle(p.x, p.y, theta = agent.theta)
            except util.UndefinedValueException:
                # Do it randomly if something breaks
                p_new = Particle.generate_random_set(1, world)[0]

            particles_new.append(p_new)

        # Advance all objects
        theta_0 = agent.theta
        agent.iterate()
        dtheta = agent.theta - theta_0

        for p in particles:
            p.theta += dtheta
            p.iterate(agent.velocity)






