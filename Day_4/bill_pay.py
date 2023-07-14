#Input - Ross, Rachel, Monica, Chandler, Joey, Phoebe

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#print(names_string)
#print(names)
n=len(names)
num=random.randint(0,n)

print(f"{names[num]} is going to buy the meal today!")