class main:

    def execute(self):
        print("Run")
        print("Debug")


class my_editor():
    print("Run")
    print("Debug")
    print("Simplify")
    print("Suggestions")

class laptop:

    def code (self,ide):
        ide.execute()

ide = main()

lap1 = laptop()
lap1.code(my_editor)