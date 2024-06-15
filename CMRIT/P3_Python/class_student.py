class student:
    def __init__(self, m1, m2, m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3
    def percentage(self):
        sum = (self.marks1 + self.marks2 + self.marks3/150) * 100
        return sum
    def SGPA(self):
        sum = (self.marks1 + self.marks2 + self.marks3/150) * 100
        sem1 = (sum / 10) + 0.75
        return sem1

m1 = int(input("Enter the M1 marks : "))
m2 = int(input("Enter the M2 marks : "))
m3 = int(input("Enter the M3 marks : "))
x = student(m1, m2, m3)
print(x.percentage())
print(x.SGPA())
    