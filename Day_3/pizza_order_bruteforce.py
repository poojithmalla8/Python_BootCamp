# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cost1=0
cost2=0
cost3=0
#Get Size of the Pizza Data
if size == 'S':
    cost1=15
elif size == 'M':
    cost1=20
elif size == 'L':
    cost1=25
else:
    print("Enter valid pizza size")

#Get Pepporoni Toppings details
if size == 'S' and add_pepperoni == "Y":
    cost2=2
elif size == 'M' and add_pepperoni=="Y":
    cost2=3
elif size == 'L' and add_pepperoni=="Y":
    cost2=3
else:
    cost2=0

#Get Extra Cheese Details
if size == 'S' or size == 'M' or size == 'L':
    if extra_cheese == 'Y':
        cost3=1
    else:
        cost3=0
total=cost1+cost2+cost3

print(f"Your final bill is: ${total}")