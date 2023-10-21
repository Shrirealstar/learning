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

ask = input("Do you want to know the answer...? (yes/no) : ") 
if ask == "yes":
    n = "x"
    n1 = "y"
    command = ("Let the numbers be " + n + " and " + n1+ " Then,")
    print(command)

    condition1 = (n + " - " + n1 +" = " + a + " ...(i)" )
    print(condition1)

    sum = 5*num2
    sum1 = str(sum)
    condition2 = ("and  1/5 ("+ n +" + "+ n1 +") = "+b + " => "+n + " + "+n1 +" = " + sum1 + " ...(ii)")
    print(condition2)

    sum2 = sum+num1
    sum3 = sum2/2
    sum4 = str(sum3)
    command1 = ("Adding (i) & (ii) we get "+ n + " = "+ sum4)
    print(command1)

    sum5 = sum-sum3
    sum6 = str(sum5)
    command2 = ("Putting x = " + sum4 +" in (i), we get y = "+ sum6)
    print(command2)

    final_command = ("Hence, the numbers are "+ sum4 + " and " + sum6)
    print(final_command)

else:
    print("OK, Good Luck")






