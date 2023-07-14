rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
com_in=random.randint(0,2)
user_in=int(input("What do u choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_in==0:
    print("You Chose: \n",rock)
elif user_in==1:
    print("You Chose: \n",paper)
elif user_in==2:
    print("You Chose: \n",scissors)

if com_in== 0:
    print("Computer Chose: \n",rock)
elif com_in== 1:
    print("Computer Chose: \n",paper)
elif com_in== 2:
  print("Computer Chose: \n",scissors)
  
if user_in==0 and com_in==1:
    print("Computer wins")
elif user_in==2 and com_in==1:
    print("User Wins")
elif user_in==2 and com_in==0:
    print("You Lose")
elif user_in==1 and com_in==0:
    print("User wins")
elif user_in==1 and com_in==2:
    print("You Lose")
if user_in==0 and com_in==2:
    print("User wins")
elif user_in==com_in:
    print("Game Tied")