from cs1robots import *
load_world("./worlds/beepers2.wld")

hubo = Robot(beepers = 50)
hubo.set_trace("blue")
hubo.set_pause(0.5)

hubo.move()
hubo.move()
while hubo.carries_beepers():
    hubo.drop_beeper()
hubo.move()