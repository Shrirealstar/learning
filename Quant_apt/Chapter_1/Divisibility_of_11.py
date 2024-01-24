
number = int(input("Enter a number: "))

def digit_odd_and_even(number):
    number_str = str(number)
    even_sum = 0
    odd_sum = 0

    for i in range(len(number_str)):
        digit = int(number_str[i])

        if i % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return even_sum, odd_sum

even_sum, odd_sum = digit_odd_and_even(number)

even = even_sum
odd = odd_sum

div = odd - even

if div % 11 == 0:
    print("Divisible by 11")

else: 
    print('Not Divisible by 11')
