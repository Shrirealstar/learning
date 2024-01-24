def is_prime(n):
  """Returns True if n is a prime number, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


def print_primes(n):
  """Prints the list of prime numbers up to n, inclusive."""
  for i in range(2, n + 1):
    if is_prime(i):
      print(i)


# Get user input
user_input = int(input("Enter a number: "))

# Print the list of prime numbers up to the user input
print_primes(user_input)