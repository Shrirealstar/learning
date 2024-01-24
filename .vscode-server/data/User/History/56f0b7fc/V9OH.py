import random


answer = (input("Ready!! for the question? (yes/no): "))
if answer == "yes":
    print("OK, here we go...")
    for num in range (1):
            num1 = random.randint (1,50)
            a = str(num1) 
            num2 = random.randint (5,10)
            b = str(num2)

            ques = ("The diffrence of two numbers is " + a + " and one-fifth of their sum is " + b + " Find the numbers.")
            print(ques)
else :
    print("Thank You, Bye") 

ask = int(input("What is the answer...? : "))


n = "x"
n1 = "y"
command = ("Let the numbers be " + n + " and " + n1+ " Then,")
print(command)

condition1 = (n + " - " + n1 +" = " + a + " ...(i)" )
print(condition1)

sum = 5*num2
sum1 = str(sum)
condition2 = ("and  1/5 ("+ n +" + "+ n1 +") = "+b + " ...(ii)" + " => "+n + " + "+n1 +" = " + sum1)
print(condition2)

sum2 = sum1+a
print(sum2)
sum3 = sum2/2
print(sum3)
sum4 = str(sum3)
command1 = ("Adding (i) & (ii) we get "+ n + " = "+ sum4)


