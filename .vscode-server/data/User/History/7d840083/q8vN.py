num = int(input("Enter a number : "))

if num > 100:
  print("Number is out of range...")
  
else:
  is_prime = True
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
    print("It's a prime number")
  else:
    print("It's not a prime number")