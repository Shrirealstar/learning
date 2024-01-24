import time

#User inpur
a = int(input("Enter the labour input charges : "))
b = int(input("Enter the material input cost : "))
c = int(input("Enter the capital input price : "))
d = int(input("Enter the Energy input cost : "))
e = int(input("Enter the other expenses : "))
TO = a+b+c+d+e
print("Total Output is = ", TO)
time.sleep(1)

#logic for partial productivity for individual inputs

LP = TO/a
LPF = format(LP,".2f")
print("Labour Productivity is ", LPF)
time.sleep(1)

MP = TO/b
MPF = format(MP,".2f")
print("Material Productivity is ", MPF)
time.sleep(1)

CP = TO/c
CPF = format(CP,".2f")
print("Capital Productivity is ", CPF)
time.sleep(1)

EP = TO/d
EPF = format(EP,".2f")
print("Energy Productivity is ", EPF)
time.sleep(1)

OP = TO/e
OPF = format(OP,".2f")
print("Other Productivity is ", OPF)
time.sleep(1)

#Total productivity
TP = TO/TO
print("Total Productivity is ",TP)





