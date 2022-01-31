import math
P=int(input("Enter Yield Stress load : "))
d=int(input("Enter dia : "))

A=math.pi/4*d**2
Py=P*10**3/A
print('Area is',A)
print('Yield Stress is : ',Py)
