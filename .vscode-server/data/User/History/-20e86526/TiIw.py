def is_divisible_by_2(number):
    return number % 2 == 0

def is_divisible_by_3(number):
    return sum(int(digit) for digit in str(number)) % 3 == 0

def is_divisible_by_4(number):
    last_two_digits = int(str(number)[-2:])
    return last_two_digits % 4 == 0

def is_divisible_by_5(number):
    return number % 10 == 0 or number % 10 == 5

def is_divisible_by_8(number):
    return (number % 1000) % 8 == 0

def is_divisible_by_9(number):
    return sum(int(digit) for digit in str(number)) % 9 == 0

def is_divisible_by_10(number):
    return number % 10 == 0

def is_divisible_by_11(number):
    even_sum, odd_sum = 0, 0
    number_str = str(number)
    for i, digit in enumerate(number_str):
        if i % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return (odd_sum - even_sum) % 11 == 0

n = int(input("Enter a number: "))

ask = int(input(" 1.Divisibility by 2\n " "2.Divisibility by 3\n " "3.Divisibility by 4\n " "4.Divisibility by 5\n " "5.Divisibility by 8\n " "6.Divisibility by 9\n " "7.Divisibility by 10\n " "8.Divisibility by 11\n " "\n" "Choose a test (1-8) to perform : "))


if ask == 1:
    result = is_divisible_by_2(n)
    print(f"{n} is {'divisible' if result else 'not divisible'} by 2.")

elif ask == 2:
    result = is_divisible_by_3(n)
    print(f"{n} is {'divisible' if result else 'not divisible'} by 3.")

elif ask == 3:
    result = is_divisible_by_4(n)
    print(f"{n} is {'divisible' if result else 'not divisible'} by 4.")

elif ask == 4:
    result = is_divisible_by_5(n)
    print(f"{n} is {'divisible' if result else 'not divisible'} by 5.")

elif ask == 5:
    result = is_divisible_by_8(n)
    print(f"{n} is {'divisible' if result else 'not divisible'} by 8.")

elif ask == 6:
    result = is_divisible_by_9(n)
    print(f"{n} is {'divisible' if result else 'not divisible'} by 9.")

elif ask == 7:
    result = is_divisible_by_10(n)
    print(f"{n} is {'divisible' if result else 'not divisible'} by 10.")

elif ask == 8:
    result = is_divisible_by_11(n)
    print(f"{n} is {'divisible' if result else 'not divisible'} by 11.")

else:
    print("Please select a valid test (1-8).")

