n = int(input("Enter the real number: "))

numbers = list(range(1, n + 1))

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
