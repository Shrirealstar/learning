import re
n=input("Enter your mail ID : ")
if(re.findall(r'[A-Z a-z 0-9]@gmail.com',n)):
    print("Valid ID")
else :
    print("NIL")