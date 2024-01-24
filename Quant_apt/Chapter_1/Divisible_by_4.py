n = input("Enter a number: ")

number = int(n[-2:])
sum = number % 10 + number // 10

if sum % 4 == 0:
    print('The number is Divisible by 4')

else:
    print("The number is not Divisible by 4")