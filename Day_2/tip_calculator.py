#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


bill_amt=eval(input("Enter the bill amount: $"))
people=int(input("Total number of people at the table: "))
tip=int(input("Enter the tip percentage that you would like to pay:"))
share= (bill_amt/people) * ((100+tip)/100)
#print(share)
print(round(share,2))