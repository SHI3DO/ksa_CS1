from cs1robots import *
load_world("./worlds/beepers4.wld")
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)

def move_and_pick():
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()


def walk_square_picking_all_beepers():
    # ADD ADDITIONAL CODE HERE!
    for i in range(4):
        for j in range(9):
            move_and_pick()
        hubo.turn_left()


walk_square_picking_all_beepers()