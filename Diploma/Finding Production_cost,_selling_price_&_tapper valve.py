#Given
from cmath import pi
from curses.ascii import SP
from re import L


d=float(input("Enter the dia of the job :"))
L=float(input("Enter the length of the job :"))
ms=float(input("What will be the material cost per kg? :"))
lC=float(input("What will be the labour cost per hour? :"))

v=pi/4*(d*d)*L
print('Volume of the job is :',v)

w1=7.8*v/1000
print('weight of the job is :',w1)

CM=ms*w1
print('total material cost is:',CM)

LE=30/100*lC
print("The labour expences is :",LE)

TC=CM+lC+LE
print('Total cost is, rupees',TC)

SP=TC+(0.01*TC)
print('selling price of the job is :',SP)

UI=input("Do you want to print Tapper angle? ; Yes or No : ")

if(UI=='Yes'):
    d=float(input("Enter the smaller dia of the job :"))
    D=float(input("Enter the Bigger dia of the job :"))
    l=float(input("Enter the Bigger dia of the job :"))
    TA=D-d/(2*l)
    print(TA)
elif (UI=='NO'):
    print("Thanks")


