from art import logo
import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def array_sum(array):
    arrsum = 0
    for i in array:
        arrsum += i
    return arrsum


#   Select random from the cards
player= [random.choice(cards),random.choice(cards)]
print(f"Your cards {player}")
print(f"Player's Total ------------> {array_sum(player)}")

    

dealer=[random.choice(cards),random.choice(cards)]
print(f"Dealer's First Card: {dealer[0]} ")

if array_sum(player) == 21:
    print("BlackJack! You win!!")
    print(f"Player's Total ------------> {array_sum(player)}")
    exit()


choice= input("Do you wish to continue ? yes or no: ")

if choice == 'yes':
    choice = True
else:
    choice = False

while choice:
    temp=random.choice(cards)
    player.append(temp)
    print(f"Your cards {player}")
    print(f"Player's Total ------------> {array_sum(player)}")
    if array_sum(player) > 21:
        print("Busted ❌")
        print("Dealer Won")
        print(f"Dealers's Total ------------> {array_sum(dealer)}")
        print(f"Dealer's Cards: {dealer}")
        break
    elif input("Do you wish to continue ? yes or no: ")  == "no":
        if array_sum(player) < array_sum (dealer):
            print("Dealer Won")
            print(f"Dealer's Total ------------> {array_sum(dealer)}")
            print(f"Dealer's Cards: {dealer}")

        elif array_sum(player) > array_sum (dealer):
            print("Congratulations Player Won 🏆")
            print(f"Dealer's Total ------------> {array_sum(dealer)}")
            print(f"Dealer's Cards: {dealer}")

            choice=False

if array_sum(dealer) < 16:
    temp1=random.choice(cards)
    dealer.append(temp1)
    if (array_sum(dealer) > 21):
        print("Congratulations Player Won 🏆")
        print(f"Dealer's Total ------------> {array_sum(dealer)}")
        print(f"Dealer's Cards: {dealer}")

    if array_sum(dealer) < array_sum(player):
        print("Congratulations Player Won 🏆")
        print(f"Dealer's Total ------------> {array_sum(dealer)}")
        print(f"Dealer's Cards: {dealer}")


from art import logo
import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def array_sum(array):
    arrsum = 0
    for i in array:
        arrsum += i
    return arrsum


#   Select random from the cards
player= [random.choice(cards),random.choice(cards)]
print(f"Your cards {player}")
print(f"Player's Total ------------> {array_sum(player)}")

    

dealer=[random.choice(cards),random.choice(cards)]
print(f"Dealer's First Card: {dealer[0]} ")

if array_sum(player) == 21:
    print("BlackJack! You win!!")
    print(f"Player's Total ------------> {array_sum(player)}")
    exit()


choice= input("Do you wish to continue ? yes or no: ")

if choice == 'yes':
    choice = True
else:
    choice = False

while choice:
    temp=random.choice(cards)
    player.append(temp)
    print(f"Your cards {player}")
    print(f"Player's Total ------------> {array_sum(player)}")
    if array_sum(player) > 21:
        print("Busted ❌")
        print("Dealer Won")
        print(f"Player's Total ------------> {array_sum(player)}")
        print(f"Dealers's Total ------------> {array_sum(dealer)}")
        print(f"Dealer's Cards: {dealer}")
        break
    elif input("Do you wish to continue ? yes or no: ")  == "no":
        if array_sum(player) < array_sum (dealer):
            print("Dealer Won")
            print(f"Dealer's Total ------------> {array_sum(dealer)}")
            print(f"Player's Total ------------> {array_sum(player)}")
            print(f"Dealer's Cards: {dealer}")

        elif array_sum(player) > array_sum (dealer):
            print("Congratulations Player Won 🏆")
            print(f"Player's Total ------------> {array_sum(player)}")
            print(f"Dealer's Total ------------> {array_sum(dealer)}")
            print(f"Dealer's Cards: {dealer}")

            choice=False

if array_sum(dealer) < 16:
    temp1=random.choice(cards)
    dealer.append(temp1)
    if (array_sum(dealer) > 21):
        print("Congratulations Player Won 🏆")
        print(f"Player's Total ------------> {array_sum(player)}")
        print(f"Dealer's Total ------------> {array_sum(dealer)}")
        print(f"Dealer's Cards: {dealer}")

    if array_sum(dealer) < array_sum(player):
        print("Congratulations Player Won 🏆")
        print(f"Player's Total ------------> {array_sum(player)}")
        print(f"Dealer's Total ------------> {array_sum(dealer)}")
        print(f"Dealer's Cards: {dealer}")


if array_sum(dealer) == array_sum(player):
    print(f"Common Total ------------> {array_sum(player)}")
    print(f"Dealer's Cards: {dealer}")
    print("Draw 😎")
    
from art import logo
import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def array_sum(array):
    arrsum = 0
    for i in array:
        arrsum += i
    return arrsum


#   Select random from the cards
player= [random.choice(cards),random.choice(cards)]
print(f"Your cards {player}")
print(f"Player's Total ------------> {array_sum(player)}")

    

dealer=[random.choice(cards),random.choice(cards)]
print(f"Dealer's First Card: {dealer[0]} ")

if array_sum(player) == 21:
    print("BlackJack! You win!!")
    print(f"Player's Total ------------> {array_sum(player)}")
    exit()


choice= input("Do you wish to continue ? yes or no: ")

if choice == 'yes':
    choice = True
else:
    choice = False

while choice:
    temp=random.choice(cards)
    player.append(temp)
    print(f"Your cards {player}")
    print(f"Player's Total ------------> {array_sum(player)}")
    if array_sum(player) > 21:
        print("Busted ❌")
        print("Dealer Won")
        print(f"Player's Total ------------> {array_sum(player)}")
        print(f"Dealers's Total ------------> {array_sum(dealer)}")
        print(f"Dealer's Cards: {dealer}")
        break
    elif input("Do you wish to continue ? yes or no: ")  == "no":
        if array_sum(player) < array_sum (dealer):
            print("Dealer Won")
            print(f"Dealer's Total ------------> {array_sum(dealer)}")
            print(f"Player's Total ------------> {array_sum(player)}")
            print(f"Dealer's Cards: {dealer}")

        elif array_sum(player) > array_sum (dealer):
            print("Congratulations Player Won 🏆")
            print(f"Player's Total ------------> {array_sum(player)}")
            print(f"Dealer's Total ------------> {array_sum(dealer)}")
            print(f"Dealer's Cards: {dealer}")

            choice=False

if array_sum(dealer) < 17:
    temp1=random.choice(cards)
    dealer.append(temp1)
    if (array_sum(dealer) > 21):
        print("Congratulations Player Won 🏆")
        print(f"Player's Total ------------> {array_sum(player)}")
        print(f"Dealer's Total ------------> {array_sum(dealer)}")
        print(f"Dealer's Cards: {dealer}")

    if array_sum(dealer) < array_sum(player):
        print("Congratulations Player Won 🏆")
        print(f"Player's Total ------------> {array_sum(player)}")
        print(f"Dealer's Total ------------> {array_sum(dealer)}")
        print(f"Dealer's Cards: {dealer}")


    if array_sum(dealer) > 21 and array_sum(player) > 21:
        print(f"Common Total ------------> {array_sum(player)}")
        print(f"Dealer's Cards: {dealer}")
        print("Draw 😎")
        print("Both Busted ❌")
        