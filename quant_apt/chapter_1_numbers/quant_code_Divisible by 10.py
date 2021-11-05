# Divisiblity of 10
num=int(input("Enter a Number :"))
x=[int(a) for a in str(num)]
s = str(x[-1])
print("Unit Place number is" , s)
if (int(s) % 10 ==0):
    print("Is divisible by 10")
else:
    print("Is not divisible by 10")