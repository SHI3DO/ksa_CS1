from cs1robots import *
load_world("./worlds/beepers5.wld")

hubo = Robot()
for i in range(4): hubo.move()
hubo.turn_left()
for i in range(4): hubo.move()
hubo.turn_right()

hubo.set_trace("blue")
#hubo.set_pause(0.02)


def move_and_pick():
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()

def whirl_picking_all_beepers():
    # ADD ADDITIONAL CODE HERE!
    for n in range(1,10):
        for i in range(n):
            move_and_pick()
        hubo.turn_left()
        for i in range(n):
            move_and_pick()
        hubo.turn_left()
    for i in range(9):
        move_and_pick() 


whirl_picking_all_beepers()