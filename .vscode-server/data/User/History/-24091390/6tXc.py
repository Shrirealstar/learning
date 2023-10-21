def is_divisible_by_2(number):
    # Check if the last digit of the number is in the set {0, 2, 4, 6, 8}
    last_digit = number % 10
    if last_digit in {0, 2, 4, 6, 8}:
        return True
    else:
        return False

# Test the function with examples:
number1 = int(input("Enter a number :"))

if is_divisible_by_2(number1):
    print(f"{number1} is divisible by 2.")
else:
    print(f"{number1} is not divisible by 2.")
