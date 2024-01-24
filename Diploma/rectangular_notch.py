from cmath import sqrt


l=float(input("Enter leanth of the tank :"))
l1=l/1000
b=float(input("Enter width of the tank :"))
b1=b/1000
A=l1*b1
print('Area of the tank is :',A)

w=float(input("Enter the width of rectangular notch :"))
w1=w/1000
Ho=float(input("Enter the level of water in the tank :"))
Ho1=Ho/1000
MSD1=float(input("Enter the value of 1 MSD :"))
VSD1=float(input("Enter the total number of VSD :"))
LC=MSD1/VSD1
print('Least common :',LC)
MSD=float(input("Enter the given MSD value :"))
VSD=float(input("Enter the given VSD vlaue :"))
TH=MSD+(VSD*LC)
TH1=TH/1000
print('Total Reading of H1:',TH1)

H=TH1-Ho1
print("Head of water flowes over the notch :",H)

T=int(input("Enter the time taken for rise of water for 10cm :"))
AD=A*LC/T
print("Actual Discharge is :",AD)


