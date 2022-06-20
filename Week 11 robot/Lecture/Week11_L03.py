from cs1robots import *
load_world("./worlds/wall3.wld")

hubo = Robot(beepers = 1)
hubo.set_trace("blue")
hubo.set_pause(0.1)

def go_around_world():
    hubo.drop_beeper()
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


go_around_world()