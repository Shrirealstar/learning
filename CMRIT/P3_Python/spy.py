n = int(input("Enter a int to check whhether a spy num or not : "))
sum = 0
product = 1

for i in str(n):
    product = product * int(i)
    sum = sum + int(i)

if sum == product:
    print("Spy Number")
else :
    print("Not a Spy Number")