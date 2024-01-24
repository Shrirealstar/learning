n = int(input("Enter a number : "))
def is_divisible(n):
    unit_digit = n % 10
    if unit_digit in {0, 2, 4, 6, 8}:
        return True
    else :
        return False
    
if is_divisible(True):
    print("Divisible")

else :
    print("Not")
