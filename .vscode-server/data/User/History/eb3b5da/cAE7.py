# Starting Numbers

import random
from re import A

answer = (input("Ready!! for the question? (yes/no): "))
if answer == "yes":
    print("OK")
else :
    print("Tank You, Bye")

for num in range (1):
    num1 = random.randint (1,50)
    a = str(num1) 
    print(a)
    num2 = random.randint (1,10)
    b = str(num2)
    print(b)
    num3 = random.randint (1,30)
    c = str(num3)
    print(c)

command = ("Find the number such that when " + a + " is subtracted from " + b + " times the number, the result is " + c + " more than twice the number")
print(command)
            

    




  
 
