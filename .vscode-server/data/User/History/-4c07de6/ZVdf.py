import time

LI = int(input("Enter labour input : "))
MI = int(input("Enter Material Input : "))
CI = int(input("Enter Capital input : "))
EI = int(input("Enter energy input : "))
OM = int(input("Enter MISC input : "))
output = LI+MI+CI+EI+OM+500

print("Partial Productivity Measures are ")

LP = output/LI
LPF = format(LP,".2f")
print("Labour productivity is : ",LPF)
time.sleep(1)

MP = output/MI
MPF = format(MP,"2.f")
print("Material productivity is : ",MPF)
time.sleep(1)

CP = output/CI
CPF = format(CP,"2.f")
print("Capital productivity is : ",CPF)
time.sleep(1)

EP = output/CI
EPF = format(EP,"2.f")
print("Energy productivity is : ",EPF)
time.sleep(1)

OP = output/CI
OMF = format(OP,"2.f")
print("Capital productivity is : ",OMF)
time.sleep(1)