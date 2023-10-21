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

elif ask == 2 :
    number = int(input("Enter a number: "))

    def sum_of_digits(number):
        num_str = str(number)
    
        digit_sum = 0
    
        for digit in num_str:
            digit_sum += int(digit)
    
        return digit_sum

    result = sum_of_digits(number)

    n = int(result)

    if n % 3 == 0:
        print("The number is Divisible By 3 ")

    else :
        print("The number is not Divisible By 3 ")

elif ask == 3 :
        n = input("Enter a number: ")

        number = int(n[-2:])
        sum = number % 10 + number // 10

        if sum % 4 == 0:
            print('The number is Divisible by 4')

        else:
            print("The number is not Divisible by 4")

elif ask == 4 :
    n = int(input("Enter a number: "))

    sum = n % 10

    if sum == 0:
        print("The number is divisible by 5")

    elif sum == 5:
        print("The number is divisible by 5")

    else:
        print("The number is not divisible by 5")

elif ask == 5:
    n = int(input("Enter a number: "))

    sum = n % 1000

    if sum % 8 == 0:
        print("The number is divisible by 8")

    else:
        print("The number is not divisible by 8")

elif ask == 6:
    number = int(input("Enter a number: "))

    def sum_of_digits(number):
        num_str = str(number)
        
        digit_sum = 0
        
        for digit in num_str:
            digit_sum += int(digit)
        
        return digit_sum

    result = sum_of_digits(number)

    n = int(result)

    if n % 9== 0:
        print("The number is Divisible By 9 ")

    else :
        print("The number is not Divisible By 9 ")

elif ask == 7:
    n = int(input("Enter a number: "))

    sum = n % 10

    if sum == 0:
        print("The number is divisible by 10")

    else:
        print("The number is not divisible by 10")


elif ask == 8:
    pass

else :
