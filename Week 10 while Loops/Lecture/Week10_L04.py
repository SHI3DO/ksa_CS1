from cs1robots import *
load_world("./worlds/beepers3.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.3)

# 1: move until beepers are met
while not hubo.on_beeper():
    hubo.move()

# 2: pick up all the beepers
while hubo.on_beeper():
    hubo.pick_beeper()

hubo.move()