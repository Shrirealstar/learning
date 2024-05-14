a = float(input("Enter the first side : "))
b = float(input("Enter the second side : "))
c = float(input("Enter the third side : "))

if a == b == c :
    print("Equilateral Triangle")
elif a == b or b == c or c == a :
    print("Isosceles Triangle")
else :
    print("Scalene Triangle")
    