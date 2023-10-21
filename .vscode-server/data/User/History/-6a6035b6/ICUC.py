
ask = input("Is the sum is based on solid shaft ? (y/n) : ")
if ask == "y":
#Inputs
    p = int(input("Power : "))
    n = int(input(" Speed : "))
    G = int(input("Modulus of Regidity : "))
    A = int(input("The angular : "))
    L = int(input("Leanght : "))
#Finding the Torque
    Tmean = 9.55*10*6*p/(n)
    print("Tmean :",Tmean )

else :
    ask = "Is the sum is based on hallow ? (y/n) : "



if ask == "n":
    print("Invalid Input !!!, Re-Run the program...")

