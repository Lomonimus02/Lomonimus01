def r_shift(nums):
    for i in range(len(nums), 1, -1):
        nums[i-1] = nums[i]
        nums[len(nums)] = nums[i]
    return nums
print(r_shift(1,2,3,4,5,6,7,8,9))