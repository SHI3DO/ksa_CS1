from cs1robots import *
create_world()

hubo = Robot(beepers = 100)
for i in range(4): hubo.move()
hubo.turn_left()
for i in range(4): hubo.move()
hubo.turn_right()

#hubo.set_trace("blue")
#hubo.set_pause(0.02)


def move_and_drop():
    hubo.move()
    if hubo.carries_beepers():
        hubo.drop_beeper()

def whirl_dropping_beepers():
    # ADD ADDITIONAL CODE HERE!
    for n in range(1,10):
        for i in range(n):
            move_and_drop()
        hubo.turn_left()
    for n in range(9):
        move_and_drop()


whirl_dropping_beepers()