
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
#Angular Twist/finding dia
    sum = 584*Tmean*L/(G1*A)
    sum2 = sum**(1/4)
    print(sum2)
else :
    ask = input("Is the sum is based on hallow Only ? (y/n) : ")
#Inputs
    p = int(input("Power : "))
    n = int(input("Speed : "))
    L = int(input("Leanght : "))
    G = int(input("Modulas of regidity : "))
    G1 = G*10**3
    print("Modulus of Regidity in N/mm2 :",G1 )
    do = int(input("Outter dia : "))
    di = int(input("Inner Dia : "))
#Finding the Torque
    Tmean = 9.55*10**6*p/(n)
    print("Tmean :",Tmean)
#Finding dia
    sum = 584*Tmean*L/(G1*(do**4-di**4))
    print("dia :",sum)

if ask == "n":
    ask = ("Is the sum is based on hallow subjected to Torsion (y/n) :")
#Inputs
    k = ("Ratio of Od/Id :")
if k == 0:
    k = 6;
else :
    k = k

    p = ("Power :")
    n = ("Speed :")
    Ss = ("Shear Stress :")
#Finding the Torque
    Tmean = 9.55*10**6*p/(n)
    print("Tmean :",Tmean)

#Finding the diameter

    16*Tmean/(3.14*Tmean*Ss)
    




if ask == "n":
    print("Invalid Input !!!, Re-Run the program...")




