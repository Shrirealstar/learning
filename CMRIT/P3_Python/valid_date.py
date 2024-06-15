import re
n = input("Enter a date : ")
if(re.findall(r'\d\d\d\d-\d\d-\d\d',n)):
    print("Valid date")
else:
    print("Invalid date")