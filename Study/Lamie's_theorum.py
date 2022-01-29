import math

T1=int(input("Enter T1 : "))
T2=int(input("Enter T2 : "))
T3=int(input("Enter T3 : "))

sin1=int(input("Enter sin1 : "))
sin2=int(input("Enter sin2 : "))
sin3=int(input("Enter sin3 : "))

n=T3*math.sin(math.radians(sin1))/math.sin(math.radians(sin3))

print('T1 is',n)

n1=T2*math.sin(math.radians(sin1))/math.sin(math.radians(sin3))

print('T1 is',n1)

n2=T1*math.sin(math.radians(sin2))/math.sin(math.radians(sin1))

print('T1 is',n2)
