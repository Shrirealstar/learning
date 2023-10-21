from random import randrange

for num in range(1):
    num1 = randrange(2,20,2)
    a = str(num1)
    num2 = randrange(0,10,2)   
    b = str(num2)
    num3 = randrange(0,10,2)    
    c = str(num3)

command = ("Tom's age after "+a+" years will be "+b+" times his age "+c+" years back. What is the present age of Tom's?")
print(command)

command1 = float(input("What will be the answer... : ")
sum = num2*num3+num1
sum2 = num2-1
final_sum = sum/sum2

if final_sum < 0 & 1:
    print("ERROR !!!, please Re-Run the code...")

else:
    sum = num2*num3+num1
    sum2 = num2-1
    final_sum = sum/sum2
    z = format(final_sum,".f")
    print("Tom's present age is",z)