
n = int(input("Enter a number to get factorial's of it : "))     
      
if n < 0:
    print("INVALID NUMBER !!!")

else:

    def fact(n):

        f = 1

        for i in range (1, n+1):
            f = f*i
        return(f)
    result = fact(n)
    print(result)


