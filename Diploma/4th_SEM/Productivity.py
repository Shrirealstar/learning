Ot=float(input("Enter the total policies has to be completed : "))
E=float(input("How many employees are involved ? : "))
H=float(input("working hours in a day : "))
W=float(input("How many weeks ? : "))
It=(E*H*W)
p=Ot/It
print('Employees =',p)

A=float(input("Units number ? : "))
Sp=float(input("Selling cost of each : "))
Ap=float(input("Actual cost is ? : "))
Mp=float(input("Material cost ? : "))
Oc=float(input("Over head charges : "))

p1=A*Sp/(Ap+Mp+Oc)
print('productivity is :',p1)