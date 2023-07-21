#Hurdle 4
#Env- https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#In this activity, the height of the walls is not fixed and it varies dynamically

#Env: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# Need to go to hurdle3
# Here the place of walls is dynamic

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    
def pattern2():
    turn_left()
    while wall_on_right():
        move()

    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()
    
while at_goal()!=True:
    if front_is_clear():
        move()
    elif wall_in_front():
        pattern2()