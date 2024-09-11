from game_data import data
from art import logo
from art import vs
import random

score=0
temp=0
loop=True

rand1=random.randint(0,len(data)-1)

while loop:
    rand2=random.randint(0,len(data)-1)
    A=data[rand1]['follower_count']
    B=data[rand2]['follower_count']
    
    if A==B:
        rand2= rand2=random.randint(0,len(data)-1)
        B=data[rand2]['follower_count']
    
    print(logo)
    print(f"Compare A: {data[rand1]['name']}, a {data[rand1]['description']}, from {data[rand1]['country']}")
    print(vs)
    print(f"Against B: {data[rand2]['name']}, a {data[rand2]['description']}, from {data[rand2]['country']}")
    
    winner=input("Who has more followers? Type 'A' or 'B': ")
    print("\n"*20)
    
    
    if A>B and winner=='A':
        score+=1
        print(f"You're right! Current score: {score}.")    
        temp=rand2
    elif B>A and winner=='B':
        score+=1
        print(f"You're right! Current score: {score}.")
        temp=rand1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        loop=False
    rand1=temp
    