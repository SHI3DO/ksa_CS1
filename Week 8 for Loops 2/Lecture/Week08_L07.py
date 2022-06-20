from cs1robots import *
load_world("./worlds/stairs.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.2)

def climb_up_stairs():
    hubo.move()
    for i in range(4):
        hubo.turn_left()
        hubo.move()   # vertical move
        hubo.turn_right() 
        hubo.move()   # horizontal moves
        hubo.move()


climb_up_stairs()