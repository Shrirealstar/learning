n = input("enter a binary number : ")
decimal = 0
power = 0
n = n[::-1]
for i in n:
    decimal = decimal + int(i)*2**power
    power = power + 1
print(decimal)