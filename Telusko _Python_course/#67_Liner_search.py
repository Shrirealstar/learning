pos = -1

def search(list, n):
    i = 0

    while i< len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1

    return False
    

list = [1,4,8,9,3,2,7,5]
n = 9

if search(list,n):
    print("Found at ",pos+1)

else :
    print("Not Found")    