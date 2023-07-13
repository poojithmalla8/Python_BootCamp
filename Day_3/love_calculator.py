# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=str.lower(name1)
name2=str.lower(name2)
#tc=rc=uc=ec1=lc=oc=vc=ec2=0
#Counting the number of letters

#TRUE Counter
tc=str.count(name1,'t')
tc=tc+str.count(name2,'t')
rc=str.count(name1,'r')
rc=rc+str.count(name2,'r')
uc=str.count(name1,'u')
uc=uc+str.count(name2,'u')
ec1=str.count(name1,'e')
ec1=ec1+str.count(name2,'e')
true=tc+rc+uc+ec1

#LOVE Counters
lc=str.count(name1,'l')
lc=lc+str.count(name2,'l')
oc=str.count(name1,'o')
oc=oc+str.count(name2,'o')
vc=str.count(name1,'v')
vc=vc+str.count(name2,'v')
ec2=str.count(name1,'e')
ec2=ec2+str.count(name2,'e')
love=lc+oc+vc+ec2

total=(true*10)+(love)

if total<10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total>=40 and total<=50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
