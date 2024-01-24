#Arraies in python are flexible 
#We need to have variables in a same type
#In array we can expand adn shrink the list
#1st we need to specify "type and value"

from array import *


#Con1
a = array ("i", [3,434,34,343,4,34])
print(a)

#Con2
b = array ("i", [3,434,34,343,4,34])
print(b.buffer_info())

#Con3
c = array ("i", [3,434,34,343,4,34])
print(c.typecode)


#Con4
vals = array ("i", [3,434,34,343,4,34])

for i in range (5):
    print(vals[i])
arr = array ("i", [1,2,3,4,5,6])

new_arr = array(arr.typecode, (a*a for a in arr))

for e in new_arr:
    print(e)    
