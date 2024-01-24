# Divisiblity of 5
num=int(input("Enter a Number :"))
x=[int(a) for a in str(num)]
s = str(x[-1])
print("Unit Place number is" , s)
if (int(s) % 5 ==0):
    print("Is divisible by 5")
else:
    print("Is not divisible by 5")