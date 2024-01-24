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
LP.F = format(LP,".2f")
print("Labour Productivity is ", LP.F)
time.sleep(1)

MP = TO/b
MP.F = format(MP,".2f")
print("Material Productivity is ", MP.F)
time.sleep(1)

CP = TO/c
CP.F = format(LP,".2f")
print("Capital Productivity is ", CP.F)
time.sleep(1)

EP = TO/d
EP.F = format(LP,".2f")
print("Energy Productivity is ", EP.F)
time.sleep(1)

OP = TO/e
OP.F = format(LP,".2f")
print("Other Productivity is ", OP.F)
time.sleep(1)

#Total productivity
TP = TO/TO
print("Total Productivity is ",TP)





