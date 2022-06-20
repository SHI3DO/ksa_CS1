from cs1robots import *
load_world("./worlds/beepers1-2.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.3)

def move_and_pick():
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()

for i in range(9):
    move_and_pick()