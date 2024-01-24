from cmath import pi
from xml.etree.ElementTree import PI


d=float(input("Enter the dia of the job :"))
l=float(input("Enter the length of the job :"))
w=float(input("Enter the weight of the job :"))
Y=float(input("Enter the yield point :"))
s=float(input("Enter the slop value :"))

A=pi/4*(d*d)
print('Area of the job is',A)

I=pi/64*(d*d*d*d)
print('Moment of Inertia of the job is :',I)

M=w*l/6
print('Bending Movement of job is :',M)

S=M*Y/(I)*10
print('Stress is',S)

E=23*(l*l*l)*s*9.81/(1296*I)/10000
print('Modulas of Elasticity is :',E) 