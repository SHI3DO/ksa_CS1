from cs1robots import *
create_world(avenues = 9, streets = 9)
hubo = Robot()
hubo.set_trace("blue")
#hubo.set_pause(0.02)

def moveNsteps(n):
    for i in range(n):
        hubo.move()    
        
def zigzagEntireWorld():
    hubo.turn_right()
    # ADD ADDITIONAL CODE HERE!
    for n in range(1,9):
        if n%2 == 1:
            hubo.turn_left()
            hubo.move()
            hubo.turn_left()
            moveNsteps(n)
            hubo.turn_left()
            moveNsteps(n)
        else:
            hubo.turn_right()
            hubo.move()
            hubo.turn_right()
            moveNsteps(n)
            hubo.turn_right()
            moveNsteps(n)
        
        
zigzagEntireWorld()