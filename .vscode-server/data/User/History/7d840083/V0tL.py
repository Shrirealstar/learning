user_input = int(input("Enter a number: "))

def factors(n):
  for i in range(1, n + 1):
    if n % i == 0:
        return i

factors(user_input)
print(user_input)

