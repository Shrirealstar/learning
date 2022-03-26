#Given
from cmath import pi
from re import L


d=float(input("Enter the dia of the job :"))
l=float(input("Enter the length of the job :"))
ms=float(input("What will be the material cost per kg? :"))
lC=float(input("What will be the labour cost per hour? :"))
v=pi/4*(d*d)*l
print('Volume of the job is :',v)

w1=7.8*v/1000
print('weight of the job is :',w1)

CM=ms*w1
print('total material cost is:',CM)

LE=30/100*lC
print("The labour expences is :",LE)

TC=CM+lC+LE
print('Total cost is :',TC)