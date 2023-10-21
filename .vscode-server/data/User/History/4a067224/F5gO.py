import time

#User inpur
a = int(input("Enter the labour input charges : "))
b = int(input("Enter the material input cost : "))
c = int(input("Enter the capital input price : "))
d = int(input("Enter the Energy input cost : "))
e = int(input("Enter the other expenses : "))
TO = a+b+c+d+e
print("Total Output is = ", TO)

#logic for partial productivity for individual inputs

LP = TO/a
print("Labour Productivity is ", LP)
time.sleep(1)

MP = TO/b
print("Material Productivity is ", MP)
time.sleep(1)

CP = TO/c
print("Capital Productivity is ", CP)
time.sleep(1)

EP = TO/d
print("Energy Productivity is ", EP)
time.sleep(1)

OP = TO/e
print("Other Productivity is ", OP)
time.sleep(1)

#Total productivity
TP = TO/TO
print("Total Productivity is ",TP)
time.sleep(1)





