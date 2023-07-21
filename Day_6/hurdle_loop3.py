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
     
def pattern1():
    move()
    turn_left()
    turn_around
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def pattern2():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
while at_goal()!=True:
    if front_is_clear():
        move()
    elif wall_in_front():
        pattern2()