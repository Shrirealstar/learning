F = int(input("Enter the load fo the shaft :"))
y = int(input("Angle of diflection :"))
C = int(input("Sprint Index :"))
SS = int(input("Shear Stress :"))
G = int(input("Modulus of Regidity :"))
K = 1+1/(2*C)
print(K)
d = 8*F*C*K
print(d)
d2 = 3.14*SS
print(d2)
d3 = (d/d2)**1/2
print(d3)