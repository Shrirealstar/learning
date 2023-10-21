import random

a = str(input("Enter the elder persons Name : "))
b = str(input("Enter the  younger persons Name : "))
c = str(input("What is the age difference? : "))
f = int(c)

command = (a+"'s age and "+b+"'s age is differ by "+c+" years")
print(command)

for num in range(1):
    num1 = random.randint(5,20)
d = str(num1)
e = int(d)

ask = int(input("Before "+d+" years ago, the elder one be how many times as old the younger one ? : "))

print("Age of the "+b+" be x")
print("Age of the "+a+" be x + "+c)

sum = ask*e
sum2 = f-e
sum3 = ask-1
sum4 = sum-sum2
sum5 = sum4/sum3
print("x = ",sum5)
x = str(sum5)
y = str(sum5+16)

command1 = ("Hence, "+b+"'s age is "+x+" and "+a+"'s age is "+y)