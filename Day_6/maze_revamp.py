#This is the revamped code for maze.py
#Maze.py course is not working for some of the use cases. 
# So rectified the code accordingly and made respective changes 
#Working for all the possible cases
#Just had to add a check condition before running into an infinite loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()

count=0
    
while at_goal()!=True:
   if count<=10:
     if right_is_clear():
        turn_right()
        move()
        count+=1
        #print(count)
     else:
        if front_is_clear():
            move()
        else:
            turn_left()
            if front_is_clear()!=True:
                turn_left()
                move()
   else:
       count=0
       turn_right()
       move()
       move()