class Laptop:
  def __init__(self, brand, CPU, RAM):
    # Assign values to the attributes
    self.brand = brand
    self.cpu = CPU
    self.ram = RAM
    self.licence = None
    self.office = None

  class Windows:
    def __init__(self):
      self.licence = 'licensed windows'
      self.office = 'office has licence'

lap1 = Laptop('Hp', 'i6', 8)
lap2 = Laptop('Lenovo', 'i8', 12)

# Create a Windows configuration object
windows_config = Laptop.Windows()

# Set the licence and office attributes of the laptops to the Windows configuration object
lap1.licence = windows_config.licence
lap1.office = windows_config.office
lap2.licence = windows_config.licence
lap2.office = windows_config.office

print(lap1.brand, lap1.cpu, lap1.ram)
print(lap1.licence, lap1.office)
print(lap2.brand, lap2.cpu, lap2.ram)
print(lap2.licence, lap2.office)