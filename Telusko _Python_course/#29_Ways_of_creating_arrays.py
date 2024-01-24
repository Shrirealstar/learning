
# Ways of creating arrays

from numpy import *

arr = array ([12,2,3,4,4,3])
print(arr) # Printing a array


print(arr.dtype) # it will show the type of data used in the array

arr1 = array ([12,2,3,4,4,3], float)

print(arr1) # converting the int array to the float type

arr = linspace(1,2,4) # findin the linspace of an array
print(arr)

arr = arange(1,2,4) # Finding the range of an array
print(arr)

arr = logspace(1,2,4) # Finding the logspace of an array
print('% 2f' %arr[3])# the decimal points should be 2
print(arr)


arr = ones(5) # printing ones from array
print(arr)

arr = zeros(1) # printing zero's from array
print(arr)