ask = float(int(input(" 1.Divisibility by 2\n " "2.Divisibility by 3\n " "3.Divisibility by 4\n " "4.Divisibility by 5\n " "5.Divisibility by 8\n " "5.Divisibility by 9\n " "6.Divisibility by 10\n " "7.Divisibility by 10\n " "8.Divisibility by 11\n " "which test you want to perform ? : ")))

if ask == 1 :
    def is_divisible_by_2(number):
        unit_digit= number % 2
        if unit_digit in {0, 2, 4, 6, 8}:
            return True
        else:
            return False
    
n = int(input("Enter a number :"))

if is_divisible_by_2(n):
    print(f"{n} is divisible by 2.")
else:
    print(f"{n} is not divisible by 2.")