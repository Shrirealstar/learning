import re
n = input("Enter your PAN ID : ")
if(re.findall(r'[A-Z][A-Z][A-Z][A-Z][A-Z]\d\d\d\d[A-Z]',n)):
    print("Valid PAN ID")
else :
    print("NIL")
