def sum_of_digits_at_even_and_odd_places(number):
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

# Input from the user
number = int(input("Enter a number: "))

even_sum, odd_sum = sum_of_digits_at_even_and_odd_places(number)

print("Sum of digits at even places:", even_sum)
print("Sum of digits at odd places:", odd_sum)
