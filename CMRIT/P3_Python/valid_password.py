import re
n=input("Enter password : ")
if(re.findall(r'[A-Z a-z 0-9]',n)):
    print("Valid password")
else :
    print("NIL")

lower_count = sum(1 for char in n if char.islower())
upper_count = sum(1 for char in n if char.isupper())
digit_count = sum(1 for char in n if char.isdigit())

print(f"Lowercase letters: {lower_count}")
print(f"Uppercase letters: {upper_count}")
print(f"Digits: {digit_count}")