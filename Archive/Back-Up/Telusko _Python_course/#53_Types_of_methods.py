class student:

    school = 'Halli'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2 
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    @staticmethod
    def info():
        print("This is a static variable...")

s1 = student(34,34,34)
s2 = student(34,45,34)

print(s2.avg())
print(s1.school)
student.info()