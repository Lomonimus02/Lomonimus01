def appeal(nums):
    for i in range(len(nums)):
        nums[i] = nums[len(nums)-i]
    return nums
''' эта программа производит обращение списка'''