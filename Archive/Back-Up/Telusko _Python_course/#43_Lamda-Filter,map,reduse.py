#The lamda consists of 3 sub-functions like Filter, map and reduse
#1) Filter

#Example 1 : Even filter by funtion

def f(n):
    return n%2==0
nums = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(f,nums))
print(evens, "Evens by using function")

#Example 1.1 : Odd filter by Function
def f(n):
    return n%2
nums = [1,2,3,4,5,6,7,8,9,10]
odds = list(filter(f,nums))
print(odds, "Odds by using function")

#Example 2 - Even filter by funtion
nums = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda n: n%2==0,nums))
print(evens, "Evens by using Lambda")

#Example 2.1 - odd filter by lambda
nums = [1,2,3,4,5,6,7,8,9,10]
odds = list(filter(lambda n: n%2,nums))
print(odds, "Odds by using Lambda")

#2) Map
doubles = list(map(lambda c: c+2,(evens)))
print(doubles)

#3) Reduse
from functools import reduce
add =reduce(lambda v,b : v+b,(doubles))
print(add)