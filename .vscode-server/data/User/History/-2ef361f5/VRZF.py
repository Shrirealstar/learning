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
#Diameter of the Solid Shaft
    sum = 16*Tmean/(3.14*Ss)
    d = sum**(1/3)
    print(d)
else :
    ask = input("Is the sum is based on hollow shaft (y/n): ")
if ask == "y":
        n = int(input("Speed : "))
        P = int(input("Power : "))
        USs = int(input("Ultimate Shear Stress : "))
        FOS = int(input("Factor of Safety : "))
        K = float(input("Ratio of the di/dy : "))
#Tmean of the hallow shaft
        Tmean = 9.55*10**6*P/(n)
        print("Tmean : ",Tmean)
#Shear Stress
        Ss = USs/FOS
        print("Shear Stress :",Ss)
#Diameter of hallow shaft
        sum = 16*Tmean/(3.14*Ss)
        sum1 = [1/(1-K**4)]
        sum2 = sum*sum1
        d = sum2**(1/3)
        print(d)
else :
    print("Invalid Input!!!, Re-Run the program...")


