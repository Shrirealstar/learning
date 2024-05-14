import random
n = random.randint(1,20)

for i in range(6):
    x = int(input("Guess a number 1 - 20 : "))
    if x > n:
        print("High")
    elif x < n:
        print("Low")
    else:
        print("Correct")
        break
if x == n:
    print("Good")
elif x != n:
    print("Good Try !!!")
    print("The number is ", n)
