class A():
    def show():
        print("It's A")

class B():
    pass
    def show():
        print("It's B")


a = B
a.show()