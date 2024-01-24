#Example 1


def person(name, **data):
    
    print(name)
    print(data)

person('Shri', age = 22, city = 'Bangalore', phone = 886711)



#Example 2

def person(name, **data):
    
    print(name)
    
    for i,j in data.items():
        print(i,j)
 
person('Shri', age = 22, city = 'Bangalore', phone = 886711)