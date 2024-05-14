x = input("Enter 1 string to check anagram : ")
y = input("Enter 2 string to check anagram : ")

a = sorted(x)
b = sorted(y)
if a == b:
    print("Anagram")
else:
    print("Not Anagram")


