import util
import Simulation

def test():
    file_name = "map.png"
    array = util.convert_map_to_array(util.convert_map(file_name))
    with open("map.in", "w") as f:
        for thing in array:
            for thingy in thing:
                f.write(str(thingy) +" ")
            f.write("\n")
        f.close()
    


GREEN = (59, 152, 95)
GRAY = (160, 160, 160)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 216, 0)
BLUE = (0, 28, 255)
RED = (127, 0, 0)



# def test2():
#     file_name = "map.png"
#     pic = util.convert_map(file_name)
#     Simulation.show(pic)

test()    


"""
One pixel represents one square centimeter

Robot takes up (x, y) = (29, 15)
"""
