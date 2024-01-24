def sort(nums):
    for i in range (5):
        min = i
        for j in range(i,8):
            if nums[j] < nums[min]:
                min = j

        temp = nums[i]
        nums[i] = nums[min]
        nums[min] = temp

nums = [3,5,8,9,1,4,7,2]
sort(nums)
print(nums)