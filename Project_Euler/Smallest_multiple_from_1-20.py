# Smallest Multiple from 1-20
from math import gcd
def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    return a*b//gcd(a,b)

from functools import reduce

result = reduce(lcm, range(1,21))
print(result)