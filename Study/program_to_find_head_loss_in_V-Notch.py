from cmath import sqrt
import math
cd=float(input("Enter cd value :"))
H=float(input("Enter H value :"))
c=float(input("Enter Tan value :"))
b=math.tan(c)
H1=2.5
Q=8/15*cd*sqrt(2)*sqrt(9.81)*b/2*H**H1

print(Q)