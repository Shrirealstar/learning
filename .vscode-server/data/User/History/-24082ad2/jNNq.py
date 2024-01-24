n = input("Enter a number: ")

number = int(n[-2:])
sum = number % 10 + number // 10

print(sum)