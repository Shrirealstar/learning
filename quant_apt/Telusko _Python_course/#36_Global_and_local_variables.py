#Ex:1
a = 10 # Global Variable

def sum ():
    a = 9 # Local variable
    print(a)
sum()
print(a)

#Ex:2 = changing a global variable value in local variable
x = 2

def sum2():

    global x
    x = 24
    print(x)
sum2()

#Ex:3 = changing the value of global variable in the local variable using function
x = 10
def func():
    x = 15
    print("local x: ",x)
    y = globals()['x']
    print("global x: ",y)
globals()['x'] = 20
func()