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
d2 = M*M
d3 = T*T
d4 = d2+d3
d5 = d4**(1/2)
d6 = d5*d
d7 = d6**(1/3)
print("The diameter of the shaft according to Maximau Shear Stress :",d7*10)

d = (16)/(3.14*WTS)
d2 = M*M
d3 = T*T
d4 = d2+d3
d5 = d4**(1/2)
d6 = d5*d+M
d7 = d6**(1/3)
print(d7)