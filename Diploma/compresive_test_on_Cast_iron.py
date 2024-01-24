from cmath import pi

d=float(input("Enter the dia of the job :"))
L=float(input("Enter the length of the job :"))
pb=float(input("Enter the max load of the job :"))
pl=float(input("Enter the proof load of the job :"))
sl1=float(input("Enter the slop 1 of the job :"))
sl2=float(input("Enter the slop 2 of the job :"))
sl3=float(input("Enter the slop 3 of the job :"))
LC=float(input("Enter the Least comman of the job :"))

A=pi*(d*d)/4
print('Area of the job is :',A)

I=pi*(d*d*d*d)/64
print('Module Inertia is :', I)

pls=pl/A*1000
print('Proof load is :', pls)

cs=pb/A*1000
print('Compressive Stress is :', cs)

sl=sl1*(1/LC)*(L/A)
print('Secent Stress is :', sl)

T=sl2*(1/LC)*(L/A)
print('tangent Value is :', T)

E=sl3*(1/LC)*(L/A)
print('Modulus of Elasticity is :', E)


