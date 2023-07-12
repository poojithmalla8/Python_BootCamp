height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height=eval(height)
weight=eval(weight)
BMI= (weight)/(height * height)
print(round(BMI))