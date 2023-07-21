#Env- Maze
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#Here the env is constant but the robot direction is dynamic


def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal()!=True:
    if right_is_clear():
        turn_right()
        move()
    else:
        if front_is_clear():
            move()
        else:
            turn_left()
            if front_is_clear()!=True:
                turn_left()
                move()
                