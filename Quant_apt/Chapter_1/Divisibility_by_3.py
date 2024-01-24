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
