import math
n = int(input("Enter the value of n :"))
r = int(input("Enter the value of r :"))

npr = math.factorial(n)/(math.factorial(n-r))

ncr = npr/(math.factorial(r))

print(npr)
print(ncr)

