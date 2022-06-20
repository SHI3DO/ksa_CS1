import time
from cs1robots import *

load_world("./worlds/window2.wld")

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
    # ADD ADDITIONAL CODE HERE!
    hubo.move()
    hubo.drop_beeper()
    hubo.turn_right()
    hubo.move()
    """
    while not hubo.on_beeper():
        if hubo.front_is_clear():
            if hubo.right_is_clear():
                hubo.turn_right()
                hubo.move()
                if hubo.right_is_clear():
                    # step back
                    hubo.turn_left()
                    hubo.turn_left()
                    hubo.move()
                    hubo.turn_right()
                    hubo.drop_beeper()
                    hubo.move()
            else: hubo.move()
        elif hubo.right_is_clear():
                hubo.turn_right()
                hubo.move()
        else:    # wall reached
            hubo.turn_left()    
    """
    while not hubo.on_beeper():
        if hubo.right_is_clear():
            hubo.turn_right()
            hubo.move()
            if hubo.right_is_clear():
                # step back
                hubo.turn_left()
                hubo.turn_left()
                hubo.move()
                hubo.turn_right()
                hubo.drop_beeper()
                hubo.move()
        elif hubo.front_is_clear():
            hubo.move()
        else:
            hubo.turn_left()
            
    hubo.pick_beeper()
    hubo.turn_right()


close_windows()