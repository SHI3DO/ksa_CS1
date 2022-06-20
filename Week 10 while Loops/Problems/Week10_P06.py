from cs1robots import *

create_world()
hubo = Robot(beepers = 100)

# put hubo to the right wall
hubo.set_pause(0.1)
while hubo.front_is_clear(): hubo.move()
hubo.turn_left() ; hubo.turn_left()


def putNumber(num):
    # ADD ADDITIONAL CODE HERE!
    while num > 0:
        digit = num % 10
        num = num // 10

        for i in range(digit):
            hubo.drop_beeper()
        hubo.move()


putNumber(2291)