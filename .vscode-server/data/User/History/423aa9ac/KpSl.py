import math
import random

for num in range(1):
    num1 = random.randint (35,50)
    num2 = random.randint (200,500)
    a = str(num1)
    b = str(num2)

command = ("If the the sum of two numbers is " + a + " and their product is " + b +" then find the absolute diffrence between the numbers")
print(command)

ask = int(input("What is the diffrence..?"))
if ask == "sum1":
    print("Right answer!!!")

    

    sum = num1**2 - 4*num2
    sum1 = math.sqrt(sum)
    x = format(sum1,".2f")

    print("Required diffrence = "+ x)

else:
    print("Close but not correct...")