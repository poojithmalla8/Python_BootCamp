age = input("What is your current age? ")

age=int(age)
k=90-age
x=k*365
#print(x)
y=round((x-k)/7)
#print(round(y))
z=round((x/365)*12)
#print(round(z))
print(f"You have {x} days, {y} weeks, and {z} months left.")