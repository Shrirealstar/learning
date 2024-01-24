nums = [23,11,24, 2, 4,67]
for num in nums :
    if num % 5 == 0:
        print(num)
        break
else :
    print("Number not found")