from cmath import pi
import time
ask = input("Is the sum is based on solid shaft (y/n) : ")
if ask == "y":
    n = int(input("Speed : "))
    P = int(input("Power : "))
    Ss = int(input("Shear Stress : "))
#covert the MPa to N/mm2
    time.sleep(1)
    a = 10**6*(Ss)/1000**2
    print("Shear Stress :",a,'N/mm2')
    Tmean = 9.55*10**6*P/(n)
    print("Tmean : ",Tmean)
#Diameter of the Shaft
    sum = 16*Tmean/(pi*Ss)
    print(sum)
else :
    ask = input("Is the sum is based on hollow shaft (y/n): ")
    if ask == "y":
        n = int(input("Speed : "))
        P = int(input("Power : "))
        Ss = int(input("Shear Stress : "))
        FOS = int(input("Factor of days : "))
        K = int(input("Ratio of the di/dy : "))
    else :
        print("Invalid Input!!!, Re-Run the program...")


