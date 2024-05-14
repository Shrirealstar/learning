a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a > b and a > c:
    print(a, "is the largest number")
elif b > a and b > c:
    print(b, "is the largest number")
elif a == b == c:
    print("All are equal")
else :
    print(c, "is the largest number")
