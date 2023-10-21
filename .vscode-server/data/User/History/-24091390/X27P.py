def is_divi(number):
  unit_digit = number % 10
  return unit_digit in (0, 2, 4, 6, 8)


print(is_divi(10))  # True
print(is_divi(11))  # False
