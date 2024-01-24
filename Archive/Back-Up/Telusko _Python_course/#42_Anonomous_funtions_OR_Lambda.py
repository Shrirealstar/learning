#Finding a square of a number by using a  function
n = int(input("Enter a numner to find squre of it : "))
def squre(n):
    return n*n
result = squre(n)
print(result)

#Finding a squre of a number by using a lambda or Anonomous function

u = int(input("Enter a number to find a squre of it : "))
a = lambda u : u*u
result = squre(u)
print(result)