from art import logo
import os
print(logo)

dict_auction={}

# name=input("What is your name?: ")
# bid=int(input("What is your bid?: $"))

should_continue=True

while should_continue:
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: $"))
    dict_auction[name]=bid
    
    
    
    result=input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if result == 'no':
        should_continue= False


    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    

# print(dict_auction)

values=list(dict_auction.values())
max_value = max(values)

temp=values.index(max_value)

for i,n in enumerate(dict_auction):
    if i==temp:
        print(f"The winner is {n} with a bid of ${dict_auction[n]}")

