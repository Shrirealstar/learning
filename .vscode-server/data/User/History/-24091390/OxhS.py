def is_divisible_by_2_by_unit_digit(number):
  """Returns True if the number is divisible by 2 based on the unit digit, False otherwise."""
  unit_digit = number % 10
  return unit_digit in (0, 2, 4, 6, 8)

# Test the function
print(is_divisible_by_2_by_unit_digit(10))  # True
print(is_divisible_by_2_by_unit_digit(11))  # False
