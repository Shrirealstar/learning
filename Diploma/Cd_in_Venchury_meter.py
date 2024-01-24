from cmath import pi, sqrt

d1=float(input("Enter dia at entry of Ventury Meter :"))
d2=float(input("Enter dia at exit of Ventury Meter :"))
h1=int(input("Enter value of h1 of Marcury :"))
h2=int(input("Enter value of h2 of Marcury :"))
H1=h2-h1
H2=H1/1000
print('h1~h2 in m m is :', H1)
print('h1~h2 in m is :', H2)
h=float(12.6*H2)
print('Head of water in m :', h)
l1=int(input("Enter the lenght of tank in mm :"))
l2=l1/1000
print('L in m is :', l2)
b1=int(input("Enter the breath of tank in mm :"))
b2=b1/1000
print('B in m is :', b2)
A=l2*b2
print("Area of tank is :",A)
r=int(input("Enter the value of rise of water in tank in cm :"))
r2=r/100
print("Rise of water in m m :",r2)
t=int(input("Enter time is sec :"))
a1=pi/4*d1**2
print("a1 value is :",a1)
a2=pi/4*d2**2
print("a2 value is :",a2)

# Actual Discharge
AD=(A*r2)/t
print("Actual Discharge is :",AD)

# Thearitical Value
TV=(a1*a2)
TV1=sqrt(a1**2-a2**2)
TV3=TV/TV1
TV4=sqrt(2*9.81*h)
TD=TV3*TV4
print("Thearitical Value is :",TD)

# Coefficent of Discharge
CD=(AD/TD)
print("Coefficient Discharge is :",CD)



