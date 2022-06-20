from cs1robots import *
create_world()

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.5)


def move_square():
    for i in range(4):
        hubo.move()
        hubo.turn_left()


move_square()