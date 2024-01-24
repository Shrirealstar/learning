#In variable there are 2 types of variables 
    #1. Instance variable
    #2. Class Variable

class car:

    whleel = 5
    def __init__(self):
        self.mil = 10
        self.com = "BMW"
    
C1 = car()
C2 = car()

C1.com = "Benz !!"

C2.whleel = 6

print(C1.mil, C2.com, C2.whleel)
print(C2.mil, C1.com)