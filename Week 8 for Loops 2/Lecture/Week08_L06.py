from cs1robots import *
create_world()

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)


def move_world():
    for j in range(4):
        for i in range(9):
            hubo.move()
        hubo.turn_left()


move_world()

