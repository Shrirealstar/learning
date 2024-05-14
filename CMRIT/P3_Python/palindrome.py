n1 = input("Enter a number to check palindrome: ")
# Reverse the input number
n2 = n1[::-1]
# Check if the original number is equal to its reverse
if n1 == n2:
    print("True")
else:
    print("False")
