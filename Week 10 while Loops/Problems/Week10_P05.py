from cs1robots import *
load_world("worlds/beepers7.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)

def collect_garbages():
    # move to the right wall while collecting beepers
    for i in range(9):
        hubo.move()
        while hubo.on_beeper():
            hubo.pick_beeper()
        
    # turn back
    hubo.turn_left()
    hubo.turn_left()
    
    # move to the left wall
    for i in range(9):
        hubo.move()
        
    # move upwards
    hubo.turn_right()
    hubo.move()
    
    # put all the beepers down
    while hubo.carries_beepers():
        hubo.drop_beeper()
        
    # move to the starting position
    hubo.turn_left()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()


collect_garbages()
