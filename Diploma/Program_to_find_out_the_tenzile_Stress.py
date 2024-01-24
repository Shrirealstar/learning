from cmath import pi

d=float(input("dia of the work piece :"))
l=float(input("length  of the work piece :"))
py=float(input("yield point :"))
pu=float(input("ultimate load point :"))
s=float(input("slop is :"))
fd=float(input("failure dia:"))
fl=float(input("factured length :"))
A=(pi/4)*(d**2)
A2=(pi/4)*(fd**2)

YS=(py/A)*1000
US=(pu/A)*1000
PE=(120-fl)/120*(100)
PR=(A-A2)/A*(100)
E=s*(1/0.01)*(120/A)
print('Yield stress is :',YS)
print('Ultimate tenzile stress is :',US)
print('% Elongation is :',PE)
print('% Reduction is :',PR)
print('Module of Elasticity is :',E)

