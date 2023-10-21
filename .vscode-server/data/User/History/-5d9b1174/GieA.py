# Define a class named Lapotp
class Laptop:
    def __init__(self, brand, CPU, RAM):
        # Assign values to the attributes
        self.brand = brand
        self.cpu = CPU
        self.ram = RAM
        self.licence = self.licence
        self.office = self.office

    class windows :
        def __init__(self):
            self.licence = 'licensed windoes'
            self.office = 'office has licence'


lap1 = Laptop('Hp','i6',8)
lap2 = Laptop('Lenovo','i8',12)
config1 = Laptop.windows('licensed windoes','office has licence')
config2 = Laptop.windows('licensed windoes','office has licence')

print(lap1.brand, lap1.cpu, lap1.ram) 
print(config1.licence, config1.office)
print(lap2.brand, lap2.cpu, lap2.ram)
print(config1.licence, config2.office)