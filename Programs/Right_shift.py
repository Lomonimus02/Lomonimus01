nums = [1, 2, 3, 4, 5, 6]
def r_shift(nums):
    i = 0
    b = nums[len(nums) - 1]
    for i in range(len(nums) - 2, -1, -1):
        nums[i + 1] = nums[i]
        nums[0] = b
    return nums
'''эта программа смещает список вправо'''
print(r_shift(1,2,3,4,5,6))