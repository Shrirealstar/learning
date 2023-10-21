import random

answer = (input("Ready!! for the question? (yes/no): "))
if answer == "yes":
    print("OK, here we go...")
else :
    print("Thank You, Bye") 

for num in range (2):
    num1 = random.randint (1,50)
    a = str(num1) 
    num2 = random.randint (1,10)
    b = str(num2)

    print(num1, num2)
   
