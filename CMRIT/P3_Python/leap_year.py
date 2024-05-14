x = int(input("Enter a year : "))
if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap = True
else:s
    is_leap = False
print(is_leap)

