n = int(input("Enter how may fibonacci number's want to print : "))

def  fib(n):
    a = 0
    b = 1

    if n ==1:
        print(a)

    if n <= 0:
        print("INVALID NUMBER !!! ")

    else :

        print(a)
        print(b)
        for i in range(2,n):
            
            c = a + b
            a = b
            b = c
            print(c)
fib(n)