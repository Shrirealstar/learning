n = input("Enter a number: ")

number = int(n[-3:])
sum = number % 10 + number // 10
print(sum)