# Divisible by 3, only when its sum of ditis is divisible by 3.
num = input("Enter a number:")
x = [int(a) for a in str(num)]
print(x)
s= sum(x)
if s%3==0:
    print(num, "is divisibly by 3")
else:
    print(num, "is not divisibly by 3")