n = int(input("Enter a number: "))

sum = n % 1000

if sum < 100:
    sum % 8
    print("Is divisible by 8")

else :
    print("Not")


if sum % 8 == 0:
    print("The number is divisible by 8")

else:
    print("The number is not divisible by 8")

