# A number is only divisible by 9 when its sum is divisible
num=int(input("Enter a Number :"))
x=[int(a) for a in str(num)]
print(x)
s=sum(x)
print("Sum is", s)
if (s % 9 ==0):
    print("Is divisible by 9")
else:
    print("Is not divisible by 9")