def topten():

        n = 1

        while n <= 10:
              sq = n*n
              yield sq
              n+= 1 

n = topten()


for i in n: 
    print(i)