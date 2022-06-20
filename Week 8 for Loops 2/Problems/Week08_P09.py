from cs1robots import *
create_world()
hubo = Robot()
for i in range(4): hubo.move()
hubo.turn_left()
for i in range(4): hubo.move()
hubo.turn_right()

hubo.set_trace("blue")
hubo.set_pause(0.02)

def moveNsteps(n):
    for i in range(n):
        hubo.move()    

def whirlEntireWorld():
    # ADD ADDITIONAL CODE HERE!
    for n in range(1,10):
        for i in range(n):
            hubo.move()
        hubo.turn_left()
        for i in range(n):
            hubo.move()
        hubo.turn_left()
    for i in range(9):
        hubo.move()    


whirlEntireWorld()