import math
P=int(input("Enter Tenzile Stress load : "))
d=int(input("Enter dia : "))

A=math.pi/4*d**2
Pu=P*10**3/A
print('Area is',A)
print('Tenzile  Stress is : ',Pu)