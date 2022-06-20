from cs1robots import *
create_world(avenues = 9, streets = 9)
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.02)


def zigzagEntireWorld():
    hubo.turn_right()
    # ADD ADDITIONAL CODE HERE!
    for n in range(1,9):
        if n%2 == 1:
            hubo.turn_left()
            hubo.move()
            hubo.turn_left()
            for k in range(n): 
                hubo.move()
            hubo.turn_left()
            for k in range(n): 
                hubo.move()
        else:
            hubo.turn_right()
            hubo.move()
            hubo.turn_right()
            for k in range(n): 
                hubo.move()
            hubo.turn_right()
            for k in range(n): 
                hubo.move()
        
        
zigzagEntireWorld()