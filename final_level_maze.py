def turn_around():
    turn_left()
    turn_left()

def turn_right():
     turn_left()
     turn_left()
     turn_left()

while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()