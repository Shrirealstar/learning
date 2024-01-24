# Starting Numbers

import random
from re import A

answer = (input("Ready!! for the question? (yes/no): "))
if answer == "yes":
    print("OK, here we go...")
else :
    print("Thank You, Bye")

for num in range (1):
    num1 = random.randint (1,50)
    a = str(num1) 
    num2 = random.randint (1,10)
    b = str(num2)
    num3 = random.randint (1,30)
    c = str(num3)

command = ("Find the number such that when " + a + " is subtracted from " + b + " times the number, the result is " + c + " more than twice the number")
print(command)

ask = int(input("What is your answer ? : "))
if ask == "sum2":
    print("Write Answer !!!")
else :
    print("Close but not correct..")


ask1 = input(("Do you want to know the answer? (yes/no)"))
if ask1 == "yes":
    print("OK, here we go...")
else :
    print("Ok, Best of luck")

var = (" x ")
step1 = ("Let the number be" + var)
print(step1)
step2 = ("Then, "+b+var+"- "+a+" ="+" 2"+var+"+ "+c)
int = int(2)
print(step2)
sum = num2 - int
sum1 = num1+num3
print(sum,var + "=", sum1)
sum2 = sum1/sum
print(sum2)


    




  
 
