n=int(input("Enter a number to find the place value of it:"))
x,y=0,0
while n>0:
    y=n%10
    y*=(10**x)
    n=n//10
    print(y)
    x+=1