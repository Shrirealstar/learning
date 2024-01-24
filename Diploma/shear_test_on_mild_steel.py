#Trial 1
w=float(input("Enter the width of the work piece 1 :"))
d=float(input("Enter the depth of the work piece 1 :"))
l=float(input("Enter the failure load of the of the work piece 1 :"))
A=(w*d)
S=(l*9.81/A)

#Trial 2
w1=float(input("Enter the width of the work piece 2 :"))
d1=float(input("Enter the depth of the work piece 2 :"))
l1=float(input("Enter the failure load of the of the work piece 2:"))
A1=(w1*d1)
S1=(l1*9.81/A1)

#Trial 3
w2=float(input("Enter the width of the work piece 3 :"))
d2=float(input("Enter the depth of the work piece 3 :"))
l2=float(input("Enter the failure load of the of the work piece 3 :"))
A2=(w2*d2)
S2=(l2*9.81/A2)

print("Single shear stress of trial one is",S)
print("Single shear stress of trial two is",S1)
print("Single shear stress of trial three is",S2)
