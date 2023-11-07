# Divisiblity of 8
num=int(input("Enter a Number :"))
x=[int(a) for a in str(num)]
print(x)
s = str(x[-3])+str(x[-2])+str(x[-1])
print("Number formed by last three digits is", s)
if (int(s) % 8 ==0):
    print("Is divisible by 8")
else:
    print("Is not divisible by 8")