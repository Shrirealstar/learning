
i = 1

def greet():
    global i
    i+=1
    print("Hello...", i)
    greet()

greet()