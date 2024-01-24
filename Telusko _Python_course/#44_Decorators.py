#decorators we can swap the numbers from a main function without touching it.

#Simple divisiton
def div(a,b):
    print(a/b)

div(2,4)

#swap the nimbers
def div(a,b):
    if a<b:
        a,b = b,a
    print(a/b)

div(2,4)

#Swap the numbers by using of decorators
def div(a,b):
    print(a/b)

def main_div(func):

    def div1(a,b):    
        if a<b:
            a,b = b,a
        return func(a,b)
    
    return div1
div = main_div(div)
div(2,4)