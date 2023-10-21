class main:

    def execute(self):
        print("Run")
        print("Debug")


class laptop:

    def code(self,ide):
        ide.execute()

ide = main()

lap1 = laptop()
lap1.code()