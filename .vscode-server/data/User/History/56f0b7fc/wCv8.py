import random

answer = (input("Ready!! for the question? (yes/no): "))
if answer == "yes":
    print("OK, here we go...")
    for num in range (1):
            num1 = random.randint (1,50)
            a = str(num1) 
            num2 = random.randint (1,10)
            b = str(num2)

            ques = ("The diffrence of two numbers is " + a + " and one-fifth of their sum is " + b + " Find the numbers.")
            print(ques)
else :
    print("Thank You, Bye") 

    

   
