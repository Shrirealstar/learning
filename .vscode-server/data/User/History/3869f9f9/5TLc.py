class A:
    def show():
        print("It's A")

class B(A):
    pass
    def show():
        print("It's B")


a = A
a.show()