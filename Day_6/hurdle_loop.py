#For these activities use the Reborg World in the website provided
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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
    
for n in range(0,6):
    pattern_1()