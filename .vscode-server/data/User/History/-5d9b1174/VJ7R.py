# Define a class named Lapotp
class Laptop:
    def __init__(self, brand, CPU, RAM):
        # Assign values to the attributes
        self.brand = brand
        self.cpu = CPU
        self.ram = RAM


lap1 = Laptop ('Hp', 'i6', 8)
lap2 = Laptop ('Lenovo', 'i8', 12)

print(lap1)
print(lap2)