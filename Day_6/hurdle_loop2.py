#In this hurdle, the goal point is not fixed.
#Check the env in https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
#Go to Hurdle Env 2 (Hurdle 2)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
     
def pattern_1():
    move()
    turn_left()
    turn_around
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal()!= True: #or while not at_goal():
    pattern_1()
    