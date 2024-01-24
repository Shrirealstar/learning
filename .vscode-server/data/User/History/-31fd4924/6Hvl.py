from random import randrange
import time

for num in range(1):
    num1 = randrange(2,20,2)
    a = str(num1)
    num2 = randrange(0,10,2)   
    b = str(num2)
    num3 = randrange(0,10,2)    
    c = str(num3)

command = ("Tom's age after "+a+" years will be "+b+" times his age "+c+" years back. What is the present age of Tom's?")
print(command)
time.sleep(5)

command1 = float(input("What will be the answer..? : "))
if command1 == "z":
    print("Right answer !!!")

else:
    time.sleep(3)
    print("close, but not correct...")

command3 = str(input("Do you want to know the answer ? (yes/no) : "))
print(command3)
time.sleep(3)

if command3 == "yes":
    sum = num2*num3+num1
    sum2 = num2-1
    final_sum = sum/sum2

    if final_sum < 0 & 1:
        print("ERROR !!!, please Re-Run the code...")

    else:
        sum = num2*num3+num1
        sum2 = num2-1
        final_sum = sum/sum2
        z = format(final_sum,".1f")
        print("Tom's present age is",z)

else:
    print("Thanks, Good luck...")
