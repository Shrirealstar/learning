n = input("Enter a string :")
Upper_case = 0
Lower_case = 0
for i in n:
    if i.isupper():
        Upper_case += 1
    elif i.islower():
        Lower_case += 1
print("No. of Upper case : ", Upper_case)
print("No. of Lower case : ", Lower_case)