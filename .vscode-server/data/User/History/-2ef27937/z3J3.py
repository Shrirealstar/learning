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

d = (16)/(3.14*WTS)
print(d)
d2 = (M**2+T**2)
print(math.sqrt(d2)) 
