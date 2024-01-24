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
    num2 = random.randint (1,10)
    num3 = random.randint (1,30)

command = ("Find the number such that when " + num1 + " is subtracted from " + num2 + " times the number, the result is " + num3 + " more than twice the number")
print(command)
            

    




  
 
