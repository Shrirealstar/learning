n = input("Enter string to check heterogram : ")
if len(n) == len(set(n)):
    print("Heterogram")
else:
    print("Not Heterogram")
