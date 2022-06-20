from cs1robots import *
create_world()
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.01)

def move9steps():
    for i in range(9):
        hubo.move() 

def zigzag():
    move9steps()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    move9steps()
    hubo.turn_right()
    hubo.move()
    hubo.turn_right()

def zigzagEntireWorld():
    # ADD ADDITIONAL CODE HERE!
    for i in range(4):
        zigzag()
    move9steps()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    move9steps()
    hubo.turn_left()
    move9steps()
    

zigzagEntireWorld()