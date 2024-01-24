class A():
    def __init__(self):
        print("It's A")
    
    def feature1():
        print("Feature 1")

class B(A):
    def __init__(self):
        print("It's B")

    def feature2():
        print("Feature 2")    

class C(A and B):
    def __init__(self):
        print("It's C")

a1 = C()