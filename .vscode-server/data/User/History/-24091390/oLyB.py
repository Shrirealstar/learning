n = int(input("Enter a number : "))
def is_divisible():
    unit_digit = n % 10
    if unit_digit in {0, 2, 4, 6, 8}:
        print("divisible")
    else :
        print("No")