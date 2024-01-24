# Starting Numbers

import random
from re import A

answer = (input("Ready!! for the question? (yes/no): "))
if answer == "yes":
    print("OK")
else :
    print("Tank You, Bye")

for num in range (1):
    a = int(random.randint (1,50))
    b = int(random.randint (1,10))
    c = int(random.randint (1,30))

command = ("Find the number such that when " + a + " is subtracted from " + b + " times the number, the result is " + c + " more than twice the number")
print(command)
            

    




  
 
