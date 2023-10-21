import time
ask = float(input("Is the sum is based on solid shaft (y/n) : "))
if ask == "y":
    n = int(input("Speed : "))
P = int(input("Power : "))
Ss = int(input("Shear Stress : "))
#covert the MPa to N/mm2
time.sleep(1)
a = 10**6*(Ss)/1000**2
print("Shear Stress :",a,'N/mm2')
