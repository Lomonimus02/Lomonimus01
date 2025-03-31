def l_shift(nums):
    b = nums[0]
    i = 0
    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]
    b = [len(nums) - 1]
    return nums
'''эта программа сдвигает список влево'''
print(l_shift(1,2,3,4,5,6))