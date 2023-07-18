#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_size=nr_letters+nr_numbers+nr_symbols

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

'''
password=''
for char in range(0,nr_letters):
        password=password+random.choice(letters)
#print(password)
for sym in range(0,nr_symbols):
    password+=random.choice(symbols)
#print(password)
for numb in range(0,nr_numbers):
    password+=random.choice(numbers)
print(password)
'''

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#for n in range(0,pass_size):

password_list=[]
for char in range(0,nr_letters):
        password_list.append(random.choice(letters))
#print(password)
for sym in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
#print(password)
for numb in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
fin_pass=""
print(fin_pass.join(password_list))