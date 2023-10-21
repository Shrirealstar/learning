#User Input
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
d2 = (M**2+T**2)**1/2
print(d2)

