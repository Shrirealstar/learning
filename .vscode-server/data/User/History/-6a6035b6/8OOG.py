
ask = input("Is the sum is based on solid shaft ? (y/n) : ")
if ask == "y":
#Inputs
    p = int(input("Power : "))
    n = int(input("Speed : "))
    G = int(input("Modulus of Regidity : "))
    G1 = G*10**3
    print("Modulus of Regidity in N/mm2 :",G1 )
    A = float(input("The angular : "))
    L = int(input("Leanght : "))
#Finding the Torque
    Tmean = 9.55*10**6*p/(n)
    print("Tmean :",Tmean )
#Angular Twist
    sum = 584*Tmean*L/(G1*A)
    sum2 = sum**(1/4)
    print(sum2)
else :
    ask = input("Is the sum is based on hallow ? (y/n) : ")
if ask == "n":
    print("Invalid Input !!!, Re-Run the program...")

