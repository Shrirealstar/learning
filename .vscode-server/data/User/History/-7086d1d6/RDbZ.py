import math # to use the math.sqrt function

def is_prime(number):
    # check if the number is less than 2
    if number < 2:
        return False
    # check if the number is 2
    if number == 2:
        return True
    # check if the number is even
    if number % 2 == 0:
        return False
    # check for divisors from 3 to the square root of the number
    for divisor in range(3, int(math.sqrt(number)) + 1, 2):
        if number % divisor == 0:
            return False
    # if no divisor is found, the number is prime
    return True

def find_primes(limit):
    # create an empty list to store the prime numbers
    primes = []
    # loop through all the numbers from 2 to the limit
    for number in range(2, limit + 1):
        # check if the number is prime using the previous function
        if is_prime(number):
            # add it to the list of primes
            primes.append(number)
    # return the list of primes
    return primes

# ask the user for a number
number = input("Enter a positive integer: ")
# try to convert it to an integer
try:
    number = int(number)
    # check if it is positive
    if number > 0:
        # find and print the list of primes using the previous function
        primes = find_primes(number)
        print("The prime numbers less than or equal to", number, "are:")
        print(primes)
    else:
        # print an error message if it is not positive
        print("Please enter a positive integer.")
except ValueError:
    # print an error message if it is not an integer
    print("Please enter a valid integer.")
