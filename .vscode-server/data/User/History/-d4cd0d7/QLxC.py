import random
ask = str(input("What is the Name of your father : "))
print("Your father's age is How many years more than how many time the age of your's ?")
a = int(input("Years : "))
b = int(input("Times : "))

for num in range(1):
    num1 = random.randint(5,15)
    c = str(num1)

ask1 = ("Three years hence, your's father's age will be "+c+" years more than twice the age of the yours")
print(ask1)

sum = b+a # 1 number
sum1 = 2*3 + num1 # 2 number
print("x =",sum1-sum)
sum2 = sum1-sum
sum3 = sum2*3+3
print(ask+"'s age is",sum3)