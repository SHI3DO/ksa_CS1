from cs1robots import *
load_world("./worlds/wall1.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.2)

while hubo.front_is_clear():
    hubo.move()