#User Input
import math 
M = int(input("Bending Movment :"))
T = int(input("Torque :"))
FOS = int(input("Factor Of Safty :"))
UTS = int(input("Ultimate Tensile Stress :"))
USS = int(input("Ultimate Shear Stress :"))

WTS = UTS/FOS
print("Working Tensilw Stress :",WTS)

WSS = USS/FOS
print("Working Shear Stress :",WSS)

d = (16)/(3.14*WSS)
print(d)
d2 = M**2 
d3 = T**2
print(d3)
d4 = d2+d3
d5 = (math.sqrt(d4))
d6 = d5*d
print(d6)
d7 = d6**(1/3)
print(d7)
