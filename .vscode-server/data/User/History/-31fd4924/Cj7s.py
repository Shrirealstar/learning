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


sum = num2*num3+num1
sum2 = num2-1
final_sum = sum/sum2
print(final_sum,".2f")

