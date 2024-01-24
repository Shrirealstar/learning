F1=int(input("Enter F1 : "))
F2=int(input("Enter F2 : "))
F3=int(input("Enter F3 : "))
F4=int(input("Enter F4 : "))

cos1=int(input("Enter cos1 : "))
cos2=int(input("Enter cos2 : "))
cos3=int(input("Enter cos3 : "))
cos4=int(input("Enter cos4 : "))

import math

n=F1*math.cos(math.radians(cos1))
n1=F2*math.cos(math.radians(cos2))
n2=F3*math.cos(math.radians(cos3))
n3=F4*math.cos(math.radians(cos4))

print('∑H is',n+n1+n2+n3)

F1=int(input("Enter F1 : "))
F2=int(input("Enter F2 : "))
F3=int(input("Enter F3 : "))
F4=int(input("Enter F4 : "))

sin1=int(input("Enter sin1 : "))
sin2=int(input("Enter sin2 : "))
sin3=int(input("Enter sin3 : "))
sin4=int(input("Enter sin4 : "))

n=F1*math.sin(math.radians(sin1))
n1=F2*math.sin(math.radians(sin2))
n2=F3*math.sin(math.radians(sin3))
n3=F4*math.sin(math.radians(sin4))

print('∑V is',n+n1+n2+n3)

a=float(input("Ente a Samation of H value : "))
a1=float(input("Ente a Samation of V value : "))
from math import sqrt
a2=sqrt(a ** 2+a1 ** 2)

print(a2)