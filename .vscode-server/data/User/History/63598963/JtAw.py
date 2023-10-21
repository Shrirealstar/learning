class A():
    def __init__(self):
        print("It's A")
    
    def feature1():
        print("Feature 1")

class B(A):
    def __init__(self):
        super.__init__()
        print("It's B")

    def feature2():
        print("Feature 2")    

class C(B,A):
    def feature3():
        print("Feature 3")

a1 = B()
