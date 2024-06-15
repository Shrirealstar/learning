class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def diagonal(self):
        l_dia = (self.length**2 + self.breadth**2)**0.5
        return l_dia

    def area(self):
        a = self.length * self.breadth
        return a

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
x = Rectangle(l, b)
print("Diagonal:", x.diagonal())
print("Area:", x.area())
