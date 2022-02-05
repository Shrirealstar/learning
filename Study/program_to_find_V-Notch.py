from cmath import sqrt

cd=float(input("Enter a cd value :"))
l=float(input("Enter L value :"))
H=float(input("Enter H value :"))
a=3/2
import math
Q=2/3*cd*l*math.sqrt(2)*math.sqrt(9.81)*H**a

print(Q)