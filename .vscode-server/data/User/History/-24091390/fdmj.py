def is_divisible_by_2(number):
    last_digit = number % 2
    if last_digit in {0, 2, 4, 6, 8}:
        return True
    else:
        return False
    
n = int(input("Enter a number :"))

if is_divisible_by_2(n):
    print(f"{n} is divisible by 2.")
else:
    print(f"{n} is not divisible by 2.")
