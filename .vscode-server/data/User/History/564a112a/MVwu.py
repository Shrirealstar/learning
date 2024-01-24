n = input("Enter a number: ")

number = int(n[-2:])
sum = number % 100 + number // 100

print(sum)