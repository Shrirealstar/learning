user_input = int(input("Enter a number: "))

def factors(n):
  for i in range(1, n + 1):
    if n % i == 0:
        return i

factors(user_input)

def squre(n):
   return n * n

small_fact = factors(user_input)

if user_input % small_fact == 0 and small_fact ** 2 >= user_input:
  print(small_fact)