import math
n = int(input("Enter a number :"))
n1 = math.sqrt(n)
n2 = int(n1)
n3 = n2 * n2
if n3 == n:
    print("Perfect Square")
else :
    print("Not a perfect square")