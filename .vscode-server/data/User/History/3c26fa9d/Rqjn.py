# Starting Numbers

import random

answer = (input("Ready!! for the question? (yes/no): "))
if answer == "yes":
    print("OK, here we go...")
    for num in range (1):
        num1 = random.randint (100,200)
        a = str(num1) 
        num2 = random.randint (5,10)
        b = str(num2)


    command = ("The sum of two numbers is " + a + " If one-third of the one exceeds one-seventh of the other by " + b + " find the smaller number.")
    print(command)

if answer == "no":
    print("Thank You, Bye") 

command1 = float(input("What is the answer?"))
if command1 == "sum4":
                print("Rigth answer !!!")

else:
    print("Close, but not correct...")


    ask = input("Do you want to know the answer? (yes/no): ")
    if ask == "yes":
            var = "x"

            command2 = ("Let the number be "+ var +" and ""("+a+" - "+var+")" " Then,")
            print(command2)

            sum = (var + "/3" + " - " + a + var + "/7 "+ "= " +b)
            print(sum)

            st1 = str(3)
            st2 = str(7)
            st3 = str(b)

            x = int(3)
            y = int(7)
            z = num2
            add = str(x+y)

            Mult = x*y*z
            multt = str(Mult)
            sum2 = (st2 +var +" - "+st1+" (" + a + " - " + var+ " )" + " = " + multt )
            print(sum2)

            sum3 = (num1*3) + Mult
            print( add + var+ " =",sum3)

            sum4 = (sum3/10)
            print(sum4)

    if ask == "no":
        print("OK, better luck next time...")



  
 
