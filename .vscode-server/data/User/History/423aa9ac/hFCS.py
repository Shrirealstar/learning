from cmath import sqrt
import random

for num in range(1):
    num1 = random.randfloat(1,50)
    num2 = random.randfloat(1,500)
    a = str(num1)
    b = str(num2)

command = ("If the the sum of two numbers is " + a + " and their product is " + b +" then find the absolute diffrence between the numbers")
print(command)

sum = sqrt(num1**2)
print(sum)