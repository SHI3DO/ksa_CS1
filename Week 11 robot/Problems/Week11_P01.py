from cs1robots import *
load_world("./worlds/maze.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)


def escape_maze():
    # ADD ADDITIONAL CODE HERE!
    hubo.move()

    while not hubo.on_beeper():
        if hubo.right_is_clear():
            hubo.turn_right()
            hubo.move()
        elif hubo.front_is_clear():
            hubo.move()
        else:   
            hubo.turn_left()
        
    hubo.pick_beeper()


escape_maze()
