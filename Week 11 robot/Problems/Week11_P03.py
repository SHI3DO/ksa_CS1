import time
from cs1robots import *

load_world("./worlds/window1.wld")

hubo = Robot(beepers = 100)

# put hubo in front of the door
hubo.turn_left()
for i in range(5):
    hubo.move()
hubo.turn_right()
hubo.move()
time.sleep(1)
hubo.set_trace("blue")
hubo.set_pause(0.1)


def close_windows():
    hubo.move()
    hubo.drop_beeper()
    hubo.turn_right()
    hubo.move()

    # ADD ADDITIONAL CODE HERE!
    """
    while not hubo.on_beeper():
        if hubo.front_is_clear():
            if hubo.right_is_clear():
                hubo.drop_beeper()
            hubo.move()
        else:    # wall reached
            hubo.turn_left()
    """
    while not hubo.on_beeper():
        if hubo.right_is_clear():
            hubo.drop_beeper()
            hubo.move()
        elif hubo.front_is_clear():
            hubo.move()
        else:   
            hubo.turn_left()
    
    hubo.pick_beeper()
    hubo.turn_right()


close_windows()