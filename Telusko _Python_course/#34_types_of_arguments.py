#positioning the values
def sum (a,g):
    x = a + g
    print(x)
sum(5,7)

#Default
def sum (x,y = 15):
    print(x, y)
sum(6,60)

#Variable length
def sum(c, *v):
    a = c
    b = v
    
    for i in b:
        a = a + i
    print(a)

sum(5,6,7,5,3,45)
