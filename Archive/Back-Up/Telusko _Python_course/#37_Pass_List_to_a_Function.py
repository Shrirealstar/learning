def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd       

lst = [2,4,534,343,6,2,3,6,78,23,42,675,67,56]

even, odd = count(lst)

print("Even : {} and Odd {}".format(even, odd))
print('Even :',even)
print('Odd :',odd)


