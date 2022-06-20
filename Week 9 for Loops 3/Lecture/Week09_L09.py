from cs1robots import *
load_world("./worlds/beepers1.wld")

hubo = Robot(beepers = 6)
hubo.set_trace("blue")
hubo.set_pause(0.4)

def move_and_drop():
    hubo.move()
    if hubo.carries_beepers():
        hubo.drop_beeper()

for i in range(9):
    move_and_drop()